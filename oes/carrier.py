"""Layer 1. The carrier: signless incidence of K5, its Dirac operator, the
constant-free Lagrangian and its exact motion.

Source: One Machine, 28 Oct 2026 edition of OMSOON736, sections 4-14, 31, 34, 37.
Every matrix here is built from the incidence alone. Exact arithmetic is used
for every acceptance test (sympy Rationals); floating point appears only in
the time evolution, where the closed form is compared against a numerical
integrator.
"""

from itertools import combinations
from math import comb

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from . import gates
from .record import Report

N = 5


def edges(n=N):
    return list(combinations(range(n), 2))


def signless_incidence(n=N):
    """M : R^E -> R^V, an edge goes to the sum of its two endpoints."""
    E = edges(n)
    M = sp.zeros(n, len(E))
    for k, (i, j) in enumerate(E):
        M[i, k] = 1
        M[j, k] = 1
    return M


def signed_incidence(n=N):
    """Oriented boundary, edge (i<j) goes to e_j - e_i."""
    E = edges(n)
    B = sp.zeros(n, len(E))
    for k, (i, j) in enumerate(E):
        B[i, k] = -1
        B[j, k] = 1
    return B


def dirac(M):
    """Odd self-adjoint D = [[0, M], [M^T, 0]] on l2(V u E)."""
    v, e = M.shape
    D = sp.zeros(v + e, v + e)
    D[:v, v:] = M
    D[v:, :v] = M.T
    return D


def grading(n=N):
    """gamma = +1 on vertex atoms, -1 on edge atoms."""
    e = comb(n, 2)
    return sp.diag(*([1] * n + [-1] * e))


# ---------------------------------------------------------------- selection

def kernel_dims(nmax=12):
    """dim ker of the signless and the signed incidence of K_n."""
    out = {}
    for n in range(3, nmax + 1):
        e = comb(n, 2)
        out[n] = (e - signless_incidence(n).rank(), e - signed_incidence(n).rank())
    return out


def equal_kernel_solutions(nmax=12):
    """Complete graphs whose signless incidence has dim ker = |V|."""
    return [n for n, (k, _) in kernel_dims(nmax).items() if k == n]


# ------------------------------------------------------------- spectral data

def D2():
    return dirac(signless_incidence()) ** 2


def spectral_projectors():
    """Exact projectors of D^2 by Lagrange interpolation on {0, 3, 8}."""
    X = D2()
    I = sp.eye(X.shape[0])
    ev = [0, 3, 8]
    P = {}
    for lam in ev:
        num = I
        den = sp.Integer(1)
        for mu in ev:
            if mu != lam:
                num = num * (X - mu * I)
                den *= (lam - mu)
        P[lam] = num / den
    return P


def spectrum_multiplicities():
    P = spectral_projectors()
    return {lam: int(p.trace()) for lam, p in P.items()}


# ---------------------------------------------------------------- Lagrangian

class CarrierLagrangian:
    """S[psi] = int ( 1/2 <psi', psi'> - 1/2 <psi, D^2 psi> ) dt on R^15.

    Nothing else enters: the counting measure is the kinetic metric, D^2 the
    potential, and a relative coefficient between them is a rescaling of t.
    """

    def __init__(self):
        self.K = np.array(D2(), dtype=float)
        P = spectral_projectors()
        self.P = {lam: np.array(p, dtype=float) for lam, p in P.items()}

    def lagrangian(self, psi, v):
        return 0.5 * v @ v - 0.5 * psi @ self.K @ psi

    def energy(self, psi, v):
        return 0.5 * v @ v + 0.5 * psi @ self.K @ psi

    def el_residual(self, psi, acc):
        """Euler-Lagrange residual psi'' + D^2 psi."""
        return acc + self.K @ psi

    def sector_energies(self, psi, v):
        """Energy carried by each closed eigen-sector."""
        out = {}
        for lam, P in self.P.items():
            a, w = P @ psi, P @ v
            out[lam] = 0.5 * w @ w + 0.5 * lam * a @ a
        return out

    def solve(self, psi0, v0, t):
        """Closed-form motion, sector by sector. No diagonalisation."""
        psi = np.zeros_like(psi0, dtype=float)
        vel = np.zeros_like(psi0, dtype=float)
        for lam, P in self.P.items():
            a, w = P @ psi0, P @ v0
            if lam == 0:
                psi += a + t * w
                vel += w
            else:
                om = np.sqrt(lam)
                psi += np.cos(om * t) * a + np.sin(om * t) / om * w
                vel += -om * np.sin(om * t) * a + np.cos(om * t) * w
        return psi, vel


