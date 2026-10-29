"""Layer 27. The four places: the bath, the qubits, the parent and the carrier.

The seed (E8, c') is read at four places, and each carries one sector of the model:

    the real place   E8 x R with the bath Delta on the dual torus, band [0, 256]     (layers 3, 8, 23)
    the prime 2      the half-turn's 256 momenta, the four-qubit real Paulis          (layer 22: Pauli algebra, GKSL)
    the prime 3      the sun's 81 momenta, F9^2, whose ten lines are the decad       (layer 26: the 360 parent)
    the prime 5      the tick's 25 momenta, F25, whose six lines are the hexad       (layer 25: the carrier)

(a) One formula joins the real place to the three primes. At a fixed momentum of a prime clock the band is
    eps = 240 - sum_r chi(r), with chi the matching character of the residue space.
    - At 5 and at 3 the roots lie m = 10 and m = 3 over every nonzero residue point. So every nontrivial character
      sums to -m, and eps = 240 + m: 250 on the tick's 24 and 243 on the sun's 80.
    - At 2 the roots are the 120 nonsingular points of the half-period quadric, two each. The character sums are -16
      and +16 as q(y) = 0 or 1, so eps = 256 on the 135 singular and 224 on the 120 nonsingular half-periods: the
      band's top and its saddle.
    Every one of these momenta is a critical point of the band, since a clock without eigenvalue 1 fixes the gradient.
(b) The golden ratio runs through all three primes. Phi = 1 + g + g^4 is integral, with Phi^2 = Phi + 1.
    - At 5 it is the scalar 3, a double root: ramified, and (2 Phi - 1)^2 = 5 is the Gauss sum.
    - At 3 it generates F9 = F3[Phi], the decad's field.
    - At 2 it is a cube root of unity, F4 = F2[Phi], on each prime over 2.
    The Fibonacci companion B has Pisano periods 3, 8 and 20 at 2, 3 and 5.
(c) The qubits. Under layer 22's Pauli map the two primes over 2 are two complementary stabilizer groups of 16
    commuting symmetric real Paulis. Two Paulis commute exactly when their half-periods have even inner product, c'
    keeps both groups and the mirror swaps them. W(E8)/<-1> = GO8+(2) is the real Clifford group of four qubits
    modulo the Paulis (cited: Nebe, Rains and Sloane).
(d) What the places cannot give (OBSTRUCTION). An element of order n of GL8(Z) needs psi(n) <= 8, where psi(n) is the
    sum of phi over the prime powers of n, less 1 when n = 2 mod 4.
    - The memory clock has order 90 and psi(90) = 10, so no lattice clock of the seed runs it.
    - The circle has psi(4320) = 38. Its largest images in GL8(Z) have order 60, 40 or 36, and the element orders of
      W(E8) stop at 30 (cited), the Coxeter clock.
    - AIR_801 has determinant 12402, so it is no lattice clock; only its residue mod 5 is the seed's.
"""

import functools
import itertools
from collections import Counter
from math import gcd

import numpy as np
import sympy as sp

from . import counts, cyclotomic, primes, spine

I8 = np.eye(8, dtype=np.int64)


def _fixed_momenta(h, n):
    """The n momenta y (mod E8, standard coordinates) with h y = y mod E8, for a lattice clock h without eigenvalue 1."""
    B, Binv, *_ = spine.frame()
    hs = B @ h @ Binv
    lift = np.linalg.inv(np.eye(8) - hs)
    seen = {}
    for c in itertools.product(range(-2, 3), repeat=8):
        y = lift @ (B @ np.array(c, dtype=float))
        key = tuple(np.round((Binv @ y) % 1.0, 6) % 1.0)
        seen.setdefault(key, y)
        if len(seen) == n:
            return list(seen.values())
    return list(seen.values())


