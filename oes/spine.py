"""Layer 19. The integrated spine, rebuilt: the 4320-circle, the E8 Coxeter clock,
and the tick as two carriers.

Source: the sibling's integrated build of 28 Oct 2026 in the Drive folder
"One Machine 20261028" (INTEGRATED_20261028.md, one-machine-20261028-integrated.pdf,
oes-integrated-20261028.zip) and the notes behind it (ALL_4320, SIDEREAL_DOTS,
SEGMENT_NAMES, YUGA_LATTICE, DOTS_LATTICE, ALL_DOTS, PREMA_SALINA). Its spine:

    The Coxeter number 30 cuts 4320 into 144. Six of those steps make 864.
    Five of those close the circle. ... Every one of the 4320 elements sits in
    the tower 36 x 12 x 2 x 5 = 4320. ... The path stops where 7 does not divide
    4320, the pada step 40 is not in the order-10 subgroup, the Krishna lift is
    not a sum of 4 and 5, Prema's stage index 13 is not her width 2.

In the sibling model these are integer comparisons (the Krishna stop is
`4 + 5 !== 4`), and its paper says "No stored map sends a yuga tick to a lattice
vector or a Morse point." Here:

(a) One lemma. Z/4320 has exactly one subgroup <d> for each divisor d, of order
    4320/d; <a> lies in <b> iff gcd(b,4320) | gcd(a,4320); meets are lcms and
    joins are gcds. Every circle statement of the integrated build is checked by
    this rule. Six are corrected, for example the note that calls the order-36
    meet of the pada and the cycle "the atlas" (the atlas <36> has order 120).
(b) The spine refined. The Coxeter subgroup <144> (order 30) lies between the
    order-10 subgroup and the atlas, so the tower is 36 x 4 x 3 x 2 x 5. There
    are 504 maximal chains of subgroups, and 6 of them contain the whole spine.
    The pada lies on no chain with the tick, and pada + tick is the coil <8>.
(c) The Coxeter clock. c = s1 ... s8 in W(E8) has order 30, c^15 = -I and
    characteristic polynomial Phi_30. Its exponents are the units mod 30, so 7
    is one of them. It permutes the 240 roots in 8 orbits of 30, so it commutes
    with the bath. Sending the step 144 to c (a selection, one of 8) makes the
    first three stages of the spine act on the bath.
(d) Fixed momenta. c^k fixes |det(c^k - I)| Bloch momenta: 25 for the tick,
    81 for the sun, 256 for the half-turn 2160, and only the origin for the
    other 26 non-identity elements. A fixed momentum of an element without
    eigenvalue 1 is a critical point of the band, so these are Morse points:
    the tick fixes 24 points of A4+A4, the sun 80 of E6+A2, the half-turn all
    120 of E7+A1 and all 135 of D8.
(e) Two carriers. A conjugate c' of c has c'^6 = r r' exactly, where r is the
    K5 vertex rotation on the carrier's A4 (layer 11) and r' a Coxeter element
    of the twin A4'. The tick turns two carriers. The sun turns four triangles
    (A2^4, index 9) and the half-turn flips eight edges (A1^8, index 16).
(f) Where 7 enters. The normalizer of <c'> has order 240, and every unit mod 30
    is realized. No element of order 24 commutes with c'. The day clock d
    (order 24, characteristic polynomial Phi_24) agrees with the Coxeter clock on
    the circle's common subgroup <720> (d^4 = c'^5) and turns it by the exponent
    7: d c' d^-1 = c'^7. The circle's atlas 36 = 180 - 144 becomes d c'^-1,
    of order 24, not 120.
(g) What can act on the bath. A cyclic subgroup of the circle acts faithfully on
    the bath lattice exactly when its order is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12,
    15, 18, 20, 24 or 30. The maximal ones are the Coxeter subgroup (30), the day
    (24), <216> (20) and <240> (18). The moon, nakshatra, pada and atlas
    subgroups cannot act, and the spine stops acting at the atlas.

No term is added to the action: the Coxeter clock is a symmetry of the bath
operator already in the model.
"""

import itertools
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial, gcd, lcm

import numpy as np
import sympy as sp

from . import gates, glue, handover
from .record import Report

N = 4320
X = sp.symbols("x")
UNITS30 = [m for m in range(30) if gcd(m, 30) == 1]


# --------------------------------------------------------------- the circle

def order(a):
    return N // gcd(a % N, N)


def gen(a):
    """Canonical generator of <a>: gcd(a, N), a divisor of N (N itself for <0>)."""
    return gcd(a % N, N)


def contains(a, b):
    """<b> is a subgroup of <a>."""
    return gen(b) % gen(a) == 0


def meet(a, b):
    """Generator of <a> n <b>."""
    return lcm(gen(a), gen(b)) % N


def join(a, b):
    """Generator of <a> + <b>."""
    return gcd(gen(a), gen(b)) % N


def subgroup(a):
    return frozenset(range(0, N, gen(a)))


def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def divisors(n=N):
    return [d for d in range(1, n + 1) if n % d == 0]


# The named steps of the integrated build. A name is a reading of a step. The
# step, not the name, is what the checks use.
REGISTER = {
    "Coxeter step": 144, "tick": 864, "yuga 1": 1728, "yuga 2": 1296, "yuga 3": 864,
    "yuga 4": 432, "atlas": 36, "moon": 120, "sun": 1440, "day": 180, "signs": 360,
    "nakshatra": 160, "pada": 40, "half-turn": 2160, "Human Design gate": 64,
    "Hodge trace": 150, "Prema width": 2, "Sai": 3, "Siri": 4, "Shay": 4, "Sachin": 6,
    "Jessica": 7, "Rughnath": 8, "stray": 9, "edge pair": 10, "Salina": 12,
    "Prema index": 13, "forest maps": 40, "W0 scalar": 360000,
}

# The spine, smallest first: tick < order-10 (yuga) < Coxeter < atlas < circle.
SPINE = [864, 432, 144, 36, 1]


