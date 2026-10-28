"""Layer 6. Gravity: what is intrinsic, and what needs an external input.

The canon's position (28 Oct): "Physical selection and gravitational
normalization remain external and ABSENT." "None of this is Einstein
gravity." The Wald coefficient is absent. This module respects that split.

(A) Intrinsic, status ARITHMETIC: discrete Ricci curvature (Lin-Lu-Yau, via
    optimal transport) of the graphs the carrier already builds. K5 has
    curvature 5/4; the Petersen graph and the E8 root-lattice graph are flat
    (curvature 0). These are curvatures of discrete metric spaces, not
    solutions of Einstein's equations.

(B) Conditional, status CONDITIONAL: the spectral action of the product
    geometry M4 x F, with F the carrier triple, D = D_M (x) 1 + gamma5 (x) m D_F.
    Inputs the canon does not supply: a closed spin 4-manifold M4, a cutoff
    function f with moments F0 = f(0), F1 = int f, F2 = int x f, a cutoff L and
    a mass scale m for D_F. With them, the carrier traces 15, 40, 200 fix

        Tr f(D^2/L^2) ~ (1/16 pi^2) int sqrt(g) [ 60 F2 L^4
                         - (160 m^2 + 5 R) F1 L^2 + (400 m^4 + 40 m^2 R / 3) F0 ]
                         + (curvature-squared terms, omitted)

    so that   1/(16 pi G) = 5 F1 L^2 / (16 pi^2),
              Lambda_cc  = 6 (F2/F1) L^2 - 16 m^2 + 40 (F0/F1) m^4 / L^2.

    Lambda_cc G can be given any real value by the free ratio F2/F1. That is
    the nonidentifiability the canon records, made explicit.
"""

import numpy as np
import sympy as sp

from . import carrier, gates, spacetime
from .record import Report


# --------------------------------------------------------- (A) intrinsic

