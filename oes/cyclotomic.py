"""Layer 25, the arithmetic. E8 is one line over the 30th cyclotomic integers, and the tick's residue plane is F25.

The selected Coxeter clock c' of layer 19 (c'^6 = r r', the tick) is enough to rebuild the clocks, the glue, the
six-point geometry and the carrier.

(a) The cyclotomic line. Phi_30(c') = 0, and every root v generates E8 over Z[c']: v, c'v, ..., c'^7 v is a basis.
    So E8 is the ring O = Z[zeta30] with <x v, y v> = Tr(alpha x ybar), where alpha = (2 + 2 eta + eta^2)/15 and
    eta = zeta + zeta^-1. alpha is totally positive with norm 1/disc Q(zeta15) = 3^-4 5^-6, and only the thirty
    roots of unity commute with c'.
(b) The clocks are Galois. The normalizer of <c'> has 240 = 30 x 8 elements, one coset for each unit k mod 30.
    The day, the golden clock and the mirror are sigma7, sigma11 and sigma29 (complex conjugation), each times a
    unit u with u ubar = sigma(alpha)/alpha. On Q(zeta5) sigma7 doubles the tick; on Q(zeta3) sigma11 and sigma29
    conjugate.
(c) The tick's residue plane. 1 - g has Smith form 1^6 5^2, so the tick's 25 fixed momenta are
    E8/(1 - g)E8 = F5^2. As a Z[c']-module this is O/P = F25, the residue field at the one prime over 5, and c' acts
    on it as a primitive sixth root of unity. The 240 roots fall on its 24 nonzero points, ten on each. The six
    F5-lines pull back to six A4 + A4 sublattices whose root systems partition the 240 roots. The carrier's
    A4 + A4' is one of them, and its four glue classes are the four parallel lines.
(d) The tick's symmetry. C_W(g) has 600 elements and acts on the plane as SL(2,5), the binary icosahedral group,
    and on the six lines as PSL(2,5) = A5. With the day, N_W(<g>) has 2400 elements, acting as GL(2,5) on the plane
    and as PGL(2,5) = S5, the exceptional transitive S5, on the lines. The carrier line's stabilizer (400) exchanges
    A4 and A4', so the carrier does not depend on the line or the factor chosen.
(e) The clocks on F25. The day is the Singer cycle 2 + 2 omega of order 24. AIR_801 mod 5 has the characteristic
    polynomial of minus the day. The golden and mirror clocks are Frobenius-semilinear, and r and r' are
    transvections along the carrier line.
(f) The golden ratio and the carrier. The canon's golden operator A(h0) is the quadratic Gauss sum
    r + r^4 - r^2 - r^3, and on E8 the tick's Gauss sum squares to 5. The carrier's fifteen atoms are the A4 shadows
    of the mixed roots, and their Gram plus 2/5 is the signless incidence M.
"""

import functools
import itertools
import json
from math import gcd
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

from . import carrier, glue, spine

UNITS = [k for k in range(30) if gcd(k, 30) == 1]
AIR801 = np.array([[108, 801], [106, 901]])


@functools.lru_cache(maxsize=None)
def clocks():
    """The clocks in the simple-root basis: c', g = c'^6, r, r' (layer 19) and day, golden, mirror (data/clocks.json)."""
    c, cp, r, rp, g, w = spine.spine_clock()
    J = json.loads((Path(__file__).resolve().parent.parent / "data" / "clocks.json").read_text())
    to = lambda M: spine.to_root_basis(np.array(M, dtype=float) / J["scale"])
    return {"c": cp, "g": g, "r": r, "rp": rp, "day": to(J["day"]), "golden": to(J["golden"]),
            "mirror": to(J["mirror"])}


def _pow(M, k):
    return spine.mpow(M, k % 30)


def _alpha15(M):
    """15 alpha(M) = 2 + 2 eta + eta^2 with eta = M + M^-1, for M a power of c'."""
    eta = M + spine.inverse(M)
    return 2 * np.eye(8, dtype=np.int64) + 2 * eta + eta @ eta


