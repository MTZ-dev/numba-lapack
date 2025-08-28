#!/usr/bin/env python3
# tools/gen_stubs_from_pxd.py
from __future__ import annotations
import sys, re, importlib
from pathlib import Path
from typing import Dict, List, Optional

# -- ensure project root importable
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Import your runtime module; this triggers intrinsic generation.
nb = importlib.import_module("numba_lapack")
if hasattr(nb, "_discover_and_generate"):
    try:
        nb._discover_and_generate(verbose=False)
    except Exception:
        pass

# Locate SciPy .pxd files
try:
    import importlib.resources as res
    PXD_BLAS = res.files("scipy.linalg") / "cython_blas.pxd"
    PXD_LAP  = res.files("scipy.linalg") / "cython_lapack.pxd"
except Exception as e:
    print("Cannot locate SciPy .pxd via importlib.resources:", e)
    sys.exit(1)

if not PXD_BLAS.is_file() or not PXD_LAP.is_file():
    print("Missing cython_blas.pxd or cython_lapack.pxd — is SciPy installed?")
    sys.exit(1)

# ------------------ parsing ------------------

ALIAS_TO_NP = {
    "s": "np.float32",
    "d": "np.float64",
    "c": "np.complex64",
    "z": "np.complex128",
}
INT_TOKENS  = {"int", "lapack_int"}
BOOL_TOKENS = {"bint"}
CHAR_TOKENS = {"char"}

class Arg:
    __slots__ = ("base", "ptr_depth", "name", "raw")
    def __init__(self, base: str, ptr_depth: int, name: str, raw: str):
        self.base = base
        self.ptr_depth = ptr_depth
        self.name = name
        self.raw = raw

class PXDSignature:
    __slots__ = ("name", "ret", "args")
    def __init__(self, name: str, ret: str, args: List[Arg]):
        self.name = name
        self.ret = ret
        self.args = args

SIG_RE = re.compile(
    r"^cdef\s+([A-Za-z0-9_ ]+?)\s+([A-Za-z0-9_]+)\s*\((.*?)\)\s*noexcept.*$",
    re.M,
)

def _strip_comments(txt: str) -> str:
    return "\n".join(
        line for line in txt.splitlines()
        if not line.strip().startswith("#")
    )

def _norm(s: str) -> str:
    return " ".join(s.split())

def _parse_arg(tok: str) -> Optional[Arg]:
    t = tok.strip()
    if not t or " " not in t:
        return None
    tpart, name = t.rsplit(" ", 1)
    ptr_depth = tpart.count("*")
    base = _norm(tpart.replace("*", "").strip())
    name = name.lstrip("*&").strip()  # never include '*' in the argument name
    return Arg(base, ptr_depth, name, tok)

def parse_pxd(path: Path) -> Dict[str, PXDSignature]:
    text = _strip_comments(path.read_text(encoding="utf-8", errors="ignore"))
    out: Dict[str, PXDSignature] = {}
    for m in SIG_RE.finditer(text):
        rett = _norm(m.group(1))
        name = m.group(2)
        args_s = m.group(3).strip()
        # Skip function-pointer typedefs like cselect*/dselect*/...
        if name.startswith(("cselect", "dselect", "sselect", "zselect")):
            continue
        args: List[Arg] = []
        if args_s and args_s != "void":
            parts = [p.strip() for p in args_s.split(",") if p.strip()]
            for p in parts:
                a = _parse_arg(p)
                if a:
                    args.append(a)
        out[name] = PXDSignature(name, rett, args)
    return out

pxd_funcs: Dict[str, PXDSignature] = {}
pxd_funcs.update(parse_pxd(PXD_BLAS))
pxd_funcs.update(parse_pxd(PXD_LAP))
PXD_NAMES = set(pxd_funcs.keys())

# ------------------ typing (no pointer stars) ------------------

