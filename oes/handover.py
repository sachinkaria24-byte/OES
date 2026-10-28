"""Layer 16. The 28 Oct handover (Locked Memory), audited claim by claim.

Source: "LOCKED MEMORY - OES End-to-End & Spectral Model Handover - 28 Oct 2026"
(Google Drive, created 11:00 UTC). Each statement is replayed where its operands
are in this repository; the rest are REPORTED. The corrections are collected in
docs/HANDOVER_ADDENDUM.md.

New here: the critical census of the band function on the alcove. Its vertices
and edges carry 11 critical families with 243,600 points and Morse sum 0, as
the handover says. Their 11 values are exactly the in-band characteristic roots
of the order-16 W_n recurrence of layer 14. Also new: the printed chart T_6 has
every column sum equal to 5, so it preserves the contrast lattice
V_c = {x in Z^6 : sum x = 0}. Its restriction there is a literal 5x5 integer
operator with determinant 31, which explains 155 = 5 * 31.
"""

import itertools
from fractions import Fraction
from math import comb, factorial

import numpy as np
import sympy as sp
from scipy.optimize import brentq

from . import carrier, court, gates, literal, recurrence
from .record import Report

HANDOVER_BANNER = {
    "AUTH": "NOT_PASS", "ScientificGold": "FALSE", "GoldDepth": 0, "G_OES": "FALSE",
    "SCR6": "NOT_RUN_OPERAND_ABSENT", "TIME_BIND": "UNBOUND", "DYN_BIND": "NOT_INSTALLED",
    "BIND_Q31": "UNBOUND", "PredictionFreeze": "NOT_TRIGGERED", "P": "NOT_PASS",
    "W_E": "NOT_PASS", "W_L": "NOT_PASS", "E": "NOT_PASS", "I": "NOT_PASS",
    "T3081": "UNOPENED", "x_executed": "000000", "R6/A40/A52": "FROZEN",
}

WE8 = 696729600


def e8_roots():
    R = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = np.zeros(8)
                v[i], v[j] = si, sj
                R.append(v)
    for signs in itertools.product((1, -1), repeat=8):
        if np.prod(signs) == 1:
            R.append(np.array(signs) / 2)
    return np.array(R)


def alcove_vertices():
    """0 and omega_i / m_i for the Bourbaki simple roots of E8."""
    a = np.zeros((8, 8))
    a[0] = np.array([1, -1, -1, -1, -1, -1, -1, 1]) / 2
    a[1] = np.eye(8)[0] + np.eye(8)[1]
    for k in range(2, 8):
        a[k] = np.eye(8)[k - 1] - np.eye(8)[k - 2]
    marks = np.array([2, 3, 4, 6, 5, 4, 3, 2])
    omega = np.linalg.inv(a).T
    return [np.zeros(8)] + [omega[i] / marks[i] for i in range(8)]


def _weyl_order(typ, rank):
    if typ == "A":
        return factorial(rank + 1)
    if typ == "D":
        return 2 ** (rank - 1) * factorial(rank)
    return {6: 51840, 7: 2903040, 8: 696729600}[rank]


def stabiliser(R, x, tol=1e-9):
    """Root subsystem {r : r.x in Z}: (type, |W| of it)."""
    ip = R @ x
    S = R[np.abs(ip - np.round(ip)) < tol]
    G = np.abs(S @ S.T) > 1e-9
    seen, parts, order = set(), [], 1
    for i in range(len(S)):
        if i in seen:
            continue
        stack, comp = [i], []
        seen.add(i)
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in np.nonzero(G[u])[0]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        rank, m = np.linalg.matrix_rank(S[comp]), len(comp)
        typ = next(t for t, f in (("A", lambda r: r * (r + 1)), ("D", lambda r: 2 * r * (r - 1)),
                                  ("E", lambda r: {6: 72, 7: 126, 8: 240}.get(r, -1)))
                   if f(rank) == m and not (t == "D" and rank < 4))
        parts.append(f"{typ}{rank}")
        order *= _weyl_order(typ, rank)
    return "+".join(sorted(parts, reverse=True)), order


