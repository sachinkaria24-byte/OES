"""Layer 7. Cosmology: an FLRW minisuperspace of the conditional product geometry.

Status CONDITIONAL throughout. The canon has no cosmology: IceCube/LHAASO
scales and the vacuum amplitude are REMOVED, TIME_BIND is UNBOUND. What can be
done honestly is to take the conditional gravity of layer 6 (G and Lambda_cc
from the spectral action with explicit free inputs) and let the carrier field
be spatially homogeneous on a flat FLRW background:

    S = int dt a^3 [ -3 a'^2/(8 pi G a^2) + 1/2 |psi'|^2 - 1/2 m^2 <psi, D^2 psi>
                     - Lambda_cc / (8 pi G) ]

    psi'' + 3 H psi' + m^2 D^2 psi = 0,
    H^2 = (8 pi G / 3) rho + Lambda_cc / 3,    H' = -4 pi G |psi'|^2.

The carrier then has a definite cosmological content once the inputs are
chosen: the five kernel modes are massless (kinetic, rho ~ a^-6), the eight
lambda = 3 and two lambda = 8 modes are massive (time-averaged rho ~ a^-3, dust),
and Lambda_cc either dominates at once (natural cutoff, the vacuum-energy
problem) or is tuned away. No observed cosmological number is predicted.
"""

import numpy as np
from scipy.integrate import solve_ivp

from . import carrier, gates, gravity
from .record import Report


class FLRW:
    def __init__(self, G, Lcc, m=1.0):
        self.G, self.L, self.m = G, Lcc, m
        self.K = m ** 2 * np.array(carrier.D2(), float)
        P = carrier.spectral_projectors()
        self.P = {lam: np.array(p, float) for lam, p in P.items()}

    def rho(self, psi, v):
        return 0.5 * v @ v + 0.5 * psi @ self.K @ psi

    def H0(self, psi, v):
        return np.sqrt(8 * np.pi * self.G / 3 * self.rho(psi, v) + self.L / 3)

    def rhs(self, t, X):
        lna, H = X[0], X[1]
        psi, v = X[2:17], X[17:]
        return np.concatenate([[H, -4 * np.pi * self.G * v @ v],
                               v, -3 * H * v - self.K @ psi])

    def evolve(self, psi0, v0, t_end, n=4000):
        X0 = np.concatenate([[0.0, self.H0(psi0, v0)], psi0, v0])
        ts = np.linspace(0, t_end, n)
        sol = solve_ivp(self.rhs, (0, t_end), X0, t_eval=ts, method="DOP853",
                        rtol=1e-11, atol=1e-13)
        return sol

    def constraint(self, X):
        H, psi, v = X[1], X[2:17], X[17:]
        return H ** 2 - 8 * np.pi * self.G / 3 * self.rho(psi, v) - self.L / 3

    def sector_rho(self, X):
        psi, v = X[2:17], X[17:]
        out = {}
        for lam, P in self.P.items():
            a, w = P @ psi, P @ v
            out[lam] = 0.5 * w @ w + 0.5 * self.m ** 2 * lam * a @ a
        return out


def _slope(lna, logr, frac=0.5):
    k = int(len(lna) * (1 - frac))
    return np.polyfit(lna[k:], logr[k:], 1)[0]


def run():
    rep = Report("7-cosmology")
    C = gates.CONDITIONAL
    L, m = 10.0, 1.0
    psi0, v0 = carrier.canon_initial_datum()

    F2 = gravity.tuned_F2(1, 1, L, m, 0.0)
    G, Lcc = gravity.newton_and_vacuum(1, 1, F2, L, m)
    U = FLRW(G, Lcc, m)
    sol = U.evolve(psi0, v0, 300.0)
    res = max(abs(U.constraint(sol.y[:, i])) for i in range(sol.y.shape[1]))
    rep.add("Friedmann constraint preserved along the flow (tuned Lambda_cc = 0)", C,
            res < 1e-8, res)
    lna = sol.y[0]
    rs = [U.sector_rho(sol.y[:, i]) for i in range(sol.y.shape[1])]
    s0 = _slope(lna, np.log([r[0] for r in rs]))
    mass = np.array([r[3] + r[8] for r in rs])
    s_m = _slope(lna, np.log(mass))
    rep.add("kernel (massless) sector: rho ~ a^-6 (stiff)", C, abs(s0 + 6) < 0.05, s0)
    rep.add("massive sectors (3, 8): time-averaged rho ~ a^-3 (dust)", C,
            abs(s_m + 3) < 0.15, s_m)
    a_end = float(np.exp(lna[-1]))
    rep.add("expansion decelerates, a(t) ~ t^(2/3) at late times", C,
            abs(_slope(np.log(sol.t[1:]), lna[1:]) - 2 / 3) < 0.05,
            {"a_end": a_end, "p": _slope(np.log(sol.t[1:]), lna[1:])})

    G, Lcc = gravity.newton_and_vacuum(1, 1, 1, L, m)
    U = FLRW(G, Lcc, m)
    sol = U.evolve(psi0, v0, 30.0, n=600)
    Hds = np.sqrt(Lcc / 3)
    rep.add("natural cutoff f=e^-x: de Sitter at once, H -> sqrt(Lambda_cc/3)", C,
            abs(sol.y[1, -1] / Hds - 1) < 1e-3,
            {"H_end": float(sol.y[1, -1]), "H_dS": float(Hds)},
            note="the vacuum term 6 L^2 swamps the carrier: the usual "
                 "cosmological-constant problem, not a prediction")
    rep.add("IceCube/LHAASO scales, vacuum amplitude (27/5)^3 e^-280",
            gates.REMOVED, True)
    rep.add("any observed cosmological parameter (H0, Omega, w)", gates.UNFORMED, True,
            note="needs m, L, f and TIME_BIND; all external")
    return rep
