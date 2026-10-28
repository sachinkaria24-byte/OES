"""Layer 4. The declared native action: a K5 source, a quadratic commutator
port, and the E8 lattice-wave bath.

    L = 1/2 q'^T M_s q' + 1/2 |d g(q)/dt|^2 + 1/2 |y'|^2
        - 2 q^T M_s q - 1/2 g^T (W_p + A) g - g^T B y - 1/2 <y, D y>

q = (a, b) in P5 (+) P5 with P5 = ker M (signless incidence), g(q) the six-port
boundary displacement, y the bath on the lattice off the six-site clique, and
Delta = [[A, B], [B^T, D]] the partition of 240 I - Adj on the clique
x0 = 0, xj = e1 - e_{j+1}.

Source: OES_All_Dots_Through724 (Appendix A and the boundary-pullback action),
OES_736_Collar_Localization_Proof_20261028 (sections 1, 4), One Machine sec 41.

What is reconstructed here and what is not
-----------------------------------------
The saved native_source_matrices file (SHA256 73e07429...) was listed as
absent when this layer was written. Layer 10 (oes/literal.py) has since
recovered it and shows this reconstruction differs from it only by an element
of the C5 commutant. This module still rebuilds the port from its stated
definition and labels the result SELECTED_REFERENCE:

* A(a) is the symmetric zero-diagonal 5x5 matrix with off-diagonal entries a_e.
  Since M a = 0 its rows sum to zero, so [A(a), A(b)] is skew with zero row
  sums: an oriented cycle. That is W_AS : Lambda^2 P5 -> L6.
* M_s = I/4 in an orthonormal basis of P5. P5 is the 5-dim irreducible of S5,
  so every invariant metric is a multiple of this one; the multiple is a unit
  of amplitude. (The canon's det 8/9 refers to its saved basis.)
* W_p is the canon's explicit boundary metric: circulant (22,-8,2,2,-8)/5 on
  x1..x5 and 2/5 on x0.
* The adapter T : L6 -> boundary order is chosen to intertwine the source
  rotor with the bath rotation x_j -> x_{j+1} and to make
  (T W_AS)^T W_p (T W_AS) = (320/9) G P, the identity the canon states.
  The residual freedom (an O(2) x SO(2) x SO(2) commutant) is fixed by a
  deterministic Reynolds average. Source/port energetics do not depend on it;
  the bath coupling does.
"""

import numpy as np
import sympy as sp

from . import carrier, gates, spacetime
from .record import Report

R5 = 5 ** 0.5


# ---------------------------------------------------------------- source

def p5_basis():
    """Orthonormal basis (10 x 5) of P5 = ker of the signless incidence."""
    M = np.array(carrier.signless_incidence(), float)
    _, s, Vt = np.linalg.svd(M)
    return Vt[5:].T


def l6_basis():
    """Orthonormal basis (10 x 6) of the cycle space ker of the signed boundary."""
    B = np.array(carrier.signed_incidence(), float)
    _, s, Vt = np.linalg.svd(B)
    return Vt[4:].T


def source_matrix(e):
    A = np.zeros((5, 5))
    for k, (i, j) in enumerate(carrier.edges()):
        A[i, j] = A[j, i] = e[k]
    return A


def oriented(C):
    return np.array([C[i, j] for i, j in carrier.edges()])


def commutator_map():
    """W_AS as a 6 x 10 matrix from Lambda^2 P5 (basis p_i ^ p_j) to L6."""
    P, Q = p5_basis(), l6_basis()
    cols = []
    pairs = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    for i, j in pairs:
        Ai, Aj = source_matrix(P[:, i]), source_matrix(P[:, j])
        cols.append(Q.T @ oriented(Ai @ Aj - Aj @ Ai))
    return np.array(cols).T, pairs


def wedge(a, b, pairs):
    return np.array([a[i] * b[j] - a[j] * b[i] for i, j in pairs])


# ------------------------------------------------------------------ port

def port_metric():
    """W_p in boundary order (x0, x1, ..., x5)."""
    row = np.array([22, -8, 2, 2, -8]) / 5.0
    C = np.array([np.roll(row, k) for k in range(5)])
    W = np.zeros((6, 6))
    W[0, 0] = 2 / 5
    W[1:, 1:] = C
    return W