def band_at_places():
    """(a): the band at the prime clocks' fixed momenta, from the characters of the residue spaces."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    k = cyclotomic.clocks()
    P = spine.mpow
    clocks = {5: (k["g"], 25), 3: (P(k["c"], 10), 81), 2: (P(k["c"], 15), 256)}
    band = lambda y: float(240 - np.cos(2 * np.pi * (R @ y)).sum())
    grad = lambda y: float(np.linalg.norm((np.sin(2 * np.pi * (R @ y))[:, None] * R).sum(axis=0)))
    values, critical = {}, {}
    for p, (h, n) in clocks.items():
        ys = _fixed_momenta(h, n)
        values[p] = Counter(int(round(band(y))) for y in ys) if len(ys) == n else None
        critical[p] = len(ys) == n and max(grad(y) for y in ys) < 1e-9
    Lq5 = cyclotomic.residue()[0]
    Lq3 = primes.sun_residue()[0]
    sums = {}
    for p, pts, dim in ((5, (RB @ Lq5.T) % 5, 2), (3, (RB @ Lq3.T) % 3, 4)):
        out = Counter()
        for y in itertools.product(range(p), repeat=dim):
            if any(y):
                t = Counter(int(x @ np.array(y)) % p for x in pts)
                out[(t[0] - t[1]) if len({t[a] for a in range(1, p)}) == 1 else None] += 1
        sums[p] = out
    Ci = C.astype(np.int64)
    q = lambda v: (int(v @ Ci @ v) // 2) % 2
    half = Counter()
    for y in itertools.product(range(2), repeat=8):
        if any(y):
            y = np.array(y)
            t = Counter(int(x @ Ci @ y) % 2 for x in RB % 2)
            half[(q(y), t[0] - t[1])] += 1
    return {
        "on the dual torus the band at the prime clocks' fixed momenta is 0 and 250 (24 times) at the tick, 0 and 243 "
        "(80 times) at the sun, and 0, 224 (120 times) and 256 (135 times) at the half-turn, and every one of these "
        "momenta is a critical point (a clock without eigenvalue 1 fixes the gradient)":
            values == {5: Counter({0: 1, 250: 24}), 3: Counter({0: 1, 243: 80}), 2: Counter({0: 1, 224: 120, 256: 135})}
            and all(critical.values()),
        "those values are character sums on the residue spaces, eps = 240 - sum_r chi(r): with ten roots over each of the "
        "tick's 24 nonzero residue points and three over each of the sun's 80, every nontrivial character sums to -10 "
        "and -3, so eps = 240 + 10 = 250 and 240 + 3 = 243":
            sums == {5: Counter({-10: 24}), 3: Counter({-3: 80})} and 240 + 10 == 250 and 240 + 3 == 243,
        "at the prime 2 the roots are the nonsingular points of the half-period quadric, two each, and a character "
        "sums to -16 when q(y) = 0 and +16 when q(y) = 1: eps = 256 on the 135 singular and 224 on the 120 nonsingular "
        "half-periods, the band's top and its saddle":
            half == Counter({(0, -16): 135, (1, 16): 120}) and 240 + 16 == 256 and 240 - 16 == 224,
    }


def golden_places():
    """(b): the golden ratio Phi = 1 + g + g^4 at the three primes, and the Fibonacci companion's Pisano periods."""
    k = cyclotomic.clocks()
    g = k["g"]
    Phi = I8 + g + spine.mpow(g, 4)
    I4 = np.eye(4, dtype=np.int64)
    Q3 = primes.on_sun(Phi[None])[0]
    phi3 = primes.sun_geometry()["phi"]
    field = lambda X: {tuple(((a * I4 + b * X) % 3).flatten()) for a in range(3) for b in range(3)}
    c = sp.Matrix(k["c"].tolist())

    def kernel(A):
        ns = sp.polys.matrices.DomainMatrix.from_Matrix(A).convert_to(sp.GF(2)).nullspace().to_Matrix()
        return np.array([[int(t) % 2 for t in ns.row(i)] for i in range(ns.shape[0])], dtype=np.int64)
    span = lambda K: {tuple(((np.array(a) @ K) % 2).tolist()) for a in itertools.product(range(2), repeat=4)}
    primes2 = [span(kernel(c ** 4 + c + sp.eye(8))), span(kernel(c ** 4 + c ** 3 + sp.eye(8)))]
    keeps = all({tuple(((Phi @ np.array(v)) % 2).tolist()) for v in S} == S for S in primes2)
    Bf = sp.Matrix([[1, 1], [1, 0]])
    pisano = [next(n for n in range(1, 100) if (Bf ** n).applyfunc(lambda e, p=p: e % p) == sp.eye(2)) for p in (2, 3, 5)]
    G = 2 * Phi - I8
    return {
        "the golden ratio Phi = 1 + g + g^4 is integral on E8 with Phi^2 = Phi + 1, and 2 Phi - 1 = g + g^4 - g^2 - g^3 is "
        "the Gauss sum, of square 5":
            np.array_equal(Phi @ Phi, Phi + I8) and np.array_equal(G @ G, 5 * I8)
            and np.array_equal(G, g + spine.mpow(g, 4) - spine.mpow(g, 2) - spine.mpow(g, 3)),
        "at 5 it is ramified: on the tick's plane Phi is the scalar 3, and x^2 - x - 1 = (x - 3)^2 mod 5; at 3 it is "
        "inert: on the sun's momenta Phi is not in F3, and F3[Phi] is the F9 of the decad; at 2 it is inert: on the "
        "half-periods Phi^2 + Phi + 1 = 0, and Phi keeps both primes over 2, a cube root of unity in F4 = F2[Phi]":
            np.array_equal(cyclotomic.on_plane(Phi), 3 * np.eye(2, dtype=np.int64))
            and sp.expand(sp.Poly((sp.Symbol("x") - 3) ** 2 - (sp.Symbol("x") ** 2 - sp.Symbol("x") - 1), sp.Symbol("x"),
                                  modulus=5).as_expr()) == 0
            and np.array_equal((Q3 @ Q3) % 3, (Q3 + I4) % 3) and not any(np.array_equal(Q3 % 3, a * I4) for a in range(3))
            and field(Q3) == field(phi3)
            and not ((Phi @ Phi + Phi + I8) % 2).any() and keeps and not np.array_equal(Phi % 2, I8),
        "the Fibonacci companion B = [[1, 1], [1, 0]] has Pisano periods 3, 8 and 20 at 2, 3 and 5: the orders of a "
        "generator of F4^x and F9^x, and at 5 a scalar 3 times a unipotent, (B - 3)^2 = 0 mod 5":
            pisano == [3, 8, 20] and ((Bf - 3 * sp.eye(2)) ** 2).applyfunc(lambda e: e % 5) == sp.zeros(2)
            and (Bf - 3 * sp.eye(2)).applyfunc(lambda e: e % 5) != sp.zeros(2),
    }


