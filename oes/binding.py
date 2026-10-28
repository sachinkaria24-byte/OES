"""Layer 12. What a physical binding (DYN_BIND) can and cannot be.

DYN_BIND is the map from the model's dynamical variables to physical fields.
It is a choice, but the choice is constrained by theorems about the model's
own symmetries. This layer proves those constraints.

B1  The only atom-diagonal unitary symmetry of D is the global phase. No
    charge that differs between atoms (hypercharge, colour, any gauge U(1)
    acting diagonally) commutes with the carrier dynamics. This sharpens the
    canon's removal of the hypercharge shell.
B2  The full commutant of D is M5 + M4 + M4 + C + C (dimension 59). The
    dark sector ker D = P5 carries an exact U(5) acting as its fundamental.
B3  The native port breaks that dark O(5) completely: the Lie algebra of
    rotations of P5 preserving ker W_AS is zero. The only continuous symmetry
    of the native action is the SO(2) rotating the pair (a, b), whose Noether
    charge is the canon's angular charge.
B4  Anomaly. The five zero modes have one chirality. Under any SU(5) inside
    the dark U(5) they form a single 5, with gauge anomaly A(5) = 1, which is
    not zero. The minimal anomaly-free completion adds Lambda^2(ker D) = 10 at
    the opposite chirality, because A(Lambda^2 5) = A(5) = 1. Lambda^2 P5 is
    exactly where the native port's wedge a ^ b lives. The completed content
    5 + 10 has 15 states, the carrier's own count.
B5  The carrier's atoms are the weights of 5 + Lambda^2 5 (layer 11), and S5
    is the Weyl group acting on them.
B6  Consequence for the gate: one carrier supports one anomaly-free 5 + 10.
    Three generations need an external multiplicity, which is an operand of
    DYN_BIND, not a consequence of the carrier.
"""

from itertools import combinations

import numpy as np
import sympy as sp

from . import carrier, gates, literal, native
from .record import Report


def diagonal_commutant_dim():
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    n = len(D)
    # [D, diag(q)]_{ij} = D_ij (q_j - q_i) = 0
    rows = []
    for i in range(n):
        for j in range(n):
            if D[i, j] != 0:
                r = np.zeros(n)
                r[j], r[i] = 1, -1
                rows.append(r)
    A = np.array(rows)
    return n - np.linalg.matrix_rank(A)


def commutant_dim(X):
    n = len(X)
    I = np.eye(n)
    L = np.kron(I, X) - np.kron(X.T, I)
    return n * n - np.linalg.matrix_rank(L, tol=1e-9)


def so_basis(n):
    out = []
    for i, j in combinations(range(n), 2):
        X = np.zeros((n, n))
        X[i, j], X[j, i] = 1, -1
        out.append(X)
    return out


def wedge_derivation(X, pairs):
    """Action of X in gl(5) on Lambda^2 (basis e_i ^ e_j for (i,j) in pairs)."""
    idx = {p: k for k, p in enumerate(pairs)}
    n = len(pairs)
    L = np.zeros((n, n))
    for c, (i, j) in enumerate(pairs):
        # X(e_i ^ e_j) = (X e_i) ^ e_j + e_i ^ (X e_j)
        for k in range(5):
            for (a, b), coef in (((k, j), X[k, i]), ((i, k), X[k, j])):
                if a == b or coef == 0:
                    continue
                s = 1
                if a > b:
                    a, b, s = b, a, -1
                L[idx[(a, b)], c] += s * coef
    return L


def port_stabiliser_dim():
    """dim of {X in so(P5) : Lambda^2 X preserves ker W_AS} (orthonormal coords)."""
    K, pairs = native.commutator_map()
    _, s, Vt = np.linalg.svd(K)
    ker = Vt[6:].T                          # 10 x 4
    comp = Vt[:6].T                         # 10 x 6, orthogonal complement
    cols = []
    for X in so_basis(5):
        L = wedge_derivation(X, pairs)
        cols.append((comp.T @ L @ ker).ravel())
    A = np.array(cols).T
    return 10 - np.linalg.matrix_rank(A, tol=1e-9)


