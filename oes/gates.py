"""Status vocabulary and the standing gate ledger of the OES canon.

Every result in this package carries one status. The first five are the
canon's own words (One Machine, 28 Oct 2026 edition of OMSOON736, section 3).
The last two are added here and are never promoted by any check.

THEOREM            a finite check on constructed matrices returns zero, or an
                   identity of polynomials / dimensions derived from one.
ARITHMETIC         a count whose parent bases are not matrices in this package.
OBSTRUCTION        a proved impossibility.
REMOVED            a constant or postulate that is not a count, rank or trace
                   of D. Listed, never set to zero as a fit.
UNFORMED           a named historical operator with no equation here.
SELECTED_REFERENCE a construction made here from the canon's stated
                   definitions where the saved original operand is absent.
                   Its free choices are stated. It is not the original.
CONDITIONAL        mathematics that needs an input the canon marks external or
                   absent (a 4-manifold, a cutoff function, a mass scale).
                   It never feeds back into the carrier Lagrangian.
"""

THEOREM = "THEOREM"
ARITHMETIC = "ARITHMETIC"
OBSTRUCTION = "OBSTRUCTION"
REMOVED = "REMOVED"
UNFORMED = "UNFORMED"
SELECTED_REFERENCE = "SELECTED_REFERENCE"
CONDITIONAL = "CONDITIONAL"

STATUSES = (THEOREM, ARITHMETIC, OBSTRUCTION, REMOVED, UNFORMED,
            SELECTED_REFERENCE, CONDITIONAL)

# Read from LOCKED_MEMORY_OES_CONSOLIDATED_20261028.txt and the 28 Oct
# One Machine edition. Nothing in this package changes any of these.
GATES = {
    "AUTH": "NOT_PASS",
    "ScientificGold": "FALSE",
    "GoldDepth": 0,
    "G_OES": "FALSE",
    "SCR6": "NOT_RUN_OPERAND_ABSENT",
    "TIME_BIND": "UNBOUND",
    "DYN_BIND": "NOT_INSTALLED",
    "BIND_Q31": "UNBOUND",
    "PredictionFreeze": "NOT_TRIGGERED",
    "P": "NOT_PASS", "W_E": "NOT_PASS", "W_L": "NOT_PASS",
    "E": "NOT_PASS", "I": "NOT_PASS",
    "T3081": "UNOPENED",
    "x_executed": "000000",
    "R6/A40/A52": "FROZEN",
    "numbered_baseline": "OMSOON736",
}

# Section 13 of the 28 Oct edition, plus the 28 Oct side notes.
REMOVED_CONSTANTS = [
    "quarter defect 9/40 and every angle built from it",
    "CKM, PMNS, Jarlskog invariant, mass exponents (no Yukawa block of D)",
    "hypercharge shell SU(3)xSU(2)xU(1)",
    "printed potential A(1)",
    "cortex scales / complex Ginzburg-Landau constants",
    "portal, spring, detuning, second clock",
    "IceCube and LHAASO scales (no GeV in the spectrum)",
    "SO(2) by subtracting 3 from 5 (no continuum dimension theorem)",
    "imported noncommutative dimensions (Hilbert dimension is 15)",
    "vacuum amplitude (27/5)^3 e^-280 as a prediction",
    "alpha = 1/137 (Legendre symbol (5/137) = -1)",
]

UNFORMED_OPERANDS = [
    "six SCR6 operands", "original 31 seam rows", "502-dim Hodge-Dirac",
    "237-dim fiber observer", "historical MPKG adapter", "E8 glue map",
    "lattice sequence c60", "native 4944-dim transition / 5048-dim pullback",
    "ports R1, 025, 250, Jfix, Sawan, Hemkuver", "historical Agni/Soma/Suraj",
    "Sakshin operator (original)", "I6L", "Wald coefficient",
    "physical 1401-dim sector with calibrated time",
    "saved native_source_matrices (SHA256 73e07429...)",
    "literal conflicting 5x5 determinant operand (155 vs 4805)",
]


def ledger():
    """The gate ledger as a plain dict, for results.json."""
    return {"gates": dict(GATES), "removed": list(REMOVED_CONSTANTS),
            "unformed": list(UNFORMED_OPERANDS)}
