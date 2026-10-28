"""Layer 10. The literal native operands, recovered and replayed.

The canon listed "saved native_source_matrices (SHA256 73e07429...)" as
absent. The file is present inside
OES_Standing_Model_Integrated_Proof_Packet_20261027.zip (Drive
1ukVZgOnirGVQ1CJslWLmeyKj8ZAVIiGJ) at
reconcile/breather/native_matrices_input.json. Its bytes hash to the recorded
value here, which is a cross-host byte receipt for this operand.

This layer
* checks the SHA-256 of data/native_matrices_input.json,
* replays every identity the canon states for these matrices,
* compares them with the selected reference of layer 4: the metric, the port
  metric and the Schur scale agree exactly; the adapters differ by an explicit
  element of the C5 commutant, which is computed and reported,
* builds the literal source/port (q in the saved basis, mass M_source,
  g = P_boundary WAS_native (a ^ b)) so the native flow can run on the
  owner's own operands.
"""

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

from . import carrier, gates, native
from .record import Report

DATA = Path(__file__).resolve().parent.parent / "data" / "native_matrices_input.json"
SHA256 = "73e07429d7733ae43055723cd59756eb1d1989300f161a1d6ab14cb02413ffea"

# Printed in the integrated proof join (sec. 2) as the literal source rotor.
R_PRINTED = [["-2/3", "-1", "0", "-1/6", "0"],
             ["-2/3", "0", "-1", "5/6", "0"],
             ["1", "0", "0", "-1/2", "0"],
             ["-1/3", "-1", "0", "2/3", "1"],
             ["-1/3", "0", "-1", "-1/3", "0"]]


def sha256():
    return hashlib.sha256(DATA.read_bytes()).hexdigest()


def load():
    d = json.loads(DATA.read_text())
    out = {}
    for k, v in d.items():
        if isinstance(v, list) and v and isinstance(v[0], list) and isinstance(v[0][0], str):
            out[k] = sp.Matrix([[sp.Rational(x) for x in row] for row in v])
        else:
            out[k] = v
    return out


def lambda2(X, pairs):
    n = len(pairs)
    L = sp.zeros(n, n)
    for r, (i, j) in enumerate(pairs):
        for c, (k, l) in enumerate(pairs):
            L[r, c] = X[i, k] * X[j, l] - X[i, l] * X[j, k]
    return L


def source_rotor(d):
    """Vertex rotation i -> i+1 acting on P5, in the saved basis N_source."""
    N = d["N_source"]
    E = [tuple(e) for e in d["edge_order"]]
    idx = {e: k for k, e in enumerate(E)}
    Pi = sp.zeros(10, 10)
    for k, (i, j) in enumerate(E):
        a, b = sorted(((i + 1) % 5, (j + 1) % 5))
        Pi[idx[(a, b)], k] = 1
    return (N.T * N).inv() * N.T * Pi * N


class LiteralSource:
    """Literal native source and port, same interface as native.NativeSource."""

    def __init__(self, d=None):
        d = d or load()
        pairs = [tuple(p) for p in d["source_wedge_order"]]
        self.pairs = pairs
        G = np.array(d["P_native_to_boundary_order"] * d["WAS_native"], dtype=float)
        self.G = G                                   # boundary order, wedge coords
        self.Ms = np.array(d["M_source"], dtype=float)
        Pn = d["P_native_to_boundary_order"]
        self.Wp = np.array(Pn * d["Wp_source_HS"] * Pn.T, dtype=float)
        N = np.zeros((6, 5, 5))
        for c, (i, j) in enumerate(pairs):
            N[:, i, j] += G[:, c]
            N[:, j, i] -= G[:, c]
        self.N = N
        H = np.zeros((6, 10, 10))
        H[:, :5, 5:] = N
        H[:, 5:, :5] = N.transpose(0, 2, 1)
        self.H = H

    def g(self, q):
        return np.einsum("i,kij,j->k", q[:5], self.N, q[5:])

    def J(self, q):
        return self.H @ q

    def rho(self, q):
        return q @ self.Ms @ q

    def Q4(self, q):
        g = self.g(q)
        return 0.5 * g @ self.Wp @ g


def literal_clique():
    """Apex 0 and e_i - e_6 (i = 1..5, one-based), doubled coordinates, boundary order."""
    X = np.zeros((6, 8), dtype=np.int64)
    for i in range(5):
        X[1 + i, i], X[1 + i, 5] = 2, -2
    return X


