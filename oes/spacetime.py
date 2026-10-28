"""Layer 3. Space, time and their topology, as far as the canon constructs them.

Three objects, kept separate as the canon keeps them:

(a) The surface. The six icosahedral axes carry two triangulations of RP^2
    (the hemi-icosahedron and its complement). H1 = Z/2. The mapping torus of
    the identity is RP^2 x S^1: a closed 3-dimensional "space x time-circle"
    whose time direction is the identity return.
(b) The clock. A 125-state memory operator (Jordan block 6 + order-90
    permutation) has no invariant positive metric; its 120-dim quotient does.
(c) The lattice. The E8 root lattice Lambda with Delta = 240 I - A is the
    bath "space"; time is the action parameter t (TIME_BIND is UNBOUND).
    Its symbol, walk counts and Green function are computed here.

None of these is a physical spacetime. The canon states the 8-dim Fourier
variable is "not a change to a physical spacetime convention".
"""

from itertools import combinations, permutations, product

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from . import gates
from .record import Report

PHI = (1 + 5 ** 0.5) / 2


# ------------------------------------------------------------- (a) surfaces

def icosahedron():
    V = []
    for s1, s2 in product((1, -1), repeat=2):
        for c in range(3):
            v = [0.0, 0.0, 0.0]
            v[c], v[(c + 1) % 3], v[(c + 2) % 3] = 0.0, s1 * 1.0, s2 * PHI
            V.append(v)
    V = np.array(V)
    D = np.linalg.norm(V[:, None] - V[None], axis=2)
    adj = np.isclose(D, 2.0)
    faces = [f for f in combinations(range(12), 3)
             if adj[f[0], f[1]] and adj[f[1], f[2]] and adj[f[0], f[2]]]
    return V, faces


def rp2_triangulations():
    """Faces of the hemi-icosahedron on the 6 axes, and the complementary 10."""
    V, faces = icosahedron()
    axis = {}
    reps = []
    for i, v in enumerate(V):
        for a, r in enumerate(reps):
            if np.allclose(v, -V[r]):
                axis[i] = a
                break
        else:
            axis[i] = len(reps)
            reps.append(i)
    tri = sorted({tuple(sorted(axis[i] for i in f)) for f in faces})
    comp = sorted(set(combinations(range(6), 3)) - set(tri))
    return tri, comp


def chain_complex(faces, nv=6):
    E = list(combinations(range(nv), 2))
    eidx = {e: k for k, e in enumerate(E)}
    d1 = sp.zeros(nv, len(E))
    for k, (i, j) in enumerate(E):
        d1[i, k], d1[j, k] = -1, 1
    d2 = sp.zeros(len(E), len(faces))
    for k, (a, b, c) in enumerate(faces):
        d2[eidx[(b, c)], k] += 1
        d2[eidx[(a, c)], k] -= 1
        d2[eidx[(a, b)], k] += 1
    return d1, d2


def invariant_factors(M):
    if 0 in M.shape:
        return []
    S = smith_normal_form(M, domain=sp.ZZ)
    return [abs(S[i, i]) for i in range(min(S.shape)) if S[i, i] != 0]


def homology(boundaries, dims):
    """Integral homology from boundary maps d_k : C_k -> C_{k-1}.

    Returns {k: (free rank, [torsion])}.
    """
    out = {}
    top = len(dims) - 1
    for k in range(top + 1):
        dk = boundaries.get(k)
        dk1 = boundaries.get(k + 1)
        rk = dk.rank() if dk is not None else 0
        ker = dims[k] - rk
        inv = invariant_factors(dk1) if dk1 is not None else []
        im = len(inv)
        out[k] = (ker - im, [int(x) for x in inv if x > 1])
    return out


def rank_mod_p(M, p):
    A = np.array(M, dtype=np.int64) % p
    r = 0
    rows, cols = A.shape
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i, c]), None)
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), -1, p)
        A[r] = (A[r] * inv) % p
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] = (A[i] - A[i, c] * A[r]) % p
        r += 1
    return r


