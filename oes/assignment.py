"""Layer 24. The particle assignment on E8's roots, worked out.

Layer 11 glued E8 from A4 + A4' and named the 200 mixed roots by the carrier's K5 sites and duads. Layer 12 named the
binding route e8 > su(5) + su(5)' and left three things to DYN_BIND: the choice of route, the generation multiplicity
and the chirality index. This layer works that route out on the 240 roots, as far as the roots go. It assigns
Standard-Model quantum numbers to every root and states what is forced, what is chosen and what is obstructed.
DYN_BIND stays NOT_INSTALLED, and nothing here enters the carrier Lagrangian.

(a) Both factors. The carrier's A4 (the roots e_i - e_j, i, j < 5) is taken as the GUT factor SU(5), and its
    orthogonal complement A4' as the family factor SU(5)'. The carrier's sites are e_a - u and its duads
    e_a + e_b - 2u, with u = (1, 1, 1, 1, 1; 0, 0, 0)/5. The twin's sites are mu_0 = 2u and
    mu_i = -u/2 + s_i/2 on the last three coordinates, with s = (1, 1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1).
    Its duads are mu_i + mu_j. Every root is a pair (carrier part, twin part). There are 20 carrier roots (24, 1),
    20 twin roots (1, 24), 50 pairs (duad, site') = (10, 5), 50 pairs (-site, duad') = (5b, 10) and their negatives
    (10b, 5b) and (5, 10b); each pair occurs once. Layer 11's (10, 5b') is this (10, 5): its twin 5 is renamed by
    the twin's outer automorphism.
(b) Moments. Over A4 + A4' the second moment is 10 I. Over (10, 5) and over (10b, 5b) it is 15 P + 10 P', and over
    (5b, 10) and (5, 10b) it is 10 P + 15 P', with P and P' the projections onto the two factors. Each class is
    anisotropic, but (10, 5) + (5b, 10) is 25 I, and the total is 60 I. The band
    eps(k) = sum (1 - cos rho.k) therefore starts 30 |k|^2.
(c) The Standard Model on the carrier factor (a selection). The colour sites are 0, 1, 2 and the weak sites 3, 4.
    T3 = (e_3 - e_4)/2 and Y = -(e_0 + e_1 + e_2)/3 + (e_3 + e_4)/2. Y is, up to scale, the only Cartan element of
    the carrier commuting with SU(3) x SU(2), and Q(e^c) = 1 fixes the scale. Every root then has colour, T3, Y and
    Q = T3 + Y. (10, 5) holds at each twin site a quark doublet, u^c and e^c; (5b, 10) holds at each twin duad d^c
    and a lepton doublet. The carrier roots are the gluons, W+- and the leptoquarks X, Y of charge -4/3 and -1/3,
    and the twin roots are the only roots with no Standard-Model charge. Every root's charge equals each of its
    colour coordinates mod 1, which is the Z6 of the Standard Model on all 240 roots. The second moment gives
    sum (T3.rho)^2 : sum (Q.rho)^2 = |T3|^2 : |Q|^2 = 3 : 8, which fixes no coupling.
(d) The choices are one Weyl orbit. J (site_a -> mu_a, mu_a -> -site_a) preserves the 240 roots, so it lies in
    W(E8), and J^2 = -1. J carries (10, 5) to (5b, 10) to (10b, 5b) to (5, 10b) and back, multiplying the grade
    in E8 / L0 = Z/5 by 2, the glue's doubling. The normalizer of A4 + A4' has order 4 x 120^2 = 57600 and acts on
    the four mixed classes through the four units of Z/5. The ten colour triples are one S5-orbit. So the factor,
    the orientation and the colour triple are all W(E8)-equivalent: the table is unique up to W(E8), and -1 in W(E8)
    exchanges every particle with its antiparticle. The 248 is real.
(e) Chirality (OBSTRUCTION). Suppose one root is taken from each pair +-rho, as whole multiplets: per twin site the
    10 or the 10b, and per twin duad the 5b or the 5 (2^15 choices). The SU(5) anomaly is then
    sum eps - sum eta, a sum of 5 signs minus a sum of 10, which is odd and never 0. The doublet count is
    5 x 3 + 10 = 25, which is odd: Witten's global anomaly. An anomaly-free set of 10's at twin sites S and 5b's at
    twin duads D needs |S| = |D|, and there are C(15, 5) = 3003 such sets, so the roots do not fix the generation
    number.
(f) Three generations (CONDITIONAL). Two roots of (10, 5) at twin sites i != j with disjoint carrier duads sum to
    the root of (5b, 10) at the duad {i, j}, and two roots at one twin site never sum to a root. So the 5b's are
    exactly the brackets of the 10's when D is the set of duads of S. In that case anomaly freedom
    |S| = C(|S|, 2) forces |S| = 3, a triangle of K5'. The ten triangles are one S5-orbit, with stabilizer
    S3 x S2. The triangle {0, 1, 2} gives 45 roots = 3 x 15, every perturbative anomaly vanishes on them, and they
    carry 12 doublets. The six-site port's roots e_a + e_5 are the 5 at the twin weight -(mu_3 + mu_4), at the
    duad disjoint from that triangle. The count 3 rests on the bracket rule and the orientation, which the roots
    do not supply, so B6 is sharpened, not discharged.
(g) Couplings are root triangles. A cubic coupling of three root fields needs alpha + beta + gamma = 0. On the
    triangle, 10_i 5b_jk reaches a 5b root (H_d) exactly when i is not in {j, k}, always at the twin duad {3, 4}: the
    down-quark and charged-lepton pattern is the permutation from each vertex to its opposite edge. 10_i 10_j
    reaches a 5 root (H_u) exactly when i != j, at -(mu_i + mu_j). No root triangle couples two 10's at one twin
    site, so the GUT top coupling 10_3 10_3 5_H has no root realization. A symmetric matrix with zero diagonal is
    never of rank one, so no up-type coupling matrix on these roots has rank one (OBSTRUCTION). The roots fix which
    couplings can be nonzero, not their sizes: no Yukawa block is formed.
(h) The six-site port. Its memory variance M_2 - M_1^2 = X^T X, with X = (1 - P) Delta P, counts the bath points
    next to two sites: 240 - 5 = 235 on the diagonal and 56 - 4 = 52 off it, so it is 183 I + 52 J (layer 22).
    Its eigenvalues 183 and 495 are positive, so X has no kernel. Every visible state leaks into the bath at the
    first step, and the six channels cannot evolve on their own. The brackets of the triangle's 10's with its 5b's
    are exactly the port's five roots.

Coordinates are kept as integers times 1/10 (roots in (1/2)Z^8, the factors' weights in (1/10)Z^8), so every
statement is exact.
"""

