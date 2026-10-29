"""Layer 26. The three primes of the Coxeter number: the regular clocks, the residue rings and the parent's A6.

E8's Coxeter number is h = 30 = 2 x 3 x 5. Layer 25 read the seed (E8, c') at the prime 5, where the tick's residue
plane F25 carries the carrier. This layer reads it at all three primes and finds the 360 parent at the prime 3.

(a) The degrees. c' has the characteristic polynomial Phi_30, so its eigenvalues are zeta^m for the eight units m
    mod 30. These are E8's exponents, the degrees m + 1 are 2, 8, 12, 14, 18, 20, 24, 30, and |W(E8)| is their
    product (cited: the order of a reflection group is the product of its degrees).
(b) The regular clocks (Springer). The regular numbers of E8 are the thirteen divisors of 30, 24 and 20, the orders
    of the Coxeter clock, the day and the golden clock (cited: Lehrer-Springer, d is regular when it divides as many
    degrees as codegrees d_i - 2). Each regular class is a power of one of the three, all its eigenvalues are
    primitive d-th roots, and its centralizer, counted here from the images of a Z[w]-basis of roots, has the order
    prod_{d | d_i} d_i: 30, 24, 20, 288, 192, 600, 46080 and 155520 for d = 30, 24, 20, 12, 8, 5, 4 and 3.
(c) Three cyclotomic lines. The clocks of order 30, 24 and 20 have cyclic centralizers, and each makes E8 one line over
    its cyclotomic integers, with a trace form Tr(beta x ybar) of norm 1/disc. Each normalizer realizes its Galois
    group (240, 192, 160 elements). The fourth cyclotomic field of degree 8, Q(zeta16), carries Z^8 and not E8:
    W(E8) has no element of order 16 (OBSTRUCTION).
(d) The prime clocks. c' = c'^15 c'^10 c'^6 = (-1) s g, the half-turn, the sun and the tick. Under 144 k -> c'^k they
    are the circle's 2160, 1440 and 864, one in each of its primary clocks. Each fixes p^(8/(p-1)) momenta,
    E8/(1 - h)E8, the residue ring of Z[zeta30] at p: F16 x F16, F81 and F25, on which c' has order 30/p. The roots
    lie 2, 3 and 10 over each point they meet, and the centralizer of each prime clock acts there as the isometry
    group of the residue form: W(E8) as GO8+(2) (cited), C_W(s) as Sp(4,3) and C_W(g) as SL(2,5) = Sp(2,5).
(e) The half-turn. The two primes over 2 split the 256 half-periods into two complementary totally singular F16's,
    swapped by the mirror, on each of which c' is a Singer cycle of order 15.
(f) The sun. The sun's 81 momenta carry the alternating form <x, (s - s^2) y> mod 3. There c' + c'^-1 is the golden
    ratio (phi^2 = phi + 1), so F9 = F3[phi] and the momenta are the plane F9^2. The 40 projective points pull back to
    40 A2 that partition the roots, two of them orthogonal exactly when their points are. The totally isotropic lines
    are 40 frames 4A2 (the generalized quadrangle W(3)), and the ten F9-lines are a spread of them.
(g) The decad. The 2160 isometries that commute with the sun and with phi act on the ten F9-lines as PSL(2,9), with
    kernel <c'^5>. An isomorphism from the hub's A6 = <r, t> sends r to the Coxeter clock, and with the hub's doubling
    sent to the day it extends to S6. So the 360 parent is the sun's A6 on its ten 4A2 frames, and the clocks act on
    it through AGL(1,5).
(h) No clock covers A6 (OBSTRUCTION; the owner, 20:22). A6's elements have orders 1 to 5, so every homomorphism from
    the circle to A6 has a cyclic image of at most five elements. Every clock group is solvable and A6 is perfect. On
    the tick's hexad the seed acts only through PGL(2,5), whose even part holds 60 of the 360. A6 is reached by the
    sun's symmetry, which is not a clock.
"""

import functools
import itertools
from collections import Counter
from math import gcd, prod

import numpy as np
import sympy as sp
from sympy.combinatorics import Permutation
from sympy.matrices.normalforms import smith_normal_form

from . import cyclotomic, spine

I8 = np.eye(8, dtype=np.int64)
DEGREES = [u + 1 for u in cyclotomic.UNITS]


def _phi(d):
    return sum(1 for j in range(1, d + 1) if gcd(j, d) == 1)


def _disc(n):
    """|disc Q(zeta_n)| = n^phi(n) / prod_(p | n) p^(phi(n)/(p - 1))."""
    f = _phi(n)
    return n ** f // prod(p ** (f // (p - 1)) for p in sp.primefactors(n))


@functools.lru_cache(maxsize=None)
def _roots():
    """The roots in the root basis, the Cartan form, a lookup and the 240 x 240 inner products."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    return RB, C, {tuple(r): i for i, r in enumerate(RB.tolist())}, (RB @ C @ RB.T).astype(np.int64)


def _perm(M):
    """The permutation of the 240 roots by the isometry M."""
    RB, _, key, _ = _roots()
    return np.array([key[tuple((M @ r).tolist())] for r in RB], dtype=np.int64)


@functools.lru_cache(maxsize=None)
def regular():
    """One element of each regular order d: a power of c', the day d or the golden clock v."""
    k = cyclotomic.clocks()
    c, day, v, P = k["c"], k["day"], k["golden"], spine.mpow
    return {30: c, 24: day, 20: v, 15: P(c, 2), 12: P(day, 2), 10: P(c, 3), 8: P(day, 3), 6: P(c, 5), 5: k["g"],
            4: P(day, 6), 3: P(c, 10), 2: P(c, 15), 1: I8}


