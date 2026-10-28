# One Machine: the spine, verified

**OES end-to-end model, integrated edition of 28 October 2026.** This rebuilds the sibling's integrated spine (`one-machine-20261028-integrated.pdf`, `oes-integrated-20261028.zip`, `INTEGRATED_20261028.md`) from matrices. It is a selected mathematical build. It is not a source admission and not a change to the canon matrices.

**AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND · DYN_BIND = NOT_INSTALLED · SCR6 = NOT_RUN_OPERAND_ABSENT · PredictionFreeze = NOT_TRIGGERED.** No gate moves, and no term is added to the action.

**Custody.**

- Repository `sachinkaria24-byte/OES`, branch `claude/lagrangian-spectral-spacetime-model-t2253b`.
- `python verify.py` replays all 20 layers in **393 checks**. Of these, 367 hold: THEOREM 256, OBSTRUCTION 39, ARITHMETIC 30, CONDITIONAL 16, UNFORMED 16, SELECTED_REFERENCE 8, REMOVED 2. The other 26 are REPORTED records.
- This edition is layer 19, `oes/spine.py` (50 checks, about 3 seconds). Layer 20, `oes/canon_sync.py` (22 checks), reconciles it with the canon as of 16:49 UTC (§12).
- `python -m pytest` runs 27 tests.
- `ports/ts/coxeterSpine.ts` ports the new checks to the sibling model's TypeScript as a drop-in audit (19 rows, residual 0).
- The earlier verified paper (`one-machine-20261028-verified.pdf`) covers layers 1–18. Section 1 recalls only what is needed here.

## Abstract

The integrated build puts the readings of the 4320-circle on one spine: "The Coxeter number 30 cuts 4320 into 144. Six of those steps make 864. Five of those close the circle." It checks this with integer comparisons, and its paper states that no stored map sends a yuga tick to a lattice vector or to a Morse point. Here the 30 is made into an operator.

The E8 Coxeter element c has order 30 and characteristic polynomial Φ₃₀. It permutes the 240 roots in eight orbits of thirty, so it is a symmetry of the bath that is already in the model. Sending the step 144 to c lets the first three stages of the spine act on the bath. The tick 864 then acts as **two K5 carrier rotations at once**, and it fixes exactly 25 Bloch momenta: the origin and 24 points of the A4+A4 critical family. The sun 1440 fixes 81 momenta and the half-turn 2160 fixes 256, and every one of these is a Morse point of the band.

The stops become theorems:

- The spine can act on the bath only up to the Coxeter subgroup. A subgroup of the circle acts on the bath lattice exactly when its order is one of 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, so the atlas, moon, nakshatra and pada cannot.
- The 7 at which the path stops is the E8 exponent through which the day clock acts on the Coxeter clock: d c d⁻¹ = c⁷.

Every circle statement of the integrated build is checked by a single lemma, and six are corrected.

## 0. What this edition changes

1. **One lemma replaces the circle "theorems."** The integrated paper states several dozen facts about Z/4320 one at a time. They are all instances of Lemma 1 (§2). The 28 statements of the build are checked against it, and six are corrected (§10).
2. **The spine gets its missing middle.** The tower 36 × 12 × 2 × 5 skips the subgroup the spine starts from. Through the Coxeter subgroup it is 36 × 4 × 3 × 2 × 5 (§3).
3. **The Coxeter number becomes the Coxeter element.** The model now has an explicit order-30 symmetry of the bath (§4), a computed set of Morse points it fixes (§5), and the tick written as two carrier rotations (§6).
4. **The stops become theorems.** What can act on the bath at all is classified (§8), and the 7 is located (§7).
5. **The checks can fail.** In the integrated model the Krishna stop is `4 + 5 !== 4` and the Prema stop is `2 !== 13`. Here every check is a computation on constructed matrices or on the subgroup lattice. A drop-in TypeScript audit carries the same checks into the sibling model (`ports/ts/`).
6. **The latest canon is read first.** Layer 20 reads the canon at 16:30 and again at 16:49 UTC. It takes one correction into this model, the contrast-plane harmonic quartic. It proves the canon's maximal group speed √30, and shows that the sibling's newest notes adopt §10. It then supplies what those notes leave unreplayed: the fixed momenta of every Coxeter power, and why the day and Coxeter clocks cannot commute on the bath (§12).