def cyclotomic_line():
    """(a): E8 = Z[c'] v, with the trace form."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    cp = clocks()["c"]
    P = [_pow(cp, k) for k in range(30)]
    v = RB[0]
    f = [int(v @ C @ P[m] @ v) for m in range(30)]
    gens = sum(abs(round(np.linalg.det(np.array([P[k] @ x for k in range(8)]).T))) == 1 for x in RB)
    phi = sp.Poly(sp.cyclotomic_poly(30, sp.Symbol("x")), sp.Symbol("x")).all_coeffs()[::-1]
    a15 = _alpha15(cp)
    power = sp.Matrix(8, 8, lambda i, j: int(np.trace(P[(i + j) % 30])))
    commuting = sum(all(int(x @ C @ P[m] @ x) == f[m] for m in range(30)) for x in RB)
    return {
        "Phi_30(c') = 0, so Z[c'] = Z[zeta30], and every one of the 240 roots v generates E8 over it: "
        "v, c'v, ..., c'^7 v is a basis":
            not sum(int(a) * P[k] for k, a in enumerate(phi)).any() and gens == 240,
        "the form is the trace form <x v, y v> = Tr(alpha x ybar) with alpha = (2 + 2 eta + eta^2)/15, eta = zeta + "
        "zeta^-1: <v, c'^m v> = Tr(alpha zeta^m) for all thirty m (the trace of multiplication on E8 = O)":
            all(int(np.trace(a15 @ P[m])) == 15 * f[m] for m in range(30)),
        "alpha is totally positive (alpha(c') is a positive self-adjoint operator) and N(alpha) = det alpha(c') = "
        "1/1265625 = 1/disc Q(zeta15) = 3^-4 5^-6, which is why E8 is unimodular":
            sp.Matrix(C @ a15).is_positive_definite and round(np.linalg.det(a15.astype(float))) == 15 ** 8 // 1265625
            and abs(power.det()) == 1265625 == 3 ** 4 * 5 ** 6,
        "only the thirty roots of unity commute with c' (Kronecker): exactly 30 roots w have the data "
        "<w, c'^m w> = <v, c'^m v>, the images of v under C_W(c') = <c'>": commuting == 30,
    }


def galois_clocks():
    """(b): the normalizer of <c'> is the Galois group times the roots of unity, and the clocks are Galois."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    k = clocks()
    cp = k["c"]
    P = [_pow(cp, j) for j in range(30)]
    v = RB[0]
    f = [int(v @ C @ P[m] @ v) for m in range(30)]
    per_unit = [sum(all(int(x @ C @ P[(u * m) % 30] @ x) == f[m] for m in range(30)) for x in RB) for u in UNITS]
    basis = np.array([P[j] @ v for j in range(8)]).T
    binv = np.linalg.inv(basis)
    exps, norms, semilinear = {}, {}, {}
    for name in ("day", "golden", "mirror"):
        n = k[name]
        e = next(j for j in range(30) if np.array_equal(n @ cp @ spine.inverse(n), P[j]))
        u = np.round(binv @ (n @ v)).astype(np.int64)
        U = sum(int(a) * P[j] for j, a in enumerate(u))
        Ubar = sum(int(a) * P[-j % 30] for j, a in enumerate(u))
        exps[name] = e
        norms[name] = np.array_equal(_alpha15(cp) @ U @ Ubar, _alpha15(P[e]))
        semilinear[name] = all(np.array_equal(n @ P[j] @ v, P[(e * j) % 30] @ U @ v) for j in range(30))
    g = k["g"]
    on5 = {name: next(j for j in range(1, 5) if np.array_equal(k[name] @ g @ spine.inverse(k[name]), spine.mpow(g, j)))
           for name in ("day", "golden", "mirror")}
    return {
        "the normalizer of <c'> has 240 = 30 x 8 elements: for each unit k mod 30 exactly 30 roots w carry the data "
        "<w, c'^(km) w> = <v, c'^m v>, so every Galois automorphism of Q(zeta30) is realized, each by thirty isometries":
            per_unit == [30] * 8,
        "the day, the golden clock and the mirror are sigma7, sigma11 and sigma29: n(x(c') v) = x(c'^k) u_n(c') v with "
        "u_n in Z[c'], and alpha u_n ubar_n = sigma_k(alpha); Gal = <7> x <11> with 29 = 7^2 x 11 mod 30":
            exps == {"day": 7, "golden": 11, "mirror": 29} and all(norms.values()) and all(semilinear.values())
            and sorted({pow(7, a, 30) * pow(11, b, 30) % 30 for a in range(4) for b in range(2)}) == UNITS
            and 7 ** 2 * 11 % 30 == 29,
        "on the tick's field Q(zeta5) the day doubles (sigma7 = sigma2), the golden clock is trivial and the mirror "
        "inverts; on the sun's field Q(zeta3) the day is trivial and the other two conjugate":
            on5 == {"day": 2, "golden": 1, "mirror": 4} and [7 % 3, 11 % 3, 29 % 3] == [1, 2, 2],
    }