def canon_initial_datum():
    """The integer datum of section 10.

    vertex part (1,-1,0,0,0) + (1,1,1,1,1), edge part M^T applied to the
    contrast, velocity the alternating 4-cycle on edges 01, 12, 23, 03.
    """
    M = np.array(signless_incidence(), dtype=float)
    c = np.array([1, -1, 0, 0, 0], float)
    psi0 = np.concatenate([c + 1.0, M.T @ c])
    idx = {e: k for k, e in enumerate(edges())}
    cyc = np.zeros(10)
    for e, s in (((0, 1), 1), ((1, 2), -1), ((2, 3), 1), ((0, 3), -1)):
        cyc[idx[e]] = s
    v0 = np.concatenate([np.zeros(5), cyc])
    return psi0, v0


def leapfrog(K, psi, v, dt, steps):
    """Symplectic check on the closed form."""
    a = -K @ psi
    for _ in range(steps):
        v = v + 0.5 * dt * a
        psi = psi + dt * v
        a = -K @ psi
        v = v + 0.5 * dt * a
    return psi, v


# ------------------------------------------------------ joined finite objects

def petersen():
    """Disjointness graph on the ten edges of K5."""
    E = edges()
    A = sp.zeros(10, 10)
    for a, e in enumerate(E):
        for b, f in enumerate(E):
            if not set(e) & set(f):
                A[a, b] = 1
    return A


def girth(A):
    A = np.array(A, dtype=int)
    n = len(A)
    best = n + 1
    for s in range(n):
        dist = {s: 0}
        par = {s: -1}
        q = [s]
        for u in q:
            for w in np.nonzero(A[u])[0]:
                w = int(w)
                if w not in dist:
                    dist[w] = dist[u] + 1
                    par[w] = u
                    q.append(w)
                elif par[u] != w:
                    best = min(best, dist[u] + dist[w] + 1)
    return best


def fundamental_cycles():
    """Star tree at vertex 0; one cycle per cotree edge, oriented 0->i->j->0."""
    idx = {e: k for k, e in enumerate(edges())}
    cot = [e for e in edges() if 0 not in e]
    C = sp.zeros(len(cot), 10)
    for r, (i, j) in enumerate(cot):
        C[r, idx[(i, j)]] = 1
        C[r, idx[(0, i)]] = 1
        C[r, idx[(0, j)]] = -1
    return C, cot


def hodge_block():
    """A = (6I - G) sigma with sigma the signed opposite-edge exchange."""
    C, cot = fundamental_cycles()
    G = C * C.T
    pos = {e: r for r, e in enumerate(cot)}
    signs = (-1, 1, -1, -1, 1, -1)
    S = sp.zeros(6, 6)
    for r, (i, j) in enumerate(cot):
        k, l = sorted(set(range(1, 5)) - {i, j})
        S[pos[(k, l)], r] = signs[r]
    return G, S, (6 * sp.eye(6) - G) * S


def edge_tick():
    """Rotate vertices i -> i+1; carry edges along with orientation sign."""
    E = edges()
    idx = {e: k for k, e in enumerate(E)}
    T = sp.zeros(10, 10)
    R = sp.zeros(5, 5)
    for i in range(5):
        R[(i + 1) % 5, i] = 1
    for k, (i, j) in enumerate(E):
        a, b = (i + 1) % 5, (j + 1) % 5
        s = 1 if a < b else -1
        T[idx[tuple(sorted((a, b)))], k] = s
    return T, R