import itertools
import json
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

import numpy as np
import sympy as sp

from . import counts, gates, glue
from .record import Report

DUADS = list(itertools.combinations(range(5), 2))
COLOUR, WEAK = (0, 1, 2), (3, 4)
U10 = np.array([2, 2, 2, 2, 2, 0, 0, 0])                                   # 10 u
SITE = np.array([10 * np.eye(8, dtype=int)[a] - U10 for a in range(5)])    # 10 (e_a - u), the carrier's 5
DUAD = {d: SITE[d[0]] + SITE[d[1]] for d in DUADS}                         # the carrier's 10
TWIN = np.array([[4, 4, 4, 4, 4, 0, 0, 0]] + [[-1] * 5 + [5 * x for x in s]
                                              for s in ((1, 1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1))])
TWIN_DUAD = {d: TWIN[d[0]] + TWIN[d[1]] for d in DUADS}
CLASSES = ["(24,1)", "(1,24)", "(10,5)", "(5b,10)", "(10b,5b)", "(5,10b)"]
CONJUGATE = {"(10,5)": "(10b,5b)", "(5b,10)": "(5,10b)", "(10b,5b)": "(10,5)", "(5,10b)": "(5b,10)",
             "(24,1)": "(24,1)", "(1,24)": "(1,24)"}
GRADE = {"(24,1)": 0, "(1,24)": 0, "(5,10b)": 1, "(10,5)": 2, "(10b,5b)": 3, "(5b,10)": 4}   # carrier class in A4*/A4
F = Fraction
Y = [F(-1, 3)] * 3 + [F(1, 2)] * 2 + [F(0)] * 3
T3 = [F(0)] * 3 + [F(1, 2), F(-1, 2)] + [F(0)] * 3
QE = [y + t for y, t in zip(Y, T3)]
TRIANGLE, PORT_DUAD = (0, 1, 2), (3, 4)
DATA = Path(__file__).resolve().parent.parent / "data" / "e8_assignment.json"


def roots10():
    return np.rint(10 * glue.roots()).astype(int)


def carrier_part(r):
    """10 P rho: the first five coordinates minus their mean (exact: their sum is a multiple of 5)."""
    s = int(r[:5].sum())
    assert s % 5 == 0
    c = np.zeros(8, dtype=int)
    c[:5] = r[:5] - s // 5
    return c


def label(v, sites, duads):
    """Name a weight (times 10) as zero, a signed site, a signed duad or a root (site difference)."""
    if not v.any():
        return ("0",)
    for a in range(5):
        for s in (1, -1):
            if np.array_equal(v, s * sites[a]):
                return ("site", a, s)
    for d in DUADS:
        for s in (1, -1):
            if np.array_equal(v, s * duads[d]):
                return ("duad", d, s)
    for a, b in itertools.permutations(range(5), 2):
        if np.array_equal(v, sites[a] - sites[b]):
            return ("root", (a, b))
    return None


def kind(cl, tl):
    if tl == ("0",) and cl[0] == "root":
        return "(24,1)"
    if cl == ("0",) and tl[0] == "root":
        return "(1,24)"
    pairs = {("duad", 1, "site", 1): "(10,5)", ("site", -1, "duad", 1): "(5b,10)",
             ("duad", -1, "site", -1): "(10b,5b)", ("site", 1, "duad", -1): "(5,10b)"}
    return pairs.get((cl[0], cl[-1], tl[0], tl[-1]) if len(cl) == 3 and len(tl) == 3 else None)


def classify():
    """Each root (times 10) with its class, carrier label and twin label."""
    out = []
    for r in roots10():
        lam = carrier_part(r)
        cl, tl = label(lam, SITE, DUAD), label(r - lam, TWIN, TWIN_DUAD)
        out.append((r, kind(cl, tl) if cl and tl else None, cl, tl))
    return out


def dot(h, r):
    """h . rho for a rational Cartan vector h and a root given times 10."""
    return sum((hi * int(ri) for hi, ri in zip(h, r)), F(0)) / 10