STUB_HDR = """\
from typing import Union, TypeVar, Generic
import numpy as np
from numpy.typing import NDArray

# =============================================================================
# Calling rules (UNSAFE wrappers):
# - Passing a machine-size UNSIGNED integer (Address = np.uintp) is interpreted
#   as a RAW POINTER to the parameter’s base dtype.
# - Passing a base scalar (e.g., np.float64, np.int32) to a pointer parameter
#   means: allocate a 1-slot temporary and pass its ADDRESS (by-ref scalar).
# - Passing a NumPy array of the right dtype means: pass its DATA POINTER.
# - Passing a typed pointer Ptr[T] (editor-only alias for Numba CPointer[T])
#   is preferred; functions also accept Address for backward-compat.
# - If you intend an integer VALUE (not a pointer), pass SIGNED int32/int64.
#   Do NOT pass np.uintp unless you really mean a pointer.
# - Flags like 'N','T','U' should be ord('N') or np.uint8(ord('N')).
# =============================================================================

# Raw pointer/address (pointer-sized UNSIGNED). Distinct from int32/int64.
Address = np.uintp

# Editor-only alias for a typed pointer (runtime uses Numba CPointer[T]).
T = TypeVar("T")
class Ptr(Generic[T]): ...  # stub-only; no runtime

# BLAS/LAPACK "int" parameters are LP64 or ILP64 depending on the backend.
BlasInt = Union[np.int32, np.int64]

# Char flags like 'N','T','U' are passed as ord(...) or np.uint8.
Char8 = Union[np.uint8, int]

# Convenience unions for pointer-like params:
#     scalar | ndarray[dtype] | Ptr[dtype] | Address
ScalarOrArray32   = Union[np.float32,    NDArray[np.float32],    Ptr[np.float32],    Address]
ScalarOrArray64   = Union[np.float64,    NDArray[np.float64],    Ptr[np.float64],    Address]
ScalarOrArrayC64  = Union[np.complex64,  NDArray[np.complex64],  Ptr[np.complex64],  Address]
ScalarOrArrayC128 = Union[np.complex128, NDArray[np.complex128], Ptr[np.complex128], Address]
ScalarOrArrayU8   = Union[np.uint8,      NDArray[np.uint8],      Ptr[np.uint8],      Address]
ScalarOrArrayBool = Union[np.bool_,      NDArray[np.bool_],      Ptr[np.bool_],      Address]

# Int pointer-like params can be 32-bit or 64-bit depending on BLAS build:
ScalarOrArrayInt  = Union[BlasInt, NDArray[np.int32], NDArray[np.int64], Ptr[np.int32], Ptr[np.int64], Address]
"""

STUB_MANUAL = """
# === Runtime helpers (manually documented) ====================================

\"\"\"Return the raw data address of a NumPy array (pointer-sized unsigned int).\"\"\"
def data_ptr(a: NDArray[Any]) -> Address: ...

\"\"\"Allocate a one-slot temporary for the scalar and return its address.
Notes:
- Passing np.uintp anywhere means *raw pointer* (unsafe).
- For integer VALUES, pass SIGNED int32/int64 (not np.uintp).
\"\"\"
def byref(x: Union[np.float32, np.float64, np.complex64, np.complex128,
                   np.int32, np.int64, np.uint8, np.bool_]) -> Address: ...
"""

def stub_type_for_arg(a: Arg) -> str:
    """
    Friendly stub type for each argument. We do not display '*' (pointers).
    For pointer params we allow scalar/array/typed pointer/Address.
    """
    base = a.base
    if base in ALIAS_TO_NP:
        return {
            "s": "ScalarOrArray32",
            "d": "ScalarOrArray64",
            "c": "ScalarOrArrayC64",
            "z": "ScalarOrArrayC128",
        }[base]
    if base in INT_TOKENS:
        return "ScalarOrArrayInt"
    if base in BOOL_TOKENS:
        return "ScalarOrArrayBool"
    if base in CHAR_TOKENS:
        return "ScalarOrArrayU8"
    if base.endswith(("select1","select2","select3")):
        return "Address"  # function-pointer callbacks (opaque)
    return "object"