@functools.lru_cache(maxsize=None)
def residue():
    """The quotient map E8 -> E8/(1 - g)E8 = F5^2 (two coordinates mod 5), its six lines, and the action of a
    lattice map on it."""
    g = clocks()["g"]
    I8 = np.eye(8, dtype=np.int64)
    ker = sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix((I8 - g).T.tolist())).convert_to(sp.GF(5))
    ns = ker.nullspace().to_Matrix()
    Lq = np.array([[int(x) % 5 for x in ns.row(i)] for i in range(ns.shape[0])], dtype=np.int64)
    lines = []
    for a, b in itertools.product(range(5), repeat=2):
        if (a, b) != (0, 0):
            L = frozenset(((t * a) % 5, (t * b) % 5) for t in range(1, 5))
            if L not in lines:
                lines.append(L)
    return Lq, lines


def point(x):
    Lq, _ = residue()
    return tuple(int(t) for t in (Lq @ np.asarray(x)) % 5)


def on_plane(n):
    """The 2 x 2 matrix over F5 by which the lattice map n acts on E8/(1 - g)E8 (n must normalize <g>)."""
    Lq, _ = residue()
    target = (Lq @ n) % 5
    for cols in itertools.combinations(range(8), 2):
        S = sp.Matrix(Lq[:, cols].tolist())
        if S.det() % 5:
            Q = (target[:, cols] @ np.array(S.inv_mod(5).tolist(), dtype=np.int64)) % 5
            if np.array_equal((Q @ Lq) % 5, target):
                return Q
    return None


def on_lines(Q):
    _, lines = residue()
    out = []
    for L in lines:
        p = next(iter(L))
        img = tuple(int(t) for t in (Q @ np.array(p)) % 5)
        out.append(next(i for i, M in enumerate(lines) if img in M))
    return tuple(out)


def _order(Q, p=5):
    P, I = np.eye(len(Q), dtype=np.int64), np.eye(len(Q), dtype=np.int64)
    for k in range(1, 1000):
        P = (P @ Q) % p
        if np.array_equal(P, I):
            return k


def _perm_order(s):
    q, k = s, 1
    while q != tuple(range(len(s))):
        q, k = tuple(s[i] for i in q), k + 1
    return k


def _components(roots, C):
    n = len(roots)
    adj = {a: [b for b in range(n) if b != a and int(roots[a] @ C @ roots[b]) in (1, -1)] for a in range(n)}
    seen, comps = set(), []
    for a in range(n):
        if a not in seen:
            stack, comp = [a], {a}
            while stack:
                for b in adj[stack.pop()]:
                    if b not in comp:
                        comp.add(b)
                        stack.append(b)
            seen |= comp
            comps.append(len(comp))
    return sorted(comps)


