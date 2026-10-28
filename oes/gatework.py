"""Layer 13. Executing the physical gates as far as mathematics can.

The canon distinguishes four transition types (S364 master lock):
  a new theorem head changes what is KNOWN;
  an authenticated root changes what can be EXECUTED;
  a binary receipt changes what can be COMPARED;
  an independent warrant changes what can be PROMOTED.
Each gate below is driven to the boundary of its own type.

TIME_BIND  (structure: THEOREM; binding: needs one clock datum, CTB9)
  * Countermodel A: calibrations tau and 2 tau give identical native records.
    So no internal datum can bind time.
  * Sufficiency: one measured frequency assigned to one native mode fixes tau
    uniquely, and then every other frequency is a prediction.
  * The canon's Salina and Prema naturality courts (23 Sep addendum, secs
    10-11) vanish identically for the carrier flow.

PredictionFreeze  (READY; trigger is the owner's act)
  The register of calibration-invariant numbers is written to
  data/prediction_register.json and hashed.

W_L  (EXECUTED on the canon's recorded physical candidate)
  The PMNS strict branch (sin^2 th12 = 1199/3759, sin^2 th13 = 27/1280), which
  the 22 Oct note calls "the frozen candidate" (frozen informally: the
  PredictionFreeze gate itself was never triggered), against the
  canon-recorded Bari Oct-2026 fit. Gaussian, uncorrelated.

T3081  (BLOCKED by the network policy for the official SOFA host; receipt
  method demonstrated on the native operand file)

AUTH / SCR6  (PREPARED; owner signature required)
  data/owner_transaction.json packages P_cl, SELECT_CERT, ROLE_BIND and G_role,
  the canon's minimal ingress antichain, with SHA-256 for every operand.
"""

import hashlib
import json
from math import erf, exp, sqrt
from pathlib import Path

import numpy as np

from . import carrier, gates, literal
from .record import Report

ROOT = Path(__file__).resolve().parent.parent
REGISTER = ROOT / "data" / "prediction_register.json"
TRANSACTION = ROOT / "data" / "owner_transaction.json"


# ------------------------------------------------------------------ TIME_BIND

class Calibration:
    """t = tau * u: the canon's readout law omega = omega_hat / tau (CTB3)."""

    def __init__(self, tau):
        self.tau = tau

    def frequency(self, omega_hat):
        return omega_hat / self.tau

    @staticmethod
    def from_datum(omega_hat, omega_measured):
        return Calibration(omega_hat / omega_measured)


def _flows(tau):
    from scipy.linalg import expm
    K = np.array(carrier.D2(), float)
    n = len(K)
    A_nat = np.block([[np.zeros((n, n)), np.eye(n)], [-K, np.zeros((n, n))]])
    A_phys = np.block([[np.zeros((n, n)), np.eye(n)], [-K / tau ** 2, np.zeros((n, n))]])
    S = np.diag(np.r_[np.ones(n), np.ones(n) / tau])      # positions fixed, velocities / tau
    return (lambda u: expm(u * A_nat)), (lambda t: expm(t * A_phys)), S


def salina_prema(tau=2.7):
    """max_u || S U_native(u) - U_phys(tau u) S ||  (canon 23 Sep, sec. 10)."""
    Un, Up, S = _flows(tau)
    return max(float(np.abs(S @ Un(u) - Up(tau * u) @ S).max()) for u in np.linspace(0, 5, 11))


def countermodel_A():
    """Two calibrations, identical native records, different physical frequencies."""
    psi0, v0 = carrier.canon_initial_datum()
    x0 = np.r_[psi0, v0]
    labels = np.linspace(0, 7, 15)
    rec, freq = {}, {}
    for tau in (1.0, 2.0):
        Un, Up, S = _flows(tau)
        rec[tau] = np.array([(Up(tau * u) @ (S @ x0))[:15] for u in labels])
        freq[tau] = np.sqrt(8.0) / tau
    return float(np.abs(rec[1.0] - rec[2.0]).max()), freq


# ------------------------------------------------------------ PredictionFreeze

