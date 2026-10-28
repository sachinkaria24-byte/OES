# OES end-to-end model

This repository holds a checked mathematical model of the OES canon at the OMSOON736 cut (28 Oct 2026). It covers the carrier Lagrangian, the spectral triple, spacetime and topology, the native E8-bath action, observers, gravity and cosmology. The full write-up, with a status on every statement, is in [`docs/MODEL.md`](docs/MODEL.md).

**AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND.** A passing check is a statement about constructed matrices. It is not a physical result, and no gate moves.

```
pip install -r requirements.txt
python verify.py          # 119 checks, ~90 s, writes results.json
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

Two constructions are not the canon's originals:

- **SELECTED_REFERENCE.** The native port is rebuilt from its stated definition, because the saved native source matrices are absent.
- **CONDITIONAL.** The gravity and cosmology layers need an external 4-manifold, a cutoff function and a mass scale. The canon does not supply them, and the results show they are not identified.