def residue_plane():
    """(c): the 25 fixed momenta of the tick are F25, and its six lines are six A4 + A4."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    k = clocks()
    g = k["g"]
    Lq, lines = residue()
    snf = smith_normal_form(sp.Matrix((np.eye(8, dtype=np.int64) - g).tolist()), domain=sp.ZZ)
    X = on_plane(k["c"])
    field = all(np.array_equal((a * np.eye(2, dtype=np.int64) + b * X) % 5, np.zeros((2, 2), dtype=np.int64))
                or round(np.linalg.det(a * np.eye(2) + b * X)) % 5 for a in range(5) for b in range(5))
    pts = [point(x) for x in RB]
    fibres = {p: pts.count(p) for p in set(pts)}
    pulled = [[RB[i] for i in range(240) if pts[i] in L] for L in lines]
    _, A, Ap = glue.a4_pair()
    to_rb = lambda rows: np.round(np.array(rows) @ Binv.T).astype(np.int64)
    A_pts, Ap_pts = {point(x) for x in to_rb(A)}, {point(x) for x in to_rb(Ap)}
    carrier_line = next(i for i, L in enumerate(lines) if A_pts <= L)
    S = glue.chain_order(glue.simple_system(A))
    cls = {}
    for i, x in enumerate(R):
        p = pts[i]
        if p not in lines[carrier_line]:
            cls.setdefault(glue.class_mod_a4(glue.projector(A) @ x, S), set()).add(p)
    return {
        "1 - g has Smith form 1^6 5^2, so the tick's 25 fixed momenta are E8/(1 - g)E8 = F5^2; c' acts on it with "
        "x^2 - x + 1, irreducible mod 5, so F5[c'] is the field F25 = O/P (P the one prime of Q(zeta15) over 5) and "
        "c' is a primitive sixth root of unity there":
            [snf[i, i] for i in range(8)] == [1] * 6 + [5] * 2 and Lq.shape == (2, 8)
            and (int(np.trace(X)) % 5, round(np.linalg.det(X)) % 5) == (1, 1) and field and _order(X) == 6,
        "the 240 roots fall on the 24 nonzero points of the plane, ten on each":
            len(fibres) == 24 and set(fibres.values()) == {10} and (0, 0) not in fibres,
        "the six lines pull back to six A4 + A4 sublattices: each holds 40 roots in two orthogonal A4 systems of rank "
        "8, and the six root systems partition the 240 roots":
            len(lines) == 6 and all(len(x) == 40 and _components(x, C) == [20, 20]
                                    and np.linalg.matrix_rank(np.array(x, dtype=float)) == 8 for x in pulled)
            and sum(len(x) for x in pulled) == 240,
        "the carrier's A4 + A4' is the pullback of one line: all 40 of its roots lie on it, and the index is 5 for both; "
        "its four glue classes are the four lines parallel to it, five points and fifty roots each":
            A_pts | Ap_pts == set(lines[carrier_line]) and len(A) + len(Ap) == 40
            and len(cls) == 4 and all(len(s) == 5 for s in cls.values())
            and all({tuple((np.array(p) - np.array(q)) % 5) for p in s for q in s} - {(0, 0)} <= lines[carrier_line]
                    for s in cls.values()),
    }


@functools.lru_cache(maxsize=None)
def centralizer():
    """C_W(g): the isometries commuting with the tick, fixed by the images of a Z[g]-basis of two roots."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    g = clocks()["g"]
    ip = lambda x, y: int(x @ C @ y)
    Pg = [spine.mpow(g, j) for j in range(5)]
    span = lambda a, b: np.array([Pg[j] @ a for j in range(4)] + [Pg[j] @ b for j in range(4)]).T
    al = RB[0]
    be = next(b for b in RB[1:] if abs(round(np.linalg.det(span(al, b)))) == 1)
    binv = np.linalg.inv(span(al, be))
    data = lambda a, b: [ip(a, Pg[j] @ b) for j in range(5)]
    ca = [x for x in RB if data(x, x) == data(al, al)]
    cb = [y for y in RB if data(y, y) == data(be, be)]
    out = []
    for x in ca:
        for y in cb:
            if data(x, y) == data(al, be):
                W = np.round(span(x, y) @ binv).astype(np.int64)
                if np.array_equal(W @ g, g @ W) and spine.is_weyl(W):
                    out.append(W)
    return out