def qubit_primes():
    """(c): the two primes over 2 are complementary stabilizer groups of the four-qubit real Paulis."""
    B, Binv, *_ = spine.frame()
    k = cyclotomic.clocks()
    c = sp.Matrix(k["c"].tolist())

    def kernel(A):
        ns = sp.polys.matrices.DomainMatrix.from_Matrix(A).convert_to(sp.GF(2)).nullspace().to_Matrix()
        return np.array([[int(t) % 2 for t in ns.row(i)] for i in range(ns.shape[0])], dtype=np.int64)
    span = lambda K: [tuple(((np.array(a) @ K) % 2).tolist()) for a in itertools.product(range(2), repeat=4)]
    S1, S2 = span(kernel(c ** 4 + c + sp.eye(8))), span(kernel(c ** 4 + c ** 3 + sp.eye(8)))
    alpha2 = np.array(counts.SIMPLE_ROOTS_X2)
    cartan = alpha2 @ alpha2.T // 4
    single = counts._letters()
    gens = [functools.reduce(np.kron, [single[counts.LETTERS.index(a)] for a in w])
            for w in ["".join(counts.LETTERS[a] for a in w) for w in counts.dynkin_paulis()]]
    phi = lambda x: functools.reduce(lambda a, b: a @ b, [gens[i] for i in range(8) if x[i]], np.eye(16, dtype=np.int64))
    dynkin = lambda v: tuple(int(t) % 2 for t in np.rint((2 * (B @ np.array(v, dtype=float))) @ np.linalg.inv(alpha2)))
    D1, D2 = [dynkin(v) for v in S1], [dynkin(v) for v in S2]
    M1, M2 = [phi(x) for x in D1], [phi(x) for x in D2]
    commute = lambda a, b: np.array_equal(a @ b, b @ a)
    gen_rule = all(commute(gens[i], gens[j]) == (cartan[i, j] % 2 == 0) for i in range(8) for j in range(8))
    keep = lambda M, S: {tuple(((M @ np.array(v)) % 2).tolist()) for v in S}
    return {
        "layer 22's Pauli map sends the simple roots to eight real Pauli strings that anticommute exactly when the roots "
        "are joined in the Dynkin diagram, so two products phi(x), phi(y) commute exactly when <x, y> is even, and the "
        "transpose sign of phi(x) is (-1)^q(x)":
            gen_rule and all(np.array_equal(phi(x).T, (1 - 2 * ((np.array(x) @ cartan @ np.array(x) // 2) % 2)) * phi(x))
                             for x in D1 + D2),
        "the two primes over 2 go to two stabilizer groups: 16 commuting symmetric real Paulis each, meeting only in the "
        "identity, and every half-period is uniquely a sum of one from each, so every real Pauli is plus or minus a "
        "product of an element of each group":
            all(commute(a, b) for a in M1 for b in M1) and all(commute(a, b) for a in M2 for b in M2)
            and all(np.array_equal(a, a.T) for a in M1 + M2) and set(D1) & set(D2) == {(0,) * 8}
            and len({tuple((np.array(a) + np.array(b)) % 2) for a in D1 for b in D2}) == 256,
        "the Coxeter clock keeps both stabilizer groups, a Singer cycle of order 15 on each, and the mirror exchanges "
        "them; W(E8)/<-1> = GO8+(2) is the real Clifford group of four qubits modulo the Paulis (cited: Nebe, Rains and "
        "Sloane)":
            keep(k["c"], S1) == set(S1) and keep(k["c"], S2) == set(S2) and keep(k["mirror"], S1) == set(S2)
            and next(j for j in range(1, 31) if all(np.array_equal((spine.mpow(k["c"], j) @ np.array(v)) % 2, np.array(v))
                                                   for v in S1)) == 15,
    }


def _psi(n):
    """The least d with an element of order n in GL_d(Z): the sum of phi(p^a) over p^a || n, less 1 if n = 2 mod 4 and
    n > 2."""
    f = sp.factorint(n)
    total = sum(int(sp.totient(p ** a)) for p, a in f.items())
    return total - (1 if n % 4 == 2 and n > 2 else 0)


def limits():
    """(d), OBSTRUCTION: what no clock of the seed can run."""
    divisors = [d for d in range(1, 4321) if 4320 % d == 0]
    allowed = sorted(d for d in divisors if _psi(d) <= 8)
    air = sp.Matrix([[108, 801], [106, 901]])
    return {
        "an element of order n of GL8(Z) needs psi(n) <= 8 (psi sums phi over the prime powers of n, less 1 when n = 2 "
        "mod 4): psi(30) = 6 for the Coxeter clock, psi(24) = psi(20) = 6 for the day and the golden clock, but "
        "psi(90) = 10, so the memory clock of order 90 is run by no lattice clock of the seed":
            (_psi(30), _psi(24), _psi(20), _psi(90)) == (6, 6, 6, 10) and _psi(2) == 1 and _psi(6) == 2,
        "the circle has psi(4320) = 38: its images in GL8(Z) have orders among the divisors with psi <= 8, the largest "
        "60, 40 and 36, and the element orders of W(E8) stop at 30 (cited), the Coxeter clock's <144>; the circle stays "
        "an input":
            _psi(4320) == 38 and allowed[-3:] == [36, 40, 60],
        "AIR_801 = [[108, 801], [106, 901]] has determinant 12402 = 2 x 3^2 x 13 x 53, so it is no lattice clock; only its "
        "residue mod 5, minus the day, is the seed's":
            air.det() == 12402 and sp.factorint(12402) == {2: 1, 3: 2, 13: 1, 53: 1},
    }


def sectors():
    """The four places carry the four sectors: each sector's dot is built from the seed through its place."""
    from . import unify
    path = lambda d: unify._root(d, unify.DERIVATION)[1]
    return {
        "the derivation reaches each sector through its place: the bath from E8 itself (the real place), the Pauli "
        "algebra and GKSL through the half-periods (2), the 360 parent through the sun's decad (3), and the carrier "
        "through the tick's residue plane (5)":
            path("bath") == ["bath", "E8"] and "halfper" in path("pauli") and "halfper" in path("gksl")
            and "sun" in path("parent") and "residue" in path("carrier") and "residue" in path("source")
            and path("halfper")[1] == "cyclo" and path("sun")[1] == "cyclo",
    }


def run():
    from . import gates
    from .record import Report
    rep = Report("27-places")
    T, OB = gates.THEOREM, gates.OBSTRUCTION
    for fn, status in ((band_at_places, T), (golden_places, T), (qubit_primes, T), (limits, OB), (sectors, T)):
        for name, ok in fn().items():
            rep.add(name, status, ok)
    rep.add("cited: W(E8)/<-1> = GO8+(2), the real Clifford group of four qubits modulo the Paulis (Nebe, Rains and "
            "Sloane); the element orders of W(E8) are at most 30", gates.SELECTED_REFERENCE, True)
    return rep