# ------------------------------------------------------------------ (a) both factors

def factors():
    rows = classify()
    n = Counter(k for _, k, _, _ in rows)
    pairs = {k: Counter((cl[1], tl[1]) for _, kk, cl, tl in rows if kk == k) for k in CLASSES[2:]}
    product = {"(10,5)": {(d, i) for d in DUADS for i in range(5)}, "(5b,10)": {(a, d) for a in range(5) for d in DUADS}}
    product["(10b,5b)"], product["(5,10b)"] = product["(10,5)"], product["(5b,10)"]
    gram = TWIN @ TWIN.T
    twin_roots = {tuple(TWIN[i] - TWIN[j]) for i, j in itertools.permutations(range(5), 2)}
    _, _, Ap = glue.a4_pair()
    out, _, gpairs, _ = glue.decompose()
    return {
        "the twin sites mu_i sum to 0 with |mu_i|^2 = 4/5 and mu_i.mu_j = -1/5, and their differences are the 20 roots "
        "of A4', the orthogonal complement of the carrier's A4": not TWIN.sum(0).any()
        and np.array_equal(gram, 100 * np.eye(5, dtype=int) - 20) and twin_roots == {tuple(np.rint(10 * r).astype(int)) for r in Ap},
        "every root is a carrier root, a twin root, a pair (duad, site'), a pair (-site, duad') or minus one of these "
        "pairs: 20 + 20 + 4 x 50": None not in n and n == Counter({"(24,1)": 20, "(1,24)": 20, "(10,5)": 50, "(5b,10)": 50,
                                                                    "(10b,5b)": 50, "(5,10b)": 50}),
        "each class is the full product of its weight sets, each pair once: (10, 5) is the carrier's 10 duads times the "
        "twin's 5 sites, (5b, 10) the carrier's 5 sites times the twin's 10 duads, so the twin's 10 is Lambda^2 of its 5":
            all(set(pairs[k]) == product[k] and set(pairs[k].values()) == {1} for k in CLASSES[2:]),
        "it agrees with layer 11: 20 + 20 + 200, and four class pairs of 50 for the carrier grades 1, 2, 3, 4":
            out == {"A4": 20, "A4'": 20, "mixed": 200} and sorted(k1 for k1, _ in gpairs) == [1, 2, 3, 4]
            and set(gpairs.values()) == {50},
    }


# ------------------------------------------------------------------ (b) moments

def moments():
    rows = classify()
    P = np.zeros((8, 8), dtype=int)
    P[:5, :5] = 5 * np.eye(5, dtype=int) - 1                                # 5 P
    Pp = 5 * np.eye(8, dtype=int) - P                                       # 5 P'
    cov = {k: sum((np.outer(r, r) for r, kk, _, _ in rows if kk == k), np.zeros((8, 8), dtype=int)) for k in CLASSES}
    L0 = cov["(24,1)"] + cov["(1,24)"]                                      # times 100
    total = sum(cov.values())
    k = [F(3, 7), F(-1, 2), F(2, 5), F(1), F(0), F(-5, 3), F(1, 4), F(2)]
    quad = sum(dot(k, r) ** 2 for r, *_ in rows)
    five = sum(np.outer(m, m) for m in TWIN)
    ten = sum(np.outer(DUAD[d], DUAD[d]) for d in DUADS)
    return {
        "over A4 + A4' the second moment is 10 I (each A4 gives 10 times its projection)": np.array_equal(L0, 1000 * np.eye(8, dtype=int)),
        "the weight covariances are sum mu mu^T = P' over the 5 and sum lambda lambda^T = 3 P over the 10, so (10, 5) "
        "and (10b, 5b) each give 5 x 3 P + 10 P' = 15 P + 10 P', and (5b, 10) and (5, 10b) each give 10 P + 15 P'":
            np.array_equal(5 * five, 100 * Pp) and np.array_equal(5 * ten, 300 * P)
            and all(np.array_equal(5 * cov[c], 1500 * P + 1000 * Pp) for c in ("(10,5)", "(10b,5b)"))
            and all(np.array_equal(5 * cov[c], 1000 * P + 1500 * Pp) for c in ("(5b,10)", "(5,10b)")),
        "each mixed class is anisotropic, but (10, 5) + (5b, 10) is 25 I and all 240 roots give 10 I + 2 x 25 I = 60 I":
            len(set(np.diag(cov["(10,5)"]).tolist())) == 2
            and np.array_equal(cov["(10,5)"] + cov["(5b,10)"], 2500 * np.eye(8, dtype=int))
            and np.array_equal(total, 6000 * np.eye(8, dtype=int)),
        "so the band eps(k) = sum (1 - cos rho.k) starts (1/2) sum (rho.k)^2 = 30 |k|^2, the native dispersion "
        "coefficient (checked at a rational k)": quad == 60 * sum(x * x for x in k) and quad / 2 == 30 * sum(x * x for x in k),
    }


# ------------------------------------------------------------------ (c) the Standard Model on the carrier factor

def colour_part(r):
    lam = [F(int(x), 10) for x in carrier_part(r)[:3]]
    m = sum(lam, F(0)) / 3
    return [x - m for x in lam]


