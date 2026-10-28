# OES end-to-end model

This repository holds a checked mathematical model of the OES canon at the OMSOON736 cut (28 Oct 2026). It covers the carrier Lagrangian, the spectral triple, spacetime and topology, the native E8-bath action, observers, gravity and cosmology. The full write-up, with a status on every statement, is in [`docs/MODEL.md`](docs/MODEL.md).

**AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND.** A passing check is a statement about constructed matrices. It is not a physical result, and no gate moves.

```
pip install -r requirements.txt
python verify.py          # all layers, ~90 s, writes results.json
python verify.py --fast   # skips the nonlinear E8-bath flow
python -m pytest -q
```

| layer | module | content | status mix |
|---|---|---|---|
| 1 carrier | `oes/carrier.py` | K5 selection, D, spec {0⁵,3⁸,8²}, S = ∫½ψ̇² − ½ψD²ψ, exact motion, Petersen/Hodge/tick | THEOREM |
| 2 spectral | `oes/spectral.py` | heat trace, ζ_D, spectral dimension, moments 15/40/200 | THEOREM |
| 3 spacetime | `oes/spacetime.py` | RP² pair, RP²×S¹, clock 125→120, E8 roots/walks/symbol/Green, clique coupling | THEOREM, OBSTRUCTION |
| 4 native | `oes/native.py` | source–port–bath action, W_AS, W_p, 40/9 quartic, radiation channel, nonlinear flow | THEOREM, SELECTED_REFERENCE |
| 5 observer | `oes/observer.py` | Kalman/Gramian readouts, Witten index −5, hidden sector | THEOREM |
| 6 gravity | `oes/gravity.py` | LLY curvature; M⁴×F spectral action → G, Λ_cc | ARITHMETIC, CONDITIONAL |
| 7 cosmology | `oes/cosmology.py` | FLRW with the carrier field: stiff a⁻⁶ + dust a⁻³ sectors | CONDITIONAL |
| 8 frontier | `oes/frontier.py` | band-edge orbit 135, 224-saddle expansion (40/169), Agni–Soma; sibling closures recorded | THEOREM, REPORTED |
| 9 joins | `oes/joins.py` | J1–J10: the maps that make the layers one object, plus shared integers kept apart | THEOREM, ARITHMETIC |
| 10 literal | `oes/literal.py` | the recovered native operand file (SHA 73e07429…), every canon identity replayed, the native flow on the owner's operands | THEOREM |
| 11 glue | `oes/glue.py` | the E8 glue maps: D8 + s, and A4 ⊕ A4′ with x ↦ ±2x; the carrier as the A4 shadow of the mixed roots | THEOREM |
| 12 binding | `oes/binding.py` | DYN_BIND constraints: no diagonal gauge charge, dark U(5), anomaly-free 5 + 10 completion | THEOREM, OBSTRUCTION, CONDITIONAL |
| 13 gates | `oes/gatework.py` | TIME_BIND courts, PredictionFreeze register, W_L on the frozen PMNS candidate, the T3081 and AUTH/SCR6 packages | THEOREM, CONDITIONAL, UNFORMED |
| 14 recurrence | `oes/recurrence.py` | canon W₀…W₅₅ replayed, new terms to W₆₀ (W₉₀ in progress), recurrence exclusion frontier | THEOREM |

Part II of `docs/MODEL.md` is the path from the mathematics to the operands and the physical gates.

Two constructions are not the canon's originals:

- **SELECTED_REFERENCE.** Layer 4 rebuilds the native port from its stated definition. Layer 10 now runs on the recovered literal operands, and shows the two differ only by a C5-commutant element.
- **CONDITIONAL.** The gravity and cosmology layers need an external 4-manifold, a cutoff function and a mass scale. The canon does not supply them, and the results show they are not identified.