def tick_normalizer():
    """(d): the tick's centralizer is <g> x SL(2,5) on the plane, and its normalizer gives PGL(2,5) on the lines."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    k = clocks()
    g, day = k["g"], k["day"]
    cent = centralizer()
    norm = [W @ spine.mpow(day, j) for W in cent for j in range(4)]
    img_c = {tuple(on_plane(W).flatten()) for W in cent}
    img_n = {tuple(on_plane(W).flatten()) for W in norm}
    mats = lambda s: [np.array(q).reshape(2, 2) for q in s]
    trivial = [W for W in cent if np.array_equal(on_plane(W), np.eye(2, dtype=np.int64))]
    lines_c = {on_lines(Q) for Q in mats(img_c)}
    lines_n = {on_lines(Q) for Q in mats(img_n)}
    _, A, Ap = glue.a4_pair()
    to_rb = lambda rows: {tuple(x) for x in np.round(np.array(rows) @ Binv.T).astype(np.int64)}
    SA, SAp = to_rb(A), to_rb(Ap)
    stab = [W for W in norm if {tuple(W @ np.array(x)) for x in SA} <= SA | SAp]
    swap = [W for W in stab if {tuple(W @ np.array(x)) for x in SA} == SAp]
    return {
        "C_W(g) has 600 elements; modulo <g> (the five that fix the plane) it acts on the plane as SL(2,5), the binary "
        "icosahedral group (120 matrices of determinant 1, one involution), and on the six lines as PSL(2,5) = A5, "
        "transitively":
            len(cent) == 600 and len(trivial) == 5 and all(any(np.array_equal(W, spine.mpow(g, j)) for j in range(5))
                                                         for W in trivial)
            and len(img_c) == 120 and {round(np.linalg.det(Q)) % 5 for Q in mats(img_c)} == {1}
            and sum(_order(Q) == 2 for Q in mats(img_c)) == 1 and len(lines_c) == 60
            and {s[0] for s in lines_c} == set(range(6)),
        "with the day the normalizer N_W(<g>) has 2400 elements, acting on the plane as GL(2,5) (480) and on the six "
        "lines as PGL(2,5) = S5, the exceptional S5, transitively":
            all(any(np.array_equal(W @ g @ spine.inverse(W), spine.mpow(g, j)) for j in range(1, 5)) for W in norm[::37])
            and len({tuple(W.flatten()) for W in norm}) == 2400 and len(img_n) == 480 and len(lines_n) == 120
            and {s[0] for s in lines_n} == set(range(6)),
        "the carrier line's stabilizer has 400 elements, and 200 of them exchange A4 and A4': the carrier is the same "
        "from every line and either factor":
            len(stab) == 400 and len(swap) == 200,
    }


def clock_residues():
    """(e): the clocks on the residue field, and AIR_801 mod 5."""
    k = clocks()
    Q = {name: on_plane(k[name]) for name in ("c", "day", "golden", "mirror", "r", "rp")}
    lin = {name: _perm_order(on_lines(M)) for name, M in Q.items()}
    commutes = lambda M: np.array_equal((M @ Q["c"]) % 5, (Q["c"] @ M) % 5)
    a, b = 2, 2
    air = AIR801 % 5
    md = (-Q["day"]) % 5
    conj = next((np.array(P).reshape(2, 2) for P in itertools.product(range(5), repeat=4)
                 if round(np.linalg.det(np.array(P).reshape(2, 2))) % 5
                 and np.array_equal((np.array(P).reshape(2, 2) @ air) % 5, (md @ np.array(P).reshape(2, 2)) % 5)), None)
    carrier_line = next(i for i, s in enumerate(on_lines(Q["r"])) if s == i)
    return {
        "on F25 the Coxeter clock has order 6 (order 3 on the lines); the day is the F25-element 2 + 2 omega, omega the "
        "image of c', of order 24: a Singer cycle, which turns the six lines in one 6-cycle":
            _order(Q["c"]) == 6 and lin["c"] == 3
            and np.array_equal(Q["day"], (a * np.eye(2, dtype=np.int64) + b * Q["c"]) % 5)
            and _order(Q["day"]) == 24 and lin["day"] == 6,
        "the golden clock (order 4) and the mirror (order 2) do not commute with omega: they are Frobenius-semilinear, "
        "as sigma11 and sigma29 act on Q(zeta3); each swaps lines in pairs":
            _order(Q["golden"]) == 4 and _order(Q["mirror"]) == 2 and not commutes(Q["golden"])
            and not commutes(Q["mirror"]) and lin["golden"] == 2 and lin["mirror"] == 2 and commutes(Q["day"]),
        "the carrier and twin rotations are transvections along the carrier line, inverse to each other (r r' = g acts "
        "trivially): each fixes the carrier line and turns the other five in a 5-cycle":
            all(_order(Q[n]) == 5 and round(np.trace(Q[n])) % 5 == 2 for n in ("r", "rp"))
            and np.array_equal((Q["r"] @ Q["rp"]) % 5, np.eye(2, dtype=np.int64))
            and on_lines(Q["r"])[carrier_line] == carrier_line and lin["r"] == 5,
        "AIR_801 mod 5 = [[3, 1], [1, 1]] has the irreducible characteristic polynomial x^2 + x + 2 of minus the day, "
        "so it is conjugate in GL(2,5) to -d on the tick's residue plane: the canon's 801 matrix is that Singer cycle":
            air.tolist() == [[3, 1], [1, 1]] and (int(np.trace(air)) % 5, round(np.linalg.det(air)) % 5)
            == (int(np.trace(md)) % 5, round(np.linalg.det(md)) % 5) == (4, 2)
            and all((x * x + x + 2) % 5 for x in range(5)) and conj is not None and _order(air) == 24,
    }


def golden_gauss():
    """(f): the golden ratio is the quadratic Gauss sum of the tick."""
    k = clocks()
    E = carrier.edges()
    h0 = sp.Matrix([1 if (j - i) % 5 in (1, 4) else -1 for i, j in E])
    A_h0 = sp.zeros(5)
    for t, (i, j) in enumerate(E):
        A_h0[i, j] = A_h0[j, i] = h0[t]
    r = sp.zeros(5)
    for i in range(5):
        r[(i + 1) % 5, i] = 1
    gauss = r + r ** 4 - r ** 2 - r ** 3
    P5 = sp.eye(5) - sp.ones(5, 5) / 5
    g = k["g"]
    G8 = g + spine.mpow(g, 4) - spine.mpow(g, 2) - spine.mpow(g, 3)
    phi = sp.Symbol("phi")
    return {
        "the canon's golden operator K = A(h0), +1 on the pentagon and -1 on the pentagram, is the quadratic Gauss sum "
        "r + r^4 - r^2 - r^3 = sum (j/5) r^j of the carrier rotation, so K^2 = 5 on A4 and Phi = (1 + K)/2 is the "
        "golden ratio, the real quadratic field Q(sqrt5) inside Q(zeta5)":
            A_h0 == gauss and (gauss ** 2 * P5 - 5 * P5).is_zero_matrix
            and (((P5 + gauss) / 2) ** 2 - (P5 + gauss) / 2 - P5).is_zero_matrix,
        "on all of E8 the tick's Gauss sum g + g^4 - g^2 - g^3 squares to 5 (1 + g + ... + g^4 = 0, as g fixes no "
        "vector), so sqrt5 and the golden ratio act on the whole lattice":
            not sum(spine.mpow(g, j) for j in range(5)).any() and np.array_equal(G8 @ G8, 5 * np.eye(8, dtype=np.int64))
            and sp.solve(phi ** 2 - phi - 1, phi) == [sp.Rational(1, 2) - sp.sqrt(5) / 2, sp.Rational(1, 2) + sp.sqrt(5) / 2],
    }


def carrier_shadows():
    """(f): the carrier's fifteen atoms are the A4 shadows of the mixed roots."""
    u = sp.ones(5, 1) / 5
    Vw = [sp.eye(5)[:, i] - u for i in range(5)]
    Ew = [sp.eye(5)[:, j] + sp.eye(5)[:, k] - 2 * u for j, k in carrier.edges()]
    M = sp.Matrix(carrier.signless_incidence())
    gram = sp.Matrix(5, 10, lambda i, e: (Vw[i].T * Ew[e])[0])
    D = sp.Matrix(sp.BlockMatrix([[sp.zeros(5), M], [M.T, sp.zeros(10)]]))
    out, atoms, pairs, _ = glue.decompose()
    return {
        "the 200 mixed roots project onto the carrier's A4 as the five vertex weights e_i - u (norm 4/5) and the ten edge "
        "weights e_j + e_k - 2u (norm 6/5), with signs: the carrier's fifteen atoms, 5 + 10, one SU(5) generation":
            out == {"A4": 20, "A4'": 20, "mixed": 200} and {a[:2] for a in atoms if a} ==
            {("V", i) for i in range(5)} | {("E", e) for e in carrier.edges()}
            and (Vw[0].T * Vw[0])[0] == sp.Rational(4, 5) and (Ew[0].T * Ew[0])[0] == sp.Rational(6, 5),
        "the shadows' Gram plus 2/5 is the signless incidence M, so the carrier's Dirac D = [[0, M], [M^T, 0]] is the "
        "shadow incidence, and D^2 = M M^T + M^T M has spectrum 0^5 3^8 8^2":
            gram + sp.Rational(2, 5) * sp.ones(5, 10) == M
            and sorted((D * D).eigenvals().items()) == [(0, 5), (3, 8), (8, 2)],
    }


