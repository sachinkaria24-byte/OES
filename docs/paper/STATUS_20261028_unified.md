# One Machine, the unified edition: 28 October 2026

This puts the whole model in one text with one ledger: the verified build (layers 1–18), the integrated spine (layer 19), the canon synchronization (layer 20), the sibling's 28 October ledger of joins (layer 21), and the sibling's evening notes with the canon's 19:10 continuation (layer 22). It is a selected mathematical build replayed from matrices. It is not a source admission and not a change to the canon matrices.

AUTH = NOT_PASS. ScientificGold = FALSE. TIME_BIND = UNBOUND. The six SCR6 operands stay absent. No gate moves, and no term is added to the action.

**Model:** GitHub `sachinkaria24-byte/OES`, branch `claude/lagrangian-spectral-spacetime-model-t2253b`.

- `python verify.py` runs 22 layers and 449 checks. Of these, 412 hold: THEOREM 291, OBSTRUCTION 41, ARITHMETIC 35, CONDITIONAL 17, UNFORMED 18, SELECTED_REFERENCE 8, REMOVED 2. The other 37 are REPORTED records.
- `pytest` runs 37 tests.
- The newest layers are `oes/ledger.py` (layer 21, 19 checks) and `oes/counts.py` (layer 22, 37 checks).
- `ports/ts/ledgerJoins.ts` carries it into the sibling's app. Together with `coxeterSpine.ts` that is 35 rows, residual 0.
- `data/clocks.json` holds the explicit clock matrices. `docs/LEDGER.md` lists every join with its status.

**Paper:** `one-machine-20261028-unified.pdf`, with its Markdown source in `docs/paper/`. It supersedes the verified and spine papers. On Drive (One Machine 20261028) the Google Doc `one-machine-20261028-unified` holds the 19:06 version, from before layer 22.

New in this edition:

- **The tick bit.** The tick 864 lies in ⟨x⟩ iff 5 does not divide x. The sibling's ledger has 129 tick sentences from 35 joins, and every one of them is this bit. Their step counts, indices and 38 stated subgroup orders also agree. The numbers that ride on the bit are counts, and no map joins them.
- **The tick is a commutator.** d c′ d⁻¹ c′⁻¹ = c′⁶ = r r′. The twist by 7 and the two-carrier tick are one fact.
- **The day–Coxeter group** (order 120) has centre ⟨c′⁵⟩ (the shared ⟨720⟩) and derived group the tick. It permutes its five day clocks as the affine group of the pentagon: the tick rotates them, the day doubles them (pentagon to pentagram), and the centre fixes them. This is the ledger's "twenty affine maps".
- **The golden clock.** v has order 20, twist 11 and v⁴ = the tick. ⟨216⟩ on the circle and B = [[1,1],[1,0]] mod 5 obey the same law. The affine 20 is not cyclic.
- **The mirror.** The circle's x ↦ −x is realized by involutions with twist −1. On the carrier they act as the pentagon reflection, which fixes three atoms. The fifteen-atom involution i ↦ 14 − i does not keep D².
- **Carrier exchange.** No involution exchanges the carrier A4 and its twin A4′. Every exchange has order 4, 8, 12 or 20 and doubles the index-5 glue. Every element that keeps both acts on the glue by ±1.
- **The order-24 element.** The sibling's build reports it as not constructed. It is given explicitly, with the golden clock and the mirror, in `data/clocks.json`.
- **Energy.** The checked datum has energy 34 = 20 + (3 + 9) + 2. E_V = 23 and E_E = 11 are conserved separately. Under canonical quantization the carrier cannot entangle vertices with edges (CONDITIONAL).
- **Spin counts.** 240 = D8 (112) + one half-spin orbit (128). 135 = [W(E8) : W(D8)] is the band-top D8 family, and 256 = 1 + 120 + 135.
- **Field.** The source q̈ + 4q = 0 is not a carrier mode, because 4 ∉ spec D² (OBSTRUCTION).