def particle(k, cl, tl):
    """The Standard-Model name of a root in the selected orientation; conjugate classes get a trailing '~'."""
    if k == "(1,24)":
        return "family"
    if k == "(24,1)":
        a, b = cl[1]
        if a in COLOUR and b in COLOUR:
            return "gluon"
        if a in WEAK and b in WEAK:
            return "W+" if (a, b) == (3, 4) else "W-"
        if a in COLOUR:
            return "X" if b == 3 else "Y"                                    # (3, 2) at Y = -5/6: Q = -4/3, -1/3
        return "X~" if a == 3 else "Y~"
    bar = "" if k in ("(10,5)", "(5b,10)") else "~"
    if k in ("(10,5)", "(10b,5b)"):
        a, b = cl[1]
        if b in COLOUR:
            return "u^c" + bar
        if a in COLOUR:
            return ("u" if b == 3 else "d") + bar
        return "e^c" + bar
    a = cl[1]
    return ("d^c" if a in COLOUR else "e" if a == 3 else "nu") + bar


def table():
    """Every root with its class, labels and Standard-Model quantum numbers."""
    out = []
    for r, k, cl, tl in classify():
        out.append({"root": r, "class": k, "carrier": cl, "twin": tl, "particle": particle(k, cl, tl),
                    "T3": dot(T3, r), "Y": dot(Y, r), "Q": dot(QE, r), "colour": colour_part(r)})
    return out


def standard_model():
    rows = table()
    by = lambda k: Counter(x["particle"] for x in rows if x["class"] == k)
    charge = {}
    for x in rows:
        charge.setdefault(x["particle"], set()).add((x["Y"], x["Q"]))
    h = sp.Matrix([[1, -1, 0, 0, 0], [0, 1, -1, 0, 0], [0, 0, 0, 1, -1], [1, 1, 1, 1, 1]])
    null = h.nullspace()
    neutral = [x for x in rows if x["Y"] == 0 and x["T3"] == 0 and not any(x["colour"])]
    t3sq, qsq = sum(x["T3"] ** 2 for x in rows), sum(x["Q"] ** 2 for x in rows)
    per_class = all(sum(x["T3"] ** 2 for x in rows if x["class"] == k) * 8
                    == 3 * sum(x["Q"] ** 2 for x in rows if x["class"] == k) for k in CLASSES[2:])
    return {
        "the Cartan elements of the carrier factor that commute with SU(3) x SU(2) (orthogonal to e_0 - e_1, e_1 - e_2 "
        "and e_3 - e_4) form one line, spanned by Y = (-1/3, -1/3, -1/3, 1/2, 1/2); Q(e^c) = 1 fixes its scale":
            len(null) == 1 and [F(int(x.p), int(x.q)) for x in null[0] / null[0][3] / 2] == Y[:5],
        "(10, 5) holds at each of the 5 twin sites u, d (3 colours each), u^c (3) and e^c; (5b, 10) holds at each of "
        "the 10 twin duads d^c (3), e and nu; the conjugate classes hold the antiparticles":
            by("(10,5)") == Counter({"u": 15, "d": 15, "u^c": 15, "e^c": 5})
            and by("(5b,10)") == Counter({"d^c": 30, "e": 10, "nu": 10})
            and by("(10b,5b)") == Counter({"u~": 15, "d~": 15, "u^c~": 15, "e^c~": 5})
            and by("(5,10b)") == Counter({"d^c~": 30, "e~": 10, "nu~": 10}),
        "the carrier roots are the 6 gluon roots, W+ and W-, and 12 leptoquark roots X, Y (and conjugates) at "
        "Y = -5/6 with Q = -4/3 and -1/3; the twin roots are all family roots": by("(24,1)") == Counter(
            {"gluon": 6, "W+": 1, "W-": 1, "X": 3, "Y": 3, "X~": 3, "Y~": 3}) and by("(1,24)") == Counter({"family": 20}),
        "every root of each kind has the Standard Model's hypercharge and charge, and its antiparticle the opposite: "
        "u (1/6, 2/3), d (1/6, -1/3), u^c (-2/3, -2/3), "
        "e^c (1, 1), d^c (1/3, 1/3), e (-1/2, -1), nu (-1/2, 0), W+- (0, +-1), X (-5/6, -4/3), Y (-5/6, -1/3)":
            all(charge[n] == {v} and charge[n + "~"] == {(-v[0], -v[1])} for n, v in {
                "u": (F(1, 6), F(2, 3)), "d": (F(1, 6), F(-1, 3)), "u^c": (F(-2, 3), F(-2, 3)), "e^c": (1, 1),
                "d^c": (F(1, 3), F(1, 3)), "e": (F(-1, 2), -1), "nu": (F(-1, 2), 0), "X": (F(-5, 6), F(-4, 3)),
                "Y": (F(-5, 6), F(-1, 3))}.items())
            and charge["W+"] == {(0, 1)} and charge["W-"] == {(0, -1)} and charge["gluon"] == charge["family"] == {(0, 0)},
        "charge quantization on all 240 roots: Q minus each colour coordinate is an integer, so colour singlets and "
        "octets have integer charge, triplets 2/3 and antitriplets 1/3 mod 1 (the Z6 of the Standard Model)":
            all((x["Q"] - c).denominator == 1 for x in rows for c in x["colour"]),
        "the roots with no Standard-Model charge (Y = T3 = 0, colour weight 0) are exactly the 20 family roots":
            len(neutral) == 20 and all(x["class"] == "(1,24)" for x in neutral),
        "the second moment fixes the trace ratio: sum (T3.rho)^2 : sum (Q.rho)^2 = 60 |T3|^2 : 60 |Q|^2 = 3 : 8 over all "
        "240 roots and over each mixed class; it fixes no coupling": t3sq == 60 * sum(t * t for t in T3)
            and qsq == 60 * sum(q * q for q in QE) and t3sq / qsq == F(3, 8) and per_class,
    }


