import itertools
from fractions import Fraction

import pytest

from oes import (assignment, band, binding, canon_sync, carrier, cosmology, counts, court, cyclotomic, dots, frontier,
                 gates, gatework, glue, gravity, handover, joins, ledger, literal, native, observer, places,
                 primes, principal, recurrence, snapshot, spacetime, spectral, spine, unify, waves)

LAYERS = {
    "carrier": carrier.run,
    "spectral": spectral.run,
    "spacetime": spacetime.run,
    "native": lambda: native.run(simulate=False),
    "observer": observer.run,
    "gravity": gravity.run,
    "cosmology": cosmology.run,
    "frontier": frontier.run,
    "joins": joins.run,
    "literal": lambda: literal.run(simulate=False),
    "glue": glue.run,
    "binding": binding.run,
    "gates": gatework.run,
    "recurrence": recurrence.run,
    "court": court.run,
    "handover": handover.run,
    "waves": waves.run,
    "snapshot": snapshot.run,
    "spine": spine.run,
    "canon": canon_sync.run,
    "ledger": ledger.run,
    "counts": counts.run,
    "dots": dots.run,
}


@pytest.mark.parametrize("name", list(LAYERS))
def test_layer(name):
    rep = LAYERS[name]()
    bad = [(c.name, c.value) for c in rep.checks if not c.passed]
    assert not bad, bad


def test_gates_never_promoted():
    assert gates.GATES["AUTH"] == "NOT_PASS"
    assert gates.GATES["ScientificGold"] == "FALSE"
    assert gates.GATES["TIME_BIND"] == "UNBOUND"


def test_carrier_lagrangian_has_no_extra_term():
    import numpy as np
    L = carrier.CarrierLagrangian()
    psi, v = carrier.canon_initial_datum()
    assert np.isclose(L.lagrangian(psi, v), 0.5 * v @ v - 0.5 * psi @ L.K @ psi)
    assert np.isclose(L.energy(psi, v), 34.0)


def test_walkfast_matches_weyl_orbit_engine():
    from oes import walkfast, walks
    p = walkfast.PRIMES[0]
    assert walkfast.walk_counts_mod(6, p) == [w % p for w in walks.KNOWN]


def test_gcrd_recovers_a_known_minimal_recurrence():
    # C(2n, n) satisfies (n + 1) a(n+1) = (4n + 2) a(n); higher-order multiples of it
    # must have that operator as their greatest common right divisor.
    from math import comb

    from oes import ore
    p = 1769473
    a = [comb(2 * n, n) % p for n in range(80)]
    ops = ore.kernel_operators(recurrence.shape_matrix(a, 3, 2, p), 3, 2, p)
    G = ore.gcrd(ops, p)
    assert [list(c) for c in G] == [[(-2) % p, (-4) % p], [1, 1]]


def test_circle_lemma_matches_brute_force():
    import random
    rng = random.Random(4320)
    for _ in range(200):
        a, b = rng.randrange(spine.N), rng.randrange(spine.N)
        A, B = spine.subgroup(a), spine.subgroup(b)
        assert spine.subgroup(spine.meet(a, b)) == A & B
        span, todo = {0}, [0]
        while todo:
            x = todo.pop()
            for y in ((x + a) % spine.N, (x + b) % spine.N):
                if y not in span:
                    span.add(y)
                    todo.append(y)
        assert spine.subgroup(spine.join(a, b)) == frozenset(span)
        assert spine.contains(a, b) == (B <= A)
        assert len(A) == spine.order(a)


def test_tick_turns_two_carriers():
    import numpy as np
    c, cp, r, rp, g, w = spine.spine_clock()
    assert np.array_equal(spine.mpow(cp, 6), r @ rp)
    assert np.array_equal(spine.mpow(cp, 15), -spine.I8)
    assert round(abs(np.linalg.det((spine.mpow(cp, 6) - spine.I8).astype(float)))) == 25


def test_tick_is_one_bit():
    from math import gcd
    for x in range(4320):
        assert (864 % gcd(x, 4320) == 0) == (x % 5 != 0)


def test_day_and_coxeter_commutator_is_the_tick():
    import numpy as np
    _, cp, _, _, g, _ = spine.spine_clock()
    d = spine.day_clock()
    assert np.array_equal(d @ cp @ spine.inverse(d) @ spine.inverse(cp), g)


def test_clock_file_and_ledger_page_are_current():
    import json
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    assert json.loads((root / "data" / "clocks.json").read_text()) == json.loads(json.dumps(ledger.clock_matrices()))
    assert (root / "docs" / "LEDGER.md").read_text() == counts.ledger_page()


