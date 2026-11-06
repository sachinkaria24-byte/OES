# How to cross the gates

*6 Nov 2026. Layer 23 checks `gpr_poset`, `gpr_hashes`, `gpr_falsifiers`, `gpr_loaded_observability` and `gpr_designs`; the binding maps are in [`BINDING.md`](BINDING.md). This page is the result of a pattern search over the separate model's gate corpus on Google Drive (its contracts, intake forms, preflight receipts, mincuts and the vNext12 controlling court order of 6 Nov), read as data, reconciled with the model's own gate table and audited adversarially. Nothing on it is a physical claim.*

## 0. Standing

Every gate is shut, identically in `oes/gates.py` and in every Drive file: AUTH NOT_PASS, SCR6 NOT_RUN_OPERAND_ABSENT, BIND_Q31 UNBOUND, TIME_BIND UNBOUND, DYN_BIND NOT_INSTALLED, PredictionFreeze NOT_TRIGGERED, T3081 UNOPENED, P, W_E, W_L, E, I NOT_PASS, ScientificGold FALSE, the original evidence groups 0/19. The Drive holds no SI-traceable datum bound to the model: every number presented as a measurement is a synthetic fixture (a mock ρ = 4/3, a nominal 0.25 kg and 1 N/m marked "not metrology"), an empty template (holdout tables with no rows, contracts with every measured value null, a signature manifest with every hash null, freeze drafts that say they are not frozen), or a literature benchmark disclaimed as a prediction. No source names a single one of the 19 evidence groups.

Three rules hold throughout, in the model and in every Drive contract: no user-editable flag promotes a gate; missing is null, not a measured zero; a checksum or a draft is not a freeze.

## 1. What can and cannot be done by mathematics

Mathematics has done what it can: each gate is reduced to its minimal external input, the map from that input to the bound model is installed with the dimensionless invariants a realisation must pass first ([`BINDING.md`](BINDING.md)), the prepared owner transaction and the prediction register are written and hashed (`oes/gatework.py`), and the measurement design for the dynamics is a theorem (section 4 below). No gate is crossable by mathematics alone. The only partial exceptions are proof obligations inside a decision: the certificate half of the strict six-dimensional spectral branch, owed only if that branch is chosen, and the port-adapter question, which `oes/binding.py`'s B0 has already decided as an obstruction (no S5- or D5-equivariant adapter; C5 is maximal).

## 2. The gates as a poset

The nodes are the model's gate keys together with the Drive ledger's eighteen interfaces, placed in the separate model's controlling court order (C0 to C6). Each node has one input type and one supplier.

| court | node | input (type) | supplier | model key |
|---|---|---|---|---|
| C0 provenance | O0 owner | identity record + owner signature | the research owner | AUTH |
| C0 | P_WIT / BIND_TX | witness signature + binding-transaction receipt + anchored verifier keys | independent witness and verifier | AUTH |
| C1 source and action | physical child | decision: particle physics, engineered network or acoustic lane (MODEL §14) | owner | DYN_BIND, SCR6 |
| C1 | A_MASTER | literal action bytes + SHA-256 + port policy + matter branch | owner | — |
| C1 | root chart | adoption of the model's root chart (layer 24) or an owner-verified chart | owner | — |
| C1 | port order | the ten marked K5 edges with transducer positions | owner + laboratory | — |
| C1 | SCR6 operands | six files of shapes 2×2, 55×55, 169×69 (complex), 24×24 (skew), 31×7, 5×18, with hashes; the run criterion is UNFORMED in the model | owner | SCR6 |
| C1 | Q31 map | the 31-to-10 mapping bytes | owner | BIND_Q31 |
| C1 | dynamics choice | H_sel, generation multiplicity, chirality index, completion member θ | owner | DYN_BIND |
| C1 | spectral branch | decision; ten certificates owed only on the strict six-dimensional branch | owner, derivation | — |
| C1 | group names | the identities of the 19 original evidence groups | owner | — |
| C2 time | timebase | clock certificate, traceable seconds | metrology laboratory | TIME_BIND |
| C2 | clock datum | exactly one SI interval: T_half in s, Ξ in s⁻⁴ or s* in s⁻¹, on a preparation that first passes the ρ-free invariants | laboratory + owner's mode label | TIME_BIND |
| C3 dynamics pilot | SI chain | m (kg), k and δk (N/m), gains, phase, delay, covariance, each with nonzero uncertainty | laboratory | DYN_BIND |
| C3 | free, loaded, sham runs | ten-port responses at dyadic rates with one anchor; four loads on a spanning tree of K5 | laboratory | DYN_BIND |
| C4 observer | source-sensitive Q readout | an independent readout in separate custody; required only if source-family identities are claimed | laboratory | BIND_Q31 |
| C5 freeze | prediction freeze | owner signature + independent custodian seal, UTC-timestamped before any holdout, over the register bytes, the tolerances, the dyadic depth, the secant convention and the per-group predictions | owner + custodian | PredictionFreeze |
| C6 evidence | the 19 groups | raw data per named group, SI unit, uncertainty, independent control, per-group warrant | owner + 19 warrants | — |
| C6 | blind holdout | the sealed design run after the seal with custodian-randomised identifiers | laboratory + custodian | — |
| C6 | external warrant | an independent adjudicator's signed warrant over the freeze, the raw hashes, the uncertainties and the absence of retrospective fitting | adjudicator | P, W_E, E, I (assigned here by selection) |
| C6 | ScientificGold | a frozen prediction, independent data and a preregistered test on a declared physical system (MODEL §13) | independent review | ScientificGold, GoldDepth, G_OES |