# ------------------------------------------------------------------ (d) the choices are one Weyl orbit

def swap():
    """J: site_a -> mu_a, mu_a -> -site_a, as an exact 8 x 8 matrix."""
    S = sp.Matrix.hstack(*[sp.Matrix(SITE[a]) for a in range(4)], *[sp.Matrix(TWIN[a]) for a in range(4)])
    T = sp.Matrix.hstack(*[sp.Matrix(TWIN[a]) for a in range(4)], *[-sp.Matrix(SITE[a]) for a in range(4)])
    return T * S.inv()


def weyl_orbit():
    J = swap()
    rows = classify()
    keys = {tuple(r): k for r, k, _, _ in rows}
    image = [J * sp.Matrix(r) for r, *_ in rows]
    integral = all(all(x.is_integer for x in v) for v in image)
    moved = {k: Counter(keys.get(tuple(int(x) for x in v)) for v, (_, kk, _, _) in zip(image, rows) if kk == k)
             for k in CLASSES} if integral else {}
    permutes = integral and {tuple(int(x) for x in v) for v in image} == set(keys)
    cycle = {"(10,5)": "(5b,10)", "(5b,10)": "(10b,5b)", "(10b,5b)": "(5,10b)", "(5,10b)": "(10,5)"}
    return J, rows, keys, moved, cycle, permutes


def normalizer():
    """Which sign changes of the two factors keep the roots: (1, 1) and (-1, -1) only."""
    rows = classify()
    roots = {tuple(r) for r, *_ in rows}
    out = {}
    for s, t in itertools.product((1, -1), repeat=2):
        img = set()
        for r, *_ in rows:
            lam = carrier_part(r)
            img.add(tuple(s * lam + t * (r - lam)))
        out[(s, t)] = img == roots
    return out


def choices():
    J, rows, keys, moved, cycle, permutes = weyl_orbit()
    signs = normalizer()
    triples = {frozenset(c) for c in itertools.combinations(range(5), 3)}
    orbit = {frozenset(p[i] for i in COLOUR) for p in itertools.permutations(range(5))}
    perm_keeps = all({tuple(np.r_[r[list(p)], r[5:]]) for r, *_ in rows} == set(keys)
                     and all(np.array_equal(np.r_[TWIN[i][list(p)], TWIN[i][5:]], TWIN[i]) for i in range(5))
                     for p in itertools.permutations(range(5)))
    neg = {k: Counter(keys[tuple(-r)] for r, kk, _, _ in rows if kk == k) for k in CLASSES}
    return {
        "J (site_a -> mu_a, mu_a -> -site_a) is orthogonal and permutes the 240 roots, so it lies in W(E8) (the "
        "automorphisms of the E8 root system are its Weyl group), and J^2 = -1": J.T * J == sp.eye(8) and permutes
        and J * J == -sp.eye(8),
        "J exchanges the carrier and twin factors and carries (10, 5) -> (5b, 10) -> (10b, 5b) -> (5, 10b) -> (10, 5), "
        "multiplying the grade in E8 / L0 = Z/5 by 2, the glue's doubling": moved["(24,1)"] == Counter({"(1,24)": 20})
        and moved["(1,24)"] == Counter({"(24,1)": 20})
        and all(moved[a] == Counter({b: 50}) for a, b in cycle.items())
        and all(GRADE[b] == 2 * GRADE[a] % 5 for a, b in cycle.items()),
        "of the sign changes of the two factors only (1, 1) and (-1, -1) keep the roots, so the normalizer of A4 + A4' "
        "is (W(A4) x W(A4')) x <J>, of order 2 x 2 x 120^2 = 57600, acting on the four mixed classes through all four "
        "units of Z/5 (W x W' as 1, J as 2, -1 as 4)": signs == {(1, 1): True, (1, -1): False, (-1, 1): False, (-1, -1): True}
        and 2 * 2 * 120 ** 2 == 57600 and sorted({pow(2, n, 5) for n in range(4)}) == [1, 2, 3, 4],
        "the 120 permutations of the carrier sites are Weyl elements that keep every twin weight, and the ten colour "
        "triples are one orbit: the colour choice is unique up to W(A4)": perm_keeps and orbit == triples
        and len(triples) == 10,
        "-1 lies in W(E8) and sends each mixed class to its conjugate: no W(E8)-invariant rule tells a particle from "
        "its antiparticle (the 248 is real)": all(neg[k] == Counter({CONJUGATE[k]: n}) for k, n in
                                                   (("(10,5)", 50), ("(5b,10)", 50), ("(10b,5b)", 50), ("(5,10b)", 50))),
    }


# ------------------------------------------------------------------ (e) chirality

def anomaly(weights, h):
    return sum(dot(h, r) ** 3 for r in weights)


def multiplets():
    """The mixed roots grouped into Standard-Model GUT multiplets: per twin site the 10, per twin duad the 5b."""
    rows = classify()
    ten = {i: [r for r, k, cl, tl in rows if k == "(10,5)" and tl[1] == i] for i in range(5)}
    fiveb = {d: [r for r, k, cl, tl in rows if k == "(5b,10)" and tl[1] == d] for d in DUADS}
    return ten, fiveb