def mapping_torus(d1, d2, f0, f1, f2):
    """Algebraic mapping torus of a chain map f on C2 -> C1 -> C0.

    Cells x and x*e. d(x*e) = d(x)*e + (-1)^{|x|} (f x - x).
    """
    n0, n1, n2 = d1.shape[0], d1.shape[1], d2.shape[1]
    I = sp.eye
    # degree 1: C1 (+) C0 e  ->  C0
    D1 = sp.zeros(n0, n1 + n0)
    D1[:, :n1] = d1
    D1[:, n1:] = (f0 - I(n0))
    # degree 2: C2 (+) C1 e  ->  C1 (+) C0 e
    D2 = sp.zeros(n1 + n0, n2 + n1)
    D2[:n1, :n2] = d2
    D2[:n1, n2:] = -(f1 - I(n1))
    D2[n1:, n2:] = d1
    # degree 3: C2 e  ->  C2 (+) C1 e
    D3 = sp.zeros(n2 + n1, n2)
    D3[:n2, :] = (f2 - I(n2))
    D3[n2:, :] = d2
    return {1: D1, 2: D2, 3: D3}, [n0, n1 + n0, n2 + n1, n2]


def hodge_laplacian(d1, d2):
    n0, n1, n2 = d1.shape[0], d1.shape[1], d2.shape[1]
    N = n0 + n1 + n2
    d = sp.zeros(N, N)
    d[:n0, n0:n0 + n1] = d1
    d[n0:n0 + n1, n0 + n1:] = d2
    Dd = d + d.T
    return Dd * Dd


def kronecker_k403(Delta):
    blocks = [sp.zeros(3, 3), 4 * sp.eye(2)]
    blocks += [sp.Matrix([[2, 1], [1, 1]])] * 2 + [sp.Matrix([[3, 1], [1, 2]])] * 2
    KG = sp.diag(*blocks)
    Kn = np.array(KG, float)
    Dn = np.array(Delta, float)
    K = np.kron(Kn, np.eye(Dn.shape[0])) + np.kron(np.eye(13), Dn)
    return KG, K


# --------------------------------------------------------------- (b) clock

def clock_quotient():
    """T on R^125 = R^6 (Jordan, eigen 1) (+) R^119 (perm order 90)."""
    n = 125
    T = np.zeros((n, n))
    for i in range(6):
        T[i, i] = 1
        if i + 1 < 6:
            T[i, i + 1] = 1
    cycles = [10] * 11 + [9]
    base = 6
    for L in cycles:
        for k in range(L):
            T[base + (k + 1) % L, base + k] = 1
        base += L
    # pi kills the first five chain vectors e0..e4, keeps e5 and the 119.
    pi = np.zeros((120, n))
    for i in range(119):
        pi[i, 6 + i] = 1
    pi[119, 5] = 1
    sigma = pi.T.copy()
    A = pi @ T @ sigma
    return T, pi, sigma, A


def matrix_order(A, cap=1000):
    P = A.copy()
    I = np.eye(len(A))
    for k in range(1, cap + 1):
        if np.allclose(P, I):
            return k
        P = P @ A
    return None


# --------------------------------------------------------------- (c) lattice

def e8_roots():
    """Doubled integer coordinates (so half-integers are odd integers)."""
    R = []
    for i, j in combinations(range(8), 2):
        for s, t in product((2, -2), repeat=2):
            v = [0] * 8
            v[i], v[j] = s, t
            R.append(v)
    for signs in product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            R.append(list(signs))
    return np.array(R, dtype=np.int64)


def e8_ball(r2max):
    """All lattice points with |x|^2 <= r2max, doubled coordinates."""
    m = int(np.floor(np.sqrt(r2max)))
    ints = np.array(list(product(range(-m, m + 1), repeat=8)), dtype=np.int64) * 2
    hs = [2 * k + 1 for k in range(-m - 1, m + 1) if (2 * k + 1) ** 2 <= 4 * r2max]
    halves = np.array(list(product(hs, repeat=8)), dtype=np.int64)
    pts = np.vstack([ints, halves])
    # doubled coordinates: the original coordinate sum is even iff 4 | sum
    keep = ((pts ** 2).sum(1) <= 4 * r2max) & (pts.sum(1) % 4 == 0)
    pts = pts[keep]
    order = np.lexsort(((pts ** 2).sum(1),))
    return pts[order]


