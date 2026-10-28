# OES end-to-end model

This repository holds a checked mathematical model of the OES canon at the OMSOON736 cut (28 Oct 2026). It covers the carrier Lagrangian, the spectral triple, spacetime and topology, the native E8-bath action, observers, gravity and cosmology. The full write-up, with a status on every statement, is in [`docs/MODEL.md`](docs/MODEL.md).

**AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND.** A passing check is a statement about constructed matrices. It is not a physical result, and no gate moves.

```
pip install -r requirements.txt
python verify.py          # all 22 layers, ~4 min, writes results.json
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
| 14 recurrence | `oes/recurrence.py`, `oes/walkfast.py`, `oes/ore.py` | canon W₀…W₅₅ replayed; exact W₉₀; a second engine (D8 + spinor) to W₆₀₀ mod primes; the W_n recurrence formed mod four primes: order 16, degree 58, 16 exact growth rates (11 in the band) | THEOREM, UNFORMED |
| 15 court | `oes/court.py` | Court U19.81 audited claim by claim: script errors, true-moment envelopes, MDS code, clock-symmetry obstruction, cofactor 68 | THEOREM, OBSTRUCTION, UNFORMED, REPORTED |
| 16 handover | `oes/handover.py` | the 28 Oct Locked Memory handover audited: alcove critical census (11 families, 243,600 points, Morse sum 0 = the recurrence's in-band roots), the literal 5-dim operand T₆\|V_c (det 31), corrections in `docs/HANDOVER_ADDENDUM.md` | THEOREM, OBSTRUCTION, ARITHMETIC, UNFORMED, REPORTED |
| 17 waves | `oes/waves.py` | sound, light, frequency and phase on the K5 edges: Hodge split sound (4) + light (6) with d0d0ᵀ + Curl² = 5I, the canon's Hodge block A = −curl, helicities = the icosahedral 3 and 3′ locked to C5 phases, conversion selection rules, port frequency doubling, bath sound speed² 30 = 5 + 25 | THEOREM, CONDITIONAL, ARITHMETIC |
| 18 snapshot | `oes/snapshot.py` | the 14:16 Drive snapshot rebuilt from matrices: density of the nine bath frequencies on T⁹ (Besicovitch), all eleven Hessians and coherent coefficients, walk asymptotics 1 − 2/n + (23/15)/n², Agni = Curl², the five-port Hankel, the cube, Spanda (rank-19 correction), the 4320-circle | THEOREM, SELECTED_REFERENCE, ARITHMETIC, OBSTRUCTION |
| 19 spine | `oes/spine.py` | the integrated spine rebuilt: every 4320-circle statement checked by one lemma (six corrected), the tower refined through the Coxeter subgroup (36 × 4 × 3 × 2 × 5), the E8 Coxeter clock (Φ₃₀, exponents = units mod 30) acting on the bath, its tick = two K5 carriers (c′⁶ = rr′), fixed momenta 25/81/256 = the A4+A4, E6+A2, E7+A1 + D8 Morse points, the day turning the Coxeter clock by the exponent 7, and which parts of the circle can act on the bath at all | THEOREM, OBSTRUCTION, SELECTED_REFERENCE, ARITHMETIC |
| 20 canon | `oes/canon_sync.py` | the latest canon read and reconciled (16:30 UTC, re-read 16:49): the contrast-plane harmonic correction, the bath's maximal group speed √30 proved, the Canon Check's preparation identities and scalar bound, the sibling's circle notes (two duality errors corrected), the day–Coxeter group of order 120, the separate model's observer, sensor census, flag geometry and transfer functions rebuilt, and the 16:31–16:43 notes: Coxeter powers with their fixed momenta Φₙ(1)^(8/φ(n)), the atlas factor, sun and moon, and why the two clocks cannot commute on the bath | THEOREM, OBSTRUCTION, CONDITIONAL, ARITHMETIC, REPORTED |
| 21 ledger | `oes/ledger.py` | the sibling's 28 Oct ledger unified (canon re-read 18:20 UTC): every tick join is one bit (864 ∈ ⟨x⟩ iff 5 ∤ x; 129 sentences from 35 joins checked), the tick is the commutator of the day and Coxeter clocks (d c′ d⁻¹ c′⁻¹ = c′⁶ = r r′), the day–Coxeter group (order 120) permutes its five day clocks as the affine group of the pentagon (tick = rotation, day = doubling), the golden clock (v⁴ = tick), the mirror (the pentagon reflection on the carrier), no involution exchanges the carrier and its twin (every exchange doubles the glue), the energy's four conserved pieces, 240 = D8 + half-spin, and the explicit clock matrices in `data/clocks.json` | THEOREM, ARITHMETIC, OBSTRUCTION, CONDITIONAL, UNFORMED, REPORTED |
| 22 counts | `oes/counts.py` | the sibling's 18:32–20:23 notes, canon continuation 3 (19:10 UTC) and the separate model's 19:47 status replayed: 398 integer readings on the tick bit with their orders, subgroups and first landings; K5 (signless kernel = the zero modes of D², cycle-Gram determinant 125), Petersen, pentagon and pentagram; the root graph's closed walks 1, 0, 56, 1512, 62160; MOMENT_BIT's seven moments replayed exactly as the alternating hexagon port on the E8 lattice (μ₇ new) and square = (hexagon + octagon)/2 at every order; the order-120 clock has no (2,4,5) generating pair (the Hurwitz value 6 belongs to S5); every map from the clock to the circle kills the commutator; the three energy splits are one conserved table; the six-site moment chain 241I − J, 183I + 52J, 35366I + 8134J identified as block Stieltjes data of the A5-simplex port; the beats 11 ± 4√6 = (2√2 ± √3)²; four mirror pairs, not three, unsplit by the bit; the Petersen projectors (denominators 10, 6, 15) are the carrier's edge projectors, because MᵀM = J + I − A; the Pauli generator L(M) = 240M + 16Mᵀ − 16 tr(M) I is the bath Laplacian on its 256 half-period modes (0, 224, 256 on 1 + 120 + 135) | THEOREM, OBSTRUCTION, ARITHMETIC, UNFORMED, REPORTED |

Part II of `docs/MODEL.md` is the path from the mathematics to the operands and the physical gates.

Papers are in `docs/paper/`:

- **`one-machine-20261028-unified.pdf` is the current paper.** It covers all 22 layers with one ledger.
- `one-machine-20261028-verified.pdf` (layers 1–18) and `one-machine-20261028-spine.pdf` (layers 19–20) are kept as history.

[`docs/LEDGER.md`](docs/LEDGER.md) lists every join of both builds, including the sibling's evening notes, with its status and the layer that checks it. `data/clocks.json` holds the explicit clock matrices (the Coxeter clock, the tick, the day, the golden clock and the mirror) as elements of W(E8).

`ports/ts/` holds two drop-in TypeScript audits for the sibling model: `coxeterSpine.ts` (layer 19) and `ledgerJoins.ts` (layer 21). See `ports/ts/README.md`.

Two constructions are not the canon's originals:

- **SELECTED_REFERENCE.** Layer 4 rebuilds the native port from its stated definition. Layer 10 now runs on the recovered literal operands, and shows the two differ only by a C5-commutant element.
- **CONDITIONAL.** The gravity and cosmology layers need an external 4-manifold, a cutoff function and a mass scale. The canon does not supply them, and the results show they are not identified.