def chirality():
    ten, fiveb = multiplets()
    h = [F(1), F(2), F(3), F(4), F(-10), F(0), F(0), F(0)]
    a5 = anomaly([SITE[a] for a in range(5)], h)
    a10 = {i: anomaly(ten[i], h) / a5 for i in ten}
    a5b = {d: anomaly(fiveb[d], h) / a5 for d in fiveb}
    totals = Counter()
    for eps in itertools.product((1, -1), repeat=5):
        s = sum(e * a10[i] for e, i in zip(eps, range(5)))
        for eta in itertools.product((1, -1), repeat=10):
            totals[s + sum(e * a5b[d] for e, d in zip(eta, DUADS))] += 1
    up = lambda rs: sum(1 for r in rs if r[3] - r[4] == 10)            # one T3 = +1/2 member per doublet
    doublets = sum(up(ten[i]) for i in ten) + sum(up(fiveb[d]) for d in fiveb)
    vandermonde = sum(comb(5, k) * comb(10, k) for k in range(6))
    return {
        "per twin site the 10 has anomaly A(10) = A(5) = 1 and per twin duad the 5b has -1 (layer 12's B4)":
            set(a10.values()) == {1} and set(a5b.values()) == {-1},
        "taking one of each pair +-rho as whole multiplets (the 10 or 10b at each twin site, the 5b or 5 at each twin "
        "duad, 2^15 = 32768 choices), the SU(5) anomaly sum eps - sum eta is odd every time, from -15 to 15, never 0":
            sum(totals.values()) == 2 ** 15 and all(t.denominator == 1 and t.numerator % 2 for t in totals)
            and min(totals) == -15 and max(totals) == 15,
        "and every such choice carries 5 x 3 + 10 x 1 = 25 SU(2) doublets, an odd number: Witten's global anomaly. "
        "No chiral assignment that uses each mixed root pair once is consistent": doublets == 25
            and {up(ten[i]) for i in ten} == {3} and {up(fiveb[d]) for d in fiveb} == {1},
        "an anomaly-free set of 10's at twin sites S and 5b's at twin duads D needs |S| = |D|; there are "
        "sum C(5,k) C(10,k) = C(15,5) = 3003 such sets, so the roots do not fix the generation number":
            vandermonde == comb(15, 5) == 3003,
    }


# ------------------------------------------------------------------ (f) three generations, conditionally

def bracket_rule():
    ten, fiveb = multiplets()
    roots = {tuple(r) for r in roots10()}
    where = {tuple(r): d for d in DUADS for r in fiveb[d]}
    ok, made = True, {d: set() for d in DUADS}
    for i, j in itertools.product(range(5), repeat=2):
        for a in ten[i]:
            for b in ten[j]:
                s = tuple(a + b)
                if s in roots:
                    dl, dm = label(carrier_part(a), SITE, DUAD)[1], label(carrier_part(b), SITE, DUAD)[1]
                    ok &= i != j and not set(dl) & set(dm) and where.get(s) == tuple(sorted((i, j)))
                    if s in where:
                        made[where[s]].add(s)
                elif i != j:
                    dl, dm = label(carrier_part(a), SITE, DUAD)[1], label(carrier_part(b), SITE, DUAD)[1]
                    ok &= bool(set(dl) & set(dm))
    return ok and all(len(made[d]) == 5 for d in DUADS)


def generations():
    closed = [S for k in range(6) for S in itertools.combinations(range(5), k)
              if k == len(list(itertools.combinations(S, 2)))]
    stab = [p for p in itertools.permutations(range(5)) if {p[i] for i in TRIANGLE} == set(TRIANGLE)]
    ten, fiveb = multiplets()
    sel = [r for i in TRIANGLE for r in ten[i]] + [r for d in itertools.combinations(TRIANGLE, 2) for r in fiveb[d]]
    rows = {tuple(x["root"]): x for x in table()}
    names = Counter(rows[tuple(r)]["particle"] for r in sel)
    hc = [F(1), F(2), F(-3), F(0), F(0), F(0), F(0), F(0)]
    yy = lambda r: rows[tuple(r)]["Y"]
    anomalies = {
        "SU(3)^3": sum(dot(hc, r) ** 3 for r in sel), "SU(3)^2 Y": sum(yy(r) * dot(hc, r) ** 2 for r in sel),
        "SU(2)^2 Y": sum(yy(r) * dot(T3, r) ** 2 for r in sel), "Y^3": sum(yy(r) ** 3 for r in sel),
        "Y": sum(yy(r) for r in sel)}
    doublets = sum(1 for r in sel if dot(T3, r) == F(1, 2))
    port = [10 * np.eye(8, dtype=int)[a] + 10 * np.eye(8, dtype=int)[5] for a in range(5)]
    port_cls = Counter((kind(label(carrier_part(r), SITE, DUAD), label(r - carrier_part(r), TWIN, TWIN_DUAD)),
                        label(r - carrier_part(r), TWIN, TWIN_DUAD)[1]) for r in port)
    return {
        "two roots of (10, 5) sum to a root exactly when their twin sites differ and their carrier duads are disjoint, "
        "and the sum is then the root of (5b, 10) at the twin duad of the two sites; every root of (5b, 10) arises so, "
        "and two roots at one twin site never sum to a root": bracket_rule(),
        "if the 5b's are exactly the brackets of the 10's (D = the duads of S), anomaly freedom |S| = C(|S|, 2) "
        "forces |S| = 3: the closed anomaly-free selections are the ten triangles of K5' (and the empty one)":
            [len(S) for S in closed] == [0] + [3] * 10,
        "the ten triangles are one S5-orbit and the triangle {0, 1, 2} has stabilizer S3 x S2 of order 12, the family "
        "symmetry left by the selection": len(stab) == 12 and len({frozenset(p[i] for i in TRIANGLE)
                                                                  for p in itertools.permutations(range(5))}) == 10,
        "on the triangle {0, 1, 2}: 45 roots, three times u, d, u^c, e^c (10 per site) and d^c, e, nu (5 per edge), "
        "the 45 Weyl fermions of three generations": len(sel) == 45 and names == Counter(
            {"u": 9, "d": 9, "u^c": 9, "e^c": 3, "d^c": 9, "e": 3, "nu": 3}),
        "every perturbative anomaly vanishes on the 45 (SU(3)^3, SU(3)^2 Y, SU(2)^2 Y, Y^3 and the mixed gravitational "
        "Y), and they carry 12 doublets, an even number": set(anomalies.values()) == {0} and doublets == 12,
        "the six-site port's five roots e_a + e_5 are the GUT 5 at the twin weight -(mu_3 + mu_4): their twin duad "
        "{3, 4} is the one disjoint from the triangle": port_cls == Counter({("(5,10b)", PORT_DUAD): 5})
        and not set(PORT_DUAD) & set(TRIANGLE),
    }