## 1. The datum, recalled

- **Carrier.** The carrier has 15 atoms, the 5 vertices and 10 edges of K5. D = [[0, M], [Mᵀ, 0]] with M the signless incidence. spec D² = {0⁵, 3⁸, 8²}, and the Lagrangian is S = ∫ ½|ψ̇|² − ½⟨ψ, D²ψ⟩.
- **Bath.** The bath is the E8 root lattice with walk operator A = Σ<sub>α</sub> T<sub>α</sub> over the 240 roots, Δ = 240 − A. Its band is ε(θ) = 240 − λ(θ), where λ(θ) = Σ<sub>α</sub> cos(α·θ) on the Brillouin torus R⁸/2πE8, and the band is [0, 256].
- **Coordinates.** E8 = D8 ∪ (D8 + ½𝟏). The roots are ±eᵢ ± eⱼ and ½(±1, …, ±1) with an even number of minus signs. The Bourbaki simple roots are α₁ = ½(1, −1, …, −1, 1), α₂ = e₁ + e₂, and αₖ = eₖ₋₁ − eₖ₋₂ for k = 3, …, 8.
- **Glue.** The carrier's own root system A4 = {eᵢ − eⱼ : i, j ≤ 5} (the 20 oriented K5 edges) sits in E8. Its orthogonal complement is a twin A4′, and [E8 : A4 ⊕ A4′] = 5 (layer 11).
- **Critical census** (layer 16). λ has eleven families of critical points, 243,600 points in all, with Morse sum 0. They are the eleven in-band roots of the order-16 walk recurrence (layer 14).

| family | ε | points | Morse index | torsion order |
|---|---|---|---|---|
| E8 | 0 | 1 | 0 | 1 |
| E7+A1 | 224 | 120 | 1 | 2 |
| E6+A2 | 243 | 2,240 | 2 | 3 |
| D5+A3 | 248 | 15,120 | 3 | 4 |
| A4+A4 | 250 | 48,384 | 4 | 5 |
| A5+A2+A1 | 251 | 80,640 | 5 | 6 |
| A6+A1 (edge) | 251.5625 | 69,120 | 6 | — |
| A7 (edge) | 251.85… | 17,280 | 7 | — |
| A7+A1 | 252 | 8,640 | 7 | 4 |
| A8 | 252 | 1,920 | 8 | 3 |
| D8 | 256 | 135 | 8 | 2 |

## 2. The circle in one lemma

**Lemma 1 (THEOREM).** For every divisor d of 4320 = 2⁵·3³·5, Z/4320 has exactly one subgroup of order 4320/d, namely ⟨d⟩, and these 48 are all its subgroups. For any steps a and b:

- the order of a is 4320/gcd(a, 4320);
- ⟨b⟩ ⊆ ⟨a⟩ iff gcd(a, 4320) divides gcd(b, 4320);
- ⟨a⟩ ∩ ⟨b⟩ = ⟨lcm(gcd(a, 4320), gcd(b, 4320))⟩;
- ⟨a⟩ + ⟨b⟩ = ⟨gcd(a, b, 4320)⟩.

*Proof.* A subgroup of a cyclic group is cyclic and is generated by the gcd of its elements with the modulus. Every assertion follows. ∎

So the subgroup lattice of the circle is the divisor lattice of 4320, a product of chains of lengths 5, 3 and 1. Every statement of the form "has order", "sits inside", "meets at" or "generates" is a gcd or lcm computation.

**Step and order are dual.** The step d generates a subgroup of order 4320/d. The atlas is the *step* 36, whose subgroup ⟨36⟩ has order 120. The moon is the step 120, whose subgroup ⟨120⟩ has order 36. Confusing the two is the most common error in the integrated notes (§10, item 1).

**Readings.** Sun, moon, day, signs, nakshatra, pada, atlas, tick, the yuga segments, and the role widths (Prema 2, Sai 3, Siri 4, …) are names for steps. Appendix A lists all 29 that the build uses. The name is a SELECTED_REFERENCE; every check uses the step.

**Check.** The 28 circle statements of the integrated build hold under Lemma 1. They come from INTEGRATED, ALL_4320, SIDEREAL_DOTS, SEGMENT_NAMES, YUGA_LATTICE, DOTS_LATTICE, ALL_DOTS and the paper. Examples:

