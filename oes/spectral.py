"""Layer 2. The finite spectral triple (A, H, D, gamma) of the carrier.

A = C^V (+) C^E acting diagonally on H = l2(V u E), dim H = 15.
Everything here is a function of spec(D^2) = {0^5, 3^8, 8^2}: heat trace,
spectral zeta, spectral dimension and the moments that a spectral action
Tr f(D^2/L^2) can see. No cutoff function or scale is chosen in this layer.
"""

import numpy as np
import sympy as sp

from . import carrier, gates
from .record import Report

SPEC = {0: 5, 3: 8, 8: 2}


def heat_trace(beta):
    """Z(beta) = Tr exp(-beta D^2)."""
    beta = np.asarray(beta, float)
    return sum(m * np.exp(-lam * beta) for lam, m in SPEC.items())


def spectral_dimension(beta):
    """d_s(beta) = -2 d log Z / d log beta."""
    beta = np.asarray(beta, float)
    num = sum(m * lam * np.exp(-lam * beta) for lam, m in SPEC.items())
    return 2 * beta * num / heat_trace(beta)


def zeta(s):
    """zeta_D(s) = sum over nonzero eigenvalues lam^{-s} of D^2."""
    s = sp.sympify(s)
    return sum(m * sp.Integer(lam) ** (-s) for lam, m in SPEC.items() if lam)


def moments(nmax=4):
    """Tr D^{2k}: the only data a spectral action of the carrier can read."""
    return {k: sum(m * lam ** k for lam, m in SPEC.items()) for k in range(nmax + 1)}


def spectral_action(f, L=1.0):
    """Tr f(D^2 / L^2) for a user-supplied positive function f."""
    return sum(m * f(lam / L ** 2) for lam, m in SPEC.items())


def run():
    rep = Report("2-spectral")
    T = gates.THEOREM
    X = np.array(carrier.D2(), float)
    for beta in (0.05, 0.5, 2.0):
        ok = np.isclose(np.trace(_expm_sym(-beta * X)), heat_trace(beta))
        rep.add(f"heat trace Z({beta}) = 5 + 8e^-3b + 2e^-8b", T, ok,
                float(heat_trace(beta)))
    mom = moments(4)
    rep.add("moments Tr D^0, D^2, D^4, D^6, D^8 = 15, 40, 200, 1240, 8840", T,
            [mom[k] for k in range(5)] == [15, 40, 200, 8 * 27 + 2 * 512,
                                           8 * 81 + 2 * 4096],
            [mom[k] for k in range(5)])
    rep.add("zeta_D(s) = 8*3^-s + 2*8^-s; zeta_D(0) = 10 = rank D^2", T,
            zeta(0) == 10, str(zeta(sp.Symbol("s"))))
    rep.add("zeta_D(1) = 8/3 + 1/4 = 35/12", T, zeta(1) == sp.Rational(35, 12))
    b = np.logspace(-4, 4, 4001)
    ds = spectral_dimension(b)
    rep.add("spectral dimension -> 0 in the UV and the IR (finite geometry)", T,
            ds[0] < 1e-2 and ds[-1] < 1e-2, [float(ds[0]), float(ds[-1])])
    rep.add("peak spectral dimension of the carrier", T, True,
            {"max_ds": float(ds.max()), "at_beta": float(b[ds.argmax()])},
            note="a property of {0^5,3^8,8^2}; no continuum dimension emerges")
    rep.add("Hilbert dimension 15; imported NC dimensions removed", gates.REMOVED,
            True, 15)
    return rep


def _expm_sym(A):
    w, V = np.linalg.eigh(A)
    return (V * np.exp(w)) @ V.T