def doc_type_for_arg(a: Arg) -> str:
    """Docs label with precise dtype names, no pointer markers."""
    base = a.base
    if base in ALIAS_TO_NP:
        return {"s":"float32","d":"float64","c":"complex64","z":"complex128"}[base]
    if base in INT_TOKENS:
        return "BlasInt"
    if base in BOOL_TOKENS:
        return "bool"
    if base in CHAR_TOKENS:
        return "uint8"
    if base.endswith(("select1","select2","select3")):
        return "address"
    return "object"

def ret_hint(ret_tok: str) -> str:
    rt = ret_tok.strip()
    if rt == "void":
        return "None"
    if rt in ALIAS_TO_NP:
        return {"s":"np.float32","d":"np.float64","c":"np.complex64","z":"np.complex128"}[rt]
    if rt in INT_TOKENS:
        return "BlasInt"
    if rt in BOOL_TOKENS:
        return "bool"
    if rt in CHAR_TOKENS:
        return "np.uint8"
    return "object"

# ------------------ include only actually exported functions ------------------

def exported_runtime_functions() -> List[str]:
    # Only functions that appear in the .pxd (true BLAS/LAPACK),
    # and explicitly skip our helpers.
    out: List[str] = []
    for name, obj in nb.__dict__.items():
        if not callable(obj):
            continue
        if name in {"data_ptr", "byref"}:
            continue
        if name in PXD_NAMES:
            out.append(name)
    return sorted(out)

EXPORTED = set(exported_runtime_functions())

# ------------------ emit files ------------------

PKG_DIR  = ROOT / "numba_lapack"
DOCS_DIR = ROOT / "docs"
PKG_DIR.mkdir(exist_ok=True)
DOCS_DIR.mkdir(exist_ok=True)

def write_stub():
    lines: List[str] = []
    lines.append("# Auto-generated by tools/gen_docs_stubs_from_pxd.py — DO NOT EDIT.")
    lines.append("from __future__ import annotations")
    lines.append(STUB_HDR.rstrip())
    lines.append("")
    # inject manual helper stubs
    lines.append("from typing import Any")             # needed by NDArray[Any]
    lines.append(STUB_MANUAL.rstrip())
    lines.append("")

    names: List[str] = ["byref", "data_ptr"]          # ensure exported

    for fname in sorted(EXPORTED):
        sig = pxd_funcs.get(fname)
        sig = pxd_funcs.get(fname)
        if sig is None:
            continue  # never stub unknown names (prevents clobbering helpers)

        params = [f"{a.name}: {stub_type_for_arg(a)}" for a in sig.args]
        ret = ret_hint(sig.ret)
        doc_params = ", ".join(f"{a.name}: {doc_type_for_arg(a)}" for a in sig.args) if sig.args else "void"
        lines.append(f'""" {fname}({doc_params}) """')
        lines.append(f"def {fname}({', '.join(params)}) -> {ret}: ...")
        lines.append("")
        names.append(fname)

    lines.append(f"__all__ = {tuple(sorted(set(names)))!r}")
    (PKG_DIR / "__init__.pyi").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote stub:", PKG_DIR / "__init__.pyi")

def write_docs():
    lines: List[str] = []
    lines.append("# numba_lapack: API (from SciPy .pxd)\n")
    lines.append("> **Pointer rule:** passing `np.uintp` means *raw pointer*; for integer VALUES use signed `int32/int64`.\n")
    lines.append("> Parameters are shown without pointer markers; dtypes are precise (float32/64, complex64/128, BlasInt, uint8).\n")
    lines.append("\n| name | return | parameters |\n|---|---|---|\n")
    # Only include names that exist at runtime (exclude the skipped ~16)
    for name in sorted(EXPORTED):
        sig = pxd_funcs.get(name)
        if sig is None:
            continue
        params = ", ".join(f"{a.name}: {doc_type_for_arg(a)}" for a in sig.args) if sig.args else "void"
        lines.append(f"| `{name}` | `{ret_hint(sig.ret)}` | `{params}` |")
    (DOCS_DIR / "autogen_from_pxd.md").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote docs:", DOCS_DIR / "autogen_from_pxd.md")

def main():
    write_stub()
    write_docs()

if __name__ == "__main__":
    main()