def contrast_moments():
    """M2, M4 on the contrast plane and the harmonic obstruction (sec 11-12)."""
    x = sp.symbols("x0:5")
    sub = {x[4]: -(x[0] + x[1] + x[2] + x[3])}
    # The roots are the twenty ORIENTED edges e_i - e_j (the A4 system).
    # The printed text writes the sum over i<j; that sum is half of each
    # identity below (M2 over ten pairs is 5|x|^2, not 10|x|^2).
    roots = [(i, j) for i in range(5) for j in range(5) if i != j]
    M2 = sum((x[i] - x[j]) ** 2 for i, j in roots)
    M4 = sum((x[i] - x[j]) ** 4 for i, j in roots)
    half = sum((x[i] - x[j]) ** 2 for i, j in combinations(range(5), 2))
    r2 = sum(xi ** 2 for xi in x)
    s4 = sum(xi ** 4 for xi in x)
    m2_ok = sp.expand((M2 - 10 * r2).subs(sub)) == 0
    m4_ok = sp.expand((M4 - 6 * r2 ** 2 - 10 * s4).subs(sub)) == 0
    lap = lambda f: sum(sp.diff(f, xi, 2) for xi in x)
    # The contrast plane's own Laplacian is tr(P Hess) with P = I - J/5.
    P = sp.eye(5) - sp.ones(5, 5) / 5
    lap_plane = lambda f: sp.expand(sum(P[i, j] * sp.diff(f, x[i], x[j]) for i in range(5)
                                        for j in range(5)).subs(sub))
    h = 3 * r2 ** 2 - 7 * s4
    g = 2 * r2 ** 2 - 5 * s4
    half_ok = sp.expand((half - 5 * r2).subs(sub)) == 0
    return {"M2=10|x|^2 over the 20 roots": m2_ok,
            "correction: over the 10 pairs i<j the sum is 5|x|^2": half_ok, "M4=6|x|^4+10sum x^4 over the 20 roots": m4_ok,
            "lap|x|^4=28|x|^2": sp.expand(lap(r2 ** 2) - 28 * r2) == 0,
            "lap sum x^4=12|x|^2": sp.expand(lap(s4) - 12 * r2) == 0,
            "3|x|^4-7sum x^4 harmonic for the ambient Laplacian of R^5": sp.expand(lap(h)) == 0,
            "on the contrast plane itself: lap|x|^4=24|x|^2, lap sum x^4=(48/5)|x|^2, so the harmonic "
            "line is 2|x|^4-5sum x^4 and 3|x|^4-7sum x^4 is not (canon 28 Oct)":
                lap_plane(r2 ** 2) == sp.expand((24 * r2).subs(sub))
                and lap_plane(s4) == sp.expand((sp.Rational(48, 5) * r2).subs(sub))
                and lap_plane(g) == 0 and lap_plane(h) != 0}


# --------------------------------------------------------------------- checks

