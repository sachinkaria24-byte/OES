"""Layer 23. All dots joined (28 Oct 2026, Drive check 22:08 UTC).

A dot is an object the model builds: a space with its operator, a lattice, a group, a circle, a port. A join is a map
between two dots, built here and checked against the property that makes it that kind of map (an intertwiner, a
homomorphism, an embedding, an isometry). An obstruction is a proof that a claimed map does not exist. Two dots that
share an integer are neither; those stay readings (layers 21 and 22).

The layer builds the whole diagram from layers 1-22 and checks that it is connected: from the K5 carrier every dot is
reached through checked maps. The new joins:

- The K5 incidences are root systems. The columns of the signed incidence B are a positive system of A4, and B with the
  signless M lists the twenty positive roots of D5. B B^T = 5I - J and B B^T + M M^T = 8I are the Coxeter identities
  sum alpha alpha^T = h P with h(A4) = 5 and h(D5) = 8. So M M^T = 3I + J, and the carrier's spectrum {0, 3, 8} is
  {0, h(D5) - h(A4), h(D5)}.
- The Petersen graph is the orthogonality graph of the ten roots e_i + e_j, and M^T M is their Gram matrix.
- The edge space is Lambda^2 R^5, and B is contraction with u = (1, ..., 1). The cycles are Lambda^2 of the sum-zero
  hyperplane H, the cuts are u ^ H, and a vertex permutation acts on the edges by its second compound. The rotor plane
  is spanned by the invariant area forms of the two rotation planes of the pentagon rotation on H.
- The native source lives on ker M + ker M. Its port W_AS takes the bivector a ^ b to an oriented cycle of K5 (rank 6,
  kernel 4: CLOSURE_46's split). A change of pair scales the bivector by its determinant, and the decomposable
  bivectors form a cone of dimension 7 = 10 - 3.
- The hexagon port of MOMENT_BIT, which is the canon's selected six-port, is the oriented triangle 0-1-2 of K5 lifted
  oddly to its A4 roots. Its Fourier transform is -8i sin(x/2) sin(y/2) sin(z/2) with x + y + z = 0, so it vanishes to
  third order. Its heat trace therefore decays as t^-7, with leading coefficient 1/(22394880000000 pi^4) for the
  normalized port: the canon's triangle-cycle heat, derived.
- The six-site port is K5 coned off: its sites are the origin and the lifted vertices e_i + e_5, and its fifteen bonds
  are the ten K5 edges and five spokes.
- L0 = A4 + A4' has index 5 in E8, with root cosets 40, 50, 50, 50, 50. The bath folded to E8 / L0 has spectrum
  0, 250^4 (the canon's L0 row). The tick's 25 fixed momenta carry the bath values 0 and 250 (24 times), and the five
  characters of E8 / L0 are among them.
- The circle, W(E8) and the carrier share one tick: k 144 -> c'^k sends 864 to g = r r', g acts on the carrier's
  coordinates as the vertex rotation, and the time coordinate 4x mod 5 gives the same rotation.
- The circle maps onto the atlas Z/36 with kernel <36>, the seam. Doubling contracts the atlas 36 -> 18 -> 9 onto a
  seam, a 2-cycle and a 6-cycle. The tick bit does not descend to the atlas: every address holds 96 residues that meet
  and 24 that miss. The golden companion has Pisano order 20 mod 5, 24 mod 36 and 720 mod 4320.
- The four-cube's 16 vertices are the basis states of four qubits, and its graph Laplacian is 4 - sum X_i in the Pauli
  algebra. Its 81-cell complex (the canon's h81) has Hodge spectrum 0, 2^8, 4^24, 6^32, 8^16 and a Hodge homotopy h
  with dh + hd = I - P0, h^2 = 0, rank 40 and norm 1/sqrt 2. Adjacent vertices have effective resistance 15/32
  (CLOSURE_46).
- Lambda^4 R^8 splits 35 + 35 under the Hodge star. A Weyl reflection swaps the halves, and the clocks keep them.

The 22:08 check read the sibling's notes of 21:40-22:08 (PRIMARY_SPLIT to JOIN_CLOSURE), the separate model's joined
model and its receipts, the canon's coordination release and the new collaboration hub. Their readings on the bit are
in layer 22; their structure is joined here, with four corrections.
"""

import functools
import itertools
from collections import Counter
from fractions import Fraction
from math import gcd

import numpy as np
import sympy as sp

from . import carrier, counts, gates, glue, ledger, native, spine
from .record import Report

N = spine.N
TICK = ledger.TICK
T, SR, OB, RP = gates.THEOREM, gates.SELECTED_REFERENCE, gates.OBSTRUCTION, gates.REPORTED


def _e(i, n=5):
    return sp.Matrix(n, 1, lambda r, _: int(r == i))


def _cols(X):
    return [tuple(X[:, k]) for k in range(X.cols)]


# ------------------------------------------------------------------ (a) K5 as roots

def k5_roots():
    """The signed incidence is a positive system of A4; with the signless one it is the positive roots of D5."""
    E = carrier.edges()
    B, M = sp.Matrix(carrier.signed_incidence()), sp.Matrix(carrier.signless_incidence())
    I5, J5 = sp.eye(5), sp.ones(5, 5)
    P = I5 - J5 / 5
    a4 = {tuple(_e(i) - _e(j)) for i in range(5) for j in range(5) if i != j}
    d5 = a4 | {tuple(s * (_e(i) + _e(j))) for i, j in E for s in (1, -1)}
    signed = lambda cols: {tuple(s * sp.Matrix(c)) for c in cols for s in (1, -1)}
    f = sp.Matrix([0, 1, 2, 3, 4])
    frame = lambda roots: functools.reduce(lambda a, b: a + b, [sp.Matrix(r) * sp.Matrix(r).T for r in roots])
    MMt = M * M.T
    return {
        "the ten columns of B (e_j - e_i, i < j) are a positive system of A4: with their negatives they are the 20 "
        "roots, and (0, 1, 2, 3, 4) is positive on each": signed(_cols(B)) == a4
        and all((f.T * sp.Matrix(c))[0] > 0 for c in _cols(B)),
        "B and M together list the twenty positive roots of D5 (+-e_i +- e_j)": signed(_cols(B) + _cols(M)) == d5
        and len(d5) == 40,
        "Coxeter numbers h = roots / rank: h(A4) = 20/4 = 5 and h(D5) = 40/5 = 8, with sum over all roots of "
        "alpha alpha^T = 2h P": Fraction(len(a4), 4) == 5 and Fraction(len(d5), 5) == 8 and frame(a4) == 10 * P
        and frame(d5) == 16 * I5,
        "so B B^T = h(A4) P = 5I - J and B B^T + M M^T = h(D5) I = 8I": B * B.T == 5 * P == 5 * I5 - J5
        and B * B.T + MMt == 8 * I5,
        "M M^T = h(D5) I - h(A4) P = 3I + J, with eigenvalues h(D5) - h(A4) = 3 (four times) and h(D5) = 8 (once); "
        "so spec D^2 = {0^5, 3^8, 8^2}": MMt == 8 * I5 - 5 * P == 3 * I5 + J5 and MMt.eigenvals() == {3: 4, 8: 1}
        and carrier.spectrum_multiplicities() == {0: 5, 3: 8, 8: 2},
        "ker M (the five zero modes) is the space of linear relations among the ten roots e_i + e_j":
            len(M.nullspace()) == 10 - M.rank() == 5,
    }