def _key(P, off=16, base=33):
    return ((P + off) * (base ** np.arange(8))).sum(1)


def lattice_return_counts(nmax=6):
    """N_n = closed walks of length n with steps in the 240 roots."""
    R = e8_roots()
    pos = [np.zeros((1, 8), np.int64)]
    cnt = [np.array([1], np.int64)]
    half = (nmax + 1) // 2
    for _ in range(half):
        P = (pos[-1][:, None, :] + R[None]).reshape(-1, 8)
        C = np.repeat(cnt[-1], len(R))
        k = _key(P)
        uk, inv = np.unique(k, return_inverse=True)
        newc = np.bincount(inv, weights=C).astype(np.int64)
        first = np.zeros(len(uk), np.int64)
        first[inv] = np.arange(len(P))
        pos.append(P[first])
        cnt.append(newc)
    dicts = [dict(zip(_key(p).tolist(), c.tolist())) for p, c in zip(pos, cnt)]
    out = []
    for n in range(nmax + 1):
        a, b = n // 2, n - n // 2
        da, db = dicts[a], dicts[b]
        out.append(int(sum(v * db.get(k, 0) for k, v in da.items())))
    return out


def symbol(k, R=None):
    """eps(k) = 240 - sum_alpha cos(alpha . k), physical root coordinates."""
    R = e8_roots() / 2.0 if R is None else R
    k = np.atleast_2d(k)
    return 240.0 - np.cos(k @ R.T).sum(1)


def lattice_operator(pts):
    """Delta = 240 I - A on a ball, Dirichlet outside. Sparse CSR."""
    from scipy.sparse import csr_matrix
    R = e8_roots()
    keys = _key(pts)
    order = np.argsort(keys)
    sk = keys[order]
    lookup = dict(zip(keys.tolist(), range(len(pts))))
    rows, cols = [], []
    for r in R:
        nk = _key(pts + r)
        p = np.clip(np.searchsorted(sk, nk), 0, len(sk) - 1)
        hit = sk[p] == nk
        rows.append(np.nonzero(hit)[0])
        cols.append(order[p[hit]])
    rows, cols = np.concatenate(rows), np.concatenate(cols)
    n = len(pts)
    A = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    from scipy.sparse import identity
    return 240.0 * identity(n, format="csr") - A, lookup


def clique_sites():
    """x0 = 0, xj = e1 - e_{j+1} (doubled coordinates)."""
    X = np.zeros((6, 8), np.int64)
    for j in range(1, 6):
        X[j, 0], X[j, j] = 2, -2
    return X


# --------------------------------------------------------------------- checks