def parent_hexad():
    """The hub's 360 parent lives on the tick's hexad, the six residue lines."""
    k = clocks()
    psl = {on_lines(on_plane(W)) for W in centralizer()}
    rl = on_lines(on_plane(k["r"]))
    fixed = next(i for i in range(6) if rl[i] == i)
    order = [next(i for i in range(6) if i != fixed)]
    while len(order) < 5:
        order.append(rl[order[-1]])
    lab = {x: j for j, x in enumerate(order)}
    lab[fixed] = 5
    back = {j: x for x, j in lab.items()}
    relabel = lambda s: tuple(lab[s[back[j]]] for j in range(6))
    PS = {relabel(s) for s in psl}
    t = (0, 1, 3, 2, 5, 4)
    mul = lambda a, b: tuple(a[b[i]] for i in range(6))
    G, new = {tuple(range(6))}, [tuple(range(6))]
    while new:
        new = [mul(a, s) for a in new for s in PS | {t} if mul(a, s) not in G]
        G |= set(new)
    even = lambda s: sum(1 for i, j in itertools.combinations(range(6), 2) if s[i] > s[j]) % 2 == 0
    return {
        "label the six residue lines so that the carrier rotation is (01234), fixing the carrier line as 5: the hub's "
        "t = (23)(45) lies outside the tick's PSL(2,5), and the two generate A6, so the 360 parent is the alternating "
        "group of the tick's hexad, marked at the carrier line":
            relabel(rl) == (1, 2, 3, 4, 0, 5) and relabel(rl) in PS and t not in PS and len(G) == 360
            and all(even(s) for s in G),
    }
