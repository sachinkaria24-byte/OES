"""Layer 9. Joining the dots: the maps that make the layers one object.

A join here is an identity between matrices built in different layers. It
holds exactly, or it holds with an intertwining map in the middle. Shared
integers with no map between their parent objects are listed separately, as
the canon requires ("equal ranks are not the same maps").

The joins:

J1  E8 realisation. For each of five weights nu_a, the ten vectors
    r_(ij),a = mu_ij + nu_a are E8 roots with R_a^T R_a = M^T M and
    ker R_a = P5. Each layer with A4 closes to a D5, and their union has 120
    roots. The carrier edge gram is an E8 root gram.
J2  Petersen. M^T M = I + J - A_Pet. The carrier edge spectrum {0^5, 3^4, 8} is
    the Petersen spectrum {1^5, (-2)^4, 3} under lam = 1 - theta (+10 on the
    uniform line). P5 = the Petersen eigenvalue-1 space = ker of the del Pezzo
    line-intersection matrix J - M^T M.
J3  Port metric. W_p = 2 L(C5) (+) 0 + (2/5)(J5 (+) 1). Its moving eigenvalues
    are 2 (phi + 2) and 2 (3 - phi), where (5 +- sqrt5)/2 are the C5 Laplacian
    eigenvalues: the golden petals.
J4  Clique. Gram(x1..x5) = I + J, so M M^T = Gram + 2I. The carrier vertex
    gram is the bath clique gram shifted by 2.
J5  Surface. The 1-skeleton of the RP^2 triangulation is K6. Under coning
    ({i,6} <-> vertex i, {i,j} <-> edge ij), D is exactly the star/non-star
    block of the line-graph adjacency of K6. The carrier's 15 atoms are the
    15 edges of the surface.
J6  Dark sector = source. The hidden controllable sector of (edge force, D psi)
    is P5 (+) P5 in (position, velocity). The native source q = (a, b) lives on
    P5 (+) P5.
J7  Index. The Witten index is -5 = -(dim ker M - dim ker M^T) = -dim P5.
J8  One C5 through every layer: vertex rotation -> edge tick -> cycle rotor ->
    W_AS -> adapter T -> boundary rotation -> coordinate cycle e2..e6 in W(E8).
    The full nonlinear native vector field is equivariant.
J9  Quartic maximisers. The sharp 40/9 is attained on decomposable visible
    wedges, Gr(2,5) n P(visible) of projective dimension 2: the degree-5 del
    Pezzo surface, whose line matrix is J2's.
J10 Traces to gravity. Tr D^0, D^2, D^4 = 15, 40, 200 become heat coefficients
    60, 160 m^2, 400 m^4 (layer 6). This is the only route from the carrier to
    G and Lambda_cc, and it is CONDITIONAL.
"""

from itertools import combinations, product

import numpy as np

from . import carrier, gates, native, observer, spacetime
from .record import Report

PHI = (1 + 5 ** 0.5) / 2

SHARED_INTEGERS = [
    ("15", "dim H = |V|+|E|; edges of K6; duads/synthemes of 6; Hodge-Dirac rank+...",
     "J5 is the only map among these"),
    ("60", "E8 frame 60 I; |A5|; Dirac trace coefficient", "no map"),
    ("240", "E8 roots; 6 x 40 = 6 Tr D^2; corner diagonal", "no map"),
    ("20", "five-port visible coords; observable dims of D psi; Tr M^T M", "no map"),
    ("125", "det cycle Gram; 5^3 clock memory states", "no map"),
    ("120", "|S5|; clock quotient dim; D5 union roots", "no map"),
    ("9", "gravity 2+7; E8 clique size; ancestry 5+1+2+1", "no map"),
    ("36", "atlas addresses; 6^2; 2 x 18 Hodge parity", "no map"),
    ("4320, 108, 69120", "yuga, japa, Human Design counts", "integers only (canon)"),
]


def e8_layers():
    E = carrier.edges()
    mu = {e: np.r_[[(1.0 if k in e else 0.0) - 0.4 for k in range(5)], [0, 0, 0]] for e in E}
    nus = [np.r_[[0.4] * 5, [0, 0, 0]]]
    nus += [np.r_[[-0.1] * 5, np.array(s) / 2] for s in product((1, -1), repeat=3)
            if np.prod(s) == -1]
    return [np.array([mu[e] + nu for e in E]).T for nu in nus]


def _keys(V):
    return {tuple(np.round(2 * v).astype(int)) for v in V}