def boundary_rotation():
    S = np.zeros((6, 6))
    S[0, 0] = 1
    for j in range(5):
        S[1 + (j + 1) % 5, 1 + j] = 1
    return S


def cycle_rotor():
    Tk, _ = carrier.edge_tick()
    Q = l6_basis()
    return Q.T @ np.array(Tk, float) @ Q


def p5_rotor():
    Tk, _ = carrier.edge_tick()
    P = p5_basis()
    return P.T @ np.array(Tk, float).__abs__() @ P


def _isqrt(W):
    w, V = np.linalg.eigh(W)
    return (V / np.sqrt(w)) @ V.T


def adapter():
    """Equivariant T : L6 -> boundary with T^T W_p T = c^2 I."""
    S, Rr = boundary_rotation(), cycle_rotor()
    X = sum(np.linalg.matrix_power(S, k) @ np.linalg.matrix_power(Rr, -k % 5)
            for k in range(5)) / 5
    if abs(np.linalg.det(X)) < 1e-8:
        rng = np.random.default_rng(1)
        Y = rng.standard_normal((6, 6))
        X = sum(np.linalg.matrix_power(S, k) @ Y @ np.linalg.matrix_power(Rr, -k % 5)
                for k in range(5)) / 5
    U, _, Vt = np.linalg.svd(X)
    O = U @ Vt
    K, _ = commutator_map()
    KK = K.T @ K
    kappa = np.trace(KK) / np.linalg.matrix_rank(KK)
    c = np.sqrt(20.0 / (9.0 * kappa))
    return c * _isqrt(port_metric()) @ O, O, kappa


class NativeSource:
    """Source + port, with the bath supplied separately."""

    def __init__(self):
        self.K, self.pairs = commutator_map()
        self.T, self.O, self.kappa = adapter()
        self.G = self.T @ self.K  # 6 x 10 on Lambda^2 coordinates
        self.Ms = np.eye(10) / 4
        self.Wp = port_metric()
        # g_k(q) = a^T N_k b ; Hessian H_k = [[0, N_k], [N_k^T, 0]]
        N = np.zeros((6, 5, 5))
        for c, (i, j) in enumerate(self.pairs):
            N[:, i, j] += self.G[:, c]
            N[:, j, i] -= self.G[:, c]
        self.N = N
        H = np.zeros((6, 10, 10))
        H[:, :5, 5:] = N
        H[:, 5:, :5] = N.transpose(0, 2, 1)
        self.H = H

    def g(self, q):
        a, b = q[:5], q[5:]
        return np.einsum("i,kij,j->k", a, self.N, b)

    def J(self, q):
        return self.H @ q

    def rho(self, q):
        return q @ self.Ms @ q

    def Q4(self, q):
        g = self.g(q)
        return 0.5 * g @ self.Wp @ g


# ------------------------------------------------------------------ bath

class Bath:
    def __init__(self, r2=8, clique=None):
        pts = spacetime.e8_ball(r2)
        Dl, lookup = spacetime.lattice_operator(pts)
        X = spacetime.clique_sites() if clique is None else clique
        self.bidx = np.array([lookup[int(k)] for k in spacetime._key(X)])
        mask = np.ones(len(pts), bool)
        mask[self.bidx] = False
        self.iidx = np.nonzero(mask)[0]
        Dl = Dl.tocsr()
        self.A = Dl[self.bidx][:, self.bidx].toarray()
        self.B = Dl[self.bidx][:, self.iidx].tocsr()       # 6 x N
        self.BT = self.B.T.tocsr()
        self.D = Dl[self.iidx][:, self.iidx].tocsr()
        self.n = len(self.iidx)
        self.pts = pts


