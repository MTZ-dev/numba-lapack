#!/usr/bin/env python3
# bench_blas_lapack.py
import os, time
from statistics import median
import numpy as np
from numba import njit
from scipy.linalg import blas as sblas
from scipy.linalg import get_lapack_funcs

# Our module: BLAS/LAPACK intrinsics + helpers
from numba_lapack import (
    daxpy, ddot, dgemv, dgemm, dgesv,
    byref, data_ptr,
)

# ----------------------------------------------------------------------
# BLAS int width detection (LP64=int32, ILP64=int64)
# ----------------------------------------------------------------------
def _guess_blas_int():
    """
    Heuristic for SciPy wheels:
      - Try .ilp64 attribute on a LAPACK func
      - Else look for '64' in the doc (very rough)
      - Fallback: int32 (LP64)
    """
    try:
        A = np.ones((1, 1), np.float64, order="F")
        B = np.ones((1, 1), np.float64, order="F")
        gesv = get_lapack_funcs(("gesv",), (A, B))[0]
        ilp64 = getattr(gesv, "ilp64", None)
        if ilp64 is None:
            ilp64 = "64" in (getattr(gesv, "__doc__", "") or "")
        return np.int64 if ilp64 else np.int32
    except Exception:
        return np.int32

BLAS_INT = _guess_blas_int()

# ----------------------------------------------------------------------
# Timing helpers + throughput calculators
# ----------------------------------------------------------------------
def time_median(fn, *args, repeats=7, warmup=1):
    for _ in range(warmup):
        fn(*args)
    ts = []
    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        fn(*args)
        ts.append(time.perf_counter_ns() - t0)
    return median(ts)/1e9

def gbps_axpy(n, t):  # read x + read y + write y
    return (24.0 * n) / t / 1e9

def gbps_dot(n, t):   # read x + read y
    return (16.0 * n) / t / 1e9

def tflops_gemm(m, n, k, t):
    return (2.0 * m * n * k) / t / 1e12


# ======================================================================
# JIT wrappers — Convenience path (arrays/scalars directly)
# ======================================================================
@njit(cache=True, fastmath=True)
def j_daxpy(alpha, x, y):
    n = x.shape[0] if x.shape[0] < y.shape[0] else y.shape[0]
    daxpy(n, alpha, x, 1, y, 1)

@njit(cache=True, fastmath=True)
def j_daxpy_inc(alpha, x, incx, y, incy):
    n = x.shape[0] if x.shape[0] < y.shape[0] else y.shape[0]
    daxpy(n, alpha, x, incx, y, incy)

@njit(cache=True, fastmath=True)
def j_ddot(x, y):
    n = x.shape[0] if x.shape[0] < y.shape[0] else y.shape[0]
    return ddot(n, x, 1, y, 1)

@njit(cache=True, fastmath=True)
def j_dgemv(transA_u8, m, n, alpha, A, lda, x, incx, beta, y, incy):
    dgemv(transA_u8, m, n, alpha, A, lda, x, incx, beta, y, incy)

@njit(cache=True, fastmath=True)
def j_dgemm(transA_u8, transB_u8, m, n, k, alpha, A, lda, B, ldb, beta, C, ldc):
    dgemm(transA_u8, transB_u8, m, n, k, alpha, A, lda, B, ldb, beta, C, ldc)

@njit(cache=True, fastmath=True)
def j_dgesv(A, B, ipiv, info):
    n   = A.shape[0]
    nrh = B.shape[1]
    lda = A.shape[0] if A.shape[0] > 1 else 1
    ldb = B.shape[0] if B.shape[0] > 1 else 1
    dgesv(n, nrh, A, lda, ipiv, B, ldb, info)


