import pytest

from oes import (binding, canon_sync, carrier, cosmology, court, frontier, gates, gatework, glue, gravity,
                 handover, joins, literal, native, observer, recurrence, snapshot, spacetime,
                 spectral, spine, waves)

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
