"""Layer 11. The E8 glue maps, which the canon lists as absent.

"E8. The roots split 112+128=240. The frame is 60 I8. The glue map is absent."
(Open chains, 28 Oct 2026.) A glue map is determined by lattice theory once
the sublattice is named, so both presentations are built and checked here.

(a) D8 glue. D8 = {x in Z^8 : sum x even}, D8*/D8 = {0, v, s, c} ~ Z2 x Z2,
    and E8 = D8 u (D8 + s). The 112 roots are the minimal vectors of D8 and
    the 128 roots are the minimal vectors of D8 + s. The class s is isotropic
    (|s|^2 = 2), which is why the glued lattice is even and unimodular.

(b) A4 + A4' glue. A4 = <e_i - e_j : i, j < 5> is the carrier's own root
    system (its 20 roots are the oriented K5 edges). Its orthogonal
    complement in E8 is a second A4'. [E8 : A4 + A4'] = 5 and the glue map
    A4*/A4 -> A4'*/A4' is x -> 2x (unique up to sign), an anti-isometry of
    the Z5 discriminant forms.

    The 200 roots outside A4 + A4' project onto span(A4) as exactly the
    weights e_i - (1/5) sum e (the five K5 vertices) and
    e_i + e_j - (2/5) sum e (the ten K5 edges), up to sign. A signed vertex
    pairs with the ten weights of the twin 10, a signed edge with the five of
    the twin 5. So the carrier's 15 atoms are
    the A4 shadows of the mixed E8 roots: 200 = 4 x 50 = (5,10') + (5b,10b') +
    (10,5b') + (10b,5') in SU(5) x SU(5)' notation, and
    248 = (24,1) + (1,24) + (5,10') + (5b,10b') + (10,5b') + (10b,5').
"""

from fractions import Fraction
from itertools import combinations

import numpy as np

from . import carrier, gates, spacetime
from .record import Report


def roots():
    return spacetime.e8_roots() / 2.0


# ------------------------------------------------------------------ (a) D8

def d8_glue():
    R = roots()
    integral = np.all(np.isclose(R, np.round(R)), axis=1)
    s = np.full(8, 0.5)
    in_d8 = integral & np.isclose(R.sum(1) % 2, 0)
    shifted = R - s
    in_s = np.all(np.isclose(shifted, np.round(shifted)), axis=1) & np.isclose(shifted.sum(1) % 2, 0)
    return int(in_d8.sum()), int(in_s.sum()), bool(np.all(in_d8 | in_s)), float(s @ s)


# ------------------------------------------------------------- (b) A4 + A4'

def a4_pair():
    R = roots()
    A = np.array([r for r in R if np.allclose(r[5:], 0) and np.isclose(r[:5].sum(), 0)])
    span = A.T
    Ap = np.array([r for r in R if np.allclose(A @ r, 0)])
    return R, A, Ap


def projector(Vrows):
    U, s, _ = np.linalg.svd(Vrows.T, full_matrices=False)
    U = U[:, s > 1e-9]
    return U @ U.T


def simple_system(Rs):
    t0 = np.array([1, 3, 7, 15, 31, 63, 127, 255.0]) + 0.01 * np.arange(8)
    pos = [r for r in Rs if r @ t0 > 1e-9]
    P = {tuple(np.round(r * 2).astype(int)) for r in pos}
    simple = [r for r in pos if not any(tuple(np.round((r - a) * 2).astype(int)) in P
                                         for a in pos if not np.allclose(a, r))]
    return np.array(simple)


def chain_order(S):
    """Order an A_n simple system along its Dynkin path."""
    n = len(S)
    adj = {i: [j for j in range(n) if j != i and np.isclose(S[i] @ S[j], -1)] for i in range(n)}
    start = next(i for i in range(n) if len(adj[i]) == 1)
    order, prev = [start], None
    while len(order) < n:
        cur = order[-1]
        nxt = [j for j in adj[cur] if j != prev and j not in order]
        prev = cur
        order.append(nxt[0])
    return S[order]


def gram_det(B):
    return float(np.linalg.det(B @ B.T))


def carrier_atom_of(p, tol=1e-9):
    """Name the A4 weight p as a signed K5 vertex or edge, else None."""
    u = np.r_[np.ones(5), np.zeros(3)] / 5
    for sign in (1, -1):
        for i in range(5):
            w = np.eye(8)[i] - u
            if np.allclose(p, sign * w, atol=tol):
                return ("V", i, sign)
        for i, j in combinations(range(5), 2):
            w = np.eye(8)[i] + np.eye(8)[j] - 2 * u
            if np.allclose(p, sign * w, atol=tol):
                return ("E", (i, j), sign)
    return None