def register():
    """Calibration-invariant numbers the current model fixes (no fit, no datum)."""
    r5 = sqrt(5)
    return {
        "carrier": {
            "spec_D2": {"0": 5, "3": 8, "8": 2},
            "frequency_ratio_8_over_3": sqrt(8 / 3),
            "zero_modes": 5, "witten_index": -5,
        },
        "native": {
            "source_frequency_native": 2,
            "port_to_source_frequency_ratio": 2,
            "band_edge_to_source_frequency_ratio": 8,
            "static_contrast_response": "1/240",
            "exterior_coupling_eigenvalues": [183, 495],
            "boundary_block_eigenvalues": {"contrast": 241, "uniform": 235},
            "port_metric_spectrum": ["2/5", "2", f"{5 - r5:.15f}", f"{5 + r5:.15f}"],
            "sharp_quartic": "40/9",
            "long_wave_speed_lattice_units": sqrt(30),
            "angular_charge_symmetry": "SO(2) on (a,b)",
        },
        "bath_geometry": {
            "band": [0, 256], "band_top_orbit": 135, "saddle_value": 224,
            "saddle_curvature_law": "15/16 d^2", "cone_quartic": "40/169",
            "walk_counts": "data/walks.json (W_0..W_60)",
        },
        "binding_constraints": {
            "diagonal_symmetries_of_D": 1, "dark_symmetry": "U(5)",
            "anomaly_free_completion": "5 + Lambda^2 5 (15 states)",
            "generations_per_carrier": 1,
        },
        "glue": {"E8_over_A4xA4p_index": 5, "glue_map": "x -> 2x (mod sign)",
                 "mixed_roots": 200},
    }


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


# ----------------------------------------------------------------------- W_L

DECHORATE_MAINTAINER_SHA256 = "c39bc27f42174f7dc7cf24e3145d8ac4c835e8f4460fefaa95b6f7502ae60794"
DECHORATE_MAINTAINER_MD5 = "6f7aa37d319ec8898e4547aec1acea08"

FROZEN_PMNS = {"sin2_th12": (1199, 3759), "sin2_th13": (27, 1280)}
BARI_2026_10 = {"sin2_th12": (0.3047, 0.0055), "sin2_th13": (0.02218, 0.00055)}
NUFIT6_PULLS_REPORTED = {"sin2_th12": 1.0, "sin2_th13": -1.5, "sin2_th23_strict": -4.8}


def chi2_sf(x, k):
    """Survival function of chi^2 with k = 2 or 3 degrees of freedom."""
    if k == 2:
        return exp(-x / 2)
    if k == 3:
        return 1 - erf(sqrt(x / 2)) + sqrt(2 * x / np.pi) * exp(-x / 2)
    raise ValueError(k)


def pmns_court():
    pulls = {}
    for k, (num, den) in FROZEN_PMNS.items():
        mu, sig = BARI_2026_10[k]
        pulls[k] = (num / den - mu) / sig
    chi2 = sum(p * p for p in pulls.values())
    p2 = chi2_sf(chi2, 2)
    chi2_3 = sum(v * v for v in NUFIT6_PULLS_REPORTED.values())
    return pulls, chi2, p2, chi2_3, chi2_sf(chi2_3, 3)


# --------------------------------------------------------------- AUTH / SCR6

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def transaction(register_sha):
    files = {p: sha(ROOT / p) for p in ("data/native_matrices_input.json", "data/walks.json",
                                        "verify.py")}
    return {
        "type": "SCR6 minimal ingress antichain {P_cl, SELECT_CERT, ROLE_BIND, G_role}",
        "status": "PREPARED_FOR_OWNER_SIGNATURE",
        "P_cl": {"native_operands": files["data/native_matrices_input.json"],
                 "carrier": "signless incidence of K5 (no free data)",
                 "bath": "E8 root lattice, Delta = 240 I - A",
                 "clique": "apex 0 and e_i - e_6, i = 1..5"},
        "SELECT_CERT": [
            "S5-invariant metric on P5 is unique up to scale (P5 irreducible)",
            "Hom_S5(Lambda^2 P5, L6) is one-dimensional (Schur); W_AS forced up to scale",
            "literal port = U . reference port, U in the C5 commutant (layer 10)",
            "E8 glue map A4*/A4 -> A4'*/A4' is x -> +-2x (layer 11)",
            "dark U(5) broken to SO(2)_pair by the port (layer 12)",
        ],
        "ROLE_BIND": {
            "source": "q = (a, b) in P5 + P5, P5 = ker D on edges (dark sector)",
            "port": "g = P_boundary WAS_native (a ^ b), metric W_p",
            "bath": "h on E8 off the clique",
            "observer": "D psi readout; hidden sector = P5 + P5",
            "time": "native parameter u; TIME_BIND needs one clock datum",
        },
        "G_role": {"verifier": files["verify.py"], "walks": files["data/walks.json"],
                   "prediction_register": register_sha},
        "not_supplied_here": ["owner signature (AUTH)", "physical child H_sel",
                              "six SCR6 physical operands H_D2, C55, F_phys, Omega24, Z7, "
                              "host_to_OES"],
    }