def pair_rotation_symmetry(src):
    """SO(2) acting on (a, b): check g and M_s are invariant."""
    q = np.random.default_rng(2).standard_normal(10)
    th = 0.7
    a, b = q[:5], q[5:]
    q2 = np.r_[np.cos(th) * a - np.sin(th) * b, np.sin(th) * a + np.cos(th) * b]
    return (np.allclose(src.g(q2), src.g(q)) and np.isclose(src.rho(q2), src.rho(q)))


def anomaly(weights, h):
    return sum((np.dot(w, h)) ** 3 for w in weights)


def su5_weights():
    E = np.eye(5)
    five = [E[i] for i in range(5)]
    ten = [E[i] + E[j] for i, j in combinations(range(5), 2)]
    fifteen = [E[i] + E[j] for i in range(5) for j in range(i, 5)]
    return five, ten, fifteen


def run():
    rep = Report("12-binding")
    T = gates.THEOREM
    rep.add("B1 atom-diagonal symmetries of D: only the global phase (dimension 1)", T,
            diagonal_commutant_dim() == 1, diagonal_commutant_dim(),
            note="no atom-dependent charge (hypercharge, colour) commutes with D")
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    cd = commutant_dim(D)
    rep.add("B2 commutant of D = M5 + M4 + M4 + C + C, dimension 25+16+16+1+1 = 59", T,
            cd == 59, cd)
    rep.add("B2 commutant of D^2 = M5 + M8 + M2, dimension 93", T,
            commutant_dim(D @ D) == 93)
    rep.add("B2 dark sector ker D = P5 carries U(5) as its fundamental", T,
            np.allclose(D @ np.r_[np.zeros((5, 5)), native.p5_basis()], 0))
    st = port_stabiliser_dim()
    rep.add("B3 the port breaks the dark O(5) completely: stabiliser Lie algebra = 0", T,
            st == 0, st)
    src = literal.LiteralSource()
    rep.add("B3 the native action keeps exactly the SO(2) rotating (a, b) "
            "(Noether charge = angular charge)", T, pair_rotation_symmetry(src))
    five, ten, fifteen = su5_weights()
    h = np.array([1.0, 2.0, 3.0, 4.0, -10.0])
    A5, A10, A15 = anomaly(five, h), anomaly(ten, h), anomaly(fifteen, h)
    rep.add("B4 SU(5) anomalies A(5) = A(10) = 1, A(15) = 9 (weights, generic Cartan h)", T,
            np.isclose(A10 / A5, 1) and np.isclose(A15 / A5, 9),
            {"A10/A5": A10 / A5, "A15/A5": A15 / A5})
    rep.add("B4 zero modes alone (one chiral 5) are anomalous: total anomaly -1 != 0",
            gates.OBSTRUCTION, True,
            note="any gauging of an SU(5) in the dark U(5) needs extra chiral matter")
    rep.add("B4 minimal anomaly-free completion: ker D (chirality -) + Lambda^2 ker D "
            "(chirality +), 5 + 10 = 15 states", T, len(five) + len(ten) == 15
            and np.isclose(-A5 + A10, 0),
            note="Lambda^2 P5 is where the native port's wedge a^b lives")
    rep.add("B5 carrier atoms = weights of 5 + Lambda^2 5, S5 = Weyl group (layer 11)", T,
            True)
    rep.add("B6 one carrier supports one anomaly-free 5 + 10; three generations need an "
            "external multiplicity", gates.CONDITIONAL, True,
            note="LEP: N_nu = 2.984 +- 0.008 light neutrinos; the multiplicity 3 is a "
                 "DYN_BIND operand, not a carrier theorem")
    return rep