# ------------------------------------------------------------------ (g) couplings are root triangles

def couplings():
    rows = classify()
    roots = {tuple(r) for r, *_ in rows}
    info = {tuple(r): (k, tl) for r, k, cl, tl in rows}
    ten, fiveb = multiplets()
    sum_root = all((tuple(a + b) in roots) == (int(a @ b) == -100) for a in roots10() for b in roots10()
                   if not np.array_equal(a, b) and not np.array_equal(a, -b))
    down, up, top = Counter(), Counter(), 0
    for i in TRIANGLE:
        for d in itertools.combinations(TRIANGLE, 2):
            for a in ten[i]:
                for b in fiveb[d]:
                    g = tuple(-(a + b))
                    if g in roots:
                        down[(i, d, info[g][0], info[g][1][1])] += 1
        for j in TRIANGLE:
            for a in ten[i]:
                for b in ten[j]:
                    g = tuple(-(a + b))
                    if g in roots:
                        up[(i, j, info[g][0], info[g][1][1])] += 1
    for i in range(5):
        for a in ten[i]:
            for b in ten[i]:
                top += tuple(-(a + b)) in roots
    x, y, z = sp.symbols("x y z")
    Yu = sp.Matrix([[0, x, y], [x, 0, z], [y, z, 0]])                     # the up-type support on the triangle
    pairs = list(itertools.combinations(range(3), 2))
    rank_one = sp.solve([Yu.extract(list(r), list(c)).det() for r in pairs for c in pairs], [x, y, z], dict=True)
    opposite = {i: tuple(sorted(set(TRIANGLE) - {i})) for i in TRIANGLE}
    return {
        "for roots alpha != +-beta, alpha + beta is a root exactly when alpha.beta = -1, so a cubic coupling of three "
        "root fields, which comes from the bracket [E_alpha, E_beta] ~ E_(alpha + beta), needs alpha + beta + gamma = 0":
            sum_root,
        "on the triangle, 10_i 5b_jk reaches a 5b root (the down-type Higgs H_d) exactly when i is not in {j, k}, and "
        "always at the twin duad {3, 4}, 20 root triangles for each of the three pairs: the down-quark and charged-"
        "lepton pattern is the permutation from each vertex to its opposite edge": down == Counter(
            {(i, opposite[i], "(5b,10)", PORT_DUAD): 20 for i in TRIANGLE}),
        "10_i 10_j reaches a 5 root (the up-type Higgs H_u) exactly when i != j, at the twin weight -(mu_i + mu_j), "
        "30 root triangles for each ordered pair": up == Counter(
            {(i, j, "(5,10b)", tuple(sorted((i, j)))): 30 for i in TRIANGLE for j in TRIANGLE if i != j}),
        "no root triangle couples two 10's at one twin site, at any of the five: the GUT top coupling 10_3 10_3 5_H has "
        "no root realization, and a symmetric matrix on the up-type support (zero diagonal) has rank one only if it is "
        "0, so no up-type coupling matrix on these roots has rank one": top == 0 and rank_one == [{x: 0, y: 0, z: 0}],
    }


# ------------------------------------------------------------------ (h) the six-site port

