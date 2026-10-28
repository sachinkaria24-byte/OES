"""Layer 8. The residual front: received closures, replayed where possible.

Source: the sibling update received 28 Oct 2026 after the 01:27 UTC Drive
cut. Items whose inputs live in this repository are replayed exactly here.
Items that rest on branch-and-bound certificates or operands not in the
repository are recorded as REPORTED and are not counted as passes.

Replayed:
* band vertex v* = pi(1,1,1,1,0,0,0,0): every root gives cos = +-1, 112 plus
  and 128 minus, so eps(v*) = 256; its W(E8)-orbit has 2160 points in R^8 and
  135 classes modulo the period lattice 2 pi Lambda;
* the local bound S(v* + d) >= -16 + |d|^2 (2 - |d|^2) for |d| <= sqrt 2
  (sampled; the closed form follows from cos expansions at cos = +-1);
* the 224 saddle at pi alpha: the exact Taylor expansion to order four on
  span{E7, alpha}, eps = 224 + 6 rho^2 - 26 z^2 - rho^4/2 + 3 rho^2 z^2 + 5 z^4/6,
  and the quartic on the null cone 6 rho^2 = 26 z^2 equals (40/169) rho^4;
* Agni-Soma: (5I - G)/5 is the cycle projector and fixes the image of W_AS.
"""

from fractions import Fraction

import numpy as np

from sympy import Rational as sp_rational

from . import carrier, gates, native, spacetime
from .record import Report

# Survey of the open collar region (218.9323 < eps < 224, sqrt(313/20) < |k| < 35/8),
# 28 Oct 0741 cut: 8 x 10^6 uniform samples, then SLSQP from the 15 worst points.
# Minimum tangent curvature outside saddle caps of radius d0 (all at eps -> 224).
COLLAR_SURVEY = {0.2: 0.0301, 0.3: 0.0831, 0.5: 0.2250, 0.7: 0.4240, 0.9: 0.6645,
                 1.1: 0.9277}

REPORTED_ITEMS = [
    ("U19.74: sum-of-squares lock r^2 = 9/40 on two copies of a 5-space, and a positive "
     "collar floor up to 224",
     "the U19.74 note is not on Drive (latest court note found: U19.56); the 0741 paper "
     "also records it as not replayed. Numerically consistent with the survey below"),
    ("band [0,256] exact: alcove branch-and-bound, 247,920 pieces, margin > 1e-6",
     "computer-assisted; pieces not in this repository"),
    ("eps > 100 on the alcove outside |k|^2 <= 6 (7,523 pieces)",
     "computer-assisted; removes the single-ball dependency"),
    ("W_n recurrence order is 11: (x+12)^2 divides the leading coefficient",
     "Morse indices 7 and 8 at lambda=-12, corrections -16/3 vs -17/8; "
     "the line 'at least 10, not 11' should be deleted. Layer 14: the operator found has "
     "order 16; its characteristic polynomial has 11 roots in the band [-16, 240], "
     "(z+12)^2 among them, and 5 outside"),
    ("155 vs 4805 is a label error: 155 = det T = 5*31 (6x6 adapter); "
     "4805 = 5*31^2 is the 4th cofactor of T T^T",
     "T operand (eq. 27) is garbled in the PDF text; not rebuilt here"),
    ("rotor hex6: m1 = 242 >= 241.36, Hankel determinants positive",
     "operand not in this repository"),
    ("collar to 224: alcove reduction; min curvature positive up to 223.999 "
     "(0.065 at 223.25, 0.014 at 223.999)",
     "numerical; certified bound away from the saddle still OPEN"),
    ("convexity levels 223.25 < 223.5 < 223.53 < 223.58 are successive lower "
     "bounds, not rival theorems",
     "standing value: the largest replayed one"),
]

