# One Machine, the spine verified: 28 October 2026

This rebuilds the integrated spine (`one-machine-20261028-integrated.pdf`, `oes-integrated-20261028.zip`) from matrices. It is a selected mathematical build. It is not a source admission and not a change to the canon matrices.

AUTH = NOT_PASS. ScientificGold = FALSE. TIME_BIND = UNBOUND. The six SCR6 operands stay absent. No gate moves, and no term is added to the action.

**Model:** GitHub `sachinkaria24-byte/OES`, branch `claude/lagrangian-spectral-spacetime-model-t2253b`.

- `python verify.py` runs 20 layers and 393 checks. Of these, 367 hold: THEOREM 256, OBSTRUCTION 39, ARITHMETIC 30, CONDITIONAL 16, UNFORMED 16, SELECTED_REFERENCE 8, REMOVED 2. The other 26 are REPORTED records.
- `pytest` runs 27 tests.
- The new layers are `oes/spine.py` (layer 19, 50 checks) and `oes/canon_sync.py` (layer 20, 22 checks: the canon as of 16:49 UTC). `ports/ts/coxeterSpine.ts` is a drop-in audit for the sibling's TypeScript model.

**Paper:** `one-machine-20261028-spine.pdf`, with its Markdown source in `docs/paper/`.

New over the integrated build, each computed from matrices or from the subgroup lattice:
- **One lemma for the circle.** Z/4320 has one subgroup per divisor, and containment, meets and joins are gcd and lcm. All 28 circle statements of the build are checked by it.
- **The spine's missing middle.** The Coxeter subgroup ⟨144⟩ lies between the order-10 subgroup and the atlas, so the tower is 36 × 4 × 3 × 2 × 5. There are 504 maximal chains, 6 of them through the whole spine. The Coxeter step is tick + sun + half-turn: 864 + 1440 + 2160 ≡ 144.
- **The Coxeter clock.** The E8 Coxeter element c has order 30 and characteristic polynomial Φ₃₀, and its exponents are the units mod 30. It permutes the roots in 8 orbits of 30, so it is a symmetry of the bath already in the model. Sending 144 to c is the selection.
- **Fixed momenta are Morse points.**
  - The tick fixes 25 Bloch momenta: the origin and 24 points of A4+A4.
  - The sun fixes 81: the origin and 80 points of E6+A2.
  - The half-turn fixes all 256 half-periods: the origin, E7+A1 and D8.
- **The tick turns two carriers.** A conjugate c′ has c′⁶ = r r′, where r is the K5 vertex rotation on the carrier's A4 and r′ the twin rotation on A4′. The sun turns four triangles (A2⁴), and the half-turn flips eight edges (A1⁸).
- **Where 7 enters.**
  - The day clock d (order 24, Φ₂₄) agrees with the Coxeter clock on ⟨720⟩ and satisfies d c′ d⁻¹ = c′⁷.
  - No order-24 element commutes with c′, and the atlas 180 − 144 = 36 cannot act.
- **What can act on the bath.** A subgroup of the circle acts on the bath lattice iff its order is one of 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30. The maximal clocks are 30, 24, 20 and 18. The moon, nakshatra, pada and atlas cannot act.

Corrections to the integrated build:
- **DOTS_LATTICE.** The pada–cycle meet ⟨120⟩ has order 36 (the moon). It is not the atlas ⟨36⟩, which has order 120.
- **SIDEREAL_DOTS.** The signs and ⟨432⟩ meet in {0, 2160}, so 2160 is the only *nonzero* element.
- **360000.** It is ≡ 1440 (mod 4320), so the W₀ scalar is the sun step.
- **"Their sum 5".** Siri + Shay = 8 (order 540); the 5 of order 864 is Prema + Sai.
- **Doubling residues.** Their orders in doubling order are 4320, 2160, 1080, 540, 4320, 864.
- **Positive roots.** 8 × 30 = 240 is all the roots; the positive roots are 120 = 8 × 30 / 2.
- **The tower.** 36 × 12 × 2 × 5 skips the Coxeter subgroup; the tower is 36 × 4 × 3 × 2 × 5.
- **Superseded.** "No stored map sends a yuga tick to a lattice vector or a Morse point", "None equals 30", and "The order-5 element of the 4320-circle is not this tick".

Against the latest canon (read 16:30 UTC, re-read 16:49):
- **Position.** OMSOON736 and the 10:04 Canon Check stay controlling. The Quick Access cutoff (14:59:48) predates this edition.
- **What the sibling adopted.** The current sibling build adopts 144 = 2160 + 1440 + 864 and the twist by 7. In W(E8) the day and Coxeter clocks generate a group of order 120, not the order-720 semidirect product.
- **Correction.** "The step 5 (or 25) generates the tick": ⟨5⟩ = ⟨25⟩ has order 864, while the tick has order 5.
- **16:31–16:43 notes, restated in the 16:47 consolidation (its paper's text equals the 16:43 one).** SPINE_CORRECTIONS adopts all six circle corrections. The COXETER_POWERS, ATLAS_FACTOR and SUN_MOON statements hold.
    - The fixed momenta they leave unreplayed are proved for every power: c<sup>k</sup> fixes Φₙ(1)^(8/φ(n)) points on the torus, n = 30/gcd(k, 30). That gives 25, 81 and 256 at orders 5, 3 and 2, and 1 otherwise.
    - "The circle makes the day and Coxeter clocks commute" holds on the circle only. In W(E8) the centralizer of c′ is ⟨c′⟩.
    - The 16:43 paper still says "360000 is not a step" in one theorem.
- **Proved.** The bath's maximal group speed is √30, as a supremum. The Canon Check's preparation identities are replayed, and its scalar bound follows from layer 14.
- **Rebuilt.** From the separate major-upgrade model: the observer completion, the 252-design sensor census (162 / 90 / 72 optimal), the flag geometry with vertex distance √(8/7), and the transfer functions.
- **Absorbed.** The contrast-plane harmonic quartic is 2|x|⁴ − 5Σx⁴; 3|x|⁴ − 7Σx⁴ is the ambient one.

Not formed: the Krishna lift's operands, the epoch, GKSL, SI, BRST, BV, Einstein–Hilbert, the six SCR6 operands, the rational coefficients of the order-16 operator, and the collar.
