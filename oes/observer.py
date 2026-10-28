"""Layer 5. Observers: what a readout of the carrier can and cannot see.

The canon's observer statement (consolidated note, sec 7) is
observability/controllability: the hidden controllable sector
H_hidden(T) = Ran K_T  n  ker O_T. Here it is computed for the carrier
x = (psi, psi'), x' = A x, A = [[0, I], [-D^2, 0]], under named readouts.

Two structural facts drive every number below.

* D^2 = diag(M M^T, M^T M) is block diagonal, so the vertex and edge systems
  never exchange energy. D intertwines them (a supersymmetric pair); the
  Witten index Tr gamma e^{-beta D^2} = 0 - 5 = -5 for every beta.
* spec D^2 has three distinct values, so a single scalar readout sees at most
  2 x 3 = 6 of the 30 phase dimensions. This is the canon's Firefly remark:
  a statistic that sees one frequency line cannot select inside it.

The original Sakshin witness operator is UNFORMED and is not replaced here.
"""

import numpy as np

from . import carrier, gates
from .record import Report


def system_matrix():
    K = np.array(carrier.D2(), float)
    n = len(K)
    A = np.zeros((2 * n, 2 * n))
    A[:n, n:] = np.eye(n)
    A[n:, :n] = -K
    return A


def _orth_rows(X, tol=1e-9):
    if X.size == 0:
        return X
    _, s, Vt = np.linalg.svd(X, full_matrices=False)
    return Vt[s > tol * max(1.0, s.max())]


def kalman_obs(A, C):
    """Orthonormal rows spanning the observable subspace (iterated Krylov)."""
    V = _orth_rows(C)
    while True:
        W = _orth_rows(np.vstack([V, V @ A]))
        if len(W) == len(V):
            return W
        V = W


def kalman_ctrl(A, B):
    """Orthonormal columns spanning the reachable subspace."""
    return kalman_obs(A.T, B.T).T


def rank(X, tol=1e-8):
    s = np.linalg.svd(X, compute_uv=False)
    return int((s > tol * max(1.0, s.max())).sum())


def subspace_intersection_dim(U, V, tol=1e-8):
    """dim(col U n col V)."""
    ru, rv = rank(U, tol), rank(V, tol)
    return ru + rv - rank(np.hstack([U, V]), tol)


def null_space(X, tol=1e-8):
    _, s, Vt = np.linalg.svd(X)
    r = int((s > tol * max(1.0, s.max())).sum())
    return Vt[r:].T


def readouts():
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    Z = np.zeros((15, 15))
    I = np.eye(15)
    pos = lambda S: np.hstack([I[S], Z[S]])
    return {
        "vertex positions": pos(list(range(5))),
        "edge positions": pos(list(range(5, 15))),
        "Dirac image D psi": np.hstack([D, Z]),
        "all positions": pos(list(range(15))),
        "one vertex": pos([0]),
        "one edge": pos([5]),
        "vertex sum (uniform statistic)": np.hstack([np.r_[np.ones(5), np.zeros(10)][None], Z[:1]]),
    }


def run():
    rep = Report("5-observer")
    T = gates.THEOREM
    A = system_matrix()
    n = len(A)
    ranks = {name: rank(kalman_obs(A, C)) for name, C in readouts().items()}
    expect = {"vertex positions": 10, "edge positions": 20, "Dirac image D psi": 20,
              "all positions": 30, "one vertex": 4, "one edge": 6,
              "vertex sum (uniform statistic)": 2}
    rep.add("observable dimensions of named readouts (of 30)", T, ranks == expect, ranks)
    rep.add("vertex and edge systems decouple: D^2 block diagonal", T,
            np.allclose(np.array(carrier.D2(), float)[:5, 5:], 0))
    g = np.array(carrier.grading(), float)
    K = np.array(carrier.D2(), float)
    w = [np.trace(g @ _expm(-b * K)) for b in (0.1, 1.0, 7.0)]
    rep.add("Witten index Tr gamma e^{-beta D^2} = -5 for all beta", T,
            np.allclose(w, -5), w)
    rep.add("a scalar readout sees at most 6 phase dimensions (3 distinct lines)", T,
            max(r for k, r in ranks.items() if k.startswith(("one", "vertex sum"))) <= 6)

    # hidden controllable sectors: edge actuators, various observers
    Bedge = np.vstack([np.zeros((15, 10)), np.eye(15)[:, 5:]])
    Bvert = np.vstack([np.zeros((15, 5)), np.eye(15)[:, :5]])
    out = {}
    for bname, B in (("edge force", Bedge), ("vertex force", Bvert)):
        Kc = kalman_ctrl(A, B)
        for oname in ("vertex positions", "Dirac image D psi", "edge positions"):
            ker = null_space(kalman_obs(A, readouts()[oname]))
            dim = subspace_intersection_dim(Kc, ker) if ker.size else 0
            out[f"{bname} | {oname}"] = dim
    exp_h = {"edge force | vertex positions": 20, "edge force | Dirac image D psi": 10,
             "edge force | edge positions": 0, "vertex force | vertex positions": 0,
             "vertex force | Dirac image D psi": 0, "vertex force | edge positions": 10}
    rep.add("hidden controllable sector dim(Ran K n ker O)", T, out == exp_h, out,
            note="the 5 kernel modes (cycle drift) are reachable by edge force and "
                 "invisible to D psi: the dark sector of the carrier")

    # finite-time Gramian agrees with Kalman rank
    C = readouts()["Dirac image D psi"]
    ts = np.linspace(0, 6, 601)
    Wo = sum(_expm(A.T * t) @ C.T @ C @ _expm(A * t) for t in ts) * (ts[1] - ts[0])
    rep.add("observability Gramian W_o(6) of D psi has rank 20", T, rank(Wo, 1e-9) == 20,
            rank(Wo, 1e-9))
    rep.add("original Sakshin / 237-dim fiber observer", gates.UNFORMED, True)
    return rep


def _expm(X):
    from scipy.linalg import expm
    return expm(X)