- the order-10 subgroup is the ten multiples of 432 and contains the tick;
- ⟨360⟩ ∩ ⟨160⟩ = ⟨1440⟩, the sun;
- ⟨432⟩ ∩ ⟨360⟩ = {0, 2160};
- the pada and the tick generate the coil ⟨8⟩ of order 540.

## 3. The spine

**Theorem 2 (THEOREM).** The spine of the integrated build is the chain

0 ⊂ ⟨864⟩ (tick, order 5) ⊂ ⟨432⟩ (yuga, order 10) ⊂ ⟨144⟩ (Coxeter, order 30) ⊂ ⟨36⟩ (atlas, order 120) ⊂ Z/4320,

with indices 5, 2, 3, 4, 36. So every element has a unique address

x = d₀ + 36 d₁ + 144 d₂ + 432 d₃ + 864 d₄,  with d₀ < 36, d₁ < 4, d₂ < 3, d₃ < 2, d₄ < 5.

This was checked on all 4320 elements. The integrated tower 36 × 12 × 2 × 5 merges the two middle factors: 12 = [atlas : order-10] = 4 × 3, through the Coxeter subgroup the spine starts from.

**Proposition 3 (THEOREM).** The circle has 504 = 9!/(5!·3!·1!) maximal chains of subgroups (complete spines). Exactly 6 of them contain the whole named spine; they differ only above the atlas, where 36 = 2²·3² can be climbed in 6 orders.

**Proposition 4 (THEOREM).** The Coxeter step is the sum of the three named prime-order steps:

864 + 1440 + 2160 ≡ 144 (mod 4320),  i.e. tick + sun + half-turn = Coxeter step.

This is the Chinese remainder splitting Z/30 = Z/5 × Z/3 × Z/2. Section 6 shows that the same splitting holds for the operators.

**Proposition 5 (OBSTRUCTION).** The pada ⟨40⟩ (order 108) lies on no chain with the tick (order 5), because 5 and 108 are incomparable under divisibility. The pada and the tick generate ⟨8⟩, the coil of layer 8, of order 540 and index 8. That subgroup is the internal direct sum C₁₀₈ ⊕ C₅. This is the exact content of the stop "the pada step 40 is not in the order-10 subgroup."

## 4. The Coxeter clock

**Theorem 6 (THEOREM).** Let c = s₁s₂⋯s₈ be the product of the eight simple reflections of E8. Then:

1. c has order 30 and c¹⁵ = −I;
2. its characteristic polynomial is Φ₃₀(x) = x⁸ + x⁷ − x⁵ − x⁴ − x³ + x + 1;
3. its exponents, the m with e<sup>2πim/30</sup> an eigenvalue, are the units mod 30: 1, 7, 11, 13, 17, 19, 23, 29. They sum to 120, the number of positive roots, and the degrees m + 1 multiply to |W(E8)| = 696,729,600;
4. c permutes the 240 roots in 8 free orbits of 30. Therefore c commutes with the walk operator A = Σ<sub>α</sub> T<sub>α</sub> and preserves the band λ. It is a symmetry of the bath already in the model, not a new term.

**Definition (SELECTED_REFERENCE).** The *Coxeter clock* is the isomorphism from the order-30 subgroup ⟨144⟩ of the circle onto ⟨c⟩ that sends the step 144 to c. There are φ(30) = 8 such isomorphisms, one for each exponent. Every statement below is unchanged, up to relabeling by a unit, if another is chosen.

Under the clock, the step 144k acts on the bath as c<sup>k</sup>. In particular:

- the tick 864 = 6·144 acts as c⁶;
- the sun 1440 = 10·144 acts as c¹⁰;
- the half-turn 2160 = 15·144 acts as c¹⁵ = −I;
- the yuga segments 1728, 1296, 864, 432 act as c¹², c⁹, c⁶, c³.

**Obstruction 7.** No homomorphism from the whole circle into the automorphisms of the bath lattice extends the clock. An extension would need a lattice automorphism of order 4320. An element of GL₈(Z) of order divisible by 27 needs a primitive 27th root of unity among its eigenvalues, which has degree φ(27) = 18 > 8. ∎