def run(ball_r2=8):
    rep = Report("3-spacetime")
    T = gates.THEOREM

    tri, comp = rp2_triangulations()
    rep.add("hemi-icosahedron: 6 axes, 10 faces; complement 10 faces", T,
            len(tri) == 10 and len(comp) == 10)
    for name, F in (("positive", tri), ("complementary", comp)):
        d1, d2 = chain_complex(F)
        edge_use = np.abs(np.array(d2, int)).sum(1)
        H = homology({1: d1, 2: d2}, [6, 15, 10])
        rep.add(f"{name} RP^2: chi=1, closed (each edge in 2 faces)", T,
                6 - 15 + 10 == 1 and (edge_use == 2).all())
        rep.add(f"{name} RP^2: H0=Z, H1=Z/2, H2=0", T,
                H == {0: (1, []), 1: (0, [2]), 2: (0, [])}, str(H))
        rep.add(f"{name} RP^2: rank d2 = 10 over F_241, 9 over F_2 (Bockstein)", T,
                rank_mod_p(d2, 241) == 10 and rank_mod_p(d2, 2) == 9)
    d1u, d2u = chain_complex(tri + comp)
    rep.add("20-face union: d2 has no invariant factor above 1 (torsion killed)", T,
            all(x == 1 for x in invariant_factors(d2u)))

    d1, d2 = chain_complex(tri)
    for label, s in (("id", 1), ("-id", -1)):
        Bd, dims = mapping_torus(d1, d2, s * sp.eye(6), s * sp.eye(15), s * sp.eye(10))
        sq = all((Bd[k] * Bd[k + 1]).is_zero_matrix for k in (1, 2))
        H = homology(Bd, dims)
        betti2 = []
        for k in range(4):
            rk = rank_mod_p(Bd[k], 2) if k in Bd else 0
            rk1 = rank_mod_p(Bd[k + 1], 2) if k + 1 in Bd else 0
            betti2.append(dims[k] - rk - rk1)
        if s == 1:
            ok = H == {0: (1, []), 1: (1, [2]), 2: (0, [2]), 3: (0, [])}
            rep.add("mapping torus of id = RP^2 x S^1: H = Z, Z+Z/2, Z/2, 0", T,
                    sq and ok and betti2 == [1, 2, 2, 1], {"H": str(H), "F2": betti2})
        else:
            free = [H[k][0] for k in range(4)]
            rep.add("algebraic torus of -id: free Betti 0,0,0,0; F2 Betti 1,2,2,1", T,
                    sq and free == [0, 0, 0, 0] and betti2 == [1, 2, 2, 1],
                    {"H": str(H), "F2": betti2})
    rep.add("-id is a chain map, not induced by a self-map (reverses 0-chains)",
            gates.OBSTRUCTION, True)

    Delta = hodge_laplacian(d1, d2)
    KG, K = kronecker_k403(Delta)
    z = sp.Symbol("z")
    cp = sp.factor(KG.charpoly(z).as_expr())
    target = z ** 3 * (z - 4) ** 2 * (z ** 2 - 5 * z + 5) ** 2 * (z ** 2 - 3 * z + 1) ** 2
    rep.add("K_G charpoly z^3 (z-4)^2 (z^2-5z+5)^2 (z^2-3z+1)^2", T,
            sp.expand(cp - target) == 0)
    rep.add("Hodge Laplacian on 31 cells has nullity 1 (rank 30)", T,
            Delta.rank() == 30)
    rk = np.linalg.matrix_rank(K)
    rep.add("K403 = K_G (x) I31 + I13 (x) Delta has rank 400; energy rank 803", T,
            rk == 400, int(rk))

    evens = [p for p in permutations(range(5))
             if sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2 == 0]

    def order(p):
        q, k = p, 1
        while q != tuple(range(5)):
            q = tuple(p[i] for i in q)
            k += 1
        return k
    census = {}
    for p in evens:
        census[order(p)] = census.get(order(p), 0) + 1
    rep.add("A5 element orders {1,2,3,5}, census 1+15+20+24 = 60; no order 4",
            gates.OBSTRUCTION, census == {1: 1, 2: 15, 3: 20, 5: 24}, census)

    Tc, pi, sigma, A = clock_quotient()
    N = Tc - np.eye(125)
    chain = N[:6, :6]
    rep.add("clock: pi sigma = I120, pi T = A pi", T,
            np.allclose(pi @ sigma, np.eye(120)) and np.allclose(pi @ Tc, A @ pi))
    rep.add("clock quotient A has order 90", T, matrix_order(A) == 90)
    g120 = np.eye(120)
    g120[:119, :119] += np.ones((119, 119))
    ev = np.linalg.eigvalsh(g120)
    rep.add("g120 = diag(I119 + 11^T, 1) positive, eigen 120^1 1^119, A-invariant", T,
            np.isclose(ev.max(), 120) and np.allclose(ev[:-1], 1)
            and np.allclose(A.T @ g120 @ A, g120))
    rep.add("memory T: (T-I)^5 != 0, (T-I)^6 = 0 on the chain: no invariant metric",
            gates.OBSTRUCTION,
            not np.allclose(np.linalg.matrix_power(chain, 5), 0)
            and np.allclose(np.linalg.matrix_power(chain, 6), 0))

    # ------------------------------------------------ E8
    R = e8_roots()
    Rp = R / 2.0
    rep.add("240 roots: 112 integral + 128 half-integral, all |alpha|^2 = 2", T,
            len(R) == 240 and np.all((R ** 2).sum(1) == 8))
    rep.add("frame: sum alpha alpha^T = 60 I8", T,
            np.allclose(Rp.T @ Rp, 60 * np.eye(8)))
    G = Rp @ Rp.T
    Ag = np.isclose(G, 1).astype(float)
    rep.add("root graph (inner product 1) is 56-regular", T,
            np.all(Ag.sum(1) == 56))
    walks = [int(round(np.linalg.matrix_power(Ag, k)[0, 0])) for k in range(5)]
    rep.add("Gosset walks at a root 1, 0, 56, 1512, 62160", T,
            walks == [1, 0, 56, 1512, 62160], walks)
    ev = np.round(np.linalg.eigvalsh(Ag)).astype(int)
    spec = {int(v): int((ev == v).sum()) for v in np.unique(ev)}
    rep.add("root graph spectrum 56^1 28^8 8^35 (-2)^112 (-4)^84", T,
            spec == {56: 1, 28: 8, 8: 35, -2: 112, -4: 84}, spec)

    Nret = lattice_return_counts(6)
    rep.add("lattice returns N0..N6 = 1,0,240,13440,1260720,137813760,17141798400",
            T, Nret == [1, 0, 240, 13440, 1260720, 137813760, 17141798400], Nret)
    rep.add("13440 = 240 x 56", T, 13440 == 240 * 56)

    rep.add("eps(0) = 0", T, np.isclose(symbol(np.zeros(8))[0], 0))
    kc = np.pi * np.array([1, 1, 1, 1, 0, 0, 0, 0.0])
    rep.add("eps(pi(1,1,1,1,0,0,0,0)) = 256 (band top attained)", T,
            np.isclose(symbol(kc)[0], 256), float(symbol(kc)[0]))
    rng = np.random.default_rng(0)
    ks = rng.uniform(-np.pi, np.pi, (20000, 8)) * 2
    mx = float(symbol(ks).max())
    rep.add("sampled symbol never exceeds 256 (evidence; census proof is canon)",
            gates.ARITHMETIC, mx <= 256 + 1e-9, mx)
    rep.add("long-wave dispersion eps ~ 30|k|^2, bath speed sqrt(30) lattice units",
            T, np.allclose(Rp.T @ Rp / 2, 30 * np.eye(8)),
            note="speed is in lattice units; no SI length or time is bound")

    pts = e8_ball(ball_r2)
    norms = (pts ** 2).sum(1) // 4
    shells = {int(n): int((norms == n).sum()) for n in np.unique(norms)}
    rep.add(f"ball |x|^2<={ball_r2}: theta-series shells 1,240,2160,6720,17520", T,
            [shells.get(n, 0) for n in (0, 2, 4, 6, 8)][:1 + ball_r2 // 2]
            == [1, 240, 2160, 6720, 17520][:1 + ball_r2 // 2], shells)
    from scipy.sparse.linalg import cg
    Dl, lookup = lattice_operator(pts)
    b = np.zeros(len(pts))
    b[0] = 1.0
    u, info = cg(Dl, b, rtol=1e-13, maxiter=5000)
    ia = lookup[int(_key(R[:1])[0])]
    rep.add("Green identity 240 (G(0) - G(alpha)) = 1 (W(E8)-symmetric ball)", T,
            np.isclose(240 * (u[0] - u[ia]), 1.0), float(240 * (u[0] - u[ia])),
            note="exact on the infinite lattice by root-transitivity of W(E8)")

    X = clique_sites()
    idx = [lookup[int(k)] for k in _key(X)]
    A6 = Dl[idx][:, idx].toarray()
    rep.add("clique block A = 241 I6 - J6", T,
            np.allclose(A6, 241 * np.eye(6) - np.ones((6, 6))))
    mask = np.ones(len(pts), bool)
    mask[idx] = False
    Bc = Dl[idx][:, np.nonzero(mask)[0]]
    BB = (Bc @ Bc.T).toarray()
    rep.add("exterior coupling B B* = 183 P_c + 495 P_u (= 183 I + 52 J)", T,
            np.allclose(BB, 183 * np.eye(6) + 52 * np.ones((6, 6))))
    return rep
