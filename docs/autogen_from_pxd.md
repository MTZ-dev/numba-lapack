# numba_lapack: API (from SciPy .pxd)

> **Pointer rule:** passing `np.uintp` means *raw pointer*; for integer VALUES use signed `int32/int64`.

> Parameters are shown without pointer markers; dtypes are precise (float32/64, complex64/128, BlasInt, uint8).


| name | return | parameters |
|---|---|---|

| `caxpy` | `None` | `n: BlasInt, ca: complex64, cx: complex64, incx: BlasInt, cy: complex64, incy: BlasInt` |
| `cbbcsd` | `None` | `jobu1: uint8, jobu2: uint8, jobv1t: uint8, jobv2t: uint8, trans: uint8, m: BlasInt, p: BlasInt, q: BlasInt, theta: float32, phi: float32, u1: complex64, ldu1: BlasInt, u2: complex64, ldu2: BlasInt, v1t: complex64, ldv1t: BlasInt, v2t: complex64, ldv2t: BlasInt, b11d: float32, b11e: float32, b12d: float32, b12e: float32, b21d: float32, b21e: float32, b22d: float32, b22e: float32, rwork: float32, lrwork: BlasInt, info: BlasInt` |
| `cbdsqr` | `None` | `uplo: uint8, n: BlasInt, ncvt: BlasInt, nru: BlasInt, ncc: BlasInt, d: float32, e: float32, vt: complex64, ldvt: BlasInt, u: complex64, ldu: BlasInt, c: complex64, ldc: BlasInt, rwork: float32, info: BlasInt` |
| `ccopy` | `None` | `n: BlasInt, cx: complex64, incx: BlasInt, cy: complex64, incy: BlasInt` |
| `cdotc` | `np.complex64` | `n: BlasInt, cx: complex64, incx: BlasInt, cy: complex64, incy: BlasInt` |
| `cdotu` | `np.complex64` | `n: BlasInt, cx: complex64, incx: BlasInt, cy: complex64, incy: BlasInt` |
| `cgbbrd` | `None` | `vect: uint8, m: BlasInt, n: BlasInt, ncc: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex64, ldab: BlasInt, d: float32, e: float32, q: complex64, ldq: BlasInt, pt: complex64, ldpt: BlasInt, c: complex64, ldc: BlasInt, work: complex64, rwork: float32, info: BlasInt` |
| `cgbcon` | `None` | `norm: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex64, ldab: BlasInt, ipiv: BlasInt, anorm: float32, rcond: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cgbequ` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex64, ldab: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, info: BlasInt` |
| `cgbequb` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex64, ldab: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, info: BlasInt` |
| `cgbmv` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt, beta: complex64, y: complex64, incy: BlasInt` |
| `cgbrfs` | `None` | `trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, afb: complex64, ldafb: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cgbsv` | `None` | `n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cgbsvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, afb: complex64, ldafb: BlasInt, ipiv: BlasInt, equed: uint8, r: float32, c: float32, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cgbtf2` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex64, ldab: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `cgbtrf` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex64, ldab: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `cgbtrs` | `None` | `trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cgebak` | `None` | `job: uint8, side: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float32, m: BlasInt, v: complex64, ldv: BlasInt, info: BlasInt` |
| `cgebal` | `None` | `job: uint8, n: BlasInt, a: complex64, lda: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float32, info: BlasInt` |
| `cgebd2` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, d: float32, e: float32, tauq: complex64, taup: complex64, work: complex64, info: BlasInt` |
| `cgebrd` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, d: float32, e: float32, tauq: complex64, taup: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgecon` | `None` | `norm: uint8, n: BlasInt, a: complex64, lda: BlasInt, anorm: float32, rcond: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cgeequ` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, info: BlasInt` |
| `cgeequb` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, info: BlasInt` |
| `cgeev` | `None` | `jobvl: uint8, jobvr: uint8, n: BlasInt, a: complex64, lda: BlasInt, w: complex64, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cgeevx` | `None` | `balanc: uint8, jobvl: uint8, jobvr: uint8, sense: uint8, n: BlasInt, a: complex64, lda: BlasInt, w: complex64, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float32, abnrm: float32, rconde: float32, rcondv: float32, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cgehd2` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cgehrd` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgelq2` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cgelqf` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgels` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgelsd` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, s: float32, rcond: float32, rank: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, iwork: BlasInt, info: BlasInt` |
| `cgelss` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, s: float32, rcond: float32, rank: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cgelsy` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, jpvt: BlasInt, rcond: float32, rank: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cgemm` | `None` | `transa: uint8, transb: uint8, m: BlasInt, n: BlasInt, k: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, beta: complex64, c: complex64, ldc: BlasInt` |
| `cgemqrt` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, nb: BlasInt, v: complex64, ldv: BlasInt, t: complex64, ldt: BlasInt, c: complex64, ldc: BlasInt, work: complex64, info: BlasInt` |
| `cgemv` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt, beta: complex64, y: complex64, incy: BlasInt` |
| `cgeql2` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cgeqlf` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgeqp3` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, jpvt: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cgeqr2` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cgeqr2p` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cgeqrf` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgeqrfp` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgeqrt` | `None` | `m: BlasInt, n: BlasInt, nb: BlasInt, a: complex64, lda: BlasInt, t: complex64, ldt: BlasInt, work: complex64, info: BlasInt` |
| `cgeqrt2` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, t: complex64, ldt: BlasInt, info: BlasInt` |
| `cgeqrt3` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, t: complex64, ldt: BlasInt, info: BlasInt` |
| `cgerc` | `None` | `m: BlasInt, n: BlasInt, alpha: complex64, x: complex64, incx: BlasInt, y: complex64, incy: BlasInt, a: complex64, lda: BlasInt` |
| `cgerfs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, af: complex64, ldaf: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cgerq2` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cgerqf` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgeru` | `None` | `m: BlasInt, n: BlasInt, alpha: complex64, x: complex64, incx: BlasInt, y: complex64, incy: BlasInt, a: complex64, lda: BlasInt` |
| `cgesc2` | `None` | `n: BlasInt, a: complex64, lda: BlasInt, rhs: complex64, ipiv: BlasInt, jpiv: BlasInt, scale: float32` |
| `cgesdd` | `None` | `jobz: uint8, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, s: float32, u: complex64, ldu: BlasInt, vt: complex64, ldvt: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, iwork: BlasInt, info: BlasInt` |
| `cgesv` | `None` | `n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cgesvd` | `None` | `jobu: uint8, jobvt: uint8, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, s: float32, u: complex64, ldu: BlasInt, vt: complex64, ldvt: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cgesvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, af: complex64, ldaf: BlasInt, ipiv: BlasInt, equed: uint8, r: float32, c: float32, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cgetc2` | `None` | `n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, jpiv: BlasInt, info: BlasInt` |
| `cgetf2` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `cgetrf` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `cgetri` | `None` | `n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgetrs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cggbak` | `None` | `job: uint8, side: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float32, rscale: float32, m: BlasInt, v: complex64, ldv: BlasInt, info: BlasInt` |
| `cggbal` | `None` | `job: uint8, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float32, rscale: float32, work: float32, info: BlasInt` |
| `cggev` | `None` | `jobvl: uint8, jobvr: uint8, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, alpha: complex64, beta: complex64, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cggevx` | `None` | `balanc: uint8, jobvl: uint8, jobvr: uint8, sense: uint8, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, alpha: complex64, beta: complex64, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float32, rscale: float32, abnrm: float32, bbnrm: float32, rconde: float32, rcondv: float32, work: complex64, lwork: BlasInt, rwork: float32, iwork: BlasInt, bwork: bool, info: BlasInt` |
| `cggglm` | `None` | `n: BlasInt, m: BlasInt, p: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, d: complex64, x: complex64, y: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgghrd` | `None` | `compq: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, q: complex64, ldq: BlasInt, z: complex64, ldz: BlasInt, info: BlasInt` |
| `cgglse` | `None` | `m: BlasInt, n: BlasInt, p: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, c: complex64, d: complex64, x: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cggqrf` | `None` | `n: BlasInt, m: BlasInt, p: BlasInt, a: complex64, lda: BlasInt, taua: complex64, b: complex64, ldb: BlasInt, taub: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cggrqf` | `None` | `m: BlasInt, p: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, taua: complex64, b: complex64, ldb: BlasInt, taub: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cgtcon` | `None` | `norm: uint8, n: BlasInt, dl: complex64, d: complex64, du: complex64, du2: complex64, ipiv: BlasInt, anorm: float32, rcond: float32, work: complex64, info: BlasInt` |
| `cgtrfs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, dl: complex64, d: complex64, du: complex64, dlf: complex64, df: complex64, duf: complex64, du2: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cgtsv` | `None` | `n: BlasInt, nrhs: BlasInt, dl: complex64, d: complex64, du: complex64, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cgtsvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, nrhs: BlasInt, dl: complex64, d: complex64, du: complex64, dlf: complex64, df: complex64, duf: complex64, du2: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cgttrf` | `None` | `n: BlasInt, dl: complex64, d: complex64, du: complex64, du2: complex64, ipiv: BlasInt, info: BlasInt` |
| `cgttrs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, dl: complex64, d: complex64, du: complex64, du2: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cgtts2` | `None` | `itrans: BlasInt, n: BlasInt, nrhs: BlasInt, dl: complex64, d: complex64, du: complex64, du2: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt` |
| `chbev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, rwork: float32, info: BlasInt` |
| `chbevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `chbevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, q: complex64, ldq: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, rwork: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `chbgst` | `None` | `vect: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: complex64, ldab: BlasInt, bb: complex64, ldbb: BlasInt, x: complex64, ldx: BlasInt, work: complex64, rwork: float32, info: BlasInt` |
| `chbgv` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: complex64, ldab: BlasInt, bb: complex64, ldbb: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, rwork: float32, info: BlasInt` |
| `chbgvd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: complex64, ldab: BlasInt, bb: complex64, ldbb: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `chbgvx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: complex64, ldab: BlasInt, bb: complex64, ldbb: BlasInt, q: complex64, ldq: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, rwork: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `chbmv` | `None` | `uplo: uint8, n: BlasInt, k: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt, beta: complex64, y: complex64, incy: BlasInt` |
| `chbtrd` | `None` | `vect: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, d: float32, e: float32, q: complex64, ldq: BlasInt, work: complex64, info: BlasInt` |
| `checon` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, anorm: float32, rcond: float32, work: complex64, info: BlasInt` |
| `cheequb` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, s: float32, scond: float32, amax: float32, work: complex64, info: BlasInt` |
| `cheev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, w: float32, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cheevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, w: float32, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `cheevr` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, isuppz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `cheevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `chegs2` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `chegst` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `chegv` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, w: float32, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `chegvd` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, w: float32, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `chegvx` | `None` | `itype: BlasInt, jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `chemm` | `None` | `side: uint8, uplo: uint8, m: BlasInt, n: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, beta: complex64, c: complex64, ldc: BlasInt` |
| `chemv` | `None` | `uplo: uint8, n: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt, beta: complex64, y: complex64, incy: BlasInt` |
| `cher` | `None` | `uplo: uint8, n: BlasInt, alpha: float32, x: complex64, incx: BlasInt, a: complex64, lda: BlasInt` |
| `cher2` | `None` | `uplo: uint8, n: BlasInt, alpha: complex64, x: complex64, incx: BlasInt, y: complex64, incy: BlasInt, a: complex64, lda: BlasInt` |
| `cher2k` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, beta: float32, c: complex64, ldc: BlasInt` |
| `cherfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, af: complex64, ldaf: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cherk` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float32, a: complex64, lda: BlasInt, beta: float32, c: complex64, ldc: BlasInt` |
| `chesv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `chesvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, af: complex64, ldaf: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `cheswapr` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, i1: BlasInt, i2: BlasInt` |
| `chetd2` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, d: float32, e: float32, tau: complex64, info: BlasInt` |
| `chetf2` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `chetrd` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, d: float32, e: float32, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `chetrf` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `chetri` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, info: BlasInt` |
| `chetri2` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `chetri2x` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, nb: BlasInt, info: BlasInt` |
| `chetrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `chetrs2` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, work: complex64, info: BlasInt` |
| `chfrk` | `None` | `transr: uint8, uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float32, a: complex64, lda: BlasInt, beta: float32, c: complex64` |
| `chgeqz` | `None` | `job: uint8, compq: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex64, ldh: BlasInt, t: complex64, ldt: BlasInt, alpha: complex64, beta: complex64, q: complex64, ldq: BlasInt, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `chla_transtype` | `np.uint8` | `trans: BlasInt` |
| `chpcon` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, ipiv: BlasInt, anorm: float32, rcond: float32, work: complex64, info: BlasInt` |
| `chpev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ap: complex64, w: float32, z: complex64, ldz: BlasInt, work: complex64, rwork: float32, info: BlasInt` |
| `chpevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ap: complex64, w: float32, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `chpevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ap: complex64, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, rwork: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `chpgst` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, ap: complex64, bp: complex64, info: BlasInt` |
| `chpgv` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, ap: complex64, bp: complex64, w: float32, z: complex64, ldz: BlasInt, work: complex64, rwork: float32, info: BlasInt` |
| `chpgvd` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, ap: complex64, bp: complex64, w: float32, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `chpgvx` | `None` | `itype: BlasInt, jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ap: complex64, bp: complex64, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, work: complex64, rwork: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `chpmv` | `None` | `uplo: uint8, n: BlasInt, alpha: complex64, ap: complex64, x: complex64, incx: BlasInt, beta: complex64, y: complex64, incy: BlasInt` |
| `chpr` | `None` | `uplo: uint8, n: BlasInt, alpha: float32, x: complex64, incx: BlasInt, ap: complex64` |
| `chpr2` | `None` | `uplo: uint8, n: BlasInt, alpha: complex64, x: complex64, incx: BlasInt, y: complex64, incy: BlasInt, ap: complex64` |
| `chprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, afp: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `chpsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `chpsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, afp: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `chptrd` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, d: float32, e: float32, tau: complex64, info: BlasInt` |
| `chptrf` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, ipiv: BlasInt, info: BlasInt` |
| `chptri` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, ipiv: BlasInt, work: complex64, info: BlasInt` |
| `chptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `chsein` | `None` | `side: uint8, eigsrc: uint8, initv: uint8, select: bool, n: BlasInt, h: complex64, ldh: BlasInt, w: complex64, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: complex64, rwork: float32, ifaill: BlasInt, ifailr: BlasInt, info: BlasInt` |
| `chseqr` | `None` | `job: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex64, ldh: BlasInt, w: complex64, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `clabrd` | `None` | `m: BlasInt, n: BlasInt, nb: BlasInt, a: complex64, lda: BlasInt, d: float32, e: float32, tauq: complex64, taup: complex64, x: complex64, ldx: BlasInt, y: complex64, ldy: BlasInt` |
| `clacgv` | `None` | `n: BlasInt, x: complex64, incx: BlasInt` |
| `clacn2` | `None` | `n: BlasInt, v: complex64, x: complex64, est: float32, kase: BlasInt, isave: BlasInt` |
| `clacon` | `None` | `n: BlasInt, v: complex64, x: complex64, est: float32, kase: BlasInt` |
| `clacp2` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, b: complex64, ldb: BlasInt` |
| `clacpy` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt` |
| `clacrm` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, b: float32, ldb: BlasInt, c: complex64, ldc: BlasInt, rwork: float32` |
| `clacrt` | `None` | `n: BlasInt, cx: complex64, incx: BlasInt, cy: complex64, incy: BlasInt, c: complex64, s: complex64` |
| `cladiv` | `np.complex64` | `x: complex64, y: complex64` |
| `claed0` | `None` | `qsiz: BlasInt, n: BlasInt, d: float32, e: float32, q: complex64, ldq: BlasInt, qstore: complex64, ldqs: BlasInt, rwork: float32, iwork: BlasInt, info: BlasInt` |
| `claed7` | `None` | `n: BlasInt, cutpnt: BlasInt, qsiz: BlasInt, tlvls: BlasInt, curlvl: BlasInt, curpbm: BlasInt, d: float32, q: complex64, ldq: BlasInt, rho: float32, indxq: BlasInt, qstore: float32, qptr: BlasInt, prmptr: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float32, work: complex64, rwork: float32, iwork: BlasInt, info: BlasInt` |
| `claed8` | `None` | `k: BlasInt, n: BlasInt, qsiz: BlasInt, q: complex64, ldq: BlasInt, d: float32, rho: float32, cutpnt: BlasInt, z: float32, dlamda: float32, q2: complex64, ldq2: BlasInt, w: float32, indxp: BlasInt, indx: BlasInt, indxq: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float32, info: BlasInt` |
| `claein` | `None` | `rightv: bool, noinit: bool, n: BlasInt, h: complex64, ldh: BlasInt, w: complex64, v: complex64, b: complex64, ldb: BlasInt, rwork: float32, eps3: float32, smlnum: float32, info: BlasInt` |
| `claesy` | `None` | `a: complex64, b: complex64, c: complex64, rt1: complex64, rt2: complex64, evscal: complex64, cs1: complex64, sn1: complex64` |
| `claev2` | `None` | `a: complex64, b: complex64, c: complex64, rt1: float32, rt2: float32, cs1: float32, sn1: complex64` |
| `clag2z` | `None` | `m: BlasInt, n: BlasInt, sa: complex64, ldsa: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `clags2` | `None` | `upper: bool, a1: float32, a2: complex64, a3: float32, b1: float32, b2: complex64, b3: float32, csu: float32, snu: complex64, csv: float32, snv: complex64, csq: float32, snq: complex64` |
| `clagtm` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, alpha: float32, dl: complex64, d: complex64, du: complex64, x: complex64, ldx: BlasInt, beta: float32, b: complex64, ldb: BlasInt` |
| `clahef` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, kb: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, w: complex64, ldw: BlasInt, info: BlasInt` |
| `clahqr` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex64, ldh: BlasInt, w: complex64, iloz: BlasInt, ihiz: BlasInt, z: complex64, ldz: BlasInt, info: BlasInt` |
| `clahr2` | `None` | `n: BlasInt, k: BlasInt, nb: BlasInt, a: complex64, lda: BlasInt, tau: complex64, t: complex64, ldt: BlasInt, y: complex64, ldy: BlasInt` |
| `claic1` | `None` | `job: BlasInt, j: BlasInt, x: complex64, sest: float32, w: complex64, gamma: complex64, sestpr: float32, s: complex64, c: complex64` |
| `clals0` | `None` | `icompq: BlasInt, nl: BlasInt, nr: BlasInt, sqre: BlasInt, nrhs: BlasInt, b: complex64, ldb: BlasInt, bx: complex64, ldbx: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, givnum: float32, ldgnum: BlasInt, poles: float32, difl: float32, difr: float32, z: float32, k: BlasInt, c: float32, s: float32, rwork: float32, info: BlasInt` |
| `clalsa` | `None` | `icompq: BlasInt, smlsiz: BlasInt, n: BlasInt, nrhs: BlasInt, b: complex64, ldb: BlasInt, bx: complex64, ldbx: BlasInt, u: float32, ldu: BlasInt, vt: float32, k: BlasInt, difl: float32, difr: float32, z: float32, poles: float32, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, perm: BlasInt, givnum: float32, c: float32, s: float32, rwork: float32, iwork: BlasInt, info: BlasInt` |
| `clalsd` | `None` | `uplo: uint8, smlsiz: BlasInt, n: BlasInt, nrhs: BlasInt, d: float32, e: float32, b: complex64, ldb: BlasInt, rcond: float32, rank: BlasInt, work: complex64, rwork: float32, iwork: BlasInt, info: BlasInt` |
| `clangb` | `np.float32` | `norm: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex64, ldab: BlasInt, work: float32` |
| `clange` | `np.float32` | `norm: uint8, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, work: float32` |
| `clangt` | `np.float32` | `norm: uint8, n: BlasInt, dl: complex64, d: complex64, du: complex64` |
| `clanhb` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, k: BlasInt, ab: complex64, ldab: BlasInt, work: float32` |
| `clanhe` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, work: float32` |
| `clanhf` | `np.float32` | `norm: uint8, transr: uint8, uplo: uint8, n: BlasInt, a: complex64, work: float32` |
| `clanhp` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, ap: complex64, work: float32` |
| `clanhs` | `np.float32` | `norm: uint8, n: BlasInt, a: complex64, lda: BlasInt, work: float32` |
| `clanht` | `np.float32` | `norm: uint8, n: BlasInt, d: float32, e: complex64` |
| `clansb` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, k: BlasInt, ab: complex64, ldab: BlasInt, work: float32` |
| `clansp` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, ap: complex64, work: float32` |
| `clansy` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, work: float32` |
| `clantb` | `np.float32` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, k: BlasInt, ab: complex64, ldab: BlasInt, work: float32` |
| `clantp` | `np.float32` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, ap: complex64, work: float32` |
| `clantr` | `np.float32` | `norm: uint8, uplo: uint8, diag: uint8, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, work: float32` |
| `clapll` | `None` | `n: BlasInt, x: complex64, incx: BlasInt, y: complex64, incy: BlasInt, ssmin: float32` |
| `clapmr` | `None` | `forwrd: bool, m: BlasInt, n: BlasInt, x: complex64, ldx: BlasInt, k: BlasInt` |
| `clapmt` | `None` | `forwrd: bool, m: BlasInt, n: BlasInt, x: complex64, ldx: BlasInt, k: BlasInt` |
| `claqgb` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex64, ldab: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, equed: uint8` |
| `claqge` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, equed: uint8` |
| `claqhb` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, s: float32, scond: float32, amax: float32, equed: uint8` |
| `claqhe` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, s: float32, scond: float32, amax: float32, equed: uint8` |
| `claqhp` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, s: float32, scond: float32, amax: float32, equed: uint8` |
| `claqp2` | `None` | `m: BlasInt, n: BlasInt, offset: BlasInt, a: complex64, lda: BlasInt, jpvt: BlasInt, tau: complex64, vn1: float32, vn2: float32, work: complex64` |
| `claqps` | `None` | `m: BlasInt, n: BlasInt, offset: BlasInt, nb: BlasInt, kb: BlasInt, a: complex64, lda: BlasInt, jpvt: BlasInt, tau: complex64, vn1: float32, vn2: float32, auxv: complex64, f: complex64, ldf: BlasInt` |
| `claqr0` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex64, ldh: BlasInt, w: complex64, iloz: BlasInt, ihiz: BlasInt, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `claqr1` | `None` | `n: BlasInt, h: complex64, ldh: BlasInt, s1: complex64, s2: complex64, v: complex64` |
| `claqr2` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nw: BlasInt, h: complex64, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: complex64, ldz: BlasInt, ns: BlasInt, nd: BlasInt, sh: complex64, v: complex64, ldv: BlasInt, nh: BlasInt, t: complex64, ldt: BlasInt, nv: BlasInt, wv: complex64, ldwv: BlasInt, work: complex64, lwork: BlasInt` |
| `claqr3` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nw: BlasInt, h: complex64, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: complex64, ldz: BlasInt, ns: BlasInt, nd: BlasInt, sh: complex64, v: complex64, ldv: BlasInt, nh: BlasInt, t: complex64, ldt: BlasInt, nv: BlasInt, wv: complex64, ldwv: BlasInt, work: complex64, lwork: BlasInt` |
| `claqr4` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex64, ldh: BlasInt, w: complex64, iloz: BlasInt, ihiz: BlasInt, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `claqr5` | `None` | `wantt: bool, wantz: bool, kacc22: BlasInt, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nshfts: BlasInt, s: complex64, h: complex64, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: complex64, ldz: BlasInt, v: complex64, ldv: BlasInt, u: complex64, ldu: BlasInt, nv: BlasInt, wv: complex64, ldwv: BlasInt, nh: BlasInt, wh: complex64, ldwh: BlasInt` |
| `claqsb` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, s: float32, scond: float32, amax: float32, equed: uint8` |
| `claqsp` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, s: float32, scond: float32, amax: float32, equed: uint8` |
| `claqsy` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, s: float32, scond: float32, amax: float32, equed: uint8` |
| `clar1v` | `None` | `n: BlasInt, b1: BlasInt, bn: BlasInt, lambda_: float32, d: float32, l: float32, ld: float32, lld: float32, pivmin: float32, gaptol: float32, z: complex64, wantnc: bool, negcnt: BlasInt, ztz: float32, mingma: float32, r: BlasInt, isuppz: BlasInt, nrminv: float32, resid: float32, rqcorr: float32, work: float32` |
| `clar2v` | `None` | `n: BlasInt, x: complex64, y: complex64, z: complex64, incx: BlasInt, c: float32, s: complex64, incc: BlasInt` |
| `clarcm` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, b: complex64, ldb: BlasInt, c: complex64, ldc: BlasInt, rwork: float32` |
| `clarf` | `None` | `side: uint8, m: BlasInt, n: BlasInt, v: complex64, incv: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64` |
| `clarfb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, v: complex64, ldv: BlasInt, t: complex64, ldt: BlasInt, c: complex64, ldc: BlasInt, work: complex64, ldwork: BlasInt` |
| `clarfg` | `None` | `n: BlasInt, alpha: complex64, x: complex64, incx: BlasInt, tau: complex64` |
| `clarfgp` | `None` | `n: BlasInt, alpha: complex64, x: complex64, incx: BlasInt, tau: complex64` |
| `clarft` | `None` | `direct: uint8, storev: uint8, n: BlasInt, k: BlasInt, v: complex64, ldv: BlasInt, tau: complex64, t: complex64, ldt: BlasInt` |
| `clarfx` | `None` | `side: uint8, m: BlasInt, n: BlasInt, v: complex64, tau: complex64, c: complex64, ldc: BlasInt, work: complex64` |
| `clargv` | `None` | `n: BlasInt, x: complex64, incx: BlasInt, y: complex64, incy: BlasInt, c: float32, incc: BlasInt` |
| `clarnv` | `None` | `idist: BlasInt, iseed: BlasInt, n: BlasInt, x: complex64` |
| `clarrv` | `None` | `n: BlasInt, vl: float32, vu: float32, d: float32, l: float32, pivmin: float32, isplit: BlasInt, m: BlasInt, dol: BlasInt, dou: BlasInt, minrgp: float32, rtol1: float32, rtol2: float32, w: float32, werr: float32, wgap: float32, iblock: BlasInt, indexw: BlasInt, gers: float32, z: complex64, ldz: BlasInt, isuppz: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `clartg` | `None` | `f: complex64, g: complex64, cs: float32, sn: complex64, r: complex64` |
| `clartv` | `None` | `n: BlasInt, x: complex64, incx: BlasInt, y: complex64, incy: BlasInt, c: float32, s: complex64, incc: BlasInt` |
| `clarz` | `None` | `side: uint8, m: BlasInt, n: BlasInt, l: BlasInt, v: complex64, incv: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64` |
| `clarzb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, v: complex64, ldv: BlasInt, t: complex64, ldt: BlasInt, c: complex64, ldc: BlasInt, work: complex64, ldwork: BlasInt` |
| `clarzt` | `None` | `direct: uint8, storev: uint8, n: BlasInt, k: BlasInt, v: complex64, ldv: BlasInt, tau: complex64, t: complex64, ldt: BlasInt` |
| `clascl` | `None` | `type_bn: uint8, kl: BlasInt, ku: BlasInt, cfrom: float32, cto: float32, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, info: BlasInt` |
| `claset` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, alpha: complex64, beta: complex64, a: complex64, lda: BlasInt` |
| `clasr` | `None` | `side: uint8, pivot: uint8, direct: uint8, m: BlasInt, n: BlasInt, c: float32, s: float32, a: complex64, lda: BlasInt` |
| `classq` | `None` | `n: BlasInt, x: complex64, incx: BlasInt, scale: float32, sumsq: float32` |
| `claswp` | `None` | `n: BlasInt, a: complex64, lda: BlasInt, k1: BlasInt, k2: BlasInt, ipiv: BlasInt, incx: BlasInt` |
| `clasyf` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, kb: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, w: complex64, ldw: BlasInt, info: BlasInt` |
| `clatbs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, x: complex64, scale: float32, cnorm: float32, info: BlasInt` |
| `clatdf` | `None` | `ijob: BlasInt, n: BlasInt, z: complex64, ldz: BlasInt, rhs: complex64, rdsum: float32, rdscal: float32, ipiv: BlasInt, jpiv: BlasInt` |
| `clatps` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, ap: complex64, x: complex64, scale: float32, cnorm: float32, info: BlasInt` |
| `clatrd` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, a: complex64, lda: BlasInt, e: float32, tau: complex64, w: complex64, ldw: BlasInt` |
| `clatrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, a: complex64, lda: BlasInt, x: complex64, scale: float32, cnorm: float32, info: BlasInt` |
| `clatrz` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64` |
| `clauu2` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, info: BlasInt` |
| `clauum` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, info: BlasInt` |
| `cpbcon` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, anorm: float32, rcond: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cpbequ` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, s: float32, scond: float32, amax: float32, info: BlasInt` |
| `cpbrfs` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, afb: complex64, ldafb: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cpbstf` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, info: BlasInt` |
| `cpbsv` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cpbsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, afb: complex64, ldafb: BlasInt, equed: uint8, s: float32, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cpbtf2` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, info: BlasInt` |
| `cpbtrf` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, info: BlasInt` |
| `cpbtrs` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cpftrf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: complex64, info: BlasInt` |
| `cpftri` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: complex64, info: BlasInt` |
| `cpftrs` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cpocon` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, anorm: float32, rcond: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cpoequ` | `None` | `n: BlasInt, a: complex64, lda: BlasInt, s: float32, scond: float32, amax: float32, info: BlasInt` |
| `cpoequb` | `None` | `n: BlasInt, a: complex64, lda: BlasInt, s: float32, scond: float32, amax: float32, info: BlasInt` |
| `cporfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, af: complex64, ldaf: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cposv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cposvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, af: complex64, ldaf: BlasInt, equed: uint8, s: float32, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cpotf2` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, info: BlasInt` |
| `cpotrf` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, info: BlasInt` |
| `cpotri` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, info: BlasInt` |
| `cpotrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cppcon` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, anorm: float32, rcond: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cppequ` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, s: float32, scond: float32, amax: float32, info: BlasInt` |
| `cpprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, afp: complex64, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cppsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cppsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, afp: complex64, equed: uint8, s: float32, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cpptrf` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, info: BlasInt` |
| `cpptri` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, info: BlasInt` |
| `cpptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cpstf2` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, piv: BlasInt, rank: BlasInt, tol: float32, work: float32, info: BlasInt` |
| `cpstrf` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, piv: BlasInt, rank: BlasInt, tol: float32, work: float32, info: BlasInt` |
| `cptcon` | `None` | `n: BlasInt, d: float32, e: complex64, anorm: float32, rcond: float32, rwork: float32, info: BlasInt` |
| `cpteqr` | `None` | `compz: uint8, n: BlasInt, d: float32, e: float32, z: complex64, ldz: BlasInt, work: float32, info: BlasInt` |
| `cptrfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, d: float32, e: complex64, df: float32, ef: complex64, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cptsv` | `None` | `n: BlasInt, nrhs: BlasInt, d: float32, e: complex64, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cptsvx` | `None` | `fact: uint8, n: BlasInt, nrhs: BlasInt, d: float32, e: complex64, df: float32, ef: complex64, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cpttrf` | `None` | `n: BlasInt, d: float32, e: complex64, info: BlasInt` |
| `cpttrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, d: float32, e: complex64, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cptts2` | `None` | `iuplo: BlasInt, n: BlasInt, nrhs: BlasInt, d: float32, e: complex64, b: complex64, ldb: BlasInt` |
| `crot` | `None` | `n: BlasInt, cx: complex64, incx: BlasInt, cy: complex64, incy: BlasInt, c: float32, s: complex64` |
| `crotg` | `None` | `ca: complex64, cb: complex64, c: float32, s: complex64` |
| `cscal` | `None` | `n: BlasInt, ca: complex64, cx: complex64, incx: BlasInt` |
| `cspcon` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, ipiv: BlasInt, anorm: float32, rcond: float32, work: complex64, info: BlasInt` |
| `cspmv` | `None` | `uplo: uint8, n: BlasInt, alpha: complex64, ap: complex64, x: complex64, incx: BlasInt, beta: complex64, y: complex64, incy: BlasInt` |
| `cspr` | `None` | `uplo: uint8, n: BlasInt, alpha: complex64, x: complex64, incx: BlasInt, ap: complex64` |
| `csprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, afp: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `cspsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `cspsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, afp: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `csptrf` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, ipiv: BlasInt, info: BlasInt` |
| `csptri` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, ipiv: BlasInt, work: complex64, info: BlasInt` |
| `csptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `csrot` | `None` | `n: BlasInt, cx: complex64, incx: BlasInt, cy: complex64, incy: BlasInt, c: float32, s: float32` |
| `csrscl` | `None` | `n: BlasInt, sa: float32, sx: complex64, incx: BlasInt` |
| `csscal` | `None` | `n: BlasInt, sa: float32, cx: complex64, incx: BlasInt` |
| `cstedc` | `None` | `compz: uint8, n: BlasInt, d: float32, e: float32, z: complex64, ldz: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `cstegr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float32, e: float32, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, isuppz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `cstein` | `None` | `n: BlasInt, d: float32, e: float32, m: BlasInt, w: float32, iblock: BlasInt, isplit: BlasInt, z: complex64, ldz: BlasInt, work: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `cstemr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float32, e: float32, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, m: BlasInt, w: float32, z: complex64, ldz: BlasInt, nzc: BlasInt, isuppz: BlasInt, tryrac: bool, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `csteqr` | `None` | `compz: uint8, n: BlasInt, d: float32, e: float32, z: complex64, ldz: BlasInt, work: float32, info: BlasInt` |
| `cswap` | `None` | `n: BlasInt, cx: complex64, incx: BlasInt, cy: complex64, incy: BlasInt` |
| `csycon` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, anorm: float32, rcond: float32, work: complex64, info: BlasInt` |
| `csyconv` | `None` | `uplo: uint8, way: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, info: BlasInt` |
| `csyequb` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, s: float32, scond: float32, amax: float32, work: complex64, info: BlasInt` |
| `csymm` | `None` | `side: uint8, uplo: uint8, m: BlasInt, n: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, beta: complex64, c: complex64, ldc: BlasInt` |
| `csymv` | `None` | `uplo: uint8, n: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt, beta: complex64, y: complex64, incy: BlasInt` |
| `csyr` | `None` | `uplo: uint8, n: BlasInt, alpha: complex64, x: complex64, incx: BlasInt, a: complex64, lda: BlasInt` |
| `csyr2k` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, beta: complex64, c: complex64, ldc: BlasInt` |
| `csyrfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, af: complex64, ldaf: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `csyrk` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, beta: complex64, c: complex64, ldc: BlasInt` |
| `csysv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `csysvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, af: complex64, ldaf: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: complex64, lwork: BlasInt, rwork: float32, info: BlasInt` |
| `csyswapr` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, i1: BlasInt, i2: BlasInt` |
| `csytf2` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `csytrf` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `csytri` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, info: BlasInt` |
| `csytri2` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `csytri2x` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, work: complex64, nb: BlasInt, info: BlasInt` |
| `csytrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `csytrs2` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, ipiv: BlasInt, b: complex64, ldb: BlasInt, work: complex64, info: BlasInt` |
| `ctbcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, kd: BlasInt, ab: complex64, ldab: BlasInt, rcond: float32, work: complex64, rwork: float32, info: BlasInt` |
| `ctbmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt` |
| `ctbrfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `ctbsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt` |
| `ctbtrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex64, ldab: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `ctfsm` | `None` | `transr: uint8, side: uint8, uplo: uint8, trans: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: complex64, a: complex64, b: complex64, ldb: BlasInt` |
| `ctftri` | `None` | `transr: uint8, uplo: uint8, diag: uint8, n: BlasInt, a: complex64, info: BlasInt` |
| `ctfttp` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, arf: complex64, ap: complex64, info: BlasInt` |
| `ctfttr` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, arf: complex64, a: complex64, lda: BlasInt, info: BlasInt` |
| `ctgevc` | `None` | `side: uint8, howmny: uint8, select: bool, n: BlasInt, s: complex64, lds: BlasInt, p: complex64, ldp: BlasInt, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: complex64, rwork: float32, info: BlasInt` |
| `ctgex2` | `None` | `wantq: bool, wantz: bool, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, q: complex64, ldq: BlasInt, z: complex64, ldz: BlasInt, j1: BlasInt, info: BlasInt` |
| `ctgexc` | `None` | `wantq: bool, wantz: bool, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, q: complex64, ldq: BlasInt, z: complex64, ldz: BlasInt, ifst: BlasInt, ilst: BlasInt, info: BlasInt` |
| `ctgsen` | `None` | `ijob: BlasInt, wantq: bool, wantz: bool, select: bool, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, alpha: complex64, beta: complex64, q: complex64, ldq: BlasInt, z: complex64, ldz: BlasInt, m: BlasInt, pl: float32, pr: float32, dif: float32, work: complex64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `ctgsja` | `None` | `jobu: uint8, jobv: uint8, jobq: uint8, m: BlasInt, p: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, tola: float32, tolb: float32, alpha: float32, beta: float32, u: complex64, ldu: BlasInt, v: complex64, ldv: BlasInt, q: complex64, ldq: BlasInt, work: complex64, ncycle: BlasInt, info: BlasInt` |
| `ctgsna` | `None` | `job: uint8, howmny: uint8, select: bool, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, s: float32, dif: float32, mm: BlasInt, m: BlasInt, work: complex64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `ctgsy2` | `None` | `trans: uint8, ijob: BlasInt, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, c: complex64, ldc: BlasInt, d: complex64, ldd: BlasInt, e: complex64, lde: BlasInt, f: complex64, ldf: BlasInt, scale: float32, rdsum: float32, rdscal: float32, info: BlasInt` |
| `ctgsyl` | `None` | `trans: uint8, ijob: BlasInt, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, c: complex64, ldc: BlasInt, d: complex64, ldd: BlasInt, e: complex64, lde: BlasInt, f: complex64, ldf: BlasInt, scale: float32, dif: float32, work: complex64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `ctpcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, ap: complex64, rcond: float32, work: complex64, rwork: float32, info: BlasInt` |
| `ctpmqrt` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, nb: BlasInt, v: complex64, ldv: BlasInt, t: complex64, ldt: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, work: complex64, info: BlasInt` |
| `ctpmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, ap: complex64, x: complex64, incx: BlasInt` |
| `ctpqrt` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, nb: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, t: complex64, ldt: BlasInt, work: complex64, info: BlasInt` |
| `ctpqrt2` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, t: complex64, ldt: BlasInt, info: BlasInt` |
| `ctprfb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, v: complex64, ldv: BlasInt, t: complex64, ldt: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, work: complex64, ldwork: BlasInt` |
| `ctprfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `ctpsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, ap: complex64, x: complex64, incx: BlasInt` |
| `ctptri` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, ap: complex64, info: BlasInt` |
| `ctptrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, ap: complex64, b: complex64, ldb: BlasInt, info: BlasInt` |
| `ctpttf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, ap: complex64, arf: complex64, info: BlasInt` |
| `ctpttr` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, a: complex64, lda: BlasInt, info: BlasInt` |
| `ctrcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, a: complex64, lda: BlasInt, rcond: float32, work: complex64, rwork: float32, info: BlasInt` |
| `ctrevc` | `None` | `side: uint8, howmny: uint8, select: bool, n: BlasInt, t: complex64, ldt: BlasInt, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: complex64, rwork: float32, info: BlasInt` |
| `ctrexc` | `None` | `compq: uint8, n: BlasInt, t: complex64, ldt: BlasInt, q: complex64, ldq: BlasInt, ifst: BlasInt, ilst: BlasInt, info: BlasInt` |
| `ctrmm` | `None` | `side: uint8, uplo: uint8, transa: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt` |
| `ctrmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt` |
| `ctrrfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, x: complex64, ldx: BlasInt, ferr: float32, berr: float32, work: complex64, rwork: float32, info: BlasInt` |
| `ctrsen` | `None` | `job: uint8, compq: uint8, select: bool, n: BlasInt, t: complex64, ldt: BlasInt, q: complex64, ldq: BlasInt, w: complex64, m: BlasInt, s: float32, sep: float32, work: complex64, lwork: BlasInt, info: BlasInt` |
| `ctrsm` | `None` | `side: uint8, uplo: uint8, transa: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: complex64, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt` |
| `ctrsna` | `None` | `job: uint8, howmny: uint8, select: bool, n: BlasInt, t: complex64, ldt: BlasInt, vl: complex64, ldvl: BlasInt, vr: complex64, ldvr: BlasInt, s: float32, sep: float32, mm: BlasInt, m: BlasInt, work: complex64, ldwork: BlasInt, rwork: float32, info: BlasInt` |
| `ctrsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, a: complex64, lda: BlasInt, x: complex64, incx: BlasInt` |
| `ctrsyl` | `None` | `trana: uint8, tranb: uint8, isgn: BlasInt, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, c: complex64, ldc: BlasInt, scale: float32, info: BlasInt` |
| `ctrti2` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, a: complex64, lda: BlasInt, info: BlasInt` |
| `ctrtri` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, a: complex64, lda: BlasInt, info: BlasInt` |
| `ctrtrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, a: complex64, lda: BlasInt, b: complex64, ldb: BlasInt, info: BlasInt` |
| `ctrttf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, arf: complex64, info: BlasInt` |
| `ctrttp` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, ap: complex64, info: BlasInt` |
| `ctzrzf` | `None` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunbdb` | `None` | `trans: uint8, signs: uint8, m: BlasInt, p: BlasInt, q: BlasInt, x11: complex64, ldx11: BlasInt, x12: complex64, ldx12: BlasInt, x21: complex64, ldx21: BlasInt, x22: complex64, ldx22: BlasInt, theta: float32, phi: float32, taup1: complex64, taup2: complex64, tauq1: complex64, tauq2: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cuncsd` | `None` | `jobu1: uint8, jobu2: uint8, jobv1t: uint8, jobv2t: uint8, trans: uint8, signs: uint8, m: BlasInt, p: BlasInt, q: BlasInt, x11: complex64, ldx11: BlasInt, x12: complex64, ldx12: BlasInt, x21: complex64, ldx21: BlasInt, x22: complex64, ldx22: BlasInt, theta: float32, u1: complex64, ldu1: BlasInt, u2: complex64, ldu2: BlasInt, v1t: complex64, ldv1t: BlasInt, v2t: complex64, ldv2t: BlasInt, work: complex64, lwork: BlasInt, rwork: float32, lrwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `cung2l` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cung2r` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cungbr` | `None` | `vect: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunghr` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cungl2` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cunglq` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cungql` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cungqr` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cungr2` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, info: BlasInt` |
| `cungrq` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cungtr` | `None` | `uplo: uint8, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunm2l` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, info: BlasInt` |
| `cunm2r` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, info: BlasInt` |
| `cunmbr` | `None` | `vect: uint8, side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunmhr` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunml2` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, info: BlasInt` |
| `cunmlq` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunmql` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunmqr` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunmr2` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, info: BlasInt` |
| `cunmr3` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, info: BlasInt` |
| `cunmrq` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunmrz` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cunmtr` | `None` | `side: uint8, uplo: uint8, trans: uint8, m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, lwork: BlasInt, info: BlasInt` |
| `cupgtr` | `None` | `uplo: uint8, n: BlasInt, ap: complex64, tau: complex64, q: complex64, ldq: BlasInt, work: complex64, info: BlasInt` |
| `cupmtr` | `None` | `side: uint8, uplo: uint8, trans: uint8, m: BlasInt, n: BlasInt, ap: complex64, tau: complex64, c: complex64, ldc: BlasInt, work: complex64, info: BlasInt` |
| `dasum` | `np.float64` | `n: BlasInt, dx: float64, incx: BlasInt` |
| `daxpy` | `None` | `n: BlasInt, da: float64, dx: float64, incx: BlasInt, dy: float64, incy: BlasInt` |
| `dbbcsd` | `None` | `jobu1: uint8, jobu2: uint8, jobv1t: uint8, jobv2t: uint8, trans: uint8, m: BlasInt, p: BlasInt, q: BlasInt, theta: float64, phi: float64, u1: float64, ldu1: BlasInt, u2: float64, ldu2: BlasInt, v1t: float64, ldv1t: BlasInt, v2t: float64, ldv2t: BlasInt, b11d: float64, b11e: float64, b12d: float64, b12e: float64, b21d: float64, b21e: float64, b22d: float64, b22e: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dbdsdc` | `None` | `uplo: uint8, compq: uint8, n: BlasInt, d: float64, e: float64, u: float64, ldu: BlasInt, vt: float64, ldvt: BlasInt, q: float64, iq: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `dbdsqr` | `None` | `uplo: uint8, n: BlasInt, ncvt: BlasInt, nru: BlasInt, ncc: BlasInt, d: float64, e: float64, vt: float64, ldvt: BlasInt, u: float64, ldu: BlasInt, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dcabs1` | `np.float64` | `z: complex128` |
| `dcopy` | `None` | `n: BlasInt, dx: float64, incx: BlasInt, dy: float64, incy: BlasInt` |
| `ddisna` | `None` | `job: uint8, m: BlasInt, n: BlasInt, d: float64, sep: float64, info: BlasInt` |
| `ddot` | `np.float64` | `n: BlasInt, dx: float64, incx: BlasInt, dy: float64, incy: BlasInt` |
| `dgbbrd` | `None` | `vect: uint8, m: BlasInt, n: BlasInt, ncc: BlasInt, kl: BlasInt, ku: BlasInt, ab: float64, ldab: BlasInt, d: float64, e: float64, q: float64, ldq: BlasInt, pt: float64, ldpt: BlasInt, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dgbcon` | `None` | `norm: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float64, ldab: BlasInt, ipiv: BlasInt, anorm: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgbequ` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float64, ldab: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, info: BlasInt` |
| `dgbequb` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float64, ldab: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, info: BlasInt` |
| `dgbmv` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, alpha: float64, a: float64, lda: BlasInt, x: float64, incx: BlasInt, beta: float64, y: float64, incy: BlasInt` |
| `dgbrfs` | `None` | `trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, afb: float64, ldafb: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgbsv` | `None` | `n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dgbsvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, afb: float64, ldafb: BlasInt, ipiv: BlasInt, equed: uint8, r: float64, c: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgbtf2` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float64, ldab: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `dgbtrf` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float64, ldab: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `dgbtrs` | `None` | `trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dgebak` | `None` | `job: uint8, side: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float64, m: BlasInt, v: float64, ldv: BlasInt, info: BlasInt` |
| `dgebal` | `None` | `job: uint8, n: BlasInt, a: float64, lda: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float64, info: BlasInt` |
| `dgebd2` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, d: float64, e: float64, tauq: float64, taup: float64, work: float64, info: BlasInt` |
| `dgebrd` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, d: float64, e: float64, tauq: float64, taup: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgecon` | `None` | `norm: uint8, n: BlasInt, a: float64, lda: BlasInt, anorm: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgeequ` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, info: BlasInt` |
| `dgeequb` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, info: BlasInt` |
| `dgeev` | `None` | `jobvl: uint8, jobvr: uint8, n: BlasInt, a: float64, lda: BlasInt, wr: float64, wi: float64, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgeevx` | `None` | `balanc: uint8, jobvl: uint8, jobvr: uint8, sense: uint8, n: BlasInt, a: float64, lda: BlasInt, wr: float64, wi: float64, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float64, abnrm: float64, rconde: float64, rcondv: float64, work: float64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dgehd2` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dgehrd` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgejsv` | `None` | `joba: uint8, jobu: uint8, jobv: uint8, jobr: uint8, jobt: uint8, jobp: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, sva: float64, u: float64, ldu: BlasInt, v: float64, ldv: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dgelq2` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dgelqf` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgels` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgelsd` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, s: float64, rcond: float64, rank: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dgelss` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, s: float64, rcond: float64, rank: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgelsy` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, jpvt: BlasInt, rcond: float64, rank: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgemm` | `None` | `transa: uint8, transb: uint8, m: BlasInt, n: BlasInt, k: BlasInt, alpha: float64, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, beta: float64, c: float64, ldc: BlasInt` |
| `dgemqrt` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, nb: BlasInt, v: float64, ldv: BlasInt, t: float64, ldt: BlasInt, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dgemv` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, alpha: float64, a: float64, lda: BlasInt, x: float64, incx: BlasInt, beta: float64, y: float64, incy: BlasInt` |
| `dgeql2` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dgeqlf` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgeqp3` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, jpvt: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgeqr2` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dgeqr2p` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dgeqrf` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgeqrfp` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgeqrt` | `None` | `m: BlasInt, n: BlasInt, nb: BlasInt, a: float64, lda: BlasInt, t: float64, ldt: BlasInt, work: float64, info: BlasInt` |
| `dgeqrt2` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, t: float64, ldt: BlasInt, info: BlasInt` |
| `dgeqrt3` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, t: float64, ldt: BlasInt, info: BlasInt` |
| `dger` | `None` | `m: BlasInt, n: BlasInt, alpha: float64, x: float64, incx: BlasInt, y: float64, incy: BlasInt, a: float64, lda: BlasInt` |
| `dgerfs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, af: float64, ldaf: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgerq2` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dgerqf` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgesc2` | `None` | `n: BlasInt, a: float64, lda: BlasInt, rhs: float64, ipiv: BlasInt, jpiv: BlasInt, scale: float64` |
| `dgesdd` | `None` | `jobz: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, s: float64, u: float64, ldu: BlasInt, vt: float64, ldvt: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dgesv` | `None` | `n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dgesvd` | `None` | `jobu: uint8, jobvt: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, s: float64, u: float64, ldu: BlasInt, vt: float64, ldvt: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgesvj` | `None` | `joba: uint8, jobu: uint8, jobv: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, sva: float64, mv: BlasInt, v: float64, ldv: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgesvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, af: float64, ldaf: BlasInt, ipiv: BlasInt, equed: uint8, r: float64, c: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgetc2` | `None` | `n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, jpiv: BlasInt, info: BlasInt` |
| `dgetf2` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `dgetrf` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `dgetri` | `None` | `n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgetrs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dggbak` | `None` | `job: uint8, side: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float64, rscale: float64, m: BlasInt, v: float64, ldv: BlasInt, info: BlasInt` |
| `dggbal` | `None` | `job: uint8, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float64, rscale: float64, work: float64, info: BlasInt` |
| `dggev` | `None` | `jobvl: uint8, jobvr: uint8, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, alphar: float64, alphai: float64, beta: float64, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dggevx` | `None` | `balanc: uint8, jobvl: uint8, jobvr: uint8, sense: uint8, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, alphar: float64, alphai: float64, beta: float64, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float64, rscale: float64, abnrm: float64, bbnrm: float64, rconde: float64, rcondv: float64, work: float64, lwork: BlasInt, iwork: BlasInt, bwork: bool, info: BlasInt` |
| `dggglm` | `None` | `n: BlasInt, m: BlasInt, p: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, d: float64, x: float64, y: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgghrd` | `None` | `compq: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, q: float64, ldq: BlasInt, z: float64, ldz: BlasInt, info: BlasInt` |
| `dgglse` | `None` | `m: BlasInt, n: BlasInt, p: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, c: float64, d: float64, x: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dggqrf` | `None` | `n: BlasInt, m: BlasInt, p: BlasInt, a: float64, lda: BlasInt, taua: float64, b: float64, ldb: BlasInt, taub: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dggrqf` | `None` | `m: BlasInt, p: BlasInt, n: BlasInt, a: float64, lda: BlasInt, taua: float64, b: float64, ldb: BlasInt, taub: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgsvj0` | `None` | `jobv: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, d: float64, sva: float64, mv: BlasInt, v: float64, ldv: BlasInt, eps: float64, sfmin: float64, tol: float64, nsweep: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgsvj1` | `None` | `jobv: uint8, m: BlasInt, n: BlasInt, n1: BlasInt, a: float64, lda: BlasInt, d: float64, sva: float64, mv: BlasInt, v: float64, ldv: BlasInt, eps: float64, sfmin: float64, tol: float64, nsweep: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dgtcon` | `None` | `norm: uint8, n: BlasInt, dl: float64, d: float64, du: float64, du2: float64, ipiv: BlasInt, anorm: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgtrfs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, dl: float64, d: float64, du: float64, dlf: float64, df: float64, duf: float64, du2: float64, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgtsv` | `None` | `n: BlasInt, nrhs: BlasInt, dl: float64, d: float64, du: float64, b: float64, ldb: BlasInt, info: BlasInt` |
| `dgtsvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, nrhs: BlasInt, dl: float64, d: float64, du: float64, dlf: float64, df: float64, duf: float64, du2: float64, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dgttrf` | `None` | `n: BlasInt, dl: float64, d: float64, du: float64, du2: float64, ipiv: BlasInt, info: BlasInt` |
| `dgttrs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, dl: float64, d: float64, du: float64, du2: float64, ipiv: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dgtts2` | `None` | `itrans: BlasInt, n: BlasInt, nrhs: BlasInt, dl: float64, d: float64, du: float64, du2: float64, ipiv: BlasInt, b: float64, ldb: BlasInt` |
| `dhgeqz` | `None` | `job: uint8, compq: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float64, ldh: BlasInt, t: float64, ldt: BlasInt, alphar: float64, alphai: float64, beta: float64, q: float64, ldq: BlasInt, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dhsein` | `None` | `side: uint8, eigsrc: uint8, initv: uint8, select: bool, n: BlasInt, h: float64, ldh: BlasInt, wr: float64, wi: float64, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: float64, ifaill: BlasInt, ifailr: BlasInt, info: BlasInt` |
| `dhseqr` | `None` | `job: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float64, ldh: BlasInt, wr: float64, wi: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `disnan` | `bool` | `din: float64` |
| `dlabad` | `None` | `small: float64, large: float64` |
| `dlabrd` | `None` | `m: BlasInt, n: BlasInt, nb: BlasInt, a: float64, lda: BlasInt, d: float64, e: float64, tauq: float64, taup: float64, x: float64, ldx: BlasInt, y: float64, ldy: BlasInt` |
| `dlacn2` | `None` | `n: BlasInt, v: float64, x: float64, isgn: BlasInt, est: float64, kase: BlasInt, isave: BlasInt` |
| `dlacon` | `None` | `n: BlasInt, v: float64, x: float64, isgn: BlasInt, est: float64, kase: BlasInt` |
| `dlacpy` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt` |
| `dladiv` | `None` | `a: float64, b: float64, c: float64, d: float64, p: float64, q: float64` |
| `dlae2` | `None` | `a: float64, b: float64, c: float64, rt1: float64, rt2: float64` |
| `dlaebz` | `None` | `ijob: BlasInt, nitmax: BlasInt, n: BlasInt, mmax: BlasInt, minp: BlasInt, nbmin: BlasInt, abstol: float64, reltol: float64, pivmin: float64, d: float64, e: float64, e2: float64, nval: BlasInt, ab: float64, c: float64, mout: BlasInt, nab: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlaed0` | `None` | `icompq: BlasInt, qsiz: BlasInt, n: BlasInt, d: float64, e: float64, q: float64, ldq: BlasInt, qstore: float64, ldqs: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlaed1` | `None` | `n: BlasInt, d: float64, q: float64, ldq: BlasInt, indxq: BlasInt, rho: float64, cutpnt: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlaed2` | `None` | `k: BlasInt, n: BlasInt, n1: BlasInt, d: float64, q: float64, ldq: BlasInt, indxq: BlasInt, rho: float64, z: float64, dlamda: float64, w: float64, q2: float64, indx: BlasInt, indxc: BlasInt, indxp: BlasInt, coltyp: BlasInt, info: BlasInt` |
| `dlaed3` | `None` | `k: BlasInt, n: BlasInt, n1: BlasInt, d: float64, q: float64, ldq: BlasInt, rho: float64, dlamda: float64, q2: float64, indx: BlasInt, ctot: BlasInt, w: float64, s: float64, info: BlasInt` |
| `dlaed4` | `None` | `n: BlasInt, i: BlasInt, d: float64, z: float64, delta: float64, rho: float64, dlam: float64, info: BlasInt` |
| `dlaed5` | `None` | `i: BlasInt, d: float64, z: float64, delta: float64, rho: float64, dlam: float64` |
| `dlaed6` | `None` | `kniter: BlasInt, orgati: bool, rho: float64, d: float64, z: float64, finit: float64, tau: float64, info: BlasInt` |
| `dlaed7` | `None` | `icompq: BlasInt, n: BlasInt, qsiz: BlasInt, tlvls: BlasInt, curlvl: BlasInt, curpbm: BlasInt, d: float64, q: float64, ldq: BlasInt, indxq: BlasInt, rho: float64, cutpnt: BlasInt, qstore: float64, qptr: BlasInt, prmptr: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlaed8` | `None` | `icompq: BlasInt, k: BlasInt, n: BlasInt, qsiz: BlasInt, d: float64, q: float64, ldq: BlasInt, indxq: BlasInt, rho: float64, cutpnt: BlasInt, z: float64, dlamda: float64, q2: float64, ldq2: BlasInt, w: float64, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float64, indxp: BlasInt, indx: BlasInt, info: BlasInt` |
| `dlaed9` | `None` | `k: BlasInt, kstart: BlasInt, kstop: BlasInt, n: BlasInt, d: float64, q: float64, ldq: BlasInt, rho: float64, dlamda: float64, w: float64, s: float64, lds: BlasInt, info: BlasInt` |
| `dlaeda` | `None` | `n: BlasInt, tlvls: BlasInt, curlvl: BlasInt, curpbm: BlasInt, prmptr: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float64, q: float64, qptr: BlasInt, z: float64, ztemp: float64, info: BlasInt` |
| `dlaein` | `None` | `rightv: bool, noinit: bool, n: BlasInt, h: float64, ldh: BlasInt, wr: float64, wi: float64, vr: float64, vi: float64, b: float64, ldb: BlasInt, work: float64, eps3: float64, smlnum: float64, bignum: float64, info: BlasInt` |
| `dlaev2` | `None` | `a: float64, b: float64, c: float64, rt1: float64, rt2: float64, cs1: float64, sn1: float64` |
| `dlaexc` | `None` | `wantq: bool, n: BlasInt, t: float64, ldt: BlasInt, q: float64, ldq: BlasInt, j1: BlasInt, n1: BlasInt, n2: BlasInt, work: float64, info: BlasInt` |
| `dlag2` | `None` | `a: float64, lda: BlasInt, b: float64, ldb: BlasInt, safmin: float64, scale1: float64, scale2: float64, wr1: float64, wr2: float64, wi: float64` |
| `dlag2s` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, sa: float32, ldsa: BlasInt, info: BlasInt` |
| `dlags2` | `None` | `upper: bool, a1: float64, a2: float64, a3: float64, b1: float64, b2: float64, b3: float64, csu: float64, snu: float64, csv: float64, snv: float64, csq: float64, snq: float64` |
| `dlagtf` | `None` | `n: BlasInt, a: float64, lambda_: float64, b: float64, c: float64, tol: float64, d: float64, in_: BlasInt, info: BlasInt` |
| `dlagtm` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, alpha: float64, dl: float64, d: float64, du: float64, x: float64, ldx: BlasInt, beta: float64, b: float64, ldb: BlasInt` |
| `dlagts` | `None` | `job: BlasInt, n: BlasInt, a: float64, b: float64, c: float64, d: float64, in_: BlasInt, y: float64, tol: float64, info: BlasInt` |
| `dlagv2` | `None` | `a: float64, lda: BlasInt, b: float64, ldb: BlasInt, alphar: float64, alphai: float64, beta: float64, csl: float64, snl: float64, csr: float64, snr: float64` |
| `dlahqr` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float64, ldh: BlasInt, wr: float64, wi: float64, iloz: BlasInt, ihiz: BlasInt, z: float64, ldz: BlasInt, info: BlasInt` |
| `dlahr2` | `None` | `n: BlasInt, k: BlasInt, nb: BlasInt, a: float64, lda: BlasInt, tau: float64, t: float64, ldt: BlasInt, y: float64, ldy: BlasInt` |
| `dlaic1` | `None` | `job: BlasInt, j: BlasInt, x: float64, sest: float64, w: float64, gamma: float64, sestpr: float64, s: float64, c: float64` |
| `dlaln2` | `None` | `ltrans: bool, na: BlasInt, nw: BlasInt, smin: float64, ca: float64, a: float64, lda: BlasInt, d1: float64, d2: float64, b: float64, ldb: BlasInt, wr: float64, wi: float64, x: float64, ldx: BlasInt, scale: float64, xnorm: float64, info: BlasInt` |
| `dlals0` | `None` | `icompq: BlasInt, nl: BlasInt, nr: BlasInt, sqre: BlasInt, nrhs: BlasInt, b: float64, ldb: BlasInt, bx: float64, ldbx: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, givnum: float64, ldgnum: BlasInt, poles: float64, difl: float64, difr: float64, z: float64, k: BlasInt, c: float64, s: float64, work: float64, info: BlasInt` |
| `dlalsa` | `None` | `icompq: BlasInt, smlsiz: BlasInt, n: BlasInt, nrhs: BlasInt, b: float64, ldb: BlasInt, bx: float64, ldbx: BlasInt, u: float64, ldu: BlasInt, vt: float64, k: BlasInt, difl: float64, difr: float64, z: float64, poles: float64, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, perm: BlasInt, givnum: float64, c: float64, s: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlalsd` | `None` | `uplo: uint8, smlsiz: BlasInt, n: BlasInt, nrhs: BlasInt, d: float64, e: float64, b: float64, ldb: BlasInt, rcond: float64, rank: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlamch` | `np.float64` | `cmach: uint8` |
| `dlamrg` | `None` | `n1: BlasInt, n2: BlasInt, a: float64, dtrd1: BlasInt, dtrd2: BlasInt, index_bn: BlasInt` |
| `dlaneg` | `BlasInt` | `n: BlasInt, d: float64, lld: float64, sigma: float64, pivmin: float64, r: BlasInt` |
| `dlangb` | `np.float64` | `norm: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float64, ldab: BlasInt, work: float64` |
| `dlange` | `np.float64` | `norm: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, work: float64` |
| `dlangt` | `np.float64` | `norm: uint8, n: BlasInt, dl: float64, d_: float64, du: float64` |
| `dlanhs` | `np.float64` | `norm: uint8, n: BlasInt, a: float64, lda: BlasInt, work: float64` |
| `dlansb` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, k: BlasInt, ab: float64, ldab: BlasInt, work: float64` |
| `dlansf` | `np.float64` | `norm: uint8, transr: uint8, uplo: uint8, n: BlasInt, a: float64, work: float64` |
| `dlansp` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, ap: float64, work: float64` |
| `dlanst` | `np.float64` | `norm: uint8, n: BlasInt, d_: float64, e: float64` |
| `dlansy` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, work: float64` |
| `dlantb` | `np.float64` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, k: BlasInt, ab: float64, ldab: BlasInt, work: float64` |
| `dlantp` | `np.float64` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, ap: float64, work: float64` |
| `dlantr` | `np.float64` | `norm: uint8, uplo: uint8, diag: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, work: float64` |
| `dlanv2` | `None` | `a: float64, b: float64, c: float64, d: float64, rt1r: float64, rt1i: float64, rt2r: float64, rt2i: float64, cs: float64, sn: float64` |
| `dlapll` | `None` | `n: BlasInt, x: float64, incx: BlasInt, y: float64, incy: BlasInt, ssmin: float64` |
| `dlapmr` | `None` | `forwrd: bool, m: BlasInt, n: BlasInt, x: float64, ldx: BlasInt, k: BlasInt` |
| `dlapmt` | `None` | `forwrd: bool, m: BlasInt, n: BlasInt, x: float64, ldx: BlasInt, k: BlasInt` |
| `dlapy2` | `np.float64` | `x: float64, y: float64` |
| `dlapy3` | `np.float64` | `x: float64, y: float64, z: float64` |
| `dlaqgb` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float64, ldab: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, equed: uint8` |
| `dlaqge` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, equed: uint8` |
| `dlaqp2` | `None` | `m: BlasInt, n: BlasInt, offset: BlasInt, a: float64, lda: BlasInt, jpvt: BlasInt, tau: float64, vn1: float64, vn2: float64, work: float64` |
| `dlaqps` | `None` | `m: BlasInt, n: BlasInt, offset: BlasInt, nb: BlasInt, kb: BlasInt, a: float64, lda: BlasInt, jpvt: BlasInt, tau: float64, vn1: float64, vn2: float64, auxv: float64, f: float64, ldf: BlasInt` |
| `dlaqr0` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float64, ldh: BlasInt, wr: float64, wi: float64, iloz: BlasInt, ihiz: BlasInt, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dlaqr1` | `None` | `n: BlasInt, h: float64, ldh: BlasInt, sr1: float64, si1: float64, sr2: float64, si2: float64, v: float64` |
| `dlaqr2` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nw: BlasInt, h: float64, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: float64, ldz: BlasInt, ns: BlasInt, nd: BlasInt, sr: float64, si: float64, v: float64, ldv: BlasInt, nh: BlasInt, t: float64, ldt: BlasInt, nv: BlasInt, wv: float64, ldwv: BlasInt, work: float64, lwork: BlasInt` |
| `dlaqr3` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nw: BlasInt, h: float64, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: float64, ldz: BlasInt, ns: BlasInt, nd: BlasInt, sr: float64, si: float64, v: float64, ldv: BlasInt, nh: BlasInt, t: float64, ldt: BlasInt, nv: BlasInt, wv: float64, ldwv: BlasInt, work: float64, lwork: BlasInt` |
| `dlaqr4` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float64, ldh: BlasInt, wr: float64, wi: float64, iloz: BlasInt, ihiz: BlasInt, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dlaqr5` | `None` | `wantt: bool, wantz: bool, kacc22: BlasInt, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nshfts: BlasInt, sr: float64, si: float64, h: float64, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: float64, ldz: BlasInt, v: float64, ldv: BlasInt, u: float64, ldu: BlasInt, nv: BlasInt, wv: float64, ldwv: BlasInt, nh: BlasInt, wh: float64, ldwh: BlasInt` |
| `dlaqsb` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, s: float64, scond: float64, amax: float64, equed: uint8` |
| `dlaqsp` | `None` | `uplo: uint8, n: BlasInt, ap: float64, s: float64, scond: float64, amax: float64, equed: uint8` |
| `dlaqsy` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, s: float64, scond: float64, amax: float64, equed: uint8` |
| `dlaqtr` | `None` | `ltran: bool, lreal: bool, n: BlasInt, t: float64, ldt: BlasInt, b: float64, w: float64, scale: float64, x: float64, work: float64, info: BlasInt` |
| `dlar1v` | `None` | `n: BlasInt, b1: BlasInt, bn: BlasInt, lambda_: float64, d: float64, l: float64, ld: float64, lld: float64, pivmin: float64, gaptol: float64, z: float64, wantnc: bool, negcnt: BlasInt, ztz: float64, mingma: float64, r: BlasInt, isuppz: BlasInt, nrminv: float64, resid: float64, rqcorr: float64, work: float64` |
| `dlar2v` | `None` | `n: BlasInt, x: float64, y: float64, z: float64, incx: BlasInt, c: float64, s: float64, incc: BlasInt` |
| `dlarf` | `None` | `side: uint8, m: BlasInt, n: BlasInt, v: float64, incv: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64` |
| `dlarfb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, v: float64, ldv: BlasInt, t: float64, ldt: BlasInt, c: float64, ldc: BlasInt, work: float64, ldwork: BlasInt` |
| `dlarfg` | `None` | `n: BlasInt, alpha: float64, x: float64, incx: BlasInt, tau: float64` |
| `dlarfgp` | `None` | `n: BlasInt, alpha: float64, x: float64, incx: BlasInt, tau: float64` |
| `dlarft` | `None` | `direct: uint8, storev: uint8, n: BlasInt, k: BlasInt, v: float64, ldv: BlasInt, tau: float64, t: float64, ldt: BlasInt` |
| `dlarfx` | `None` | `side: uint8, m: BlasInt, n: BlasInt, v: float64, tau: float64, c: float64, ldc: BlasInt, work: float64` |
| `dlargv` | `None` | `n: BlasInt, x: float64, incx: BlasInt, y: float64, incy: BlasInt, c: float64, incc: BlasInt` |
| `dlarnv` | `None` | `idist: BlasInt, iseed: BlasInt, n: BlasInt, x: float64` |
| `dlarra` | `None` | `n: BlasInt, d: float64, e: float64, e2: float64, spltol: float64, tnrm: float64, nsplit: BlasInt, isplit: BlasInt, info: BlasInt` |
| `dlarrb` | `None` | `n: BlasInt, d: float64, lld: float64, ifirst: BlasInt, ilast: BlasInt, rtol1: float64, rtol2: float64, offset: BlasInt, w: float64, wgap: float64, werr: float64, work: float64, iwork: BlasInt, pivmin: float64, spdiam: float64, twist: BlasInt, info: BlasInt` |
| `dlarrc` | `None` | `jobt: uint8, n: BlasInt, vl: float64, vu: float64, d: float64, e: float64, pivmin: float64, eigcnt: BlasInt, lcnt: BlasInt, rcnt: BlasInt, info: BlasInt` |
| `dlarrd` | `None` | `range: uint8, order: uint8, n: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, gers: float64, reltol: float64, d: float64, e: float64, e2: float64, pivmin: float64, nsplit: BlasInt, isplit: BlasInt, m: BlasInt, w: float64, werr: float64, wl: float64, wu: float64, iblock: BlasInt, indexw: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlarre` | `None` | `range: uint8, n: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, d: float64, e: float64, e2: float64, rtol1: float64, rtol2: float64, spltol: float64, nsplit: BlasInt, isplit: BlasInt, m: BlasInt, w: float64, werr: float64, wgap: float64, iblock: BlasInt, indexw: BlasInt, gers: float64, pivmin: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlarrf` | `None` | `n: BlasInt, d: float64, l: float64, ld: float64, clstrt: BlasInt, clend: BlasInt, w: float64, wgap: float64, werr: float64, spdiam: float64, clgapl: float64, clgapr: float64, pivmin: float64, sigma: float64, dplus: float64, lplus: float64, work: float64, info: BlasInt` |
| `dlarrj` | `None` | `n: BlasInt, d: float64, e2: float64, ifirst: BlasInt, ilast: BlasInt, rtol: float64, offset: BlasInt, w: float64, werr: float64, work: float64, iwork: BlasInt, pivmin: float64, spdiam: float64, info: BlasInt` |
| `dlarrk` | `None` | `n: BlasInt, iw: BlasInt, gl: float64, gu: float64, d: float64, e2: float64, pivmin: float64, reltol: float64, w: float64, werr: float64, info: BlasInt` |
| `dlarrr` | `None` | `n: BlasInt, d: float64, e: float64, info: BlasInt` |
| `dlarrv` | `None` | `n: BlasInt, vl: float64, vu: float64, d: float64, l: float64, pivmin: float64, isplit: BlasInt, m: BlasInt, dol: BlasInt, dou: BlasInt, minrgp: float64, rtol1: float64, rtol2: float64, w: float64, werr: float64, wgap: float64, iblock: BlasInt, indexw: BlasInt, gers: float64, z: float64, ldz: BlasInt, isuppz: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlartg` | `None` | `f: float64, g: float64, cs: float64, sn: float64, r: float64` |
| `dlartgp` | `None` | `f: float64, g: float64, cs: float64, sn: float64, r: float64` |
| `dlartgs` | `None` | `x: float64, y: float64, sigma: float64, cs: float64, sn: float64` |
| `dlartv` | `None` | `n: BlasInt, x: float64, incx: BlasInt, y: float64, incy: BlasInt, c: float64, s: float64, incc: BlasInt` |
| `dlaruv` | `None` | `iseed: BlasInt, n: BlasInt, x: float64` |
| `dlarz` | `None` | `side: uint8, m: BlasInt, n: BlasInt, l: BlasInt, v: float64, incv: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64` |
| `dlarzb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, v: float64, ldv: BlasInt, t: float64, ldt: BlasInt, c: float64, ldc: BlasInt, work: float64, ldwork: BlasInt` |
| `dlarzt` | `None` | `direct: uint8, storev: uint8, n: BlasInt, k: BlasInt, v: float64, ldv: BlasInt, tau: float64, t: float64, ldt: BlasInt` |
| `dlas2` | `None` | `f: float64, g: float64, h: float64, ssmin: float64, ssmax: float64` |
| `dlascl` | `None` | `type_bn: uint8, kl: BlasInt, ku: BlasInt, cfrom: float64, cto: float64, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `dlasd0` | `None` | `n: BlasInt, sqre: BlasInt, d: float64, e: float64, u: float64, ldu: BlasInt, vt: float64, ldvt: BlasInt, smlsiz: BlasInt, iwork: BlasInt, work: float64, info: BlasInt` |
| `dlasd1` | `None` | `nl: BlasInt, nr: BlasInt, sqre: BlasInt, d: float64, alpha: float64, beta: float64, u: float64, ldu: BlasInt, vt: float64, ldvt: BlasInt, idxq: BlasInt, iwork: BlasInt, work: float64, info: BlasInt` |
| `dlasd2` | `None` | `nl: BlasInt, nr: BlasInt, sqre: BlasInt, k: BlasInt, d: float64, z: float64, alpha: float64, beta: float64, u: float64, ldu: BlasInt, vt: float64, ldvt: BlasInt, dsigma: float64, u2: float64, ldu2: BlasInt, vt2: float64, ldvt2: BlasInt, idxp: BlasInt, idx: BlasInt, idxc: BlasInt, idxq: BlasInt, coltyp: BlasInt, info: BlasInt` |
| `dlasd3` | `None` | `nl: BlasInt, nr: BlasInt, sqre: BlasInt, k: BlasInt, d: float64, q: float64, ldq: BlasInt, dsigma: float64, u: float64, ldu: BlasInt, u2: float64, ldu2: BlasInt, vt: float64, ldvt: BlasInt, vt2: float64, ldvt2: BlasInt, idxc: BlasInt, ctot: BlasInt, z: float64, info: BlasInt` |
| `dlasd4` | `None` | `n: BlasInt, i: BlasInt, d: float64, z: float64, delta: float64, rho: float64, sigma: float64, work: float64, info: BlasInt` |
| `dlasd5` | `None` | `i: BlasInt, d: float64, z: float64, delta: float64, rho: float64, dsigma: float64, work: float64` |
| `dlasd6` | `None` | `icompq: BlasInt, nl: BlasInt, nr: BlasInt, sqre: BlasInt, d: float64, vf: float64, vl: float64, alpha: float64, beta: float64, idxq: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, givnum: float64, ldgnum: BlasInt, poles: float64, difl: float64, difr: float64, z: float64, k: BlasInt, c: float64, s: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlasd7` | `None` | `icompq: BlasInt, nl: BlasInt, nr: BlasInt, sqre: BlasInt, k: BlasInt, d: float64, z: float64, zw: float64, vf: float64, vfw: float64, vl: float64, vlw: float64, alpha: float64, beta: float64, dsigma: float64, idx: BlasInt, idxp: BlasInt, idxq: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, givnum: float64, ldgnum: BlasInt, c: float64, s: float64, info: BlasInt` |
| `dlasd8` | `None` | `icompq: BlasInt, k: BlasInt, d: float64, z: float64, vf: float64, vl: float64, difl: float64, difr: float64, lddifr: BlasInt, dsigma: float64, work: float64, info: BlasInt` |
| `dlasda` | `None` | `icompq: BlasInt, smlsiz: BlasInt, n: BlasInt, sqre: BlasInt, d: float64, e: float64, u: float64, ldu: BlasInt, vt: float64, k: BlasInt, difl: float64, difr: float64, z: float64, poles: float64, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, perm: BlasInt, givnum: float64, c: float64, s: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dlasdq` | `None` | `uplo: uint8, sqre: BlasInt, n: BlasInt, ncvt: BlasInt, nru: BlasInt, ncc: BlasInt, d: float64, e: float64, vt: float64, ldvt: BlasInt, u: float64, ldu: BlasInt, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dlasdt` | `None` | `n: BlasInt, lvl: BlasInt, nd: BlasInt, inode: BlasInt, ndiml: BlasInt, ndimr: BlasInt, msub: BlasInt` |
| `dlaset` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, alpha: float64, beta: float64, a: float64, lda: BlasInt` |
| `dlasq1` | `None` | `n: BlasInt, d: float64, e: float64, work: float64, info: BlasInt` |
| `dlasq2` | `None` | `n: BlasInt, z: float64, info: BlasInt` |
| `dlasq3` | `None` | `i0: BlasInt, n0: BlasInt, z: float64, pp: BlasInt, dmin: float64, sigma: float64, desig: float64, qmax: float64, nfail: BlasInt, iter: BlasInt, ndiv: BlasInt, ieee: bool, ttype: BlasInt, dmin1: float64, dmin2: float64, dn: float64, dn1: float64, dn2: float64, g: float64, tau: float64` |
| `dlasq4` | `None` | `i0: BlasInt, n0: BlasInt, z: float64, pp: BlasInt, n0in: BlasInt, dmin: float64, dmin1: float64, dmin2: float64, dn: float64, dn1: float64, dn2: float64, tau: float64, ttype: BlasInt, g: float64` |
| `dlasq6` | `None` | `i0: BlasInt, n0: BlasInt, z: float64, pp: BlasInt, dmin: float64, dmin1: float64, dmin2: float64, dn: float64, dnm1: float64, dnm2: float64` |
| `dlasr` | `None` | `side: uint8, pivot: uint8, direct: uint8, m: BlasInt, n: BlasInt, c: float64, s: float64, a: float64, lda: BlasInt` |
| `dlasrt` | `None` | `id: uint8, n: BlasInt, d: float64, info: BlasInt` |
| `dlassq` | `None` | `n: BlasInt, x: float64, incx: BlasInt, scale: float64, sumsq: float64` |
| `dlasv2` | `None` | `f: float64, g: float64, h: float64, ssmin: float64, ssmax: float64, snr: float64, csr: float64, snl: float64, csl: float64` |
| `dlaswp` | `None` | `n: BlasInt, a: float64, lda: BlasInt, k1: BlasInt, k2: BlasInt, ipiv: BlasInt, incx: BlasInt` |
| `dlasy2` | `None` | `ltranl: bool, ltranr: bool, isgn: BlasInt, n1: BlasInt, n2: BlasInt, tl: float64, ldtl: BlasInt, tr: float64, ldtr: BlasInt, b: float64, ldb: BlasInt, scale: float64, x: float64, ldx: BlasInt, xnorm: float64, info: BlasInt` |
| `dlasyf` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, kb: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, w: float64, ldw: BlasInt, info: BlasInt` |
| `dlat2s` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, sa: float32, ldsa: BlasInt, info: BlasInt` |
| `dlatbs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, x: float64, scale: float64, cnorm: float64, info: BlasInt` |
| `dlatdf` | `None` | `ijob: BlasInt, n: BlasInt, z: float64, ldz: BlasInt, rhs: float64, rdsum: float64, rdscal: float64, ipiv: BlasInt, jpiv: BlasInt` |
| `dlatps` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, ap: float64, x: float64, scale: float64, cnorm: float64, info: BlasInt` |
| `dlatrd` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, a: float64, lda: BlasInt, e: float64, tau: float64, w: float64, ldw: BlasInt` |
| `dlatrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, a: float64, lda: BlasInt, x: float64, scale: float64, cnorm: float64, info: BlasInt` |
| `dlatrz` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64` |
| `dlauu2` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `dlauum` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `dnrm2` | `np.float64` | `n: BlasInt, x: float64, incx: BlasInt` |
| `dopgtr` | `None` | `uplo: uint8, n: BlasInt, ap: float64, tau: float64, q: float64, ldq: BlasInt, work: float64, info: BlasInt` |
| `dopmtr` | `None` | `side: uint8, uplo: uint8, trans: uint8, m: BlasInt, n: BlasInt, ap: float64, tau: float64, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dorbdb` | `None` | `trans: uint8, signs: uint8, m: BlasInt, p: BlasInt, q: BlasInt, x11: float64, ldx11: BlasInt, x12: float64, ldx12: BlasInt, x21: float64, ldx21: BlasInt, x22: float64, ldx22: BlasInt, theta: float64, phi: float64, taup1: float64, taup2: float64, tauq1: float64, tauq2: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorcsd` | `None` | `jobu1: uint8, jobu2: uint8, jobv1t: uint8, jobv2t: uint8, trans: uint8, signs: uint8, m: BlasInt, p: BlasInt, q: BlasInt, x11: float64, ldx11: BlasInt, x12: float64, ldx12: BlasInt, x21: float64, ldx21: BlasInt, x22: float64, ldx22: BlasInt, theta: float64, u1: float64, ldu1: BlasInt, u2: float64, ldu2: BlasInt, v1t: float64, ldv1t: BlasInt, v2t: float64, ldv2t: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dorg2l` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dorg2r` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dorgbr` | `None` | `vect: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorghr` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorgl2` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dorglq` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorgql` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorgqr` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorgr2` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, info: BlasInt` |
| `dorgrq` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorgtr` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorm2l` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dorm2r` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dormbr` | `None` | `vect: uint8, side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dormhr` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dorml2` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dormlq` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dormql` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dormqr` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dormr2` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dormr3` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, info: BlasInt` |
| `dormrq` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dormrz` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dormtr` | `None` | `side: uint8, uplo: uint8, trans: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, c: float64, ldc: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dpbcon` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, anorm: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dpbequ` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, s: float64, scond: float64, amax: float64, info: BlasInt` |
| `dpbrfs` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, afb: float64, ldafb: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dpbstf` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, info: BlasInt` |
| `dpbsv` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dpbsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, afb: float64, ldafb: BlasInt, equed: uint8, s: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dpbtf2` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, info: BlasInt` |
| `dpbtrf` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, info: BlasInt` |
| `dpbtrs` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dpftrf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: float64, info: BlasInt` |
| `dpftri` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: float64, info: BlasInt` |
| `dpftrs` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, b: float64, ldb: BlasInt, info: BlasInt` |
| `dpocon` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, anorm: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dpoequ` | `None` | `n: BlasInt, a: float64, lda: BlasInt, s: float64, scond: float64, amax: float64, info: BlasInt` |
| `dpoequb` | `None` | `n: BlasInt, a: float64, lda: BlasInt, s: float64, scond: float64, amax: float64, info: BlasInt` |
| `dporfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, af: float64, ldaf: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dposv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dposvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, af: float64, ldaf: BlasInt, equed: uint8, s: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dpotf2` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `dpotrf` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `dpotri` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `dpotrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dppcon` | `None` | `uplo: uint8, n: BlasInt, ap: float64, anorm: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dppequ` | `None` | `uplo: uint8, n: BlasInt, ap: float64, s: float64, scond: float64, amax: float64, info: BlasInt` |
| `dpprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, afp: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dppsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, b: float64, ldb: BlasInt, info: BlasInt` |
| `dppsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, afp: float64, equed: uint8, s: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dpptrf` | `None` | `uplo: uint8, n: BlasInt, ap: float64, info: BlasInt` |
| `dpptri` | `None` | `uplo: uint8, n: BlasInt, ap: float64, info: BlasInt` |
| `dpptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, b: float64, ldb: BlasInt, info: BlasInt` |
| `dpstf2` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, piv: BlasInt, rank: BlasInt, tol: float64, work: float64, info: BlasInt` |
| `dpstrf` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, piv: BlasInt, rank: BlasInt, tol: float64, work: float64, info: BlasInt` |
| `dptcon` | `None` | `n: BlasInt, d: float64, e: float64, anorm: float64, rcond: float64, work: float64, info: BlasInt` |
| `dpteqr` | `None` | `compz: uint8, n: BlasInt, d: float64, e: float64, z: float64, ldz: BlasInt, work: float64, info: BlasInt` |
| `dptrfs` | `None` | `n: BlasInt, nrhs: BlasInt, d: float64, e: float64, df: float64, ef: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, info: BlasInt` |
| `dptsv` | `None` | `n: BlasInt, nrhs: BlasInt, d: float64, e: float64, b: float64, ldb: BlasInt, info: BlasInt` |
| `dptsvx` | `None` | `fact: uint8, n: BlasInt, nrhs: BlasInt, d: float64, e: float64, df: float64, ef: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, info: BlasInt` |
| `dpttrf` | `None` | `n: BlasInt, d: float64, e: float64, info: BlasInt` |
| `dpttrs` | `None` | `n: BlasInt, nrhs: BlasInt, d: float64, e: float64, b: float64, ldb: BlasInt, info: BlasInt` |
| `dptts2` | `None` | `n: BlasInt, nrhs: BlasInt, d: float64, e: float64, b: float64, ldb: BlasInt` |
| `drot` | `None` | `n: BlasInt, dx: float64, incx: BlasInt, dy: float64, incy: BlasInt, c: float64, s: float64` |
| `drotg` | `None` | `da: float64, db: float64, c: float64, s: float64` |
| `drotm` | `None` | `n: BlasInt, dx: float64, incx: BlasInt, dy: float64, incy: BlasInt, dparam: float64` |
| `drotmg` | `None` | `dd1: float64, dd2: float64, dx1: float64, dy1: float64, dparam: float64` |
| `drscl` | `None` | `n: BlasInt, sa: float64, sx: float64, incx: BlasInt` |
| `dsbev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, info: BlasInt` |
| `dsbevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dsbevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, q: float64, ldq: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `dsbgst` | `None` | `vect: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: float64, ldab: BlasInt, bb: float64, ldbb: BlasInt, x: float64, ldx: BlasInt, work: float64, info: BlasInt` |
| `dsbgv` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: float64, ldab: BlasInt, bb: float64, ldbb: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, info: BlasInt` |
| `dsbgvd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: float64, ldab: BlasInt, bb: float64, ldbb: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dsbgvx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: float64, ldab: BlasInt, bb: float64, ldbb: BlasInt, q: float64, ldq: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `dsbmv` | `None` | `uplo: uint8, n: BlasInt, k: BlasInt, alpha: float64, a: float64, lda: BlasInt, x: float64, incx: BlasInt, beta: float64, y: float64, incy: BlasInt` |
| `dsbtrd` | `None` | `vect: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, d: float64, e: float64, q: float64, ldq: BlasInt, work: float64, info: BlasInt` |
| `dscal` | `None` | `n: BlasInt, da: float64, dx: float64, incx: BlasInt` |
| `dsdot` | `np.float64` | `n: BlasInt, sx: float32, incx: BlasInt, sy: float32, incy: BlasInt` |
| `dsfrk` | `None` | `transr: uint8, uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float64, a: float64, lda: BlasInt, beta: float64, c: float64` |
| `dsgesv` | `None` | `n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, work: float64, swork: float32, iter: BlasInt, info: BlasInt` |
| `dspcon` | `None` | `uplo: uint8, n: BlasInt, ap: float64, ipiv: BlasInt, anorm: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dspev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ap: float64, w: float64, z: float64, ldz: BlasInt, work: float64, info: BlasInt` |
| `dspevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ap: float64, w: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dspevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ap: float64, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `dspgst` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, ap: float64, bp: float64, info: BlasInt` |
| `dspgv` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, ap: float64, bp: float64, w: float64, z: float64, ldz: BlasInt, work: float64, info: BlasInt` |
| `dspgvd` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, ap: float64, bp: float64, w: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dspgvx` | `None` | `itype: BlasInt, jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ap: float64, bp: float64, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `dspmv` | `None` | `uplo: uint8, n: BlasInt, alpha: float64, ap: float64, x: float64, incx: BlasInt, beta: float64, y: float64, incy: BlasInt` |
| `dsposv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, work: float64, swork: float32, iter: BlasInt, info: BlasInt` |
| `dspr` | `None` | `uplo: uint8, n: BlasInt, alpha: float64, x: float64, incx: BlasInt, ap: float64` |
| `dspr2` | `None` | `uplo: uint8, n: BlasInt, alpha: float64, x: float64, incx: BlasInt, y: float64, incy: BlasInt, ap: float64` |
| `dsprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, afp: float64, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dspsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, ipiv: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dspsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, afp: float64, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dsptrd` | `None` | `uplo: uint8, n: BlasInt, ap: float64, d: float64, e: float64, tau: float64, info: BlasInt` |
| `dsptrf` | `None` | `uplo: uint8, n: BlasInt, ap: float64, ipiv: BlasInt, info: BlasInt` |
| `dsptri` | `None` | `uplo: uint8, n: BlasInt, ap: float64, ipiv: BlasInt, work: float64, info: BlasInt` |
| `dsptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, ipiv: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dstebz` | `None` | `range: uint8, order: uint8, n: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, d: float64, e: float64, m: BlasInt, nsplit: BlasInt, w: float64, iblock: BlasInt, isplit: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `dstedc` | `None` | `compz: uint8, n: BlasInt, d: float64, e: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dstegr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float64, e: float64, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, isuppz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dstein` | `None` | `n: BlasInt, d: float64, e: float64, m: BlasInt, w: float64, iblock: BlasInt, isplit: BlasInt, z: float64, ldz: BlasInt, work: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `dstemr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float64, e: float64, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, m: BlasInt, w: float64, z: float64, ldz: BlasInt, nzc: BlasInt, isuppz: BlasInt, tryrac: bool, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dsteqr` | `None` | `compz: uint8, n: BlasInt, d: float64, e: float64, z: float64, ldz: BlasInt, work: float64, info: BlasInt` |
| `dsterf` | `None` | `n: BlasInt, d: float64, e: float64, info: BlasInt` |
| `dstev` | `None` | `jobz: uint8, n: BlasInt, d: float64, e: float64, z: float64, ldz: BlasInt, work: float64, info: BlasInt` |
| `dstevd` | `None` | `jobz: uint8, n: BlasInt, d: float64, e: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dstevr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float64, e: float64, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, isuppz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dstevx` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float64, e: float64, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `dswap` | `None` | `n: BlasInt, dx: float64, incx: BlasInt, dy: float64, incy: BlasInt` |
| `dsycon` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, anorm: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dsyconv` | `None` | `uplo: uint8, way: uint8, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, work: float64, info: BlasInt` |
| `dsyequb` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, s: float64, scond: float64, amax: float64, work: float64, info: BlasInt` |
| `dsyev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, w: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dsyevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, w: float64, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dsyevr` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, isuppz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dsyevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `dsygs2` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dsygst` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dsygv` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, w: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dsygvd` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, w: float64, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dsygvx` | `None` | `itype: BlasInt, jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: float64, ldz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `dsymm` | `None` | `side: uint8, uplo: uint8, m: BlasInt, n: BlasInt, alpha: float64, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, beta: float64, c: float64, ldc: BlasInt` |
| `dsymv` | `None` | `uplo: uint8, n: BlasInt, alpha: float64, a: float64, lda: BlasInt, x: float64, incx: BlasInt, beta: float64, y: float64, incy: BlasInt` |
| `dsyr` | `None` | `uplo: uint8, n: BlasInt, alpha: float64, x: float64, incx: BlasInt, a: float64, lda: BlasInt` |
| `dsyr2` | `None` | `uplo: uint8, n: BlasInt, alpha: float64, x: float64, incx: BlasInt, y: float64, incy: BlasInt, a: float64, lda: BlasInt` |
| `dsyr2k` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float64, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, beta: float64, c: float64, ldc: BlasInt` |
| `dsyrfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, af: float64, ldaf: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dsyrk` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float64, a: float64, lda: BlasInt, beta: float64, c: float64, ldc: BlasInt` |
| `dsysv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dsysvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, af: float64, ldaf: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: float64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dsyswapr` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, i1: BlasInt, i2: BlasInt` |
| `dsytd2` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, d: float64, e: float64, tau: float64, info: BlasInt` |
| `dsytf2` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `dsytrd` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, d: float64, e: float64, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dsytrf` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dsytri` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, work: float64, info: BlasInt` |
| `dsytri2` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dsytri2x` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, work: float64, nb: BlasInt, info: BlasInt` |
| `dsytrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dsytrs2` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, ipiv: BlasInt, b: float64, ldb: BlasInt, work: float64, info: BlasInt` |
| `dtbcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, kd: BlasInt, ab: float64, ldab: BlasInt, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dtbmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, x: float64, incx: BlasInt` |
| `dtbrfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dtbsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, k: BlasInt, a: float64, lda: BlasInt, x: float64, incx: BlasInt` |
| `dtbtrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float64, ldab: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dtfsm` | `None` | `transr: uint8, side: uint8, uplo: uint8, trans: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: float64, a: float64, b: float64, ldb: BlasInt` |
| `dtftri` | `None` | `transr: uint8, uplo: uint8, diag: uint8, n: BlasInt, a: float64, info: BlasInt` |
| `dtfttp` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, arf: float64, ap: float64, info: BlasInt` |
| `dtfttr` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, arf: float64, a: float64, lda: BlasInt, info: BlasInt` |
| `dtgevc` | `None` | `side: uint8, howmny: uint8, select: bool, n: BlasInt, s: float64, lds: BlasInt, p: float64, ldp: BlasInt, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: float64, info: BlasInt` |
| `dtgex2` | `None` | `wantq: bool, wantz: bool, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, q: float64, ldq: BlasInt, z: float64, ldz: BlasInt, j1: BlasInt, n1: BlasInt, n2: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dtgexc` | `None` | `wantq: bool, wantz: bool, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, q: float64, ldq: BlasInt, z: float64, ldz: BlasInt, ifst: BlasInt, ilst: BlasInt, work: float64, lwork: BlasInt, info: BlasInt` |
| `dtgsen` | `None` | `ijob: BlasInt, wantq: bool, wantz: bool, select: bool, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, alphar: float64, alphai: float64, beta: float64, q: float64, ldq: BlasInt, z: float64, ldz: BlasInt, m: BlasInt, pl: float64, pr: float64, dif: float64, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dtgsja` | `None` | `jobu: uint8, jobv: uint8, jobq: uint8, m: BlasInt, p: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, tola: float64, tolb: float64, alpha: float64, beta: float64, u: float64, ldu: BlasInt, v: float64, ldv: BlasInt, q: float64, ldq: BlasInt, work: float64, ncycle: BlasInt, info: BlasInt` |
| `dtgsna` | `None` | `job: uint8, howmny: uint8, select: bool, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, s: float64, dif: float64, mm: BlasInt, m: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dtgsy2` | `None` | `trans: uint8, ijob: BlasInt, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, c: float64, ldc: BlasInt, d: float64, ldd: BlasInt, e: float64, lde: BlasInt, f: float64, ldf: BlasInt, scale: float64, rdsum: float64, rdscal: float64, iwork: BlasInt, pq: BlasInt, info: BlasInt` |
| `dtgsyl` | `None` | `trans: uint8, ijob: BlasInt, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, c: float64, ldc: BlasInt, d: float64, ldd: BlasInt, e: float64, lde: BlasInt, f: float64, ldf: BlasInt, scale: float64, dif: float64, work: float64, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dtpcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, ap: float64, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dtpmqrt` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, nb: BlasInt, v: float64, ldv: BlasInt, t: float64, ldt: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, work: float64, info: BlasInt` |
| `dtpmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, ap: float64, x: float64, incx: BlasInt` |
| `dtpqrt` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, nb: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, t: float64, ldt: BlasInt, work: float64, info: BlasInt` |
| `dtpqrt2` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, t: float64, ldt: BlasInt, info: BlasInt` |
| `dtprfb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, v: float64, ldv: BlasInt, t: float64, ldt: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, work: float64, ldwork: BlasInt` |
| `dtprfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dtpsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, ap: float64, x: float64, incx: BlasInt` |
| `dtptri` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, ap: float64, info: BlasInt` |
| `dtptrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, ap: float64, b: float64, ldb: BlasInt, info: BlasInt` |
| `dtpttf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, ap: float64, arf: float64, info: BlasInt` |
| `dtpttr` | `None` | `uplo: uint8, n: BlasInt, ap: float64, a: float64, lda: BlasInt, info: BlasInt` |
| `dtrcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, a: float64, lda: BlasInt, rcond: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dtrevc` | `None` | `side: uint8, howmny: uint8, select: bool, n: BlasInt, t: float64, ldt: BlasInt, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: float64, info: BlasInt` |
| `dtrexc` | `None` | `compq: uint8, n: BlasInt, t: float64, ldt: BlasInt, q: float64, ldq: BlasInt, ifst: BlasInt, ilst: BlasInt, work: float64, info: BlasInt` |
| `dtrmm` | `None` | `side: uint8, uplo: uint8, transa: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: float64, a: float64, lda: BlasInt, b: float64, ldb: BlasInt` |
| `dtrmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, a: float64, lda: BlasInt, x: float64, incx: BlasInt` |
| `dtrrfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, x: float64, ldx: BlasInt, ferr: float64, berr: float64, work: float64, iwork: BlasInt, info: BlasInt` |
| `dtrsen` | `None` | `job: uint8, compq: uint8, select: bool, n: BlasInt, t: float64, ldt: BlasInt, q: float64, ldq: BlasInt, wr: float64, wi: float64, m: BlasInt, s: float64, sep: float64, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `dtrsm` | `None` | `side: uint8, uplo: uint8, transa: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: float64, a: float64, lda: BlasInt, b: float64, ldb: BlasInt` |
| `dtrsna` | `None` | `job: uint8, howmny: uint8, select: bool, n: BlasInt, t: float64, ldt: BlasInt, vl: float64, ldvl: BlasInt, vr: float64, ldvr: BlasInt, s: float64, sep: float64, mm: BlasInt, m: BlasInt, work: float64, ldwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `dtrsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, a: float64, lda: BlasInt, x: float64, incx: BlasInt` |
| `dtrsyl` | `None` | `trana: uint8, tranb: uint8, isgn: BlasInt, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, c: float64, ldc: BlasInt, scale: float64, info: BlasInt` |
| `dtrti2` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `dtrtri` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `dtrtrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, a: float64, lda: BlasInt, b: float64, ldb: BlasInt, info: BlasInt` |
| `dtrttf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, arf: float64, info: BlasInt` |
| `dtrttp` | `None` | `uplo: uint8, n: BlasInt, a: float64, lda: BlasInt, ap: float64, info: BlasInt` |
| `dtzrzf` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, tau: float64, work: float64, lwork: BlasInt, info: BlasInt` |
| `dzasum` | `np.float64` | `n: BlasInt, zx: complex128, incx: BlasInt` |
| `dznrm2` | `np.float64` | `n: BlasInt, x: complex128, incx: BlasInt` |
| `dzsum1` | `np.float64` | `n: BlasInt, cx: complex128, incx: BlasInt` |
| `icamax` | `BlasInt` | `n: BlasInt, cx: complex64, incx: BlasInt` |
| `icmax1` | `BlasInt` | `n: BlasInt, cx: complex64, incx: BlasInt` |
| `idamax` | `BlasInt` | `n: BlasInt, dx: float64, incx: BlasInt` |
| `ieeeck` | `BlasInt` | `ispec: BlasInt, zero: float32, one: float32` |
| `ilaclc` | `BlasInt` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt` |
| `ilaclr` | `BlasInt` | `m: BlasInt, n: BlasInt, a: complex64, lda: BlasInt` |
| `iladiag` | `BlasInt` | `diag: uint8` |
| `iladlc` | `BlasInt` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt` |
| `iladlr` | `BlasInt` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt` |
| `ilaprec` | `BlasInt` | `prec: uint8` |
| `ilaslc` | `BlasInt` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt` |
| `ilaslr` | `BlasInt` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt` |
| `ilatrans` | `BlasInt` | `trans: uint8` |
| `ilauplo` | `BlasInt` | `uplo: uint8` |
| `ilaver` | `None` | `vers_major: BlasInt, vers_minor: BlasInt, vers_patch: BlasInt` |
| `ilazlc` | `BlasInt` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt` |
| `ilazlr` | `BlasInt` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt` |
| `isamax` | `BlasInt` | `n: BlasInt, sx: float32, incx: BlasInt` |
| `izamax` | `BlasInt` | `n: BlasInt, zx: complex128, incx: BlasInt` |
| `izmax1` | `BlasInt` | `n: BlasInt, cx: complex128, incx: BlasInt` |
| `lsame` | `bool` | `ca: uint8, cb: uint8` |
| `sasum` | `np.float32` | `n: BlasInt, sx: float32, incx: BlasInt` |
| `saxpy` | `None` | `n: BlasInt, sa: float32, sx: float32, incx: BlasInt, sy: float32, incy: BlasInt` |
| `sbbcsd` | `None` | `jobu1: uint8, jobu2: uint8, jobv1t: uint8, jobv2t: uint8, trans: uint8, m: BlasInt, p: BlasInt, q: BlasInt, theta: float32, phi: float32, u1: float32, ldu1: BlasInt, u2: float32, ldu2: BlasInt, v1t: float32, ldv1t: BlasInt, v2t: float32, ldv2t: BlasInt, b11d: float32, b11e: float32, b12d: float32, b12e: float32, b21d: float32, b21e: float32, b22d: float32, b22e: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sbdsdc` | `None` | `uplo: uint8, compq: uint8, n: BlasInt, d: float32, e: float32, u: float32, ldu: BlasInt, vt: float32, ldvt: BlasInt, q: float32, iq: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `sbdsqr` | `None` | `uplo: uint8, n: BlasInt, ncvt: BlasInt, nru: BlasInt, ncc: BlasInt, d: float32, e: float32, vt: float32, ldvt: BlasInt, u: float32, ldu: BlasInt, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `scasum` | `np.float32` | `n: BlasInt, cx: complex64, incx: BlasInt` |
| `scnrm2` | `np.float32` | `n: BlasInt, x: complex64, incx: BlasInt` |
| `scopy` | `None` | `n: BlasInt, sx: float32, incx: BlasInt, sy: float32, incy: BlasInt` |
| `scsum1` | `np.float32` | `n: BlasInt, cx: complex64, incx: BlasInt` |
| `sdisna` | `None` | `job: uint8, m: BlasInt, n: BlasInt, d: float32, sep: float32, info: BlasInt` |
| `sdot` | `np.float32` | `n: BlasInt, sx: float32, incx: BlasInt, sy: float32, incy: BlasInt` |
| `sdsdot` | `np.float32` | `n: BlasInt, sb: float32, sx: float32, incx: BlasInt, sy: float32, incy: BlasInt` |
| `sgbbrd` | `None` | `vect: uint8, m: BlasInt, n: BlasInt, ncc: BlasInt, kl: BlasInt, ku: BlasInt, ab: float32, ldab: BlasInt, d: float32, e: float32, q: float32, ldq: BlasInt, pt: float32, ldpt: BlasInt, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `sgbcon` | `None` | `norm: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float32, ldab: BlasInt, ipiv: BlasInt, anorm: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgbequ` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float32, ldab: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, info: BlasInt` |
| `sgbequb` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float32, ldab: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, info: BlasInt` |
| `sgbmv` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, alpha: float32, a: float32, lda: BlasInt, x: float32, incx: BlasInt, beta: float32, y: float32, incy: BlasInt` |
| `sgbrfs` | `None` | `trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, afb: float32, ldafb: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgbsv` | `None` | `n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sgbsvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, afb: float32, ldafb: BlasInt, ipiv: BlasInt, equed: uint8, r: float32, c: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgbtf2` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float32, ldab: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `sgbtrf` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float32, ldab: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `sgbtrs` | `None` | `trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sgebak` | `None` | `job: uint8, side: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float32, m: BlasInt, v: float32, ldv: BlasInt, info: BlasInt` |
| `sgebal` | `None` | `job: uint8, n: BlasInt, a: float32, lda: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float32, info: BlasInt` |
| `sgebd2` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, d: float32, e: float32, tauq: float32, taup: float32, work: float32, info: BlasInt` |
| `sgebrd` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, d: float32, e: float32, tauq: float32, taup: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgecon` | `None` | `norm: uint8, n: BlasInt, a: float32, lda: BlasInt, anorm: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgeequ` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, info: BlasInt` |
| `sgeequb` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, info: BlasInt` |
| `sgeev` | `None` | `jobvl: uint8, jobvr: uint8, n: BlasInt, a: float32, lda: BlasInt, wr: float32, wi: float32, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgeevx` | `None` | `balanc: uint8, jobvl: uint8, jobvr: uint8, sense: uint8, n: BlasInt, a: float32, lda: BlasInt, wr: float32, wi: float32, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float32, abnrm: float32, rconde: float32, rcondv: float32, work: float32, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `sgehd2` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sgehrd` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgejsv` | `None` | `joba: uint8, jobu: uint8, jobv: uint8, jobr: uint8, jobt: uint8, jobp: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, sva: float32, u: float32, ldu: BlasInt, v: float32, ldv: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `sgelq2` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sgelqf` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgels` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgelsd` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, s: float32, rcond: float32, rank: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `sgelss` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, s: float32, rcond: float32, rank: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgelsy` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, jpvt: BlasInt, rcond: float32, rank: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgemm` | `None` | `transa: uint8, transb: uint8, m: BlasInt, n: BlasInt, k: BlasInt, alpha: float32, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, beta: float32, c: float32, ldc: BlasInt` |
| `sgemqrt` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, nb: BlasInt, v: float32, ldv: BlasInt, t: float32, ldt: BlasInt, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `sgemv` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, alpha: float32, a: float32, lda: BlasInt, x: float32, incx: BlasInt, beta: float32, y: float32, incy: BlasInt` |
| `sgeql2` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sgeqlf` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgeqp3` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, jpvt: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgeqr2` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sgeqr2p` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sgeqrf` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgeqrfp` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgeqrt` | `None` | `m: BlasInt, n: BlasInt, nb: BlasInt, a: float32, lda: BlasInt, t: float32, ldt: BlasInt, work: float32, info: BlasInt` |
| `sgeqrt2` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, t: float32, ldt: BlasInt, info: BlasInt` |
| `sgeqrt3` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, t: float32, ldt: BlasInt, info: BlasInt` |
| `sger` | `None` | `m: BlasInt, n: BlasInt, alpha: float32, x: float32, incx: BlasInt, y: float32, incy: BlasInt, a: float32, lda: BlasInt` |
| `sgerfs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, af: float32, ldaf: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgerq2` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sgerqf` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgesc2` | `None` | `n: BlasInt, a: float32, lda: BlasInt, rhs: float32, ipiv: BlasInt, jpiv: BlasInt, scale: float32` |
| `sgesdd` | `None` | `jobz: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, s: float32, u: float32, ldu: BlasInt, vt: float32, ldvt: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `sgesv` | `None` | `n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sgesvd` | `None` | `jobu: uint8, jobvt: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, s: float32, u: float32, ldu: BlasInt, vt: float32, ldvt: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgesvj` | `None` | `joba: uint8, jobu: uint8, jobv: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, sva: float32, mv: BlasInt, v: float32, ldv: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgesvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, af: float32, ldaf: BlasInt, ipiv: BlasInt, equed: uint8, r: float32, c: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgetc2` | `None` | `n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, jpiv: BlasInt, info: BlasInt` |
| `sgetf2` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `sgetrf` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `sgetri` | `None` | `n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgetrs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sggbak` | `None` | `job: uint8, side: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float32, rscale: float32, m: BlasInt, v: float32, ldv: BlasInt, info: BlasInt` |
| `sggbal` | `None` | `job: uint8, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float32, rscale: float32, work: float32, info: BlasInt` |
| `sggev` | `None` | `jobvl: uint8, jobvr: uint8, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, alphar: float32, alphai: float32, beta: float32, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sggevx` | `None` | `balanc: uint8, jobvl: uint8, jobvr: uint8, sense: uint8, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, alphar: float32, alphai: float32, beta: float32, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float32, rscale: float32, abnrm: float32, bbnrm: float32, rconde: float32, rcondv: float32, work: float32, lwork: BlasInt, iwork: BlasInt, bwork: bool, info: BlasInt` |
| `sggglm` | `None` | `n: BlasInt, m: BlasInt, p: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, d: float32, x: float32, y: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgghrd` | `None` | `compq: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, q: float32, ldq: BlasInt, z: float32, ldz: BlasInt, info: BlasInt` |
| `sgglse` | `None` | `m: BlasInt, n: BlasInt, p: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, c: float32, d: float32, x: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sggqrf` | `None` | `n: BlasInt, m: BlasInt, p: BlasInt, a: float32, lda: BlasInt, taua: float32, b: float32, ldb: BlasInt, taub: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sggrqf` | `None` | `m: BlasInt, p: BlasInt, n: BlasInt, a: float32, lda: BlasInt, taua: float32, b: float32, ldb: BlasInt, taub: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgsvj0` | `None` | `jobv: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, d: float32, sva: float32, mv: BlasInt, v: float32, ldv: BlasInt, eps: float32, sfmin: float32, tol: float32, nsweep: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgsvj1` | `None` | `jobv: uint8, m: BlasInt, n: BlasInt, n1: BlasInt, a: float32, lda: BlasInt, d: float32, sva: float32, mv: BlasInt, v: float32, ldv: BlasInt, eps: float32, sfmin: float32, tol: float32, nsweep: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sgtcon` | `None` | `norm: uint8, n: BlasInt, dl: float32, d: float32, du: float32, du2: float32, ipiv: BlasInt, anorm: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgtrfs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, dl: float32, d: float32, du: float32, dlf: float32, df: float32, duf: float32, du2: float32, ipiv: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgtsv` | `None` | `n: BlasInt, nrhs: BlasInt, dl: float32, d: float32, du: float32, b: float32, ldb: BlasInt, info: BlasInt` |
| `sgtsvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, nrhs: BlasInt, dl: float32, d: float32, du: float32, dlf: float32, df: float32, duf: float32, du2: float32, ipiv: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sgttrf` | `None` | `n: BlasInt, dl: float32, d: float32, du: float32, du2: float32, ipiv: BlasInt, info: BlasInt` |
| `sgttrs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, dl: float32, d: float32, du: float32, du2: float32, ipiv: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sgtts2` | `None` | `itrans: BlasInt, n: BlasInt, nrhs: BlasInt, dl: float32, d: float32, du: float32, du2: float32, ipiv: BlasInt, b: float32, ldb: BlasInt` |
| `shgeqz` | `None` | `job: uint8, compq: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float32, ldh: BlasInt, t: float32, ldt: BlasInt, alphar: float32, alphai: float32, beta: float32, q: float32, ldq: BlasInt, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `shsein` | `None` | `side: uint8, eigsrc: uint8, initv: uint8, select: bool, n: BlasInt, h: float32, ldh: BlasInt, wr: float32, wi: float32, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: float32, ifaill: BlasInt, ifailr: BlasInt, info: BlasInt` |
| `shseqr` | `None` | `job: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float32, ldh: BlasInt, wr: float32, wi: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `slabad` | `None` | `small: float32, large: float32` |
| `slabrd` | `None` | `m: BlasInt, n: BlasInt, nb: BlasInt, a: float32, lda: BlasInt, d: float32, e: float32, tauq: float32, taup: float32, x: float32, ldx: BlasInt, y: float32, ldy: BlasInt` |
| `slacn2` | `None` | `n: BlasInt, v: float32, x: float32, isgn: BlasInt, est: float32, kase: BlasInt, isave: BlasInt` |
| `slacon` | `None` | `n: BlasInt, v: float32, x: float32, isgn: BlasInt, est: float32, kase: BlasInt` |
| `slacpy` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt` |
| `sladiv` | `None` | `a: float32, b: float32, c: float32, d: float32, p: float32, q: float32` |
| `slae2` | `None` | `a: float32, b: float32, c: float32, rt1: float32, rt2: float32` |
| `slaebz` | `None` | `ijob: BlasInt, nitmax: BlasInt, n: BlasInt, mmax: BlasInt, minp: BlasInt, nbmin: BlasInt, abstol: float32, reltol: float32, pivmin: float32, d: float32, e: float32, e2: float32, nval: BlasInt, ab: float32, c: float32, mout: BlasInt, nab: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `slaed0` | `None` | `icompq: BlasInt, qsiz: BlasInt, n: BlasInt, d: float32, e: float32, q: float32, ldq: BlasInt, qstore: float32, ldqs: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `slaed1` | `None` | `n: BlasInt, d: float32, q: float32, ldq: BlasInt, indxq: BlasInt, rho: float32, cutpnt: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `slaed2` | `None` | `k: BlasInt, n: BlasInt, n1: BlasInt, d: float32, q: float32, ldq: BlasInt, indxq: BlasInt, rho: float32, z: float32, dlamda: float32, w: float32, q2: float32, indx: BlasInt, indxc: BlasInt, indxp: BlasInt, coltyp: BlasInt, info: BlasInt` |
| `slaed3` | `None` | `k: BlasInt, n: BlasInt, n1: BlasInt, d: float32, q: float32, ldq: BlasInt, rho: float32, dlamda: float32, q2: float32, indx: BlasInt, ctot: BlasInt, w: float32, s: float32, info: BlasInt` |
| `slaed4` | `None` | `n: BlasInt, i: BlasInt, d: float32, z: float32, delta: float32, rho: float32, dlam: float32, info: BlasInt` |
| `slaed5` | `None` | `i: BlasInt, d: float32, z: float32, delta: float32, rho: float32, dlam: float32` |
| `slaed6` | `None` | `kniter: BlasInt, orgati: bool, rho: float32, d: float32, z: float32, finit: float32, tau: float32, info: BlasInt` |
| `slaed7` | `None` | `icompq: BlasInt, n: BlasInt, qsiz: BlasInt, tlvls: BlasInt, curlvl: BlasInt, curpbm: BlasInt, d: float32, q: float32, ldq: BlasInt, indxq: BlasInt, rho: float32, cutpnt: BlasInt, qstore: float32, qptr: BlasInt, prmptr: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `slaed8` | `None` | `icompq: BlasInt, k: BlasInt, n: BlasInt, qsiz: BlasInt, d: float32, q: float32, ldq: BlasInt, indxq: BlasInt, rho: float32, cutpnt: BlasInt, z: float32, dlamda: float32, q2: float32, ldq2: BlasInt, w: float32, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float32, indxp: BlasInt, indx: BlasInt, info: BlasInt` |
| `slaed9` | `None` | `k: BlasInt, kstart: BlasInt, kstop: BlasInt, n: BlasInt, d: float32, q: float32, ldq: BlasInt, rho: float32, dlamda: float32, w: float32, s: float32, lds: BlasInt, info: BlasInt` |
| `slaeda` | `None` | `n: BlasInt, tlvls: BlasInt, curlvl: BlasInt, curpbm: BlasInt, prmptr: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float32, q: float32, qptr: BlasInt, z: float32, ztemp: float32, info: BlasInt` |
| `slaein` | `None` | `rightv: bool, noinit: bool, n: BlasInt, h: float32, ldh: BlasInt, wr: float32, wi: float32, vr: float32, vi: float32, b: float32, ldb: BlasInt, work: float32, eps3: float32, smlnum: float32, bignum: float32, info: BlasInt` |
| `slaev2` | `None` | `a: float32, b: float32, c: float32, rt1: float32, rt2: float32, cs1: float32, sn1: float32` |
| `slaexc` | `None` | `wantq: bool, n: BlasInt, t: float32, ldt: BlasInt, q: float32, ldq: BlasInt, j1: BlasInt, n1: BlasInt, n2: BlasInt, work: float32, info: BlasInt` |
| `slag2` | `None` | `a: float32, lda: BlasInt, b: float32, ldb: BlasInt, safmin: float32, scale1: float32, scale2: float32, wr1: float32, wr2: float32, wi: float32` |
| `slag2d` | `None` | `m: BlasInt, n: BlasInt, sa: float32, ldsa: BlasInt, a: float64, lda: BlasInt, info: BlasInt` |
| `slags2` | `None` | `upper: bool, a1: float32, a2: float32, a3: float32, b1: float32, b2: float32, b3: float32, csu: float32, snu: float32, csv: float32, snv: float32, csq: float32, snq: float32` |
| `slagtf` | `None` | `n: BlasInt, a: float32, lambda_: float32, b: float32, c: float32, tol: float32, d: float32, in_: BlasInt, info: BlasInt` |
| `slagtm` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, alpha: float32, dl: float32, d: float32, du: float32, x: float32, ldx: BlasInt, beta: float32, b: float32, ldb: BlasInt` |
| `slagts` | `None` | `job: BlasInt, n: BlasInt, a: float32, b: float32, c: float32, d: float32, in_: BlasInt, y: float32, tol: float32, info: BlasInt` |
| `slagv2` | `None` | `a: float32, lda: BlasInt, b: float32, ldb: BlasInt, alphar: float32, alphai: float32, beta: float32, csl: float32, snl: float32, csr: float32, snr: float32` |
| `slahqr` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float32, ldh: BlasInt, wr: float32, wi: float32, iloz: BlasInt, ihiz: BlasInt, z: float32, ldz: BlasInt, info: BlasInt` |
| `slahr2` | `None` | `n: BlasInt, k: BlasInt, nb: BlasInt, a: float32, lda: BlasInt, tau: float32, t: float32, ldt: BlasInt, y: float32, ldy: BlasInt` |
| `slaic1` | `None` | `job: BlasInt, j: BlasInt, x: float32, sest: float32, w: float32, gamma: float32, sestpr: float32, s: float32, c: float32` |
| `slaln2` | `None` | `ltrans: bool, na: BlasInt, nw: BlasInt, smin: float32, ca: float32, a: float32, lda: BlasInt, d1: float32, d2: float32, b: float32, ldb: BlasInt, wr: float32, wi: float32, x: float32, ldx: BlasInt, scale: float32, xnorm: float32, info: BlasInt` |
| `slals0` | `None` | `icompq: BlasInt, nl: BlasInt, nr: BlasInt, sqre: BlasInt, nrhs: BlasInt, b: float32, ldb: BlasInt, bx: float32, ldbx: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, givnum: float32, ldgnum: BlasInt, poles: float32, difl: float32, difr: float32, z: float32, k: BlasInt, c: float32, s: float32, work: float32, info: BlasInt` |
| `slalsa` | `None` | `icompq: BlasInt, smlsiz: BlasInt, n: BlasInt, nrhs: BlasInt, b: float32, ldb: BlasInt, bx: float32, ldbx: BlasInt, u: float32, ldu: BlasInt, vt: float32, k: BlasInt, difl: float32, difr: float32, z: float32, poles: float32, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, perm: BlasInt, givnum: float32, c: float32, s: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `slalsd` | `None` | `uplo: uint8, smlsiz: BlasInt, n: BlasInt, nrhs: BlasInt, d: float32, e: float32, b: float32, ldb: BlasInt, rcond: float32, rank: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `slamch` | `np.float32` | `cmach: uint8` |
| `slamrg` | `None` | `n1: BlasInt, n2: BlasInt, a: float32, strd1: BlasInt, strd2: BlasInt, index_bn: BlasInt` |
| `slangb` | `np.float32` | `norm: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float32, ldab: BlasInt, work: float32` |
| `slange` | `np.float32` | `norm: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, work: float32` |
| `slangt` | `np.float32` | `norm: uint8, n: BlasInt, dl: float32, d: float32, du: float32` |
| `slanhs` | `np.float32` | `norm: uint8, n: BlasInt, a: float32, lda: BlasInt, work: float32` |
| `slansb` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, k: BlasInt, ab: float32, ldab: BlasInt, work: float32` |
| `slansf` | `np.float32` | `norm: uint8, transr: uint8, uplo: uint8, n: BlasInt, a: float32, work: float32` |
| `slansp` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, ap: float32, work: float32` |
| `slanst` | `np.float32` | `norm: uint8, n: BlasInt, d: float32, e: float32` |
| `slansy` | `np.float32` | `norm: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, work: float32` |
| `slantb` | `np.float32` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, k: BlasInt, ab: float32, ldab: BlasInt, work: float32` |
| `slantp` | `np.float32` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, ap: float32, work: float32` |
| `slantr` | `np.float32` | `norm: uint8, uplo: uint8, diag: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, work: float32` |
| `slanv2` | `None` | `a: float32, b: float32, c: float32, d: float32, rt1r: float32, rt1i: float32, rt2r: float32, rt2i: float32, cs: float32, sn: float32` |
| `slapll` | `None` | `n: BlasInt, x: float32, incx: BlasInt, y: float32, incy: BlasInt, ssmin: float32` |
| `slapmr` | `None` | `forwrd: bool, m: BlasInt, n: BlasInt, x: float32, ldx: BlasInt, k: BlasInt` |
| `slapmt` | `None` | `forwrd: bool, m: BlasInt, n: BlasInt, x: float32, ldx: BlasInt, k: BlasInt` |
| `slapy2` | `np.float32` | `x: float32, y: float32` |
| `slapy3` | `np.float32` | `x: float32, y: float32, z: float32` |
| `slaqgb` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: float32, ldab: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, equed: uint8` |
| `slaqge` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, r: float32, c: float32, rowcnd: float32, colcnd: float32, amax: float32, equed: uint8` |
| `slaqp2` | `None` | `m: BlasInt, n: BlasInt, offset: BlasInt, a: float32, lda: BlasInt, jpvt: BlasInt, tau: float32, vn1: float32, vn2: float32, work: float32` |
| `slaqps` | `None` | `m: BlasInt, n: BlasInt, offset: BlasInt, nb: BlasInt, kb: BlasInt, a: float32, lda: BlasInt, jpvt: BlasInt, tau: float32, vn1: float32, vn2: float32, auxv: float32, f: float32, ldf: BlasInt` |
| `slaqr0` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float32, ldh: BlasInt, wr: float32, wi: float32, iloz: BlasInt, ihiz: BlasInt, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `slaqr1` | `None` | `n: BlasInt, h: float32, ldh: BlasInt, sr1: float32, si1: float32, sr2: float32, si2: float32, v: float32` |
| `slaqr2` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nw: BlasInt, h: float32, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: float32, ldz: BlasInt, ns: BlasInt, nd: BlasInt, sr: float32, si: float32, v: float32, ldv: BlasInt, nh: BlasInt, t: float32, ldt: BlasInt, nv: BlasInt, wv: float32, ldwv: BlasInt, work: float32, lwork: BlasInt` |
| `slaqr3` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nw: BlasInt, h: float32, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: float32, ldz: BlasInt, ns: BlasInt, nd: BlasInt, sr: float32, si: float32, v: float32, ldv: BlasInt, nh: BlasInt, t: float32, ldt: BlasInt, nv: BlasInt, wv: float32, ldwv: BlasInt, work: float32, lwork: BlasInt` |
| `slaqr4` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: float32, ldh: BlasInt, wr: float32, wi: float32, iloz: BlasInt, ihiz: BlasInt, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `slaqr5` | `None` | `wantt: bool, wantz: bool, kacc22: BlasInt, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nshfts: BlasInt, sr: float32, si: float32, h: float32, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: float32, ldz: BlasInt, v: float32, ldv: BlasInt, u: float32, ldu: BlasInt, nv: BlasInt, wv: float32, ldwv: BlasInt, nh: BlasInt, wh: float32, ldwh: BlasInt` |
| `slaqsb` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, s: float32, scond: float32, amax: float32, equed: uint8` |
| `slaqsp` | `None` | `uplo: uint8, n: BlasInt, ap: float32, s: float32, scond: float32, amax: float32, equed: uint8` |
| `slaqsy` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, s: float32, scond: float32, amax: float32, equed: uint8` |
| `slaqtr` | `None` | `ltran: bool, lreal: bool, n: BlasInt, t: float32, ldt: BlasInt, b: float32, w: float32, scale: float32, x: float32, work: float32, info: BlasInt` |
| `slar1v` | `None` | `n: BlasInt, b1: BlasInt, bn: BlasInt, lambda_: float32, d: float32, l: float32, ld: float32, lld: float32, pivmin: float32, gaptol: float32, z: float32, wantnc: bool, negcnt: BlasInt, ztz: float32, mingma: float32, r: BlasInt, isuppz: BlasInt, nrminv: float32, resid: float32, rqcorr: float32, work: float32` |
| `slar2v` | `None` | `n: BlasInt, x: float32, y: float32, z: float32, incx: BlasInt, c: float32, s: float32, incc: BlasInt` |
| `slarf` | `None` | `side: uint8, m: BlasInt, n: BlasInt, v: float32, incv: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32` |
| `slarfb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, v: float32, ldv: BlasInt, t: float32, ldt: BlasInt, c: float32, ldc: BlasInt, work: float32, ldwork: BlasInt` |
| `slarfg` | `None` | `n: BlasInt, alpha: float32, x: float32, incx: BlasInt, tau: float32` |
| `slarfgp` | `None` | `n: BlasInt, alpha: float32, x: float32, incx: BlasInt, tau: float32` |
| `slarft` | `None` | `direct: uint8, storev: uint8, n: BlasInt, k: BlasInt, v: float32, ldv: BlasInt, tau: float32, t: float32, ldt: BlasInt` |
| `slarfx` | `None` | `side: uint8, m: BlasInt, n: BlasInt, v: float32, tau: float32, c: float32, ldc: BlasInt, work: float32` |
| `slargv` | `None` | `n: BlasInt, x: float32, incx: BlasInt, y: float32, incy: BlasInt, c: float32, incc: BlasInt` |
| `slarnv` | `None` | `idist: BlasInt, iseed: BlasInt, n: BlasInt, x: float32` |
| `slarra` | `None` | `n: BlasInt, d: float32, e: float32, e2: float32, spltol: float32, tnrm: float32, nsplit: BlasInt, isplit: BlasInt, info: BlasInt` |
| `slarrb` | `None` | `n: BlasInt, d: float32, lld: float32, ifirst: BlasInt, ilast: BlasInt, rtol1: float32, rtol2: float32, offset: BlasInt, w: float32, wgap: float32, werr: float32, work: float32, iwork: BlasInt, pivmin: float32, spdiam: float32, twist: BlasInt, info: BlasInt` |
| `slarrc` | `None` | `jobt: uint8, n: BlasInt, vl: float32, vu: float32, d: float32, e: float32, pivmin: float32, eigcnt: BlasInt, lcnt: BlasInt, rcnt: BlasInt, info: BlasInt` |
| `slarrd` | `None` | `range: uint8, order: uint8, n: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, gers: float32, reltol: float32, d: float32, e: float32, e2: float32, pivmin: float32, nsplit: BlasInt, isplit: BlasInt, m: BlasInt, w: float32, werr: float32, wl: float32, wu: float32, iblock: BlasInt, indexw: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `slarre` | `None` | `range: uint8, n: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, d: float32, e: float32, e2: float32, rtol1: float32, rtol2: float32, spltol: float32, nsplit: BlasInt, isplit: BlasInt, m: BlasInt, w: float32, werr: float32, wgap: float32, iblock: BlasInt, indexw: BlasInt, gers: float32, pivmin: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `slarrf` | `None` | `n: BlasInt, d: float32, l: float32, ld: float32, clstrt: BlasInt, clend: BlasInt, w: float32, wgap: float32, werr: float32, spdiam: float32, clgapl: float32, clgapr: float32, pivmin: float32, sigma: float32, dplus: float32, lplus: float32, work: float32, info: BlasInt` |
| `slarrj` | `None` | `n: BlasInt, d: float32, e2: float32, ifirst: BlasInt, ilast: BlasInt, rtol: float32, offset: BlasInt, w: float32, werr: float32, work: float32, iwork: BlasInt, pivmin: float32, spdiam: float32, info: BlasInt` |
| `slarrk` | `None` | `n: BlasInt, iw: BlasInt, gl: float32, gu: float32, d: float32, e2: float32, pivmin: float32, reltol: float32, w: float32, werr: float32, info: BlasInt` |
| `slarrr` | `None` | `n: BlasInt, d: float32, e: float32, info: BlasInt` |
| `slarrv` | `None` | `n: BlasInt, vl: float32, vu: float32, d: float32, l: float32, pivmin: float32, isplit: BlasInt, m: BlasInt, dol: BlasInt, dou: BlasInt, minrgp: float32, rtol1: float32, rtol2: float32, w: float32, werr: float32, wgap: float32, iblock: BlasInt, indexw: BlasInt, gers: float32, z: float32, ldz: BlasInt, isuppz: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `slartg` | `None` | `f: float32, g: float32, cs: float32, sn: float32, r: float32` |
| `slartgp` | `None` | `f: float32, g: float32, cs: float32, sn: float32, r: float32` |
| `slartgs` | `None` | `x: float32, y: float32, sigma: float32, cs: float32, sn: float32` |
| `slartv` | `None` | `n: BlasInt, x: float32, incx: BlasInt, y: float32, incy: BlasInt, c: float32, s: float32, incc: BlasInt` |
| `slaruv` | `None` | `iseed: BlasInt, n: BlasInt, x: float32` |
| `slarz` | `None` | `side: uint8, m: BlasInt, n: BlasInt, l: BlasInt, v: float32, incv: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32` |
| `slarzb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, v: float32, ldv: BlasInt, t: float32, ldt: BlasInt, c: float32, ldc: BlasInt, work: float32, ldwork: BlasInt` |
| `slarzt` | `None` | `direct: uint8, storev: uint8, n: BlasInt, k: BlasInt, v: float32, ldv: BlasInt, tau: float32, t: float32, ldt: BlasInt` |
| `slas2` | `None` | `f: float32, g: float32, h: float32, ssmin: float32, ssmax: float32` |
| `slascl` | `None` | `type_bn: uint8, kl: BlasInt, ku: BlasInt, cfrom: float32, cto: float32, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, info: BlasInt` |
| `slasd0` | `None` | `n: BlasInt, sqre: BlasInt, d: float32, e: float32, u: float32, ldu: BlasInt, vt: float32, ldvt: BlasInt, smlsiz: BlasInt, iwork: BlasInt, work: float32, info: BlasInt` |
| `slasd1` | `None` | `nl: BlasInt, nr: BlasInt, sqre: BlasInt, d: float32, alpha: float32, beta: float32, u: float32, ldu: BlasInt, vt: float32, ldvt: BlasInt, idxq: BlasInt, iwork: BlasInt, work: float32, info: BlasInt` |
| `slasd2` | `None` | `nl: BlasInt, nr: BlasInt, sqre: BlasInt, k: BlasInt, d: float32, z: float32, alpha: float32, beta: float32, u: float32, ldu: BlasInt, vt: float32, ldvt: BlasInt, dsigma: float32, u2: float32, ldu2: BlasInt, vt2: float32, ldvt2: BlasInt, idxp: BlasInt, idx: BlasInt, idxc: BlasInt, idxq: BlasInt, coltyp: BlasInt, info: BlasInt` |
| `slasd3` | `None` | `nl: BlasInt, nr: BlasInt, sqre: BlasInt, k: BlasInt, d: float32, q: float32, ldq: BlasInt, dsigma: float32, u: float32, ldu: BlasInt, u2: float32, ldu2: BlasInt, vt: float32, ldvt: BlasInt, vt2: float32, ldvt2: BlasInt, idxc: BlasInt, ctot: BlasInt, z: float32, info: BlasInt` |
| `slasd4` | `None` | `n: BlasInt, i: BlasInt, d: float32, z: float32, delta: float32, rho: float32, sigma: float32, work: float32, info: BlasInt` |
| `slasd5` | `None` | `i: BlasInt, d: float32, z: float32, delta: float32, rho: float32, dsigma: float32, work: float32` |
| `slasd6` | `None` | `icompq: BlasInt, nl: BlasInt, nr: BlasInt, sqre: BlasInt, d: float32, vf: float32, vl: float32, alpha: float32, beta: float32, idxq: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, givnum: float32, ldgnum: BlasInt, poles: float32, difl: float32, difr: float32, z: float32, k: BlasInt, c: float32, s: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `slasd7` | `None` | `icompq: BlasInt, nl: BlasInt, nr: BlasInt, sqre: BlasInt, k: BlasInt, d: float32, z: float32, zw: float32, vf: float32, vfw: float32, vl: float32, vlw: float32, alpha: float32, beta: float32, dsigma: float32, idx: BlasInt, idxp: BlasInt, idxq: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, givnum: float32, ldgnum: BlasInt, c: float32, s: float32, info: BlasInt` |
| `slasd8` | `None` | `icompq: BlasInt, k: BlasInt, d: float32, z: float32, vf: float32, vl: float32, difl: float32, difr: float32, lddifr: BlasInt, dsigma: float32, work: float32, info: BlasInt` |
| `slasda` | `None` | `icompq: BlasInt, smlsiz: BlasInt, n: BlasInt, sqre: BlasInt, d: float32, e: float32, u: float32, ldu: BlasInt, vt: float32, k: BlasInt, difl: float32, difr: float32, z: float32, poles: float32, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, perm: BlasInt, givnum: float32, c: float32, s: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `slasdq` | `None` | `uplo: uint8, sqre: BlasInt, n: BlasInt, ncvt: BlasInt, nru: BlasInt, ncc: BlasInt, d: float32, e: float32, vt: float32, ldvt: BlasInt, u: float32, ldu: BlasInt, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `slasdt` | `None` | `n: BlasInt, lvl: BlasInt, nd: BlasInt, inode: BlasInt, ndiml: BlasInt, ndimr: BlasInt, msub: BlasInt` |
| `slaset` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, alpha: float32, beta: float32, a: float32, lda: BlasInt` |
| `slasq1` | `None` | `n: BlasInt, d: float32, e: float32, work: float32, info: BlasInt` |
| `slasq2` | `None` | `n: BlasInt, z: float32, info: BlasInt` |
| `slasq3` | `None` | `i0: BlasInt, n0: BlasInt, z: float32, pp: BlasInt, dmin: float32, sigma: float32, desig: float32, qmax: float32, nfail: BlasInt, iter: BlasInt, ndiv: BlasInt, ieee: bool, ttype: BlasInt, dmin1: float32, dmin2: float32, dn: float32, dn1: float32, dn2: float32, g: float32, tau: float32` |
| `slasq4` | `None` | `i0: BlasInt, n0: BlasInt, z: float32, pp: BlasInt, n0in: BlasInt, dmin: float32, dmin1: float32, dmin2: float32, dn: float32, dn1: float32, dn2: float32, tau: float32, ttype: BlasInt, g: float32` |
| `slasq6` | `None` | `i0: BlasInt, n0: BlasInt, z: float32, pp: BlasInt, dmin: float32, dmin1: float32, dmin2: float32, dn: float32, dnm1: float32, dnm2: float32` |
| `slasr` | `None` | `side: uint8, pivot: uint8, direct: uint8, m: BlasInt, n: BlasInt, c: float32, s: float32, a: float32, lda: BlasInt` |
| `slasrt` | `None` | `id: uint8, n: BlasInt, d: float32, info: BlasInt` |
| `slassq` | `None` | `n: BlasInt, x: float32, incx: BlasInt, scale: float32, sumsq: float32` |
| `slasv2` | `None` | `f: float32, g: float32, h: float32, ssmin: float32, ssmax: float32, snr: float32, csr: float32, snl: float32, csl: float32` |
| `slaswp` | `None` | `n: BlasInt, a: float32, lda: BlasInt, k1: BlasInt, k2: BlasInt, ipiv: BlasInt, incx: BlasInt` |
| `slasy2` | `None` | `ltranl: bool, ltranr: bool, isgn: BlasInt, n1: BlasInt, n2: BlasInt, tl: float32, ldtl: BlasInt, tr: float32, ldtr: BlasInt, b: float32, ldb: BlasInt, scale: float32, x: float32, ldx: BlasInt, xnorm: float32, info: BlasInt` |
| `slasyf` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, kb: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, w: float32, ldw: BlasInt, info: BlasInt` |
| `slatbs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, x: float32, scale: float32, cnorm: float32, info: BlasInt` |
| `slatdf` | `None` | `ijob: BlasInt, n: BlasInt, z: float32, ldz: BlasInt, rhs: float32, rdsum: float32, rdscal: float32, ipiv: BlasInt, jpiv: BlasInt` |
| `slatps` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, ap: float32, x: float32, scale: float32, cnorm: float32, info: BlasInt` |
| `slatrd` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, a: float32, lda: BlasInt, e: float32, tau: float32, w: float32, ldw: BlasInt` |
| `slatrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, a: float32, lda: BlasInt, x: float32, scale: float32, cnorm: float32, info: BlasInt` |
| `slatrz` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32` |
| `slauu2` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, info: BlasInt` |
| `slauum` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, info: BlasInt` |
| `snrm2` | `np.float32` | `n: BlasInt, x: float32, incx: BlasInt` |
| `sopgtr` | `None` | `uplo: uint8, n: BlasInt, ap: float32, tau: float32, q: float32, ldq: BlasInt, work: float32, info: BlasInt` |
| `sopmtr` | `None` | `side: uint8, uplo: uint8, trans: uint8, m: BlasInt, n: BlasInt, ap: float32, tau: float32, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `sorbdb` | `None` | `trans: uint8, signs: uint8, m: BlasInt, p: BlasInt, q: BlasInt, x11: float32, ldx11: BlasInt, x12: float32, ldx12: BlasInt, x21: float32, ldx21: BlasInt, x22: float32, ldx22: BlasInt, theta: float32, phi: float32, taup1: float32, taup2: float32, tauq1: float32, tauq2: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorcsd` | `None` | `jobu1: uint8, jobu2: uint8, jobv1t: uint8, jobv2t: uint8, trans: uint8, signs: uint8, m: BlasInt, p: BlasInt, q: BlasInt, x11: float32, ldx11: BlasInt, x12: float32, ldx12: BlasInt, x21: float32, ldx21: BlasInt, x22: float32, ldx22: BlasInt, theta: float32, u1: float32, ldu1: BlasInt, u2: float32, ldu2: BlasInt, v1t: float32, ldv1t: BlasInt, v2t: float32, ldv2t: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `sorg2l` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sorg2r` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sorgbr` | `None` | `vect: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorghr` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorgl2` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sorglq` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorgql` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorgqr` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorgr2` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, info: BlasInt` |
| `sorgrq` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorgtr` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorm2l` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `sorm2r` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `sormbr` | `None` | `vect: uint8, side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sormhr` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sorml2` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `sormlq` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sormql` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sormqr` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sormr2` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `sormr3` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, info: BlasInt` |
| `sormrq` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sormrz` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `sormtr` | `None` | `side: uint8, uplo: uint8, trans: uint8, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, c: float32, ldc: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `spbcon` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, anorm: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `spbequ` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, s: float32, scond: float32, amax: float32, info: BlasInt` |
| `spbrfs` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, afb: float32, ldafb: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `spbstf` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, info: BlasInt` |
| `spbsv` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `spbsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, afb: float32, ldafb: BlasInt, equed: uint8, s: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `spbtf2` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, info: BlasInt` |
| `spbtrf` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, info: BlasInt` |
| `spbtrs` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `spftrf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: float32, info: BlasInt` |
| `spftri` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: float32, info: BlasInt` |
| `spftrs` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, b: float32, ldb: BlasInt, info: BlasInt` |
| `spocon` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, anorm: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `spoequ` | `None` | `n: BlasInt, a: float32, lda: BlasInt, s: float32, scond: float32, amax: float32, info: BlasInt` |
| `spoequb` | `None` | `n: BlasInt, a: float32, lda: BlasInt, s: float32, scond: float32, amax: float32, info: BlasInt` |
| `sporfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, af: float32, ldaf: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sposv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sposvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, af: float32, ldaf: BlasInt, equed: uint8, s: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `spotf2` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, info: BlasInt` |
| `spotrf` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, info: BlasInt` |
| `spotri` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, info: BlasInt` |
| `spotrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sppcon` | `None` | `uplo: uint8, n: BlasInt, ap: float32, anorm: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sppequ` | `None` | `uplo: uint8, n: BlasInt, ap: float32, s: float32, scond: float32, amax: float32, info: BlasInt` |
| `spprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, afp: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sppsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, b: float32, ldb: BlasInt, info: BlasInt` |
| `sppsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, afp: float32, equed: uint8, s: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `spptrf` | `None` | `uplo: uint8, n: BlasInt, ap: float32, info: BlasInt` |
| `spptri` | `None` | `uplo: uint8, n: BlasInt, ap: float32, info: BlasInt` |
| `spptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, b: float32, ldb: BlasInt, info: BlasInt` |
| `spstf2` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, piv: BlasInt, rank: BlasInt, tol: float32, work: float32, info: BlasInt` |
| `spstrf` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, piv: BlasInt, rank: BlasInt, tol: float32, work: float32, info: BlasInt` |
| `sptcon` | `None` | `n: BlasInt, d: float32, e: float32, anorm: float32, rcond: float32, work: float32, info: BlasInt` |
| `spteqr` | `None` | `compz: uint8, n: BlasInt, d: float32, e: float32, z: float32, ldz: BlasInt, work: float32, info: BlasInt` |
| `sptrfs` | `None` | `n: BlasInt, nrhs: BlasInt, d: float32, e: float32, df: float32, ef: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, info: BlasInt` |
| `sptsv` | `None` | `n: BlasInt, nrhs: BlasInt, d: float32, e: float32, b: float32, ldb: BlasInt, info: BlasInt` |
| `sptsvx` | `None` | `fact: uint8, n: BlasInt, nrhs: BlasInt, d: float32, e: float32, df: float32, ef: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, info: BlasInt` |
| `spttrf` | `None` | `n: BlasInt, d: float32, e: float32, info: BlasInt` |
| `spttrs` | `None` | `n: BlasInt, nrhs: BlasInt, d: float32, e: float32, b: float32, ldb: BlasInt, info: BlasInt` |
| `sptts2` | `None` | `n: BlasInt, nrhs: BlasInt, d: float32, e: float32, b: float32, ldb: BlasInt` |
| `srot` | `None` | `n: BlasInt, sx: float32, incx: BlasInt, sy: float32, incy: BlasInt, c: float32, s: float32` |
| `srotg` | `None` | `sa: float32, sb: float32, c: float32, s: float32` |
| `srotm` | `None` | `n: BlasInt, sx: float32, incx: BlasInt, sy: float32, incy: BlasInt, sparam: float32` |
| `srotmg` | `None` | `sd1: float32, sd2: float32, sx1: float32, sy1: float32, sparam: float32` |
| `srscl` | `None` | `n: BlasInt, sa: float32, sx: float32, incx: BlasInt` |
| `ssbev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, info: BlasInt` |
| `ssbevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `ssbevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, q: float32, ldq: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `ssbgst` | `None` | `vect: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: float32, ldab: BlasInt, bb: float32, ldbb: BlasInt, x: float32, ldx: BlasInt, work: float32, info: BlasInt` |
| `ssbgv` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: float32, ldab: BlasInt, bb: float32, ldbb: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, info: BlasInt` |
| `ssbgvd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: float32, ldab: BlasInt, bb: float32, ldbb: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `ssbgvx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: float32, ldab: BlasInt, bb: float32, ldbb: BlasInt, q: float32, ldq: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `ssbmv` | `None` | `uplo: uint8, n: BlasInt, k: BlasInt, alpha: float32, a: float32, lda: BlasInt, x: float32, incx: BlasInt, beta: float32, y: float32, incy: BlasInt` |
| `ssbtrd` | `None` | `vect: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, d: float32, e: float32, q: float32, ldq: BlasInt, work: float32, info: BlasInt` |
| `sscal` | `None` | `n: BlasInt, sa: float32, sx: float32, incx: BlasInt` |
| `ssfrk` | `None` | `transr: uint8, uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float32, a: float32, lda: BlasInt, beta: float32, c: float32` |
| `sspcon` | `None` | `uplo: uint8, n: BlasInt, ap: float32, ipiv: BlasInt, anorm: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sspev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ap: float32, w: float32, z: float32, ldz: BlasInt, work: float32, info: BlasInt` |
| `sspevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ap: float32, w: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `sspevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ap: float32, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `sspgst` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, ap: float32, bp: float32, info: BlasInt` |
| `sspgv` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, ap: float32, bp: float32, w: float32, z: float32, ldz: BlasInt, work: float32, info: BlasInt` |
| `sspgvd` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, ap: float32, bp: float32, w: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `sspgvx` | `None` | `itype: BlasInt, jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ap: float32, bp: float32, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `sspmv` | `None` | `uplo: uint8, n: BlasInt, alpha: float32, ap: float32, x: float32, incx: BlasInt, beta: float32, y: float32, incy: BlasInt` |
| `sspr` | `None` | `uplo: uint8, n: BlasInt, alpha: float32, x: float32, incx: BlasInt, ap: float32` |
| `sspr2` | `None` | `uplo: uint8, n: BlasInt, alpha: float32, x: float32, incx: BlasInt, y: float32, incy: BlasInt, ap: float32` |
| `ssprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, afp: float32, ipiv: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `sspsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, ipiv: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sspsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, afp: float32, ipiv: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `ssptrd` | `None` | `uplo: uint8, n: BlasInt, ap: float32, d: float32, e: float32, tau: float32, info: BlasInt` |
| `ssptrf` | `None` | `uplo: uint8, n: BlasInt, ap: float32, ipiv: BlasInt, info: BlasInt` |
| `ssptri` | `None` | `uplo: uint8, n: BlasInt, ap: float32, ipiv: BlasInt, work: float32, info: BlasInt` |
| `ssptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, ipiv: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `sstebz` | `None` | `range: uint8, order: uint8, n: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, d: float32, e: float32, m: BlasInt, nsplit: BlasInt, w: float32, iblock: BlasInt, isplit: BlasInt, work: float32, iwork: BlasInt, info: BlasInt` |
| `sstedc` | `None` | `compz: uint8, n: BlasInt, d: float32, e: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `sstegr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float32, e: float32, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, isuppz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `sstein` | `None` | `n: BlasInt, d: float32, e: float32, m: BlasInt, w: float32, iblock: BlasInt, isplit: BlasInt, z: float32, ldz: BlasInt, work: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `sstemr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float32, e: float32, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, m: BlasInt, w: float32, z: float32, ldz: BlasInt, nzc: BlasInt, isuppz: BlasInt, tryrac: bool, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `ssteqr` | `None` | `compz: uint8, n: BlasInt, d: float32, e: float32, z: float32, ldz: BlasInt, work: float32, info: BlasInt` |
| `ssterf` | `None` | `n: BlasInt, d: float32, e: float32, info: BlasInt` |
| `sstev` | `None` | `jobz: uint8, n: BlasInt, d: float32, e: float32, z: float32, ldz: BlasInt, work: float32, info: BlasInt` |
| `sstevd` | `None` | `jobz: uint8, n: BlasInt, d: float32, e: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `sstevr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float32, e: float32, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, isuppz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `sstevx` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float32, e: float32, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `sswap` | `None` | `n: BlasInt, sx: float32, incx: BlasInt, sy: float32, incy: BlasInt` |
| `ssycon` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, anorm: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `ssyconv` | `None` | `uplo: uint8, way: uint8, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, work: float32, info: BlasInt` |
| `ssyequb` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, s: float32, scond: float32, amax: float32, work: float32, info: BlasInt` |
| `ssyev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, w: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `ssyevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, w: float32, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `ssyevr` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, isuppz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `ssyevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `ssygs2` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `ssygst` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `ssygv` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, w: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `ssygvd` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, w: float32, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `ssygvx` | `None` | `itype: BlasInt, jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, vl: float32, vu: float32, il: BlasInt, iu: BlasInt, abstol: float32, m: BlasInt, w: float32, z: float32, ldz: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `ssymm` | `None` | `side: uint8, uplo: uint8, m: BlasInt, n: BlasInt, alpha: float32, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, beta: float32, c: float32, ldc: BlasInt` |
| `ssymv` | `None` | `uplo: uint8, n: BlasInt, alpha: float32, a: float32, lda: BlasInt, x: float32, incx: BlasInt, beta: float32, y: float32, incy: BlasInt` |
| `ssyr` | `None` | `uplo: uint8, n: BlasInt, alpha: float32, x: float32, incx: BlasInt, a: float32, lda: BlasInt` |
| `ssyr2` | `None` | `uplo: uint8, n: BlasInt, alpha: float32, x: float32, incx: BlasInt, y: float32, incy: BlasInt, a: float32, lda: BlasInt` |
| `ssyr2k` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float32, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, beta: float32, c: float32, ldc: BlasInt` |
| `ssyrfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, af: float32, ldaf: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `ssyrk` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float32, a: float32, lda: BlasInt, beta: float32, c: float32, ldc: BlasInt` |
| `ssysv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `ssysvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, af: float32, ldaf: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, rcond: float32, ferr: float32, berr: float32, work: float32, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `ssyswapr` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, i1: BlasInt, i2: BlasInt` |
| `ssytd2` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, d: float32, e: float32, tau: float32, info: BlasInt` |
| `ssytf2` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `ssytrd` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, d: float32, e: float32, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `ssytrf` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `ssytri` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, work: float32, info: BlasInt` |
| `ssytri2` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `ssytri2x` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, work: float32, nb: BlasInt, info: BlasInt` |
| `ssytrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `ssytrs2` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, ipiv: BlasInt, b: float32, ldb: BlasInt, work: float32, info: BlasInt` |
| `stbcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, kd: BlasInt, ab: float32, ldab: BlasInt, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `stbmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, x: float32, incx: BlasInt` |
| `stbrfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `stbsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, k: BlasInt, a: float32, lda: BlasInt, x: float32, incx: BlasInt` |
| `stbtrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: float32, ldab: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `stfsm` | `None` | `transr: uint8, side: uint8, uplo: uint8, trans: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: float32, a: float32, b: float32, ldb: BlasInt` |
| `stftri` | `None` | `transr: uint8, uplo: uint8, diag: uint8, n: BlasInt, a: float32, info: BlasInt` |
| `stfttp` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, arf: float32, ap: float32, info: BlasInt` |
| `stfttr` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, arf: float32, a: float32, lda: BlasInt, info: BlasInt` |
| `stgevc` | `None` | `side: uint8, howmny: uint8, select: bool, n: BlasInt, s: float32, lds: BlasInt, p: float32, ldp: BlasInt, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: float32, info: BlasInt` |
| `stgex2` | `None` | `wantq: bool, wantz: bool, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, q: float32, ldq: BlasInt, z: float32, ldz: BlasInt, j1: BlasInt, n1: BlasInt, n2: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `stgexc` | `None` | `wantq: bool, wantz: bool, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, q: float32, ldq: BlasInt, z: float32, ldz: BlasInt, ifst: BlasInt, ilst: BlasInt, work: float32, lwork: BlasInt, info: BlasInt` |
| `stgsen` | `None` | `ijob: BlasInt, wantq: bool, wantz: bool, select: bool, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, alphar: float32, alphai: float32, beta: float32, q: float32, ldq: BlasInt, z: float32, ldz: BlasInt, m: BlasInt, pl: float32, pr: float32, dif: float32, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `stgsja` | `None` | `jobu: uint8, jobv: uint8, jobq: uint8, m: BlasInt, p: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, tola: float32, tolb: float32, alpha: float32, beta: float32, u: float32, ldu: BlasInt, v: float32, ldv: BlasInt, q: float32, ldq: BlasInt, work: float32, ncycle: BlasInt, info: BlasInt` |
| `stgsna` | `None` | `job: uint8, howmny: uint8, select: bool, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, s: float32, dif: float32, mm: BlasInt, m: BlasInt, work: float32, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `stgsy2` | `None` | `trans: uint8, ijob: BlasInt, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, c: float32, ldc: BlasInt, d: float32, ldd: BlasInt, e: float32, lde: BlasInt, f: float32, ldf: BlasInt, scale: float32, rdsum: float32, rdscal: float32, iwork: BlasInt, pq: BlasInt, info: BlasInt` |
| `stgsyl` | `None` | `trans: uint8, ijob: BlasInt, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, c: float32, ldc: BlasInt, d: float32, ldd: BlasInt, e: float32, lde: BlasInt, f: float32, ldf: BlasInt, scale: float32, dif: float32, work: float32, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `stpcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, ap: float32, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `stpmqrt` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, nb: BlasInt, v: float32, ldv: BlasInt, t: float32, ldt: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, work: float32, info: BlasInt` |
| `stpmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, ap: float32, x: float32, incx: BlasInt` |
| `stpqrt` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, nb: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, t: float32, ldt: BlasInt, work: float32, info: BlasInt` |
| `stpqrt2` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, t: float32, ldt: BlasInt, info: BlasInt` |
| `stprfb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, v: float32, ldv: BlasInt, t: float32, ldt: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, work: float32, ldwork: BlasInt` |
| `stprfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `stpsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, ap: float32, x: float32, incx: BlasInt` |
| `stptri` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, ap: float32, info: BlasInt` |
| `stptrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, ap: float32, b: float32, ldb: BlasInt, info: BlasInt` |
| `stpttf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, ap: float32, arf: float32, info: BlasInt` |
| `stpttr` | `None` | `uplo: uint8, n: BlasInt, ap: float32, a: float32, lda: BlasInt, info: BlasInt` |
| `strcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, a: float32, lda: BlasInt, rcond: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `strevc` | `None` | `side: uint8, howmny: uint8, select: bool, n: BlasInt, t: float32, ldt: BlasInt, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: float32, info: BlasInt` |
| `strexc` | `None` | `compq: uint8, n: BlasInt, t: float32, ldt: BlasInt, q: float32, ldq: BlasInt, ifst: BlasInt, ilst: BlasInt, work: float32, info: BlasInt` |
| `strmm` | `None` | `side: uint8, uplo: uint8, transa: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: float32, a: float32, lda: BlasInt, b: float32, ldb: BlasInt` |
| `strmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, a: float32, lda: BlasInt, x: float32, incx: BlasInt` |
| `strrfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, x: float32, ldx: BlasInt, ferr: float32, berr: float32, work: float32, iwork: BlasInt, info: BlasInt` |
| `strsen` | `None` | `job: uint8, compq: uint8, select: bool, n: BlasInt, t: float32, ldt: BlasInt, q: float32, ldq: BlasInt, wr: float32, wi: float32, m: BlasInt, s: float32, sep: float32, work: float32, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `strsm` | `None` | `side: uint8, uplo: uint8, transa: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: float32, a: float32, lda: BlasInt, b: float32, ldb: BlasInt` |
| `strsna` | `None` | `job: uint8, howmny: uint8, select: bool, n: BlasInt, t: float32, ldt: BlasInt, vl: float32, ldvl: BlasInt, vr: float32, ldvr: BlasInt, s: float32, sep: float32, mm: BlasInt, m: BlasInt, work: float32, ldwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `strsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, a: float32, lda: BlasInt, x: float32, incx: BlasInt` |
| `strsyl` | `None` | `trana: uint8, tranb: uint8, isgn: BlasInt, m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, c: float32, ldc: BlasInt, scale: float32, info: BlasInt` |
| `strti2` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, a: float32, lda: BlasInt, info: BlasInt` |
| `strtri` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, a: float32, lda: BlasInt, info: BlasInt` |
| `strtrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, a: float32, lda: BlasInt, b: float32, ldb: BlasInt, info: BlasInt` |
| `strttf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, arf: float32, info: BlasInt` |
| `strttp` | `None` | `uplo: uint8, n: BlasInt, a: float32, lda: BlasInt, ap: float32, info: BlasInt` |
| `stzrzf` | `None` | `m: BlasInt, n: BlasInt, a: float32, lda: BlasInt, tau: float32, work: float32, lwork: BlasInt, info: BlasInt` |
| `xerbla_array` | `None` | `srname_array: uint8, srname_len: BlasInt, info: BlasInt` |
| `zaxpy` | `None` | `n: BlasInt, za: complex128, zx: complex128, incx: BlasInt, zy: complex128, incy: BlasInt` |
| `zbbcsd` | `None` | `jobu1: uint8, jobu2: uint8, jobv1t: uint8, jobv2t: uint8, trans: uint8, m: BlasInt, p: BlasInt, q: BlasInt, theta: float64, phi: float64, u1: complex128, ldu1: BlasInt, u2: complex128, ldu2: BlasInt, v1t: complex128, ldv1t: BlasInt, v2t: complex128, ldv2t: BlasInt, b11d: float64, b11e: float64, b12d: float64, b12e: float64, b21d: float64, b21e: float64, b22d: float64, b22e: float64, rwork: float64, lrwork: BlasInt, info: BlasInt` |
| `zbdsqr` | `None` | `uplo: uint8, n: BlasInt, ncvt: BlasInt, nru: BlasInt, ncc: BlasInt, d: float64, e: float64, vt: complex128, ldvt: BlasInt, u: complex128, ldu: BlasInt, c: complex128, ldc: BlasInt, rwork: float64, info: BlasInt` |
| `zcgesv` | `None` | `n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, work: complex128, swork: complex64, rwork: float64, iter: BlasInt, info: BlasInt` |
| `zcopy` | `None` | `n: BlasInt, zx: complex128, incx: BlasInt, zy: complex128, incy: BlasInt` |
| `zcposv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, work: complex128, swork: complex64, rwork: float64, iter: BlasInt, info: BlasInt` |
| `zdotc` | `np.complex128` | `n: BlasInt, zx: complex128, incx: BlasInt, zy: complex128, incy: BlasInt` |
| `zdotu` | `np.complex128` | `n: BlasInt, zx: complex128, incx: BlasInt, zy: complex128, incy: BlasInt` |
| `zdrot` | `None` | `n: BlasInt, cx: complex128, incx: BlasInt, cy: complex128, incy: BlasInt, c: float64, s: float64` |
| `zdrscl` | `None` | `n: BlasInt, sa: float64, sx: complex128, incx: BlasInt` |
| `zdscal` | `None` | `n: BlasInt, da: float64, zx: complex128, incx: BlasInt` |
| `zgbbrd` | `None` | `vect: uint8, m: BlasInt, n: BlasInt, ncc: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex128, ldab: BlasInt, d: float64, e: float64, q: complex128, ldq: BlasInt, pt: complex128, ldpt: BlasInt, c: complex128, ldc: BlasInt, work: complex128, rwork: float64, info: BlasInt` |
| `zgbcon` | `None` | `norm: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex128, ldab: BlasInt, ipiv: BlasInt, anorm: float64, rcond: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zgbequ` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex128, ldab: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, info: BlasInt` |
| `zgbequb` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex128, ldab: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, info: BlasInt` |
| `zgbmv` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt, beta: complex128, y: complex128, incy: BlasInt` |
| `zgbrfs` | `None` | `trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, afb: complex128, ldafb: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zgbsv` | `None` | `n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zgbsvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, afb: complex128, ldafb: BlasInt, ipiv: BlasInt, equed: uint8, r: float64, c: float64, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zgbtf2` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex128, ldab: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `zgbtrf` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex128, ldab: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `zgbtrs` | `None` | `trans: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zgebak` | `None` | `job: uint8, side: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float64, m: BlasInt, v: complex128, ldv: BlasInt, info: BlasInt` |
| `zgebal` | `None` | `job: uint8, n: BlasInt, a: complex128, lda: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float64, info: BlasInt` |
| `zgebd2` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, d: float64, e: float64, tauq: complex128, taup: complex128, work: complex128, info: BlasInt` |
| `zgebrd` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, d: float64, e: float64, tauq: complex128, taup: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgecon` | `None` | `norm: uint8, n: BlasInt, a: complex128, lda: BlasInt, anorm: float64, rcond: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zgeequ` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, info: BlasInt` |
| `zgeequb` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, info: BlasInt` |
| `zgeev` | `None` | `jobvl: uint8, jobvr: uint8, n: BlasInt, a: complex128, lda: BlasInt, w: complex128, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zgeevx` | `None` | `balanc: uint8, jobvl: uint8, jobvr: uint8, sense: uint8, n: BlasInt, a: complex128, lda: BlasInt, w: complex128, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, ilo: BlasInt, ihi: BlasInt, scale: float64, abnrm: float64, rconde: float64, rcondv: float64, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zgehd2` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zgehrd` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgelq2` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zgelqf` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgels` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgelsd` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, s: float64, rcond: float64, rank: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, iwork: BlasInt, info: BlasInt` |
| `zgelss` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, s: float64, rcond: float64, rank: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zgelsy` | `None` | `m: BlasInt, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, jpvt: BlasInt, rcond: float64, rank: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zgemm` | `None` | `transa: uint8, transb: uint8, m: BlasInt, n: BlasInt, k: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, beta: complex128, c: complex128, ldc: BlasInt` |
| `zgemqrt` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, nb: BlasInt, v: complex128, ldv: BlasInt, t: complex128, ldt: BlasInt, c: complex128, ldc: BlasInt, work: complex128, info: BlasInt` |
| `zgemv` | `None` | `trans: uint8, m: BlasInt, n: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt, beta: complex128, y: complex128, incy: BlasInt` |
| `zgeql2` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zgeqlf` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgeqp3` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, jpvt: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zgeqr2` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zgeqr2p` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zgeqrf` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgeqrfp` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgeqrt` | `None` | `m: BlasInt, n: BlasInt, nb: BlasInt, a: complex128, lda: BlasInt, t: complex128, ldt: BlasInt, work: complex128, info: BlasInt` |
| `zgeqrt2` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, t: complex128, ldt: BlasInt, info: BlasInt` |
| `zgeqrt3` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, t: complex128, ldt: BlasInt, info: BlasInt` |
| `zgerc` | `None` | `m: BlasInt, n: BlasInt, alpha: complex128, x: complex128, incx: BlasInt, y: complex128, incy: BlasInt, a: complex128, lda: BlasInt` |
| `zgerfs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, af: complex128, ldaf: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zgerq2` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zgerqf` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgeru` | `None` | `m: BlasInt, n: BlasInt, alpha: complex128, x: complex128, incx: BlasInt, y: complex128, incy: BlasInt, a: complex128, lda: BlasInt` |
| `zgesc2` | `None` | `n: BlasInt, a: complex128, lda: BlasInt, rhs: complex128, ipiv: BlasInt, jpiv: BlasInt, scale: float64` |
| `zgesdd` | `None` | `jobz: uint8, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, s: float64, u: complex128, ldu: BlasInt, vt: complex128, ldvt: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, iwork: BlasInt, info: BlasInt` |
| `zgesv` | `None` | `n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zgesvd` | `None` | `jobu: uint8, jobvt: uint8, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, s: float64, u: complex128, ldu: BlasInt, vt: complex128, ldvt: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zgesvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, af: complex128, ldaf: BlasInt, ipiv: BlasInt, equed: uint8, r: float64, c: float64, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zgetc2` | `None` | `n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, jpiv: BlasInt, info: BlasInt` |
| `zgetf2` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `zgetrf` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `zgetri` | `None` | `n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgetrs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zggbak` | `None` | `job: uint8, side: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float64, rscale: float64, m: BlasInt, v: complex128, ldv: BlasInt, info: BlasInt` |
| `zggbal` | `None` | `job: uint8, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float64, rscale: float64, work: float64, info: BlasInt` |
| `zggev` | `None` | `jobvl: uint8, jobvr: uint8, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, alpha: complex128, beta: complex128, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zggevx` | `None` | `balanc: uint8, jobvl: uint8, jobvr: uint8, sense: uint8, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, alpha: complex128, beta: complex128, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, ilo: BlasInt, ihi: BlasInt, lscale: float64, rscale: float64, abnrm: float64, bbnrm: float64, rconde: float64, rcondv: float64, work: complex128, lwork: BlasInt, rwork: float64, iwork: BlasInt, bwork: bool, info: BlasInt` |
| `zggglm` | `None` | `n: BlasInt, m: BlasInt, p: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, d: complex128, x: complex128, y: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgghrd` | `None` | `compq: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, q: complex128, ldq: BlasInt, z: complex128, ldz: BlasInt, info: BlasInt` |
| `zgglse` | `None` | `m: BlasInt, n: BlasInt, p: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, c: complex128, d: complex128, x: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zggqrf` | `None` | `n: BlasInt, m: BlasInt, p: BlasInt, a: complex128, lda: BlasInt, taua: complex128, b: complex128, ldb: BlasInt, taub: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zggrqf` | `None` | `m: BlasInt, p: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, taua: complex128, b: complex128, ldb: BlasInt, taub: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zgtcon` | `None` | `norm: uint8, n: BlasInt, dl: complex128, d: complex128, du: complex128, du2: complex128, ipiv: BlasInt, anorm: float64, rcond: float64, work: complex128, info: BlasInt` |
| `zgtrfs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, dl: complex128, d: complex128, du: complex128, dlf: complex128, df: complex128, duf: complex128, du2: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zgtsv` | `None` | `n: BlasInt, nrhs: BlasInt, dl: complex128, d: complex128, du: complex128, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zgtsvx` | `None` | `fact: uint8, trans: uint8, n: BlasInt, nrhs: BlasInt, dl: complex128, d: complex128, du: complex128, dlf: complex128, df: complex128, duf: complex128, du2: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zgttrf` | `None` | `n: BlasInt, dl: complex128, d: complex128, du: complex128, du2: complex128, ipiv: BlasInt, info: BlasInt` |
| `zgttrs` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, dl: complex128, d: complex128, du: complex128, du2: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zgtts2` | `None` | `itrans: BlasInt, n: BlasInt, nrhs: BlasInt, dl: complex128, d: complex128, du: complex128, du2: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt` |
| `zhbev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, rwork: float64, info: BlasInt` |
| `zhbevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zhbevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, q: complex128, ldq: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, rwork: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `zhbgst` | `None` | `vect: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: complex128, ldab: BlasInt, bb: complex128, ldbb: BlasInt, x: complex128, ldx: BlasInt, work: complex128, rwork: float64, info: BlasInt` |
| `zhbgv` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: complex128, ldab: BlasInt, bb: complex128, ldbb: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, rwork: float64, info: BlasInt` |
| `zhbgvd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: complex128, ldab: BlasInt, bb: complex128, ldbb: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zhbgvx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ka: BlasInt, kb: BlasInt, ab: complex128, ldab: BlasInt, bb: complex128, ldbb: BlasInt, q: complex128, ldq: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, rwork: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `zhbmv` | `None` | `uplo: uint8, n: BlasInt, k: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt, beta: complex128, y: complex128, incy: BlasInt` |
| `zhbtrd` | `None` | `vect: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, d: float64, e: float64, q: complex128, ldq: BlasInt, work: complex128, info: BlasInt` |
| `zhecon` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, anorm: float64, rcond: float64, work: complex128, info: BlasInt` |
| `zheequb` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, s: float64, scond: float64, amax: float64, work: complex128, info: BlasInt` |
| `zheev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, w: float64, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zheevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, w: float64, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zheevr` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, isuppz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zheevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `zhegs2` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zhegst` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zhegv` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, w: float64, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zhegvd` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, w: float64, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zhegvx` | `None` | `itype: BlasInt, jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `zhemm` | `None` | `side: uint8, uplo: uint8, m: BlasInt, n: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, beta: complex128, c: complex128, ldc: BlasInt` |
| `zhemv` | `None` | `uplo: uint8, n: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt, beta: complex128, y: complex128, incy: BlasInt` |
| `zher` | `None` | `uplo: uint8, n: BlasInt, alpha: float64, x: complex128, incx: BlasInt, a: complex128, lda: BlasInt` |
| `zher2` | `None` | `uplo: uint8, n: BlasInt, alpha: complex128, x: complex128, incx: BlasInt, y: complex128, incy: BlasInt, a: complex128, lda: BlasInt` |
| `zher2k` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, beta: float64, c: complex128, ldc: BlasInt` |
| `zherfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, af: complex128, ldaf: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zherk` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float64, a: complex128, lda: BlasInt, beta: float64, c: complex128, ldc: BlasInt` |
| `zhesv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zhesvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, af: complex128, ldaf: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zheswapr` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, i1: BlasInt, i2: BlasInt` |
| `zhetd2` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, d: float64, e: float64, tau: complex128, info: BlasInt` |
| `zhetf2` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `zhetrd` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, d: float64, e: float64, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zhetrf` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zhetri` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, info: BlasInt` |
| `zhetri2` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zhetri2x` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, nb: BlasInt, info: BlasInt` |
| `zhetrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zhetrs2` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, work: complex128, info: BlasInt` |
| `zhfrk` | `None` | `transr: uint8, uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: float64, a: complex128, lda: BlasInt, beta: float64, c: complex128` |
| `zhgeqz` | `None` | `job: uint8, compq: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex128, ldh: BlasInt, t: complex128, ldt: BlasInt, alpha: complex128, beta: complex128, q: complex128, ldq: BlasInt, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zhpcon` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, ipiv: BlasInt, anorm: float64, rcond: float64, work: complex128, info: BlasInt` |
| `zhpev` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ap: complex128, w: float64, z: complex128, ldz: BlasInt, work: complex128, rwork: float64, info: BlasInt` |
| `zhpevd` | `None` | `jobz: uint8, uplo: uint8, n: BlasInt, ap: complex128, w: float64, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zhpevx` | `None` | `jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ap: complex128, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, rwork: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `zhpgst` | `None` | `itype: BlasInt, uplo: uint8, n: BlasInt, ap: complex128, bp: complex128, info: BlasInt` |
| `zhpgv` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, ap: complex128, bp: complex128, w: float64, z: complex128, ldz: BlasInt, work: complex128, rwork: float64, info: BlasInt` |
| `zhpgvd` | `None` | `itype: BlasInt, jobz: uint8, uplo: uint8, n: BlasInt, ap: complex128, bp: complex128, w: float64, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zhpgvx` | `None` | `itype: BlasInt, jobz: uint8, range: uint8, uplo: uint8, n: BlasInt, ap: complex128, bp: complex128, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, work: complex128, rwork: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `zhpmv` | `None` | `uplo: uint8, n: BlasInt, alpha: complex128, ap: complex128, x: complex128, incx: BlasInt, beta: complex128, y: complex128, incy: BlasInt` |
| `zhpr` | `None` | `uplo: uint8, n: BlasInt, alpha: float64, x: complex128, incx: BlasInt, ap: complex128` |
| `zhpr2` | `None` | `uplo: uint8, n: BlasInt, alpha: complex128, x: complex128, incx: BlasInt, y: complex128, incy: BlasInt, ap: complex128` |
| `zhprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, afp: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zhpsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zhpsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, afp: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zhptrd` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, d: float64, e: float64, tau: complex128, info: BlasInt` |
| `zhptrf` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, ipiv: BlasInt, info: BlasInt` |
| `zhptri` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, ipiv: BlasInt, work: complex128, info: BlasInt` |
| `zhptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zhsein` | `None` | `side: uint8, eigsrc: uint8, initv: uint8, select: bool, n: BlasInt, h: complex128, ldh: BlasInt, w: complex128, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: complex128, rwork: float64, ifaill: BlasInt, ifailr: BlasInt, info: BlasInt` |
| `zhseqr` | `None` | `job: uint8, compz: uint8, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex128, ldh: BlasInt, w: complex128, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zlabrd` | `None` | `m: BlasInt, n: BlasInt, nb: BlasInt, a: complex128, lda: BlasInt, d: float64, e: float64, tauq: complex128, taup: complex128, x: complex128, ldx: BlasInt, y: complex128, ldy: BlasInt` |
| `zlacgv` | `None` | `n: BlasInt, x: complex128, incx: BlasInt` |
| `zlacn2` | `None` | `n: BlasInt, v: complex128, x: complex128, est: float64, kase: BlasInt, isave: BlasInt` |
| `zlacon` | `None` | `n: BlasInt, v: complex128, x: complex128, est: float64, kase: BlasInt` |
| `zlacp2` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, b: complex128, ldb: BlasInt` |
| `zlacpy` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt` |
| `zlacrm` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, b: float64, ldb: BlasInt, c: complex128, ldc: BlasInt, rwork: float64` |
| `zlacrt` | `None` | `n: BlasInt, cx: complex128, incx: BlasInt, cy: complex128, incy: BlasInt, c: complex128, s: complex128` |
| `zladiv` | `np.complex128` | `x: complex128, y: complex128` |
| `zlaed0` | `None` | `qsiz: BlasInt, n: BlasInt, d: float64, e: float64, q: complex128, ldq: BlasInt, qstore: complex128, ldqs: BlasInt, rwork: float64, iwork: BlasInt, info: BlasInt` |
| `zlaed7` | `None` | `n: BlasInt, cutpnt: BlasInt, qsiz: BlasInt, tlvls: BlasInt, curlvl: BlasInt, curpbm: BlasInt, d: float64, q: complex128, ldq: BlasInt, rho: float64, indxq: BlasInt, qstore: float64, qptr: BlasInt, prmptr: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float64, work: complex128, rwork: float64, iwork: BlasInt, info: BlasInt` |
| `zlaed8` | `None` | `k: BlasInt, n: BlasInt, qsiz: BlasInt, q: complex128, ldq: BlasInt, d: float64, rho: float64, cutpnt: BlasInt, z: float64, dlamda: float64, q2: complex128, ldq2: BlasInt, w: float64, indxp: BlasInt, indx: BlasInt, indxq: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, givnum: float64, info: BlasInt` |
| `zlaein` | `None` | `rightv: bool, noinit: bool, n: BlasInt, h: complex128, ldh: BlasInt, w: complex128, v: complex128, b: complex128, ldb: BlasInt, rwork: float64, eps3: float64, smlnum: float64, info: BlasInt` |
| `zlaesy` | `None` | `a: complex128, b: complex128, c: complex128, rt1: complex128, rt2: complex128, evscal: complex128, cs1: complex128, sn1: complex128` |
| `zlaev2` | `None` | `a: complex128, b: complex128, c: complex128, rt1: float64, rt2: float64, cs1: float64, sn1: complex128` |
| `zlag2c` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, sa: complex64, ldsa: BlasInt, info: BlasInt` |
| `zlags2` | `None` | `upper: bool, a1: float64, a2: complex128, a3: float64, b1: float64, b2: complex128, b3: float64, csu: float64, snu: complex128, csv: float64, snv: complex128, csq: float64, snq: complex128` |
| `zlagtm` | `None` | `trans: uint8, n: BlasInt, nrhs: BlasInt, alpha: float64, dl: complex128, d: complex128, du: complex128, x: complex128, ldx: BlasInt, beta: float64, b: complex128, ldb: BlasInt` |
| `zlahef` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, kb: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, w: complex128, ldw: BlasInt, info: BlasInt` |
| `zlahqr` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex128, ldh: BlasInt, w: complex128, iloz: BlasInt, ihiz: BlasInt, z: complex128, ldz: BlasInt, info: BlasInt` |
| `zlahr2` | `None` | `n: BlasInt, k: BlasInt, nb: BlasInt, a: complex128, lda: BlasInt, tau: complex128, t: complex128, ldt: BlasInt, y: complex128, ldy: BlasInt` |
| `zlaic1` | `None` | `job: BlasInt, j: BlasInt, x: complex128, sest: float64, w: complex128, gamma: complex128, sestpr: float64, s: complex128, c: complex128` |
| `zlals0` | `None` | `icompq: BlasInt, nl: BlasInt, nr: BlasInt, sqre: BlasInt, nrhs: BlasInt, b: complex128, ldb: BlasInt, bx: complex128, ldbx: BlasInt, perm: BlasInt, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, givnum: float64, ldgnum: BlasInt, poles: float64, difl: float64, difr: float64, z: float64, k: BlasInt, c: float64, s: float64, rwork: float64, info: BlasInt` |
| `zlalsa` | `None` | `icompq: BlasInt, smlsiz: BlasInt, n: BlasInt, nrhs: BlasInt, b: complex128, ldb: BlasInt, bx: complex128, ldbx: BlasInt, u: float64, ldu: BlasInt, vt: float64, k: BlasInt, difl: float64, difr: float64, z: float64, poles: float64, givptr: BlasInt, givcol: BlasInt, ldgcol: BlasInt, perm: BlasInt, givnum: float64, c: float64, s: float64, rwork: float64, iwork: BlasInt, info: BlasInt` |
| `zlalsd` | `None` | `uplo: uint8, smlsiz: BlasInt, n: BlasInt, nrhs: BlasInt, d: float64, e: float64, b: complex128, ldb: BlasInt, rcond: float64, rank: BlasInt, work: complex128, rwork: float64, iwork: BlasInt, info: BlasInt` |
| `zlangb` | `np.float64` | `norm: uint8, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex128, ldab: BlasInt, work: float64` |
| `zlange` | `np.float64` | `norm: uint8, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, work: float64` |
| `zlangt` | `np.float64` | `norm: uint8, n: BlasInt, dl: complex128, d_: complex128, du: complex128` |
| `zlanhb` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, k: BlasInt, ab: complex128, ldab: BlasInt, work: float64` |
| `zlanhe` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, work: float64` |
| `zlanhf` | `np.float64` | `norm: uint8, transr: uint8, uplo: uint8, n: BlasInt, a: complex128, work: float64` |
| `zlanhp` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, ap: complex128, work: float64` |
| `zlanhs` | `np.float64` | `norm: uint8, n: BlasInt, a: complex128, lda: BlasInt, work: float64` |
| `zlanht` | `np.float64` | `norm: uint8, n: BlasInt, d_: float64, e: complex128` |
| `zlansb` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, k: BlasInt, ab: complex128, ldab: BlasInt, work: float64` |
| `zlansp` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, ap: complex128, work: float64` |
| `zlansy` | `np.float64` | `norm: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, work: float64` |
| `zlantb` | `np.float64` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, k: BlasInt, ab: complex128, ldab: BlasInt, work: float64` |
| `zlantp` | `np.float64` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, ap: complex128, work: float64` |
| `zlantr` | `np.float64` | `norm: uint8, uplo: uint8, diag: uint8, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, work: float64` |
| `zlapll` | `None` | `n: BlasInt, x: complex128, incx: BlasInt, y: complex128, incy: BlasInt, ssmin: float64` |
| `zlapmr` | `None` | `forwrd: bool, m: BlasInt, n: BlasInt, x: complex128, ldx: BlasInt, k: BlasInt` |
| `zlapmt` | `None` | `forwrd: bool, m: BlasInt, n: BlasInt, x: complex128, ldx: BlasInt, k: BlasInt` |
| `zlaqgb` | `None` | `m: BlasInt, n: BlasInt, kl: BlasInt, ku: BlasInt, ab: complex128, ldab: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, equed: uint8` |
| `zlaqge` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, r: float64, c: float64, rowcnd: float64, colcnd: float64, amax: float64, equed: uint8` |
| `zlaqhb` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, s: float64, scond: float64, amax: float64, equed: uint8` |
| `zlaqhe` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, s: float64, scond: float64, amax: float64, equed: uint8` |
| `zlaqhp` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, s: float64, scond: float64, amax: float64, equed: uint8` |
| `zlaqp2` | `None` | `m: BlasInt, n: BlasInt, offset: BlasInt, a: complex128, lda: BlasInt, jpvt: BlasInt, tau: complex128, vn1: float64, vn2: float64, work: complex128` |
| `zlaqps` | `None` | `m: BlasInt, n: BlasInt, offset: BlasInt, nb: BlasInt, kb: BlasInt, a: complex128, lda: BlasInt, jpvt: BlasInt, tau: complex128, vn1: float64, vn2: float64, auxv: complex128, f: complex128, ldf: BlasInt` |
| `zlaqr0` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex128, ldh: BlasInt, w: complex128, iloz: BlasInt, ihiz: BlasInt, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zlaqr1` | `None` | `n: BlasInt, h: complex128, ldh: BlasInt, s1: complex128, s2: complex128, v: complex128` |
| `zlaqr2` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nw: BlasInt, h: complex128, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: complex128, ldz: BlasInt, ns: BlasInt, nd: BlasInt, sh: complex128, v: complex128, ldv: BlasInt, nh: BlasInt, t: complex128, ldt: BlasInt, nv: BlasInt, wv: complex128, ldwv: BlasInt, work: complex128, lwork: BlasInt` |
| `zlaqr3` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nw: BlasInt, h: complex128, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: complex128, ldz: BlasInt, ns: BlasInt, nd: BlasInt, sh: complex128, v: complex128, ldv: BlasInt, nh: BlasInt, t: complex128, ldt: BlasInt, nv: BlasInt, wv: complex128, ldwv: BlasInt, work: complex128, lwork: BlasInt` |
| `zlaqr4` | `None` | `wantt: bool, wantz: bool, n: BlasInt, ilo: BlasInt, ihi: BlasInt, h: complex128, ldh: BlasInt, w: complex128, iloz: BlasInt, ihiz: BlasInt, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zlaqr5` | `None` | `wantt: bool, wantz: bool, kacc22: BlasInt, n: BlasInt, ktop: BlasInt, kbot: BlasInt, nshfts: BlasInt, s: complex128, h: complex128, ldh: BlasInt, iloz: BlasInt, ihiz: BlasInt, z: complex128, ldz: BlasInt, v: complex128, ldv: BlasInt, u: complex128, ldu: BlasInt, nv: BlasInt, wv: complex128, ldwv: BlasInt, nh: BlasInt, wh: complex128, ldwh: BlasInt` |
| `zlaqsb` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, s: float64, scond: float64, amax: float64, equed: uint8` |
| `zlaqsp` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, s: float64, scond: float64, amax: float64, equed: uint8` |
| `zlaqsy` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, s: float64, scond: float64, amax: float64, equed: uint8` |
| `zlar1v` | `None` | `n: BlasInt, b1: BlasInt, bn: BlasInt, lambda_: float64, d: float64, l: float64, ld: float64, lld: float64, pivmin: float64, gaptol: float64, z: complex128, wantnc: bool, negcnt: BlasInt, ztz: float64, mingma: float64, r: BlasInt, isuppz: BlasInt, nrminv: float64, resid: float64, rqcorr: float64, work: float64` |
| `zlar2v` | `None` | `n: BlasInt, x: complex128, y: complex128, z: complex128, incx: BlasInt, c: float64, s: complex128, incc: BlasInt` |
| `zlarcm` | `None` | `m: BlasInt, n: BlasInt, a: float64, lda: BlasInt, b: complex128, ldb: BlasInt, c: complex128, ldc: BlasInt, rwork: float64` |
| `zlarf` | `None` | `side: uint8, m: BlasInt, n: BlasInt, v: complex128, incv: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128` |
| `zlarfb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, v: complex128, ldv: BlasInt, t: complex128, ldt: BlasInt, c: complex128, ldc: BlasInt, work: complex128, ldwork: BlasInt` |
| `zlarfg` | `None` | `n: BlasInt, alpha: complex128, x: complex128, incx: BlasInt, tau: complex128` |
| `zlarfgp` | `None` | `n: BlasInt, alpha: complex128, x: complex128, incx: BlasInt, tau: complex128` |
| `zlarft` | `None` | `direct: uint8, storev: uint8, n: BlasInt, k: BlasInt, v: complex128, ldv: BlasInt, tau: complex128, t: complex128, ldt: BlasInt` |
| `zlarfx` | `None` | `side: uint8, m: BlasInt, n: BlasInt, v: complex128, tau: complex128, c: complex128, ldc: BlasInt, work: complex128` |
| `zlargv` | `None` | `n: BlasInt, x: complex128, incx: BlasInt, y: complex128, incy: BlasInt, c: float64, incc: BlasInt` |
| `zlarnv` | `None` | `idist: BlasInt, iseed: BlasInt, n: BlasInt, x: complex128` |
| `zlarrv` | `None` | `n: BlasInt, vl: float64, vu: float64, d: float64, l: float64, pivmin: float64, isplit: BlasInt, m: BlasInt, dol: BlasInt, dou: BlasInt, minrgp: float64, rtol1: float64, rtol2: float64, w: float64, werr: float64, wgap: float64, iblock: BlasInt, indexw: BlasInt, gers: float64, z: complex128, ldz: BlasInt, isuppz: BlasInt, work: float64, iwork: BlasInt, info: BlasInt` |
| `zlartg` | `None` | `f: complex128, g: complex128, cs: float64, sn: complex128, r: complex128` |
| `zlartv` | `None` | `n: BlasInt, x: complex128, incx: BlasInt, y: complex128, incy: BlasInt, c: float64, s: complex128, incc: BlasInt` |
| `zlarz` | `None` | `side: uint8, m: BlasInt, n: BlasInt, l: BlasInt, v: complex128, incv: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128` |
| `zlarzb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, v: complex128, ldv: BlasInt, t: complex128, ldt: BlasInt, c: complex128, ldc: BlasInt, work: complex128, ldwork: BlasInt` |
| `zlarzt` | `None` | `direct: uint8, storev: uint8, n: BlasInt, k: BlasInt, v: complex128, ldv: BlasInt, tau: complex128, t: complex128, ldt: BlasInt` |
| `zlascl` | `None` | `type_bn: uint8, kl: BlasInt, ku: BlasInt, cfrom: float64, cto: float64, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `zlaset` | `None` | `uplo: uint8, m: BlasInt, n: BlasInt, alpha: complex128, beta: complex128, a: complex128, lda: BlasInt` |
| `zlasr` | `None` | `side: uint8, pivot: uint8, direct: uint8, m: BlasInt, n: BlasInt, c: float64, s: float64, a: complex128, lda: BlasInt` |
| `zlassq` | `None` | `n: BlasInt, x: complex128, incx: BlasInt, scale: float64, sumsq: float64` |
| `zlaswp` | `None` | `n: BlasInt, a: complex128, lda: BlasInt, k1: BlasInt, k2: BlasInt, ipiv: BlasInt, incx: BlasInt` |
| `zlasyf` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, kb: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, w: complex128, ldw: BlasInt, info: BlasInt` |
| `zlat2c` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, sa: complex64, ldsa: BlasInt, info: BlasInt` |
| `zlatbs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, x: complex128, scale: float64, cnorm: float64, info: BlasInt` |
| `zlatdf` | `None` | `ijob: BlasInt, n: BlasInt, z: complex128, ldz: BlasInt, rhs: complex128, rdsum: float64, rdscal: float64, ipiv: BlasInt, jpiv: BlasInt` |
| `zlatps` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, ap: complex128, x: complex128, scale: float64, cnorm: float64, info: BlasInt` |
| `zlatrd` | `None` | `uplo: uint8, n: BlasInt, nb: BlasInt, a: complex128, lda: BlasInt, e: float64, tau: complex128, w: complex128, ldw: BlasInt` |
| `zlatrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, normin: uint8, n: BlasInt, a: complex128, lda: BlasInt, x: complex128, scale: float64, cnorm: float64, info: BlasInt` |
| `zlatrz` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128` |
| `zlauu2` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `zlauum` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `zpbcon` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, anorm: float64, rcond: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zpbequ` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, s: float64, scond: float64, amax: float64, info: BlasInt` |
| `zpbrfs` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, afb: complex128, ldafb: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zpbstf` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, info: BlasInt` |
| `zpbsv` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zpbsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, afb: complex128, ldafb: BlasInt, equed: uint8, s: float64, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zpbtf2` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, info: BlasInt` |
| `zpbtrf` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, info: BlasInt` |
| `zpbtrs` | `None` | `uplo: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zpftrf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: complex128, info: BlasInt` |
| `zpftri` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: complex128, info: BlasInt` |
| `zpftrs` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zpocon` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, anorm: float64, rcond: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zpoequ` | `None` | `n: BlasInt, a: complex128, lda: BlasInt, s: float64, scond: float64, amax: float64, info: BlasInt` |
| `zpoequb` | `None` | `n: BlasInt, a: complex128, lda: BlasInt, s: float64, scond: float64, amax: float64, info: BlasInt` |
| `zporfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, af: complex128, ldaf: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zposv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zposvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, af: complex128, ldaf: BlasInt, equed: uint8, s: float64, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zpotf2` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `zpotrf` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `zpotri` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `zpotrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zppcon` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, anorm: float64, rcond: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zppequ` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, s: float64, scond: float64, amax: float64, info: BlasInt` |
| `zpprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, afp: complex128, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zppsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zppsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, afp: complex128, equed: uint8, s: float64, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zpptrf` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, info: BlasInt` |
| `zpptri` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, info: BlasInt` |
| `zpptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zpstf2` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, piv: BlasInt, rank: BlasInt, tol: float64, work: float64, info: BlasInt` |
| `zpstrf` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, piv: BlasInt, rank: BlasInt, tol: float64, work: float64, info: BlasInt` |
| `zptcon` | `None` | `n: BlasInt, d: float64, e: complex128, anorm: float64, rcond: float64, rwork: float64, info: BlasInt` |
| `zpteqr` | `None` | `compz: uint8, n: BlasInt, d: float64, e: float64, z: complex128, ldz: BlasInt, work: float64, info: BlasInt` |
| `zptrfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, d: float64, e: complex128, df: float64, ef: complex128, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zptsv` | `None` | `n: BlasInt, nrhs: BlasInt, d: float64, e: complex128, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zptsvx` | `None` | `fact: uint8, n: BlasInt, nrhs: BlasInt, d: float64, e: complex128, df: float64, ef: complex128, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zpttrf` | `None` | `n: BlasInt, d: float64, e: complex128, info: BlasInt` |
| `zpttrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, d: float64, e: complex128, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zptts2` | `None` | `iuplo: BlasInt, n: BlasInt, nrhs: BlasInt, d: float64, e: complex128, b: complex128, ldb: BlasInt` |
| `zrot` | `None` | `n: BlasInt, cx: complex128, incx: BlasInt, cy: complex128, incy: BlasInt, c: float64, s: complex128` |
| `zrotg` | `None` | `ca: complex128, cb: complex128, c: float64, s: complex128` |
| `zscal` | `None` | `n: BlasInt, za: complex128, zx: complex128, incx: BlasInt` |
| `zspcon` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, ipiv: BlasInt, anorm: float64, rcond: float64, work: complex128, info: BlasInt` |
| `zspmv` | `None` | `uplo: uint8, n: BlasInt, alpha: complex128, ap: complex128, x: complex128, incx: BlasInt, beta: complex128, y: complex128, incy: BlasInt` |
| `zspr` | `None` | `uplo: uint8, n: BlasInt, alpha: complex128, x: complex128, incx: BlasInt, ap: complex128` |
| `zsprfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, afp: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zspsv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zspsvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, afp: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zsptrf` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, ipiv: BlasInt, info: BlasInt` |
| `zsptri` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, ipiv: BlasInt, work: complex128, info: BlasInt` |
| `zsptrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zstedc` | `None` | `compz: uint8, n: BlasInt, d: float64, e: float64, z: complex128, ldz: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zstegr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float64, e: float64, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, abstol: float64, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, isuppz: BlasInt, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zstein` | `None` | `n: BlasInt, d: float64, e: float64, m: BlasInt, w: float64, iblock: BlasInt, isplit: BlasInt, z: complex128, ldz: BlasInt, work: float64, iwork: BlasInt, ifail: BlasInt, info: BlasInt` |
| `zstemr` | `None` | `jobz: uint8, range: uint8, n: BlasInt, d: float64, e: float64, vl: float64, vu: float64, il: BlasInt, iu: BlasInt, m: BlasInt, w: float64, z: complex128, ldz: BlasInt, nzc: BlasInt, isuppz: BlasInt, tryrac: bool, work: float64, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `zsteqr` | `None` | `compz: uint8, n: BlasInt, d: float64, e: float64, z: complex128, ldz: BlasInt, work: float64, info: BlasInt` |
| `zswap` | `None` | `n: BlasInt, zx: complex128, incx: BlasInt, zy: complex128, incy: BlasInt` |
| `zsycon` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, anorm: float64, rcond: float64, work: complex128, info: BlasInt` |
| `zsyconv` | `None` | `uplo: uint8, way: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, info: BlasInt` |
| `zsyequb` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, s: float64, scond: float64, amax: float64, work: complex128, info: BlasInt` |
| `zsymm` | `None` | `side: uint8, uplo: uint8, m: BlasInt, n: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, beta: complex128, c: complex128, ldc: BlasInt` |
| `zsymv` | `None` | `uplo: uint8, n: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt, beta: complex128, y: complex128, incy: BlasInt` |
| `zsyr` | `None` | `uplo: uint8, n: BlasInt, alpha: complex128, x: complex128, incx: BlasInt, a: complex128, lda: BlasInt` |
| `zsyr2k` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, beta: complex128, c: complex128, ldc: BlasInt` |
| `zsyrfs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, af: complex128, ldaf: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `zsyrk` | `None` | `uplo: uint8, trans: uint8, n: BlasInt, k: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, beta: complex128, c: complex128, ldc: BlasInt` |
| `zsysv` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zsysvx` | `None` | `fact: uint8, uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, af: complex128, ldaf: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, rcond: float64, ferr: float64, berr: float64, work: complex128, lwork: BlasInt, rwork: float64, info: BlasInt` |
| `zsyswapr` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, i1: BlasInt, i2: BlasInt` |
| `zsytf2` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, info: BlasInt` |
| `zsytrf` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zsytri` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, info: BlasInt` |
| `zsytri2` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zsytri2x` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, work: complex128, nb: BlasInt, info: BlasInt` |
| `zsytrs` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `zsytrs2` | `None` | `uplo: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, ipiv: BlasInt, b: complex128, ldb: BlasInt, work: complex128, info: BlasInt` |
| `ztbcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, kd: BlasInt, ab: complex128, ldab: BlasInt, rcond: float64, work: complex128, rwork: float64, info: BlasInt` |
| `ztbmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt` |
| `ztbrfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `ztbsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt` |
| `ztbtrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, kd: BlasInt, nrhs: BlasInt, ab: complex128, ldab: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `ztfsm` | `None` | `transr: uint8, side: uint8, uplo: uint8, trans: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: complex128, a: complex128, b: complex128, ldb: BlasInt` |
| `ztftri` | `None` | `transr: uint8, uplo: uint8, diag: uint8, n: BlasInt, a: complex128, info: BlasInt` |
| `ztfttp` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, arf: complex128, ap: complex128, info: BlasInt` |
| `ztfttr` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, arf: complex128, a: complex128, lda: BlasInt, info: BlasInt` |
| `ztgevc` | `None` | `side: uint8, howmny: uint8, select: bool, n: BlasInt, s: complex128, lds: BlasInt, p: complex128, ldp: BlasInt, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: complex128, rwork: float64, info: BlasInt` |
| `ztgex2` | `None` | `wantq: bool, wantz: bool, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, q: complex128, ldq: BlasInt, z: complex128, ldz: BlasInt, j1: BlasInt, info: BlasInt` |
| `ztgexc` | `None` | `wantq: bool, wantz: bool, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, q: complex128, ldq: BlasInt, z: complex128, ldz: BlasInt, ifst: BlasInt, ilst: BlasInt, info: BlasInt` |
| `ztgsen` | `None` | `ijob: BlasInt, wantq: bool, wantz: bool, select: bool, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, alpha: complex128, beta: complex128, q: complex128, ldq: BlasInt, z: complex128, ldz: BlasInt, m: BlasInt, pl: float64, pr: float64, dif: float64, work: complex128, lwork: BlasInt, iwork: BlasInt, liwork: BlasInt, info: BlasInt` |
| `ztgsja` | `None` | `jobu: uint8, jobv: uint8, jobq: uint8, m: BlasInt, p: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, tola: float64, tolb: float64, alpha: float64, beta: float64, u: complex128, ldu: BlasInt, v: complex128, ldv: BlasInt, q: complex128, ldq: BlasInt, work: complex128, ncycle: BlasInt, info: BlasInt` |
| `ztgsna` | `None` | `job: uint8, howmny: uint8, select: bool, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, s: float64, dif: float64, mm: BlasInt, m: BlasInt, work: complex128, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `ztgsy2` | `None` | `trans: uint8, ijob: BlasInt, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, c: complex128, ldc: BlasInt, d: complex128, ldd: BlasInt, e: complex128, lde: BlasInt, f: complex128, ldf: BlasInt, scale: float64, rdsum: float64, rdscal: float64, info: BlasInt` |
| `ztgsyl` | `None` | `trans: uint8, ijob: BlasInt, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, c: complex128, ldc: BlasInt, d: complex128, ldd: BlasInt, e: complex128, lde: BlasInt, f: complex128, ldf: BlasInt, scale: float64, dif: float64, work: complex128, lwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `ztpcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, ap: complex128, rcond: float64, work: complex128, rwork: float64, info: BlasInt` |
| `ztpmqrt` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, nb: BlasInt, v: complex128, ldv: BlasInt, t: complex128, ldt: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, work: complex128, info: BlasInt` |
| `ztpmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, ap: complex128, x: complex128, incx: BlasInt` |
| `ztpqrt` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, nb: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, t: complex128, ldt: BlasInt, work: complex128, info: BlasInt` |
| `ztpqrt2` | `None` | `m: BlasInt, n: BlasInt, l: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, t: complex128, ldt: BlasInt, info: BlasInt` |
| `ztprfb` | `None` | `side: uint8, trans: uint8, direct: uint8, storev: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, v: complex128, ldv: BlasInt, t: complex128, ldt: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, work: complex128, ldwork: BlasInt` |
| `ztprfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `ztpsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, ap: complex128, x: complex128, incx: BlasInt` |
| `ztptri` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, ap: complex128, info: BlasInt` |
| `ztptrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, ap: complex128, b: complex128, ldb: BlasInt, info: BlasInt` |
| `ztpttf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, ap: complex128, arf: complex128, info: BlasInt` |
| `ztpttr` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, a: complex128, lda: BlasInt, info: BlasInt` |
| `ztrcon` | `None` | `norm: uint8, uplo: uint8, diag: uint8, n: BlasInt, a: complex128, lda: BlasInt, rcond: float64, work: complex128, rwork: float64, info: BlasInt` |
| `ztrevc` | `None` | `side: uint8, howmny: uint8, select: bool, n: BlasInt, t: complex128, ldt: BlasInt, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, mm: BlasInt, m: BlasInt, work: complex128, rwork: float64, info: BlasInt` |
| `ztrexc` | `None` | `compq: uint8, n: BlasInt, t: complex128, ldt: BlasInt, q: complex128, ldq: BlasInt, ifst: BlasInt, ilst: BlasInt, info: BlasInt` |
| `ztrmm` | `None` | `side: uint8, uplo: uint8, transa: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt` |
| `ztrmv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt` |
| `ztrrfs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, x: complex128, ldx: BlasInt, ferr: float64, berr: float64, work: complex128, rwork: float64, info: BlasInt` |
| `ztrsen` | `None` | `job: uint8, compq: uint8, select: bool, n: BlasInt, t: complex128, ldt: BlasInt, q: complex128, ldq: BlasInt, w: complex128, m: BlasInt, s: float64, sep: float64, work: complex128, lwork: BlasInt, info: BlasInt` |
| `ztrsm` | `None` | `side: uint8, uplo: uint8, transa: uint8, diag: uint8, m: BlasInt, n: BlasInt, alpha: complex128, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt` |
| `ztrsna` | `None` | `job: uint8, howmny: uint8, select: bool, n: BlasInt, t: complex128, ldt: BlasInt, vl: complex128, ldvl: BlasInt, vr: complex128, ldvr: BlasInt, s: float64, sep: float64, mm: BlasInt, m: BlasInt, work: complex128, ldwork: BlasInt, rwork: float64, info: BlasInt` |
| `ztrsv` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, a: complex128, lda: BlasInt, x: complex128, incx: BlasInt` |
| `ztrsyl` | `None` | `trana: uint8, tranb: uint8, isgn: BlasInt, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, c: complex128, ldc: BlasInt, scale: float64, info: BlasInt` |
| `ztrti2` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `ztrtri` | `None` | `uplo: uint8, diag: uint8, n: BlasInt, a: complex128, lda: BlasInt, info: BlasInt` |
| `ztrtrs` | `None` | `uplo: uint8, trans: uint8, diag: uint8, n: BlasInt, nrhs: BlasInt, a: complex128, lda: BlasInt, b: complex128, ldb: BlasInt, info: BlasInt` |
| `ztrttf` | `None` | `transr: uint8, uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, arf: complex128, info: BlasInt` |
| `ztrttp` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, ap: complex128, info: BlasInt` |
| `ztzrzf` | `None` | `m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunbdb` | `None` | `trans: uint8, signs: uint8, m: BlasInt, p: BlasInt, q: BlasInt, x11: complex128, ldx11: BlasInt, x12: complex128, ldx12: BlasInt, x21: complex128, ldx21: BlasInt, x22: complex128, ldx22: BlasInt, theta: float64, phi: float64, taup1: complex128, taup2: complex128, tauq1: complex128, tauq2: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zuncsd` | `None` | `jobu1: uint8, jobu2: uint8, jobv1t: uint8, jobv2t: uint8, trans: uint8, signs: uint8, m: BlasInt, p: BlasInt, q: BlasInt, x11: complex128, ldx11: BlasInt, x12: complex128, ldx12: BlasInt, x21: complex128, ldx21: BlasInt, x22: complex128, ldx22: BlasInt, theta: float64, u1: complex128, ldu1: BlasInt, u2: complex128, ldu2: BlasInt, v1t: complex128, ldv1t: BlasInt, v2t: complex128, ldv2t: BlasInt, work: complex128, lwork: BlasInt, rwork: float64, lrwork: BlasInt, iwork: BlasInt, info: BlasInt` |
| `zung2l` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zung2r` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zungbr` | `None` | `vect: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunghr` | `None` | `n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zungl2` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zunglq` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zungql` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zungqr` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zungr2` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, info: BlasInt` |
| `zungrq` | `None` | `m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zungtr` | `None` | `uplo: uint8, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunm2l` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, info: BlasInt` |
| `zunm2r` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, info: BlasInt` |
| `zunmbr` | `None` | `vect: uint8, side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunmhr` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, ilo: BlasInt, ihi: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunml2` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, info: BlasInt` |
| `zunmlq` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunmql` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunmqr` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunmr2` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, info: BlasInt` |
| `zunmr3` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, info: BlasInt` |
| `zunmrq` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunmrz` | `None` | `side: uint8, trans: uint8, m: BlasInt, n: BlasInt, k: BlasInt, l: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zunmtr` | `None` | `side: uint8, uplo: uint8, trans: uint8, m: BlasInt, n: BlasInt, a: complex128, lda: BlasInt, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, lwork: BlasInt, info: BlasInt` |
| `zupgtr` | `None` | `uplo: uint8, n: BlasInt, ap: complex128, tau: complex128, q: complex128, ldq: BlasInt, work: complex128, info: BlasInt` |
| `zupmtr` | `None` | `side: uint8, uplo: uint8, trans: uint8, m: BlasInt, n: BlasInt, ap: complex128, tau: complex128, c: complex128, ldc: BlasInt, work: complex128, info: BlasInt` |