## 5. Fixed momenta are Morse points

**Lemma 8 (THEOREM).** Let g ∈ W(E8) have no eigenvalue 1, and let gθ ≡ θ on the Brillouin torus. Then θ is a critical point of λ.

*Proof.* λ(gθ) = λ(θ) for all θ, so gᵀ∇λ(gθ) = ∇λ(θ). At a fixed point ∇λ(gθ) = ∇λ(θ), so ∇λ(θ) is fixed by g⁻¹. Since g has no eigenvalue 1, ∇λ(θ) = 0. ∎

The number of fixed momenta of g is |det(g − I)|, the order of E8/(g − I)E8.

**Theorem 9 (THEOREM).** The 29 non-identity elements of the Coxeter clock fix the following momenta.

| element of the circle | on the bath | order | fixed momenta | which Morse points |
|---|---|---|---|---|
| tick 864 (and 1728, 2592, 3456) | c⁶, c¹², c¹⁸, c²⁴ | 5 | 25 = 5² | the origin and 24 points of A4+A4 (ε = 250, index 4) |
| sun 1440 (and 2880) | c¹⁰, c²⁰ | 3 | 81 = 3⁴ | the origin and 80 points of E6+A2 (ε = 243, index 2) |
| half-turn 2160 | c¹⁵ = −I | 2 | 256 = 2⁸ | all half-periods: the origin, all 120 of E7+A1 (ε = 224), all 135 of D8 (ε = 256) |
| the other 22, orders 6, 10, 15, 30 | c<sup>k</sup> | — | 1 | the origin only |

The fixed groups are (Z/5)², (Z/3)⁴ and (Z/2)⁸. The band values are exact, computed in the cyclotomic integers Z[ζₚ]. At all 362 fixed momenta the floating-point gradient is below 2·10⁻¹³. The Morse indices and stabiliser types were recomputed at each point.

The prime-order elements of the clock thus see exactly the Morse families of torsion orders 2, 3 and 5. The A8 family is also 3-torsion, but the sun misses it. The families of torsion orders 4 and 6 and the two edge families are not seen. As arithmetic only: the 29 elements fix 22 + 4·25 + 2·81 + 256 = 540 momenta in all, the order of the coil (ARITHMETIC; no map joins the two).

## 6. The tick turns two carriers

Let r be the K5 vertex rotation, the cyclic permutation of the first five coordinates. It acts on the carrier's A4 by moving each oriented edge eᵢ − eⱼ to eᵢ₊₁ − eⱼ₊₁, and it fixes the twin A4′. Let r′ = s(e₆+e₇) · s(½(1,1,1,1,1,−1,−1,1)) · s(½(−1,−1,−1,−1,−1,1,−1,1)) · s(e₇−e₆), a Coxeter element of the twin A4′. It fixes the carrier's A4.

**Theorem 10 (THEOREM).** There is a w ∈ W(E8) such that the Coxeter element c′ = w c w⁻¹ satisfies

**c′⁶ = r r′**

exactly. So the tick of the circle acts on the bath as the carrier's own rotation on A4 together with the twin rotation on A4′: **the tick turns two carriers.** In standard coordinates, 2c′ is the signed 0–1 matrix

```
 0  1 -1  0  1  1  0  0
 1  0  0 -1  0  0  1  1
 0  1 -1  0 -1 -1  0  0
-1  0  0 -1  0  0  1 -1
 1  0  0  1  0  0  1 -1
 1  0  0 -1  0  0 -1 -1
 0 -1 -1  0 -1  1  0  0
 0  1  1  0 -1  1  0  0
```

c′ is the product of the reflections in the simple system −e₄−e₈, e₁−e₂, e₄+e₆, ½(−1,1,−1,−1,1,−1,1,1), ½(1,1,1,1,−1,−1,−1,−1), ½(−1,−1,1,−1,1,1,−1,1), −e₃−e₅, e₃+e₇, taken in that order.

**Theorem 11 (THEOREM).**

