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
(e) The clock lattice (30 Oct). The clocks of the number level are subgroups and quotients of the principal circle, read
    in the seed's terms. The nine nonzero critical steps are the union of <2160>, <1440>, <1080> and <864> and generate the
    grain <72> (60 = lcm(2, 3, 4, 5) points); the time clock and the observer clock meet in 0 and add to the golden
    step's subgroup <216> = Z/20, and with the sun's <1440> to the grain. The thirteen regular steps are multiples
    of 36 and generate the seam <36> (120 = lcm(30, 24, 20) points; the Coxeter and day steps already do), so the
    atlas Z/36 is the circle modulo its regular steps. The 27-clock <160> is the Sylow 3-subgroup, holding the sun's
    step rho/3; the coil <8> is the grain plus the 27-clock; the miss set <5> is the kernel of the time coordinate, the
    points of order prime to 5; the vortex Z/9 is the 27-clock modulo the sun. The observer clock's step rho/4 carries
    the regular class 4, the day's sixth power d^6. The seed names the orders 5, 4, 60 and 120 (the critical types,
    the lcm of the critical orders, the lcm of the regular orders): the time clock, the observer clock and the grain are
    the seed's. The orders 27, 32, 540 and 864 and the quotient sizes 36 and 9 come from factoring the canon's
    4320 = 2^5 3^3 5 and do not divide 120. But the 27-clock is the seed's too (1 Nov, singular_primary): the
    principal points of 3-power order that fix a root are exactly <rho/27>, so the 27-clock, the vortex (its image
    on the sun's A8) and the coil (<rho/60> + <rho/27>) are derived; only the miss set and the atlas need the
    circle's 2-part 32 = 2^5, the cofactor's 2^2 over the seam's 2^3. None of the generators 72, 36, 160, 8, 5
    is critical, and |<36>| = 120 = |G120| only numerically.
(f) Uniqueness. The Weyl vector is the half-sum of the positive roots and is regular, so it determines its positive
    system; W(E8) permutes the positive systems transitively (cited) and keeps the band, so every conjugate circle
    k -> k w rho / 4320 has the same band values and the same critical steps and types: the principal circle is
    unique up to W(E8). A positive system and its opposite give the same circle (w = -1 sends k -> -k); otherwise
    the conjugate circles are different subsets of the torus.
What stays the canon's: the 2-part 32 = 2^5 of the sampling at 4320 points (the 3-part is the seed's <rho/27>, the
5-part its critical 5; no single rule of the seed gives 2^5 3^3 5), and the stage indices with their orientation
(stage_frame: the labelling k -> k rho/4320 is the seed's, the one-sided segment {0..14} is not). The seed's group of
order 4320 (the decad's stabilizer in C_W(s)) and the absence of a Weyl clock of order 36 are recorded as
obstructions (decad_stabilizer, no_order_36). The circle's Coxeter step, its critical steps and the grain are the seed's.
"""

import functools
from collections import Counter
from math import gcd, lcm

import numpy as np
import sympy as sp

from . import cyclotomic, handover, primes, spine

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


def clock_lattice():
    """(e): the clocks of the number level are the subgroup lattice of the principal circle, read in the seed's terms."""
    _, rs, ht = weyl_vector()
    R = spine.frame()[4]
    S, reg, k = spine.subgroup, primes.regular(), cyclotomic.clocks()
    order = lambda x: N // gcd(x, N)
    grads = np.array([np.linalg.norm(_gradient(rs * j / N)) for j in range(N)])
    crit = [j for j in range(1, N) if grads[j] < 1e-8]
    gen = lambda steps: S(functools.reduce(gcd, steps))                 # the subgroup the steps generate
    add = lambda A, B: frozenset((a + b) % N for a in A for b in B)
    kernel = lambda m: frozenset(x for x in range(N) if m * x % N == 0)
    of_order = lambda n: [j for j in crit if order(j) == n]
    steps = [(N // d) % N for d in reg]
    stab = {j: handover.stabiliser(R, rs * j / N)[0] for j in (72, 36, 160, 8, 5, 144, 180, 216)}
    heights = Counter(int(h) for h in ht if h > 0)
    return {
        "the band's nine nonzero critical steps are the union of the four subgroups <2160>, <1440>, <1080> and <864>, so they "
        "generate <gcd> = <72>, the grain: 60 = lcm(2, 3, 4, 5) points k rho/60, the golden step 216 = rho/20 times the "
        "sun's step 1440 = rho/3":
            crit == [864, 1080, 1440, 1728, 2160, 2592, 2880, 3240, 3456]
            and frozenset(crit) | {0} == S(2160) | S(1440) | S(1080) | S(864) and gen(crit) == S(72)
            and len(S(72)) == 60 == lcm(2, 3, 4, 5) and add(S(216), S(1440)) == S(72) and (N // 20, N // 3) == (216, 1440),
        "the steps 4320/d of the thirteen regular orders are multiples of 36 = 4320/120 (thirteen of its 120 multiples), "
        "120 = lcm(30, 24, 20), and "
        "they generate the seam <36>, as the Coxeter step 144 and the day's step 180 already do (gcd 36; the golden step "
        "216 = 6 x 36 adds nothing): the atlas Z/36 is the principal circle modulo the subgroup its regular steps "
        "generate, the largest quotient in which every step of regular order (56 steps) and every critical step vanishes":
            all(s % 36 == 0 for s in steps) and gen(steps) == S(36) == gen([144, 180]) and 216 == 6 * 36
            and len(S(36)) == 120 == lcm(30, 24, 20) and all(j % 36 == 0 for j in crit)
            and (N // 30, N // 24, N // 20) == (144, 180, 216) and {x % 36 for x in range(N)} == set(range(36))
            and sum(1 for x in range(N) if order(x) in reg) == 56 and all(x % 36 == 0 for x in range(N) if order(x) in reg),
        "the 27-clock <160> is the Sylow 3-subgroup of the circle, its unique subgroup of order 27 (4320 = 2^5 3^3 5), "
        "the points of order a power of 3; it holds the sun's step 1440 = rho/3, whose spectrum is the regular class "
        "3, the sun s = c'^10, and the two A8 critical steps":
            [d for d in spine.divisors() if len(S(d)) == 27] == [160] and S(160) == kernel(27) and N == 2 ** 5 * 3 ** 3 * 5
            and frozenset(of_order(3)) == S(1440) - {0} <= S(160) and np.array_equal(reg[3], spine.mpow(k["c"], 10)),
        "the time clock <864> is 0 with the four critical steps of order 5 (A4 + A4), the circle's 5-part; the observer "
        "clock <1080> is 0, the two critical steps of order 4 (D5 + A3) and their square, the half-turn 2160 (D8), the "
        "order-4 subgroup of the 2-part <135>":
            S(864) == frozenset([0] + of_order(5)) == kernel(5) and S(1080) == frozenset([0, 2160] + of_order(4)) == kernel(4)
            and S(1080) <= S(135) == kernel(32) and of_order(2) == [2160],
        "the coil <8> is the sum <72> + <160> of the grain and the 27-clock, which meet in the sun's subgroup <1440>: "
        "60 x 27 / 3 = 540 points, the kernel of x -> 540 x with 540 = lcm(4, 27, 5); it is also generated by the "
        "time clock, the observer clock and the 27-clock":
            add(S(72), S(160)) == S(8) and S(72) & S(160) == S(1440) and len(S(8)) == 540 == 60 * 27 // 3
            and S(8) == kernel(540) and lcm(4, 27, 5) == 540 and gen([864, 1080, 160]) == S(8),
        "the miss set <5> is the kernel of the time coordinate x -> 3456 x, the points of order prime to 5, the sum "
        "<135> + <160> of the 2-part and the 3-part (32 x 27 = 864 points), with Z/4320 = <864> + <5>; it holds every "
        "critical step but the time clock's four":
            S(5) == kernel(3456) == kernel(864) == add(S(135), S(160)) and len(S(5)) == 864
            and all(order(x) % 5 for x in S(5)) and S(864) & S(5) == {0} and add(S(864), S(5)) == frozenset(range(N))
            and {j for j in crit if j in S(5)} == {1080, 1440, 2160, 2880, 3240},
        "the vortex Z/9 is the 27-clock modulo the sun's subgroup: x -> x mod 9 maps <160> onto Z/9 with kernel <1440>, "
        "and the whole circle onto it with kernel <9> = <36> + <135>, the seam plus the 2-part (480 points); the atlas "
        "and the vortex see no step of regular order and no critical step, all being 0 mod 36":
            {x % 9 for x in S(160)} == set(range(9)) and frozenset(x for x in S(160) if x % 9 == 0) == S(1440)
            and frozenset(x for x in range(N) if x % 9 == 0) == S(9) == add(S(36), S(135)) and len(S(9)) == 480,
        "the time clock and the observer clock meet in 0 and add to <216> = Z/20, the golden step's subgroup, Z/5 x Z/4: "
        "the golden step rho/20 is the sum of the two small clocks; with the sun's subgroup <1440> they add to the grain, "
        "<864> + <1080> + <1440> = <72>; and the observer clock's step 1080 = rho/4 carries the spectrum of the regular "
        "class 4, the day's sixth power d^6 (d^12 = -1 is the half-turn at the observer clock's square 2160)":
            S(864) & S(1080) == {0} and add(S(864), S(1080)) == S(216) and len(S(216)) == 20
            and add(add(S(864), S(1080)), S(1440)) == S(72) and np.array_equal(reg[4], spine.mpow(k["day"], 6))
            and np.array_equal(spine.mpow(k["day"], 12), -np.eye(8, dtype=np.int64)) and 2160 == 2 * 1080,
        "the seed names four of these orders: 5 and 4 (the critical types A4 + A4 and D5 + A3), 60 (the lcm of the critical "
        "orders) and 120 (the lcm of the regular orders), so the time clock, the observer clock and the grain are the seed's; "
        "27, 32, 540 and 864 and the quotient sizes 36 and 9 come from the factorization of the canon's 4320 = 2^5 3^3 5 "
        "and do not divide 120, so the 27-clock, the coil, the miss set, the atlas and the vortex need the circle's "
        "cofactor 36 = 4320/120 = 2^2 3^2; the stages (0 to 14, not a subgroup) and the memory clock (order 90, with the "
        "same 3^2, reached through 24 maps) are fixed by no order":
            (len(S(864)), len(S(1080)), len(S(72)), len(S(36))) == (5, 4, 60, 120) and all(120 % n == 0 for n in (5, 4, 60))
            and (len(S(160)), len(S(135)), len(S(8)), len(S(5)), N // len(S(36)), N // len(S(9))) == (27, 32, 540, 864, 36, 9)
            and all(120 % n for n in (27, 32, 540, 864, 36, 9)) and N // 120 == 36 == 2 ** 2 * 3 ** 2 and N == 2 ** 5 * 3 ** 3 * 5
            and 90 == 2 * 3 ** 2 * 5 and 120 % 90 and N % 90 == 0,
        "none of the generators 72, 36, 160, 8 and 5 is a critical step (the band's gradient there is at least 4.8, the "
        "band 146.28, 46.86, 249.63, 2.51 and 0.98); 72, 36, 8 and 5 have orders above 29 and trivial stabilizers, 160 "
        "has order 27 and the stabilizer A1 of the one root pair of height 27; of the clocks' steps 144 has a trivial "
        "stabilizer, 180 the stabilizer A1 and 216 the stabilizer A1 + A1, and none is critical":
            all(grads[j] > 4.8 for j in (72, 36, 160, 8, 5))
            and all(abs(_band(rs * j / N) - e) < 5e-3 for j, e in zip((72, 36, 160, 8, 5), (146.28, 46.86, 249.63, 2.51, 0.98)))
            and all(stab[j] == "" for j in (72, 36, 8, 5)) and stab[160] == "A1" and {h: heights[h] for h in heights if h % 27 == 0} == {27: 1}
            and (stab[144], stab[180], stab[216]) == ("", "A1", "A1+A1") and all(grads[j] > 1 for j in (144, 180, 216)),
        "|<36>| = 120 = |G120| only numerically: <36> is cyclic while G120 = <g> x| <d> has element orders 1, 2, 3, 4, 5, "
        "6, 8, 10, 12, 15, 24, 30 and no element of order 20 or 120; the golden clock v is not in it (only its even "
        "powers), and <c', d, v> is the 240-element normalizer of <c'>":
            (lambda G, key: len(G) == 120 and sorted(Counter(spine.mat_order(M) for M in G)) == [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 24, 30]
             and key(np.rint(k["golden"]).astype(np.int64)) not in {key(M) for M in G}
             and [j for j in range(20) if key(spine.mpow(np.rint(k["golden"]).astype(np.int64), j)) in {key(M) for M in G}] == list(range(0, 20, 2))
             and len(primes._matrix_group([np.rint(k["c"]).astype(np.int64), np.rint(k["day"]).astype(np.int64),
                                           np.rint(k["golden"]).astype(np.int64)])) == 240)(
                primes._matrix_group([np.rint(k["c"]).astype(np.int64), np.rint(k["day"]).astype(np.int64)]), lambda M: M.tobytes()),
    }


def principal_uniqueness():
    """(f): the principal circle is unique up to W(E8), which keeps the band."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, rs, ht = weyl_vector()
    I8 = np.eye(8, dtype=np.int64)
    simple = []
    for i in range(8):
        s = I8.copy()
        s[i, :] -= C[i, :]
        simple.append(s)
    pos = RB[ht > 0]
    roots = {tuple(v) for v in RB.tolist()}
    plus = {tuple(v) for v in pos.tolist()}
    image = lambda w: {tuple(v) for v in (w @ pos.T).T.tolist()}
    positive = lambda S: len(S) == 120 and S | {tuple(-np.array(v)) for v in S} == roots and not (S & {tuple(-np.array(v)) for v in S})
    halfsum = lambda S: sum(np.array(v) for v in S)
    c, cp, _, _, _, w19 = spine.spine_clock()
    rng = np.random.default_rng(7)
    straight = []
    while len(straight) < 5:
        x = rng.integers(-40, 41, size=8)
        if (RB @ C @ x == 0).any():
            continue                                        # not regular: some root is orthogonal to x
        y, w = x.copy(), I8.copy()
        while any((C @ y)[i] < 0 for i in range(8)):
            i = next(i for i in range(8) if (C @ y)[i] < 0)
            y, w = simple[i] @ y, simple[i] @ w
        wi = spine.inverse(w)
        S = {tuple(v) for v in RB[RB @ C @ x > 0].tolist()}
        straight.append(positive(S) and S == image(wi) and np.array_equal(halfsum(S), 2 * (wi @ rho)) and spine.is_weyl(w)
                        and bool(((C @ y) > 0).all()))
    conj = {}
    for name, w in (("s1", simple[0]), ("w19", w19)):
        ws = spine.to_standard(w)
        pts = [rs * k / N for k in range(N)]
        crit = [k for k in range(1, N) if np.linalg.norm(_gradient(ws @ pts[k])) < 1e-8]
        conj[name] = (max(abs(_band(ws @ p) - _band(p)) for p in pts) < 1e-9 and crit == [864, 1080, 1440, 1728, 2160, 2592, 2880, 3240, 3456]
                      and [handover.stabiliser(R, ws @ pts[k])[0] for k in crit] == ["A4+A4", "D5+A3", "A8", "A4+A4", "D8", "A4+A4", "A8", "D5+A3", "A4+A4"])
    units = [u for u in range(1, N) if gcd(u, N) == 1]
    return {
        "the Weyl vector is the half-sum of the 120 positive roots, and it is regular: <r, rho> = ht(r) is never 0, so "
        "rho determines its positive system {r : <r, rho> > 0} and no Weyl element but 1 fixes it (cited: the stabilizer "
        "of a regular vector in W is trivial)":
            np.array_equal(2 * rho, pos.sum(axis=0)) and bool((ht != 0).all()) and plus == {tuple(v) for v in RB[RB @ C @ rho > 0].tolist()},
        "for each simple reflection s_i the positive system s_i Phi+ differs from Phi+ in the one root alpha_i, and its "
        "Weyl vector is s_i rho = rho - alpha_i, again of norm 620":
            all(positive(image(s)) and len(image(s) ^ plus) == 2 and np.array_equal(halfsum(image(s)), 2 * (s @ rho))
                and np.array_equal(s @ rho, rho - I8[i]) and int((s @ rho) @ C @ (s @ rho)) == 620 for i, s in enumerate(simple)),
        "for layer 19's conjugator w, for c' and for c the positive system w Phi+ has the Weyl vector w rho, and a "
        "regular vector x straightened into the fundamental chamber by simple reflections has the positive system "
        "{r : <r, x> > 0} = w^-1 Phi+ with Weyl vector w^-1 rho (five random regular vectors); cited: W(E8) permutes "
        "the positive systems transitively, so these are all of them":
            all(positive(image(w)) and np.array_equal(halfsum(image(w)), 2 * (w @ rho)) for w in (w19, cp, c)) and all(straight),
        "W(E8) keeps E8 and its roots, so it acts on the momentum torus and keeps the band: along the conjugate circle "
        "k -> k w rho / 4320 (w = s1, w = layer 19's w) the band agrees with the principal circle's at all 4320 steps, "
        "and the critical steps and their types D8, A8, D5 + A3 and A4 + A4 are the same; so the principal circle is "
        "unique up to W(E8); a positive system and its opposite give the same circle (w = -1 sends k -> -k), and otherwise "
        "the conjugate circles are different subsets of the torus (no unit u mod 4320 has w rho = u rho mod 4320 E8 for "
        "w = s_i, layer 19's w, c or c'); the finite check covers the band's W-invariance and these positive systems, "
        "the transitivity is cited":
            all(conj.values()) and not ((-rho - (N - 1) * rho) % N).any()
            and not any(not ((u * rho - w @ rho) % N).any() for w in simple + [w19, c, cp] for u in units),
    }


def _alcove_points(M, ks):
    """Exact reduction of the points k rho/M (k in ks) to E8's closed fundamental alcove, as integer vectors scaled by M
    in root coordinates (affine Weyl moves); two points are conjugate under W(E8) and the lattice iff they reduce alike."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, _, ht = weyl_vector()
    theta = RB[int(np.argmax(ht))]
    tC = theta @ C
    Y = np.array([(k % M) * rho for k in ks], dtype=np.int64)
    while True:
        CY = Y @ C
        neg = (CY < 0).any(axis=1)
        over = ~neg & (Y @ tC > M)
        if not neg.any() and not over.any():
            return Y
        rows = np.nonzero(neg)[0]
        i = np.argmax(CY[rows] < 0, axis=1)
        Y[rows, i] -= CY[rows, i]
        rows0 = np.nonzero(over)[0]
        Y[rows0] -= (Y[rows0] @ tC - M)[:, None] * theta[None, :]


def singular_primary():
    """Cofactor-free: the principal points of p-power order that fix a root. For a prime p they form <rho/p^a>, p^a the
    largest p-power dividing a root height: 16, 27, 25 for p = 2, 3, 5. Sing_3 = <rho/27> is the 27-clock (Galois-dual to
    the chain E8 > A8 > A3 + A2 + A1 > A1), Sing_3/<rho/3> acts faithfully on the sun's A8 (the vortex), and the grain
    <rho/60> plus Sing_3 is <rho/540> (the coil): three dots of the circle's cofactor 36 come from the seed. The circle's
    p-parts are 32, 27, 5; only its 3-part is Sing_3, and its 2-part 32 = 2^5 is the one factor the seed does not name."""
    from fractions import Fraction
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, rs, ht = weyl_vector()
    Qz = lambda den: frozenset(Fraction(j, den) for j in range(den))
    add = lambda A, Bs: frozenset((a + b) % 1 for a in A for b in Bs)
    singular = lambda M, k: any((k * int(h)) % M == 0 for h in ht if h > 0)
    sing = {p: max(b for b in range(8) if all(singular(p ** b, k) for k in range(p ** b))) for p in (2, 3, 5)}
    fix = {m: [i for i in range(240) if all((Fraction(k, m) * int(ht[i])) % 1 == 0 for k in range(m))] for m in (1, 3, 9, 27)}
    a8 = [i for i in range(240) if int(ht[i]) % 3 == 0]
    act = lambda t: tuple((t * int(ht[i])) % 1 for i in a8)

    def fusion(M):
        units = [u for u in range(1, M + 1) if gcd(u, M) == 1]
        Y = _alcove_points(M, units)
        return [u for u, y in zip(units, Y) if np.array_equal(y, Y[0])]
    limit = {p: max([1] + [p ** b for b in range(1, {2: 9, 3: 6, 5: 4}[p]) if len(fusion(p ** b)) > 2]) for p in (2, 3, 5)}
    return {
        "the principal points of 3-power order that fix a root are exactly <rho/27> (every point of order 81 is "
        "regular), 27 the largest power of 3 dividing a root height; likewise <rho/16> and <rho/25> for 2 and 5":
            {p: p ** a for p, a in sing.items()} == {2: 16, 3: 27, 5: 25} and not singular(81, 1)
            and {p: max(sp.multiplicity(p, int(h)) for h in ht if h > 0) for p in (2, 3, 5)} == sing,
        "the subgroup of <rho/27> of order 3^a fixes exactly the roots of height divisible by 3^a, of types E8, A8, "
        "A3 + A2 + A1 and A1 (240, 72, 20 and 2 roots): the 27-clock with no reference to 4320":
            all(fix[m] == [i for i in range(240) if int(ht[i]) % m == 0] for m in fix)
            and [len(fix[m]) for m in (1, 3, 9, 27)] == [240, 72, 20, 2]
            and [handover.stabiliser(R, rs / m)[0] for m in (1, 3, 9, 27)] == ["E8", "A8", "A3+A2+A1", "A1"],
        "Sing_3 acts on the root spaces of the sun's A8 with kernel exactly <rho/3>: the vortex Z/9 = Sing_3/<rho/3>":
            sorted(t for t in Qz(27) if all(v == 0 for v in act(t))) == sorted(Qz(3)) and len({act(t) for t in Qz(27)}) == 9,
        "the grain <rho/60> (the group of the critical steps) plus Sing_3 is <rho/540>, meeting it in <rho/3>: the coil, "
        "with no reference to 4320":
            add(Qz(60), Qz(27)) == Qz(540) and Qz(60) & Qz(27) == Qz(3),
        "the circle's p-parts are 32, 27 and 5; Sing_p gives 16, 27, 25, the first regular p-power orders are 32, 81, 125, "
        "and the last p-power orders at which E8 fuses principal points beyond +-1 are 32, none and 25: only the 3-part is "
        "Sing_3, and no one rule gives 2^5 3^3 5":
            {p: p ** sp.multiplicity(p, N) for p in (2, 3, 5)} == {2: 32, 3: 27, 5: 5}
            and [min(p ** b for b in range(1, 6) if not singular(p ** b, 1)) for p in (2, 3, 5)] == [32, 81, 125]
            and limit == {2: 32, 3: 1, 5: 25}
            and 16 * 27 * 25 != N and 32 * 81 * 125 != N and 32 * 25 != N,
        "with Sing_3 the cofactor 36 = (32/8)(27/3) keeps one external factor, 4 = 32/8, the circle's 2-part over the "
        "seam's: the miss set (864 = 32 x 27) and the atlas (the circle modulo the seam) need it, while Sing_2 + Sing_3 "
        "has only 432 points":
            N // 120 == 36 == (32 // 8) * (27 // 3) and len(add(Qz(16), Qz(27))) == 432 and 32 * 27 == 864,
    }


@functools.lru_cache(maxsize=None)
def stage_frame():
    """The circle's labeling is the seed's, and the stages fix an orientation. E8 conjugacy on the principal circle has
    2137 classes, each closed under k -> -k, and realizes only u = +-1 on a generator; rho/4320 is, up to sign, the
    generator of least band. The stage set {0, ..., 14} is not closed under w = -1: it fixes the orientation (a positive
    system) and is then the fifteen least-band points of the half-circle; the seed's own fifteen least-band points are
    {-7, ..., 7}, and its order-15 subgroup <rho/15> meets the stages only in 0."""
    from . import counts
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, rs, ht = weyl_vector()
    Y = _alcove_points(N, range(N))
    cls = {}
    for k in range(N):
        cls.setdefault(Y[k].tobytes(), set()).add(k)
    of = {k: frozenset(c_) for c_ in cls.values() for k in c_}
    units = [u for u in range(1, N) if gcd(u, N) == 1]
    stages = set(range(15))
    closure = set().union(*[of[k] for k in stages])
    fixed = lambda k: frozenset(i for i in range(240) if (k * int(ht[i])) % N == 0)
    x = sp.Symbol("x")
    heights = Counter(int(h) for h in ht)

    def chi(d, u):
        a = [0] * d
        a[0] += 8
        for h, m_ in heights.items():
            a[(u * h) % d] += m_
        return sp.rem(sp.Poly(list(reversed(a)), x), sp.Poly(sp.cyclotomic_poly(d, x), x))
    galois = all((sp.rem(sp.Poly(chi(d, 1).as_expr().subs(x, x ** u), x), sp.Poly(sp.cyclotomic_poly(d, x), x))
                  - chi(d, u)).is_zero for d in (9, 27, 32, 36, 540) for u in [u for u in range(2, d) if gcd(u, d) == 1][:4])
    crit = [864, 1080, 1440, 1728, 2160, 2592, 2880, 3240, 3456]
    band = [_band(rs * k / N) for k in range(N)]
    gen_by_band = sorted(units, key=lambda u: band[u])
    low = sorted(range(N), key=lambda k: band[k])[:15]
    c_ = np.rint(cyclotomic.clocks()["c"]).astype(np.int64)
    fl = counts.first_landing
    return {
        "E8 conjugacy on the principal circle has 2137 classes, each closed under k -> -k (w = -1), and realizes only the "
        "units +-1 on a generator":
            len(cls) == 2137 and all({(-k) % N for k in c_s} == c_s for c_s in cls.values())
            and sorted(u for u in units if u in of[1]) == [1, N - 1],
        "the labeling k -> k rho/4320 is the seed's: rho/4320 and its negative are the two generators of least band, and "
        "the band rises strictly along k = 0, ..., 29; a relabeling k -> u k (u not +-1) keeps the roots fixed at every "
        "point and the nine critical steps but sends the band to its Galois conjugate sigma_u (exact in Z[zeta_d] for "
        "d = 9, 27, 32, 36, 540), which no conjugation of E8 does":
            sorted(gen_by_band[:2]) == [1, N - 1] and band[gen_by_band[2]] > band[1] + 1
            and all(band[i] < band[i + 1] for i in range(29))
            and all(fixed((u * k) % N) == fixed(k) for u in units[:40] for k in range(0, N, 7))
            and all({(u * k) % N for k in crit} == set(crit) for u in units) and galois,
        "the stage set {0, ..., 14} is not closed under w = -1 (its E8 closure is {-14, ..., 14}, 29 points): it fixes "
        "the orientation, a positive system, and is then the fifteen least-band points of the half-circle 0..2160; the "
        "seed's own fifteen least-band points are {-7, ..., 7}, and its order-15 subgroup <rho/15> = <288> meets the "
        "stages only in 0: the count fifteen and the one-sided segment are the canon's":
            closure == set(range(15)) | {N - j for j in range(1, 15)}
            and sorted(k if k < N // 2 else k - N for k in low) == list(range(-7, 8))
            and sorted(sorted(range(N // 2 + 1), key=lambda k: band[k])[:15]) == list(range(15))
            and min(band[15:N // 2 + 1]) > band[14] and set(range(0, N, 288)) & stages == {0},
        "the stages' landing pattern is the seed's: c'^2 = s^2 g^2, a stage k lands exactly when the tick part g^(2k) is "
        "not 1 (5 does not divide k), and under k -> u k the first landings go (m, level) -> (m, u level)":
            np.array_equal(spine.mpow(c_, 2), spine.mpow(c_, 20) @ spine.mpow(c_, 12))
            and [k for k in range(15) if counts.STAGE_LANDINGS[k] is not None] == [k for k in range(15) if k % 5]
            and all(fl((u * k) % N) == (None if fl(k) is None else (fl(k)[0], (u * fl(k)[1]) % N))
                    for u in units[:50] for k in range(15)),
    }


@functools.lru_cache(maxsize=None)
def _decad_data():
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, rs, ht = weyl_vector()
    theta = RB[int(np.argmax(ht))]
    I8 = np.eye(8, dtype=np.int64)
    E = primes.elements(3).astype(np.int64)
    Q = primes.sun_matrices()
    S = primes.sun_geometry()
    phi, decad, over = S["phi"], S["decad"], S["over"]
    I4 = np.eye(4, dtype=np.int64)
    QP = (Q @ phi) % 3
    lin = np.all(QP == (phi @ Q) % 3, axis=(1, 2))
    anti = np.all(QP == (((I4 - phi) % 3) @ Q) % 3, axis=(1, 2))
    proj_of = lambda v: min(tuple(v), tuple(((2 * np.array(v)) % 3).tolist()))
    frames = [frozenset(i for q in {proj_of(x) for x in L} for i in over[q]) for L in decad]
    fr_of = np.zeros(240, dtype=np.int64)
    for j, F in enumerate(frames):
        fr_of[list(F)] = j
    key = {tuple(r): i for i, r in enumerate(RB.tolist())}
    perm = lambda M: np.array([key[tuple(r)] for r in (RB @ M.T).tolist()])
    keeps = lambda M: all(len(set(fr_of[perm(M)[list(F)]].tolist())) == 1 for F in frames)
    return E, Q, lin, anti, frames, fr_of, perm, keeps


@functools.lru_cache(maxsize=None)
def decad_stabilizer(full=False):
    """The seed's group of order 4320, and why it is not the circle. G = the elements of the sun's centralizer
    C_W(s) that keep the decad (equivalently, F9-semilinear on the sun's momenta, F9 = F3[c' + c'^-1]): 4320 elements,
    index 36 in C_W(s); it holds G120 = <c', d> with index 36; its image on the ten frames is S6 with kernel <c'^5>.
    The whole stabilizer of the decad in W(E8) has 8640 elements, all normalizing <s>, and holds N(<c'>) with index 36.
    But G has exponent 120, no element above order 30, abelianization of order at most 6 and Sylow 3-subgroups of
    exponent 3: every homomorphism from Z/4320 to G kills <120> and has at most 30 points of image."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, rs, ht = weyl_vector()
    theta = RB[int(np.argmax(ht))]
    I8 = np.eye(8, dtype=np.int64)
    E, Q, lin, anti, frames, fr_of, perm, keeps = _decad_data()
    G = E[lin | anti]
    keyM = lambda M: M.tobytes()
    Gk = {keyM(M) for M in G}
    k = cyclotomic.clocks()
    c, d, v, m = (np.rint(k[n]).astype(np.int64) for n in ("c", "day", "golden", "mirror"))
    G120 = primes._matrix_group([c, d])
    NC = primes._matrix_group([c, d, v])
    fperm = lambda M: tuple(int(fr_of[perm(M)[next(iter(F))]]) for F in frames)
    img = {fperm(M) for M in G[:: 1]}
    kern = [M for M in G if fperm(M) == tuple(range(10))]
    orders = Counter(spine.mat_order(M) for M in G)
    rng = np.random.default_rng(1)
    comm = [a @ b @ spine.inverse(a) @ spine.inverse(b) for a, b in
            ((G[rng.integers(len(G))], G[rng.integers(len(G))]) for _ in range(300))]
    D = primes._matrix_group(list({keyM(M): M for M in comm}.values())[:40])
    out = {
        "the elements of C_W(s) (155520) that are F9-linear or F9-antilinear on the sun's momenta are 2160 + 2160 = 4320, "
        "exactly those that keep the decad of ten 4A2 frames; index 36 in C_W(s), whose orbit of the decad has 36 members":
            int(lin.sum()) == 2160 == int(anti.sum()) and len(G) == 4320 == N
            and all(keeps(M) for M in G[::97]) and len(E) // len(G) == 36,
        "G holds G120 = <c', d> (the Coxeter clock and the day) with index 36 = 4320/120, and acts on the ten frames as "
        "S6 (720 permutations) with kernel <c'^5>, G120 as AGL(1,5) (20)":
            len(G120) == 120 and all(keyM(M) in Gk for M in G120) and len(G) // len(G120) == 36
            and len(img) == 720 and {keyM(M) for M in kern} == {keyM(spine.mpow(c, 5 * j)) for j in range(6)}
            and len({fperm(M) for M in G120}) == 20,
        "but G is not the circle: its element orders are 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 24, 30, its exponent is 120, "
        "it has no element of order 9 or 27 (its Sylow 3-subgroups have exponent 3) and its commutators generate a "
        "subgroup of order at least 720 (abelianization at most 6): every homomorphism Z/4320 -> G kills <120> "
        "(36 points) and has image of order at most 30":
            sorted(orders) == [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 24, 30]
            and functools.reduce(lcm, orders) == 120 and 9 not in orders and len(D) >= 720 and len(G) // len(D) <= 6,
    }
    if full:
        # all of Stab_W(decad): enumerate N_W(F0) through the 4A2 simple systems of frame F0, keep the decad, x 10
        IP = RB @ C @ RB.T
        F0 = sorted(frames[0])
        comps, left = [], set(F0)
        while left:
            i = left.pop(); comp, stack = {i}, [i]
            while stack:
                u = stack.pop()
                for w in list(left):
                    if IP[u, w] != 0:
                        left.discard(w); comp.add(w); stack.append(w)
            comps.append(sorted(comp))
        base, pairs = [], []
        for comp in comps:
            a = comp[0]; b = next(j for j in comp if IP[a, j] == -1)
            base += [a, b]
            pairs.append([(x, y) for x in comp for y in comp if IP[x, y] == -1])
        X = RB[base].T
        det = round(np.linalg.det(X.astype(float)))
        adj = np.rint(np.linalg.inv(X.astype(float)) * det).astype(np.int64)
        nF0, stab = 0, []
        for pi in __import__('itertools').permutations(range(4)):
            for ch in __import__('itertools').product(range(12), repeat=4):
                cols = [t for i in range(4) for t in pairs[pi[i]][ch[i]]]
                W = RB[cols].T @ adj
                if (W % det).any():
                    continue
                W //= det
                nF0 += 1
                if keeps(W):
                    stab.append(W)
        s = spine.mpow(c, 10)
        normal = all(any(np.array_equal(W @ s @ spine.inverse(W), spine.mpow(s, j)) for j in (1, 2)) for W in stab)
        out["the whole stabilizer of the decad in W(E8) has 10 x 864 = 8640 elements (N_W(F0) has 62208), all "
            "normalizing <s>: G is its half that commutes with the sun, and N(<c'>) = <c', d, v> (240) sits in it with "
            "index 36 too; so 36 is canonical (the clocks' index in the decad's symmetry, at both levels) and 4320 is the "
            "order at the centralizer level only"] = (
            nF0 == 62208 and len(stab) == 864 and normal and len(NC) == 240 and all(keeps(M) for M in NC)
            and keeps(m) and 10 * len(stab) // len(NC) == 36)
    return out


@functools.lru_cache(maxsize=None)
def no_order_36():
    """The atlas obstruction: GL8(Z) has elements of order 36 (Phi4 Phi9, Phi4 Phi18; psi(36) = 8) but W(E8) has
    none. w of order 36 has w^4 of characteristic polynomial Phi9 Phi1^2; that class (E6(a1), here c7^2) fixes an A2
    with E6 orthogonal; w keeps both, acting on A2 with order 1, 2, 3 or 6 and on E6 inside <x> x <-1> (order | 18).
    Cited: Steinberg (pointwise stabilizers are reflection subgroups), E6 is unique in E8 up to W."""
    B, Binv, C, Cinv, R, RB = spine.frame()
    rho, rs, ht = weyl_vector()
    theta = RB[int(np.argmax(ht))]
    I8 = np.eye(8, dtype=np.int64)
    x = sp.Symbol("x")
    ds = [d for d in range(1, 61) if sp.totient(d) <= 8]

    def combos(budget, start, acc):
        if budget == 0:
            yield acc
            return
        for i in range(start, len(ds)):
            f = int(sp.totient(ds[i]))
            if f <= budget:
                yield from combos(budget - f, i, acc + [ds[i]])
    polys = [cmb for cmb in combos(8, 0, []) if functools.reduce(lcm, cmb, 1) == 36]
    refl = lambda i: I8 - np.outer(I8[i], C[i])
    perp = [i for i in range(8) if int(I8[i] @ C @ theta) == 0]
    X = spine.mpow(functools.reduce(lambda a, b: a @ b, [refl(i) for i in perp], I8), 2)
    fixed_roots = [i for i in range(240) if np.array_equal(X @ RB[i], RB[i])]
    a1 = RB[fixed_roots[0]]
    a2 = next(RB[i] for i in fixed_roots if int(a1 @ C @ RB[i]) == -1)
    G2 = np.array([[a1 @ C @ a1, a1 @ C @ a2], [a2 @ C @ a1, a2 @ C @ a2]])
    auts = [np.array(t).reshape(2, 2) for t in __import__('itertools').product(range(-2, 3), repeat=4)
            if np.array_equal(np.array(t).reshape(2, 2).T @ G2 @ np.array(t).reshape(2, 2), G2)]
    o2 = lambda T: next(j for j in range(1, 13) if np.array_equal(np.linalg.matrix_power(T, j), np.eye(2, dtype=np.int64)))
    orth = [i for i in range(240) if int(RB[i] @ C @ a1) == 0 and int(RB[i] @ C @ a2) == 0]
    pos = [RB[i] for i in orth if ht[i] > 0]
    pset = {tuple(r) for r in pos}
    simple = [r for r in pos if not any(tuple(r - s_) in pset for s_ in pos)]
    W6 = primes._matrix_group([I8 - np.outer(r, r @ C) for r in simple])
    keyM = lambda M: M.tobytes()
    cpk = lambda M: tuple(np.rint(np.poly(M.astype(float))).astype(int).tolist())
    same = {keyM(M) for M in W6 if cpk(M) == cpk(X)}
    cls = {keyM(g @ X @ spine.inverse(g)) for g in W6}
    cent = [M for M in W6 if np.array_equal(M @ X, X @ M)]
    W_orders = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 18, 20, 24, 30}
    return {
        "the degree-8 products of cyclotomic polynomials of order 36 are Phi4 Phi9 and Phi4 Phi18 (psi(36) = 8), so "
        "GL8(Z) has elements of order 36; for both, w^4 has Phi9 Phi1^2":
            polys == [[4, 9], [4, 18]],
        "x = c7^2 (order 9, Phi9 Phi1^2) fixes exactly six roots, an A2 (Gram [[2, -1], [-1, 2]]), and the 72 roots "
        "orthogonal to it are an E6; the A2 lattice has 12 isometries, of orders 1, 2, 3, 6":
            spine.mat_order(X) == 9 and sp.expand(sp.Matrix(X.tolist()).charpoly(x).as_expr()
                                                  - sp.cyclotomic_poly(9, x) * (x - 1) ** 2) == 0
            and len(fixed_roots) == 6 and G2.tolist() == [[2, -1], [-1, 2]] and len(orth) == 72
            and handover.stabiliser(R[orth], np.zeros(8))[0] == "E6"
            and len(auts) == 12 and sorted({o2(T) for T in auts}) == [1, 2, 3, 6],
        "in W(E6) (51840) the elements with x's characteristic polynomial are one class of 5760, with centralizer <x> "
        "of order 9, and -1 is not in W(E6): an element commuting with x acts on E6 inside <x> x <-1> and on A2 by an "
        "isometry, so its order divides 18, and W(E8) has no element of order 36 (the atlas Z/36 is no Weyl clock); "
        "of the 19 divisors of 4320 that GL8(Z) allows, 16, 36, 40 and 60 are not orders of W(E8) (cited list)":
            len(W6) == 51840 and same == cls and len(cls) == 5760 and len(cent) == 9
            and keyM(-I8) not in {keyM(M) for M in W6}
            and [d for d in spine.divisors() if sum(int(sp.totient(p ** e)) for p, e in sp.factorint(d).items())
                 - (1 if d % 4 == 2 else 0) <= 8 and d not in W_orders] == [16, 36, 40, 60],
    }


def run():
    from . import gates
    from .record import Report
    rep = Report("28-principal")
    T = gates.THEOREM
    for fn in (circle, regular_steps, band_on_circle, critical_steps, clock_lattice, principal_uniqueness,
               singular_primary, stage_frame, decad_stabilizer, no_order_36):
        for name, ok in fn().items():
            rep.add(name, T, ok)
    rep.add("cited: the principal element exp(2 pi i rho/h) is conjugate in the compact group to a lift of the Coxeter "
            "element (Kostant 1959); the lifts of an element without eigenvalue 1 are conjugate under the torus",
            gates.SELECTED_REFERENCE, True)
    return rep