STILL_OPEN = [
    "certified collar 218.9323 < eps < 224: needs an analytic saddle cap of radius ~1 "
    "(margin 15/16 d^2) and a non-grid bound outside it",
    "scalar W_n recurrence over Q: layer 14 forms it mod four primes (order 16, degree 58, "
    "characteristic roots exact); rational coefficients and a proof for all n open",
    "2740-dim five-port, -8/9 moment, Jordan drops, return-corner ranks (no operands)",
    "wave decay 1/4 vs 1/6, Schrodinger prefactor 204 vs 206 (no derivations)",
]

V_STAR = np.array([2, 2, 2, 2, 0, 0, 0, 0])  # doubled coordinates of v*/pi


def band_vertex_split():
    R = spacetime.e8_roots()
    ph = (R @ V_STAR) // 4          # alpha . v* / pi, an integer
    plus = int((ph % 2 == 0).sum())
    return plus, len(R) - plus


def band_orbit():
    """W(E8)-orbit of v* in R^8 and its classes modulo 2 pi Lambda."""
    R = spacetime.e8_roots()
    seen = {tuple(V_STAR)}
    front = [V_STAR]
    while front:
        new = []
        for x in front:
            for a in R[:120]:
                y = x - ((x @ a) // 4) * a
                t = tuple(y)
                if t not in seen:
                    seen.add(t)
                    new.append(y)
        front = new
    O = np.array(sorted(seen))
    # x ~ y iff (x - y)/4 lies in Lambda (physical coordinates)
    def in_lattice(d):
        if np.any(d % 2):
            return False
        w = d // 2                  # doubled coords of (x-y)/4
        return (np.all(w % 2 == 0) or np.all(w % 2 != 0)) and w.sum() % 4 == 0
    reps = []
    for x in O:
        if not any(in_lattice(x - r) for r in reps):
            reps.append(x)
    return len(O), len(reps)


def local_bound_slack(samples=100000, seed=0):
    R = spacetime.e8_roots() / 2.0
    k = np.pi * V_STAR / 2.0
    rng = np.random.default_rng(seed)
    worst = np.inf
    for _ in range(samples // 2000):
        d = rng.standard_normal((2000, 8))
        d *= rng.random((2000, 1)) * 2 ** 0.5 / np.linalg.norm(d, axis=1, keepdims=True)
        S = np.cos((k + d) @ R.T).sum(1)
        n2 = (d ** 2).sum(1)
        worst = min(worst, float((S + 16 - n2 * (2 - n2)).min()))
    return worst


def saddle_expansion():
    """Exact order-4 Taylor coefficients of eps at pi*alpha on span{u, alpha}.

    alpha = e1 + e2, u = (e3 - e4)/sqrt2 (an E7 direction), z along alpha/sqrt2.
    Coefficients are returned as Fractions keyed by (power of rho, power of z).
    """
    R = spacetime.e8_roots()        # doubled
    a = np.array([2, 2, 0, 0, 0, 0, 0, 0])
    r = np.array([0, 0, 2, -2, 0, 0, 0, 0])
    coef = {}
    for b in R:
        ph = (b @ a) // 4           # b . alpha
        sgn = 1 if ph % 2 == 0 else -1
        # b.u = (b.r)/(4 sqrt2) ; b.(alpha/sqrt2) = (b.a)/(4 sqrt2): write both as p/sqrt2
        p, q = Fraction(int(b @ r), 4), Fraction(int(b @ a), 4)
        # cos(pi ph + t) = sgn (1 - t^2/2 + t^4/24), t = (p rho + q z)/sqrt2
        for (i, j), c in {(2, 0): p * p, (1, 1): 2 * p * q, (0, 2): q * q}.items():
            coef[(i, j)] = coef.get((i, j), 0) + sgn * c / 4      # -(-t^2/2), /2 from sqrt2^2
        for i in range(5):
            from math import comb
            c = comb(4, i) * p ** i * q ** (4 - i)
            coef[(i, 4 - i)] = coef.get((i, 4 - i), 0) - sgn * c / 96   # -(t^4/24), /4
        coef[(0, 0)] = coef.get((0, 0), 0) - sgn
    coef[(0, 0)] += 240
    return {k: v for k, v in coef.items() if v != 0}


def saddle_law():
    """Tangent curvature of the 224 level at distance d from pi*alpha.

    Uses the exact order-4 expansion (isotropic in E7 to that order) in the
    (rho, z) plane and returns the leading coefficient of the series in d.
    """
    import sympy as sp
    r, z, d, t1 = sp.symbols("rho z d theta1", real=True)
    f = 6 * r ** 2 - 26 * z ** 2 - r ** 4 / 2 + 3 * r ** 2 * z ** 2 + sp.Rational(5, 6) * z ** 4
    th = sp.atan2(sp.sqrt(sp.Rational(3, 16)), sp.sqrt(sp.Rational(13, 16))) + t1 * d ** 2
    P = {r: d * sp.cos(th), z: d * sp.sin(th)}
    lev = sp.series(f.subs(P), d, 0, 6).removeO()
    t1v = sp.solve(sp.expand(lev / d ** 4).subs(d, 0), t1)[0]
    fr, fz = sp.diff(f, r), sp.diff(f, z)
    H = sp.Matrix([[sp.diff(f, r, 2), sp.diff(f, r, z)], [sp.diff(f, r, z), sp.diff(f, z, 2)]])
    tv = sp.Matrix([-fz, fr])
    kap = (tv.T * H * tv)[0] / (tv.T * tv)[0]
    ser = sp.series(sp.simplify(kap.subs(P).subs(t1, t1v)), d, 0, 4).removeO()
    return sp.nsimplify(sp.expand(ser).coeff(d, 2)), sp.expand(ser).coeff(d, 0)


def tangent_curvature(k):
    R = spacetime.e8_roots() / 2.0
    ph = R @ k
    c, s = np.cos(ph), np.sin(ph)
    g = R.T @ s
    H = (R.T * c) @ R
    n = g / np.linalg.norm(g)
    P = np.eye(8) - np.outer(n, n)
    return np.linalg.eigvalsh(P @ H @ P + 1e3 * np.outer(n, n))[0]


def saddle_law_numeric(d, ndir=60, seed=0):
    """min tangent curvature on the 224 level at distance d, over E7 directions."""
    from scipy.optimize import brentq
    R = spacetime.e8_roots() / 2.0
    a = np.array([1, 1, 0, 0, 0, 0, 0, 0.0])
    ah = a / np.sqrt(2)
    rng = np.random.default_rng(seed)
    best = np.inf
    for _ in range(ndir):
        w = rng.standard_normal(8)
        w -= (w @ ah) * ah
        w /= np.linalg.norm(w)
        th0 = np.arctan2(np.sqrt(3 / 16), np.sqrt(13 / 16))
        f = lambda th: 240 - np.cos(R @ (np.pi * a + d * (np.cos(th) * w + np.sin(th) * ah))).sum() - 224
        th = brentq(f, th0 - 0.3, th0 + 0.3)
        best = min(best, tangent_curvature(np.pi * a + d * (np.cos(th) * w + np.sin(th) * ah)))
    return best


def coil():
    from math import gcd
    N, pada, yuga = 4320, 40, 1728
    order = lambda s: N // gcd(s, N)
    joint = N // gcd(gcd(pada, yuga), N)
    A = {(pada * i) % N for i in range(order(pada))}
    B = {(yuga * i) % N for i in range(order(yuga))}
    fib, k = (0, 1), 0
    while True:
        fib, k = (fib[1], (fib[0] + fib[1]) % 5), k + 1
        if fib == (0, 1):
            break
    return order(pada), order(yuga), joint, N // joint, A & B, k


def run():
    rep = Report("8-frontier")
    T = gates.THEOREM
    plus, minus = band_vertex_split()
    rep.add("band vertex v*: cos = +1 on 112 roots, -1 on 128; eps(v*) = 256", T,
            (plus, minus) == (112, 128), [plus, minus])
    n, cls = band_orbit()
    rep.add("W(E8)-orbit of v*: 2160 points in R^8, 135 classes mod 2 pi Lambda", T,
            (n, cls) == (2160, 135), [n, cls])
    slack = local_bound_slack()
    rep.add("S(v*+d) >= -16 + |d|^2 (2-|d|^2) for |d| <= sqrt2 (sampled)",
            gates.ARITHMETIC, slack > -1e-12, slack)
    c = saddle_expansion()
    target = {(0, 0): 224, (2, 0): 6, (0, 2): -26, (4, 0): Fraction(-1, 2),
              (2, 2): 3, (0, 4): Fraction(5, 6)}
    rep.add("224 saddle: eps = 224 + 6rho^2 - 26z^2 - rho^4/2 + 3rho^2z^2 + 5z^4/6", T,
            c == target, {str(k): str(v) for k, v in c.items()})
    cone = (target[(4, 0)] + target[(2, 2)] * Fraction(3, 13)
            + target[(0, 4)] * Fraction(9, 169))
    rep.add("quartic on the cone 6rho^2 = 26z^2 is (40/169) rho^4 > 0", T,
            cone == Fraction(40, 169), str(cone))
    Bs = np.array(carrier.signed_incidence(), float)
    P = (5 * np.eye(10) - Bs.T @ Bs) / 5
    img = native.l6_basis() @ native.commutator_map()[0]
    rep.add("Agni-Soma: (5I-G)/5 is the cycle projector and fixes W_AS (not rivals)", T,
            np.allclose(P @ P, P) and np.allclose(P @ img, img))
    c2, c0 = saddle_law()
    rep.add("224 level near the saddle: tangent curvature = (15/16) d^2 + O(d^4)", T,
            c2 == sp_rational(15, 16) and c0 == 0, str(c2),
            note="exact from the order-4 expansion; the margin vanishes quadratically "
                 "at the saddle, so no box grid can reach it")
    num = {d: saddle_law_numeric(d) / d ** 2 for d in (0.1, 0.3)}
    rep.add("numerical replay of the saddle law on the true symbol (ratio -> 15/16)",
            gates.ARITHMETIC, all(abs(v - 15 / 16) < 0.02 for v in num.values()), num)
    rep.add("collar survey: min tangent curvature outside caps of radius d0 is positive, "
            "about 0.8-0.93 d0^2", gates.ARITHMETIC,
            all(v > 0 for v in COLLAR_SURVEY.values()), COLLAR_SURVEY,
            note="8e6 samples + constrained optimisation; evidence, not a certificate")
    need = {d0: (lam / 85.0) for d0, lam in COLLAR_SURVEY.items()}
    rep.add("first-order box certificate outside a radius-1 cap needs box radius < 0.01: "
            "> 1e13 boxes in one Weyl chamber", gates.OBSTRUCTION, need[1.1] < 0.012,
            {str(k): v for k, v in need.items()},
            note="chamber shell volume ~4e-4; so the collar needs an analytic cap of "
                 "radius ~1 plus a non-grid argument")
    po, yo, jo, idx, meet, pis = coil()
    rep.add("coil: in Z/4320 pada step 40 (order 108) and yuga step 1728 (order 5) "
            "generate order 540, index 8, meeting only at 0; Pisano(5) = 20 | 540", T,
            (po, yo, jo, idx, meet, pis) == (108, 5, 540, 8, {0}, 20) and 540 % 20 == 0,
            [po, yo, jo, idx, sorted(meet), pis])
    for name, note in REPORTED_ITEMS:
        rep.add(name, gates.REPORTED, True, note=note)
    for name in STILL_OPEN:
        rep.add(name, gates.UNFORMED, True, note="open")
    return rep