def coordinate_cycle(pts):
    """sigma: e_{c} -> e_{c+1} for c = 1..5 cyclically (0-based coordinates)."""
    Q = pts.copy()
    Q[:, [2, 3, 4, 5, 1]] = pts[:, [1, 2, 3, 4, 5]]
    return Q


def run():
    rep = Report("9-joins")
    T = gates.THEOREM
    M = np.array(carrier.signless_incidence(), float)
    P5 = native.p5_basis()
    roots = _keys(spacetime.e8_roots() / 2.0)

    # J1
    layers = e8_layers()
    ok = all(_keys(R.T) <= roots and np.allclose(R.T @ R, M.T @ M)
             and np.linalg.matrix_rank(R) == 5 and np.allclose(R @ P5, 0) for R in layers)
    rep.add("J1 r_(ij),a = mu_ij + nu_a are E8 roots; R_a^T R_a = M^T M; ker R_a = P5",
            T, ok)
    common = [np.eye(8)[i] - np.eye(8)[j] for i in range(5) for j in range(5) if i != j]
    union, closed = set(), True
    for R in layers:
        S = list(R.T) + [-x for x in R.T] + common
        K = _keys(S)
        union |= K
        closed &= len(K) == 40 and all(
            tuple(np.round(2 * (b - (a @ b) * a)).astype(int)) in K for a in S for b in S)
    rep.add("J1 each layer + A4 is a reflection-closed 40-root D5; union has 120 roots",
            T, closed and len(union) == 120, len(union))

    # J2
    A = np.array(carrier.petersen(), float)
    I10, J10 = np.eye(10), np.ones((10, 10))
    rep.add("J2 M^T M = I + J - A_Petersen (carrier edge potential = Petersen complement)",
            T, np.allclose(M.T @ M, I10 + J10 - A))
    rep.add("J2 P5 = Petersen eigenvalue-1 space = ker of del Pezzo lines J - M^T M", T,
            np.allclose(A @ P5, P5) and np.allclose((J10 - M.T @ M) @ P5, 0))

    # J3
    W = native.port_metric()
    S5 = native.boundary_rotation()[1:, 1:]
    L = 2 * np.eye(5) - S5 - S5.T
    X = np.zeros((6, 6))
    X[1:, 1:] = 2 * L + 0.4 * np.ones((5, 5))
    X[0, 0] = 0.4
    ev = np.sort(np.linalg.eigvalsh(L))
    rep.add("J3 W_p = 2 L(C5) + (2/5)(J5 + 1); L(C5) eigen 0, 3-phi (x2), phi+2 (x2)", T,
            np.allclose(W, X) and np.allclose(ev, [0, 3 - PHI, 3 - PHI, PHI + 2, PHI + 2]))

    # J4
    Xc = spacetime.clique_sites()[1:] / 2.0
    Gc = Xc @ Xc.T
    rep.add("J4 Gram(x1..x5) = I + J and M M^T = Gram + 2I", T,
            np.allclose(Gc, np.eye(5) + np.ones((5, 5)))
            and np.allclose(M @ M.T, Gc + 2 * np.eye(5)))

    # J5
    tri, _ = spacetime.rp2_triangulations()
    skel = {p for f in tri for p in combinations(f, 2)}
    atoms = [(i, 5) for i in range(5)] + carrier.edges()
    LG = np.array([[1.0 if a != b and set(a) & set(b) else 0.0 for b in atoms] for a in atoms])
    blk = np.zeros((15, 15))
    blk[:5, :5] = np.ones((5, 5)) - np.eye(5)
    blk[5:, 5:] = M.T @ M - 2 * I10
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    rep.add("J5 RP^2 1-skeleton is K6, and D = A_L(K6) - diag(J-I, M^T M - 2I)", T,
            len(skel) == 15 and np.allclose(D, LG - blk))

    # J6
    Asys = observer.system_matrix()
    Bedge = np.vstack([np.zeros((15, 10)), np.eye(15)[:, 5:]])
    Kc = observer.kalman_ctrl(Asys, Bedge)
    ker = observer.null_space(observer.kalman_obs(Asys, observer.readouts()["Dirac image D psi"]))
    # hidden = intersection; build it and compare with P5 (+) P5 on edge atoms
    Pk = Kc @ Kc.T
    Pn = ker @ ker.T
    w, V = np.linalg.eigh(Pk @ Pn @ Pk)
    Hd = V[:, w > 1 - 1e-8]
    target = np.zeros((30, 10))
    target[5:15, :5] = P5
    target[20:30, 5:] = P5
    same = (Hd.shape[1] == 10 and observer.rank(np.hstack([Hd, target])) == 10)
    rep.add("J6 hidden sector (edge force | D psi) = P5 (+) P5 = native source space", T,
            same, Hd.shape[1])

    # J7
    g = np.diag(np.array(carrier.grading(), float))
    wD, VD = np.linalg.eigh(D @ D)
    kerD2 = VD[:, np.abs(wD) < 1e-9]
    index = float(((kerD2 ** 2) * g[:, None]).sum())
    rep.add("J7 Witten index = Tr(gamma on ker D^2) = 0 - 5 = -dim P5 = -index(M)", T,
            np.isclose(index, -5) and 10 - np.linalg.matrix_rank(M) == P5.shape[1], index)
    rep.add("J7 ker D^2 is supported on edges and equals P5", T,
            np.allclose(kerD2[:5], 0) and observer.rank(np.hstack([kerD2[5:], P5])) == 5)

    # J8
    pts = spacetime.e8_ball(8)
    keys = spacetime._key(pts)
    lookup = dict(zip(keys.tolist(), range(len(pts))))
    perm = np.array([lookup[int(k)] for k in spacetime._key(coordinate_cycle(pts))])
    Rd = spacetime.e8_roots()
    rep.add("J8 coordinate cycle e2->...->e6 preserves the roots (an element of W(E8))", T,
            _keys(coordinate_cycle(Rd) / 2.0) == _keys(Rd / 2.0))
    X6 = spacetime.clique_sites()
    cyc = spacetime._key(coordinate_cycle(X6))
    clq = {int(k): i for i, k in enumerate(spacetime._key(X6))}
    Smap = np.zeros((6, 6))
    for i, k in enumerate(cyc):
        Smap[clq[int(k)], i] = 1
    rep.add("J8 it acts on the clique as the boundary rotation S (x0 fixed, xj -> xj+1)", T,
            np.allclose(Smap, native.boundary_rotation()))
    sysn = native.NativeSystem(r2=8)
    b = sysn.b
    # bath permutation on interior sites: site s -> perm[s]
    pos = {s: i for i, s in enumerate(b.iidx)}
    Pi = np.array([pos[perm[s]] for s in b.iidx])
    Pr = native.p5_rotor()
    rng = np.random.default_rng(11)
    Xr = np.concatenate([0.1 * rng.standard_normal(20), 1e-3 * rng.standard_normal(2 * b.n)])

    def act(Z):
        q, v, y, w = sysn.split(Z)
        q2 = np.r_[Pr @ q[:5], Pr @ q[5:]]
        v2 = np.r_[Pr @ v[:5], Pr @ v[5:]]
        y2, w2 = np.empty_like(y), np.empty_like(w)
        y2[Pi], w2[Pi] = y, w
        return np.concatenate([q2, v2, y2, w2])
    err = np.abs(sysn.rhs(act(Xr)) - act(sysn.rhs(Xr))).max()
    rep.add("J8 full nonlinear native vector field is C5-equivariant (carrier -> bath)",
            gates.SELECTED_REFERENCE, err < 1e-10, float(err),
            note="holds for the reconstructed adapter T, which was chosen equivariant")

    # J9
    src = native.NativeSource()
    u, v, ratio = native.balanced_visible_pair(src)
    w = native.wedge(u, v, src.pairs)
    Kw = native.commutator_map()[0]
    kerK = observer.null_space(Kw)
    vis = np.abs(kerK.T @ w).max()
    # projective dimension of {decomposable wedges in the visible space}
    eps = 1e-6
    q0 = np.r_[u, v]

    def kpart(q):
        return kerK.T @ native.wedge(q[:5], q[5:], src.pairs)
    Jac = np.array([(kpart(q0 + eps * e) - kpart(q0 - eps * e)) / (2 * eps) for e in np.eye(10)]).T
    # pairs (a, b) with visible wedge, modulo GL2 acting on the pair (dim 4)
    dim = 10 - observer.rank(Jac, 1e-6) - 4
    rep.add("J9 40/9 maximiser is a visible decomposable wedge; locus has proj. dim 2 "
            "(del Pezzo surface of J2)", T, vis < 1e-6 and dim == 2,
            {"kernel part": float(vis), "dim": int(dim)})

    rep.add("J10 traces 15, 40, 200 -> heat coefficients 60, 160 m^2, 400 m^4 (layer 6)",
            gates.CONDITIONAL, True, note="the only carrier -> gravity route")

    for n, where, verdict in SHARED_INTEGERS:
        rep.add(f"shared integer {n}: {where}", gates.ARITHMETIC, True, note=verdict)
    return rep