# ======================================================================
# JIT wrappers — All-pointer path (byref for *everything* scalar-like)
# ======================================================================
@njit(cache=True, fastmath=False)  # keep simple while validating ABI
def j_daxpy_allptr(alpha, x, y):
    n   = x.shape[0] if x.shape[0] < y.shape[0] else y.shape[0]
    one = BLAS_INT(1)
    daxpy(byref(BLAS_INT(n)),
          byref(alpha),
          data_ptr(x),
          byref(one),
          data_ptr(y),
          byref(one))

@njit(cache=True, fastmath=False)
def j_daxpy_inc_allptr(alpha, xs, incx, ys, incy):
    n = xs.shape[0] if xs.shape[0] < ys.shape[0] else ys.shape[0]
    daxpy(byref(BLAS_INT(n)),
          byref(alpha),
          data_ptr(xs), byref(BLAS_INT(incx)),
          data_ptr(ys), byref(BLAS_INT(incy)))

@njit(cache=True, fastmath=False)
def j_ddot_allptr(x, y):
    n   = x.shape[0] if x.shape[0] < y.shape[0] else y.shape[0]
    one = BLAS_INT(1)
    return ddot(byref(BLAS_INT(n)),
                data_ptr(x), byref(one),
                data_ptr(y), byref(one))

@njit(cache=True, fastmath=False)
def j_dgemv_allptr(transA_u8, m, n, alpha, A, lda, x, incx, beta, y, incy):
    dgemv(byref(transA_u8),
          byref(BLAS_INT(m)), byref(BLAS_INT(n)),
          byref(alpha),
          data_ptr(A), byref(BLAS_INT(lda)),
          data_ptr(x), byref(BLAS_INT(incx)),
          byref(beta),
          data_ptr(y), byref(BLAS_INT(incy)))

@njit(cache=True, fastmath=False)
def j_dgemm_allptr(transA_u8, transB_u8, m, n, k, alpha, A, lda, B, ldb, beta, C, ldc):
    dgemm(byref(transA_u8), byref(transB_u8),
          byref(BLAS_INT(m)), byref(BLAS_INT(n)), byref(BLAS_INT(k)),
          byref(alpha),
          data_ptr(A), byref(BLAS_INT(lda)),
          data_ptr(B), byref(BLAS_INT(ldb)),
          byref(beta),
          data_ptr(C), byref(BLAS_INT(ldc)))

@njit(cache=True, fastmath=False)
def j_dgesv_allptr(A, B, ipiv, info):
    n   = A.shape[0]
    nrh = B.shape[1]
    lda = A.shape[0] if A.shape[0] > 1 else 1
    ldb = B.shape[0] if B.shape[0] > 1 else 1
    dgesv(byref(BLAS_INT(n)), byref(BLAS_INT(nrh)),
          data_ptr(A), byref(BLAS_INT(lda)),
          data_ptr(ipiv),
          data_ptr(B), byref(BLAS_INT(ldb)),
          data_ptr(info))

# ----------------------------------------------------------------------
# Tiny smoke test for the all-pointer ABI (catches ILP64/LP64 mistakes)
# ----------------------------------------------------------------------
def _smoke_allptr():
    x = np.array([1.0, 2.0], np.float64)
    y = np.array([3.0, 4.0], np.float64)
    j_daxpy_allptr(2.0, x, y)       # y := 2*x + y -> [5, 8]
    assert np.allclose(y, [5.0, 8.0])
    s = j_ddot_allptr(x, y)         # 1*5 + 2*8 = 21
    assert abs(float(s) - 21.0) < 1e-12