def petersen_roots():
    """The Petersen graph is the orthogonality graph of the ten roots e_i + e_j (or of the ten A4 roots of B)."""
    E = carrier.edges()
    B, M = sp.Matrix(carrier.signed_incidence()), sp.Matrix(carrier.signless_incidence())
    A = carrier.petersen()
    Gp, Gm = M.T * M, B.T * B
    orth = lambda G: sp.Matrix(10, 10, lambda a, b: int(a != b and G[a, b] == 0))
    touch = lambda G: sp.Matrix(10, 10, lambda a, b: int(a != b and abs(G[a, b]) == 1))
    return {
        "M^T M is the Gram matrix of the roots e_i + e_j: 2 on the diagonal, 1 for edges that share a vertex, 0 for "
        "disjoint edges": all(Gp[a, b] == (2 if a == b else len(set(E[a]) & set(E[b]))) for a in range(10)
                              for b in range(10)),
        "the Petersen graph is their orthogonality graph, and that of the A4 roots in B: A = J + I - M^T M":
            orth(Gp) == A == orth(Gm) and A == sp.ones(10, 10) + sp.eye(10) - Gp,
        "the line graph is |<alpha_e, alpha_f>| = 1, and M^T M - 2I": touch(Gp) == touch(Gm) == Gp - 2 * sp.eye(10),
    }


def compound2(P):
    """The second compound of a 5 x 5 matrix on the basis e_i ^ e_j (i < j): the K5 edge basis."""
    E = carrier.edges()
    return sp.Matrix(10, 10, lambda a, b: P.extract(list(E[a]), list(E[b])).det())


def exterior():
    """The edge space is Lambda^2 R^5: B is contraction with u, the cycles are Lambda^2 H and the cuts u ^ H."""
    E = carrier.edges()
    B = sp.Matrix(carrier.signed_incidence())
    u = sp.ones(5, 1)
    wedge = lambda a, b: sp.Matrix([a[i] * b[j] - a[j] * b[i] for i, j in E])
    contract = lambda a, b: (u.T * a)[0] * b - (u.T * b)[0] * a
    rng = np.random.default_rng(23)
    pairs = [(sp.Matrix(rng.integers(-5, 6, 5)), sp.Matrix(rng.integers(-5, 6, 5))) for _ in range(4)]
    H = [_e(i) - _e(4) for i in range(4)]
    L2H = sp.Matrix.hstack(*[wedge(H[i], H[j]) for i, j in itertools.combinations(range(4), 2)])
    cuts = sp.Matrix.hstack(*[wedge(u, h) for h in H])
    perm = lambda f: sp.Matrix(5, 5, lambda a, b: int(a == f(b)))
    maps = [lambda i: (i + 1) % 5, lambda i: 2 * i % 5, lambda i: (3 - i) % 5, lambda i: (-i) % 5]
    # the rotation of H by 72 and 144 degrees: the invariant area form of each rotation plane
    R5 = np.roll(np.eye(5), 1, axis=0)
    vals, vecs = np.linalg.eig(R5)
    forms = []
    for k in (1, 2):
        z = vecs[:, np.argmin(abs(vals - np.exp(2j * np.pi * k / 5)))]
        v, w = z.real, z.imag
        forms.append(np.array([v[i] * w[j] - v[j] * w[i] for i, j in E]))
    plane = np.array([counts._oriented_cycle(1), counts._oriented_cycle(2)], dtype=float)[:, :, 0].T
    C2 = np.array(compound2(perm(maps[0])), dtype=float)
    fixed = lambda w: np.allclose(C2 @ w, w)
    in_plane = lambda w: np.allclose(plane @ np.linalg.lstsq(plane, w, rcond=None)[0], w)
    return {
        "B applied to the coordinates of a ^ b is the contraction (u.a) b - (u.b) a: B is contraction with u":
            all(B * wedge(a, b) == contract(a, b) for a, b in pairs),
        "the cycles ker B are Lambda^2 H (dimension 6) and the cuts, the image of B^T, are u ^ H (dimension 4), "
        "orthogonal to them": (B * L2H).is_zero_matrix and L2H.rank() == 6 and cuts.rank() == 4
        and (L2H.T * cuts).is_zero_matrix and sp.Matrix.hstack(cuts, B.T).rank() == 4,
        "a vertex permutation acts on the oriented edges by its second compound, and commutes with B": all(
            counts._edge_action(f) == compound2(perm(f)) and B * compound2(perm(f)) == perm(f) * B for f in maps),
        "the rotor plane is spanned by the invariant area forms of the rotation planes of the pentagon rotation "
        "(72 and 144 degrees) on H": all(fixed(w) and in_plane(w) for w in forms)
        and np.linalg.matrix_rank(np.array(forms)) == 2,
    }


def source_port():
    """The native source lives on ker M + ker M, and its port takes the bivector a ^ b to an oriented K5 cycle."""
    P, Q = native.p5_basis(), native.l6_basis()
    W, pairs = native.commutator_map()
    M = np.array(carrier.signless_incidence(), float)
    B = np.array(carrier.signed_incidence(), float)
    rng = np.random.default_rng(46)
    a, b = rng.standard_normal(5), rng.standard_normal(5)
    T2 = np.array([[2.0, 1.0], [1.0, 3.0]])
    a2, b2 = np.array([a, b]).T @ T2[:, 0], np.array([a, b]).T @ T2[:, 1]
    wedge = lambda x, y: native.wedge(x, y, pairs)
    jac = np.array([np.concatenate([[y[j] if k == i else (-y[i] if k == j else 0) for k in range(5)],
                                    [-x[j] if k == i else (x[i] if k == j else 0) for k in range(5)]])
                    for (i, j) in pairs for x, y in [(a, b)]])
    cyc = Q @ (W @ wedge(a, b))
    Aa, Ab = native.source_matrix(P @ a), native.source_matrix(P @ b)
    return {
        "the source coordinates q = (a, b) live on ker M + ker M (an orthonormal basis of the five zero modes)":
            np.allclose(M @ P, 0) and np.allclose(P.T @ P, np.eye(5)),
        "the port W_AS: Lambda^2 ker M -> cycles has rank 6 and kernel 4 (CLOSURE_46's split of the exterior square)":
            W.shape == (6, 10) and np.linalg.matrix_rank(W) == 6,
        "W_AS(a ^ b) is the oriented K5 cycle [A(a), A(b)], in ker B": np.allclose(B @ cyc, 0)
        and np.allclose(cyc, native.oriented(Aa @ Ab - Ab @ Aa)),
        "a change of pair by T scales the bivector by det T": np.allclose(wedge(a2, b2), np.linalg.det(T2) * wedge(a, b)),
        "the decomposable bivectors a ^ b form a cone of dimension 7 = 10 - 3 (the pair has 10 coordinates, SL(2) has 3)":
            np.linalg.matrix_rank(jac) == 7,
    }


# --------------------------------------------------------- (b) the ports on the lattice

def _matching_sum(vecs):
    """Sum over perfect matchings of the product of inner products (the Gaussian moment, Isserlis)."""
    if not vecs:
        return 1
    first, rest = vecs[0], vecs[1:]
    return sum(int(first @ rest[i]) * _matching_sum(rest[:i] + rest[i + 1:]) for i in range(len(rest)))


