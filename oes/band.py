"""The band edge: sup eps = 256 on E8, with a proof.

The bath's band is eps(k) = 240 - Lambda(k), Lambda(k) = sum over the 240 roots of cos(r.k). Layer 8 records the
canon's alcove branch and bound (247,920 pieces) for sup eps = 256, and layer 22 notes that nothing here proves it.
This module proves it: Lambda >= -16 everywhere, i.e. the adjoint character of E8 is at least -8 = -rank.

1. D8 + spinors (exact, by Fourier coefficients). With c_i = cos k_i, C_i = cos(k_i/2), S_i = sin(k_i/2),

       Lambda = 4 e2(c) + 128 (prod C + prod S),

   since 4 e2(c) expands to one exponential per root +-e_i +- e_j, and 128 (prod C + prod S) to
   (1/2) sum_s (1 + prod sign s) e^(i s.k) over s in (+-1/2)^8, one exponential per root with an even number of minus
   signs.

2. Worst signs. |prod C| = prod sqrt((1 + c_i)/2) and |prod S| = prod sqrt((1 - c_i)/2), so with x = c,

       Lambda + 16 >= 8 phi(x),   phi = 2 + e2(x)/2 - prod sqrt(1 + x_i) - prod sqrt(1 - x_i),   x in [-1, 1]^8.

3. Three values. phi attains its minimum on the cube. At a minimizer each coordinate in (-1, 1) satisfies
   2 (1 - t^2) d phi/d x_i = (S - t)(1 - t^2) - P+ (1 - t) + P- (1 + t) = 0, one monic cubic for all of them
   (S = sum x, P+- the two products); a coordinate at +1 forces P- = 0 and leaves a quadratic, one at -1 forces P+ = 0,
   and both leave t = S. So a minimizer takes at most three values, and lies in one of the partitions
   (6,1,1), (5,2,1), (4,3,1), (4,2,2), (3,3,2) of the eight coordinates, with values cos 2a, cos 2b, cos 2g for
   (a, b, g) in [0, pi/2]^3. There sqrt(1 + cos 2a) = sqrt2 cos a, and

       phi_n = 2 + e2/2 - 16 prod cos^n_j - 16 prod sin^n_j,

   a trigonometric polynomial.

4. Certificate. Each phi_n >= 0 on [0, pi/2]^3 by branch and bound with outward-rounded interval arithmetic
   (natural and mean-value enclosures, vectorized), except inside small boxes around its zeros. Around each zero the
   interval Hessian is positive definite (Gershgorin, mpmath intervals), and phi_n and its gradient vanish exactly at
   the zero (sympy), so phi_n >= 0 there by convexity, with the zero its only minimizer.

So Lambda >= -16, with equality exactly where x is 0, +-(1, ..., 1) or has four entries +1 and four -1 (and the spinor
products take the worst signs): the 135 classes of the band-edge orbit of layer 8. Hence sup eps = 256, and
spec Delta = [0, 256].
"""

import functools
import itertools

import numpy as np
import sympy as sp
from mpmath import iv

from . import glue

PARTITIONS = [(6, 1, 1), (5, 2, 1), (4, 3, 1), (4, 2, 2), (3, 3, 2)]
TRIG = 4.5e-16                      # bound on the libm error of cos and sin on [0, pi]
INF = np.inf
TOP = np.nextafter(np.pi / 2, INF)  # the float above pi/2, so [0, TOP] covers [0, pi/2]


# ------------------------------------------------------------------ interval arithmetic, rounded outward

def _dn(x):
    return np.nextafter(x, -INF)


def _up(x):
    return np.nextafter(x, INF)