# ======================================================================
# Main benchmark
# ======================================================================
def main():
    rng = np.random.default_rng(0)
    print("NumPy:", np.__version__)
    print("BLAS_INT dtype:", BLAS_INT)

    # -------- Level-1: daxpy / ddot (contiguous + strided) --------
    print("\n== Level-1: daxpy / ddot ==")
    _smoke_allptr()

    N = 20_000_000
    x = rng.standard_normal(N).astype(np.float64)
    y0 = rng.standard_normal(N).astype(np.float64)
    alpha = 2.0

    # contiguous correctness
    y_ref = y0 + alpha * x
    y = y0.copy()
    j_daxpy(alpha, x, y)
    assert np.allclose(y, y_ref)

    # true strided correctness (mutate a real strided view)
    xs = x[::2]               # stride 2
    ybuf = y0.copy()
    ys = ybuf[1::2]           # stride 2 view
    y_ref2 = ys.copy()
    y_ref2 += alpha * xs

    incx = xs.strides[0] // xs.itemsize
    incy = ys.strides[0] // ys.itemsize

    j_daxpy_inc(alpha, xs, incx, ys, incy)      # convenience
    assert np.allclose(ys, y_ref2)

    # all-pointer variant for strided
    ybuf2 = y0.copy()
    ys2 = ybuf2[1::2]
    j_daxpy_inc_allptr(alpha, xs, incx, ys2, incy)
    assert np.allclose(ys2, y_ref2)

    # ddot correctness
    dot_ref = float(np.dot(x, y0))
    dot_val = float(j_ddot(x, y0))
    dot_val2 = float(j_ddot_allptr(x, y0))
    assert np.allclose(dot_val, dot_ref)
    assert np.allclose(dot_val2, dot_ref)

    # timings vs NumPy & SciPy BLAS (SciPy returns arrays)
    t_axpy_numba = time_median(j_daxpy, alpha, x, y0.copy(), repeats=5)
    t_axpy_numba_ptr = time_median(j_daxpy_allptr, alpha, x, y0.copy(), repeats=5)

    t_axpy_numpy = time_median(lambda a, xx, yy: yy.__iadd__(a * xx),
                               alpha, x, y0.copy(), repeats=5)

    def saxpy_scipy(a, xx, yy):
        y_out = sblas.daxpy(xx, yy, a=a, n=xx.size, incx=1, incy=1)
        np.copyto(yy, y_out)
    t_axpy_scipy = time_median(saxpy_scipy, alpha, x, y0.copy(), repeats=5)

    t_ddot_numba = time_median(j_ddot, x, y0, repeats=5)
    t_ddot_numba_ptr = time_median(j_ddot_allptr, x, y0, repeats=5)
    t_ddot_numpy = time_median(np.dot, x, y0, repeats=5)
    t_ddot_scipy = time_median(lambda xx, yy: sblas.ddot(xx, yy, n=xx.size, incx=1, incy=1),
                               x, y0, repeats=5)

    print(f"daxpy  numba(arr/scal): {t_axpy_numba:.6f}s  ~{gbps_axpy(N,t_axpy_numba):.2f} GB/s")
    print(f"daxpy  numba(all-ptr) : {t_axpy_numba_ptr:.6f}s  ~{gbps_axpy(N,t_axpy_numba_ptr):.2f} GB/s")
    print(f"daxpy  numpy          : {t_axpy_numpy:.6f}s")
    print(f"daxpy  scipy          : {t_axpy_scipy:.6f}s")
    print(f"ddot   numba(arr)     : {t_ddot_numba:.6f}s  ~{gbps_dot(N,t_ddot_numba):.2f} GB/s")
    print(f"ddot   numba(all-ptr) : {t_ddot_numba_ptr:.6f}s  ~{gbps_dot(N,t_ddot_numba_ptr):.2f} GB/s")
    print(f"ddot   numpy          : {t_ddot_numpy:.6f}s")
    print(f"ddot   scipy          : {t_ddot_scipy:.6f}s")

    # -------- Level-2: dgemv --------
    print("\n== Level-2: dgemv ==")
    m, n = 8000, 4000
    A = np.asfortranarray(rng.standard_normal((m, n), dtype=np.float64))
    xvec = rng.standard_normal(n).astype(np.float64)
    yvec0 = rng.standard_normal(m).astype(np.float64)
    alpha, beta = 1.2, -0.3

    y_ref = alpha * (A @ xvec) + beta * yvec0
    yvec = yvec0.copy()
    j_dgemv(np.uint8(ord('N')), m, n, alpha, A, max(1,m), xvec, 1, beta, yvec, 1)
    assert np.allclose(yvec, y_ref, rtol=1e-11, atol=1e-11)

    yvec2 = yvec0.copy(order="C")
    j_dgemv_allptr(np.uint8(ord('N')), m, n, alpha, A, max(1,m), xvec, 1, beta, yvec2, 1)
    assert np.allclose(yvec2, y_ref, rtol=1e-11, atol=1e-11)

    t_gemv_numba = time_median(j_dgemv, np.uint8(ord('N')), m, n, alpha, A, max(1,m),
                               xvec, 1, beta, yvec0.copy(), 1, repeats=5)
    t_gemv_numba_ptr = time_median(j_dgemv_allptr, np.uint8(ord('N')), m, n, alpha, A, max(1,m),
                                   xvec, 1, beta, yvec0.copy(), 1, repeats=5)
    t_gemv_scipy = time_median(lambda AA, xx, yy: sblas.dgemv(alpha, AA, xx, beta=beta, y=yy, trans=0),
                               A, xvec, yvec0.copy(), repeats=5)
    t_gemv_numpy = time_median(lambda AA, xx: AA @ xx, A, xvec, repeats=5)

    print(f"dgemv  numba(arr/scal): {t_gemv_numba:.6f}s")
    print(f"dgemv  numba(all-ptr) : {t_gemv_numba_ptr:.6f}s")
    print(f"dgemv  numpy (matvec)  : {t_gemv_numpy:.6f}s")
    print(f"dgemv  scipy           : {t_gemv_scipy:.6f}s")

    # -------- Level-3: dgemm --------
    print("\n== Level-3: dgemm (NN) ==")
    m, k, n = 2048, 1024, 512
    A = np.asfortranarray(rng.standard_normal((m, k), dtype=np.float64))
    B = np.asfortranarray(rng.standard_normal((k, n), dtype=np.float64))
    C0 = np.asfortranarray(rng.standard_normal((m, n), dtype=np.float64))
    alpha, beta = 1.25, -0.5
    C_ref = alpha * (A @ B) + beta * C0

    C = C0.copy(order='F')
    j_dgemm(np.uint8(ord('N')), np.uint8(ord('N')),
            m, n, k, alpha, A, max(1,m), B, max(1,k), beta, C, max(1,m))
    assert np.allclose(C, C_ref, rtol=1e-11, atol=1e-11)

    C2 = C0.copy(order='F')
    j_dgemm_allptr(np.uint8(ord('N')), np.uint8(ord('N')),
                   m, n, k, alpha, A, max(1,m), B, max(1,k), beta, C2, max(1,m))
    assert np.allclose(C2, C_ref, rtol=1e-11, atol=1e-11)

    t_gemm_numba = time_median(j_dgemm, np.uint8(ord('N')), np.uint8(ord('N')),
                               m, n, k, alpha, A, max(1,m), B, max(1,k),
                               beta, C0.copy(order='F'), max(1,m), repeats=5)
    t_gemm_numba_ptr = time_median(j_dgemm_allptr, np.uint8(ord('N')), np.uint8(ord('N')),
                                   m, n, k, alpha, A, max(1,m), B, max(1,k),
                                   beta, C0.copy(order='F'), max(1,m), repeats=5)
    t_gemm_scipy = time_median(lambda AA, BB, CC: sblas.dgemm(alpha, AA, BB, beta=beta, c=CC, trans_a=0, trans_b=0),
                               A, B, C0.copy(order='F'), repeats=5)
    t_gemm_numpy = time_median(lambda AA, BB: AA @ BB, A, B, repeats=3)

    print(f"dgemm  numba(arr/scal): {t_gemm_numba:.6f}s  ~{tflops_gemm(m,n,k,t_gemm_numba):.2f} TFLOP/s")
    print(f"dgemm  numba(all-ptr) : {t_gemm_numba_ptr:.6f}s  ~{tflops_gemm(m,n,k,t_gemm_numba_ptr):.2f} TFLOP/s")
    print(f"dgemm  numpy (matmul)  : {t_gemm_numpy:.6f}s")
    print(f"dgemm  scipy           : {t_gemm_scipy:.6f}s")

    # -------- LAPACK: dgesv --------
    print("\n== LAPACK: dgesv (solve Ax=B) ==")
    n, nrhs = 800, 3
    A = np.asfortranarray(rng.standard_normal((n, n), dtype=np.float64))
    A += n * np.eye(n, dtype=np.float64)
    B = np.asfortranarray(rng.standard_normal((n, nrhs), dtype=np.float64))
    X_ref = np.linalg.solve(A.copy(order='F'), B.copy(order='F'))

    # convenience
    A_lu = A.copy(order='F'); B_sol = B.copy(order='F')
    ipiv = np.empty(n, dtype=BLAS_INT, order='F')
    info = np.zeros(1, dtype=BLAS_INT, order='F')
    j_dgesv(A_lu, B_sol, ipiv, info)
    assert int(info[0]) == 0
    assert np.allclose(B_sol, X_ref, rtol=1e-10, atol=1e-10)

    # all-pointer
    A_lu2 = A.copy(order='F'); B_sol2 = B.copy(order='F')
    ipiv2 = np.empty(n, dtype=BLAS_INT, order='F')
    info2 = np.zeros(1, dtype=BLAS_INT, order='F')
    j_dgesv_allptr(A_lu2, B_sol2, ipiv2, info2)
    assert int(info2[0]) == 0
    assert np.allclose(B_sol2, X_ref, rtol=1e-10, atol=1e-10)

    dgesv_ref = get_lapack_funcs(("gesv",), (A, B))[0]
    def run_dgesv_ref(AA, BB):
        AA = AA.copy(order='F'); BB = BB.copy(order='F')
        out = dgesv_ref(AA, BB, overwrite_a=1, overwrite_b=1)
        # SciPy version differences:
        if isinstance(out, tuple):
            if len(out) == 4:
                lu, piv, x, info3 = out
            elif len(out) == 3:
                x, piv, info3 = out
            else:
                raise RuntimeError(f"Unexpected gesv return arity: {len(out)}")
            if int(info3) != 0:
                raise RuntimeError(f"gesv info={info3}")
            return x
        raise RuntimeError("Unexpected gesv return type")

    t_gesv_numba     = time_median(j_dgesv,         A.copy(order='F'), B.copy(order='F'),
                                   np.empty(n, dtype=BLAS_INT, order='F'), np.zeros(1, BLAS_INT, order='F'),
                                   repeats=3)
    t_gesv_numba_ptr = time_median(j_dgesv_allptr,  A.copy(order='F'), B.copy(order='F'),
                                   np.empty(n, dtype=BLAS_INT, order='F'), np.zeros(1, BLAS_INT, order='F'),
                                   repeats=3)
    t_gesv_scipy     = time_median(run_dgesv_ref, A, B, repeats=3)

    print(f"dgesv  numba(arr/scal): {t_gesv_numba:.6f}s  (n={n}, nrhs={nrhs})")
    print(f"dgesv  numba(all-ptr) : {t_gesv_numba_ptr:.6f}s  (n={n}, nrhs={nrhs})")
    print(f"dgesv  scipy          : {t_gesv_scipy:.6f}s")

    print("\nAll checks passed.")

if __name__ == "__main__":
    # If you want less variance, uncomment to pin threads:
    # os.environ["OPENBLAS_NUM_THREADS"] = "1"
    # os.environ["MKL_NUM_THREADS"] = "1"
    main()