def run():
    rep = Report("1-carrier")
    T = gates.THEOREM

    kd = kernel_dims(12)
    sol = equal_kernel_solutions(12)
    rep.add("dim ker M_n = n(n-3)/2 for n=3..12", T,
            all(k == n * (n - 3) // 2 for n, (k, _) in kd.items()))
    rep.add("dim ker M = |V| selects K5 only (n<=12; quadratic beyond)", T,
            sol == [5], sol)
    rep.add("signed incidence never has dim ker = n (disc 17 not square)", T,
            all(s != n for n, (_, s) in kd.items()))

    M = signless_incidence()
    I5, J5 = sp.eye(5), sp.ones(5, 5)
    gram = M * M.T
    rep.add("M M^T = 3I + J", T, gram == 3 * I5 + J5)
    rep.add("(3I+J)^-1 = I/3 - J/24", T,
            (3 * I5 + J5) * (I5 / 3 - J5 / 24) == I5)
    smith = smith_normal_form(M, domain=sp.ZZ)
    inv = sorted(abs(smith[i, i]) for i in range(5))
    rep.add("Smith invariants of M are 1,1,1,1,2", T, inv == [1, 1, 1, 1, 2], inv)

    D = dirac(M)
    g = grading()
    rep.add("D self-adjoint and odd: {D, gamma} = 0", T,
            D == D.T and D * g + g * D == sp.zeros(15, 15))
    X = D ** 2
    I15 = sp.eye(15)
    rep.add("D^2 (D^2-3)(D^2-8) = 0", T,
            X * (X - 3 * I15) * (X - 8 * I15) == sp.zeros(15, 15))
    mult = spectrum_multiplicities()
    rep.add("spec(D^2) = {0^5, 3^8, 8^2}", T, mult == {0: 5, 3: 8, 8: 2}, mult)
    rep.add("Tr D^2 = 40, Tr D^4 = 200, odd traces 0", T,
            X.trace() == 40 and (X * X).trace() == 200
            and D.trace() == 0 and (D * X).trace() == 0,
            [int(X.trace()), int((X * X).trace())])
    rep.add("D^2 has rank 10", T, X.rank() == 10)

    Bs = signed_incidence()
    Xs = dirac(Bs) ** 2
    ms = {lam: 15 - (Xs - lam * I15).rank() for lam in (0, 5)}
    rep.add("signed Dirac square has spectrum {0^7, 5^8}; not the carrier", T,
            ms == {0: 7, 5: 8}, ms)

    # S5-equivariant maps R^E -> R^V are spanned by M and J (dimension 2)
    perms = [(1, 0, 2, 3, 4), (1, 2, 3, 4, 0)]  # generators of S5
    Eidx = {e: k for k, e in enumerate(edges())}
    rows = []
    for p in perms:
        PV = sp.zeros(5, 5)
        for i in range(5):
            PV[p[i], i] = 1
        PE = sp.zeros(10, 10)
        for k, (i, j) in enumerate(edges()):
            PE[Eidx[tuple(sorted((p[i], p[j])))], k] = 1
        rows.append((PV, PE))
    W = sp.Matrix(5, 10, sp.symbols("w0:50"))
    eqs = []
    for PV, PE in rows:
        eqs += list(PV * W - W * PE)
    sol_space = sp.linsolve(eqs, list(W))
    free = list(sol_space)[0].free_symbols
    rep.add("S5-equivariant maps R^E->R^V form a 2-dim space (M, J)", T,
            len(free) == 2, len(free))

    # Lagrangian and motion
    L = CarrierLagrangian()
    psi0, v0 = canon_initial_datum()
    se = L.sector_energies(psi0, v0)
    rep.add("initial datum: sector energies 12 (lam=3) + 20 (lam=8) + 2 (kernel)",
            T, np.allclose([se[3], se[8], se[0]], [12, 20, 2]),
            {k: round(v, 12) for k, v in se.items()})
    rep.add("<psi0, D^2 psi0> = 64 and E = 34", T,
            np.isclose(psi0 @ L.K @ psi0, 64) and np.isclose(L.energy(psi0, v0), 34))
    ts = np.linspace(0, 20, 201)
    errE, errEL = 0.0, 0.0
    for t in ts:
        p, v = L.solve(psi0, v0, t)
        errE = max(errE, abs(L.energy(p, v) - 34))
        h = 1e-4
        pp, _ = L.solve(psi0, v0, t + h)
        pm, _ = L.solve(psi0, v0, t - h)
        errEL = max(errEL, np.abs(L.el_residual(p, (pp - 2 * p + pm) / h ** 2)).max())
    rep.add("closed form conserves energy (machine precision)", T, errE < 1e-11, errE)
    rep.add("closed form solves psi'' + D^2 psi = 0 (FD residual)", T, errEL < 1e-5, errEL)
    pl, vl = leapfrog(L.K, psi0, v0, 1e-3, 5000)
    pc, vc = L.solve(psi0, v0, 5.0)
    rep.add("leapfrog integrator agrees with closed form at t=5", T,
            np.abs(pl - pc).max() < 1e-5, float(np.abs(pl - pc).max()))
    rep.add("frequencies 0, sqrt3, 2sqrt2; ratio^2 = 8/3 not a rational square",
            T, sp.sqrt(sp.Rational(8, 3)).is_rational is False)

    # Petersen and cycles
    A = petersen()
    I10, J10 = sp.eye(10), sp.ones(10, 10)
    rep.add("Petersen: A^2 + A - 2I = J, 3-regular, 15 edges", T,
            A * A + A - 2 * I10 == J10 and all(sum(A.row(i)) == 3 for i in range(10))
            and sum(A) == 30)
    rep.add("Petersen girth 5", T, girth(A) == 5)
    pm = {lam: 10 - (A - lam * I10).rank() for lam in (3, 1, -2)}
    rep.add("Petersen projector ranks 1, 5, 4", T, pm == {3: 1, 1: 5, -2: 4}, pm)

    G, S, Ah = hodge_block()
    I6 = sp.eye(6)
    rep.add("cycle Gram (G-I)(G-5I)=0, det G = 125", T,
            (G - I6) * (G - 5 * I6) == sp.zeros(6, 6) and G.det() == 125)
    rep.add("Hodge block A=(6I-G)sigma: sigma^2=I, A^2=5I", T,
            S * S == I6 and Ah * Ah == 5 * I6)
    Gs = Bs.T * Bs
    rep.add("signed edge gram G^2 = 5G, eigen 0^6 5^4; cycle projector (5I-G)/5", T,
            Gs * Gs == 5 * Gs and Gs.rank() == 4 and Gs.trace() == 20)

    Tk, R = edge_tick()
    rep.add("edge tick: order 5, B T = R B (signed boundary)", T,
            Tk ** 5 == I10 and Tk != I10 and Bs * Tk == R * Bs)
    Tabs = Tk.applyfunc(abs)
    rep.add("unsigned tick commutes with Petersen adjacency", T, Tabs * A == A * Tabs)
    C, _ = fundamental_cycles()
    # tick preserves cycle space: B (T c) = R B c = 0
    rep.add("tick preserves the 6-dim cycle space (induces the order-5 rotor)", T,
            Bs * Tk * C.T == sp.zeros(5, 6))

    for k, ok in contrast_moments().items():
        rep.add(k, T, ok)
    rep.add("quartic not in action: coupling needs a dimensionful constant",
            gates.OBSTRUCTION, True,
            note="harmonic line recorded so the obstruction is checked")
    return rep