def lly_curvature(dist, nbrs, x, y):
    """Lin-Lu-Yau curvature of edge xy: 2 * kappa_{1/2} (Bourne et al.)."""
    from scipy.optimize import linprog
    mx = {x: 0.5}
    for z in nbrs[x]:
        mx[z] = mx.get(z, 0) + 0.5 / len(nbrs[x])
    my = {y: 0.5}
    for z in nbrs[y]:
        my[z] = my.get(z, 0) + 0.5 / len(nbrs[y])
    S, Tt = list(mx), list(my)
    c = np.array([dist(s, t) for s in S for t in Tt], float)
    nS, nT = len(S), len(Tt)
    Aeq = np.zeros((nS + nT, nS * nT))
    for i in range(nS):
        Aeq[i, i * nT:(i + 1) * nT] = 1
    for j in range(nT):
        Aeq[nS + j, j::nT] = 1
    beq = np.r_[[mx[s] for s in S], [my[t] for t in Tt]]
    res = linprog(c, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    W = res.fun
    return 2 * (1 - W)


def graph_from_adj(A):
    A = np.array(A, int)
    n = len(A)
    nbrs = {i: list(np.nonzero(A[i])[0]) for i in range(n)}
    D = np.full((n, n), 99)
    for s in range(n):
        D[s, s] = 0
        q = [s]
        for u in q:
            for w in nbrs[u]:
                if D[s, w] == 99:
                    D[s, w] = D[s, u] + 1
                    q.append(w)
    return nbrs, (lambda a, b: D[a, b])


def e8_edge_curvature():
    """LLY curvature of the edge (0, alpha) in the E8 root-lattice graph."""
    R = spacetime.e8_roots()
    two = {tuple(r) for r in R}
    sums = {tuple(a + b) for a in R for b in R}

    def dist(a, b):
        d = tuple(np.subtract(a, b))
        if not any(d):
            return 0
        if d in two:
            return 1
        if d in sums:
            return 2
        return 3
    x = (0,) * 8
    y = tuple(R[0])
    nbrs = {x: [tuple(r) for r in R], y: [tuple(np.add(y, r)) for r in R]}
    return lly_curvature(dist, nbrs, x, y)


# ------------------------------------------------------- (B) conditional

def product_heat_coefficients():
    """Small-t expansion of (4 - tR/3) * Tr exp(-t m^2 D_F^2) to O(t^2)."""
    t, R, m = sp.symbols("t R m", positive=True)
    ZF = sum(mult * sp.exp(-t * m ** 2 * lam) for lam, mult in {0: 5, 3: 8, 8: 2}.items())
    expr = sp.series((4 - t * R / 3) * ZF, t, 0, 3).removeO()
    return sp.Poly(sp.expand(expr), t).all_coeffs()[::-1], (t, R, m)


def newton_and_vacuum(F0, F1, F2, L, m):
    G = np.pi / (5 * F1 * L ** 2)
    Lcc = 6 * (F2 / F1) * L ** 2 - 16 * m ** 2 + 40 * (F0 / F1) * m ** 4 / L ** 2
    return G, Lcc


def tuned_F2(F0, F1, L, m, target_Lcc=0.0):
    """The F2 that gives a chosen Lambda_cc: the free knob."""
    return F1 * (target_Lcc + 16 * m ** 2 - 40 * (F0 / F1) * m ** 4 / L ** 2) / (6 * L ** 2)


def run():
    rep = Report("6-gravity")
    Ar = gates.ARITHMETIC
    nb, d = graph_from_adj(np.ones((5, 5)) - np.eye(5))
    k5 = lly_curvature(d, nb, 0, 1)
    rep.add("LLY Ricci curvature of K5 = 5/4 (= n/(n-1))", Ar, np.isclose(k5, 5 / 4), k5,
            note="positive discrete curvature of the carrier graph; not Einstein gravity")
    nb, d = graph_from_adj(carrier.petersen())
    kp = lly_curvature(d, nb, 0, int(nb[0][0]))
    rep.add("LLY curvature of the Petersen graph = 0 (edge-transitive)", Ar,
            abs(kp) < 1e-9, kp)
    ke8 = e8_edge_curvature()
    rep.add("LLY curvature of the E8 root-lattice graph = 0 (flat bath space)", Ar,
            abs(ke8) < 1e-9, ke8, note="as for Z^n: the abelian lattice is discretely "
                                       "Ricci-flat; only K5 carries positive curvature")

    coeffs, (t, R, m) = product_heat_coefficients()
    ok = (sp.simplify(coeffs[0] - 60) == 0
          and sp.simplify(coeffs[1] + 160 * m ** 2 + 5 * R) == 0
          and sp.simplify(coeffs[2] - 400 * m ** 4 - sp.Rational(40, 3) * m ** 2 * R) == 0)
    rep.add("M4 x F heat coefficients 60, -(160 m^2 + 5R), 400 m^4 + 40 m^2 R/3",
            gates.CONDITIONAL, ok, [str(c) for c in coeffs],
            note="uses Tr D_F^0=15, Tr D_F^2=40, Tr D_F^4=200 and spinor rank 4")
    G, Lcc = newton_and_vacuum(1, 1, 1, 10.0, 1.0)
    rep.add("f = e^-x, L = 10 m: G = pi/(500 m^2), Lambda_cc = 584.4 m^2 (natural)",
            gates.CONDITIONAL, np.isclose(G, np.pi / 500) and np.isclose(Lcc, 584.4),
            {"G": G, "Lambda_cc": Lcc})
    F2 = tuned_F2(1, 1, 10.0, 1.0)
    G2, L2 = newton_and_vacuum(1, 1, F2, 10.0, 1.0)
    rep.add("nonidentifiability: F2/F1 tunes Lambda_cc to any value (here 0)",
            gates.CONDITIONAL, np.isclose(L2, 0) and F2 > 0, {"F2": F2, "G": G2})
    rep.add("Einstein-Hilbert power 4 = cut rank, vacuum power 6 = cycle rank",
            Ar, True, note="shared integers only (canon 28 Oct); not a derivation")
    rep.add("Wald coefficient, Newton constant in SI, horizon/area map",
            gates.UNFORMED, True)
    return rep