def triangle_port():
    """The alternating hexagon (MOMENT_BIT, the canon's six-port) is the oriented triangle 0-1-2 of K5."""
    e2 = 2 * np.eye(8, dtype=np.int64)
    tri = [(0, 1), (1, 2), (2, 0)]
    alpha2 = [e2[a] - e2[b] for a, b in tri]                     # doubled coordinates
    pts, signs = alpha2 + [-x for x in alpha2], [1, 1, 1, -1, -1, -1]
    a1, a2 = e2[0] - e2[1], e2[1] - e2[2]
    hexagon, hsigns = [a1, a1 + a2, a2, -a1, -a1 - a2, -a2], [1, -1, 1, -1, 1, -1]
    as_dict = lambda P, S: {tuple(p.tolist()): s for p, s in zip(P, S)}
    B = sp.Matrix(carrier.signed_incidence())
    E = carrier.edges()
    cycle = sp.zeros(10, 1)
    for a, b in tri:
        cycle[E.index((min(a, b), max(a, b)))] += 1 if a < b else -1
    k = sp.Matrix(sp.symbols("k0:8"))
    dot = lambda x: (k.T * sp.Matrix(x.tolist()))[0] / 2
    mom = [sp.expand(sum(s * dot(x) ** n for x, s in zip(pts, signs))) for n in range(4)]
    x, y, z = [dot(al) for al in alpha2]
    rng = np.random.default_rng(7)
    ks = rng.standard_normal((6, 8))
    phat = lambda q: sum(s * np.exp(0.5j * (q @ p)) for p, s in zip(pts, signs))
    closed = lambda q: -8j * np.prod([np.sin(0.25 * (q @ al)) for al in alpha2])
    R2 = counts._roots2()
    real = [al // 2 for al in alpha2]
    m = _matching_sum([v for v in real for _ in range(2)])
    lead = sp.Integer(m) * sp.pi ** 4 / ((2 * sp.pi) ** 8 * 30 ** 4 * 60 ** 3)
    moments = counts.lattice_moments(pts, signs, 4)
    return {
        "the alternating hexagon of layer 22 is the oriented triangle 0 -> 1 -> 2 -> 0 of K5, each A4 root of it with +1 "
        "and its reverse with -1": as_dict(pts, signs) == as_dict(hexagon, hsigns),
        "the triangle is a cycle of K5, so the port has charge 0 and dipole 0; it is odd": (B * cycle).is_zero_matrix
        and mom[0] == 0 and mom[1] == 0 and mom[2] == 0,
        "its Fourier transform is -8i sin(x/2) sin(y/2) sin(z/2), x + y + z = 0 for x = k . alpha, so its lowest "
        "moment is the cubic sum s (k.p)^3 = 6xyz": all(np.isclose(phat(q), closed(q)) for q in ks)
        and sp.expand(x + y + z) == 0 and sp.expand(mom[3] - 6 * x * y * z) == 0,
        "its moments are MOMENT_BIT's 1, 242, 58691, 14259954, 3470101592 (per unit norm)": [v // 6 for v in moments]
        == [1, 242, 58691, 14259954, 3470101592],
        "the frame sum rho rho^T = 60 I gives eps(k) = 30 |k|^2 + O(|k|^4), and E[(xyz)^2] = 12 sigma^6 (Isserlis)":
            np.array_equal(R2.T @ R2, 240 * np.eye(8, dtype=np.int64)) and m == 12,
        "so <p, e^{-t Delta} p> / |p|^2 = t^-7 / (22394880000000 pi^4) (1 + O(1/t)): the canon's triangle-cycle heat, "
        "with exponent (8 + 2 x 3) / 2 = 7": sp.simplify(lead / 6 - 1 / (22394880000000 * sp.pi ** 4)) == 0
        and (8 + 2 * 3) // 2 == 7,
    }


def cone():
    """The six-site port is K5 coned off: the origin and the five lifted vertices e_i + e_5."""
    e2 = 2 * np.eye(8, dtype=np.int64)
    sites = [0 * e2[0]] + [e2[i] + e2[5] for i in range(5)]
    roots = {tuple(r.tolist()) for r in counts._roots2()}
    a4 = {tuple((e2[i] - e2[j]).tolist()) for i in range(5) for j in range(5) if i != j}
    bonds = [(a, b) for a, b in itertools.combinations(range(6), 2)]
    diff = lambda a, b: tuple((sites[a] - sites[b]).tolist())
    return {
        "all fifteen differences of the six sites are E8 roots (an A5 simplex)": all(diff(a, b) in roots for a, b in bonds),
        "the ten bonds between lifted vertices are the A4 roots e_i - e_j, the ten K5 edges": {diff(a, b) for a, b in bonds
                                                                                              if a and b} <= a4
        and len([1 for a, b in bonds if a and b]) == 10,
        "the five bonds to the origin are the spokes e_i + e_5": all(diff(a, 0) == tuple((e2[a - 1] + e2[5]).tolist())
                                                                     for a in range(1, 6)),
        "these are the sites of layer 22's six-site chain (241 I - J, 183 I + 52 J, 35366 I + 8134 J)":
            all(counts.six_site_chain().values()),
    }


# ------------------------------------------------------ (c) A4 + A4' and the fixed momenta

def glue_cosets():
    """L0 = A4 + A4' has index 5 in E8; root cosets 40/50/50/50/50; the folded bath 0, 250^4."""
    out, atoms, pairs, _ = glue.decompose()
    per = Counter({0: out["A4"] + out["A4'"]})
    for (k1, _), n in pairs.items():
        per[k1] += n
    n = [per[c] for c in range(5)]
    F = sp.Matrix(5, 5, lambda a, b: (240 if a == b else 0) - n[(b - a) % 5])
    _, A, Ap = glue.a4_pair()
    lattice_index = round(np.sqrt(abs(np.linalg.det(np.vstack([glue.simple_system(A), glue.simple_system(Ap)])
                                                    @ np.vstack([glue.simple_system(A), glue.simple_system(Ap)]).T))))
    return {
        "L0 = A4 + A4' has index 5 in E8 (Gram determinant 25 = 5^2)": lattice_index == 5,
        "the 240 roots fall into the five cosets of L0 as 40, 50, 50, 50, 50": n == [40, 50, 50, 50, 50],
        "the glue pairs the classes by x -> +-2x": all(k2 == 2 * k1 % 5 for (k1, k2) in pairs)
        or all(k2 == -2 * k1 % 5 for (k1, k2) in pairs),
        "the bath folded to E8 / L0 = Z/5 is 240 - sum n_c S_c, with spectrum 0 and 250 (four times)":
            F.eigenvals() == {0: 1, 250: 4},
    }


def tick_momenta():
    """The 25 fixed momenta of the tick g = r r' carry the bath values 0 and 250; E8 / L0 is five of them."""
    _, _, _, _, g, _ = spine.spine_clock()
    G = spine.to_standard(g)
    R = glue.roots()
    _, A, Ap = glue.a4_pair()
    L0 = np.vstack([A, Ap])
    simple = np.array([0.5 * np.array([1, -1, -1, -1, -1, -1, -1, 1]), np.eye(8)[0] + np.eye(8)[1]]
                      + [np.eye(8)[k + 1] - np.eye(8)[k] for k in range(6)])
    Minv = np.linalg.inv(G - np.eye(8))
    pts = {}
    for c in itertools.product(range(5), repeat=8):
        x = Minv @ (np.array(c) @ simple)                      # k / 2 pi, fixed by g mod Lambda
        key = tuple(np.round((np.linalg.solve(simple.T, x) % 1.0) * 5).astype(int) % 5)
        pts.setdefault(key, x)
        if len(pts) == 25:
            break
    integral = lambda c: np.allclose(c, np.round(c), atol=1e-6)
    eps = Counter(int(round(240 - np.cos(2 * np.pi * R @ x).sum())) for x in pts.values())
    dual = [x for x in pts.values() if integral(L0 @ x)]
    eps_dual = Counter(int(round(240 - np.cos(2 * np.pi * R @ x).sum())) for x in dual)
    return {
        "|det(g - I)| = 25 fixed momenta of the tick, each fixed mod 2 pi Lambda": round(abs(np.linalg.det(G - np.eye(8))))
        == 25 and len(pts) == 25 and all(integral(np.linalg.solve(simple.T, G @ x - x)) for x in pts.values()),
        "the bath is 0 at one of them and 250 at the other 24": eps == {0: 1, 250: 24},
        "five of them are the characters of E8 / L0, with the folded values 0, 250^4": len(dual) == 5
        and eps_dual == {0: 1, 250: 4},
    }


# ------------------------------------------------------------ (d) the clocks and the circle

def clock_joins():
    """The circle, W(E8) and the carrier share one tick."""
    _, cp, r, _, g, _ = spine.spine_clock()
    S = spine.to_standard
    Rm, G = S(r), S(g)
    iota = np.vstack([np.eye(5), np.zeros((3, 5))])
    R5 = np.roll(np.eye(5), 1, axis=0)
    H = np.eye(5) - 1 / 5
    D2 = sp.Matrix(carrier.D2())
    E = carrier.edges()

    def carrier_perm(f):
        P = sp.zeros(15, 15)
        for i in range(5):
            P[f(i), i] = 1
        for k, (i, j) in enumerate(E):
            P[5 + E.index(tuple(sorted((f(i), f(j))))), 5 + k] = 1
        return P
    affine = [lambda i, a=a, b=b: (a * i + b) % 5 for a in (1, 2, 3, 4) for b in range(5)]
    _, labels = ledger.day_coxeter_group()
    return {
        "r acts on the carrier's five coordinates as the vertex rotation i -> i + 1 and fixes the other three":
            np.allclose(Rm @ iota, iota @ R5) and np.allclose(Rm[5:, 5:], np.eye(3)),
        "the tick g = c'^6 = r r' agrees with r on the carrier's A4 (the sum-zero part)": np.allclose(G @ iota @ H, iota @ R5 @ H),
        "k 144 -> c'^k is an isomorphism <144> -> <c'> of order 30, and it sends the tick 864 to g": spine.order(144) == 30
        and spine.mat_order(cp) == 30 and np.array_equal(spine.mpow(cp, 6), g) and TICK == 6 * 144,
        "the time coordinate kappa(x) = 4x mod 5 sends the tick to 1: the same rotation of the vertices": 4 * TICK % 5 == 1,
        "the day-Coxeter group acts on its five day clocks as AGL(1,5): the tick rotates, the day doubles":
            labels["tick"] == {x: (x + 1) % 5 for x in range(5)} and labels["day"] == {x: 2 * x % 5 for x in range(5)},
        "all twenty affine maps i -> a i + b of the vertices commute with D^2 on the 15 atoms": all(
            carrier_perm(f) * D2 == D2 * carrier_perm(f) for f in affine),
    }


def primary_split():
    """PRIMARY_SPLIT and DOUBLING_PARTS: the circle is the product of a 2-clock, a 27-clock and the time clock."""
    e2, e27, e5 = 3105, 2080, 3456
    part = lambda x, e: x * e % N
    order_mod = lambda m: next(k for k in range(1, 100) if pow(2, k, m) == 1)
    kill = lambda x: next(k for k in range(1, 10) if (2 ** k * part(x, e2)) % N == 0)
    return {
        "3105 + 2080 + 3456 = 1, each idempotent, pairwise products 0": (e2 + e27 + e5) % N == 1
        and all(e * e % N == e for e in (e2, e27, e5)) and all(a * b % N == 0 for a, b in
                                                              itertools.combinations((e2, e27, e5), 2)),
        "every residue is the sum of its three parts": all((part(x, e2) + part(x, e27) + part(x, e5)) % N == x
                                                           for x in range(N)),
        "the pure clocks are <135> (order 32), <160> (order 27, the nakshatra) and <864> (order 5)":
            spine.subgroup(135) == {x for x in range(N) if part(x, e27) == part(x, e5) == 0}
            and spine.subgroup(160) == {x for x in range(N) if part(x, e2) == part(x, e5) == 0}
            and spine.subgroup(TICK) == {x for x in range(N) if part(x, e2) == part(x, e27) == 0},
        "the observer clock <1080> is the order-4 subgroup of the 2-clock; the sun 1440 is pure 27-part; 1728 is pure time":
            spine.subgroup(1080) <= spine.subgroup(135) and part(1440, e27) == 1440 and part(1728, e5) == 1728,
        "the tithi is 2160 + 1440 + 864 and the mass step is 1080 + 3456": (2160 + 1440 + 864) % N == 144
        and (1080 + 3456) % N == 216 and (part(144, e2), part(144, e27), part(144, e5)) == (2160, 1440, 864)
        and (part(216, e2), part(216, e27), part(216, e5)) == (1080, 0, 3456),
        "doubling: nilpotent on the 2-part (the generator dies at the fifth doubling), order 4 on the time clock, "
        "order 18 on the 27-clock (the ninth doubling is -1); after 36 = lcm(4, 18) the odd parts return": kill(135) == 5
        and order_mod(5) == 4 and order_mod(27) == 18 and pow(2, 9, 27) == 26 and sp.ilcm(4, 18) == 36
        and all(part(2 ** 36 * x, e27) == part(x, e27) and part(2 ** 36 * x, e5) == part(x, e5) for x in range(0, N, 7)),
    }


def atlas():
    """The atlas is the quotient circle -> Z/36 (address x mod 36), with kernel the seam <36>."""
    addr = lambda x: x % 36
    dbl = lambda a: 2 * a % 36
    images = [set(range(36))]
    for _ in range(4):
        images.append({dbl(a) for a in images[-1]})
    nine = images[2]
    orbit = lambda a: [a] + list(itertools.takewhile(lambda b: b != a, (functools.reduce(lambda x, _: dbl(x), range(k), a)
                                                                        for k in range(1, 10))))
    steps_to = lambda a, target: next(k for k in range(0, 10) if functools.reduce(lambda x, _: dbl(x), range(k), a) in target)
    seam = {x for x in range(N) if addr(x) == 0}
    per_address = [Counter(x % 5 == 0 for x in range(a, N, 36)) for a in range(36)]
    return {
        "x -> x mod 36 is a homomorphism of the circle onto Z/36 with kernel the seam <36> (order 120)":
            seam == spine.subgroup(36) and len(seam) == 120
            and all(addr(x + y) == (addr(x) + addr(y)) % 36 for x, y in [(4000, 999), (2160, 2161), (864, 3456)]),
        "the tick, the yuga blocks, the golden step, the sun, the observer point and the half-turn are on the seam":
            all(addr(x) == 0 for x in (864, 432, 1296, 1728, 216, 1440, 1080, 2160, 72)),
        "the addresses of 901, 801, 106, 108, 12402, 160, 135, 256, 224, 120, 325, 105625 are 1, 9, 34, 0, 18, 16, 27, 4, "
        "8, 12, 1, 1, and 5184 = 144 x 36": [addr(x) for x in (901, 801, 106, 108, 12402, 160, 135, 256, 224, 120, 325,
                                                                 105625)] == [1, 9, 34, 0, 18, 16, 27, 4, 8, 12, 1, 1]
        and 5184 == 144 * 36,
        "doubling contracts the atlas 36 -> 18 -> 9 -> 9: the multiples of 4, a seam, a 2-cycle {12, 24} and a 6-cycle "
        "4 -> 8 -> 16 -> 32 -> 28 -> 20": [len(s) for s in images] == [36, 18, 9, 9, 9] and nine == set(range(0, 36, 4))
        and sorted(orbit(12)) == [12, 24] and orbit(4) == [4, 8, 16, 32, 28, 20],
        "address 18 reaches the seam in one contraction, 9 and 27 in two; 1 enters the cycle at 4 and 34 at 32":
            steps_to(18, {0}) == 1 and steps_to(9, {0}) == 2 and steps_to(27, {0}) == 2
            and dbl(dbl(1)) == 4 and dbl(34) == 32 and 16 in orbit(4),
        "the tick bit does not descend to the atlas: every address holds 96 residues that meet and 24 that miss":
            all(c == Counter({False: 96, True: 24}) for c in per_address),
    }


def pisano():
    """The golden companion B = [[1, 1], [1, 0]] on the circle's rings."""
    B = np.array([[1, 1], [1, 0]], dtype=object)

    def order(m):
        P, k = B % m, 1
        while not (P == np.eye(2, dtype=object)).all():
            P, k = (P @ B) % m, k + 1
        return k
    orders = {m: order(m) for m in (5, 27, 32, 36, 4320)}
    return {
        "B has order 20 mod 5 (the order of the golden step 216), 24 mod 36, 48 mod 32, 72 mod 27 and 720 mod 4320":
            orders == {5: 20, 27: 72, 32: 48, 36: 24, 4320: 720} and spine.order(216) == 20,
        "reduction mod 36 sends B (order 720) to B (order 24), and 24 atlas steps are one tick": 720 % 24 == 0
        and 24 * 36 == TICK,
    }


def air_801():
    """AIR_801's matrix [[108, 801], [106, 901]]."""
    A = sp.Matrix([[108, 801], [106, 901]])
    A5 = A.applyfunc(lambda x: x % 5)
    power = lambda k: (A5 ** k).applyfunc(lambda x: x % 5)
    order = next(k for k in range(1, 481) if power(k) == sp.eye(2))
    proj = next(k for k in range(1, 481) if power(k)[0, 1] == power(k)[1, 0] == 0 and power(k)[0, 0] == power(k)[1, 1])
    t = sp.symbols("t")
    poly = (t ** 3 - 1) * (1 + t ** 6 + t ** 12 + t ** 18 + t ** 24)
    return {
        "det = 12402; mod 5 it is [[3, 1], [1, 1]] with determinant 2": A.det() == 12402
        and A5 == sp.Matrix([[3, 1], [1, 1]]) and A5.det() % 5 == 2,
        "its order in GL(2,5) is 24 and in PGL(2,5) 6 (its characteristic polynomial is irreducible mod 5: a Singer cycle)":
            order == 24 and proj == 6 and sp.Poly(t ** 2 - 4 * t + 2, t, modulus=5).is_irreducible,
        "(t^3 - 1)(1 + t^6 + ... + t^24) has degree 27 and a simple root at 1": sp.degree(poly, t) == 27
        and poly.subs(t, 1) == 0 and sp.diff(poly, t).subs(t, 1) != 0,
    }


# ------------------------------------------------------------- (e) the four-cube, Hodge 70

def _cube_complex(n=4):
    cells = list(itertools.product((0, 1, 2), repeat=n))       # 2 marks the interval
    index = {c: k for k, c in enumerate(cells)}
    d = np.zeros((len(cells), len(cells)), dtype=np.int64)
    for c in cells:
        free = [p for p in range(n) if c[p] == 2]
        for j, p in enumerate(free):
            for end, sign in ((1, 1), (0, -1)):
                f = list(c)
                f[p] = end
                d[index[tuple(f)], index[c]] += (-1) ** j * sign
    return cells, d


def four_cube():
    """The 81-cell complex of the four-cube (h81), its Hodge homotopy, and its vertices as four qubits."""
    cells, d = _cube_complex()
    dims = Counter(c.count(2) for c in cells)
    Lap = d @ d.T + d.T @ d
    vals = Counter(np.rint(np.linalg.eigvalsh(Lap.astype(float))).astype(int).tolist())
    w, V = np.linalg.eigh(Lap.astype(float))
    # Delta^+ from the eigenvectors (the eigenvalues are 0, 2, 4, 6, 8); numpy 2.5.3's pinv returns this 81 x 81
    # pseudo-inverse with an error near 1e-2 here, while the eigh form is exact to 1e-14
    Lp = (V[:, w > 0.5] / w[w > 0.5]) @ V[:, w > 0.5].T
    h = d.T @ Lp
    P0 = np.eye(81) - Lap @ Lp
    I81 = np.eye(81)
    verts = [k for k, c in enumerate(cells) if 2 not in c]
    edges = [k for k, c in enumerate(cells) if c.count(2) == 1]
    d1 = d[np.ix_(verts, edges)]
    L = d1 @ d1.T
    X, one = np.array([[0, 1], [1, 0]]), np.eye(2, dtype=np.int64)
    qubit = lambda i: functools.reduce(np.kron, [X if k == i else one for k in range(4)])
    order = [sum(cells[v][k] << (3 - k) for k in range(4)) for v in verts]
    Lq = np.zeros((16, 16), dtype=np.int64)
    Lq[np.ix_(order, order)] = L
    Ls = sp.Matrix(L.tolist())
    Lplus = (Ls + sp.ones(16, 16) / 16).inv() - sp.ones(16, 16) / 16
    s, t = verts.index(cells.index((0, 0, 0, 0))), verts.index(cells.index((1, 0, 0, 0)))
    b = sp.Matrix([int(k == s) - int(k == t) for k in range(16)])
    R = (b.T * Lplus * b)[0]
    return {
        "the four-cube complex has 16, 32, 24, 8, 1 cells (81 in all) and d^2 = 0": [dims[k] for k in range(5)]
        == [16, 32, 24, 8, 1] and not np.any(d @ d),
        "its Hodge Laplacian has spectrum 0, 2^8, 4^24, 6^32, 8^16 (layer 21's count, now on the complex)":
            vals == {0: 1, 2: 8, 4: 24, 6: 32, 8: 16},
        "the Hodge homotopy h = d^T Delta^+ has dh + hd = I - P0, h^2 = 0, rank 40 and norm 1/sqrt 2 (the canon's h81)":
            np.allclose(d @ h + h @ d, I81 - P0) and np.allclose(h @ h, 0) and np.linalg.matrix_rank(h) == 40
            and np.isclose(np.linalg.norm(h, 2), 1 / np.sqrt(2)),
        "its 16 vertices are the basis states of four qubits: the graph Laplacian is 4 - sum X_i, in the Pauli algebra":
            np.array_equal(Lq, 4 * np.eye(16, dtype=np.int64) - sum(qubit(i) for i in range(4))),
        "adjacent vertices have effective resistance 15/32, between |b|^2 / 8 = 1/4 and |b|^2 / 2 = 1 (CLOSURE_46)":
            R == sp.Rational(15, 32) and sp.Rational(1, 4) < R < 1,
    }


def hodge70():
    """Lambda^4 R^8 = 35 + 35 under the Hodge star; reflections swap the halves, the clocks keep them."""
    quads = list(itertools.combinations(range(8), 4))
    idx = {q: k for k, q in enumerate(quads)}

    def sign(p):
        s, p = 1, list(p)
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                if p[i] > p[j]:
                    s = -s
        return s
    star = np.zeros((70, 70))
    for q in quads:
        c = tuple(k for k in range(8) if k not in q)
        star[idx[c], idx[q]] = sign(q + c)
    comp = lambda S: np.array([[np.linalg.det(S[np.ix_(a, b)]) for b in quads] for a in quads])
    refl = np.eye(8)
    refl[[0, 1]] = refl[[1, 0]]                                  # the reflection in e_0 - e_1
    _, cp, r, _, g, _ = spine.spine_clock()
    d, (_, v) = spine.day_clock(), ledger.golden_clock()
    clocks = [spine.to_standard(x) for x in (cp, r, g, d, v)]
    vals = Counter(np.rint(np.linalg.eigvalsh(star)).astype(int).tolist())
    return {
        "the Hodge star on Lambda^4 R^8 is an involution with 35 + 35 eigenvalues +1 and -1":
            np.allclose(star @ star, np.eye(70)) and np.allclose(star, star.T) and vals == {1: 35, -1: 35},
        "a Weyl reflection anticommutes with it and swaps the halves": np.allclose(comp(refl) @ star, -star @ comp(refl)),
        "the Coxeter clock, the carrier rotation, the tick, the day and the golden clock have determinant 1 and keep "
        "the halves": all(np.isclose(np.linalg.det(C), 1) and np.allclose(comp(C) @ star, star @ comp(C)) for C in clocks),
    }


# ------------------------------------------------------------------- the 22:08 notes

def notes_2208():
    """The arithmetic of the 21:40-22:08 notes, and the four corrections."""
    q = lambda a: a % 36
    return {
        "PRIMARY_SPLIT and DOUBLING_PARTS: 3105 + 2080 + 3456 = 8641 = 2 x 4320 + 1; 2160 + 1440 + 864 = 4464 = 4320 + 144; "
        "1080 + 3456 = 4536 = 4320 + 216; 4 x 3456 = 13824 = 3 x 4320 + 864; 2^5 = 32; 2^9 = 512 = 19 x 27 - 1":
            3105 + 2080 + 3456 == 2 * N + 1 and 2160 + 1440 + 864 == N + 144 and 1080 + 3456 == N + 216
            and 4 * 3456 == 3 * N + TICK and 2 ** 9 == 19 * 27 - 1,
        "AIR_801 and ATLAS_801: 108 x 901 - 801 x 106 = 12402 = 344 x 36 + 18; 901 = 25 x 36 + 1; 801 = 22 x 36 + 9; "
        "4 x 6 + 2 x 3 + 1 = 31; 6 x 36 = 216; 24 x 36 = 864; 5 + 7 + 4 + 5 + 5 + 5 + 5 = 36":
            108 * 901 - 801 * 106 == 12402 == 344 * 36 + 18 and 901 == 25 * 36 + 1 and 801 == 22 * 36 + 9
            and 4 * 6 + 2 * 3 + 1 == 31 and 6 * 36 == 216 and 24 * 36 == TICK and 5 + 7 + 4 + 5 * 4 == 36,
        "GOLDEN_ATLAS and ATLAS_CYCLE: 216 = 6 x 36; 2 + 4 + 6 + 8 = 20; 20 x 216 = 4320; 432 = 12 x 36; of 0..35, 28 "
        "integers are prime to 5 and 8 are multiples": 216 == 6 * 36 and 2 + 4 + 6 + 8 == 20 and 20 * 216 == N
        and 432 == 12 * 36 and sum(1 for a in range(36) if a % 5) == 28,
        "CLOSURE_46 and JOIN_CLOSURE: C(5, 2) = 10 = 6 + 4 = 7 + 3; 72^2 = 5184, 325^2 = 105625; 1 + 120 + 135 = 256; "
        "256 - 224 = 32; 5184 = 6 x 864": sp.binomial(5, 2) == 10 == 6 + 4 == 7 + 3 and 72 ** 2 == 5184
        and 325 ** 2 == 105625 and 1 + 120 + 135 == 256 and 256 - 224 == 32 and 5184 == 6 * TICK,
        "GOLDEN_ATLAS, ATLAS_801 and ATLAS_CYCLE corrected: an address does not meet or miss the tick (1 and 145 share "
        "address 1, and 1 meets while 145 misses); the 28 and 8 count the integers 0..35": q(1) == q(145)
        and ledger.contains_tick(1) and not ledger.contains_tick(145),
        "GOLDEN_ATLAS and ATLAS_CYCLE corrected: address 18 reaches the seam in one contraction, not two": q(2 * 18) == 0,
        "GOLDEN_ATLAS corrected: address 16 does move under contraction (16 -> 32 -> 28 -> 20 -> 4 -> 8 -> 16); it "
        "stays among the nine": q(2 * 16) == 32 and 16 % 4 == 0,
        "ATLAS_801 corrected: 36 atlas steps, 36 x 36 = 1296, meet the tick; the count that misses is the atlas order 120":
            ledger.contains_tick(36 * 36) and not ledger.contains_tick(120),
    }


# ------------------------------------------------------------------- the diagram

DOTS = {
    "V": ("K5 vertices", "R^5, the five atoms", "1"),
    "E": ("K5 edges", "Lambda^2 R^5, the ten atoms", "1, 23"),
    "carrier": ("carrier", "R^15 with D^2 = M M^T + M^T M, spectrum 0^5 3^8 8^2", "1"),
    "kerM": ("zero modes", "ker M, the five dark modes", "1, 5"),
    "cycles": ("cycles", "ker B = Lambda^2 H, six", "22, 23"),
    "rotor": ("rotor plane", "the C5-fixed plane of the cycles", "22, 23"),
    "petersen": ("Petersen", "the graph on the ten edges", "1, 22"),
    "datum": ("datum", "(psi0, v0) with energy 34", "1, 22"),
    "source": ("source", "q'' + 4q = 0 on ker M + ker M", "4"),
    "A4": ("A4", "the 20 roots e_i - e_j", "11"),
    "D5": ("D5", "the 40 roots +-e_i +- e_j", "23"),
    "E8": ("E8", "the lattice and its 240 roots", "3, 11"),
    "L0": ("A4 + A4'", "index 5 in E8", "11, 23"),
    "bath": ("bath", "Delta = 240 - sum of root translations", "8, 22"),
    "momenta": ("tick momenta", "the 25 fixed momenta of the tick", "23"),
    "halfper": ("half-periods", "Lambda / 2 Lambda, 256", "22"),
    "pauli": ("Pauli algebra", "M16(R) with L", "22"),
    "gksl": ("GKSL", "the semigroup e^-tL", "22"),
    "triangle": ("triangle port", "the oriented triangle 0-1-2 on the lattice", "22, 23"),
    "sixsite": ("six-site port", "K5 coned off, an A5 simplex", "4, 22, 23"),
    "moments": ("moments", "the Stieltjes data of the ports", "22"),
    "clocks": ("W(E8) clocks", "c', g = r r', d, v, m", "19, 21"),
    "G120": ("day-Coxeter group", "<c', d>, order 120", "21, 22"),
    "AGL": ("AGL(1,5)", "the affine group of the pentagon", "21"),
    "circle": ("circle", "Z/4320", "19"),
    "time": ("time clock", "<864> = Z/5", "21, 22"),
    "observer": ("observer clock", "<1080>, inside the 2-clock <135>", "22, 23"),
    "c27": ("27-clock", "<160>, the nakshatra", "20, 23"),
    "atlas": ("atlas", "Z/36 = circle / <36>", "23"),
    "golden": ("golden companion", "B = [[1, 1], [1, 0]]", "21, 22"),
    "stages": ("stages", "the fifteen indices", "22"),
    "cube": ("four-cube", "the 81-cell complex of [0, 1]^4", "21, 23"),
    "hodge": ("Hodge 70", "Lambda^4 R^8 = 35 + 35", "23"),
}

# (from, to, short label, the map, status, check)
JOINS = [
    ("E", "A4", "B", "the signed incidence: its columns are a positive system of A4", T, "k5_roots"),
    ("E", "D5", "B and M", "the two incidences: the twenty positive roots of D5", T, "k5_roots"),
    ("A4", "D5", "inclusion", "A4 is the sub-root-system e_i - e_j of D5", T, "k5_roots"),
    ("D5", "carrier", "Coxeter numbers", "M M^T = h(D5) I - h(A4) P: spec D^2 = {0, h(D5) - h(A4), h(D5)} = {0, 3, 8}", T,
     "k5_roots"),
    ("E", "V", "contraction", "B is contraction with u = (1, 1, 1, 1, 1) on Lambda^2 R^5", T, "exterior"),
    ("E", "kerM", "relations", "ker M is the space of relations among the roots e_i + e_j", T, "k5_roots"),
    ("E", "petersen", "orthogonality", "Petersen is the orthogonality graph of the roots e_i + e_j", T, "petersen_roots"),
    ("petersen", "carrier", "projectors", "the Petersen projectors are the carrier's edge projectors", T,
     "counts.petersen_projectors"),
    ("E", "cycles", "Lambda^2 H", "ker B = Lambda^2 of the sum-zero hyperplane; cuts u ^ H", T, "exterior"),
    ("cycles", "rotor", "area forms", "the C5-fixed plane, spanned by the invariant area forms", T, "exterior"),
    ("rotor", "E8", "Gram 10I", "the rotor pair of near and far roots, turned by a Weyl doubling", T,
     "counts.rotor_plane"),
    ("kerM", "datum", "v0", "the datum's velocity is the alternating 4-cycle in ker M", T, "counts.tick_tock"),
    ("datum", "carrier", "Legendre", "H = 1/2 |v|^2 + 1/2 psi D^2 psi = 34, the zero modes holding 2", T,
     "counts.tick_tock"),
    ("kerM", "source", "q = (a, b)", "the native source lives on ker M + ker M", T, "source_port"),
    ("source", "cycles", "W_AS", "a ^ b -> [A(a), A(b)], an oriented K5 cycle (rank 6, kernel 4)", T, "source_port"),
    ("source", "carrier", "no mode", "4 is not in spec D^2: the source is not a carrier mode", OB, "field"),
    ("source", "sixsite", "port", "the port metric and the boundary rotation of the native action", SR, "native_port"),
    ("A4", "E8", "embedding", "the first five coordinates: A4 and D5 roots are E8 roots", T, "embed"),
    ("D5", "E8", "embedding", "the first five coordinates", T, "embed"),
    ("A4", "L0", "A4 + A4'", "index 5, root cosets 40, 50, 50, 50, 50, glue x -> +-2x", T, "glue_cosets"),
    ("L0", "bath", "folding", "the bath on E8 / L0 = Z/5: 0, 250^4", T, "glue_cosets"),
    ("clocks", "momenta", "fixed points", "the 25 fixed momenta of the tick g", T, "tick_momenta"),
    ("momenta", "bath", "values", "the bath is 0 once and 250 at the other 24", T, "tick_momenta"),
    ("E8", "bath", "Delta", "240 - sum of the 240 root translations; frame 60 I", T, "triangle_port"),
    ("E8", "halfper", "mod 2", "Lambda -> Lambda / 2 Lambda; 120 root classes", T, "counts.folded_bath"),
    ("halfper", "pauli", "phi", "the Walsh-Hadamard conjugate of the folded bath is L in the Pauli basis", T,
     "counts.pauli_quotient"),
    ("pauli", "gksl", "GKSL", "-L(X) = 2 sum (A X A^T - X) over the 120 antisymmetric Paulis", T, "counts.pauli_quotient"),
    ("cycles", "triangle", "odd lift", "the triangle 0-1-2 lifted to its A4 roots", T, "triangle_port"),
    ("triangle", "moments", "Delta^n", "MOMENT_BIT's moments; heat t^-7 / (22394880000000 pi^4)", T, "triangle_port"),
    ("V", "sixsite", "cone", "the origin and the lifted vertices e_i + e_5: K5 coned off", T, "cone"),
    ("sixsite", "moments", "blocks", "241 I - J, 183 I + 52 J, 35366 I + 8134 J", T, "cone"),
    ("V", "clocks", "r", "r acts on the carrier's coordinates as the vertex rotation; g = r r' on A4", T, "clock_joins"),
    ("circle", "clocks", "k 144 -> c'^k", "the Coxeter subgroup <144> onto <c'>, 864 -> g", SR, "clock_joins"),
    ("circle", "time", "idempotent 3456", "the time part of the primary split", T, "primary_split"),
    ("circle", "observer", "idempotent 3105", "the 2-part; the observer clock is its order-4 subgroup", T, "primary_split"),
    ("circle", "c27", "idempotent 2080", "the 27-part, generated by the nakshatra 160", T, "primary_split"),
    ("time", "V", "kappa = 4x mod 5", "translation by 864 intertwined with the vertex rotor", T, "counts.two_clocks"),
    ("clocks", "G120", "<c', d>", "the day-Coxeter group, order 120, derived group the tick", T, "clock_joins"),
    ("G120", "circle", "24 maps", "every homomorphism to the circle kills the commutator", T, "counts.circle_maps"),
    ("G120", "AGL", "day clocks", "G / centre on the five day clocks: the tick rotates, the day doubles", T,
     "clock_joins"),
    ("AGL", "carrier", "i -> a i + b", "the twenty affine maps of the vertices commute with D^2", T, "clock_joins"),
    ("circle", "atlas", "x mod 36", "onto Z/36 with kernel the seam <36>; doubling contracts it", T, "atlas"),
    ("golden", "circle", "B^k -> 216 k", "order 20 mod 5, the order of the golden step; 720 mod 4320", SR, "pisano"),
    ("golden", "atlas", "mod 36", "order 24, the tick in atlas steps", T, "pisano"),
    ("stages", "circle", "k -> k", "the fifteen indices as steps, with first landings", T, "counts.check_claims"),
    ("cube", "pauli", "4 - sum X_i", "the four-cube's vertices are four qubits", T, "four_cube"),
    ("clocks", "hodge", "Lambda^4", "reflections swap the 35 + 35 halves, the clocks keep them", T, "hodge70"),
]

# rows for docs/LEDGER.md: (join, the statement, the unified statement, status, layer)
LEDGER_ROWS = [
    ("the K5 incidences", "B B^T = 5I - J; signless + ordinary = 8I", "the Coxeter identities of A4 and D5: the carrier's spectrum {0, 3, 8} is {0, h(D5) - h(A4), h(D5)}", T, "23"),
    ("Petersen as roots", "A = J + I - M^T M", "the orthogonality graph of the ten roots e_i + e_j, whose Gram matrix is M^T M", T, "23"),
    ("the selected six-port (canon)", "moments 1, 242, 58691, 14259954; triangle-cycle heat t^-7 with 1/(22394880000000 pi^4)", "the oriented triangle 0-1-2 of K5 lifted to the lattice; its Fourier transform -8i sin(x/2) sin(y/2) sin(z/2) vanishes to third order, which gives the exponent and the coefficient", T, "23"),
    ("L0 (canon)", "A4 + A4' of index 5; root cosets 40/50/50/50/50; folded spectrum 0, 250^4", "replayed; the tick's 25 fixed momenta carry 0 and 250 (24 times), and E8 / L0 is five of them", T, "11, 23"),
    ("h81 (canon)", "chain counts 16/32/24/8/1; spectrum 0, 2^8, 4^24, 6^32, 8^16; dh + hd = I - P0, h^2 = 0, rank 40, norm 1/sqrt 2", "replayed on the 81-cell complex; its vertices are four qubits with Laplacian 4 - sum X_i; adjacent resistance 15/32", T, "21, 23"),
    ("Hodge 70 (canon)", "35 + 35 halves interchanged by a Weyl reflection", "replayed; the clocks of determinant 1 keep the halves", T, "23"),
    ("primary split (PRIMARY_SPLIT, DOUBLING_PARTS)", "3105 + 2080 + 3456 = 1; doubling kills the 2-part and returns the time and 27 parts after 4 and 18", "replayed; 36 = lcm(4, 18) returns the odd parts, and no doubling count returns all three", T, "20, 23"),
    ("the atlas (GOLDEN_ATLAS, ATLAS_801, ATLAS_CYCLE)", "addresses meet or miss the tick; 18 falls to the seam in two contractions; 16 does not move", "the atlas is the quotient Z/36, and the bit does not descend to it (96 meets and 24 misses at every address); 18 falls in one contraction; 16 is on the 6-cycle", T, "23"),
    ("the 801 matrix (AIR_801)", "order 24 in GL(2,5), projective order 6", "replayed: a Singer cycle mod 5", T, "23"),
    ("the bivector (CLOSURE_46)", "a change of pair scales a ^ b by its determinant; a cone of dimension 7; rank 6, kernel 4", "the native port W_AS: Lambda^2 ker M -> cycles of K5, rank 6 and kernel 4; the cone has dimension 7 = 10 - 3", T, "4, 23"),
    ("all dots", "-", "33 dots and 47 joins in one connected diagram (docs/DOTS.md)", T, "23"),
    ("separate model's joined model (22:02)", "158 check groups, 80 matrices, 63 typed relationships", "recorded, not rerun", RP, "23"),
]

NOT_JOINED = [
    ("separate model's joined model (22:02)", "158 check groups, 12 review groups, 80 matrices, 63 typed relationships; "
                                              "sha256 b0c17731...", RP),
    ("canon SMEAR (184 / 481)", "a rank-6 port T and a rank-4 projector P with minor -512 alpha^4 / 25; the operands are "
                                "not stored here", RP),
    ("source-to-cube bridge", "rank 10 with an exact left decoder (canon); not stored here", RP),
    ("AIR_801's 31 points", "the orbit list 6 + 6 + 6 + 6 + 3 + 3 + 1 needs a permutation of 31 points; none is stored", RP),
    ("air", "no air operator is stored, and none is formed", gates.UNFORMED),
]


def _checks():
    field = lambda: {"4 is not in spec D^2 = {0, 3, 8}": 4 not in carrier.spectrum_multiplicities()}
    embed = lambda: {
        "the A4 and D5 roots, put in the first five coordinates, are E8 roots": all(
            tuple(np.r_[np.array(rt, dtype=float), np.zeros(3)].tolist()) in {tuple(r) for r in glue.roots().tolist()}
            for rt in {tuple(s * (_e(i) + t * _e(j))) for i, j in carrier.edges() for s in (1, -1) for t in (1, -1)})}
    native_port = lambda: {
        "the boundary rotation fixes x0 and has order 5, and the port metric W_p commutes with it":
            np.allclose(np.linalg.matrix_power(native.boundary_rotation(), 5), np.eye(6))
            and native.boundary_rotation()[0, 0] == 1
            and np.allclose(native.boundary_rotation() @ native.port_metric(), native.port_metric() @ native.boundary_rotation())}
    claims = lambda: {"every reading holds and the stages land as stored": (lambda r: not r[0] and r[1])(counts.check_claims())}
    return {
        "k5_roots": k5_roots, "petersen_roots": petersen_roots, "exterior": exterior, "source_port": source_port,
        "triangle_port": triangle_port, "cone": cone, "glue_cosets": glue_cosets, "tick_momenta": tick_momenta,
        "clock_joins": clock_joins, "primary_split": primary_split, "atlas": atlas, "pisano": pisano,
        "four_cube": four_cube, "hodge70": hodge70, "field": field, "embed": embed, "native_port": native_port,
        "counts.petersen_projectors": counts.petersen_projectors, "counts.rotor_plane": counts.rotor_plane,
        "counts.tick_tock": counts.tick_tock, "counts.folded_bath": counts.folded_bath,
        "counts.pauli_quotient": counts.pauli_quotient, "counts.two_clocks": counts.two_clocks,
        "counts.circle_maps": counts.circle_maps, "counts.check_claims": claims,
    }


def components(passed):
    """Connected components of the dots under the joins that hold (maps, not obstructions)."""
    parent = {k: k for k in DOTS}

    def find(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k
    for (a, b, _, _, status, _), ok in zip(JOINS, passed):
        if ok and status in (T, SR):
            parent[find(a)] = find(b)
    groups = {}
    for k in DOTS:
        groups.setdefault(find(k), []).append(k)
    return list(groups.values())


def dots_page():
    lines = ["# All dots joined", "",
             "Every object the model builds is a dot, and every map between two dots that layer 23 (`oes/dots.py`) "
             "builds and checks is a join. A dashed arrow is an obstruction: a proof that the map does not exist. Two "
             "dots that share an integer are not joined by it; those integers stay readings (`docs/LEDGER.md`). "
             "Generated by `dots_page()`; `tests/test_model.py` checks that this file is current.", "",
             "```mermaid", "flowchart LR"]
    for key, (name, _, _) in DOTS.items():
        lines.append(f'    {key}["{name}"]')
    for a, b, short, _, status, _ in JOINS:
        arrow = "-.->" if status == OB else "-->"
        lines.append(f'    {a} {arrow}|"{short}"| {b}')
    lines += ["```", "", f"{len(DOTS)} dots and {len(JOINS)} joins. With the obstruction left out, the joins that "
              "hold connect every dot: the diagram is one piece.", "",
              "## Dots", "", "| dot | what it is | layers |", "|---|---|---|"]
    cell = lambda x: x.replace("|", "\\|")
    for key, (name, what, layers) in DOTS.items():
        lines.append(f"| {cell(name)} | {cell(what)} | {layers} |")
    lines += ["", "## Joins", "", "| from | to | the map | status | check |", "|---|---|---|---|---|"]
    for a, b, _, what, status, check in JOINS:
        lines.append(f"| {cell(DOTS[a][0])} | {cell(DOTS[b][0])} | {cell(what)} | {status} | `{check}` |")
    lines += ["", "## Not joined", "", "| object | why | status |", "|---|---|---|"]
    for name, why, status in NOT_JOINED:
        lines.append(f"| {cell(name)} | {cell(why)} | {status} |")
    lines += ["", "AUTH = NOT_PASS. ScientificGold = FALSE. No term is added to the action.", ""]
    return "\n".join(lines)


def run():
    rep = Report("23-dots")
    checks = _checks()
    results = {key: fn() for key, fn in checks.items()}
    held = {key: all(bool(v) for v in res.values()) for key, res in results.items()}
    passed = [held[ck] for *_, ck in JOINS]
    for (a, b, _, what, status, ck), ok in zip(JOINS, passed):
        rep.add(f"{DOTS[a][0]} -> {DOTS[b][0]}: {what}", status, ok, results[ck] if ck in results else None)
    comps = components(passed)
    rep.add(f"the {len(DOTS)} dots and {len(JOINS)} joins form one connected diagram (the obstruction left out)", T,
            len(comps) == 1, [sorted(c) for c in comps])
    a8 = air_801()
    rep.add("AIR_801's matrix [[108, 801], [106, 901]]: det 12402; mod 5 a Singer cycle of order 24 in GL(2,5) and 6 in "
            "PGL(2,5); the clock polynomial has degree 27 and a simple root at 1", T, all(a8.values()), a8)
    n8 = notes_2208()
    rep.add("the 22:08 notes: the primary split, the doubling parts, the 801 matrix, the atlas, the bivector and the "
            "joined ledger as arithmetic, and four corrections (an address does not carry the tick bit; address 18 "
            "falls in one contraction; address 16 cycles; 36 atlas steps meet)", T, all(n8.values()), n8)
    rep.add("Drive check 22:08: the sibling's notes PRIMARY_SPLIT, DOUBLING_PARTS, AIR_801, ATLAS_801, GOLDEN_ATLAS, "
            "ATLAS_CYCLE, CLOSURE_46, JOINED_RECEIPT and JOIN_CLOSURE (21:40-22:08) and its paper one-machine-20261028-"
            "unify (21:43, seventeen checks); the separate model's update overlay (21:46), joined model (22:02) and "
            "checkpoint (22:04); the canon's coordination release OES_COORD_20261029 (one new sheet in each workbook, "
            "every prior cell kept, no gate changed) and the collaboration hub with its open tasks", RP, True)
    for name, why, status in NOT_JOINED:
        rep.add(f"not joined: {name}: {why}", status, True)
    return rep