- The sun c′¹⁰ permutes the 240 roots in 80 triangles. Four mutually orthogonal triangles span A2⁴, of index 9 in E8: the sun turns four triangles.
- The half-turn c′¹⁵ = −I flips eight orthogonal edges, A1⁸ of index 16.
- So for p = 2, 3, 5, the order-p element of the Coxeter clock rotates 8/(p−1) copies of the complete graph K<sub>p</sub> and fixes p<sup>8/(p−1)</sup> momenta: 256, 81, 25.
- The splitting of Proposition 4 holds for the operators: c′ = (−I)·c′¹⁰·c′⁶, the half-turn times the sun times the tick.
- The yuga segments act as 1728 ↦ (rr′)², 864 ↦ rr′, 1296 ↦ −(rr′)⁴ and 432 ↦ −(rr′)³.

This is the map the integrated paper calls absent ("No stored map sends a yuga tick to a lattice vector or a Morse point"). It is a selected construction: the generator and the conjugate are chosen. Its properties are theorems.

## 7. Where 7 enters

**Theorem 12 (THEOREM).**

- The normalizer of ⟨c′⟩ in W(E8) has order 240 = 30 × 8. Every unit mod 30, and so every exponent of E8, is realized by conjugation: w c′ w⁻¹ = c′<sup>m</sup>. The centralizer is ⟨c′⟩ itself.
- No element of order 24 commutes with c′. The 40 elements of order 24 that normalize ⟨c′⟩ act on it by the exponent 7 or by 13 = 7⁻¹, twenty each.
- There is a **day clock** d of order 24, with characteristic polynomial Φ₂₄ = x⁸ − x⁴ + 1, such that:
    - d⁴ = c′⁵, so the two clocks agree on the circle's common subgroup ⟨720⟩, since 4·180 = 5·144 = 720;
    - **d c′ d⁻¹ = c′⁷.**

On the circle the steps 144 and 180 commute and generate the atlas, 36 = 180 − 144, of order 120. On the bath the day and the Coxeter clock can be realized together only with the twist by the exponent 7, and d c′⁻¹ has order 24, not 120.

**Corollary 13 (OBSTRUCTION).** The atlas cannot act on the bath. The 7 at which the integrated path stops is the E8 exponent by which the day acts on the Coxeter clock. "7 does not divide 4320" remains true: the circle has no element of order 7. On the circle, multiplication by 7 is an automorphism of order 36.

The day's quarter d⁶ is the step 1080, of order 4. It fixes 16 momenta: the origin and 15 points of D8 at the top of the band. d³ (order 8) fixes the origin and 3 points of D8, and d⁸ = c′¹⁰ is the sun.

**Proposition 14 (THEOREM).** The order-20 clock ⟨216⟩ normalizes the Coxeter clock with the twist 11. All 24 such elements have this twist, and one with v² = c′³ agrees with the Coxeter clock on the shared yuga subgroup ⟨432⟩ (characteristic polynomial Φ₂₀). No element of order 18 normalizes the Coxeter clock.

## 8. What can act on the bath

**Theorem 15 (THEOREM).** A subgroup of the circle acts faithfully on the bath lattice, that is, embeds in W(E8) = Aut(E8), if and only if its order is one of

1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30.

*Proof.*

1. **Existence.** Explicit elements realize every order on the list:
    - powers of c′ give 1, 2, 3, 5, 6, 10, 15 and 30;
    - powers of d give 4, 8, 12 and 24;
    - the order-20 clock gives 20;
    - seeded products of reflections give 9 and 18.
2. **Degree bound.** An element of order m in GL₈(Z) needs Σ φ(pᵃ) over the prime powers of m to be at most 8 (minus 1 when m ≡ 2 mod 4). Among the divisors of 4320 this leaves only 16, 36, 40 and 60 beyond the list.
3. **16.** |W(E8)| and |W(D8)| both have 2-part 2¹⁴, so W(D8) contains a Sylow 2-subgroup of W(E8). The 2-elements of W(D8) have order at most 8, since a negative 8-cycle is not in D8.
4. **36.** The fourth power of such an element has characteristic polynomial Φ₉(x − 1)². By Steinberg's theorem it lies in the Weyl group of the roots orthogonal to its fixed plane, which must be an E6. The orthogonal lattice is even and binary of determinant 3, i.e. A2. Aut(A2) has 12 elements, of orders 1, 2, 3 and 6, and none of order 4.
5. **40 and 60.** The 8th or 12th power has characteristic polynomial Φ₅(x − 1)⁴, so it lies in an A4. The 5,806,080 = 240·56·27·16 ordered A4 chains of E8 form one W-orbit, because 5,806,080 = |W(E8)|/|W(A4′)|. So both lattices are A4. Aut(A4) has 240 elements, of orders 1, 2, 3, 4, 5, 6 and 10 only, so the order cannot be 40 or 60. ∎