def run():
    rep = Report("13-gates")
    T = gates.THEOREM
    diff, freq = countermodel_A()
    rep.add("TIME_BIND Countermodel A: tau = 1 and tau = 2 give identical records at native "
            "labels but physical frequencies in ratio 2:1", T,
            diff < 1e-9 and np.isclose(freq[1.0] / freq[2.0], 2), {"record_difference": diff},
            note="no internal datum can bind time (canon 27 Oct, replayed on the carrier)")
    c = Calibration.from_datum(2.0, 1.0e3)
    ratio_invariant = np.isclose(c.frequency(16) / c.frequency(2), 8) and \
        np.isclose(Calibration(5.0).frequency(16) / Calibration(5.0).frequency(2), 8)
    rep.add("TIME_BIND sufficiency: one datum fixes tau uniquely; frequency ratios are "
            "calibration-invariant", T, ratio_invariant and np.isclose(c.tau, 2e-3))
    sp_res = salina_prema()
    rep.add("Salina square S U_native(u) = U_phys(tau u) S holds for the calibrated carrier "
            "flow (Prema follows)", T, sp_res < 1e-9, sp_res)
    rep.add("TIME_BIND gate: structure complete; binding needs ONE authenticated clock "
            "datum and the owner's choice of which native mode it labels",
            gates.CONDITIONAL, True, note="CTB9: unbound only for lack of metrology")

    reg = register()
    REGISTER.parent.mkdir(exist_ok=True)
    REGISTER.write_bytes(canonical_bytes(reg))
    reg_sha = hashlib.sha256(canonical_bytes(reg)).hexdigest()
    rep.add("PredictionFreeze register written (calibration-invariant, no fit)", T,
            REGISTER.exists(), reg_sha,
            note="READY_TO_TRIGGER: freezing is the owner's act; nothing is compared yet")

    pulls, chi2, p2, chi2_3, p3 = pmns_court()
    rep.add("W_L executed: recorded PMNS strict branch vs Bari Oct-2026 "
            "(sin^2 th12, sin^2 th13)", gates.ARITHMETIC,
            abs(pulls["sin2_th12"] - 2.59) < 0.01 and abs(pulls["sin2_th13"] + 1.98) < 0.01,
            {"pulls": pulls, "chi2": chi2, "dof": 2, "p": p2},
            note="reproduces the canon's +2.59, -1.98 sigma; p = 0.005: disfavoured at 2.8 sigma")
    rep.add("W_L with the reported NuFIT 6.0 pulls incl. strict th23 (-4.8 sigma): excluded",
            gates.REPORTED, True, {"chi2": chi2_3, "dof": 3, "p": p3},
            note="the canon's recorded physical candidate fails; 28 Oct already removed "
                 "PMNS from the carrier")
    rep.add("T3081 dEchorate cross-host identity: official SOFA host blocked by network "
            "policy (HTTP 403 at the proxy)", gates.UNFORMED, True,
            note="maintainer copy 10E4VCAA1UoIVG-xVJLD9ByxsK2HAHgwl, SHA c39bc27f...; "
                 "allow sofacoustics.org / zenodo.org to run it")
    rep.add("T3081 maintainer side replayed on a second host (28 Oct, via the Drive "
            "connector): SHA-256 c39bc27f..., MD5 6f7aa37d..., 1,724,358 bytes - identical "
            "to the FinalRun 15 Aug receipt", gates.REPORTED, True,
            {"sha256": DECHORATE_MAINTAINER_SHA256, "md5": DECHORATE_MAINTAINER_MD5},
            note="third-party file, not stored in the repo; the official-host side stays open")
    rep.add("cross-host byte receipt method demonstrated: native operand file hash equals "
            "the canon-recorded hash", T, literal.sha256() == literal.SHA256)
    tx = transaction(reg_sha)
    TRANSACTION.write_text(json.dumps(tx, indent=1))
    rep.add("AUTH/SCR6 owner transaction prepared (P_cl, SELECT_CERT, ROLE_BIND, G_role)",
            gates.CONDITIONAL, TRANSACTION.exists(), tx["status"],
            note="AUTH is the research owner's signature, not a computation")
    rep.add("ScientificGold: needs an independent warrant (frozen prediction + independent "
            "data + preregistered test on a declared physical system)", gates.UNFORMED, True)
    return rep