def six_site_port():
    roots = {tuple(r) for r in roots10()}
    sites = [np.zeros(8, dtype=int)] + [10 * np.eye(8, dtype=int)[a] + 10 * np.eye(8, dtype=int)[5] for a in range(5)]
    V = {tuple(s) for s in sites}
    nbr = lambda s: {tuple(np.array(s) + np.array(r)) for r in roots}
    G0 = sp.Matrix(6, 6, lambda i, j: len((nbr(sites[i]) & nbr(sites[j])) - V))
    chain = counts.six_site_chain()
    ten, fiveb = multiplets()
    brackets = {tuple(a + b) for i in TRIANGLE for d in itertools.combinations(TRIANGLE, 2) if i not in d
                for a in ten[i] for b in fiveb[d] if tuple(a + b) in roots}
    return {
        "the port's memory variance M_2 - M_1^2 = X^T X, with X = (1 - P) Delta P, counts the bath points next to two "
        "sites: 240 - 5 = 235 on the diagonal and 56 - 4 = 52 off it, which is 183 I + 52 J (layer 22)":
            G0 == 183 * sp.eye(6) + 52 * sp.ones(6, 6) and all(chain.values()),
        "its eigenvalues 183 (five times) and 495 are positive, so X has no kernel: every visible state leaks into the "
        "bath at the first step, and the six channels cannot evolve on their own": G0.eigenvals() == {183: 5, 495: 1},
        "the brackets of the triangle's 10's with its 5b's are exactly the port's five roots e_a + e_5":
            brackets == {tuple(s) for s in sites[1:]},
    }


# ------------------------------------------------------------------ the table

def _fmt(x):
    return str(x) if isinstance(x, (int, Fraction)) else x


def _name(lab, prime=""):
    if lab[0] == "0":
        return "0"
    if lab[0] == "root":
        return f"root{prime} {lab[1][0]}-{lab[1][1]}"
    sign = "+" if lab[2] == 1 else "-"
    where = lab[1] if lab[0] == "site" else "".join(map(str, lab[1]))
    return f"{sign}{lab[0]}{prime} {where}"


def table_data():
    rows = table()
    gen = {}
    for g, i in enumerate(TRIANGLE):
        gen[("(10,5)", i)] = g + 1
        gen[("(5b,10)", tuple(sorted(set(TRIANGLE) - {i})))] = g + 1
    out = []
    for x in rows:
        k, cl, tl = x["class"], x["carrier"], x["twin"]
        twin = tl[1] if len(tl) > 1 else None
        role = None
        if (k, twin) in gen:
            role = f"generation {gen[(k, twin)]}"
        elif k == "(5b,10)" and twin == PORT_DUAD:
            role = "H_d"
        elif k == "(5,10b)" and twin == PORT_DUAD:
            role = "six-site port"
        out.append({
            "root_times_2": [int(v) // 5 for v in x["root"]],
            "class": k,
            "carrier": _name(cl), "twin": _name(tl, "'"),
            "particle": x["particle"],
            "T3": _fmt(x["T3"]), "hypercharge": _fmt(x["Y"]), "Q": _fmt(x["Q"]),
            "triangle_selection": role,
        })
    return {
        "about": "The 240 roots of E8 under A4 + A4' (layer 24, oes/assignment.py). The carrier's A4 is taken as SU(5) "
                 "with colour sites 0, 1, 2 and weak sites 3, 4, and the orientation (10,5) + (5b,10) is taken as "
                 "matter (SELECTED_REFERENCE; every choice is W(E8)-equivalent). 'triangle_selection' marks the three "
                 "generations on the twin triangle {0, 1, 2}, which is CONDITIONAL on the bracket rule. A '~' marks an "
                 "antiparticle. DYN_BIND stays NOT_INSTALLED.",
        "twin_sites_times_10": TWIN.tolist(),
        "hypercharge": [str(y) for y in Y[:5]], "T3": [str(t) for t in T3[:5]],
        "roots": out,
    }


def write_table(path=DATA):
    path.write_text(json.dumps(table_data(), indent=1) + "\n")


# ------------------------------------------------------------------ run

def run():
    rep = Report("24-assignment")
    T, SR, OB, CD, UF = gates.THEOREM, gates.SELECTED_REFERENCE, gates.OBSTRUCTION, gates.CONDITIONAL, gates.UNFORMED
    for name, ok in factors().items():
        rep.add(name, T, ok)
    for name, ok in moments().items():
        rep.add(name, T, ok)
    rep.add("the selection: the carrier's A4 as SU(5), colour sites 0, 1, 2 and weak sites 3, 4, and (10, 5) + (5b, 10) "
            "as matter; these three free choices are stated, DYN_BIND stays NOT_INSTALLED, and B1 still forbids any "
            "atom-diagonal charge on the carrier", SR, True)
    for name, ok in standard_model().items():
        rep.add(name, T, ok)
    for name, ok in choices().items():
        rep.add(name, T, ok)
    ch = chirality()
    for k, (name, ok) in enumerate(ch.items()):
        rep.add(name, OB if k in (1, 2) else T, ok)
    ge = generations()
    for name, ok in ge.items():
        rep.add(name, T, ok)
    rep.add("three generations rest on two inputs the roots do not supply, the orientation and the bracket rule; with "
            "them the count is 3 and the triangle is the one opposite the six-site port's duad. Layer 12's B6 is "
            "sharpened, not discharged", CD, all(ge.values()))
    cp = couplings()
    for k, (name, ok) in enumerate(cp.items()):
        rep.add(name, OB if k == 3 else T, ok)
    rep.add("the roots fix which couplings can be nonzero, not their sizes: no Yukawa block is formed, "
            "and masses and mixings stay with the canon's removed constants", UF, True)
    for name, ok in six_site_port().items():
        rep.add(name, T, ok)
    rep.add("data/e8_assignment.json is the table of all 240 roots", T,
            DATA.exists() and json.loads(DATA.read_text()) == table_data())
    return rep