class Iv:
    """Arrays of intervals [lo, hi]; every +, -, * is rounded outward by one ulp."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=float)
        self.hi = self.lo if hi is None else np.asarray(hi, dtype=float)

    def __add__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(_dn(self.lo + o.lo), _up(self.hi + o.hi))

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        return Iv(_dn(self.lo - o.hi), _up(self.hi - o.lo))

    def __rsub__(self, o):
        return Iv(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, Iv) else Iv(o)
        p = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return Iv(_dn(np.minimum.reduce(p)), _up(np.maximum.reduce(p)))

    __rmul__ = __mul__

    def pow(self, n):
        """[lo, hi] with lo >= 0, to the power n."""
        assert np.all(self.lo >= 0)
        lo, hi = np.ones_like(self.lo), np.ones_like(self.hi)
        for _ in range(n):
            lo, hi = _dn(lo * self.lo), _up(hi * self.hi)
        return Iv(np.maximum(lo, 0.0), hi)

    def sq(self):
        a, b = self.lo * self.lo, self.hi * self.hi
        lo = np.where((self.lo <= 0) & (self.hi >= 0), 0.0, _dn(np.minimum(a, b)))
        return Iv(lo, _up(np.maximum(a, b)))


def _cos(lo, hi):
    """cos on [lo, hi] inside [0, pi] (up to an ulp past pi): decreasing."""
    return Iv(np.maximum(np.cos(hi) - TRIG, -1.0), np.minimum(np.cos(lo) + TRIG, 1.0))


def _cos_base(lo, hi):
    """cos a on [lo, hi] for the true domain a in [0, pi/2], where it is nonnegative."""
    return Iv(np.maximum(np.cos(hi) - TRIG, 0.0), np.minimum(np.cos(lo) + TRIG, 1.0))


def _sin(lo, hi):
    """sin on [lo, hi] inside [0, TOP]: nonnegative and at least sin lo."""
    return Iv(np.maximum(np.sin(lo) - TRIG, 0.0), np.minimum(np.sin(hi) + TRIG, 1.0))


def _sin2(lo, hi):
    """sin 2a for a in [lo, hi] inside [0, TOP]: it rises to 1 at pi/4 and falls back."""
    a, b = np.sin(2 * lo), np.sin(2 * hi)
    top = np.where((lo <= np.pi / 4) & (hi >= np.pi / 4), 1.0, np.maximum(a, b) + TRIG)
    return Iv(np.minimum(a, b) - TRIG, np.minimum(top, 1.0))


def _phi(n, L, U):
    """Natural interval extension of phi_n on the boxes [L, U] (arrays of shape (m, 3))."""
    c = [_cos_base(L[:, j], U[:, j]) for j in range(3)]
    s = [_sin(L[:, j], U[:, j]) for j in range(3)]
    X = [_cos(2 * L[:, j], 2 * U[:, j]) for j in range(3)]
    e2 = Iv(np.zeros(len(L)))
    for j in range(3):
        if n[j] > 1:
            e2 = e2 + (n[j] * (n[j] - 1) // 2) * X[j].sq()
        for k in range(j + 1, 3):
            e2 = e2 + (n[j] * n[k]) * (X[j] * X[k])
    pp = 16 * (c[0].pow(n[0]) * c[1].pow(n[1]) * c[2].pow(n[2]))
    pm = 16 * (s[0].pow(n[0]) * s[1].pow(n[1]) * s[2].pow(n[2]))
    return 2 + 0.5 * e2 - pp - pm


def _grad(n, L, U):
    """Interval enclosures of d phi_n / d a_j on the boxes."""
    c = [_cos_base(L[:, j], U[:, j]) for j in range(3)]
    s = [_sin(L[:, j], U[:, j]) for j in range(3)]
    X = [_cos(2 * L[:, j], 2 * U[:, j]) for j in range(3)]
    S = n[0] * X[0] + n[1] * X[1] + n[2] * X[2]
    out = []
    for j in range(3):
        k, m = [i for i in range(3) if i != j]
        e2part = (-n[j]) * ((S - X[j]) * _sin2(L[:, j], U[:, j]))
        plus = (16 * n[j]) * (c[j].pow(n[j] - 1) * s[j] * c[k].pow(n[k]) * c[m].pow(n[m]))
        minus = (16 * n[j]) * (s[j].pow(n[j] - 1) * c[j] * s[k].pow(n[k]) * s[m].pow(n[m]))
        out.append(e2part + plus - minus)
    return out


def lower_bound(n, L, U):
    """A rigorous lower bound of phi_n on each box: the better of the natural and the mean-value enclosures."""
    natural = _phi(n, L, U).lo
    M = (L + U) / 2
    centred = _phi(n, M, M)
    for j, g in enumerate(_grad(n, L, U)):
        centred = centred + g * Iv(_dn(L[:, j] - M[:, j]), _up(U[:, j] - M[:, j]))
    return np.maximum(natural, centred.lo)


# ------------------------------------------------------------------ the exact side: phi_n, its zeros, its Hessian

A, B, G = sp.symbols("a b g", real=True)


def phi_n(n):
    X = [sp.cos(2 * v) for v in (A, B, G)]
    S = sum(k * x for k, x in zip(n, X))
    Q = sum(k * x ** 2 for k, x in zip(n, X))
    return 2 + (S ** 2 - Q) / 4 - 16 * sp.cos(A) ** n[0] * sp.cos(B) ** n[1] * sp.cos(G) ** n[2] \
        - 16 * sp.sin(A) ** n[0] * sp.sin(B) ** n[1] * sp.sin(G) ** n[2]


def zeros(n):
    """Where phi_n vanishes: the centre (x = 0), the two corners (x = +-1), and four against four where the partition
    allows it."""
    q = sp.pi / 2
    out = [(sp.pi / 4,) * 3, (sp.Integer(0),) * 3, (q,) * 3]
    for side in itertools.product((0, 1), repeat=3):
        if sum(k for k, t in zip(n, side) if t == 0) == 4:
            out.append(tuple(sp.Integer(0) if t == 0 else q for t in side))
    return out


def _iv_fn(expr):
    return sp.lambdify((A, B, G), expr, modules=[{"cos": iv.cos, "sin": iv.sin, "mpf": iv.mpf, "pi": iv.pi}, "mpmath"])


def _hessian_pd(hess, box):
    """Gershgorin on the mpmath interval Hessian over the box: each diagonal entry beats its off-diagonal row."""
    X = [iv.mpf([lo, hi]) for lo, hi in box]
    H = [[h(*X) for h in row] for row in hess]
    return all(H[i][i].a > sum(max(abs(H[i][j].a), abs(H[i][j].b)) for j in range(3) if j != i) for i in range(3))


def convexity_boxes(n, r0=0.2):
    """For each zero: phi_n and its gradient vanish there exactly, and the largest box of half-width r0 / 2^m around it
    on which the interval Hessian is positive definite."""
    f = phi_n(n)
    v = (A, B, G)
    hess = [[_iv_fn(sp.diff(f, x, y)) for y in v] for x in v]
    out = []
    for z in zeros(n):
        sub = dict(zip(v, z))
        exact = sp.simplify(f.subs(sub)) == 0 and all(sp.simplify(sp.diff(f, x).subs(sub)) == 0 for x in v)
        zf = np.array([float(t) for t in z])
        r = r0
        while not _hessian_pd(hess, [(x - r, x + r) for x in zf]):
            r /= 2
            if r < 1e-4:
                return None
        out.append((exact, zf - r, zf + r))
    return out


def certify(n, max_levels=80):
    """Branch and bound over [0, pi/2]^3 outside the convexity boxes; returns (boxes examined, levels, convexity boxes)
    or None if a box cannot be certified within max_levels halvings."""
    boxes = convexity_boxes(n)
    if boxes is None or not all(ok for ok, _, _ in boxes):
        return None
    L, U = np.zeros((1, 3)), np.full((1, 3), TOP)
    examined, level = 0, 0
    while len(L):
        level += 1
        if level > max_levels:
            return None
        inside = np.zeros(len(L), dtype=bool)
        for _, lo, hi in boxes:
            inside |= np.all((L >= lo) & (U <= hi), axis=1)
        L, U = L[~inside], U[~inside]
        if not len(L):
            break
        examined += len(L)
        keep = lower_bound(n, L, U) <= 0
        L, U = L[keep], U[keep]
        idx = np.arange(len(L))
        k = np.argmax(U - L, axis=1)
        mid = (L[idx, k] + U[idx, k]) / 2
        L1, U1, L2, U2 = L.copy(), U.copy(), L.copy(), U.copy()
        U1[idx, k] = mid
        L2[idx, k] = mid
        L, U = np.vstack([L1, L2]), np.vstack([U1, U2])
    return examined, level, boxes


# ------------------------------------------------------------------ the checks

def lam(k):
    """Lambda(k) = sum over the roots of cos(r.k)."""
    return float(np.cos(glue.roots() @ np.asarray(k, dtype=float)).sum())


def edge_classes():
    """The points k = (pi/2) m, m in Z^8, with Lambda(k) = -16, counted modulo the period lattice 2 pi E8.

    For a root r, r.k = (pi/4)(2r.m), so Lambda = a + b sqrt2/2 with integer a, b read off 2r.m mod 8. Every class of
    Z^8 / 4E8 appears twice among the classes of Z^8 / 4D8, which {0,..,3}^8 and its shift by 4e_1 represent."""
    R2 = np.rint(2 * glue.roots()).astype(np.int64)
    base = np.array(list(itertools.product(range(4), repeat=8)), dtype=np.int64)
    count = 0
    for shift in (0, 4):
        M = base.copy()
        M[:, 0] += shift
        for start in range(0, len(M), 8192):
            j = (M[start:start + 8192] @ R2.T) % 8
            a = (j == 0).sum(1) - (j == 4).sum(1)
            b = ((j == 1) | (j == 7)).sum(1) - ((j == 3) | (j == 5)).sum(1)
            count += int(((a == -16) & (b == 0)).sum())
    return count // 2


@functools.lru_cache(maxsize=None)
def _certificates():
    return {n: certify(n) for n in PARTITIONS}


def edge():
    """sup eps = 256: the proof in four steps, and the edge's 135 classes."""
    R = glue.roots()
    R2 = {tuple(np.rint(2 * r).astype(int)) for r in R}
    d8 = {tuple(2 * s * np.eye(8, dtype=int)[i] + 2 * t * np.eye(8, dtype=int)[j])
          for i, j in itertools.combinations(range(8), 2) for s in (1, -1) for t in (1, -1)}
    spin = {s for s in itertools.product((1, -1), repeat=8) if np.prod(s) == 1}
    x = sp.symbols("x0:8")
    e2 = sum(x[i] * x[j] for i, j in itertools.combinations(range(8), 2))
    Pp = sp.prod([sp.sqrt(1 + v) for v in x])
    Pm = sp.prod([sp.sqrt(1 - v) for v in x])
    phi = 2 + e2 / 2 - Pp - Pm
    tt, SS, PP, PM = sp.symbols("t S P_plus P_minus")
    cubic = (SS - tt) * (1 - tt ** 2) - PP * (1 - tt) + PM * (1 + tt)
    lhs = 2 * (1 - x[0] ** 2) * sp.diff(phi, x[0])
    rhs = cubic.subs({tt: x[0], SS: sum(x), PP: Pp, PM: Pm})
    certs = _certificates()
    v_star = np.pi * np.array([1, 1, 1, 1, 0, 0, 0, 0])
    return {
        "the 240 roots are the 112 D8 roots +-e_i +- e_j and the 128 half-vectors (+-1/2)^8 with an even number of minus "
        "signs, so by Fourier coefficients Lambda = 4 e2(cos k) + 128 (prod cos(k_i/2) + prod sin(k_i/2)); at worst "
        "spinor signs Lambda + 16 >= 8 phi(cos k), phi = 2 + e2/2 - prod sqrt(1 + x_i) - prod sqrt(1 - x_i)":
            R2 == d8 | spin and len(R2) == 240 and abs(lam(2 * np.pi * np.eye(8)[0]) + 16) < 1e-12,
        "at a minimizer of phi each free coordinate t solves one monic cubic, 2(1 - t^2) d phi/d x_i = "
        "(S - t)(1 - t^2) - P+ (1 - t) + P- (1 + t): at most three values, so the five partitions (6,1,1), (5,2,1), "
        "(4,3,1), (4,2,2), (3,3,2) with values cos 2a, cos 2b, cos 2g carry every minimizer":
            sp.simplify(lhs - rhs) == 0 and sp.Poly(cubic, tt).LC() == 1,
        "each phi_n >= 0 on [0, pi/2]^3: interval branch and bound (outward rounding) outside boxes around its zeros, "
        "where phi_n and its gradient vanish exactly and the interval Hessian is positive definite":
            all(c is not None for c in certs.values()),
        "so Lambda >= -16 and sup eps = 256, attained exactly on the 135 classes of the band-edge orbit of layer 8 "
        "(x = 0, x = +-(1, ..., 1) or four entries +1 and four -1)": edge_classes() == 135
            and abs(lam(v_star) + 16) < 1e-12,
    }


def certificate_sizes():
    """Boxes examined, levels and convexity half-widths for each partition."""
    return {n: (c[0], c[1], [round(float(hi[0] - lo[0]) / 2, 4) for _, lo, hi in c[2]])
            for n, c in _certificates().items() if c is not None}