def integrated_claims():
    """The circle statements of the integrated build, each as (note, statement, holds)."""
    o = order
    tens = sorted(subgroup(432))
    out = [
        ("INTEGRATED", "4320 / 30 = 144, 6 x 144 = 864, order(864) = 5, 5 x 864 = 4320",
         N // 30 == 144 and 6 * 144 == 864 and o(864) == 5 and 5 * 864 == N),
        ("INTEGRATED", "the order-10 subgroup is the multiples of 432 and contains the tick",
         tens == list(range(0, N, 432)) and len(tens) == 10 and contains(432, 864)),
        ("INTEGRATED", "yuga 1 and 3 generate the order-5 subgroup, yuga 2 and 4 the order-10 one",
         subgroup(1728) == subgroup(864) and subgroup(1296) == subgroup(432) and o(1296) == 10),
        ("INTEGRATED", "tower: [C:<36>] = 36, [<36>:<432>] = 12, [<432>:<864>] = 2, |<864>| = 5",
         (N // o(36), o(36) // o(432), o(432) // o(864), o(864)) == (36, 12, 2, 5)),
        ("INTEGRATED", "64 x 6 x 6 x 6 x 5 = 69120 = 16 x 4320", 64 * 6 ** 3 * 5 == 16 * N),
        ("INTEGRATED", "<360> meets <160> in <1440>", meet(360, 160) == 1440),
        ("INTEGRATED", "160 = 16 mod 36 (atlas coset 16)", 160 % 36 == 16),
        ("INTEGRATED", "no element of order 7", all(7 * x % N for x in range(1, N))),
        ("INTEGRATED", "the pada step 40 is not in <432>", not contains(432, 40)),
        ("ALL_4320", "48 divisors, the order classes add to 4320",
         len(divisors()) == 48 and sum(phi(d) for d in divisors()) == N),
        ("ALL_4320", "<432> is one coset out of 432 and 40 is in another",
         N // o(432) == 432 and 40 % 432 != 0),
        ("SIDEREAL_DOTS", "order(64) = 135, 2160 / 135 = 16, 6 x 6 x 6 x 5 = 1080 = 27 x 40",
         o(64) == 135 and 2160 // 135 == 16 and 6 ** 3 * 5 == 1080 == 27 * 40),
        ("SIDEREAL_DOTS", "12 x 30 x 12 = 4320, order(30) = 144, 27 x 4 = 108",
         12 * 30 * 12 == N and o(30) == 144 and 27 * 4 == 108),
        ("SIDEREAL_DOTS", "order(360) = 12, <432> n <360> = {0, 2160}, 360 = 10 x 36",
         o(360) == 12 and subgroup(432) & subgroup(360) == {0, 2160} and 360 == 10 * 36),
        ("SEGMENT_NAMES", "the ten multiples of 432 read as 12, 24, 36, 48, 60, 72, 84, 96, 108 atlases",
         [x // 36 for x in tens[1:]] == [12, 24, 36, 48, 60, 72, 84, 96, 108] and 1296 == 36 ** 2),
        ("YUGA_LATTICE", "1728 + 1296 + 864 + 432 = 4320, 1728 = 2 x 864, 1296 = 3 x 432, 864 does not divide 1296",
         1728 + 1296 + 864 + 432 == N and 1728 == 2 * 864 and 1296 == 3 * 432 and 1296 % 864 != 0),
        ("DOTS_LATTICE", "<3> n <2> has order 720, <3> + <2> is the circle",
         o(meet(3, 2)) == 720 and join(3, 2) == 1),
        ("DOTS_LATTICE", "<4> n <6> has order 360, <4> + <6> = <2> of order 2160",
         o(meet(4, 6)) == 360 and join(4, 6) == 2 and o(2) == 2160),
        ("DOTS_LATTICE", "<12> lies in <3>, <2>, <4>, <6> and not in <10>",
         all(contains(s, 12) for s in (3, 2, 4, 6)) and not contains(10, 12)),
        ("DOTS_LATTICE", "<40> lies in <2> and <10>; <9> lies in <3> and not in <2>",
         contains(2, 40) and contains(10, 40) and contains(3, 9) and not contains(2, 9)),
        ("ALL_DOTS", "orders of 2, 3, 4, 6, 10, 12, 13, 7, 9 are 2160, 1440, 1080, 720, 432, 360, 4320, 4320, 480",
         [o(s) for s in (2, 3, 4, 6, 10, 12, 13, 7, 9)] == [2160, 1440, 1080, 720, 432, 360, N, N, 480]),
        ("ALL_DOTS", "order(40) = 108 = 3 x 36, 40 = 8 x 5 = 10 x 4", o(40) == 108 == 3 * 36),
        ("PAPER", "pada and tick generate <8> of order 540, index 8, meeting only at 0",
         join(40, 864) == 8 and o(8) == 540 and meet(40, 864) == 0),
        ("PAPER", "lcm(40, 864) = 4320, 36 x 40 = 1440, 250 x 1440 = 360000",
         lcm(40, 864) == N and 36 * 40 == 1440 and 250 * 1440 == 360000),
        ("PAPER", "<180> n <40> = <360> (order 12); <864> n <180> = 0",
         meet(180, 40) == 360 and o(360) == 12 and meet(864, 180) == 0),
        ("PAPER", "the step 18 has order 240 and contains <216> (order 20) and <90> (order 48), "
                  "which meet in <1080>",
         o(18) == 240 and contains(18, 216) and contains(18, 90) and meet(216, 90) == 1080),
        ("PAPER", "36 x {2,3,4,5,6,8} have orders 60, 40, 30, 24, 20, 15; 252 and 468 have order 120",
         [o(36 * k) for k in (2, 3, 4, 5, 6, 8)] == [60, 40, 30, 24, 20, 15]
         and o(252) == o(468) == 120),
        ("PAPER", "the step 120 has order 36 and the step 36 has order 120", o(120) == 36 and o(36) == 120),
    ]
    return out


def errata():
    """Six statements of the integrated build that the lemma corrects."""
    o = order
    return {
        "DOTS_LATTICE says the pada order 108 'meets the cycle order 720 only at 36, the atlas'. "
        "The meet <40> n <6> is <120>, of order 36 (the moon). The atlas <36> has order 120. "
        "The paper itself says 'The order 36 is not the atlas'":
            meet(40, 6) == 120 and o(120) == 36 and o(36) == 120 and subgroup(120) != subgroup(36),
        "SIDEREAL_DOTS: the signs and <432> 'meet at order 2, whose only element is 2160'. "
        "The subgroup is {0, 2160}; 2160 is its only nonzero element":
            subgroup(432) & subgroup(360) == {0, 2160},
        "paper: '360000 is not a step'. 360000 = 1440 mod 4320, so the W0 scalar is the sun step":
            360000 % N == 1440,
        "paper: 'Siri and Shay, both 4 ... Their sum 5 has order 864'. Siri + Shay = 8 (Rughnath, "
        "order 540); the 5 of order 864 is Prema + Sai":
            4 + 4 == 8 and o(8) == 540 and 2 + 3 == 5 and o(5) == 864,
        "paper: 'The doubling residues have circle orders 4320, 2160, 1080, 540, 864, 4320'. In "
        "doubling order 1, 2, 4, 8, 7, 5 they are 4320, 2160, 1080, 540, 4320, 864":
            [o(pow(2, k, 9)) for k in range(6)] == [N, 2160, 1080, 540, N, 864],
        "paper and e8Frame: 'Rank 8 times the mark sum 30 recovers the 120 positive roots'. "
        "8 x 30 = 240 is all the roots; the positive roots are 8 x 30 / 2 = 120":
            8 * 30 == 240 and 8 * 30 // 2 == 120,
    }


def tower_bijection(chain=SPINE):
    """Mixed-radix coordinates x = d0 + 36 d1 + 144 d2 + 432 d3 + 864 d4 along the spine."""
    gens = chain[::-1]                     # 1, 36, 144, 432, 864
    radices = [order(gens[i]) // order(gens[i + 1]) for i in range(len(gens) - 1)] + [order(gens[-1])]
    image = {sum(d * s for d, s in zip(digits, gens)) % N
             for digits in itertools.product(*[range(k) for k in radices])}
    return radices, len(image) == N


def chains_through(orders):
    """Maximal chains of subgroups from 0 to the circle through subgroups of the given orders."""
    def exps(n):
        return [sp.multiplicity(p, n) for p in (2, 3, 5)]

    def segment(a, b):
        e = [y - x for x, y in zip(exps(a), exps(b))]
        if min(e) < 0:
            return 0
        return factorial(sum(e)) // np.prod([factorial(k) for k in e])
    pts = [1] + sorted(orders) + [N]
    total = 1
    for a, b in zip(pts, pts[1:]):
        total *= segment(a, b)
    return int(total)


# ------------------------------------------------------------- E8 in the root basis

@lru_cache(maxsize=None)
def frame():
    """Bourbaki simple roots (rows of S), Cartan C, roots in the simple-root basis."""
    S = np.zeros((8, 8))
    S[0] = np.array([1, -1, -1, -1, -1, -1, -1, 1]) / 2
    S[1] = np.eye(8)[0] + np.eye(8)[1]
    for k in range(2, 8):
        S[k] = np.eye(8)[k - 1] - np.eye(8)[k - 2]
    B = S.T
    Binv = np.linalg.inv(B)
    C = np.round(S @ S.T).astype(np.int64)
    Cinv = np.round(np.linalg.inv(C)).astype(np.int64)
    R = handover.e8_roots()
    RB = np.round(R @ Binv.T).astype(np.int64)
    assert np.allclose(RB @ B.T, R) and np.array_equal(C @ Cinv, np.eye(8, dtype=np.int64))
    return B, Binv, C, Cinv, R, RB


I8 = np.eye(8, dtype=np.int64)


def mpow(M, k):
    out = I8.copy()
    for _ in range(k):
        out = out @ M
    return out


def inverse(w):
    """Inverse of a lattice isometry: w^-1 = C^-1 w^T C."""
    _, _, C, Cinv, _, _ = frame()
    return Cinv @ w.T @ C


def mat_order(M, cap=200):
    P = I8.copy()
    for k in range(1, cap + 1):
        P = P @ M
        if np.array_equal(P, I8):
            return k
    return None


def is_weyl(w):
    """w preserves the Cartan form and the root set (Aut(E8) = W(E8))."""
    _, _, C, _, _, RB = frame()
    return (np.array_equal(w.T @ C @ w, C)
            and {tuple(v) for v in RB @ w.T} == {tuple(v) for v in RB})


def to_root_basis(M_std):
    B, Binv, *_ = frame()
    X_ = Binv @ M_std @ B
    Xi = np.round(X_).astype(np.int64)
    assert np.allclose(X_, Xi)
    return Xi


def to_standard(M_root):
    B, Binv, *_ = frame()
    return B @ M_root @ Binv


def half_signed(M_std):
    """M_std = M/2 with M a signed 0-1 matrix having four nonzeros in each row."""
    M2 = 2 * M_std
    Mi = np.round(M2)
    return bool(np.allclose(M2, Mi) and np.all(np.abs(Mi) <= 1) and np.all((Mi != 0).sum(1) == 4))


def charpoly(M):
    return sp.Poly(sp.Matrix(M.tolist()).charpoly(X).as_expr(), X)


def coxeter():
    """c = s1 s2 ... s8 for the Bourbaki simple roots, in the simple-root basis."""
    _, _, C, *_ = frame()
    c = I8.copy()
    for i in range(8):
        s = I8.copy()
        s[i, :] -= C[i, :]
        c = c @ s
    return c


def exponents(M):
    ev = np.linalg.eigvals(M.astype(float))
    return sorted(int(round(np.angle(z) / (2 * np.pi) * 30)) % 30 for z in ev)


def root_orbits(M):
    _, _, _, _, _, RB = frame()
    seen, sizes = set(), []
    for v in RB:
        if tuple(v) in seen:
            continue
        k, u = 0, v.copy()
        while True:
            seen.add(tuple(u))
            u, k = M @ u, k + 1
            if np.array_equal(u, v):
                break
        sizes.append(k)
    return sizes


# ---------------------------------------------------------------- fixed momenta

def fixed_momenta(g):
    """The fixed points of g on the Brillouin torus R^8 / E8, in simple-root coordinates y
    (theta = 2 pi B y). Returns integer vectors Y and the common denominator n."""
    Minv = sp.Matrix((g - I8).tolist()).inv()
    gens = [tuple(Fraction(int(sp.fraction(e)[0]), int(sp.fraction(e)[1])) % 1
                  for e in Minv[:, j]) for j in range(8)]
    zero = tuple(Fraction(0) for _ in range(8))
    group, frontier = {zero}, [zero]
    while frontier:
        new = []
        for p in frontier:
            for q in gens:
                s = tuple((a + b) % 1 for a, b in zip(p, q))
                if s not in group:
                    group.add(s)
                    new.append(s)
        frontier = new
    n = lcm(*[v.denominator for p in group for v in p])
    Y = np.array([[int(v * n) for v in p] for p in sorted(group)], dtype=np.int64)
    return Y, n


@lru_cache(maxsize=None)
def _band_from_counts(n, counts):
    poly = sum(cnt * (X ** k + X ** ((n - k) % n)) for k, cnt in counts)
    rem = sp.rem(sp.expand(poly), sp.cyclotomic_poly(n, X), X) if n > 1 else poly
    rem = sp.Poly(rem, X)
    cs = rem.all_coeffs()[::-1]
    if any(c != 0 for c in cs[1:]):
        return None
    return sp.Rational(cs[0], 2) if cs else sp.Integer(0)


def band_value(Yrow, n):
    """lambda = sum over roots of cos(2 pi (C a) . y), exactly, at y = Y / n."""
    _, _, C, _, _, RB = frame()
    k = (RB @ C @ Yrow) % n
    counts = tuple(sorted(Counter(int(v) for v in k).items()))
    return _band_from_counts(n, counts)


def classify_fixed(g):
    """Tally the fixed momenta of g by (lambda, stabiliser type, Morse index of eps)."""
    B, _, _, _, R, _ = frame()
    Y, n = fixed_momenta(g)
    tally, gmax = Counter(), 0.0
    for row in Y:
        xs = B @ (row / n)
        lam = band_value(row, n)
        grad = 2 * np.pi * np.sin(2 * np.pi * R @ xs) @ R
        gmax = max(gmax, float(np.linalg.norm(grad)))
        typ, _ = handover.stabiliser(R, xs)
        H = 4 * np.pi ** 2 * (R.T * np.cos(2 * np.pi * R @ xs)) @ R
        idx = int((np.linalg.eigvalsh(H) < -1e-9).sum())
        tally[(str(lam), typ, idx)] += 1
    return len(Y), dict(tally), gmax


# ----------------------------------------------------------------- two carriers

def reflection_std(v):
    v = np.asarray(v, float)
    return np.eye(8) - 2 * np.outer(v, v) / (v @ v)


def carrier_rotations():
    """r: the K5 vertex rotation on coordinates 0..4 (the carrier's A4 of layer 11);
    r': a Coxeter element of the twin A4' (product of its four simple reflections)."""
    r = np.zeros((8, 8))
    for i in range(5):
        r[(i + 1) % 5, i] = 1
    for i in range(5, 8):
        r[i, i] = 1
    _, A, Ap = glue.a4_pair()
    Sp = glue.chain_order(glue.simple_system(Ap))
    rp = np.eye(8)
    for v in Sp:
        rp = rp @ reflection_std(v)
    return to_root_basis(r), to_root_basis(rp), A, Ap


def conjugator(src, dst, k_basis=(4, 4)):
    """Some w in W(E8) with w src w^-1 = dst, for src, dst of order 5 without fixed vectors.
    w is fixed by the images of two roots, alpha and beta, whose src-orbits span."""
    _, _, C, _, _, RB = frame()
    ip = lambda u, v: int(u @ C @ v)
    P_src = [mpow(src, k) for k in range(5)]
    P_dst = [mpow(dst, k) for k in range(5)]
    al = RB[0]
    for be in RB[1:]:
        basis = np.array([P_src[k] @ al for k in range(4)] + [P_src[k] @ be for k in range(4)]).T
        if round(abs(np.linalg.det(basis))) == 0:
            continue
        g_aa = [ip(al, P_src[k] @ al) for k in range(5)]
        g_bb = [ip(be, P_src[k] @ be) for k in range(5)]
        g_ab = [ip(al, P_src[k] @ be) for k in range(5)]
        cand_a = [v for v in RB if [ip(v, P_dst[k] @ v) for k in range(5)] == g_aa]
        cand_b = [v for v in RB if [ip(v, P_dst[k] @ v) for k in range(5)] == g_bb]
        binv = np.linalg.inv(basis)
        for ap in cand_a:
            for bp in cand_b:
                if [ip(ap, P_dst[k] @ bp) for k in range(5)] != g_ab:
                    continue
                img = np.array([P_dst[k] @ ap for k in range(4)] + [P_dst[k] @ bp for k in range(4)]).T
                W = img @ binv
                Wi = np.round(W).astype(np.int64)
                if np.allclose(W, Wi) and np.array_equal(Wi @ src, dst @ Wi) and is_weyl(Wi):
                    return Wi
        break
    return None


@lru_cache(maxsize=None)
def spine_clock():
    """The selected Coxeter element c' (conjugate of c) with c'^6 = r r', and its pieces."""
    c = coxeter()
    r, rp, A, Ap = carrier_rotations()
    g = r @ rp
    w = conjugator(mpow(c, 6), g)
    cp = w @ c @ inverse(w)
    return c, cp, r, rp, g, w


def orthogonal_orbit_family(M, size, count):
    """count mutually orthogonal M-orbits of roots of the given size, each spanning A_{size-1}
    with M acting as its Coxeter element (consecutive inner products -1)."""
    _, _, C, _, _, RB = frame()
    ip = lambda u, v: int(u @ C @ v)
    orbs, seen = [], set()
    for v in RB:
        if tuple(v) in seen:
            continue
        o = [v]
        while len(o) < size:
            o.append(M @ o[-1])
        for u in o:
            seen.add(tuple(u))
        if np.array_equal(M @ o[-1], v) and all(ip(o[i], o[i + 1]) == -1 for i in range(size - 1)) \
                and all(ip(o[i], o[j]) == 0 for i in range(size) for j in range(i + 2, size)
                        if not (i == 0 and j == size - 1)):
            orbs.append(o)

    def orth(a, b):
        return all(ip(x, y) == 0 for x in a for y in b)

    def search(chosen, start):
        if len(chosen) == count:
            return chosen
        for i in range(start, len(orbs)):
            if all(orth(orbs[i], orbs[j]) for j in chosen):
                got = search(chosen + [i], i + 1)
                if got:
                    return got
        return None
    pick = search([], 0)
    if pick is None:
        return None, len(orbs)
    vecs = [orbs[i][k] for i in pick for k in range(size - 1)]
    G = np.array(vecs) @ C @ np.array(vecs).T
    index = round(np.sqrt(round(np.linalg.det(G))))
    return index, len(orbs)


# ------------------------------------------------------------------ normalizer

def conjugates_cyclic(src, dst):
    """All w in W(E8) with w src w^-1 = dst, for src of order 30 (any root is a cyclic vector)."""
    _, _, C, _, _, RB = frame()
    al = RB[0]
    Ps = [mpow(src, k) for k in range(8)]
    Pd = [mpow(dst, k) for k in range(8)]
    basis = np.array([Ps[k] @ al for k in range(8)]).T
    binv = np.linalg.inv(basis)
    sols = []
    for ap in RB:
        W = np.array([Pd[k] @ ap for k in range(8)]).T @ binv
        Wi = np.round(W).astype(np.int64)
        if np.allclose(W, Wi) and np.array_equal(Wi.T @ C @ Wi, C) and np.array_equal(Wi @ src, dst @ Wi):
            sols.append(Wi)
    return sols


@lru_cache(maxsize=None)
def normalizer():
    """[(twist m, w)] for every w in W(E8) with w c' w^-1 = c'^m."""
    _, cp, *_ = spine_clock()
    return tuple((m, w) for m in UNITS30 for w in conjugates_cyclic(cp, mpow(cp, m)))


@lru_cache(maxsize=None)
def day_clock():
    """The selected day clock: order 24, d^4 = c'^5, d c' d^-1 = c'^7."""
    _, cp, *_ = spine_clock()
    return next(w for m, w in normalizer() if m == 7 and mat_order(w) == 24
                and np.array_equal(mpow(w, 4), mpow(cp, 5)))


# ------------------------------------------------------- what can act on the bath

def min_dimension(m):
    """Least n with an element of order m in GL_n(Z) (Kuzmanovich-Pavlichenkov)."""
    if m <= 2:
        return m - 1 if m == 2 else 0
    total = sum(phi(p ** sp.multiplicity(p, m)) for p in sp.primefactors(m))
    return total - 1 if m % 4 == 2 else total


def lattice_automorphism_orders(simple):
    """Orders of all automorphisms of the root lattice with the given simple roots (rows)."""
    G = np.round(simple @ simple.T).astype(int)
    roots = []
    n = len(simple)
    for coeffs in itertools.product(range(-2, 3), repeat=n):
        v = np.array(coeffs) @ simple
        if np.isclose(v @ v, 2):
            roots.append(v)
    roots = np.array(roots)
    auts = []
    for imgs in itertools.product(range(len(roots)), repeat=n):
        Im = roots[list(imgs)]
        if np.array_equal(np.round(Im @ Im.T).astype(int), G):
            auts.append(np.round(Im @ np.linalg.pinv(simple), 9))   # simple-root coordinates
    orders = Counter()
    for A_ in auts:
        P, k = A_.copy(), 1
        while not np.allclose(P, np.eye(n)):
            P, k = P @ A_, k + 1
        orders[k] += 1
    return len(auts), dict(orders)


def d8_two_orders():
    """2-parts of element orders in W(D8): signed cycle types with an even number of negative cycles."""
    best = 1
    for part in sp.utilities.iterables.partitions(8):
        cycles = [k for k, mult in part.items() for _ in range(mult)]
        for signs in itertools.product((1, -1), repeat=len(cycles)):
            if signs.count(-1) % 2:
                continue
            o = lcm(*[k if s > 0 else 2 * k for k, s in zip(cycles, signs)])
            best = max(best, 2 ** sp.multiplicity(2, o))
    return best


def a4_chain_count():
    """Ordered A4 chains (a1, a2, a3, a4) of roots: consecutive inner products -1, others 0."""
    _, _, C, _, _, RB = frame()
    G = RB @ C @ RB.T
    M1, M0 = (G == -1).astype(float), (G == 0).astype(float)
    total = 0.0
    for b in range(240):
        Xa = M1[:, b][:, None] * M0                 # (a, c): a ~ b, a _|_ c
        Yd = M1 * M0[:, b][:, None]                 # (d, c): d ~ c, d _|_ b
        total += float(M1[b] @ (Xa * (M0 @ Yd)).sum(axis=0))
    return int(round(total))


def find_orders(targets, seed=19, tries=20000):
    """Elements of W(E8) of the given orders, from seeded random products of root reflections."""
    _, _, C, _, _, RB = frame()
    refl = [I8 - np.outer(a, C @ a) for a in RB]
    rng = np.random.default_rng(seed)
    found = {}
    for _ in range(tries):
        w = I8.copy()
        for i in rng.integers(0, 240, size=int(rng.integers(8, 24))):
            w = w @ refl[i]
        o = mat_order(w, cap=60)
        if o in targets and o not in found:
            found[o] = w
            if len(found) == len(targets):
                break
    return found


# --------------------------------------------------------------------------- run

def run():
    rep = Report("19-spine")
    T, AR, OB, SR, RP, UF = (gates.THEOREM, gates.ARITHMETIC, gates.OBSTRUCTION,
                             gates.SELECTED_REFERENCE, gates.REPORTED, gates.UNFORMED)

    # (a) the circle in one lemma ---------------------------------------------------
    divs = divisors()
    lemma = all(len(subgroup(d)) == N // d for d in divs) and len({subgroup(a) for a in range(N)}) == 48
    duality = all(contains(a, b) == (gen(b) % gen(a) == 0) for a in divs for b in divs)
    rep.add("one lemma: Z/4320 has exactly 48 subgroups, one <d> of order 4320/d for each divisor d; "
            "<b> lies in <a> iff gcd(a,4320) | gcd(b,4320); meets are lcms, joins are gcds", T,
            lemma and duality, {"subgroups": 48})
    claims = integrated_claims()
    by_note = Counter(n for n, _, ok in claims)
    bad = [s for _, s, ok in claims if not ok]
    rep.add(f"the {len(claims)} circle statements of the integrated build hold under the lemma "
            "(INTEGRATED, ALL_4320, SIDEREAL_DOTS, SEGMENT_NAMES, YUGA_LATTICE, DOTS_LATTICE, "
            "ALL_DOTS, paper)", T, not bad, {"by note": dict(by_note), "failing": bad})
    for text, ok in errata().items():
        rep.add("correction: " + text, OB, ok)
    rep.add("readings: sun 1440, moon 120, day 180, signs 360, nakshatra 160, pada 40, atlas 36, tick 864, "
            "Prema 2, Jessica 7, Salina 12 ... are names for steps; the step decides every check",
            SR, len(REGISTER) == 29, {k: [v, order(v)] for k, v in REGISTER.items()})

    # (b) the spine refined ---------------------------------------------------------------
    radices, bij = tower_bijection()
    rep.add("the Coxeter subgroup <144> (order 30) lies between <432> (order 10) and the atlas <36> "
            "(order 120), so the tower refines to 36 x 4 x 3 x 2 x 5; the mixed-radix address "
            "x = d0 + 36 d1 + 144 d2 + 432 d3 + 864 d4 is a bijection on all 4320 elements", T,
            contains(36, 144) and contains(144, 432) and bij and radices == [36, 4, 3, 2, 5],
            radices, note="the integrated tower 36 x 12 x 2 x 5 skips the subgroup the spine starts from; "
                          "12 = [atlas : order-10] = 4 x 3 through the Coxeter subgroup")
    total, through = chains_through([]), chains_through([5, 10, 30, 120])
    rep.add("maximal chains of subgroups from 0 to the circle: 504 = 9!/(5! 3! 1!); exactly 6 pass "
            "through the whole spine tick < order-10 < Coxeter < atlas", T,
            (total, through) == (504, 6), [total, through])
    rep.add("the pada <40> (order 108) lies on no chain with the tick (5 and 108 are incomparable); "
            "pada + tick = <8>, the coil of layer 8 (order 540), an internal direct sum C108 + C5", OB,
            not contains(40, 864) and not contains(864, 40) and join(40, 864) == 8 and meet(40, 864) == 0)
    rep.add("the Coxeter step is the sum of the sun, the tick and the half-turn: "
            "864 + 1440 + 2160 = 144 mod 4320 (Z/30 = Z/5 x Z/3 x Z/2)", T,
            (864 + 1440 + 2160) % N == 144 and (order(864), order(1440), order(2160)) == (5, 3, 2))

    # (c) the Coxeter clock -------------------------------------------------------------------
    B, Binv, C, Cinv, R, RB = frame()
    c, cp, r, rp, g, w = spine_clock()
    rep.add("Cartan matrix of the Bourbaki simple roots: det 1, 7 bonds", T,
            round(np.linalg.det(C)) == 1 and int((C == -1).sum()) // 2 == 7)
    k30 = [k for k in range(1, 31) if np.array_equal(mpow(c, k), I8)]
    rep.add("the Coxeter element c = s1 s2 ... s8 has order 30 and c^15 = -I", T,
            k30 == [30] and np.array_equal(mpow(c, 15), -I8))
    rep.add("charpoly(c) = Phi_30 = x^8 + x^7 - x^5 - x^4 - x^3 + x + 1", T,
            charpoly(c) == sp.Poly(sp.cyclotomic_poly(30, X), X), str(charpoly(c).as_expr()))
    ex = exponents(c)
    rep.add("the exponents of c are the units mod 30: 1, 7, 11, 13, 17, 19, 23, 29 (sum 120 = number of "
            "positive roots; degrees m + 1 multiply to |W(E8)| = 696729600)", T,
            ex == UNITS30 and sum(ex) == 120 and int(np.prod([m + 1 for m in ex])) == handover.WE8, ex)
    rep.add("c permutes the 240 roots in 8 free orbits of 30 (240 = 8 x 30), so it commutes with the "
            "bath walk operator sum_alpha T_alpha and preserves the band lambda", T,
            sorted(root_orbits(c)) == [30] * 8 and is_weyl(c))
    rep.add("selected embedding: the order-30 subgroup <144> of the circle is sent to <c> by 144 -> c. "
            "There are phi(30) = 8 such isomorphisms, one for each exponent", SR, phi(30) == 8,
            note="the selection is the generator; every statement below is independent of it up to "
                 "relabelling by a unit mod 30")
    o4320 = sp.totient(27) > 8 and sp.totient(32) > 8
    rep.add("no homomorphism from the circle to the bath lattice extends 144 -> c: an extension needs an "
            "automorphism of order 4320, and no element of GL_8(Z) has order divisible by 27 or 32 "
            "(phi(27) = 18 > 8, phi(32) = 16 > 8)", OB, bool(o4320))

    # (d) fixed momenta ------------------------------------------------------------------------
    dets = {k: round(abs(np.linalg.det((mpow(c, k) - I8).astype(float)))) for k in range(1, 30)}
    expect = {k: {5: 25, 3: 81, 2: 256}.get(30 // gcd(k, 30), 1) for k in range(1, 30)}
    rep.add("|det(c^k - I)| fixed Bloch momenta: 25 for the order-5 powers (tick), 81 for the order-3 "
            "powers (sun), 256 for c^15 (half-turn 2160), 1 for the other 22 powers", T,
            dets == expect, {k: dets[k] for k in (1, 2, 3, 5, 6, 10, 15)})
    n6, t6, g6 = classify_fixed(mpow(cp, 6))
    n10, t10, g10 = classify_fixed(mpow(cp, 10))
    n15, t15, g15 = classify_fixed(mpow(cp, 15))
    rep.add("every fixed momentum is a critical point of the band (the gradient is fixed by an "
            "element with no eigenvalue 1, hence zero): max |grad| at the 362 fixed momenta", T,
            max(g6, g10, g15) < 1e-9, max(g6, g10, g15))
    rep.add("the tick c^6 fixes 25 momenta: the origin and 24 points of the A4+A4 family "
            "(lambda = -10, eps = 250, Morse index 4); the fixed group is (Z/5)^2", T,
            n6 == 25 and t6 == {("240", "E8", 0): 1, ("-10", "A4+A4", 4): 24}, t6)
    rep.add("the sun c^10 fixes 81 momenta: the origin and 80 points of E6+A2 (lambda = -3, eps = 243, "
            "index 2); the fixed group is (Z/3)^4", T,
            n10 == 81 and t10 == {("240", "E8", 0): 1, ("-3", "E6+A2", 2): 80}, t10)
    rep.add("the half-turn c^15 = -I fixes the 256 half-periods: the origin, all 120 points of E7+A1 "
            "(eps = 224) and all 135 of D8 (eps = 256)", T,
            n15 == 256 and t15 == {("240", "E8", 0): 1, ("16", "E7+A1", 1): 120, ("-16", "D8", 8): 135}, t15)
    tot = sum({5: 25, 3: 81, 2: 256}.get(30 // gcd(k, 30), 1) for k in range(1, 30))
    rep.add("the 29 non-identity Coxeter powers fix 22 x 1 + 4 x 25 + 2 x 81 + 256 = 540 momenta in "
            "all, the order of the coil", AR, tot == 540, tot, note="a count; no map joins it to the coil")

    # (e) two carriers -----------------------------------------------------------------------
    rep.add("selected Coxeter element c' = w c w^-1 (w in W(E8)) with c'^6 = r r' exactly: r is the K5 "
            "vertex rotation on the carrier's A4 (coordinates 0..4) and r' a Coxeter element of the twin "
            "A4'. The tick turns two carriers", T,
            w is not None and np.array_equal(mpow(cp, 6), g) and is_weyl(w) and is_weyl(cp)
            and charpoly(cp) == charpoly(c) and half_signed(to_standard(cp)),
            note="in the standard coordinates of E8, c' = M/2 with M a signed 0-1 matrix, "
                 "four nonzeros in each row")
    _, A4, A4p = glue.a4_pair()
    rS = to_standard(r)
    on_A4 = all(np.allclose(rS @ v, np.r_[v[4], v[:4], v[5:]]) for v in A4)
    fixes_twin = all(np.allclose(rS @ v, v) for v in A4p)
    rpS = to_standard(rp)
    twin_cycle = (all(np.allclose(rpS @ v, v) for v in A4)
                  and charpoly(rp) == sp.Poly(sp.cyclotomic_poly(5, X) * (X - 1) ** 4, X))
    rep.add("r permutes the 20 oriented K5 edges e_i - e_j of the carrier's A4 by i -> i+1 and fixes the "
            "twin; r' fixes the carrier's A4 and has charpoly Phi_5 (x-1)^4; r r' has charpoly Phi_5^2", T,
            on_A4 and fixes_twin and twin_cycle
            and charpoly(g) == sp.Poly(sp.cyclotomic_poly(5, X) ** 2, X))
    sun_index, sun_orbits = orthogonal_orbit_family(mpow(cp, 10), 3, 4)
    rep.add("the sun c'^10 permutes the roots in 80 triangles (A2 orbits); four orthogonal ones span "
            "A2^4 of index 9 in E8: the sun turns four triangles", T,
            sun_orbits == 80 and sun_index == 9, [sun_orbits, sun_index])
    half = np.array([[1, 1, 0, 0, 0, 0, 0, 0], [1, -1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0],
                     [0, 0, 1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, -1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, -1]], float)
    rep.add("the half-turn c'^15 = -I flips eight orthogonal edges, A1^8 of index 16. For p = 2, 3, 5 the "
            "order-p Coxeter element rotates 8/(p-1) copies of K_p and fixes p^(8/(p-1)) momenta", T,
            np.array_equal(mpow(cp, 15), -I8) and round(np.sqrt(np.linalg.det(half @ half.T))) == 16
            and [p ** (8 // (p - 1)) for p in (2, 3, 5)] == [256, 81, 25])
    s_ = mpow(cp, 10)
    rep.add("the Coxeter element is the product of the half-turn, the sun and the tick: c' = (-I) c'^10 c'^6, "
            "matching 144 = 2160 + 1440 + 864 on the circle", T,
            np.array_equal(cp, -(s_ @ g)) and np.array_equal(s_ @ g, g @ s_))
    rep.add("the yuga segments act on the bath: 1728 -> c'^12 = (r r')^2, 864 -> r r', 1296 -> c'^9 = -(r r')^4, "
            "432 -> c'^3 = -(r r')^3", T,
            all(np.array_equal(mpow(cp, k), sgn * mpow(g, e))
                for k, sgn, e in ((12, 1, 2), (6, 1, 1), (9, -1, 4), (3, -1, 3))))

    # (f) where 7 enters ------------------------------------------------------------------------
    Nm = normalizer()
    twists = Counter(m for m, _ in Nm)
    cent = [wv for m, wv in Nm if m == 1]
    rep.add("the normalizer of <c'> in W(E8) has order 240 = 30 x 8: every unit mod 30 (every exponent) is "
            "realized by conjugation, and the centralizer is <c'> itself (30 elements)", T,
            len(Nm) == 240 and all(twists[m] == 30 for m in UNITS30) and len(cent) == 30)
    o24 = [(m, wv) for m, wv in Nm if mat_order(wv) == 24]
    rep.add("no element of order 24 commutes with c'. Elements of order 24 normalizing <c'> turn it by 7 or "
            "13 = 7^-1 (20 each)", T,
            Counter(m for m, _ in o24) == Counter({7: 20, 13: 20}))
    day = day_clock()
    rep.add("the day clock d: order 24, charpoly Phi_24 = x^8 - x^4 + 1, d^4 = c'^5 (the two clocks agree "
            "on the circle's common subgroup <720> = 4 x 180 = 5 x 144), and d c' d^-1 = c'^7", T,
            charpoly(day) == sp.Poly(sp.cyclotomic_poly(24, X), X)
            and np.array_equal(day @ cp @ inverse(day), mpow(cp, 7)))
    atlas_orders = sorted({mat_order(wv @ inverse(cp)) for m, wv in o24
                           if np.array_equal(mpow(wv, 4), mpow(cp, 5))})
    rep.add("the circle's atlas 36 = 180 - 144 has order 120; on the bath d c'^-1 has order 24 for every day "
            "d with d^4 = c'^5, never 120. The atlas cannot act: the day and the Coxeter clock meet on the "
            "bath only through the twist 7", OB,
            order(36) == 120 and mat_order(day @ inverse(cp)) == 24 and atlas_orders == [24],
            atlas_orders)
    nd = {k: classify_fixed(mpow(day, k))[:2] for k in (6, 3)}
    rep.add("the day's quarter d^6 (step 1080, order 4) fixes 16 momenta: the origin and 15 D8 points at the "
            "band top; d^3 (step 540, order 8) fixes the origin and 3 D8 points; d^8 = c'^10 is the sun", T,
            nd[6] == (16, {("240", "E8", 0): 1, ("-16", "D8", 8): 15})
            and nd[3] == (4, {("240", "E8", 0): 1, ("-16", "D8", 8): 3})
            and np.array_equal(mpow(day, 8), mpow(cp, 10)), {k: v[1] for k, v in nd.items()})
    o20 = [(m, wv) for m, wv in Nm if mat_order(wv) == 20]
    v20 = next((wv for m, wv in o20 if np.array_equal(mpow(wv, 2), mpow(cp, 3))), None)
    rep.add("the order-20 clock <216> normalizes the Coxeter clock with the twist 11 (all 24 such elements); "
            "one with v^2 = c'^3 agrees on the shared yuga subgroup <432>, charpoly Phi_20", T,
            set(m for m, _ in o20) == {11} and len(o20) == 24 and v20 is not None
            and charpoly(v20) == sp.Poly(sp.cyclotomic_poly(20, X), X))
    rep.add("no element of order 18 normalizes the Coxeter clock (the clock <240> of order 18 cannot be "
            "fitted around it)", OB, all(mat_order(wv) != 18 for _, wv in Nm))
    rep.add("on the circle, x -> 7x is an automorphism of order 36 (the multiplicative order of 7 mod 4320); "
            "the circle has no element of order 7", T,
            sp.n_order(7, N) == 36 and all(7 * x % N for x in range(1, N)))

    # (g) what can act on the bath ------------------------------------------------------------------
    cand = [m for m in divs if min_dimension(m) <= 8]
    rep.add("degree bound: an element of order m | 4320 in GL_8(Z) needs m in {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, "
            "15, 16, 18, 20, 24, 30, 36, 40, 60}", T,
            cand == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 30, 36, 40, 60], cand)
    v2 = sp.multiplicity(2, handover.WE8) == sp.multiplicity(2, 2 ** 7 * factorial(8)) == 14
    rep.add("no element of order 16: W(D8) holds a Sylow 2-subgroup of W(E8) (both orders have 2-part 2^14) "
            "and its 2-elements have order at most 8", OB, v2 and d8_two_orders() == 8)
    S_A2 = np.array([[1, -1, 0], [0, 1, -1]], float)
    S_A4 = np.array([[1, -1, 0, 0, 0], [0, 1, -1, 0, 0], [0, 0, 1, -1, 0], [0, 0, 0, 1, -1]], float)
    nA2, oA2 = lattice_automorphism_orders(S_A2)
    nA4, oA4 = lattice_automorphism_orders(S_A4)
    chains = a4_chain_count()
    rep.add("no element of order 36: its 4th power has charpoly Phi_9 (x-1)^2, so (Steinberg) it lies in an "
            "E6 whose complement lattice is even of determinant 3, i.e. A2; Aut(A2) has 12 elements of "
            "orders 1, 2, 3, 6 and no element of order 4", OB, nA2 == 12 and set(oA2) == {1, 2, 3, 6}, oA2)
    rep.add("no element of order 40 or 60: its 8th or 12th power has charpoly Phi_5 (x-1)^4, so it lies in "
            "an A4; all 5806080 = 240 x 56 x 27 x 16 ordered A4 chains form one orbit (|W(E8)| / |W(A4')|), "
            "so both lattices are A4, and Aut(A4) (240 elements) has orders 1, 2, 3, 4, 5, 6, 10 only", OB,
            chains == 5806080 == handover.WE8 // 120 and nA4 == 240 and set(oA4) == {1, 2, 3, 4, 5, 6, 10},
            {"chains": chains, "Aut(A4) orders": oA4})
    have = {k: mpow(cp, 30 // k) for k in (1, 2, 3, 5, 6, 10, 15, 30)}
    have.update({24: day, 12: mpow(day, 2), 8: mpow(day, 3), 4: mpow(day, 6), 20: v20})
    have.update(find_orders({9, 18}))
    realized = sorted(k for k, M in have.items() if M is not None and mat_order(M) == k and is_weyl(M))
    rep.add("realized here by explicit elements of W(E8): orders 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, "
            "24, 30. So a subgroup of the circle acts faithfully on the bath iff its order is one of these; "
            "the maximal ones are <144> (30), the day <180> (24), <216> (20) and <240> (18)", T,
            realized == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30], realized)
    ok_orders = set(realized)
    verdict = {name: order(gen_) in ok_orders for name, gen_ in
               (("tick", 864), ("order-10", 432), ("Coxeter", 144), ("atlas", 36), ("circle", 1),
                ("sun", 1440), ("day", 180), ("signs", 360), ("moon", 120), ("nakshatra", 160),
                ("pada", 40), ("Salina", 12), ("Human Design gate", 64))}
    rep.add("the spine acts on the bath up to the Coxeter subgroup and stops at the atlas; the moon (36), "
            "nakshatra (27), pada (108) and atlas (120) subgroups cannot act at all", OB,
            verdict == {"tick": True, "order-10": True, "Coxeter": True, "atlas": False, "circle": False,
                        "sun": True, "day": True, "signs": True, "moon": False, "nakshatra": False,
                        "pada": False, "Salina": False, "Human Design gate": False}, verdict)
    rep.add("the Human Design count 69120 = |W(E8)| / |W(A6 x A1)| is the size of the A6+A1 critical family; "
            "exactly three families are whole numbers of circles: A6+A1 (16), A7 (4), A7+A1 (2)", AR,
            69120 == handover.WE8 // (factorial(7) * 2)
            and [n for n in (1, 120, 2240, 15120, 48384, 80640, 69120, 17280, 8640, 1920, 135)
                 if n % N == 0] == [69120, 17280, 8640],
            note="shared integers; no map joins Human Design to the bath")

    # stops that stay where they are ---------------------------------------------------------------
    rep.add("the Krishna lift is a typed composition whose operands are not in this repository; the sibling "
            "check of the stop is the integer test 4 + 5 != 4", RP, True,
            note="not replayable here; the check does not test the lift")
    rep.add("Prema's stage index 13 is not her width 2: on the circle <13> is the whole circle and <2> has "
            "index 2; the sibling check is 2 != 13", RP, order(13) == N and order(2) == 2160,
            note="the stage typing itself is canon data not in this repository")
    rep.add("birth time, epoch and ayanamsha: none is stored, so the sidereal readings stay counts", UF, True)
    return rep