**Corollary 16.**

- The maximal clocks of the circle on the bath are ⟨144⟩ (Coxeter, 30), ⟨180⟩ (day, 24), ⟨216⟩ (20) and ⟨240⟩ (18). The Coxeter subgroup is the largest.
- The spine acts on the bath through tick, yuga and Coxeter, and stops at the atlas (OBSTRUCTION).
- The moon (order 36), nakshatra (27), pada (108), atlas (120), Salina's ⟨12⟩ (360) and the Human Design gate ⟨64⟩ (135) cannot act on the bath at all (OBSTRUCTION).

## 9. The stops, restated

| stop in the integrated build | its check there | what is proved here | status |
|---|---|---|---|
| 7 does not divide 4320 | `4320 % 7 !== 0` | no element of order 7; 7 is the twist d c′ d⁻¹ = c′⁷ of the day on the Coxeter clock (§7) | OBSTRUCTION, THEOREM |
| pada 40 not in the order-10 subgroup | `40 % 432 !== 0` | the pada is on no chain with the tick, pada + tick = coil (§3), and the pada subgroup cannot act on the bath (§8) | OBSTRUCTION |
| Krishna lift not 4 + 5 | `4 + 5 !== 4` | the typed operands are not in this repository; the integer test does not test the lift | REPORTED |
| Prema's index 13 not her width 2 | `2 !== 13` | on the circle ⟨13⟩ is everything and ⟨2⟩ has index 2; the stage typing is canon data not stored here | REPORTED |
| no birth time, epoch or ayanamsha | — | unchanged; the sidereal readings stay counts | UNFORMED |
| atlas | not stated | the spine stops acting on the bath at the atlas: no lattice automorphism has order 120 | OBSTRUCTION |

## 10. Corrections to the integrated build

1. **DOTS_LATTICE**: "The pada order 108 … meets the cycle order 720 only at 36, the atlas." ⟨40⟩ ∩ ⟨6⟩ = ⟨120⟩ has *order* 36; it is the moon. The atlas ⟨36⟩ has order 120. The integrated paper itself says "The order 36 is not the atlas."
2. **SIDEREAL_DOTS**: "meet at order 2, whose only element is 2160." The subgroup is {0, 2160}; 2160 is its only nonzero element.
3. **Paper**: "360000 is not a step." 360000 ≡ 1440 (mod 4320), so the W₀ scalar reduces to the sun step.
4. **Paper**: "Siri and Shay, both 4, … Their sum 5 has order 864." Siri + Shay = 8, which is Rughnath, of order 540. The 5 of order 864 is Prema + Sai.
5. **Paper**: "The doubling residues have circle orders 4320, 2160, 1080, 540, 864, 4320." In doubling order 1, 2, 4, 8, 7, 5 they are 4320, 2160, 1080, 540, 4320, 864.
6. **Paper and `e8Frame.ts`**: "Rank 8 times the mark sum 30 recovers the 120 positive roots." 8 × 30 = 240 is all the roots. The positive roots are 8 × 30/2; the model code has the /2.
7. **INTEGRATED**: the tower 36 × 12 × 2 × 5 skips the Coxeter subgroup the spine starts from. It is 36 × 4 × 3 × 2 × 5 (Theorem 2).
8. **Superseded**:
    - "No stored map sends a yuga tick to a lattice vector or a Morse point."
    - "The typed rotor orders are 4, 5 and 20. None equals 30."
    - "The order-5 element of the 4320-circle is not this tick."

    Under the selected clock, the tick acts on the bath as rr′, the carrier rotation on A4 together with the twin rotation, and fixes 24 Morse points. The order-30 rotor is c′.

## 11. Status and what stays open

