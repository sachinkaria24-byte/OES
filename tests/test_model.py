import pytest

from oes import carrier, cosmology, gates, gravity, native, observer, spacetime, spectral

LAYERS = {
    "carrier": carrier.run,
    "spectral": spectral.run,
    "spacetime": spacetime.run,
    "native": lambda: native.run(simulate=False),
    "observer": observer.run,
    "gravity": gravity.run,
    "cosmology": cosmology.run,
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