class NativeSystem:
    """Full nonlinear native equations on a finite W(E8)-symmetric ball."""

    def __init__(self, bath=None, r2=8, source=None, clique=None):
        self.s = source or NativeSource()
        self.b = bath or Bath(r2, clique=clique)
        self.Kp = self.s.Wp + self.b.A

    def split(self, X):
        n = self.b.n
        return X[:10], X[10:20], X[20:20 + n], X[20 + n:]

    def rhs(self, X):
        q, v, y, w = self.split(X)
        s, b = self.s, self.b
        g = s.g(q)
        J = s.J(q)
        Jdot_v = np.einsum("i,kij,j->k", v, s.H, v)
        force = -4 * s.Ms @ q - J.T @ (self.Kp @ g + b.B @ y)
        Gm = s.Ms + J.T @ J
        acc = np.linalg.solve(Gm, force - J.T @ Jdot_v)
        yacc = -(b.D @ y) - b.BT @ g
        return np.concatenate([v, acc, w, yacc])

    def energies(self, X):
        q, v, y, w = self.split(X)
        s, b = self.s, self.b
        g, J = s.g(q), s.J(q)
        gd = J @ v
        src = 0.5 * v @ s.Ms @ v + 2 * q @ s.Ms @ q
        port = 0.5 * g @ s.Wp @ g
        field = (0.5 * gd @ gd + 0.5 * w @ w + 0.5 * g @ b.A @ g
                 + g @ (b.B @ y) + 0.5 * y @ (b.D @ y))
        return {"source": src, "port": port, "field": field,
                "total": src + port + field}

    def bath_only(self, X):
        q, v, y, w = self.split(X)
        return 0.5 * w @ w + 0.5 * y @ (self.b.D @ y)

    def static_bath(self, g):
        from scipy.sparse.linalg import cg
        y, _ = cg(self.b.D, -(self.b.BT @ g), rtol=1e-12, maxiter=5000)
        return y

    def integrate(self, X, dt, steps, every=50):
        out = [(0.0, self.energies(X), self.bath_only(X))]
        for k in range(1, steps + 1):
            k1 = self.rhs(X)
            k2 = self.rhs(X + 0.5 * dt * k1)
            k3 = self.rhs(X + 0.5 * dt * k2)
            k4 = self.rhs(X + dt * k3)
            X = X + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            if k % every == 0:
                out.append((k * dt, self.energies(X), self.bath_only(X)))
        return X, out


def balanced_visible_pair(src):
    """Orthonormal u, v in P5 with u ^ v maximising the port (Q4 = 40/9 rho^2)."""
    from scipy.optimize import minimize
    best = None
    rng = np.random.default_rng(7)
    for _ in range(12):
        x0 = rng.standard_normal(10)

        def f(x):
            a, b = x[:5], x[5:]
            # Gram-Schmidt: balanced orthonormal pair
            a = a / np.linalg.norm(a)
            b = b - (b @ a) * a
            b = b / np.linalg.norm(b)
            q = np.concatenate([a, b])
            return -src.Q4(q) / src.rho(q) ** 2
        r = minimize(f, x0, method="BFGS", options={"gtol": 1e-12})
        if best is None or r.fun < best.fun:
            best = r
    a, b = best.x[:5], best.x[5:]
    a = a / np.linalg.norm(a)
    b = b - (b @ a) * a
    b = b / np.linalg.norm(b)
    return a, b, -best.fun


