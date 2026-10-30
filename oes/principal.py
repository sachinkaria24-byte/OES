"""Layer 28. The principal circle: the canon's circle is a circle of the seed's momenta.

No lattice clock runs the canon's circle Z/4320 (layer 27: psi(4320) = 38 > 8). A circle of momenta does. E8 is
unimodular, so the bath's momenta live on the torus R^8 / E8, and the Weyl vector rho, the sum of the fundamental
weights, is a lattice vector with <r, rho> = ht(r) for every root r. The torus is the maximal torus of the compact
group E8, the band is eps = 248 - chi with chi its adjoint character, and the circle is t -> t rho.

(a) The principal circle. In the root basis rho = (46, 68, 91, 135, 110, 84, 57, 29), with |rho|^2 = 620 and coprime
    coordinates, so k -> k rho / 4320 embeds Z/4320 in the momentum torus. The positive roots of height j number
    #{i : m_i >= j}, the partition dual to the exponents 1, 7, 11, 13, 17, 19, 23, 29 (Kostant), and the highest root
    has height 29 = h - 1.
(b) The steps of the regular orders. The point rho/d acts on the adjoint representation g = t + sum_r g_r by
    zeta_d^ht(r) on g_r. For each of the thirteen regular numbers d its spectrum is that of a lift of the regular
    clock w_d: each primitive d-th root 8/phi(d) times from the clock on t, plus 240/d copies of every d-th root from
    the 240/d free orbits of w_d on the roots. At d = 30 Kostant's theorem (cited) makes exp(2 pi i rho/30) conjugate
    to a lift of c'. So the canon's step 144 is the Coxeter clock's lift, and its steps 180 and 216 carry the spectra
    of the day and the golden clock; 216 is the canon's golden step B^k -> 216k.
(c) The band on the circle. At the step 4320/d of a regular order the Ramanujan sum gives eps = 248 - 8 mu(d)/phi(d):
    256, 252, 248, 250, 244, 248, 246, 248, 247, 248, 248 and 249 for d = 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24 and 30.
    The circle's highest point is the band's top 256, at the half-turn 2160 alone.
(d) The critical steps are the canon's small clocks. The band is critical on the circle exactly at its nine elements
    of order 2 to 5, where the centralizer has full rank 8 and dimension 240/d:
        2160                    order 2   D8        eps 256   the half-turn, the 2-clock's involution
        1440, 2880              order 3   A8        eps 252   the 27-clock's order-3 steps
        1080, 3240              order 4   D5 + A3   eps 248   the observer clock's generators
        864, 1728, 2592, 3456   order 5   A4 + A4   eps 250   the time clock
    These are the alcove's vertices of marks 2, 3, 4 and 5 and four of the eleven critical families of layer 16. The
    time clock's centralizer has the carrier's root system A4 + A4, in the family of the tick's 24 fixed momenta.
    Every step of order above 29 is regular: 4234 of the 4319 nonzero steps.
What stays the canon's: the number 4320 and its stage indices. The circle's Coxeter step and its small clocks are the
seed's.
"""

import functools
from collections import Counter
from math import gcd

import numpy as np
import sympy as sp

from . import handover, primes, spine

N = 4320
EXPONENTS = [1, 7, 11, 13, 17, 19, 23, 29]