@functools.lru_cache(maxsize=None)
def centralizer(d):
    """C_W(w) for the regular clock w of order d: the root tuples (u_1, ..., u_m) that carry the data of a Z[w]-basis
    of roots (v_1, ..., v_m), m = 8/phi(d), and the basis. An isometry commuting with w is fixed by the u_i, and every
    tuple with the same data <u_a, w^j u_b> = <v_a, w^j v_b> gives one (Aut(E8) = W(E8))."""
    w = regular()[d]
    f, m = _phi(d), 8 // _phi(d)
    RB, C, key, IP = _roots()
    Wm = np.array([_perm(spine.mpow(w, j)) for j in range(d)])
    M = IP[:, Wm]
    Pw = [spine.mpow(w, j) for j in range(f)]
    vs = next(list(cb) for cb in itertools.combinations(range(240), m)
              if abs(round(np.linalg.det(np.array([Pw[j] @ RB[i] for i in cb for j in range(f)], dtype=float).T))) == 1)
    data = {(a, b): M[vs[a], :, vs[b]] for a in range(m) for b in range(m)}
    diag = M[np.arange(240), :, np.arange(240)]
    selfmask = [np.all(diag == data[(a, a)][None, :], axis=1) for a in range(m)]
    leaves = []

    def grow(prefix):
        a = len(prefix)
        if a == m:
            leaves.append(prefix)
            return
        mask = selfmask[a].copy()
        for b, ub in enumerate(prefix):
            mask &= np.all(M[ub] == data[(b, a)][:, None], axis=0)
        for u in np.nonzero(mask)[0]:
            grow(prefix + [int(u)])
    grow([])
    return np.array(leaves, dtype=np.int64), vs


@functools.lru_cache(maxsize=None)
def elements(d):
    """The matrices of C_W(w) for the regular clock w of order d (int8; entries of W(E8) in the root basis are small)."""
    w = regular()[d]
    f, m = _phi(d), 8 // _phi(d)
    RB = _roots()[0]
    leaves, vs = centralizer(d)
    Wm = np.array([_perm(spine.mpow(w, j)) for j in range(f)])
    basis = np.array([spine.mpow(w, j) @ RB[i] for i in vs for j in range(f)], dtype=np.int64).T
    binv = np.rint(np.linalg.inv(basis.astype(float))).astype(np.int64)
    assert np.array_equal(basis @ binv, I8)
    out = np.empty((len(leaves), 8, 8), dtype=np.int8)
    for lo in range(0, len(leaves), 20000):
        L = leaves[lo:lo + 20000]
        cols = np.stack([RB[Wm[j][L[:, i]]] for i in range(m) for j in range(f)], axis=2)
        chunk = cols @ binv
        assert np.abs(chunk).max() < 128
        out[lo:lo + 20000] = chunk
    return out