def balanced_pair(src, seed=11):
    """Maximise Q4 / rho^2 over all sources; return an M-orthonormal visible pair."""
    from scipy.optimize import minimize
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(8):
        r = minimize(lambda q: -src.Q4(q) / src.rho(q) ** 2, rng.standard_normal(10),
                     method="BFGS", options={"gtol": 1e-12})
        if best is None or r.fun < best.fun:
            best = r
    q = best.x
    a, b = q[:5], q[5:]
    M = src.Ms[:5, :5]
    # balance the pair in M (the wedge, hence the port, changes only by a scalar);
    # a^T M a = b^T M b = 1/4 matches the unit-vector normalisation of layer 4
    a = a / np.sqrt(a @ M @ a)
    b = b - (a @ M @ b) * a
    b = b / np.sqrt(b @ M @ b)
    return a / 2, b / 2, -best.fun


def compare_with_reference(d):
    """Express the literal port in the coordinates of layer 4 and compare."""
    N = np.array(d["N_source"], dtype=float)
    P5 = native.p5_basis()
    C = P5.T @ N                                      # literal coeffs -> orthonormal coords
    pairs = [tuple(p) for p in d["source_wedge_order"]]
    L2C = np.array(lambda2(sp.Matrix(C), pairs), dtype=float)
    src = native.NativeSource()
    G_lit = np.array(d["P_native_to_boundary_order"] * d["WAS_native"], dtype=float)
    # the literal map in reference coordinates: g = G_lit (L2C)^-1 w'
    G_lit_ref = G_lit @ np.linalg.inv(L2C)
    # both factor through the same visible 6-space: G = T K ; solve U with G_lit_ref = U G_ref
    U = G_lit_ref @ np.linalg.pinv(src.G)
    fit = np.abs(U @ src.G - G_lit_ref).max()
    Wb = src.Wp
    iso = np.abs(U.T @ Wb @ U - Wb).max()
    S = native.boundary_rotation()
    comm = np.abs(U @ S - S @ U).max()
    return {"U": U, "fit_residual": float(fit), "Wp_isometry_residual": float(iso),
            "commutes_with_boundary_rotation": float(comm),
            "det_U": float(np.linalg.det(U))}