- **Layer 19** holds 50 checks: THEOREM 29, OBSTRUCTION 14, SELECTED_REFERENCE 2, ARITHMETIC 2, REPORTED 2, UNFORMED 1. **Layer 20** holds 22: THEOREM 12, OBSTRUCTION 3, ARITHMETIC 2, CONDITIONAL 1, REPORTED 4.
- **Arithmetic only** (shared integers; no map joins them):
    - 69120 = |W(E8)|/|W(A6×A1)| is the size of the A6+A1 family and also the Human Design count;
    - exactly three families are whole numbers of circles: A6+A1 (16), A7 (4) and A7+A1 (2);
    - the Coxeter powers fix 540 momenta in all.
- **Unchanged and open**:
    - the convexity collar inside (223.58, 224);
    - the rational coefficients of the order-16 walk recurrence, and its proof for every n;
    - the six SCR6 operands, the epoch, the Krishna lift's operands, GKSL, SI, BRST, BV and Einstein–Hilbert.
- **Owner decisions** remain the only route to moving a gate: AUTH, DYN_BIND, TIME_BIND, PredictionFreeze and T3081.

## 12. Against the latest canon (16:49 UTC)

Layer 20 reads the canon before anything is built on this edition. It was read at 16:30 UTC and again at 16:49, after the sibling posted four more notes. The sibling's 16:47 consolidation (CURRENT_20261028_2046) restates those notes, and its paper's text is identical to the 16:43 paper discussed below.

- **Position.** In the Quick Access workbook (updated 15:05 UTC, cutoff 14:59:48), OMSOON736 and the 10:04 Canon Check stay controlling. The earlier verified build is listed as a SELECTED REFERENCE. This edition arrived after the cutoff.
- **What the sibling adopted.** The sibling's builds of 16:18–16:43 UTC take over the splitting 144 = 2160 + 1440 + 864 of Proposition 4. They also take over the twist by 7, as "a separate extension in which the day element normalizes the Coxeter clock". SPINE_CORRECTIONS (16:31) takes over all six corrections of §10.
    - In W(E8) the twist extension is realized, and it is smaller than the abstract one. The day and Coxeter clocks generate a group of order exactly **120**, because d⁴ = c′⁵.
    - The semidirect product C₃₀ ⋊ C₂₄ of order 720 cannot embed, since the normalizer of ⟨c′⟩ has order 240.
- **New errors in the sibling's notes.** "The step 5 generates the tick" and "the step 25 generates the tick subgroup, order 864" confuse step and order. ⟨5⟩ = ⟨25⟩ is the subgroup of order 864; the tick has order 5. The 16:43 paper does not repeat these errors. It calls 5 "dual to the tick step".
- **What remains in the 16:43 sibling paper.**
    - One remnant. Its circle-subgroup theorem still says "360000 is not a step", next to its own correction "the scalar 360000 reduces to 1440".
    - The harmonic statement is still doubled. Its §13 calls 3|p|⁴ − 7Σp⁴ "the unique primitive harmonic line" on the contrast plane, but computes it with the ambient Laplacian of ℝ⁵. A later theorem says 2s₂² − 5s₄ is invariant-harmonic and 3s₂² − 7s₄ is not. Each is right for its own Laplacian, so the statement should name which one it uses. Layer 1 records both.
- **What the new notes leave unreplayed.** COXETER_POWERS shows that no named power of the Coxeter element fixes a root. It leaves the 25, 81 and 256 fixed momenta unreplayed, as "a different set".
    - They are indeed a different set. On the Brillouin torus, c<sup>k</sup> fixes <span style="white-space:nowrap">|det(c<sup>k</sup> − I)| = Φ<sub>n</sub>(1)<sup>8/φ(n)</sup></span> points, where n = 30/gcd(k, 30). This holds for every k.
    - The count is 1 at orders 30, 15, 10 and 6, 25 at order 5, 81 at order 3, and 256 at order 2.
    - So fixed momenta beyond the origin occur exactly at prime-power orders. They are the Morse points of §5.