def regular_clocks():
    """(a), (b): the degrees from c', the regular numbers, and the centralizers by Springer's formula."""
    x = sp.Symbol("x")
    k = cyclotomic.clocks()
    P = spine.mpow
    codeg = [e - 2 for e in DEGREES]
    reg = [d for d in range(1, 31) if sum(e % d == 0 for e in DEGREES) == sum(e % d == 0 for e in codeg)]
    div = sorted({d for n in (30, 24, 20) for d in range(1, n + 1) if n % d == 0})
    char = lambda w: sp.expand(sp.Matrix(w.tolist()).charpoly(x).as_expr())
    pure = all(char(w) == sp.expand(sp.cyclotomic_poly(d, x) ** (8 // _phi(d))) for d, w in regular().items())
    counted = {d: len(centralizer(d)[0]) for d in (30, 24, 20, 12, 8, 5, 4, 3)}
    springer = {d: prod(e for e in DEGREES if e % d == 0) for d in counted}
    c, g, s = k["c"], k["g"], P(k["c"], 10)
    return {
        "c' has the characteristic polynomial Phi_30, so E8's exponents are the eight units mod 30 and its degrees "
        "are 2, 8, 12, 14, 18, 20, 24, 30, with product |W(E8)| = 696729600 (cited: the order of a reflection group "
        "is the product of its degrees)":
            char(c) == sp.expand(sp.cyclotomic_poly(30, x)) and DEGREES == [2, 8, 12, 14, 18, 20, 24, 30]
            and prod(DEGREES) == 696729600,
        "the regular numbers (cited: Lehrer-Springer, d divides as many degrees as codegrees d_i - 2) are 1, 2, 3, 4, 5, "
        "6, 8, 10, 12, 15, 20, 24, 30: exactly the divisors of the three clocks' orders 30, 24 and 20":
            reg == div == [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30],
        "each regular class is a power of c', the day or the golden clock whose eigenvalues are all primitive d-th "
        "roots: its characteristic polynomial is Phi_d^(8/phi(d)), so its zeta_d-eigenspace has the dimension "
        "#{i : d | d_i} = 8/phi(d) of a regular eigenspace":
            pure and all(sum(e % d == 0 for e in DEGREES) == 8 // _phi(d) for d in regular()),
        "the centralizers, counted from the images of a Z[w]-basis of roots, have the orders prod_(d | d_i) d_i "
        "(Springer): 30, 24, 20, 288, 192, 600, 46080 and 155520 for d = 30, 24, 20, 12, 8, 5, 4 and 3; c'^2, c'^3 and "
        "c'^5 have the centralizers of c', g and s (c' = -(c'^2)^8, c'^3 = -g^3, c'^5 = -s^2), and -1 is central":
            counted == springer and list(counted.values()) == [30, 24, 20, 288, 192, 600, 46080, 155520]
            and np.array_equal(-P(P(c, 2), 8), c) and np.array_equal(P(c, 3), -P(g, 3))
            and np.array_equal(P(c, 5), -P(s, 2)) and np.array_equal(P(c, 15), -I8),
    }


def _beta(w, n):
    """For a root v with Z[w] v = E8: the coefficients of beta in Q[w] with <v, w^m v> = Tr(beta zeta^m), the trace
    matrix Tr(zeta^(i + j)), the data <v, w^m v> and the powers of w."""
    RB, C, _, _ = _roots()
    Pw = [spine.mpow(w, j) for j in range(n)]
    v = next(r for r in RB if abs(round(np.linalg.det(np.array([Pw[j] @ r for j in range(8)], dtype=float).T))) == 1)
    f = [int(v @ C @ Pw[m] @ v) for m in range(n)]
    T = sp.Matrix(8, 8, lambda i, j: int(np.trace(Pw[(i + j) % n])))
    return T.solve(sp.Matrix(f[:8])), T, f, Pw


def cyclotomic_lines():
    """(c): E8 is a line over Z[zeta30], Z[zeta24] and Z[zeta20], and each clock's normalizer is its Galois group."""
    RB, C, _, IP = _roots()
    k = cyclotomic.clocks()
    Cm = sp.Matrix(C.tolist())
    gens, forms, norms, normalizers = {}, {}, {}, {}
    want = {30: [sp.Rational(2, 15), sp.Rational(2, 15), sp.Rational(1, 15), 0],
            24: [sp.Rational(1, 12), sp.Rational(-1, 6), sp.Rational(1, 12), sp.Rational(1, 12)],
            20: [sp.Rational(1, 2), sp.Rational(3, 10), sp.Rational(-1, 10), sp.Rational(-1, 10)]}
    for n, w in ((30, k["c"]), (24, k["day"]), (20, k["golden"])):
        Pw = [spine.mpow(w, j) for j in range(n)]
        gens[n] = sum(abs(round(np.linalg.det(np.array([Pw[j] @ r for j in range(8)], dtype=float).T))) == 1
                      for r in RB)
        cvec, T, f, _ = _beta(w, n)
        mat = lambda j: sp.Matrix(Pw[j % n].tolist())
        beta = sum((cvec[j] * mat(j) for j in range(8)), sp.zeros(8))
        eta = mat(1) + mat(n - 1)
        forms[n] = (beta == sum((want[n][j] * eta ** j for j in range(4)), sp.zeros(8))
                    and all((beta * mat(m)).trace() == f[m] for m in range(n))
                    and beta == sum((cvec[j] * mat(-j) for j in range(8)), sp.zeros(8))
                    and (Cm * beta).is_positive_definite)
        norms[n] = (beta.det(), abs(T.det()), _disc(n))
        v = next(i for i in range(240) if abs(round(np.linalg.det(np.array([Pw[j] @ RB[i] for j in range(8)],
                                                                               dtype=float).T))) == 1)
        Wm = np.array([_perm(Pw[m]) for m in range(n)])
        fv = IP[v, Wm[:, v]]
        normalizers[n] = [int(np.sum(np.all(IP[np.arange(240)[:, None], Wm[[(u * m) % n for m in range(n)]].T] == fv,
                                            axis=1))) for u in range(n) if gcd(u, n) == 1]
    return {
        "the three clocks with cyclic centralizers make E8 a line over their cyclotomic integers: 240, 144 and 160 of "
        "the roots v have Z[w] v = E8 for w = c', the day and the golden clock (Phi_30, Phi_24 and Phi_20)":
            (gens[30], gens[24], gens[20]) == (240, 144, 160),
        "the forms are trace forms Tr(beta x ybar), eta = zeta + zeta^-1: beta = (2 + 2 eta + eta^2)/15 over "
        "Q(zeta30), (1 - 2 eta + eta^2 + eta^3)/12 over Q(zeta24) and (5 + 3 eta - eta^2 - eta^3)/10 over Q(zeta20), "
        "each real and totally positive":
            all(forms.values()),
        "each beta has norm 1/disc: 3^-4 5^-6, 2^-16 3^-4 and 2^-8 5^-6, so all three lines are unimodular":
            all(b == sp.Rational(1, dd) and t == dd for b, t, dd in norms.values())
            and [norms[n][2] for n in (30, 24, 20)] == [3 ** 4 * 5 ** 6, 2 ** 16 * 3 ** 4, 2 ** 8 * 5 ** 6],
        "each normalizer realizes its Galois group: for every unit u mod n exactly |C_W(w)| roots carry the data of "
        "w^u, so |N_W(<w>)| = 30 x 8 = 240, 24 x 8 = 192 and 20 x 8 = 160":
            normalizers == {30: [30] * 8, 24: [24] * 8, 20: [20] * 8},
    }


def no_sixteen():
    """(c), OBSTRUCTION: Q(zeta16), the fourth cyclotomic field of degree 8, does not carry E8."""
    x = sp.Symbol("x")
    S = sp.zeros(8)
    for i in range(7):
        S[i + 1, i] = 1
    S[0, 7] = -1
    comp = sp.Matrix(8, 8, lambda i, j: 1 if i == j + 1 else 0)
    coeffs = sp.Poly(sp.cyclotomic_poly(16, x), x).all_coeffs()[::-1]
    for i in range(8):
        comp[i, 7] = -coeffs[i]
    orders = Counter(spine.mat_order(W.astype(np.int64)) for W in elements(8))
    return {
        "Q(zeta16) carries Z^8, not E8: the signed 8-cycle of Z^8 has characteristic polynomial x^8 + 1 = Phi_16":
            sp.expand(S.charpoly(x).as_expr() - sp.cyclotomic_poly(16, x)) == 0,
        "W(E8) has no element of order 16: one would have the characteristic polynomial Phi_16, so its square would "
        "have Phi_8^2 and be a regular element of order 8, conjugate to d^3 (cited: Springer); but C_W(d^3), 192 "
        "elements, has orders 1, 2, 3, 4, 6, 8, 12 and 24 only":
            sp.expand((comp ** 2).charpoly(x).as_expr() - sp.cyclotomic_poly(8, x) ** 2) == 0
            and sum(orders.values()) == 192 and sorted(orders) == [1, 2, 3, 4, 6, 8, 12, 24],
    }


@functools.lru_cache(maxsize=None)
def sun_residue():
    """The quotient map E8 -> E8/(1 - s)E8 = F3^4 (four coordinates mod 3), the form <x, (s - s^2) y> in those
    coordinates, and the action of a stack of lattice maps on it."""
    s = regular()[3]
    _, C, _, _ = _roots()
    ker = sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix((I8 - s).T.tolist())).convert_to(sp.GF(3))
    ns = ker.nullspace().to_Matrix()
    Lq = np.array([[int(t) % 3 for t in ns.row(i)] for i in range(ns.shape[0])], dtype=np.int64)
    cols = next(c for c in itertools.combinations(range(8), 4) if round(np.linalg.det(Lq[:, c].astype(float))) % 3)
    Sinv = np.array(sp.Matrix(Lq[:, cols].tolist()).inv_mod(3).tolist(), dtype=np.int64)
    lifts = np.zeros((8, 4), dtype=np.int64)
    lifts[list(cols), :] = Sinv
    Om = (lifts.T @ C @ (s - spine.mpow(s, 2)) @ lifts) % 3
    return Lq, cols, Sinv, Om


def on_sun(Ws):
    """The 4 x 4 matrices over F3 by which lattice maps commuting with s act on the sun's momenta."""
    Lq, cols, Sinv, _ = sun_residue()
    out = []
    for lo in range(0, len(Ws), 20000):
        T = np.einsum("ij,njk->nik", Lq, np.asarray(Ws[lo:lo + 20000], dtype=np.int64)) % 3
        out.append((T[:, :, list(cols)] @ Sinv) % 3)
    return np.concatenate(out)


@functools.lru_cache(maxsize=None)
def sun_matrices():
    """The action of all of C_W(s) on the sun's momenta."""
    return on_sun(elements(3))


def _code(Q):
    return (Q.reshape(len(Q), -1) * (3 ** np.arange(Q.shape[1] * Q.shape[2]))).sum(axis=1)


def _order_mod(Q, p):
    P, I = np.eye(len(Q), dtype=np.int64), np.eye(len(Q), dtype=np.int64)
    for j in range(1, 200):
        P = (P @ Q) % p
        if np.array_equal(P, I):
            return j


@functools.lru_cache(maxsize=None)
def sun_geometry():
    """The sun's momenta as F9^2: phi = c' + c'^-1 on them, the projective points, the A2 over each, the totally
    isotropic lines and the ten F9-lines."""
    RB, C, _, IP = _roots()
    k = cyclotomic.clocks()
    Lq, _, _, Om = sun_residue()
    phi = on_sun((k["c"] + spine.inverse(k["c"]))[None])[0]
    pts = [p for p in itertools.product(range(3), repeat=4) if any(p)]
    proj = sorted({min(p, tuple((2 * np.array(p)) % 3)) for p in pts})
    F9 = [(a * np.eye(4, dtype=np.int64) + b * phi) % 3 for a in range(3) for b in range(3)]
    decad = []
    for p in pts:
        L = frozenset(tuple(((m @ np.array(p)) % 3).tolist()) for m in F9) - {(0,) * 4}
        if L not in decad:
            decad.append(L)
    rpt = [tuple(x) for x in ((RB @ Lq.T) % 3).tolist()]
    over = {q: [i for i in range(240) if rpt[i] in (q, tuple((2 * np.array(q)) % 3))] for q in proj}
    form = lambda a, b: int(np.array(a) @ Om @ np.array(b)) % 3
    iso = set()
    for a, b in itertools.combinations(proj, 2):
        if form(a, b) == 0:
            span = frozenset(min(tuple(((i * np.array(a) + j * np.array(b)) % 3).tolist()),
                                 tuple(((2 * i * np.array(a) + 2 * j * np.array(b)) % 3).tolist()))
                             for i in range(3) for j in range(3) if (i, j) != (0, 0))
            iso.add(span)
    return dict(phi=phi, proj=proj, decad=decad, rpt=rpt, over=over, form=form, iso=iso)


def prime_clocks():
    """(d): the half-turn, the sun and the tick, and their residue rings."""
    x = sp.Symbol("x")
    RB, C, _, _ = _roots()
    k = cyclotomic.clocks()
    c, P = k["c"], spine.mpow
    h = {2: P(c, 15), 3: P(c, 10), 5: P(c, 6)}
    snf = {p: [smith_normal_form(sp.Matrix((I8 - h[p]).tolist()), domain=sp.ZZ)[i, i] for i in range(8)] for p in h}
    mod = {p: sp.Poly(sp.cyclotomic_poly(30, x), x, modulus=p).factor_list()[1] for p in h}
    Qc3 = on_sun(c[None])[0]
    phi10 = sp.Poly(sp.cyclotomic_poly(10, x), x).all_coeffs()[::-1]
    pts3 = Counter(tuple(v) for v in ((RB @ sun_residue()[0].T) % 3).tolist())
    pts5 = Counter(cyclotomic.point(v) for v in RB)
    pts2 = Counter(tuple(v) for v in (RB % 2).tolist())
    return {
        "c' = c'^15 c'^10 c'^6 = (-1) s g, the half-turn, the sun and the tick (31 = 1 mod 30); under 144 k -> c'^k "
        "they are the circle's 2160, 1440 and 864, in its 2-clock <135>, its 27-clock <160> and its time clock <864>":
            np.array_equal(h[2] @ h[3] @ h[5], c) and np.array_equal(h[2], -I8)
            and [144 * 15, 144 * 10, 144 * 6] == [2160, 1440, 864] and 2160 % 135 == 0 and 1440 % 160 == 0
            and (135 * 32, 160 * 27) == (4320, 4320),
        "each fixes p^(8/(p-1)) momenta: 1 - h has Smith form 2^8, 1^4 3^4 and 1^6 5^2, so E8/(1 - h)E8 has 256, 81 "
        "and 25 points":
            snf == {2: [2] * 8, 3: [1] * 4 + [3] * 4, 5: [1] * 6 + [5] * 2},
        "these are the residue rings of Z[zeta30] at 2, 3 and 5: Phi_30 is a product of two quartics mod 2, the square "
        "of Phi_10 mod 3 and the fourth power of Phi_6 mod 5, so c' acts on the three quotients with order 30/p = 15, "
        "10 and 6, and they are F16 x F16, F81 and F25":
            sorted((f.degree(), e) for f, e in mod[2]) == [(4, 1), (4, 1)]
            and [(f.degree(), e) for f, e in mod[3]] == [(4, 2)] and [(f.degree(), e) for f, e in mod[5]] == [(2, 4)]
            and spine.mat_order(c) == 30 and np.array_equal(P(c, 15) % 2, I8)
            and _order_mod(Qc3, 3) == 10 and not (sum(int(a) * np.linalg.matrix_power(Qc3, j)
                                                      for j, a in enumerate(phi10)) % 3).any()
            and cyclotomic._order(cyclotomic.on_plane(c)) == 6,
        "the roots lie two over each of the 120 nonsingular half-periods, three over each of the sun's 80 nonzero "
        "momenta and ten over each of the tick's 24: 240 = 2 x 120 = 3 x 80 = 10 x 24":
            (len(pts2), set(pts2.values())) == (120, {2}) and (len(pts3), set(pts3.values())) == (80, {3})
            and (len(pts5), set(pts5.values())) == (24, {10}),
    }


def prime_residues():
    """(d): the centralizer of each prime clock acts on its residue as the isometry group of the residue form."""
    Q = sun_matrices()
    codes = _code(Q)
    _, fib = np.unique(codes, return_counts=True)
    _, _, _, Om = sun_residue()
    s = regular()[3]
    trivial = [i for i in np.nonzero(codes == _code(np.eye(4, dtype=np.int64)[None])[0])[0]]
    E = elements(3)
    kept = np.all(np.einsum("nji,jk,nkl->nil", Q, Om, Q) % 3 == Om[None], axis=(1, 2))
    _, _, C, _, _, _ = spine.frame()
    order_sp = lambda n, q: q ** (n * n) * prod(q ** (2 * i) - 1 for i in range(1, n + 1))
    order_o8 = 2 * 2 ** 12 * (2 ** 4 - 1) * prod(2 ** (2 * i) - 1 for i in range(1, 4))
    tick = cyclotomic.tick_normalizer()
    return {
        "C_W(s), 155520 elements, acts on the sun's 81 momenta by 51840 = 155520/3 matrices over F3, three elements to "
        "each, with kernel <s>":
            len(E) == 155520 and len(fib) == 51840 and set(fib.tolist()) == {3} and len(trivial) == 3
            and all(any(np.array_equal(E[i].astype(np.int64), spine.mpow(s, j)) for j in range(3)) for i in trivial),
        "all of them keep the alternating form <x, (s - s^2) y> mod 3, which is well defined on E8/(1 - s)E8 "
        "((1 - s)^T C (s - s^2) = 3 C s) and nondegenerate: C_W(s)/<s> is Sp(4,3), of order "
        "3^4 (3^2 - 1)(3^4 - 1) = 51840":
            kept.all() and np.array_equal((I8 - s).T @ C @ (s - spine.mpow(s, 2)), 3 * C @ s)
            and np.array_equal((Om + Om.T) % 3, np.zeros((4, 4), dtype=np.int64)) and not np.diag(Om).any()
            and round(np.linalg.det(Om.astype(float))) % 3 != 0 and order_sp(2, 3) == 51840,
        "likewise C_W(g), 600 elements, acts on the tick's plane as SL(2,5) = Sp(2,5), of order 600/5 = 120, and "
        "W(E8) acts on the half-periods keeping q(x) = <x, x>/2 mod 2, with |W(E8)| = 2 |GO8+(2)| = 2 x 348364800 "
        "(cited: W(E8)/<-1> = GO8+(2))":
            all(tick.values()) and order_sp(1, 5) == 120 and prod(DEGREES) == 2 * order_o8 and order_o8 == 348364800,
    }


def half_turn():
    """(e): the half-periods are F16 x F16, the two primes over 2."""
    RB, C, _, _ = _roots()
    k = cyclotomic.clocks()
    c = sp.Matrix(k["c"].tolist())

    def kernel(A):
        ns = sp.polys.matrices.DomainMatrix.from_Matrix(A).convert_to(sp.GF(2)).nullspace().to_Matrix()
        return np.array([[int(t) % 2 for t in ns.row(i)] for i in range(ns.shape[0])], dtype=np.int64)
    K1, K2 = kernel(c ** 4 + c + sp.eye(8)), kernel(c ** 4 + c ** 3 + sp.eye(8))
    span = lambda K: [tuple(((np.array(a) @ K) % 2).tolist()) for a in itertools.product(range(2), repeat=4)]
    q = lambda v: (int(np.array(v) @ C @ np.array(v)) // 2) % 2
    rank2 = sp.polys.matrices.DomainMatrix.from_Matrix(sp.Matrix(np.vstack([K1, K2]).tolist())).convert_to(sp.GF(2)).rank()
    singer = lambda K: next(j for j in range(1, 100) if all(np.array_equal((spine.mpow(k["c"], j) @ v) % 2, v)
                                                            for v in K))
    mirror = {tuple(((k["mirror"] @ np.array(v)) % 2).tolist()) for v in span(K1)}
    qs = Counter(q(v) for v in itertools.product(range(2), repeat=8))
    return {
        "E8/2E8 = F16 x F16: the kernels of c'^4 + c' + 1 and c'^4 + c'^3 + 1 mod 2 have dimension 4 each and are "
        "complementary, and c' is a Singer cycle of order 15 on each":
            K1.shape == K2.shape == (4, 8) and rank2 == 8 and singer(K1) == singer(K2) == 15,
        "both are totally singular for q(x) = <x, x>/2 mod 2, and the mirror (complex conjugation) swaps them: they "
        "are the two primes over 2":
            all(q(v) == 0 for v in span(K1) + span(K2)) and mirror == set(span(K2)),
        "q is 1 on 120 half-periods and 0 on 136 = 1 + 135: the hyperbolic form of GO8+(2), whose 120 nonsingular "
        "points carry the 240 roots, two each":
            qs == Counter({0: 136, 1: 120})
            and set(Counter(tuple(v) for v in (RB % 2).tolist()).values()) == {2}
            and all(q(v) == 1 for v in (RB % 2).tolist()),
    }


def sun():
    """(f): the sun's momenta are F9^2, with 40 A2 over their points and a spread of ten 4A2 frames."""
    RB, C, _, IP = _roots()
    S = sun_geometry()
    phi, proj, decad, over, form, iso = S["phi"], S["proj"], S["decad"], S["over"], S["form"], S["iso"]
    A2 = {q: cyclotomic._components(RB[over[q]], C) for q in proj}
    orth = lambda a, b: not IP[np.ix_(over[a], over[b])].any()
    decad_proj = [{min(p, tuple((2 * np.array(p)) % 3)) for p in L} for L in decad]
    return {
        "on the sun's momenta c' + c'^-1 satisfies phi^2 = phi + 1, the golden ratio, which is not in F3: so "
        "F9 = F3[phi] and the 81 momenta are the plane F9^2":
            np.array_equal((phi @ phi) % 3, (phi + np.eye(4, dtype=np.int64)) % 3)
            and all((a * a - a - 1) % 3 for a in range(3)),
        "the 40 projective points pull back to 40 A2 (six roots each, r, sr, s^2 r and their negatives) that partition "
        "the 240 roots, and two of them are orthogonal exactly when their points are orthogonal for the form":
            len(proj) == 40 and all(len(over[q]) == 6 and A2[q] == [6] for q in proj)
            and sum(len(over[q]) for q in proj) == 240
            and all(orth(a, b) == (form(a, b) == 0) for a, b in itertools.combinations(proj, 2)),
        "so the 40 totally isotropic lines, four points on each and four through each point (the generalized "
        "quadrangle W(3)), are 40 frames 4A2: four mutually orthogonal A2 of 24 roots":
            len(iso) == 40 and all(len(L) == 4 for L in iso)
            and all(sum(q in L for L in iso) == 4 for q in proj)
            and all(cyclotomic._components(RB[[i for q in L for i in over[q]]], C) == [6] * 4 for L in iso),
        "the ten F9-lines are totally isotropic and partition the 40 points: a spread of W(3), ten 4A2 frames that "
        "partition the 240 roots (the sun's decad)":
            len(decad) == 10 and all(len(L) == 8 for L in decad) and all(frozenset(P_) in iso for P_ in decad_proj)
            and sorted(q for P_ in decad_proj for q in P_) == proj,
    }


@functools.lru_cache(maxsize=None)
def _decad_action():
    """The F9-linear isometries commuting with s, their permutations of the ten F9-lines, and those of c', g and the
    day."""
    k = cyclotomic.clocks()
    S = sun_geometry()
    phi, decad = S["phi"], S["decad"]
    E = elements(3)
    Q = sun_matrices()
    lin = np.nonzero(np.all((Q @ phi) % 3 == (phi @ Q) % 3, axis=(1, 2)))[0]
    where = {p: i for i, L in enumerate(decad) for p in L}
    perm = lambda M: tuple(where[tuple(((M @ np.array(next(iter(L)))) % 3).tolist())] for L in decad)
    H = [perm(Q[i]) for i in lin]
    one = lambda M: perm(on_sun(M[None])[0])
    return dict(E=E, lin=lin, H=H, R=one(k["c"]), Rg=one(k["g"]), D=one(k["day"]), dets=_f9_dets(Q[lin], phi))


def _f9_dets(Q, phi):
    """The determinants over F9 = F3[phi] of F9-linear maps Q of F81 = F9^2, as pairs (a, b) = a + b phi."""
    v = np.array([1, 0, 0, 0], dtype=np.int64)
    basis = lambda w: np.array([v, (phi @ v) % 3, w, (phi @ w) % 3], dtype=np.int64).T
    w = next(np.array(w, dtype=np.int64) for w in itertools.product(range(3), repeat=4)
             if round(np.linalg.det(basis(np.array(w)).astype(float))) % 3)
    binv = np.array(sp.Matrix(basis(w).tolist()).inv_mod(3).tolist(), dtype=np.int64)
    cv, cw = ((binv @ ((Q @ u) % 3).T).T % 3 for u in (v, w))
    mul = lambda x, y: ((x[0] * y[0] + x[1] * y[1]) % 3, (x[0] * y[1] + x[1] * y[0] + x[1] * y[1]) % 3)
    out = []
    for a, b in zip(cv, cw):
        p, q = mul((a[0], a[1]), (b[2], b[3])), mul((b[0], b[1]), (a[2], a[3]))
        out.append((int(p[0] - q[0]) % 3, int(p[1] - q[1]) % 3))
    return out


def _mul(a, b):
    return tuple(a[b[i]] for i in range(len(b)))


def _iso(gens, images):
    """The map words in gens -> words in images, if it is a well-defined injective homomorphism (both act by
    composition a o b), as a dict on the generated group."""
    e = tuple(range(len(gens[0])))
    phi, frontier = {e: tuple(range(len(images[0])))}, [e]
    while frontier:
        new = []
        for h in frontier:
            for x, X in zip(gens, images):
                hx, img = _mul(h, x), _mul(phi[h], X)
                if hx in phi:
                    if phi[hx] != img:
                        return None
                else:
                    phi[hx] = img
                    new.append(hx)
        frontier = new
    return phi if len(set(phi.values())) == len(phi) else None


def _closure(gens, mul=_mul, e=None):
    """The group generated by gens: permutations under composition by default."""
    e = tuple(range(len(gens[0]))) if e is None else e
    S, new = {e}, [e]
    while new:
        new = [mul(a, g) for a in new for g in gens if mul(a, g) not in S]
        S |= set(new)
    return S


def _inv(a):
    return tuple(sorted(range(len(a)), key=lambda i: a[i]))


def _derived(S):
    """The commutator subgroup of a permutation group given by its elements."""
    return _closure(list({_mul(_mul(a, b), _mul(_inv(a), _inv(b))) for a in S for b in S}))


def decad():
    """(g): the 360 parent is the sun's PSL(2,9) on its ten 4A2 frames, with r the Coxeter clock and the doubling the
    day."""
    from . import dots
    D_ = _decad_action()
    E, lin, H, R, Rg, D, dets = D_["E"], D_["lin"], D_["H"], D_["R"], D_["Rg"], D_["D"], D_["dets"]
    G = set(H)
    kernel = {tuple(E[lin[j]].astype(np.int64).flatten()) for j, p in enumerate(H) if p == tuple(range(10))}
    c5 = {tuple(spine.mpow(cyclotomic.clocks()["c"], 5 * j).flatten()) for j in range(6)}
    A = dots._a6()
    r, t = A["r"], A["t"]
    dbl = tuple([(2 * i) % 5 for i in range(5)] + [5])
    order = lambda p: next(j for j in range(1, 50) if functools.reduce(_mul, [p] * j) == tuple(range(len(p))))
    invol = sorted(p for p in G if order(p) == 2)
    isos = [T for T in invol if (lambda f: f is not None and len(f) == 360)(_iso([r, t], [R, T]))]
    s6 = [T for T in isos if (lambda f: f is not None and len(f) == 720)(_iso([r, t, dbl], [R, T, D]))]
    affine = _closure([R, D])
    return {
        "the isometries that commute with the sun and with phi, F9-linear on its momenta, are 2160 = 3 x 720, each "
        "of determinant 1 over F9, so modulo <s> they are SL(2,9); they act on the ten F9-lines as a group of 360 with "
        "kernel <c'^5> = <-s>":
            len(lin) == 2160 and set(dets) == {(1, 0)} and len(G) == 360 and kernel == c5,
        "an isomorphism from the hub's A6 = <r, t> onto that group sends r to the Coxeter clock c' (the tick acts on "
        "the lines as c' does): the 360 parent is the sun's PSL(2,9) on its ten 4A2 frames":
            len(isos) == 10 and R == Rg and R in G,
        "on the ten frames c' is a fixed-point-free 5-element, and the day has order 4, conjugates it to its square "
        "(d c' d^-1 = c'^7) and lies outside the 360: the day-Coxeter group acts as AGL(1,5), and the isomorphism "
        "extends to S6 = PSigmaL(2,9) with the hub's doubling sent to the day":
            order(R) == 5 and not any(R[i] == i for i in range(10)) and order(D) == 4
            and _mul(_mul(D, R), tuple(sorted(range(10), key=lambda i: D[i]))) == _mul(R, R) and D not in G
            and len(affine) == 20 and len(affine & G) == 10 and len(s6) > 0,
    }


def parent_cover():
    """(h), OBSTRUCTION: no clock homomorphism covers A6."""
    from . import dots
    A = dots._a6()
    Gr, mul = A["G"], A["mul"]
    e = tuple(range(6))
    order = {a: next(j for j in range(1, 7) if functools.reduce(mul, [a] * j) == e) for a in Gr}
    orders = Counter(order.values())
    homs = sum(1 for a in Gr if 4320 % order[a] == 0)
    address = dots._address()
    not_hom = address(0) == e and any(address(j + 1) != mul(address(j), address(1)) for j in range(4319))
    perfect = _derived(Gr)
    k = cyclotomic.clocks()
    norm = _matrix_group([k["c"], k["day"], k["golden"], k["mirror"]])
    codes = lambda X: {tuple(M.flatten()) for M in X}
    series, N, derived = [len(norm)], norm, False
    while series[-1] > 1 and len(series) < 6:
        N = _commutators(N)
        series.append(len(N))
        if series[-1] == 30:
            derived = codes(N) == {tuple(spine.mpow(k["c"], j).flatten()) for j in range(30)}
    G120 = _matrix_group([k["c"], k["day"]])
    agl = _closure([(1, 2, 3, 4, 0), (0, 2, 4, 1, 3)])
    agl1 = _derived(agl)
    agl2 = _derived(agl1)
    gl = [np.array([[a, b], [c, d]], dtype=np.int64) for a, b, c, d in itertools.product(range(5), repeat=4)
          if (a * d - b * c) % 5]
    hexad = {cyclotomic.on_lines(M) for M in gl}
    even = [p for p in hexad if Permutation(list(p)).is_even]
    return {
        "A6 has 1, 45, 80, 90 and 144 elements of orders 1 to 5, all dividing 4320, so Z/4320 has exactly 360 "
        "homomorphisms to A6, one for each image of 1, and each has a cyclic image of at most five elements: the "
        "address map's orbits 5^4 10^2 20^16 add to 360, but no clock homomorphism covers A6, and the address map, "
        "onto all 360, is not a homomorphism":
            orders == Counter({1: 1, 2: 45, 3: 80, 4: 90, 5: 144}) and homs == 360 and max(orders) == 5
            and 5 * 4 + 10 * 2 + 20 * 16 == 360 and not_hom,
        "every clock lies in the normalizer of <c'>, 240 elements, whose derived series 240 > 30 > 1 ends at the "
        "identity (its commutator subgroup is <c'>), so every clock group, the day-Coxeter group of 120 among them, is "
        "solvable, as are the circle (abelian) and AGL(1,5) (20 > 5 > 1); A6 is perfect, its commutators generate all "
        "360, so no clock group maps onto it":
            series == [240, 30, 1] and derived and len(G120) == 120 and codes(G120) <= codes(norm)
            and (len(agl), len(agl1), len(agl2)) == (20, 5, 1) and len(perfect) == 360,
        "on the tick's hexad the seed acts only through GL(2,5), whose image on the six lines is PGL(2,5): 120 "
        "permutations, of which the 60 even ones are PSL(2,5), one sixth of A6. A6 is reached by the sun's symmetry, "
        "which is not a clock":
            len(gl) == 480 and len(hexad) == 120 and len(even) == 60,
    }


def _matrix_group(gens):
    """The finite group of lattice isometries generated by gens, as an array of matrices."""
    seen = {tuple(I8.flatten()): I8}
    new = [I8]
    while new:
        nxt = []
        for a in new:
            for g in gens:
                b = a @ g
                kb = tuple(b.flatten())
                if kb not in seen:
                    seen[kb] = b
                    nxt.append(b)
        new = nxt
    return np.array(list(seen.values()))


def _commutators(G):
    """The subgroup generated by the commutators a b a^-1 b^-1 of the matrix group G."""
    Ginv = np.array([spine.inverse(M) for M in G])
    AB = np.einsum("aij,bjk->abik", G, G)
    X = np.einsum("abij,ajk->abik", AB, Ginv)
    Y = np.einsum("abij,bjk->abik", X, Ginv).reshape(-1, 8, 8)
    _, first = np.unique(Y.reshape(len(Y), -1), axis=0, return_index=True)
    return _matrix_group(list(Y[first]))


def run():
    from . import gates
    from .record import Report
    rep = Report("26-primes")
    T, OB = gates.THEOREM, gates.OBSTRUCTION
    for fn, status in ((regular_clocks, T), (cyclotomic_lines, T), (no_sixteen, OB), (prime_clocks, T),
                       (prime_residues, T), (half_turn, T), (sun, T), (decad, T), (parent_cover, OB)):
        for name, ok in fn().items():
            rep.add(name, status, ok)
    rep.add("cited: the order of W(E8) is the product of its degrees; Lehrer-Springer's criterion for regular numbers "
            "and Springer's theorems (regular elements of one order are conjugate, and their centralizers have the "
            "orders of the degrees, replayed here); W(E8)/<-1> = GO8+(2)", gates.SELECTED_REFERENCE, True)
    return rep
