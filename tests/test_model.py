import itertools
from fractions import Fraction

import pytest

from oes import (assignment, binding, canon_sync, carrier, cosmology, counts, court, dots, frontier, gates,
                 gatework, glue, gravity, handover, joins, ledger, literal, native, observer, recurrence, snapshot,
                 spacetime, spectral, spine, waves)

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
    assert lv["layers"] == list(range(1, 25))
    assert sorted(dots.LEVEL_OF) == sorted(dots.DOTS)
    assert all(len(c) == 1 for c in lv["inside"].values()) and all(lv["between"])
    # THEOREM joins alone leave out exactly the two conditional dots and the memory clock, joined by selection
    assert sorted(sorted(c) for c in lv["theorem"] if len(c) == 1) == [["cosmology"], ["gravity"], ["memory"]]
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
    # drop the 801 matrix's map to the surface, and two maps cut the matrix off
    joins = dots.JOINS
    monkeypatch.setattr(dots, "JOINS", [j for j in joins if {dots.LEVEL_OF[j[0]], dots.LEVEL_OF[j[1]]} != {1, 5}])
    assert dots.level_pairs()[(1, 5)] == 0
    monkeypatch.setattr(dots, "JOINS", [j for j in joins if j[:2] != ("air801", "surface")])
    assert not all(dots.no_two_maps().values())


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