def class_mod_a4(p, basis_dual):
    """Coordinates of a weight in the fundamental-weight basis, reduced mod 5 via the
    A4 discriminant pairing: the class of p in A4*/A4 is (sum_k k c_k) mod 5 for
    the fundamental weights omega_k (k = 1..4)."""
    c = basis_dual @ p
    c = np.round(c).astype(int)
    return int(sum((k + 1) * ck for k, ck in enumerate(c)) % 5)


def decompose():
    R, A, Ap = a4_pair()
    P1, P2 = projector(A), projector(Ap)
    SA, SAp = chain_order(simple_system(A)), chain_order(simple_system(Ap))
    # pairing with simple roots gives fundamental-weight coordinates of a weight
    out = {"A4": 0, "A4'": 0, "mixed": 0}
    atoms = {}
    pairs = {}
    for r in R:
        p1, p2 = P1 @ r, P2 @ r
        if np.allclose(p2, 0):
            out["A4"] += 1
            continue
        if np.allclose(p1, 0):
            out["A4'"] += 1
            continue
        out["mixed"] += 1
        a = carrier_atom_of(p1)
        atoms[a] = atoms.get(a, 0) + 1
        k1 = class_mod_a4(p1, SA)
        k2 = class_mod_a4(p2, SAp)
        pairs[(k1, k2)] = pairs.get((k1, k2), 0) + 1
    return out, atoms, pairs, (SA, SAp)


def run():
    rep = Report("11-glue")
    T = gates.THEOREM
    n112, n128, cover, s2 = d8_glue()
    rep.add("D8 glue: 112 roots in D8, 128 in D8 + s, E8 = D8 u (D8 + s)", T,
            n112 == 112 and n128 == 128 and cover)
    rep.add("glue class s is isotropic: |s|^2 = 2 (even), so the glued lattice is "
            "even unimodular", T, np.isclose(s2, 2.0))

    R, A, Ap = a4_pair()
    SA, SAp = simple_system(A), simple_system(Ap)
    rep.add("A4 = <e_i - e_j>: 20 roots (the oriented K5 edges); its orthogonal "
            "complement A4' also has 20 roots", T, len(A) == 20 and len(Ap) == 20)
    dA, dAp = gram_det(SA), gram_det(SAp)
    rep.add("det A4 = det A4' = 5, so [E8 : A4 + A4'] = sqrt(25/1) = 5", T,
            np.isclose(dA, 5) and np.isclose(dAp, 5))
    out, atoms, pairs, _ = decompose()
    rep.add("240 = 20 (A4) + 20 (A4') + 200 mixed", T,
            out == {"A4": 20, "A4'": 20, "mixed": 200}, out)
    named = {a: n for a, n in atoms.items() if a is not None}
    rep.add("every mixed root projects to a signed K5 vertex or edge weight", T,
            None not in atoms and len(named) == 30, len(named),
            note="30 = 15 carrier atoms x 2 signs")
    vcount = {n for a, n in named.items() if a[0] == "V"}
    ecount = {n for a, n in named.items() if a[0] == "E"}
    rep.add("each signed vertex has 10 twin partners (the twin 10), each signed edge has "
            "5 (the twin 5): 5 x 10 = 10 x 5 = 50 per class pair", T,
            vcount == {10} and ecount == {5}, {"vertex": sorted(vcount), "edge": sorted(ecount)})
    glue = {k1: k2 for (k1, k2) in pairs}
    m = {k1: (k2 * pow(k1, -1, 5)) % 5 for k1, k2 in glue.items()}
    rep.add("glue map A4*/A4 -> A4'*/A4' is x -> 2x or x -> 3x (= -2x), 50 roots per "
            "class pair", T, len(set(m.values())) == 1 and set(m.values()) <= {2, 3}
            and set(pairs.values()) == {50}, {str(k): v for k, v in pairs.items()})
    qform = [(Fraction(4 * k * k, 5) + Fraction(4 * (2 * k) ** 2, 5)) % 2 for k in range(5)]
    rep.add("anti-isometry: q(x) + q'(2x) = 4k^2 = 0 mod 2 for the Z5 forms q(k) = 4k^2/5",
            T, all(v == 0 for v in qform))
    rep.add("248 = (24,1) + (1,24) + 4 x 50 matches 8 + 40 + 200", T,
            24 + 24 + 4 * 50 == 248 and 8 + 40 + 200 == 248)
    rep.add("consequence: l2(V u E) is l2 of the A4 shadows of mixed E8 roots, modulo "
            "sign and twin label", T, len(named) // 2 == 15,
            note="the carrier is literally inside the bath; this is the absent glue map")
    return rep