@functools.lru_cache(maxsize=None)
def weyl_vector():
    """rho in the root basis and in standard coordinates, and the heights of the 240 roots."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho = Cinv @ np.ones(8, dtype=np.int64)
    return rho, B @ rho, RB @ C @ rho


def _band(x):
    R = spine.frame()[4]
    return 240 - np.cos(2 * np.pi * (R @ x)).sum()


def _gradient(x):
    R = spine.frame()[4]
    return (np.sin(2 * np.pi * (R @ x))[:, None] * R).sum(axis=0)


def _phi(d):
    return sum(1 for j in range(1, d + 1) if gcd(j, d) == 1)


def circle():
    """(a): rho is a primitive lattice vector whose pairing with the roots is the height."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, _, ht = weyl_vector()
    pos = Counter(int(h) for h in ht if h > 0)
    return {
        "the Weyl vector rho has <alpha_i, rho> = 1 for every simple root, root coordinates (46, 68, 91, 135, 110, 84, "
        "57, 29), |rho|^2 = 620 and coprime coordinates, and <r, rho> is the height of every root r":
            np.array_equal(C @ rho, np.ones(8, dtype=np.int64)) and rho.tolist() == [46, 68, 91, 135, 110, 84, 57, 29]
            and int(rho @ C @ rho) == 620 and np.gcd.reduce(rho) == 1 and np.array_equal(ht, RB.sum(axis=1)),
        "so k -> k rho / 4320 embeds the circle Z/4320 in the momentum torus R^8 / E8: every step k has order "
        "4320 / gcd(k, 4320) there, as on the circle":
            all(int(np.lcm.reduce([N // gcd(N, k * int(c)) for c in rho])) == N // gcd(N, k) for k in range(1, N)),
        "the positive roots of height j number #{i : m_i >= j} for the exponents 1, 7, 11, 13, 17, 19, 23, 29 (Kostant's "
        "dual partition), and the highest root has height 29 = h - 1":
            [pos[j] for j in range(1, 30)] == [sum(m >= j for m in EXPONENTS) for j in range(1, 30)]
            and max(pos) == 29 and sum(pos.values()) == 120,
    }


def regular_steps():
    """(b): at rho/d the adjoint spectrum is that of a lift of the regular clock of order d."""
    _, _, ht = weyl_vector()
    out, free = {}, {}
    for d, w in primes.regular().items():
        spec = Counter(int(h) % d for h in ht)
        spec[0] += 8
        lift = {j: 240 // d + (8 // _phi(d) if gcd(j, d) == 1 else 0) for j in range(d)}
        out[d] = all(spec[j] == lift[j] for j in range(d))
        perm = primes._perm(w)
        sizes, seen = Counter(), set()
        for i in range(240):
            n, j = 0, i
            while j not in seen:
                seen.add(j)
                j, n = int(perm[j]), n + 1
            if n:
                sizes[n] += 1
        free[d] = sizes == Counter({d: 240 // d})
    return {
        "for each of the thirteen regular numbers d, rho/d acts on the adjoint representation with the spectrum of a "
        "lift of the regular clock w_d: each primitive d-th root 8/phi(d) times from w_d on the Cartan, and 240/d "
        "copies of every d-th root from the roots":
            sorted(out) == [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30] and all(out.values()),
        "w_d turns the 240 roots in 240/d free orbits of length d: 8 for c' (30), 10 for the day (24) and 12 for the "
        "golden clock (20)":
            all(free.values()) and (240 // 30, 240 // 24, 240 // 20) == (8, 10, 12),
        "so the canon's steps 144, 180 and 216 = 4320/30, 4320/24 and 4320/20 carry the spectra of c', the day and the "
        "golden clock, and 216 is the canon's golden step B^k -> 216k":
            (N // 30, N // 24, N // 20) == (144, 180, 216) and all(out[d] for d in (30, 24, 20)),
    }


def band_on_circle():
    """(c): the band at the regular steps, and its top."""
    _, rs, _ = weyl_vector()
    exact = {d: 248 - sp.Rational(8 * sp.mobius(d), _phi(d)) for d in primes.regular() if d > 1}
    ramanujan = all(sp.nsimplify(sp.simplify(sum(sp.exp(2 * sp.pi * sp.I * j / d) for j in range(d) if gcd(j, d) == 1)))
                    == sp.mobius(d) for d in exact)
    values = [_band(rs * k / N) for k in range(N)]
    return {
        "at the step 4320/d of a regular order the band is 248 - chi = 248 - 8 mu(d)/phi(d) (the Ramanujan sum of the "
        "primitive d-th roots is mu(d)): 256, 252, 248, 250, 244, 248, 246, 248, 247, 248, 248 and 249 for d = 2, 3, "
        "4, 5, 6, 8, 10, 12, 15, 20, 24 and 30":
            ramanujan and all(abs(values[N // d] - float(e)) < 1e-9 for d, e in exact.items())
            and [exact[d] for d in sorted(exact)] == [256, 252, 248, 250, 244, 248, 246, 248, 247, 248, 248, 249],
        "the circle's highest point is the band's top 256, at the half-turn 2160 alone":
            abs(max(values) - 256) < 1e-9 and [k for k in range(N) if values[k] > 256 - 1e-6] == [2160],
    }


def critical_steps():
    """(d): the band is critical on the circle exactly at the steps of order 2 to 5."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, rs, ht = weyl_vector()
    grads = np.array([np.linalg.norm(_gradient(rs * k / N)) for k in range(N)])
    crit = [k for k in range(1, N) if grads[k] < 1e-8]
    kinds = {k: handover.stabiliser(R, rs * k / N)[0] for k in crit}
    census = {t: f for (_, t), f in handover.critical_census().items()}
    theta = RB[int(np.argmax(ht))]
    marks = theta.tolist()
    vertex = {i: handover.stabiliser(R, B @ Cinv[:, i] / marks[i])[0] for i in range(8)}
    regular = [k for k in range(1, N) if handover.stabiliser(R, rs * k / N)[1] == 1]
    rank = lambda k: np.linalg.matrix_rank(R[np.abs(R @ (rs * k / N) - np.round(R @ (rs * k / N))) < 1e-9])
    return {
        "the band is critical on the circle exactly at its nine nonzero elements of order 2 to 5: 2160 (D8), 1440 and "
        "2880 (A8), 1080 and 3240 (D5 + A3) and 864, 1728, 2592, 3456 (A4 + A4)":
            crit == [864, 1080, 1440, 1728, 2160, 2592, 2880, 3240, 3456]
            and kinds == {2160: "D8", 1440: "A8", 2880: "A8", 1080: "D5+A3", 3240: "D5+A3", 864: "A4+A4", 1728: "A4+A4",
                          2592: "A4+A4", 3456: "A4+A4"}
            and sorted({N // gcd(k, N) for k in crit}) == [2, 3, 4, 5] and min(grads[k] for k in range(1, N) if k not in crit) > 1e-3,
        "there the centralizer has full rank 8 and dimension 8 + #roots = 240/d (120, 80, 60, 48), and the four types "
        "are the critical families D8 (eps 256, 135 points, index 8), A8 (252, 1920, 8), D5 + A3 (248, 15120, 3) and "
        "A4 + A4 (250, 48384, 4) of layer 16":
            all(rank(k) == 8 for k in crit)
            and {N // gcd(k, N): 8 + int(np.sum(np.abs(R @ (rs * k / N) - np.round(R @ (rs * k / N))) < 1e-9)) for k in crit}
            == {2: 120, 3: 80, 4: 60, 5: 48}
            and [(round(240 - census[t]["lambda"]), census[t]["orbit"], census[t]["index"]) for t in ("D8", "A8", "D5+A3", "A4+A4")]
            == [(256, 135, 8), (252, 1920, 8), (248, 15120, 3), (250, 48384, 4)],
        "they are the alcove's vertices of marks 2, 3, 4 and 5: the vertex omega_i / a_i (a the highest root's "
        "coefficients 2, 3, 4, 6, 5, 4, 3, 2) has the type D8, A8, D5 + A3 and A4 + A4 at a node of mark 2, 3, 4 and 5":
            marks == [2, 3, 4, 6, 5, 4, 3, 2]
            and all(any(vertex[i] == t and marks[i] == m for i in range(8))
                    for t, m in (("D8", 2), ("A8", 3), ("D5+A3", 4), ("A4+A4", 5))),
        "the time clock <864> is the A4 + A4 vertex, the carrier's root system and the family of the tick's 24 fixed "
        "momenta; the observer clock <1080> is D5 + A3 with its square the D8 half-turn; the 27-clock <160> meets the "
        "critical set in its order-3 steps 1440 and 2880":
            {kinds[864 * j] for j in range(1, 5)} == {"A4+A4"} and kinds[1080] == kinds[3240] == "D5+A3"
            and kinds[2160] == "D8" and {k for k in crit if k % 160 == 0} == {1440, 2880},
        "a step is regular, with trivial stabilizer, exactly when its order exceeds 29, the highest root's height: "
        "4234 of the 4319 nonzero steps":
            len(regular) == 4234 and all((N // gcd(k, N) > 29) == (k in set(regular)) for k in range(1, N)),
    }


def run():
    from . import gates
    from .record import Report
    rep = Report("28-principal")
    T = gates.THEOREM
    for fn in (circle, regular_steps, band_on_circle, critical_steps):
        for name, ok in fn().items():
            rep.add(name, T, ok)
    rep.add("cited: the principal element exp(2 pi i rho/h) is conjugate in the compact group to a lift of the Coxeter "
            "element (Kostant 1959); the lifts of an element without eigenvalue 1 are conjugate under the torus",
            gates.SELECTED_REFERENCE, True)
    return rep