Two leaves are in scope only for one child. W_L (the lepton likelihood) belongs to the particle-physics child; it is NOT_PASS by evidence and no external act reopens it, only a new lepton-sector candidate, which is a theory act. T3081 belongs to the acoustic lane; it needs the two official hosts and, because the maintainer hash the model holds is itself a reported value, a third copy to adjudicate any mismatch. The keys x_executed, R6/A40/A52 and numbered_baseline are states and labels, not gates.

TIME_BIND depends on the timebase and the signed port only. It does not depend on the kilogram-and-newton chain: time is one number ρ, and the SI second enters nowhere else. The chain is a dynamics input, for absolute units.

## 3. The minimal external acts, in order

Eleven acts, nine unconditional and two conditional (the Q readout and the host receipt), cross every node, each the sole crosser of at least one node. The order respects every dependency once two downward edges are allowed for: AUTH and the witness sit in court C0 but sign the manifest of C1, so they close after it (the act sequence runs through the courts as C1, C0, C1, C0, C2, C3, C4, C5, C6, C6). On the acoustic lane the host receipt precedes the warrant.

1. **Declare the physical child.** One decision. It fixes which leaves are in scope.
2. **Sign the prepared transaction as it stands.** The literal bytes of `data/owner_transaction.json` (SHA-256 73b32ebe…), which carry the hashes of the native operand file, the verifier and the walk table and the prediction register. This is the owner's identity act.
3. **The owner manifest.** A second signed document, whose bytes necessarily differ from the first: the action bytes and their hash, the port policy and matter branch, the root chart, the port order, the six SCR6 operand hashes, the Q31 map hash, H_sel with multiplicity, chirality and θ, the spectral-branch decision, and the names of the 19 groups.
4. **Witness and verifier.** The independent witness signs the record and the binding transaction over the same bytes; the verifier's keys are anchored independently. AUTH would pass here, not before.
5. **One clock datum.** A clock certificate and one SI interval on a preparation that first passes the invariants of [`BINDING.md`](BINDING.md): the exact ratio Ξ_mass/Ξ_q = 2117/389 and I₁ = 2117·u_half⁴ ∈ (0.07614507, 0.07614566) are the model's own; I₃ and I₂ rest on the crossover certificate read as data. Route (i) needs a pure mass preparation blind to the nineteen source ports; route (iii) needs the secant convention declared first. TIME_BIND would pass.
6. **The pilot.** The apparatus with its SI chain; free, loaded and sham ten-port responses at dyadic rates with one anchor G(z₀). The loads form a spanning tree of K5 (section 4). What the model predicts: the load identity G_L⁻¹ − G₀⁻¹ = (δ/ρ²)eeᵀ on the loaded edge only; d²/Ξ_q = δ²/389 for the declared load δ; the dyadic tail Σ(4ᴺz) ≤ BBᵀ/(4ᴺz); the 19-source tail constant D19 = 967P₈ + 389P₇ + 83P₄, trace 10791; the ranks of section 4. This is DYN_BIND's measurement half; with act 3's choice half, DYN_BIND would be installed. A five-load pentagon (any of K5's twelve five-cycles) survives one failed load and its frame is the best conditioned, with condition number the golden ratio (section 4).
7. **The Q readout** (only if source-family identities are claimed).
8. **The freeze.** The owner signs and an independent custodian seals, before any holdout, the register bytes (SHA-256 7b59e592…, 30 calibration-invariant entries in 5 kinds), the tolerances, the dyadic depth N from the declared noise budget, the secant convention, in the dimensionless form x = s/s*, and the per-group predictions. The register holds no per-group entry, so those predictions are a theory act that must precede this one.
9. **The 19 groups.** Raw data with hashes, SI units, uncertainties, independent controls and a warrant for each named group. 0/19 becomes 19/19 only group by group; each missing item is individually blocking.
10. **The blind holdout and the warrant.** The sealed design is run blind; the adjudicator signs the warrant; the Gold decision follows as independent review of a frozen prediction, independent data and a preregistered test.
11. **T3081** (acoustic lane only): allow the two hosts, fetch, compare bytes.

Counts (`gpr_poset`): 11 acts, 9 unconditional and 2 conditional; 7 signatures plus 19 per-group warrants; 8 owner decisions (child, port policy, branch, H_sel, multiplicity, chirality, θ, chart); exactly one measured scalar at the first act that carries a model check, the clock datum. Nothing in the Drive or the model supplies any of them.

## 4. The measurement design is a theorem

The separate model's vNext12 loaded-observability theorem is replayed exactly on the model's K5 (`gpr_loaded_observability`). With B the signed incidence, P₄ = BᵀB/5 the cut projector and P₆ = I − P₄ the cycle projector, a free response G₀ = g₆P₆ + g₄P₄ and an edge load κe_je_jᵀ obey the Woodbury identity G_j⁻¹ − G₀⁻¹ = κe_je_jᵀ exactly. A cycle reader with loads on an edge set S reads rank 11 − c(S), where c(S) counts the connected components of S on the five vertices. So four loads give full rank exactly when they form a spanning tree: 125 of the 210 four-edge sets (5 stars, 60 paths, 60 forks), every one with Gram determinant 1/125, and the five stars are the best conditioned, with Gram (I₄ + J₄)/5, inverse 5I₄ − J₄ and condition number √5. More than four loads are full rank exactly when the loaded graph is connected. The path tree's Gram is the A4 Cartan matrix over 5, with condition number √(5 + 2√5) = 3.0777, and the fork's is 2.8351; the three characteristic polynomials of the separate model's vNext13 note replay exactly (`gpr_designs`). Its five-load pentagon design also replays: K5 has twelve five-cycles, deleting any one edge of any of them leaves a spanning tree, and the frame Gram of a five-cycle is the pentagon Laplacian over 5, with nonzero eigenvalues (5 ∓ √5)/10 twice, five times the roots of the model's one quadratic x² − 5x + 5, so its condition number is the golden ratio exactly, below the star's √5. Three further exact statements of the Invariant × Dyadic × Port-Adapter master (6 Nov, 15:54) replay on the generic block: the band fingerprint 4z²e(z) → BBᵀ (so e(4z)/e(z) → 1/16 per band and the band ratios tend to 967/389 and 389/83), the noise optimum 4ᴺ = √(β/(z²ε)) for the dyadic depth, and the port-adapter no-go that compression does not commute with inversion, (UᵀGU)⁻¹ − UᵀG⁻¹U = −b²/(z + c), which is 11/4 against 3 on K = [[2, 1], [1, 3]] at z = 1.

## 5. What the sources disagree on, and what was corrected

The Drive counts the cut differently in every file (9 mincut rows, 6 blocking classes, 25 obligations, 18 interfaces, 35 null fields, 26 intake fields, 63 court items, and the Invariant master's five tasks: source/auth, adapter/types, one action, lab/time, claim/warrant, which are acts 2–4, 3, 1 and 3, 5–6, and 8–10 above); the poset above is one reading, marked as a selection. The separate model's first synthesis of this corpus put the kilogram chain under TIME_BIND, crossed SCR6 before AUTH, read ScientificGold as a conjunction with W_L and T3081, and quoted as model predictions several numbers the model does not hold (a leakage 127P₆ + 392P₄, a static gap of 8, the ratios 1/4, 7/4, 19/4, a 98/53 null count, a Bonferroni value); all of that was removed. The model's W_L row in MODEL §13 said that adding the reported θ₂₃ pull to the two-angle χ² gives 26.3; the code computes 26.3 from the three reported NuFIT pulls alone, and the two Bari pulls plus −4.8 would give 33.7. The row now says so.

## 6. What would change this page

A signature, a certificate, a raw trace or a named group would each turn one null into a record and move one node. Until then the gates stay shut, and this page is the complete list of what is missing.