New in layer 22 (the sibling's 48 notes of 18:32–20:23, the canon's 19:10 continuation and the separate model's 19:47 status):

- **Counts.** 398 more readings on the tick bit, from 47 notes, all hold. Each is checked with its stated order, subgroup, steps or first landing.
- **Moments, replayed.** MOMENT_BIT's seven moments 1, 242, 58691, 14259954, 3470101592, 845582723240, 206295748792515 are the moments of the alternating hexagon port on the E8 lattice. They are computed exactly, and μ₇ = 50383499822338790 is new. The canon's square and octagon ports are replayed too, and square = (hexagon + octagon)/2 at every order.
- **Graphs.** K5, Petersen, pentagon and pentagram, and the root graph's closed walks 1, 0, 56, 1512, 62160 are rebuilt.
- **The Hurwitz value 6.** It belongs to S5 (genus 4). The stored order-120 clock has one involution and no (2, 4, 5) generating pair.
- **The commutator and 864.** Every one of the 24 maps from the clock to the circle kills the commutator. The tick reaches 864 only through the Coxeter clock alone.
- **Energy.** The three splits are one conserved table: vertex (0, 3, 20) and edge (2, 9, 0). Its columns are the stored 2 + 12 + 20.
- **The six-site chain.** MOMENT_CHAIN's blocks 241I − J, 183I + 52J and 35366I + 8134J are M₁, M₂ − M₁² and M₃ − 2M₁M₂ + M₁³ of the A5-simplex port. The canon had listed the last as unidentified.
- **Beats.** The separate model's squared beats 11 ± 4√6 are (2√2 ± √3)², the beats of the carrier's two oscillating sectors.
- **SEVEN_ONE, corrected.** Four mirror pairs, not three, are left unsplit by the bit: 1–13, 2–12, 3–11 and 6–8.
- **Petersen projectors.** The sibling's J/10, (4I + 2A − J)/6 and (5I − 5A + J)/15 are the carrier's edge projectors (sector 8, the five zero modes, sector 3), because MᵀM = J + I − A. The denominators 10, 6, 15 are the gap products 2·5, 2·3, 3·5. The Gram determinant 648 is det(3I + J), the carrier's vertex block.
- **Every breath.** 3 and 8 share no period because 8/3 is not a rational square; "not a multiple" is not the criterion.
- **The Pauli generator is the bath.** PAULI_178's L(M) = 240M + 16Mᵀ − 16 tr(M) I is the bath Laplacian on its 256 half-period modes. Eight antisymmetric Paulis anticommuting along the E8 diagram map Λ/2Λ onto the Paulis with L φ(x) = ε(πx) φ(x): 0, 224 (the E7+A1 saddles) and 256 (the D8 band top) on 1 + 120 + 135.
- **Mass and energy.** The "mass determinant" 216 is det(3W) for the source metric of layer 10; the datum's 2 is the kinetic energy of a dark 4-cycle.

Against the canon:

- **Position.** The Quick Access sheet 00_FULL_RECONCILIATION_20261028 (review cutoff 17:19:41) keeps OMSOON736 controlling. No Matrix ID is new, and the frozen gates stay. That sheet still lists this repository's 14:37 build (18 layers, 320 checks).
- **What the sibling adopted.** The sibling's CANON_READ (17:06) adopted the layer-20 corrections, and its 18:17 full edition keeps them. Its 19:05 ONE_BIT note adopts the commutator [d, c′] = c′⁶ of layer 21.
- **Continuation 3.** The canon sheet 00_CURRENT_20261028_1910 (review cutoff 19:10:16) records the 21-layer build as source-reported. It keeps OMSOON736 and every frozen gate.

Not formed: source infinity, foam, the double slit, entanglement as stored data, a Bell count, the photoelectric effect, a work function, electron, photon, proton, Compton and Bohr lengths, 19 Standard-Model parameters, the six SCR6 operands, the Krishna lift's operands, the epoch, GKSL, SI, BRST, BV and Einstein–Hilbert. Still open: the collar (223.58, 224) and the rational coefficients of the order-16 operator.
