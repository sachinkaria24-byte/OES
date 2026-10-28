import pytest

from oes import (binding, carrier, cosmology, court, frontier, gates, gatework, glue, gravity,
                 handover, joins, literal, native, observer, recurrence, spacetime, spectral)

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