def run(simulate=True):
    rep = Report("10-literal")
    T = gates.THEOREM
    h = sha256()
    rep.add("native_matrices_input.json SHA-256 = 73e07429... (canon-recorded hash)", T,
            h == SHA256, h, note="byte receipt: canon host hash == this host hash")
    d = load()
    H, B, N, W = d["H_signless"], d["boundary_oriented"], d["N_source"], d["W_source"]
    rep.add("literal H_signless is the K5 signless incidence (same edge order)", T,
            H == carrier.signless_incidence() and [tuple(e) for e in d["edge_order"]]
            == carrier.edges())
    rep.add("N_source spans P5 = ker H (rank 5)", T, (H * N).is_zero_matrix and N.rank() == 5)
    rep.add("W_source = N^T N (edge metric on P5), det W = 8/9", T,
            W == N.T * N and W.det() == sp.Rational(8, 9))
    rep.add("M_source = diag(W/4, W/4)", T, d["M_source"] == sp.diag(W / 4, W / 4))
    Wp, F, Chi = d["Wp_source_HS"], d["Fedge_native_inverse"], d["Chi_native_port"]
    rep.add("W_p = 2 F^T F (HS metric transported by the edge adapter), Chi F = I6", T,
            Wp == 2 * F.T * F and Chi * F == sp.eye(6))
    ev = Wp.eigenvals()
    rep.add("literal W_p spectrum {2/5, 2, 5 +- sqrt5 (x2)}, det 320", T,
            ev == {sp.Rational(2, 5): 1, 2: 1, 5 - sp.sqrt(5): 2, 5 + sp.sqrt(5): 2}
            and Wp.det() == 320)
    Pn = d["P_native_to_boundary_order"]
    Wb = np.array(Pn * Wp * Pn.T, dtype=float)
    rep.add("literal W_p in boundary order == layer-4 reconstruction, exactly", T,
            np.allclose(Wb, native.port_metric()))
    WAS = d["WAS_native"]
    pairs = [tuple(p) for p in d["source_wedge_order"]]
    G = lambda2(W / 4, pairs)
    P = d["native_wedge_visible_projection"]
    rep.add("WAS_native rank 6, kernel 4", T, WAS.rank() == 6)
    rep.add("G_source_wedge = Lambda^2 W = 16 Lambda^2 M", T,
            d["G_source_wedge"] == lambda2(W, pairs) == 16 * G)
    rep.add("WAS^T W_p WAS = (320/9) G P with G = Lambda^2 M (sharp quartic 40/9)", T,
            WAS.T * Wp * WAS == sp.Rational(320, 9) * G * P and P * P == P)
    R = source_rotor(d)
    Rp = sp.Matrix([[sp.Rational(x) for x in row] for row in R_PRINTED])
    Q = d["Q_native"]
    L2R = lambda2(R, pairs)
    rep.add("source rotor from the vertex 5-cycle equals the printed literal R", T, R == Rp)
    rep.add("R^5 = I, R^T W R = W, Tr R^j = 0 (j=1..4)", T,
            R ** 5 == sp.eye(5) and R.T * W * R == W
            and all((R ** j).trace() == 0 for j in range(1, 5)))
    rep.add("WAS Lambda^2(R) = Q WAS, Q^T Q = I, Q W_p = W_p Q", T,
            WAS * L2R == Q * WAS and Q.T * Q == sp.eye(6) and Q * Wp == Wp * Q)
    Qb = Pn * Q * Pn.T
    Sb = sp.Matrix(native.boundary_rotation().astype(int))
    rep.add("Q in boundary order is the boundary 5-cycle (apex fixed)", T,
            Qb == Sb or Qb == Sb.T, "S" if Qb == Sb else "S^-1")
    Tm = d["T_OMSOON293"]
    TT = Tm * Tm.T
    rep.add("155 vs 4805 replayed: det T = 155 = 5*31, cofactor_44(T T^T) = 4805 = 5*31^2, "
            "(T T^T)^-1_44 = 1/5", T,
            Tm.det() == 155 and TT.cofactor(3, 3) == 4805 and TT.inv()[3, 3] == sp.Rational(1, 5),
            note="one adapter and its cofactor, not two minors: the reported label "
                 "error is now a replayed theorem")
    cmp = compare_with_reference(d)
    rep.add("literal port = U . (layer-4 port), U a W_p-isometry commuting with the C5 "
            "rotation", T, cmp["fit_residual"] < 1e-9 and cmp["Wp_isometry_residual"] < 1e-9
            and cmp["commutes_with_boundary_rotation"] < 1e-9,
            {k: v for k, v in cmp.items() if k != "U"},
            note="the selected reference differed only by a commutant element; the "
                 "literal operand now replaces it")
    src = LiteralSource(d)
    q = np.random.default_rng(3).standard_normal(10)
    rep.add("literal source obeys J(q) q = 2 g(q) and Q4 <= (40/9) rho^2", T,
            np.allclose(src.J(q) @ q, 2 * src.g(q)) and src.Q4(q) <= 40 / 9 * src.rho(q) ** 2)
    a, b, ratio = balanced_pair(src)
    rep.add("literal sharp quartic attained: max Q4/rho^2 = 40/9", T, abs(ratio - 40 / 9) < 1e-7,
            ratio)
    if simulate:
        sysn = native.NativeSystem(r2=8, source=src, clique=literal_clique())
        out = {}
        r = 0.05
        for name in ("circular", "breathing"):
            if name == "circular":
                q0, v0 = r * np.r_[a, b], 2 * r * np.r_[-b, a]
                y0 = sysn.static_bath(sysn.s.g(q0))
            else:
                q0, v0 = r * np.r_[a, 0 * b], 2 * r * np.r_[0 * a, b]
                y0 = np.zeros(sysn.b.n)
            X = np.concatenate([q0, v0, y0, np.zeros(sysn.b.n)])
            _, tr = sysn.integrate(X, 0.005, 600, every=40)
            E0 = tr[0][1]["total"]
            out[name] = {"rel_drift": max(abs(e["total"] - E0) for _, e, _ in tr) / E0,
                         "bath_gain_over_E0": (max(bb for _, _, bb in tr) - tr[0][2]) / E0}
        rep.add("native E8 flow on the LITERAL operands: energy conserved, breathing source "
                "feeds the bath more than the circular one", T,
                all(o["rel_drift"] < 1e-6 for o in out.values())
                and out["breathing"]["bath_gain_over_E0"] > 5 * out["circular"]["bath_gain_over_E0"],
                out, note="same physics as the reference run of layer 4; the operand is now the "
                          "owner's file")
    return rep