def test_hexagon_port_moments():
    import numpy as np
    a1, a2 = np.array([2, -2, 0, 0, 0, 0, 0, 0]), np.array([0, 2, -2, 0, 0, 0, 0, 0])
    hexagon = [a1, a1 + a2, a2, -a1, -a1 - a2, -a2]
    m = counts.lattice_moments(hexagon, [1, -1, 1, -1, 1, -1], 4)
    assert [x // 6 for x in m] == [1, 242, 58691, 14259954, 3470101592]


def test_six_site_moment_chain():
    chain = counts.six_site_chain()
    assert all(chain.values()), chain


def test_petersen_projectors_are_the_carrier_edge_projectors():
    proj = counts.petersen_projectors()
    assert all(proj.values()), proj


def test_pauli_generator_is_the_bath_on_its_half_periods():
    pauli = counts.pauli_bath()
    assert all(pauli.values()), pauli


def test_pauli_file_is_current():
    import json
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    assert json.loads((root / "data" / "pauli_half_periods.json").read_text()) == counts.pauli_table()


def test_rotor_plane_and_tick_doubling():
    assert all(counts.rotor_plane().values())
    assert all(counts.rotor_shadow().values())


def test_every_circle_map_kills_the_commutator():
    maps = counts.circle_maps()
    assert all(maps.values()), maps


def test_datum_cycle_and_spanda():
    for check in (counts.tick_tock, counts.spanda, counts.five_names):
        out = check()
        assert all(out.values()), out


def test_two_clocks_generate_order_20_not_the_circle():
    out = counts.two_clocks()
    assert all(out.values()), out
    time, obs = spine.subgroup(864), spine.subgroup(1080)
    assert len({(a + b) % spine.N for a in time for b in obs}) == 20
    assert [x % 5 for x in ledger.LEVELS] == [0, 4, 3, 2, 1]


def test_pauli_generator_is_the_quotient_bath_and_a_gksl_generator():
    out = counts.pauli_quotient()
    assert all(out.values()), out


def test_k5_incidences_are_root_systems():
    for check in (dots.k5_roots, dots.petersen_roots, dots.exterior):
        out = check()
        assert all(out.values()), out


def test_triangle_port_heat_coefficient():
    out = dots.triangle_port()
    assert all(out.values()), out


def test_glue_cosets_and_tick_momenta():
    for check in (dots.glue_cosets, dots.tick_momenta):
        out = check()
        assert all(out.values()), out


def test_atlas_and_four_cube():
    for check in (dots.atlas, dots.primary_split, dots.four_cube, dots.hodge70):
        out = check()
        assert all(out.values()), out


def test_k6_walks_and_the_l11_exclusion():
    for check in (dots.cone_line_graph, dots.paired_response, dots.band_expansion, dots.sym_square_orbits,
                  dots.walks_join, dots.l11_exclusion):
        out = check()
        assert all(out.values()), out


def test_coil_nakshatra_and_the_address_lift():
    for check in (dots.coil, dots.nakshatra_map, dots.address_lift, dots.notes_2303):
        out = check()
        assert all(out.values()), out
    # the tick bit is the time coordinate's, and the address does not see it
    for a in range(36):
        assert {ledger.contains_tick(x) for x in range(a, spine.N, 36)} == {True, False}


def test_golden_family_and_the_mpkg_block():
    for check in (dots.golden_family, dots.mpkg_block, dots.p31_clock):
        out = check()
        assert all(out.values()), out


def test_the_carrier_s5_is_the_cone_point_stabilizer():
    out = dots.cone_symmetry()
    assert all(out.values()), out
    obstruction = [j for j in dots.JOINS if j[:2] == ("pgl", "carrier")]
    assert len(obstruction) == 1 and obstruction[0][4] == gates.OBSTRUCTION


def test_grain_vortex_and_the_shift_law():
    for check in (dots.grain, dots.vortex, dots.shift_law, dots.golden_identities, dots.doubling_split,
                  dots.notes_2343):
        out = check()
        assert all(out.values()), out
    # doubling inverts a shift exactly when the shift has order dividing 3
    assert [s for s in range(spine.N) if 2 * s % spine.N == -s % spine.N] == [0, 1440, 2880]


def test_ticks_misses_towers_and_the_hankel_obstruction():
    for check in (dots.tick_miss, dots.doubling_orbits, dots.towers, dots.modules_8_11, dots.hankel_25):
        out = check()
        assert all(out.values()), out
    # the tick bit is the tick part: x misses exactly when 3456 x = 0
    assert all(ledger.contains_tick(x) == (3456 * x % spine.N != 0) for x in range(spine.N))


def test_eight_root_frame_symbol_and_protection():
    for check in (dots.eight_roots, dots.root_symbol, dots.protection, dots.notes_0029):
        out = check()
        assert all(out.values()), out


def test_edge_tick_port_moments_and_the_frozen_towers():
    for check in (dots.edge_tick, dots.port_moments, dots.notes_0051, dots.splits_corrections):
        out = check()
        assert all(out.values()), out
    # the tower of fives freezes: heights 3 and 4 agree on the circle
    assert pow(5, 5 ** 5, spine.N) == pow(5, 5 ** 5 ** 5, spine.N) == 245


def test_no_dot_hangs_by_one_join():
    nb = dots.no_bridge()
    assert all(nb.values()), nb
    for check in (dots.projective_plane, dots.air_801_joins, dots.gksl_census, dots.stage_landings,
                  dots.torus_calibration, dots.literal_incidences, dots.measure_band, dots.wave_calibration):
        out = check()
        assert all(out.values()), out
    # the check can fail: cutting both maps at the calibration cuts it off
    cut = [not (j[1] == "calibration" and j[4] != gates.OBSTRUCTION) for j in dots.JOINS]
    assert len(dots.components(cut)) == 2


def test_root_scheme_simplex_and_the_golden_split():
    for check in (dots.root_scheme, dots.frame_cliques, dots.simplex_grades, dots.golden_split, dots.notes_0154):
        out = check()
        assert all(out.values()), out
    # GOLDEN_GRAVITY corrected: a subgroup of the circle contains the ticks exactly when 5 divides its order
    ticks = spine.subgroup(ledger.TICK)
    assert all((ticks <= spine.subgroup(spine.N // d)) == (d % 5 == 0) for d in range(1, spine.N + 1) if spine.N % d == 0)


def test_sidebands_observer_charges_and_the_golden_hessian():
    for check in (dots.walk_convolutions, dots.clock_sidebands, dots.observer_completion, dots.six_site_torsion,
                  dots.seven_pairs_algebra, dots.golden_port, dots.charges, dots.census_stabilizers, dots.frame_faces,
                  dots.rotor_firewall, dots.notes_0252, dots.notes_0255):
        out = check()
        assert all(out.values()), out
    # the sideband lift needs the address: read the fibre index without subtracting it and most ticks come back wrong
    wrong = [j for j in range(spine.N)
             if (j % 36 + 36 * ((105 * (j % 32 // 4) + 40 * (j % 27 // 9) + 96 * (j % 5)) % 120)) % spine.N != j]
    assert len(wrong) > spine.N // 2
    # the hypercharge alone on the zero modes is anomalous; only with Lambda^2 at the other chirality does it cancel
    third, half = dots.Fraction(1, 3), dots.Fraction(1, 2)
    Y = [-third, -third, -third, half, half]
    assert sum(y ** 3 for y in Y) == dots.Fraction(5, 36) != 0
    assert "charges" in dots.LEVELS[-1][2] and dots.LEVEL_OF["charges"] == 5


def test_all_dots_are_joined():
    rep = dots.run()
    assert all(c.passed for c in rep.checks)
    assert len(dots.components([True] * len(dots.JOINS))) == 1
    # without the calibration's one map it is cut off: the connectivity check can fail
    cut = [not (j[1] == "calibration" and j[4] != gates.OBSTRUCTION) for j in dots.JOINS]
    assert len(dots.components(cut)) == 2


def test_every_level_is_joined():
    passed = [True] * len(dots.JOINS)
    lv = dots.levels(passed)
    assert lv["layers"] == list(range(1, 29))
    assert sorted(dots.LEVEL_OF) == sorted(dots.DOTS)
    assert all(len(c) == 1 for c in lv["inside"].values()) and all(lv["between"])
    # THEOREM joins alone leave out exactly the two conditional dots
    assert sorted(sorted(c) for c in lv["theorem"] if len(c) == 1) == [["cosmology"], ["gravity"]]
    for check in (dots.surface, dots.cube_cuts, dots.critical_momenta, dots.nine_torus, dots.triple, dots.readout,
                  dots.sound_light, dots.calibration):
        out = check()
        assert all(out.values()), out


def test_every_pair_of_levels_and_no_two_maps(monkeypatch):
    pairs = list(itertools.combinations(range(len(dots.LEVELS)), 2))
    assert all(dots.level_pairs()[p] for p in pairs)
    n2 = dots.no_two_maps()
    assert all(n2.values()), n2
    for check in (dots.tick_halfperiods, dots.light_symmetries, dots.outer_s6, dots.s5_weyl, dots.air801_surface,
                  dots.tick_cuts_f2, dots.small_joins, dots.hodge_halfper, dots.memory_clock):
        out = check()
        assert all(out.values()), out
    # both checks can fail: drop the maps between symmetry and physics, and that pair has none;
    # drop the 801 matrix's maps to the surface and from the residue plane, and two maps cut the matrix off
    joins = dots.JOINS
    monkeypatch.setattr(dots, "JOINS", [j for j in joins if {dots.LEVEL_OF[j[0]], dots.LEVEL_OF[j[1]]} != {1, 5}])
    assert dots.level_pairs()[(1, 5)] == 0
    monkeypatch.setattr(dots, "JOINS", [j for j in joins if j[:2] not in (("air801", "surface"), ("residue", "air801"))])
    assert not all(dots.no_two_maps().values())


def test_no_two_dots_and_the_memory_without_selection(monkeypatch):
    for check in (dots.memory_quotients, dots.massless_tower, dots.stiff_kernel, dots.cosmos_calibration,
                  dots.day_units, dots.frame_a8, dots.cube_frobenius, dots.grain_steps, dots.plane_synthemes):
        out = check()
        assert all(out.values()), out
    nd = dots.no_two_dots()
    assert all(nd.values()), nd
    # a non-unit power of the memory clock changes its cycle type, so only the 24 unit steppings are conjugate to it
    perm, cycles, P = dots._memory()
    lengths = lambda p: sorted(len(c) for c in dots._cycles(p))
    assert lengths(P[7]) == lengths(perm) != lengths(P[2])
    # both checks can fail: without the three new conditional maps the datum and the triple cut off the product
    # geometry and FLRW, and without the memory's 24 maps THEOREM joins leave the memory clock out
    joins = dots.JOINS
    monkeypatch.setattr(dots, "JOINS", [j for j in joins
                                        if j[5] not in ("massless_tower", "stiff_kernel", "cosmos_calibration")])
    assert not all(dots.no_two_dots().values())
    monkeypatch.setattr(dots, "JOINS", [j for j in joins if j[5] != "memory_quotients"])
    assert ["memory"] in [sorted(c) for c in dots.components([True] * len(dots.JOINS), statuses=(gates.THEOREM,))]


def test_the_0928_notes_replay():
    for check in (dots.walks_by_angle, dots.port_leak, dots.two_ticks, dots.filled_simplex, dots.charge_marks,
                  dots.infrared, dots.stated_block, dots.notes_1007, dots.notes_1007_arithmetic, dots.golden_root_port,
                  dots.shared_bath, dots.notes_1038):
        out = check()
        assert all(out.values()), out
    # the Hankel test can fail: a measure with two atoms has a vanishing 3 x 3 Hankel determinant
    import sympy as sp
    m = [sp.Rational(1 + 2 ** k, 2) for k in range(5)]
    assert sp.Matrix(3, 3, lambda i, j: m[i + j]).det() == 0


def test_the_1112_replay():
    for check in (dots.marked_charge, dots.twelve_markings, dots.golden_infrared, dots.word_duads, dots.words_c5,
                  dots.notes_1119, dots.notes_1119_arithmetic):
        out = check()
        assert all(out.values()), out
    import sympy as sp
    # the isotropy test can fail: E8's roots are not an 8-design
    assert dots._isotropic(8) is None
    # the window can fail: a ratio above (49 + 12 sqrt5)/41 makes rho_psi negative
    r5 = sp.sqrt(5)
    W = sp.Matrix([[(17 + 5 * r5) / 45, (17 - 5 * r5) / 45], [(13 + r5) / 45, (13 - r5) / 45]])
    rho = W.inv() * sp.Matrix([2, 1])
    assert sp.N(rho[1]) < 0 < sp.N(rho[0])
    # without the sign twist the duads are another module: the reflection's trace is 3, not 1
    words, C, R = dots._words()
    Ct, Rt, e = dots._duads()
    assert (R.trace(), Rt.trace(), Rt.applyfunc(abs).trace()) == (1, 1, 3)


def test_the_1144_replay():
    for check in (dots.hodge_contexts, dots.context_responses, dots.overlap_hodge, dots.hodge_averaging,
                  dots.word_sylow, dots.clock_root_address, dots.coordinate_bridge, dots.notes_1207):
        out = check()
        assert all(out.values()), out
    import sympy as sp
    J, P, Pc, U, K, Qf, Pm, L = dots._hodge()
    ctx = dots._contexts()
    Se = sum((C for C, s in ctx if s == 1), sp.zeros(10))
    So = sum((C for C, s in ctx if s == -1), sp.zeros(10))
    # the coefficient tests can fail: 16/5 is not the inverse's coefficient, and the parity difference is not J itself
    assert not dots._zero(Se * sp.Rational(16, 5) * So - Pc) and dots._zero(Se * sp.Rational(5, 16) * So - Pc)
    assert not dots._zero(So - Se - J)
    # the defect vanishes exactly when the two fixed responses agree
    G = 3 * P["+"] + 3 * P["-"] + 5 * P["phi"] + 7 * P["psi"]
    assert dots._zero(J * G - G * J)
    G = 2 * P["+"] + 3 * P["-"] + 5 * P["phi"] + 7 * P["psi"]
    assert not dots._zero(J * G - G * J)


def test_the_theorem_diagram(monkeypatch):
    for check in (dots.datum_orbit, dots.witness_loop, dots.frame_affine, dots.tick_actions, dots.theorem_connectivity):
        out = check()
        assert all(out.values()), out
    # the checks can fail: without S5 -> datum the datum lies on two THEOREM maps, which then cut it off; without
    # time -> triple the number and physics levels are joined by one THEOREM map
    joins = dots.JOINS
    monkeypatch.setattr(dots, "JOINS", [j for j in joins if j[:2] != ("S5", "datum")])
    out = dots.theorem_connectivity()
    assert not out["every one of those dots lies on at least three THEOREM maps"]
    assert not out["no one THEOREM map and no two THEOREM maps hold that diagram together"]
    monkeypatch.setattr(dots, "JOINS", [j for j in joins if j[:2] != ("time", "triple")])
    out = dots.theorem_connectivity()
    assert not out["every pair of the six levels is joined directly by at least two THEOREM maps"]
    assert out["no one THEOREM map and no two THEOREM maps hold that diagram together"]
    # the frame maps really are affine: j -> 3457 j keeps the address, while j -> 2 j does not
    import numpy as np
    j = np.arange(4320)
    assert np.array_equal(3457 * j % 4320 % 36, j % 36) and not np.array_equal(2 * j % 4320 % 36, j % 36)


def test_the_1259_replay():
    for check in (dots.agni_soma, dots.agni_factor, dots.agni_pullback, dots.source_phase, dots.sylow_lines,
                  dots.notes_1259, dots.notes_1259_arithmetic):
        out = check()
        assert all(out.values()), out
    import sympy as sp
    E, N5, sym, F, a, b = dots._source()
    # the witness is the hub's: move one coordinate of b and the commutator's square leaves 1392
    Fw = F(a, N5 * sp.Matrix([-1, -2, -1, -2, 1]))
    assert (Fw.T * Fw)[0] != 1392
    # the factorization pins L_out: with the opposite sign on its fixed part it fails at the witness
    Pc, R5, U, K, Qf, Pm, L = dots._marked()
    Q, m, h = dots._chain()
    D = dots.compound2(sp.Matrix(5, 5, lambda r, c: int(r == (2 * c) % 5)))
    Kv = sp.eye(5) + 2 * (R5 + R5.T)
    wedge = lambda x, y: sp.Matrix([x[i] * y[j] - x[j] * y[i] for i, j in E])
    mix = Q * Kv * ((h.T * a)[0] / 10 * m * b - (h.T * b)[0] / 10 * m * a)
    for sign, holds in ((-1, True), (1, False)):
        Lout = (sign * Qf + 3 * D * Qf + 2 * Pm) / 5
        assert (F(a, b) == Lout * wedge(m * a, m * b) - sp.Rational(2, 5) * mix) == holds


def test_the_band_edge_is_256():
    out = band.edge()
    assert all(out.values()), out
    # the reduced inequality is sharp exactly in dimension 8: at x = (1, ..., 1) both sides are 16, while in nine
    # dimensions 2^(9/2) exceeds 2 + 36/2
    assert 2 ** 4 == 2 + 28 // 2 and 2 ** 4.5 > 2 + 36 / 2
    # the box bound alone cannot pass a zero: around the centre of (4, 2, 2) its lower bound is not positive
    import numpy as np
    L, U = np.full((1, 3), np.pi / 4 - 0.01), np.full((1, 3), np.pi / 4 + 0.01)
    assert band.lower_bound((4, 2, 2), L, U)[0] <= 0
    # and the edge is where the canon says: Lambda = -16 at the band vertex, above -16 just off it
    assert abs(band.lam(np.pi * np.array([1, 1, 1, 1, 0, 0, 0, 0])) + 16) < 1e-12
    assert band.lam(np.pi * np.array([1, 1, 1, 1, 0.1, 0, 0, 0])) > -16


def test_the_1426_replay():
    for check in (dots.wedge_port, dots.three_ports, dots.root_shell_krylov, dots.schur_memory, dots.hodge_star,
                  dots.syntheme_bridge, dots.sylow_frame, dots.word_source, dots.clock_sylow, dots.band_top,
                  dots.notes_1418):
        out = check()
        assert all(out.values()), out
    import sympy as sp
    # one root shell is what makes the growth unending: the origin with the all-ones function on the roots closes at
    # the first step, since Delta delta_0 = 240 delta_0 - 1_R, so its degree-1 block Hankel has rank 3, not 4
    R10, V, W, Bw, G, h, Hc = dots._wedge()
    count = {c: int((G == c).sum()) for c in h}
    M = [sp.Matrix([[h[2][n], 240 * h[1][n]], [240 * h[1][n], sum(count[c] * h[c][n] for c in h)]]) for n in range(3)]
    assert sp.Matrix(sp.BlockMatrix([[M[0], M[1]], [M[1], M[2]]])).rank() == 3
    # the Pfaffian of the quartic witness keeps its value under a 3-cycle and flips under a transposition
    E, N5, sym, F, a, b = dots._source()
    A, B = sym(N5 * sp.Matrix([2, 1, -1, 0, 1])), sym(N5 * sp.Matrix([0, -1, 1, 1, -2]))
    R = sp.Matrix.vstack(sp.eye(4), -sp.ones(1, 4))
    pf = lambda X: (lambda Y: Y[0, 1] * Y[2, 3] - Y[0, 2] * Y[1, 3] + Y[0, 3] * Y[1, 2])(R.T * X * R)
    for p, sign in (((1, 2, 0, 3, 4), 1), ((1, 0, 2, 3, 4), -1)):
        P = sp.Matrix(5, 5, lambda r, c: int(r == p[c]))
        assert pf(P * (A * B - B * A) * P.T) == sign * 175


def test_the_1534_replay():
    for check in (dots.pair_frame, dots.parity_ports, dots.dark_port, dots.notes_1534):
        out = check()
        assert all(out.values()), out
    import numpy as np
    # the hub's seed, read without the twin's outer automorphism, is not a lattice site here; with it, it is x0
    X, V4, W4 = dots._norm_four()
    keys = {tuple(V4[k]) + tuple(W4[k]) for k in range(len(X))}
    assert (-12, -2, -2, 8, 8, -4, -4, 6, -4, 6) not in keys and (-12, -2, -2, 8, 8, 4, 4, -6, 4, -6) in keys
    # the odd port is odd under inversion and the root-wedge port even: that is the whole parity argument
    R10, V, W, Bw, G, h, Hc = dots._wedge()
    neg = [{tuple(r): k for k, r in enumerate(R10)}[tuple(-r)] for r in R10]
    Od = dots._odd_port()
    assert np.array_equal(Od[neg], -Od) and np.array_equal(Bw[neg], Bw)


def test_the_1616_replay():
    for check in (dots.two_dark, dots.fusion_frame, dots.source_coding, dots.k4_planes, dots.notes_1616):
        out = check()
        assert all(out.values()), out
    import sympy as sp
    from sympy.matrices.normalforms import smith_normal_form
    # the triple wedge is even in the twin block, so the twin's sign convention cannot change the second dark port
    X, V4, W4 = dots._norm_four()
    tw = lambda v, w: sp.Matrix([v, w, [5 * a * b - sum(p * q for p, q in zip(v, w)) for a, b in zip(v, w)]])
    assert all(tw(V4[k].tolist(), W4[k].tolist()).extract([0, 1, 2], list(t)).det()
               == tw(V4[k].tolist(), (-W4[k]).tolist()).extract([0, 1, 2], list(t)).det()
               for k in range(0, 2160, 97) for t in itertools.combinations(range(5), 3))
    # without the sign twist on the dark four the mixer orbit is not well defined: each label gets X and -X
    H, sig, S5, sgn, U = dots._six_lines()
    Xs, F = dots._mixers()
    perm = lambda p: sp.Matrix(5, 5, lambda r, c: int(r == p[c]))
    plain = {}
    for p in S5:
        plain.setdefault(sig[p][0], set()).add(tuple(dots.compound2(perm(p)) * Xs[0] * perm(p).T))
    assert all(len(v) == 2 for v in plain.values())
    # a Sylow line inside T's image leaves the word lattice at index 3
    E, N5, sym, Fc, a0, b0 = dots._source()
    G = N5.T * N5
    V = G.inv() * N5.T * sp.Matrix.hstack(*H)
    ell = sp.Matrix([[1, 2, 2, 1, 2]])
    inside = [i for i in range(6) if (ell * V)[i] % 3 == 0]
    assert all(smith_normal_form(sp.Matrix.hstack(dots._word_adapter(), V[:, i]), domain=sp.ZZ)[4, 4] == 3
               for i in inside)
    # source vectors from two different K4 planes do not commute
    P0 = N5 * sp.Matrix.hstack(*N5.extract([k for k, e in enumerate(E) if 0 in e], list(range(5))).nullspace())
    P1 = N5 * sp.Matrix.hstack(*N5.extract([k for k, e in enumerate(E) if 1 in e], list(range(5))).nullspace())
    assert not Fc(P0[:, 0], P1[:, 0]).is_zero_matrix


def test_the_1651_replay():
    for check in (dots.k4_complete, dots.dark_branches, dots.tomography, dots.notes_1651):
        out = check()
        assert all(out.values()), out
    import sympy as sp
    E, N5, sym, F, a0, b0 = dots._source()
    G = N5.T * N5
    # a generic dark bivector is not a plane: the sum of two kernel basis vectors fails a Pluecker quadric
    pairs = list(itertools.combinations(range(5), 2))
    W = sp.Matrix.hstack(*[F(N5[:, i], N5[:, j]) for i, j in pairs])
    K = W.nullspace()
    b = K[0] + K[1]
    c = lambda i, j: b[pairs.index((i, j))] if i < j else -b[pairs.index((j, i))]
    assert any(c(i, j) * c(k, l) - c(i, k) * c(j, l) + c(i, l) * c(j, k) != 0
               for i, j, k, l in itertools.combinations(range(5), 4))
    # without the word congruence every plane lattice has minimum 4 twice over: the 24 and 32 come from ell
    for u in dots._planes():
        x, y = dots._lagrange(u[:, 0], u[:, 1], G)
        assert ((x.T * G * x)[0], (y.T * G * y)[0]) == (4, 4)
    # the rotating ansatz fails off the two roots: X = 8 leaves the hidden equation unbalanced at r = 1/2
    assert (10 - 8) * sp.Rational(-1, 2) != -16 * sp.Rational(1, 2) ** 3 and (10 - 8) * 3 != -2
    # with X = 0 the response cannot separate q from b: (q, b) = (1/7, 1/3) and (2/7, 7/20) give the same response
    Bs = sp.Matrix(carrier.signed_incidence())
    PB = sp.diag(sp.eye(10) - Bs.T * Bs / 5, sp.zeros(5))
    PD = sp.diag(sp.zeros(10), sp.eye(5) - sp.ones(5, 5) / 5)
    K = lambda q, b: PB * 2 + PD / b + q * PD
    assert K(sp.Rational(1, 7), sp.Rational(1, 3)) == K(sp.Rational(2, 7), sp.Rational(7, 20))


def test_the_1731_replay():
    for check in (dots.quadratic_frames, dots.dark_readout, dots.cubic_null, dots.golden_bridge, dots.notes_1731):
        out = check()
        assert all(out.values()), out
    import sympy as sp
    E, N5, sym, F, a0, b0 = dots._source()
    H, sig, S5, sgn, U = dots._six_lines()
    G = N5.T * N5
    # the five planes and six Golden lines alone reach only 10 of the 15 quadratics: the edges are needed
    V = G.inv() * N5.T * sp.Matrix.hstack(*H)
    proj = [u * (u.T * G * u).inv() * u.T * G for u in dots._planes()] + [
        V[:, j] * V[:, j].T * G / (V[:, j].T * G * V[:, j])[0] for j in range(6)]
    assert sp.Matrix.hstack(*[sp.Matrix(list(x)) for x in proj]).rank() == 10
    # six detectors can be split into two halves that each miss a direction, so six intensities cannot always suffice
    halves = ([sp.eye(4)[:, 0], sp.eye(4)[:, 1], sp.Matrix([-1, -1, -1, -1])],
              [sp.eye(4)[:, 2], sp.eye(4)[:, 3], sp.Matrix([1, 2, 3, 5])])
    assert all(sp.Matrix.hstack(*h).rank() < 4 for h in halves)
    # the even eigenspace of a transposition is not cubic-null
    av, bv = sp.Matrix(sp.symbols("a0:5")), sp.Matrix(sp.symbols("b0:5"))
    A, B = sym(N5 * av), sym(N5 * bv)
    phi1 = sp.expand(((A ** 2 + B ** 2) * A).trace() / 6)
    plus = (G.inv() * N5.T * dots._edge_perm((1, 0, 2, 3, 4)) * N5 - sp.eye(5)).nullspace()
    a = sum((sp.Symbol(f"s{k}") * w for k, w in enumerate(plus)), sp.zeros(5, 1))
    assert sp.expand(phi1.subs(dict(zip(list(av) + list(bv), list(a) + [0] * 5)))) != 0


def test_the_1804_replay():
    for check in (dots.dark_measurement, dots.plane_tomography, dots.notes_1804):
        out = check()
        assert all(out.values()), out
    import itertools
    import sympy as sp
    # without the dark metric the five planes are no tight frame, and four of the five planes are no measurement
    D = 15 * sp.eye(4) - 3 * sp.ones(4, 4)
    P = [sp.eye(4)[:, k] for k in range(4)] + [-sp.ones(4, 1)]
    assert sum((p * p.T for p in P), sp.zeros(4)) == sp.eye(4) + sp.ones(4, 4)
    assert sum((p * p.T * D / 15 for p in P[:4]), sp.zeros(4)) != sp.eye(4)
    # the bright six alone leave the dark four unread, so the commutator by itself cannot immerse the planes
    E, N5, sym, F, a0, b0 = dots._source()
    W = sp.Matrix.hstack(*[F(N5[:, i], N5[:, j]) for i, j in itertools.combinations(range(5), 2)])
    assert len(W.nullspace()) == 4


def test_the_1835_replay():
    for check in (dots.seventh_sensor, dots.preparability, dots.exterior_code, dots.dark_information,
                  dots.causal_records, dots.parent_readers, dots.two_36s, dots.golden30, dots.parent_closure,
                  dots.notes_1835):
        out = check()
        assert all(out.values()), out
    import functools
    import numpy as np
    import sympy as sp
    G, pairs, wedge, Hm, W, Km, z = dots._dark_chart()
    # the six bright readings alone miss every dark ray, and ell12 alone repeats its labels
    ell12 = sp.Matrix([0, -3, 0, -1, 0, 3, 1, 0, 1, -1])
    assert all((W * x).is_zero_matrix for x in z)
    assert len({(ell12.T * x)[0] for x in z}) == 2
    # without the dark probes the bright frame inverts only the bright six
    E, N5, sym, F, a0, b0 = dots._source()
    H, sig, S5, sgn, U = dots._six_lines()
    V = G.inv() * N5.T * sp.Matrix.hstack(*H)
    Q = [wedge(V[:, i], V[:, j]) for i, j in itertools.combinations(range(6), 2)]
    PD = Km * (Km.T * Hm * Km).inv() * Km.T * Hm
    assert sum((x * x.T * Hm for x in Q), sp.zeros(10)) * (sp.eye(10) - PD) / 144 != sp.eye(10)
    # a reflection of D10 in place of t delays nothing, and four r-settings never reach the whole parent
    A = dots._a6()
    assert len(dots._rref_p(np.vstack([A["F30"], A["right"](A["F30"], A["w"])]))[1]) == 30
    r4 = [functools.reduce(A["mul"], [A["r"]] * k) for k in range(1, 4)]
    assert len(dots._rref_p(np.vstack([A["O90"]] + [A["right"](A["O90"], g) for g in r4]))[1]) < 360



def test_the_one_object():
    for check in (cyclotomic.cyclotomic_line, cyclotomic.galois_clocks, cyclotomic.residue_plane,
                  cyclotomic.tick_normalizer, cyclotomic.clock_residues, cyclotomic.golden_gauss,
                  cyclotomic.carrier_shadows, cyclotomic.parent_hexad, unify.uniqueness, unify.derivation,
                  dots.notes_1909, dots.address_map, dots.notes_1950, dots.notes_2033, dots.notes_2117,
                  dots.notes_2150, dots.notes_2222, dots.notes_2253,
                  dots.notes_2325, dots.notes_2356, dots.six_lines, dots.notes_0032,
                  dots.petersen_sequence, dots.notes_0117):
        out = check()
        assert all(out.values()), out
    import numpy as np
    k = cyclotomic.clocks()
    I8 = np.eye(8, dtype=np.int64)
    # the carrier rotation alone fixes the twin A4', so it has no finite residue plane; the tick alone does not make
    # E8 a cyclic line (its ring Z[zeta5] has rank 4)
    assert np.linalg.matrix_rank((I8 - k["r"]).astype(float)) == 4
    B, Binv, C, Cinv, R, RB = spine.frame()
    g = k["g"]
    assert all(np.linalg.matrix_rank(np.array([spine.mpow(g, j) @ v for j in range(8)], dtype=float)) == 4 for v in RB[:24])
    # the golden clock is not F25-linear, and a wrong derivation edge is caught
    Q = cyclotomic.on_plane(k["golden"])
    X = cyclotomic.on_plane(k["c"])
    assert not np.array_equal((Q @ X) % 5, (X @ Q) % 5)
    assert unify._join("L0", "residue", "k5_roots") is None
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    assert (root / "docs" / "UNIFIED.md").read_text() == unify.unified_page()

def test_the_three_primes():
    for check in (primes.regular_clocks, primes.cyclotomic_lines, primes.no_sixteen, primes.prime_clocks,
                  primes.prime_residues, primes.half_turn, primes.sun, primes.decad, primes.parent_cover):
        out = check()
        assert all(out.values()), out
    import numpy as np
    k = cyclotomic.clocks()
    # the clocks alone reach only the affine 20 on the decad, ten of them in A6
    D = primes._decad_action()
    affine = primes._closure([D["R"], D["D"]])
    assert len(affine) == 20 and len(affine & set(D["H"])) == 10
    # the day is not F9-linear on the sun's momenta, so it is not in the parent's A6, and r cannot go to the day
    phi = primes.sun_geometry()["phi"]
    Qd = primes.on_sun(k["day"][None])[0]
    assert not np.array_equal((Qd @ phi) % 3, (phi @ Qd) % 3)
    A = dots._a6()
    assert primes._iso([A["r"], A["t"]], [D["D"], D["R"]]) is None
    # the golden clock has roots that do not generate E8 over Z[v], and a wrong root misses the day's data
    RB = spine.frame()[5]
    P = [spine.mpow(k["golden"], j) for j in range(8)]
    assert any(abs(round(np.linalg.det(np.array([M @ r for M in P], dtype=float).T))) == 5 for r in RB)
    # the parent hangs from the sun's decad in the derivation
    assert unify.DERIVATION["parent"] == ("sun", "primes.decad")
    rep = primes.run()
    assert all(c.passed for c in rep.checks)


def test_the_four_places():
    for check in (places.band_at_places, places.golden_places, places.qubit_primes, places.limits, places.sectors):
        out = check()
        assert all(out.values()), out
    import numpy as np
    k = cyclotomic.clocks()
    # a clock with eigenvalue 1 has no finite set of fixed momenta: the carrier rotation r fixes the twin A4'
    I8 = np.eye(8, dtype=np.int64)
    assert round(abs(np.linalg.det((I8 - k["r"]).astype(float)))) == 0
    # the golden ratio is not a scalar mod 3 and not the identity mod 2, and the circle's psi is far above 8
    assert places._psi(4320) > 8 and places._psi(30) <= 8 and places._psi(60) == 8 and places._psi(72) > 8
    # the four sectors hang from their places in the derivation
    assert unify.DERIVATION["halfper"][0] == "cyclo" and unify.DERIVATION["momenta"][0] == "residue"
    rep = places.run()
    assert all(c.passed for c in rep.checks)


def test_the_principal_circle():
    for check in (principal.circle, principal.regular_steps, principal.band_on_circle, principal.critical_steps):
        out = check()
        assert all(out.values()), out
    import numpy as np
    from math import gcd
    rho, rs, ht = principal.weyl_vector()
    # rho is no fixed momentum of the seed's own tick or Coxeter clock: the principal points live in another torus
    k = cyclotomic.clocks()
    I8 = np.eye(8, dtype=np.int64)
    assert not any(np.allclose(((I8 - k[n]) @ rho) / d, np.round(((I8 - k[n]) @ rho) / d)) for n in ("g", "c") for d in (5, 30))
    # the step of order 6 is not critical, and its centralizer A4 + A3 has rank 7
    from oes import handover, spine
    R = spine.frame()[4]
    assert handover.stabiliser(R, rs * 720 / 4320)[0] == "A4+A3"
    # the circle and the derivation: the circle stays an input, its interface the selection 144 -> c'
    assert unify.DERIVATION["principal"] == ("E8", "principal.circle") and "circle" in unify.INPUTS
    assert 4320 // gcd(144, 4320) == 30 and 4320 // gcd(864, 4320) == 5


def test_the_free_chain():
    out = dots.free_chain()
    assert all(out.values()), out
    from math import factorial
    # a measure on three points has a chain that stops at the third step
    assert court.chebyshev([sum(Fraction(x) ** n for x in (0, 100, 256)) for n in range(12)])[2] == 3
    # the edge exponents show: the weight E (256 - E), exponent 1 instead of 3, misses the return chain's beta_45 by 14
    beta = lambda a, b: Fraction(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))
    lin = court.chebyshev([256 ** n * beta(n + 2, 2) / beta(2, 2) for n in range(91)])
    ret = court.chebyshev(court.laplacian_moments(recurrence.load_walks(), 90))
    assert abs(lin[1][44] - ret[1][44]) > 10


def test_the_particle_assignment_on_e8_roots():
    for check in (assignment.factors, assignment.moments, assignment.standard_model, assignment.choices,
                  assignment.chirality, assignment.generations, assignment.couplings, assignment.six_site_port):
        out = check()
        assert all(out.values()), out
    # J squares to -1 and swaps the factors; the opposite sign does not keep the roots
    import sympy as sp
    J = assignment.swap()
    assert J * J == -sp.eye(8)
    # a wrong hypercharge (colour and weak exchanged) breaks the charges, and a relabelled twin moves the port
    Y, Q, twin = assignment.Y, assignment.QE, assignment.TWIN
    try:
        assignment.Y = [Fraction(-1, 2)] * 2 + [Fraction(1, 3)] * 3 + [Fraction(0)] * 3
        assignment.QE = [y + t for y, t in zip(assignment.Y, assignment.T3)]
        assert not all(assignment.standard_model().values())
        assignment.Y, assignment.QE = Y, Q
        assignment.TWIN = twin[[3, 1, 2, 0, 4]]
        assignment.TWIN_DUAD = {d: assignment.TWIN[d[0]] + assignment.TWIN[d[1]] for d in assignment.DUADS}
        assert not all(assignment.generations().values())
    finally:
        assignment.Y, assignment.QE, assignment.TWIN = Y, Q, twin
        assignment.TWIN_DUAD = {d: twin[d[0]] + twin[d[1]] for d in assignment.DUADS}
    rep = assignment.run()
    assert all(c.passed for c in rep.checks)


def test_assignment_table_is_current():
    import json
    assert json.loads(assignment.DATA.read_text()) == assignment.table_data()


def test_dots_page_is_current():
    from pathlib import Path
    root = Path(__file__).resolve().parent.parent
    assert (root / "docs" / "DOTS.md").read_text() == dots.dots_page()


def test_typescript_port_of_the_spine():
    import shutil
    import subprocess
    from pathlib import Path
    node = shutil.which("node")
    if node is None:
        pytest.skip("node not installed")
    version = subprocess.run([node, "--version"], capture_output=True, text=True).stdout.strip().lstrip("v")
    if tuple(int(x) for x in version.split(".")[:2]) < (22, 6):
        pytest.skip("node 22.6+ needed for --experimental-strip-types")
    runner = Path(__file__).resolve().parent.parent / "ports" / "ts" / "run.mjs"
    out = subprocess.run([node, "--experimental-strip-types", "--no-warnings", str(runner)],
                         capture_output=True, text=True, timeout=120)
    assert out.returncode == 0, out.stdout + out.stderr
    assert "residual 0" in out.stdout