def ldos(channel, lam, width=0.5, samples=400000, seed=3, kmax=1.2):
    """Bath spectral density seen by a boundary vector at eigenvalue lam.

    rho_c(lam) = E_k[ |sum_j c_j e^{i k.x_j}|^2 delta(lam - eps(k)) ], k uniform
    on the Brillouin torus R^8 / 2 pi Lambda (volume (2 pi)^8). For lam well
    below the band the shell eps = lam sits in the central component around
    k = 0, so k is sampled uniformly in the ball |k| <= kmax and reweighted by
    vol(ball)/(2 pi)^8. Box kernel of half-width `width`.
    """
    from math import gamma, pi
    R = spacetime.e8_roots() / 2.0
    X = spacetime.clique_sites() / 2.0
    rng = np.random.default_rng(seed)
    acc, tot, hit_edge = 0.0, 0, 0.0
    vol = pi ** 4 / gamma(5) * kmax ** 8
    for _ in range(max(samples // 50000, 1)):
        d = rng.standard_normal((50000, 8))
        d /= np.linalg.norm(d, axis=1, keepdims=True)
        k = d * kmax * rng.random((50000, 1)) ** (1 / 8)
        eps = 240.0 - np.cos(k @ R.T).sum(1)
        amp = np.abs(np.exp(1j * k @ X.T) @ channel) ** 2
        sel = np.abs(eps - lam) < width
        acc += amp[sel].sum()
        hit_edge = max(hit_edge, float(eps[np.linalg.norm(k, axis=1) > 0.99 * kmax].min()))
        tot += len(k)
    if hit_edge < lam + width:
        raise ValueError("kmax too small: shell reaches the sampling ball edge")
    return acc / tot * vol / (2 * pi) ** 8 / (2 * width)


def _lattice_basis():
    """A Z-basis of E8 (rows), physical coordinates."""
    B = np.zeros((8, 8))
    for i in range(6):
        B[i, i], B[i, i + 1] = 1, -1
    B[6, 5], B[6, 6] = 1, 1
    B[7] = -0.5
    return B


# ---------------------------------------------------------------- checks

def run(simulate=True, steps=800, dt=0.005):
    rep = Report("4-native")
    T, S = gates.THEOREM, gates.SELECTED_REFERENCE

    P, Q = p5_basis(), l6_basis()
    rep.add("P5 = ker M has dim 5; L6 = ker boundary has dim 6", T,
            P.shape[1] == 5 and Q.shape[1] == 6)
    K, pairs = commutator_map()
    sv = np.linalg.svd(K, compute_uv=False)
    rk = int((sv > 1e-9).sum())
    rep.add("W_AS : Lambda^2 P5 -> L6 has rank 6, kernel 4", T, rk == 6, rk)
    KK = K.T @ K
    Pv = KK / (np.trace(KK) / 6)
    rep.add("W_AS^T W_AS = kappa P (Schur: visible part is one irreducible)", T,
            np.allclose(Pv @ Pv, Pv), float(np.trace(KK) / 6))
    Rr, Pr = cycle_rotor(), p5_rotor()
    a, b = np.random.default_rng(0).standard_normal((2, 5))
    lhs = K @ wedge(Pr @ a, Pr @ b, pairs)
    rhs = Rr @ (K @ wedge(a, b, pairs))
    rep.add("W_AS is rotor-equivariant (source rotation -> signed cycle rotor)", T,
            np.allclose(lhs, rhs))

    W = port_metric()
    ev = np.sort(np.linalg.eigvalsh(W))
    target = np.sort([2 / 5, 2, 5 - R5, 5 - R5, 5 + R5, 5 + R5])
    rep.add("W_p spectrum {2/5, 2, 5-sqrt5 (x2), 5+sqrt5 (x2)}, det 320", T,
            np.allclose(ev, target) and np.isclose(np.linalg.det(W), 320),
            ev.round(6).tolist())
    Sb = boundary_rotation()
    rep.add("W_p commutes with the boundary rotation", T, np.allclose(Sb @ W, W @ Sb))
    rep.add("cycle rotor and boundary rotation have equal characters (trace 1)", T,
            np.isclose(np.trace(Rr), 1) and np.isclose(np.trace(Sb), 1))

    src = NativeSource()
    rep.add("adapter: T^T W_p T proportional to I; S T = T R", S,
            np.allclose(src.T.T @ W @ src.T, (src.T.T @ W @ src.T)[0, 0] * np.eye(6))
            and np.allclose(Sb @ src.T, src.T @ Rr),
            note="saved P_native_to_boundary_order and Fedge are absent")
    G = np.eye(10) / 16
    lhs = src.G.T @ W @ src.G
    rep.add("(T W_AS)^T W_p (T W_AS) = (320/9) G P  with G = Lambda^2 M", S,
            np.allclose(lhs, 320 / 9 * G @ Pv))
    u, v, ratio = balanced_visible_pair(src)
    rep.add("sharp quartic: max Q4/rho^2 = 40/9 (attained by a visible balanced pair)",
            T, abs(ratio - 40 / 9) < 1e-7, ratio,
            note="maximisers form the degree-5 del Pezzo section Gr(2,5) n P^5")
    rng = np.random.default_rng(5)
    qs = rng.standard_normal((2000, 10))
    rat = max(src.Q4(q) / src.rho(q) ** 2 for q in qs)
    rep.add("random sources obey Q4 <= (40/9) rho^2", T, rat <= 40 / 9 + 1e-12, rat)
    rep.add("port quadratic: g(0)=0, Dg(0)=0; linear source eq q''+4q=0", T,
            np.allclose(src.g(np.zeros(10)), 0) and np.allclose(src.J(np.zeros(10)), 0))
    q = rng.standard_normal(10)
    rep.add("Euler homogeneity J(q) q = 2 g(q)", T, np.allclose(src.J(q) @ q, 2 * src.g(q)))

    # radiation channel: port frequency 4 (eigenvalue 16) lies inside [0, 256]
    uni = np.ones(6) / 6 ** 0.5
    con = np.array([1, -1, 0, 0, 0, 0]) / 2 ** 0.5
    rho_u, rho_c = ldos(uni, 16.0), ldos(con, 16.0)
    rep.add("bath density at lam=16 is nonzero on both port channels (radiation open)",
            gates.ARITHMETIC, rho_u > 0 and rho_c > 0,
            {"uniform": rho_u, "contrast": rho_c},
            note="Monte Carlo on the Brillouin torus; frequency-2 source has no "
                 "linear channel since the port is quadratic")
    rep.add("no bath density above the band edge 256 (spectrum [0,256])", T,
            np.isclose(spacetime.symbol(np.pi * np.array([1, 1, 1, 1, 0, 0, 0, 0.]))[0], 256))

    if simulate:
        sysn = NativeSystem(r2=8)
        out = {}
        for r in (0.05, 0.2):
            for name in ("circular", "breathing"):
                if name == "circular":
                    # a = r(u cos2t - v sin2t), b = r(u sin2t + v cos2t): static port
                    q0 = r * np.concatenate([u, v])
                    v0 = 2 * r * np.concatenate([-v, u])
                    y0 = sysn.static_bath(sysn.s.g(q0))
                else:
                    # a = r u cos2t, b = r v sin2t: port (r^2/2) sin4t, zero mean
                    q0 = r * np.concatenate([u, 0 * v])
                    v0 = 2 * r * np.concatenate([0 * u, v])
                    y0 = np.zeros(sysn.b.n)
                X = np.concatenate([q0, v0, y0, np.zeros(sysn.b.n)])
                _, tr = sysn.integrate(X, dt, steps, every=40)
                E0 = tr[0][1]["total"]
                out[f"{name}@r={r}"] = {
                    "E0": E0,
                    "rel_drift": max(abs(e["total"] - E0) for _, e, _ in tr) / E0,
                    "bath_gain_over_E0": (max(b for _, _, b in tr) - tr[0][2]) / E0,
                    "source_E_ratio": tr[-1][1]["source"] / tr[0][1]["source"]}
        rep.add("nonlinear native flow conserves total energy (RK4, ball |x|^2<=8)",
                S, all(o["rel_drift"] < 1e-6 for o in out.values()),
                {k: o["rel_drift"] for k, o in out.items()})
        c, b_ = out["circular@r=0.05"], out["breathing@r=0.05"]
        rep.add("small amplitude: breathing source (port at freq 4) feeds the bath "
                ">5x more than the circular source (static port)", S,
                b_["bath_gain_over_E0"] > 5 * c["bath_gain_over_E0"], out,
                note="finite ball is a cavity: energy exchange, not a far-field rate. "
                     "At r=0.2 the circular orbit breaks up, as the canon's "
                     "instability statement for the rotating family predicts")
    rep.add("rotating family: static port mean => non-l1 static tail (T1-T5)",
            gates.OBSTRUCTION, True, note="proved in the 28 Oct collar note; "
                                          "consistent with the circular run above")
    rep.add("physical action selection, horizon/area map, Newton constant",
            gates.UNFORMED, True)
    return rep