- **Commuting clocks.** SPINE_CORRECTIONS says "the circle still makes the day and Coxeter clocks commute". On the circle they do, and together they generate the atlas, of order 120. On the bath no element of order 24 commutes with c′, because the centralizer of c′ is ⟨c′⟩. No element of W(E8) has order 120. That is why the realized day clock twists (§7).
- **The atlas, the sun and the moon.** The circle statements of ATLAS_FACTOR and SUN_MOON hold (THEOREM). Examples are the tower in atlases 1, 4, 12, 24, 120, the identity 432 + 864 = 36², and the moon's primary parts 1080 + 3360 + 0. Their readings are ARITHMETIC: the sun is 40 atlases, which is the pada step; the half-turn is 60 atlases, which is the frame; and 8/3 is Coxeter cycles over the sun's cycle length.
- **A canon claim proved.** The 12:32 update's "maximum group speed exactly √30" holds as a supremum. |∇ε|² ≤ 120ε everywhere, by Cauchy–Schwarz and the frame Σααᵀ = 60I. Equality holds only as k → 0.
- **The Canon Check.**
    - The identities behind its growing-time preparation laws (P1–P2) are replayed. The laws themselves, ε<sup>−1/2</sup> for the monopole and ε<sup>−1/3</sup> for the dipole, stay CONDITIONAL on the inherited exterior contract.
    - Its scalar bound (r+1)(d+2) ≥ 195 follows from layer 14, which excludes every shape up to 455.
- **The separate model** ("Finite Spectral Dynamics with Complete Observation and Exact Cyclic Addresses", 16:07 UTC) is rebuilt from its definitions:
    - five channels are necessary and sufficient;
    - of the 252 five-edge sensor designs, 162 are complete and 90 have rank 4, and 72 are optimal with minimum eigenvalue (3 − √5)/6;
    - the 25-coordinate flag geometry has intersection det −48 and vertex distance exactly √(8/7);
    - the collocated transfer functions follow from the spectral projectors.

    Its root-to-circle intertwiner is rational, with the metric mismatch it reports. The two-carrier tick of §6 is the isometric version: c′⁶ = rr′ inside W(E8).

## Appendix A. The readings

| name | step | order | in the Coxeter subgroup | on the bath | fixed momenta |
|---|---|---|---|---|---|
| Coxeter step | 144 | 30 | yes | c′ | 1 |
| tick, yuga 3 | 864 | 5 | yes | c′⁶ = rr′ | 25 |
| yuga 1 | 1728 | 5 | yes | c′¹² = (rr′)² | 25 |
| yuga 2 (36²) | 1296 | 10 | yes | c′⁹ = −(rr′)⁴ | 1 |
| yuga 4 | 432 | 10 | yes | c′³ = −(rr′)³ | 1 |
| sun | 1440 | 3 | yes | c′¹⁰ | 81 |
| W₀ scalar 360000 | ≡ 1440 | 3 | yes | c′¹⁰ | 81 |
| half-turn | 2160 | 2 | yes | −I | 256 |
| day | 180 | 24 | no | d (selected), twist 7 | 1 |
| signs | 360 | 12 | no | d² (inside the day) | 1 |
| atlas | 36 | 120 | no | cannot act | — |
| moon | 120 | 36 | no | cannot act | — |
| nakshatra | 160 | 27 | no | cannot act | — |
| pada, forest maps | 40 | 108 | no | cannot act | — |
| Human Design gate | 64 | 135 | no | cannot act | — |
| Hodge trace | 150 | 144 | no | cannot act | — |
| Prema width | 2 | 2160 | no | cannot act | — |
| Sai | 3 | 1440 | no | cannot act | — |
| Siri, Shay | 4 | 1080 | no | cannot act | — |
| Sachin | 6 | 720 | no | cannot act | — |
| Jessica | 7 | 4320 | no | cannot act | — |
| Rughnath | 8 | 540 | no | cannot act | — |
| stray | 9 | 480 | no | cannot act | — |
| edge pair | 10 | 432 | no | cannot act | — |
| Salina | 12 | 360 | no | cannot act | — |
| Prema index | 13 | 4320 | no | cannot act | — |

"Cannot act" means no faithful action of that cyclic subgroup on the bath lattice (Theorem 15). The role widths are small steps that generate large subgroups.

## Appendix B. Replay

```
python verify.py              # 20 layers, 393 checks
python -m pytest -q           # 27 tests
node --experimental-strip-types --no-warnings ports/ts/run.mjs   # the TypeScript port
python -c "from oes import spine; print([c.name for c in spine.run().checks if not c.passed])"
```

The integrated build was read from the Drive folder "One Machine 20261028" (15:12–15:31 UTC). Its TypeScript model was read but not executed here.