def critical_census(npts=2001):
    """Critical families of eps = 240 - sum cos(2 pi r.x) on the vertices and edges of the alcove.

    Edge points have a rank-7 stabiliser, so the gradient lies along the edge and a
    critical point is a zero of the directional derivative. Returns
    {(lambda, type): {orbit, index}} with lambda = 240 - eps.
    """
    R = e8_roots()
    V = alcove_vertices()

    def grad(x):
        return 2 * np.pi * np.sin(2 * np.pi * R @ x) @ R

    def hess(x):
        return 4 * np.pi ** 2 * (R.T * np.cos(2 * np.pi * R @ x)) @ R

    fam = {}

    def add(x):
        lam = float(np.cos(2 * np.pi * R @ x).sum())
        typ, wo = stabiliser(R, x)
        w = np.linalg.eigvalsh(hess(x))
        fam.setdefault((round(lam, 8), typ), {"lambda": lam, "orbit": int(WE8 // wo),
                                              "index": int((w < 0).sum()),
                                              "nondegenerate": bool(np.min(np.abs(w)) > 1e-6)})

    for v in V:
        add(v)
    t = np.linspace(1e-4, 1 - 1e-4, npts)
    for va, vb in itertools.combinations(V, 2):
        d = vb - va
        X = va[None, :] + t[:, None] * d[None, :]
        g = (np.sin(2 * np.pi * X @ R.T) @ R) @ d
        for k in np.nonzero(np.sign(g[:-1]) != np.sign(g[1:]))[0]:
            t0 = brentq(lambda s: grad(va + s * d) @ d, t[k], t[k + 1], xtol=1e-15)
            x = va + t0 * d
            if np.linalg.norm(grad(x)) < 1e-7:
                add(x)
    return fam


def t5_construction():
    """The handover's T5x5 = (2 I4 - C) + [5], C the 5-cycle in the A4 root basis."""
    R5 = sp.zeros(5, 5)
    for i in range(5):
        R5[(i + 1) % 5, i] = 1
    S5 = sp.zeros(5, 5)
    for i in range(4):
        S5[i, i], S5[i + 1, i] = 1, -1
    for i in range(5):
        S5[i, 4] = 1
    Tcirc = 2 * sp.eye(5) - R5 + sp.Rational(4, 5) * sp.ones(5, 5)
    return S5, Tcirc, S5.inv() * Tcirc * S5


def contrast_restriction(T6):
    """T6 on V_c = {sum x = 0} in the basis e_i - e_{i+1}."""
    E = sp.zeros(6, 5)
    for i in range(5):
        E[i, i], E[i + 1, i] = 1, -1
    X = (E.T * E).inv() * E.T * T6 * E
    return X if T6 * E == E * X else None


def run():
    rep = Report("16-handover")
    T, OB, AR, RP, UF = (gates.THEOREM, gates.OBSTRUCTION, gates.ARITHMETIC, gates.REPORTED,
                         gates.UNFORMED)
    led = {k: v for k, v in gates.GATES.items() if k in HANDOVER_BANNER}
    rep.add("handover gate banner equals the standing ledger", T, led == HANDOVER_BANNER)

    # section 1
    src = literal.LiteralSource()
    rep.add("stage equation: the port Jacobian vanishes at q = 0, so the source obeys "
            "q'' + 4q = 0 there (omega_0 = 2)", T, np.allclose(src.J(np.zeros(10)), 0))
    D = np.array(carrier.dirac(carrier.signless_incidence()), float)
    w = np.round(np.linalg.eigvalsh(D @ D), 9)
    spec = {float(k): int(v) for k, v in zip(*np.unique(w, return_counts=True))}
    rep.add("carrier: spec D^2 = {0^5, 3^8, 8^2}, Tr D^2 = 40, Tr D^4 = 200", T,
            spec == {0.0: 5, 3.0: 8, 8.0: 2} and np.isclose(np.trace(D @ D), 40)
            and np.isclose(np.trace(np.linalg.matrix_power(D, 4)), 200))
    N6 = np.zeros((6, 15))
    for k, (i, j) in enumerate(itertools.combinations(range(6), 2)):
        N6[i, k] = N6[j, k] = 1
    k6 = np.round(np.linalg.eigvalsh(N6.T @ N6), 9)
    rep.add("'15-edge K6 carrier' is a relabeling: the 15 atoms are the vertices and edges "
            "of K5; the signless operator on the edges of K6 has spectrum {0^9, 4^5, 10}",
            OB, sorted(set(k6.tolist())) == [0.0, 4.0, 10.0],
            note="the spectrum (0^5, 3^8, 8^2) belongs to D^2 = MM^T + M^T M on K5")

    # section 2
    rep.add("clique weights: P_u = J/6 has entries 1/6, P_c has diagonal 5/6", AR, True)
    rep.add("relation traces Tr1 = 24 = 8*3, Tr2 = 84 = C(9,3)", RP, comb(9, 3) == 84,
            note="arithmetic true; the operands they are traces of are not defined")
    rep.add("one exterior algebra: dim Lambda(R^5) = 2^5 = 32 = 16 + 16 < 48 = 3*16", AR,
            sum(comb(5, k) for k in range(0, 6, 2)) == 16 and 2 ** 5 < 48,
            note="agrees with layer 12: one carrier, one generation")
    x, y = sp.symbols("x y")
    sos = sp.expand(sp.Rational(40, 9) * (x**2 / 2 + 3 * y**2 / 4)**2 - sp.Rational(20, 3) * x**2 * y**2
                    - sp.Rational(40, 9) * (x**2 / 2 - 3 * y**2 / 4)**2) == 0
    rep.add("9/40 tower identity (40/9)(x^2/2 + 3y^2/4)^2 - (20/3)x^2y^2 = "
            "(40/9)(x^2/2 - 3y^2/4)^2", T, sos,
            note="40/9 is the literal sharp quartic constant (layer 10); 9/40 as a physical "
                 "constant stays REMOVED (canon section 13)")
    rep.add("coil 540 = lcm(20,27) = 20*27 = 30*18 = 15*36 = 6*lcm(18,30)", AR,
            sp.ilcm(20, 27) == 540 == 20 * 27 == 30 * 18 == 15 * 36 == 6 * sp.ilcm(18, 30),
            note="numerical coincidences; the coil theorem itself is layer 8")
    d = literal.load()
    S5, Tcirc, Tlit = t5_construction()
    rep.add("handover T5x5 = (2I4 - C_A4) + [5]: integral, det 155, trace 14, and "
            "S5^-1 (2I5 - R5 + (4/5)J5) S5 with det S5 = 5", T,
            all(v.is_integer for v in Tlit) and Tlit.det() == 155 and Tlit.trace() == 14
            and S5.det() == 5)
    fives = [k for k, v in d.items() if isinstance(v, sp.Matrix) and v.shape == (5, 5)
             and v.det() == 155]
    T6 = d["T_OMSOON293"]
    z = sp.symbols("z")
    block = sp.expand(T6.charpoly(z).as_expr() - (z - 1) * Tlit.charpoly(z).as_expr()) == 0
    rep.add("that T5x5 is not literal: no 5x5 matrix of the operand file has det 155, and it is "
            "not a block of the printed chart T6 (characteristic polynomials differ)", OB,
            not fives and not block,
            note="it is built from the literal rotor R; status SELECTED_REFERENCE unless the "
                 "owner's packet defines it")
    X = contrast_restriction(T6)
    q = sp.Poly(z**5 - 3 * z**4 + 12 * z**3 - 20 * z**2 + 31 * z - 31, z)
    rep.add("literal 5-dim operand: T6 has every column sum 5, so it preserves V_c; T6|V_c is a "
            "5x5 integer matrix with det 31 and irreducible characteristic polynomial "
            "z^5 - 3z^4 + 12z^3 - 20z^2 + 31z - 31; 155 = 5 * 31", T,
            X is not None and all(v.is_integer for v in X) and X.det() == 31
            and sp.Poly(X.charpoly(z).as_expr(), z) == q and q.is_irreducible
            and sp.ones(1, 6) * T6 == 5 * sp.ones(1, 6),
            X.tolist() if X is not None else None)

    # section 3
    rng = np.random.default_rng(5)
    R2 = (2 * e8_roots()).astype(np.int64)             # doubled coordinates
    ok = True
    for _ in range(3):
        k = rng.integers(-7, 8, 8)
        ip = R2 @ k                                        # 2 (r.k)
        K2 = int(k @ k)
        ok &= (sum(int(v) ** 2 for v in ip) == 4 * 60 * K2
               and sum(int(v) ** 4 for v in ip) == 16 * 36 * K2 ** 2
               and sum(int(v) ** 6 for v in ip) == 64 * 30 * K2 ** 3)
    rep.add("7-design expansion eps(k) = 30|k|^2 - (3/2)|k|^4 + (1/24)|k|^6 + O(|k|^8)", T, ok,
            note="sum (k.r)^2 = 60|k|^2, sum (k.r)^4 = 36|k|^4, sum (k.r)^6 = 30|k|^6 over the "
                 "240 roots, exact for integer k")
    fam = critical_census()
    dat, _ = recurrence.load_operator()
    band = {}
    for r, m in dat["characteristic_roots"].items():
        v = sp.Rational(r)
        if -16 <= v <= 240:
            band[v] = m
    vals = {}
    for (lam, _typ), f in fam.items():
        q = Fraction(f["lambda"]).limit_denominator(1000)
        v = sp.Rational(q.numerator, q.denominator) if abs(float(q) - f["lambda"]) < 1e-9 else None
        vals[v] = vals.get(v, 0) + 1
    total = sum(f["orbit"] for f in fam.values())
    morse = sum((-1) ** f["index"] * f["orbit"] for f in fam.values())
    m12 = sorted((t, f["index"]) for (lam, t), f in fam.items() if abs(lam + 12) < 1e-8)
    rep.add("critical census on the alcove: 11 families, 243,600 points, Morse alternating sum "
            "0; the 11 values are the in-band characteristic roots of the order-16 W_n "
            "recurrence (layer 14)", T,
            len(fam) == 11 and total == 243600 and morse == 0 and vals == band
            and all(f["nondegenerate"] for f in fam.values())
            and m12 == [("A7+A1", 7), ("A8", 8)],
            {f"{t} lambda={f['lambda']:.6f}": [f["orbit"], f["index"]]
             for (lam, t), f in sorted(fam.items())},
            note="9 vertex families and 2 edge families (A6+A1 at -185/16, A7 at -320/27); "
                 "higher strata not searched, the match with the recurrence is independent "
                 "evidence that the band holds no others")
    W = recurrence.load_walks()
    rep.add("'W0..W84 exact, W6 = 17,141,798,400' is inside the repository's exact W0..W90", T,
            len(W) >= 91 and W[6] == 17141798400)
    rep.add("bivariate J.C.P. Miller eighth-power recurrence", RP, True,
            note="not given; the walk counts it produced agree with layer 14")
    rep.add("'order-11, degree-5 operator L11' as an exact recurrence for W_n is excluded", OB,
            bool(recurrence.excluded(W, 11, 5)),
            note="shape (11, 5) has (r+1)(d+2) = 84 <= 92 and fails on the exact W0..W90; mod p "
                 "order 11 needs degree >= 49, and the operator found has order 16. Its 11 "
                 "in-band roots are the 11 critical families, so L11 can only be the continuum "
                 "(asymptotic) part")
    sec = court.sector_moments(court.laplacian_moments(W, 52), 50)
    pd = all(court.chebyshev(M)[2] is None for M in sec.values())
    rep.add("'P25 discrete annihilator': no constant-coefficient order-25 recurrence holds for "
            "W_n or for the sector moments", OB,
            bool(recurrence.excluded(W, 25, 0)) and pd,
            note="P25 annihilates the 25-node Gauss-Jacobi sequence, which equals the moments "
                 "only through M_49; the 26x26 Hankel matrices are positive definite")
    rep.add("collar law '(15/13) r^2, equal to 3/80 at r = 1/5' is inconsistent: 3/80 = "
            "(15/16)/25, the saddle law of layer 8", OB,
            sp.Rational(15, 13) / 25 != sp.Rational(3, 80) == sp.Rational(15, 16) / 25)
    rep.add("mediant 1D collar: lambda_min > 1.00 on Curve I, >= 0.0298 on Curve II, up to 224",
            RP, True,
            note="a statement on two curves; it does not certify the 8-dim collar, which stays "
                 "open (layer 8); 0.0298 agrees with the survey floor 0.030")
    s, th = sp.symbols("s theta", real=True)
    Phi = 114 - 112 * sp.cos(sp.sqrt(2) * s) - 2 * sp.cos(2 * sp.sqrt(2) * s)
    id1 = sp.simplify(2 * sp.diff(Phi, s, 2) + sp.diff(Phi, s, 4) + 96 * sp.cos(2 * sp.sqrt(2) * s))
    e2 = sp.sqrt(2) * sp.sin(th) * sp.diff(Phi, s, 2) + sp.cos(th) * sp.diff(Phi, s, 3)
    id2 = sp.simplify(sp.expand_trig(e2.subs(s, th / sp.sqrt(2))
                                     + 16 * sp.sqrt(2) * sp.sin(th) * (sp.cos(2 * th) + 2)))
    R = e8_roots()
    ss = np.linspace(0, 3, 7)
    line = np.array([240 - np.cos(R @ (sv * np.sqrt(2) * R[0])).sum() for sv in ss])
    rep.add("root-line identities 2 Phi'' + Phi'''' = -96 cos(2 sqrt2 s) and sqrt2 sin(th) "
            "Phi'' + cos(th) Phi''' = -16 sqrt2 sin(th)(cos 2th + 2), th = sqrt2 s", T,
            id1 == 0 and id2 == 0
            and np.allclose(line, [float(Phi.subs(s, sv)) for sv in ss]),
            note="Phi(s) = eps(sqrt2 s r) for a root r: 114 - 112 cos(sqrt2 s) - 2 cos(2 sqrt2 s)")
    rep.add("uniform dispersive bound sup |K(t, x-y)| <= min(1, 3.65 t^(-9/4))", RP, True,
            note="the two identities are 1D statements on root lines and do not by themselves "
                 "bound the 8-dim kernel; the 0741 paper lists the dispersive constants as open")

    # section 4
    hs = {k: court.hausdorff(M) for k, M in sec.items()}
    rep.add("156-coordinate realization (6 boundary + 150 hidden) exact through M_50 exists: "
            "every sector's Hankel form is positive definite through M_50", T,
            all(v["fails_at"] is None for h in hs.values() for v in h.values()))
    rep.add("transverse Floquet monodromy (Tr M_j in [9999/10000, 1]) and the Legendre-Rodrigues "
            "preparation constant", RP, True, note="no operands or definitions given")
    rO, ker, rfull = court.observation_rank()
    rep.add("'exact separation theorem ker O within ker C' is reversed: for the two 6-port "
            "blocks ker O is the 4-dim cross block, so ker O is not in ker C; only the completed "
            "map has ker = 0", OB, len(ker) == 4 and rfull == 36,
            note="C extracts the cross block, which is injective on ker O")
    rep.add("'H90 identified as a [9,3,7]_q MDS code'", UF, True,
            note="the MDS facts hold (layer 15); nothing selects this code as H90")
    bad, good = court.script_loewner(sec["V5 contrast"])
    rep.add("'Stieltjes-Krein envelopes and multi-frequency criterion verified': the court "
            "script's certificate fails on the true moments", OB, bad > 0,
            note="the envelopes and the incompatibility are true, rebuilt in layer 15 from the "
                 "true moments; the script's own walk counts are wrong from W_4 on")
    rep.add("B_geom = diag(-2, 2) on C8 = C6 + C2", RP, True,
            note="sites and basis not given; for a C5-invariant pair a nonzero B lies on the "
                 "C5-trivial part, where it has 4 parameters, not 2")
    rep.add("primary paper digest SHA-256 b5590733...", RP, True,
            note="not the hash of One_Machine_20261028_0741.typ (64dfe66e...) or of the 0741 "
                 "model zip (a834dd88...) or any file in them; the PDF is not in this repository")

    # section 5
    rep.add("stoplines: SCR6 operands, physical selection, SI clock, area map and the Wald "
            "coefficient stay external", T,
            any("SCR6" in u for u in gates.UNFORMED_OPERANDS)
            and any("Wald" in u for u in gates.UNFORMED_OPERANDS)
            and gates.GATES["TIME_BIND"] == "UNBOUND")
    return rep
