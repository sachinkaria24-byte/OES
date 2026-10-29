# One Machine: the unified edition

**OES end-to-end model, 28–29 October 2026.** This edition puts the whole model in one text with one ledger. It brings together the verified build (layers 1–18), the integrated spine (layer 19), the canon synchronization (layer 20), the sibling's 28 October ledger of joins (layer 21), the sibling's evening notes with the canon's 19:10 continuation (layer 22), and one diagram of checked joins on six levels, which follows the sibling's notes to 02:55 on 29 October and the hub's release K+ADDENDUM3 (layer 23), and the particle assignment on E8's roots (layer 24). It is a selected mathematical build replayed from matrices. It is not a source admission and not a change to the canon matrices.

**AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND · DYN_BIND = NOT_INSTALLED · SCR6 = NOT_RUN_OPERAND_ABSENT · PredictionFreeze = NOT_TRIGGERED.** No gate moves, and no term is added to the action.

**Custody.**

- Repository `sachinkaria24-byte/OES`, branch `claude/lagrangian-spectral-spacetime-model-t2253b`.
- `python verify.py` replays 24 layers in **753 checks**. Of these, 680 hold: THEOREM 525, OBSTRUCTION 51, ARITHMETIC 38, UNFORMED 24, CONDITIONAL 23, SELECTED_REFERENCE 17, REMOVED 2. The other 73 are REPORTED records.
- `python -m pytest` runs 64 tests.
- `ports/ts/` holds three drop-in audits for the sibling's app (43 rows, residual 0). `data/clocks.json` holds the explicit clock matrices, `data/e8_assignment.json` the 240 roots with their Standard-Model quantum numbers, `docs/LEDGER.md` the unified ledger, and `docs/DOTS.md` draws every checked join.
- This text supersedes `one-machine-20261028-verified.pdf` (layers 1–18) and `one-machine-20261028-spine.pdf` (layers 19–20) as the current paper. Both stay in `docs/paper/` as history.

## Abstract

The model has one datum, the signless incidence of K5. It has one action, fifteen oscillators with stiffness D², and one bath, the E8 root lattice. Everything else is a map between these three objects, a count, or a gate. This edition does six things.

**It collapses the ledger.** The sibling's 28 October ledger states about forty joins. The 129 sentences of the form "X contains every tick" or "X misses every nonzero tick" all carry one bit: the tick 864 lies in ⟨X⟩ exactly when 5 does not divide X. All 129 are checked against that one line, together with their step counts, their indices and 38 stated subgroup orders. The numbers that ride on the bit are shared integers, and no map joins them.

**It puts every clock in one group.** The normalizer of the Coxeter clock in W(E8) has order 240. In it:

- the tick is the commutator of the day clock and the Coxeter clock: d c′ d⁻¹ c′⁻¹ = c′⁶ = r r′, two carrier rotations at once;
- the day–Coxeter group has order 120, centre ⟨c′⁵⟩ and derived group the tick. It permutes its five day clocks as the affine group of the pentagon: the tick rotates them and the day doubles them, pentagon to pentagram;
- the golden clock has order 20, and its fourth power is the tick;
- the circle's mirror x ↦ −x is an involution that acts on the carrier as the pentagon reflection, fixing three atoms;
- the carrier and its twin can be exchanged only by elements of order 4, 8, 12 or 20, never by an involution, and every exchange doubles their index-5 glue.

The order-24 day element, which the sibling's build reports as not constructed, is given explicitly.

**It states what is physical and what is not.**

- The energy splits into four conserved pieces, and the vertex and edge sectors never exchange energy.
- The 240 roots are D8 plus one half-spin orbit.
- The source oscillator, of frequency 2, is not a carrier mode.
- Compton and Bohr lengths, the photoelectric effect, the double slit and entanglement stay unformed. No operand is stored for them, and the action has no dimensionful constant.

**It replays the evening notes (layer 22).**

- The sibling's 28 notes of 18:32–19:21 add 223 readings on the bit, and every one holds.
- Seven moments that the sibling reported as not replayed are the moments of the alternating hexagon port on the E8 lattice. They are computed exactly from the 240 roots, and the eighth is new.
- The canon's 19:10 continuation asks two things. A commutator should not be called 864 without a map: every map from the day–Coxeter group to the circle kills it. Equal energy totals do not make equal splits: the three splits are the margins of one conserved table.

**It joins all the dots, at every level (layer 23).** Every object of the model is a dot and every checked map a join, and 60 dots with 161 joins form one connected diagram that no two maps hold together. Every layer has a dot, and the dots sit on six levels, from the integers up to physics, each joined inside and to every other level. The two K5 incidences are the positive roots of A4 and D5, so the carrier's spectrum {0, 3, 8} is {0, h(D5) − h(A4), h(D5)}. The canon's selected six-port is the oriented triangle 0-1-2 of K5, and its heat coefficient 1/(22394880000000 π⁴) follows from that. The canon's L0 spectrum 0, 250⁴ is the bath at the tick's fixed momenta, and its h81 is the four-cube complex, whose vertices are four qubits. The carrier's symmetry is the S5 that fixes the cone point of K6, the only S5 in S6 that keeps D; the transitive S5 = PGL(2,5) gives a different module.

**It works out the particle assignment on E8's roots (layer 24).** The carrier's A4 is taken as SU(5) and its twin as a family SU(5)′. Then the 240 roots carry the Standard Model's quantum numbers, with charge quantization on every root, and the assignment is unique up to W(E8). One root of every pair ±ρ is always anomalous. Three generations follow from the bracket rule and anomaly freedom, and the top coupling has no root realization.

## 0. The model on one page

| object | definition | what is proved | layer |
|---|---|---|---|
| datum | signless incidence M of Kₙ (n × C(n,2)) | dim ker M = n holds only at n = 5 | 1 |
| carrier | D = [[0, M], [Mᵀ, 0]] on ℓ²(V ⊔ E), dim 15 | spec D² = {0⁵, 3⁸, 8²}, Tr D² = 40, Tr D⁴ = 200 | 1 |
| action | S = ∫ ½\|ψ̇\|² − ½⟨ψ, D²ψ⟩ | 15 oscillators: 5 free, 8 at √3, 2 at 2√2; four conserved energies | 1, 21 |
| spectral triple | (ℂ<sup>V</sup> ⊕ ℂ<sup>E</sup>, ℓ²(V ⊔ E), D, γ) | heat trace 5 + 8e<sup>−3β</sup> + 2e<sup>−8β</sup>; Witten index −5 | 2, 5 |
| observer | Kalman readouts of (ψ, ψ̇) | dark sector P5 ⊕ P5; five channels complete it | 5, 20 |
| bath | E8 root lattice, Δ = 240 − A | band [0, 256] (256 attained; the upper bound reported); 11 critical families, 243,600 points, Morse sum 0; group speed √30 | 3, 8, 16, 20 |
| walks | W_n = closed walks of length n | one shift operator of order 16 and degree 58; its 11 in-band roots are the 11 critical values | 14, 16 |
| native action | source q on P5 ⊕ P5, quadratic port W_AS, six-site clique | q̈ + 4q = 0 at the origin; sharp quartic 40/9 | 4, 10 |
| glue | E8 ⊃ A4 ⊕ A4′ | index 5, glue x ↦ ±2x; no involution exchanges the two | 11, 21 |
| waves | Hodge complex on the K5 edges | sound (4) and light (6) are isochronous at √5; Agni = Curl² | 17 |
| circle | Z/4320 = 2⁵·3³·5 | one lemma; the tower 36 × 4 × 3 × 2 × 5; the tick bit | 19, 21 |
| assignment | E8 ⊃ SU(5) × SU(5)′ on the 240 roots | Standard-Model numbers on every root, unique up to W(E8); one root of every pair anomalous; three generations given the bracket rule | 24 |
| clocks | the normalizer of ⟨c′⟩ in W(E8), order 240 | every circle unit realized; the tick = [day, Coxeter] | 19, 21 |
| dots | 57 objects on six levels, 116 checked maps, no bridge | one connected diagram, every level joined inside and to the next; the K5 incidences are the A4 and D5 roots | 23 |
| curvature, cosmology | Lin–Lu–Yau; spectral action on M⁴ × F | discretely flat bath; G and Λ_cc only with external inputs (CONDITIONAL) | 6, 7 |
| gates | AUTH, TIME_BIND, DYN_BIND, PredictionFreeze, W_L, T3081 | none moves | 13 |

## 1. The datum, the action and the energy

**The datum.** For the complete graph Kₙ, the signless incidence M (vertex × edge) has dim ker M = n exactly when n = 5, for every n. This is the only input. The fifteen atoms are the 5 vertices and the 10 edges of K5.

**The carrier and its action.**

- D = [[0, M], [Mᵀ, 0]] is odd, with grading γ = +1 on vertices and −1 on edges.
- D² = diag(MMᵀ, MᵀM), with MMᵀ = 3I + J on the vertices. The spectrum is {0⁵, 3⁸, 8²}, so Tr D² = 40 and Tr D⁴ = 200. The kernel ker D = P5 ⊂ ℓ²(E) is the irreducible 5 of S5.
- The action S = ∫ ½|ψ̇|² − ½⟨ψ, D²ψ⟩ has no other term. A relative constant between its two terms is a rescaling of t.
- Its Euler–Lagrange equation ψ̈ + D²ψ = 0 is solved in closed form sector by sector. The frequencies are 0, √3 and 2√2, and their squared ratio 8/3 is not a rational square.

**Four conserved energies (THEOREM, layers 5 and 21).** D² is block diagonal in V ⊕ E, so the vertex and edge sectors never exchange energy. Each spectral sector λ ∈ {0, 3, 8} is also invariant. Together these give four conserved pieces.

The sibling's checked datum takes:

- vertex value (1, −1, 0, 0, 0) + (1, 1, 1, 1, 1);
- edge value Mᵀ applied to the contrast;
- velocity the alternating cycle on the edges 01, 12, 23, 03.

Its quadratic form is 64 = 40 + 6 + 18, and its energy is

> 34 = 20 (uniform vertex mode) + 3 (vertex contrast) + 9 (edge image of the contrast) + 2 (the cycle).

The vertex energy E_V = 23 and the edge energy E_E = 11 stay constant along the exact motion. The ledger's "34 = 12 + 20 + 2" is the spectral grouping of the same four pieces, with 12 = 3 + 9.

**Decoupling, quantized (CONDITIONAL).** Under canonical quantization of S, the oscillating modes evolve by U_V(t) ⊗ U_E(t). The carrier therefore never entangles vertices with edges; entanglement can only be present in the initial data. The ledger's "entanglement is not stored" becomes a sharper statement: the carrier cannot create it. The quantization is a choice the canon does not store.

**Symmetries of the action (THEOREM).**

- The graph reflection of the pentagon, i ↦ −i on the vertices, keeps D² and fixes three atoms (one vertex and two edges).
- The fifteen-atom involution i ↦ 14 − i (the ledger's "above and below") fixes one atom and has eigenspaces of ranks 8 and 7. It sends a vertex to an edge, so it does not keep D².

**The harmonic quartic (THEOREM).** The S5-invariant quartics on the contrast plane are spanned by |x|⁴ and Σxᵢ⁴. For the plane's own Laplacian, the harmonic line is 2|x|⁴ − 5Σxᵢ⁴. For the ambient Laplacian of ℝ⁵, it is 3|x|⁴ − 7Σxᵢ⁴. Neither enters the action: coupling a quartic would add a dimensionful constant.

**The source is not a carrier mode (OBSTRUCTION).** The stored source equation is q̈ + 4q = 0, with frequency 2. Since 4 ∉ spec D² = {0, 3, 8}, the source oscillator is not one of the fifteen carrier modes.

## 2. The spectral triple and the observer

**Spectral content (THEOREM, layer 2).**

- The heat trace is Z(β) = 5 + 8e<sup>−3β</sup> + 2e<sup>−8β</sup>.
- The moments are Tr D<sup>2k</sup> = 15, 40, 200, 1240, 8840.
- The spectral zeta function is ζ<sub>D</sub>(s) = 8·3<sup>−s</sup> + 2·8<sup>−s</sup>.
- The spectral dimension tends to 0 in both the UV and the IR. The carrier has no emergent continuum dimension.

**Observation (THEOREM, layers 5 and 20).**

- A scalar readout of x = (ψ, ψ̇) sees at most 6 of the 30 dimensions, two for each spectral line.
- The Witten index is Tr γ e<sup>−βD²</sup> = −5.
- The dark sector, reachable by edge forcing but invisible to Dψ, is the native source space P5 ⊕ P5 (10 dimensions).

Five fixed channels are necessary and sufficient to complete the observer. With H = [D; L], the reconstruction R satisfies RH = I₁₅, and P₀ = I − 11K/24 + K²/24 with K = D². Of the 252 five-edge sensor designs, 162 are complete and 90 have rank 4. Every complete design has determinant 1/162. The 72 optimal designs have minimum eigenvalue (3 − √5)/6.

## 3. The bath

**Roots (THEOREM, layers 3 and 21).**

- The 240 roots of E8 are 112 integer roots, which form D8, and 128 half-integer roots, which form one W(D8)-orbit (a half-spin weight set). So 248 = so(16) + 128.
- The root frame is Σααᵀ = 60I₈, and the root graph is 56-regular.
- [W(E8) : W(D8)] = 135. This is the D8 family at the top of the band, and the half-turn's 256 fixed momenta are 1 + 120 + 135.
- The ledger's "SU(2) is not derived" stands.

**The band and its critical points (THEOREM, layers 3, 8, 14, 16).** The symbol is ε(k) = 240 − Σ cos(α·k). It attains 0 and 256, the top at the band vertex π(1,1,1,1,0,0,0,0). That the range is exactly [0, 256] is reported (an alcove branch-and-bound, layer 8), and the census below agrees with it. The census covers the vertices and edges of the alcove and lists λ = 240 − ε, the number of points and the Morse index:

| family | λ | points | index | | family | λ | points | index |
|---|---|---|---|---|---|---|---|---|
| E8 | 240 | 1 | 0 | | A6+A1 (edge) | −185/16 | 69,120 | 6 |
| E7+A1 | 16 | 120 | 1 | | A7 (edge) | −320/27 | 17,280 | 7 |
| E6+A2 | −3 | 2,240 | 2 | | A7+A1 | −12 | 8,640 | 7 |
| D5+A3 | −8 | 15,120 | 3 | | A8 | −12 | 1,920 | 8 |
| A4+A4 | −10 | 48,384 | 4 | | D8 | −16 | 135 | 8 |
| A5+A2+A1 | −11 | 80,640 | 5 | | | | | |

- There are 243,600 points in all, and the Morse sum is 0 = χ(T⁸).
- The eleven values of λ are exactly the eleven in-band roots of the walk operator below, so the band geometry and the walk data are one statement.

**The walks (THEOREM, layer 14).**

- W₀…W₉₀ are exact from two independent engines, and W₀…W₆₀₀ are known modulo primes.
- Every recurrence with (r+1)(d+2) ≤ 455 is excluded.
- The annihilator is one operator L₁₆, of order 16 and degree 58, the same modulo four primes. Its characteristic polynomial has the eleven in-band roots, (z+12)² among them, and five roots outside the band.
- Asymptotically, W_n = (16/π⁴)·240ⁿ·n⁻⁴·(1 − 2/n + (23/15)/n² + O(n⁻³)).

**Speed and density.**

- The long-wave dispersion is ε = 30|k|² − (3/2)|k|⁴ + (1/24)|k|⁶ + …, so the sound speed is √30 (layer 3). This is also the bath's maximal group speed, as a supremum that is never attained: |∇ε|² ≤ 120ε, by the frame and Cauchy–Schwarz (layer 20).
- The nine positive critical energies have distinct square-free parts, so their frequencies are independent over ℚ and their flow is dense on T⁹ (layer 18).

**Open.** The convexity collar (223.58, 224) remains open.

## 4. The carrier inside the bath

**Native action (layers 4 and 10).**

- The source q = (a, b) lives in P5 ⊕ P5, with mass M_s = I/4.
- The port g = W_AS(a ∧ b) is quadratic onto the six-dimensional cycle space L6, with W_ASᵀW_AS = (10/9)P and sharp quartic constant 40/9.
- The six-site clique has A_bb = 241I − J and exterior coupling BB* = 183P_c + 495P_u.
- At linear order the source obeys q̈ + 4q = 0 and has no linear channel into the bath. Its frequency-4 harmonic lies inside the band through a thin channel.
- The printed chart T₆ preserves the contrast lattice, and T₆|V_c has determinant 31, so 155 = 5 × 31.

**Glue (THEOREM, layers 11 and 21).** The carrier's own root system A4 = {eᵢ − eⱼ : i, j ≤ 5} sits in E8, and its orthogonal complement is a twin A4′. The index is [E8 : A4 ⊕ A4′] = 5, and the glue is x ↦ ±2x. Layer 21 completes the picture with the stabilizer of the pair {A4, A4′} in W(E8), which has 57,600 elements:

- the 28,800 elements that keep each carrier act on the glue Z/5 by ±1;
- the 28,800 elements that exchange the carrier and its twin act on the glue by ±2, the doubling;
- every exchange has order 4, 8, 12 or 20. **No involution exchanges the carrier and its twin.**

The day's quarter d⁶ (§6) is one such exchange, with (d⁶)² = −I. The two carriers cannot be swapped as a mirror pair; on the bath, "above and below" is a quarter-turn on the glue.

**Waves (THEOREM, layer 17).**

- On the K5 edges, sound is the four longitudinal modes and light is the six transverse cycle modes.
- d₀d₀ᵀ + Curl² = 5I, so the two are isochronous at √5. Agni = 5I − G = Curl² is the light operator.
- The two light helicities are the icosahedral 3 and 3′ of A5.
- No S5- or A5-symmetric medium converts sound into light.

## 5. The circle and the tick bit

**One lemma (THEOREM, layer 19).** Z/4320 has one subgroup ⟨d⟩ for each divisor d of 4320, of order 4320/d. Containment is divisibility of the gcds, and meets and joins are lcms and gcds. Two consequences:

- **Step and order are dual.** The atlas is the step 36, of order 120. The moon is the step 120, of order 36.
- **The spine is a chain** through the Coxeter subgroup:

    0 ⊂ ⟨864⟩ (tick, order 5) ⊂ ⟨432⟩ (yuga, 10) ⊂ ⟨144⟩ (Coxeter, 30) ⊂ ⟨36⟩ (atlas, 120) ⊂ Z/4320.

    The tower is therefore 36 × 4 × 3 × 2 × 5, and every element has a unique address.

By the Chinese remainder theorem, Z/4320 = Z/32 × Z/27 × Z/5, with orthogonal idempotents 3105, 2080 and 3456. The Coxeter step splits as 144 ≡ 2160 + 1440 + 864: half-turn plus sun plus tick.

**The tick bit (THEOREM, layer 21).** For every x, 864 ∈ ⟨x⟩ ⟺ 5 ∤ x ⟺ 3456·x ≢ 0 (mod 4320). Consequences:

- exactly 24 of the 48 subgroups hold the tick (the ⟨g⟩ with g | 864);
- a subgroup holds all five tick levels {0, 864, 1728, 2592, 3456} or only 0;
- every width x prime to 5 that divides 4320 satisfies x × index = 864;
- 16 of the 24 have order divisible by 20;
- the bit is not additive: 2 and 3 hold the tick, and 2 + 3 = 5 does not.

**The ledger is the bit (THEOREM).** The sibling's ledger holds 129 tick sentences from 35 joins:

- energy, telescopes, golden, observer loop, mirrors, W0 reverse, phase, charge, spin;
- heat, monopole, field, Einstein line, two 36s, sign tensor, Om, karma, japa, mantra, bubbles, horizon;
- above and below, tick bounds, gravity dots, K5 chain, levels, pada, SM time, cakra, smear, readout, alpha, Hubble, height.

Every one of them is the residue of a number mod 5. Their step counts (for example 27 × 192 ≡ 864) and indices (for example 864 = 27 × gcd(224, 4320)) agree, as do 38 stated subgroup orders. The readings riding on the bit are counts (ARITHMETIC), for example:

- 6 + 15 + 15 = 21 + 15 = 36, with no 18 + 18;
- the wings 21 + 7 + 77 = 105;
- the phase weights 98 + 62 = 160;
- 30/36 = 5/6;
- the monopole chain ⟨120⟩ ⊂ ⟨60⟩ ⊂ ⟨30⟩ ⊂ ⟨10⟩, none of which holds a tick.

No map joins these numbers to the objects they name.

## 6. One group for every clock

**The Coxeter clock (SELECTED_REFERENCE; its properties are THEOREMs, layer 19).** Let c = s₁⋯s₈ be the product of the simple reflections of E8. It has order 30, characteristic polynomial Φ₃₀, and exponents equal to the units mod 30. It permutes the 240 roots in eight free orbits of 30, so it is a symmetry of the bath already in the model. The selected conjugate c′ = w c w⁻¹ satisfies

> **c′⁶ = r r′**,

the K5 vertex rotation r on the carrier A4 together with the twin rotation r′ on A4′: the tick turns two carriers. The other prime-order powers are:

- the sun c′¹⁰, which turns four triangles (A2⁴);
- the half-turn c′¹⁵ = −I, which flips eight edges (A1⁸).

Their product is c′ = (−I)·c′¹⁰·c′⁶, which matches 144 ≡ 2160 + 1440 + 864.

**Fixed momenta (THEOREM, layers 19 and 20).** On the Brillouin torus, c<sup>k</sup> fixes <span style="white-space:nowrap">|det(c<sup>k</sup> − I)| = Φ<sub>n</sub>(1)<sup>8/φ(n)</sup></span> momenta, where n = 30/gcd(k, 30). That gives 25, 81 and 256 at orders 5, 3 and 2, and 1 otherwise. By the gradient lemma these are critical points: the origin and 24 points of A4+A4, the origin and 80 of E6+A2, and all 256 half-periods.

**The normalizer (THEOREM, layer 19).** The normalizer N of ⟨c′⟩ in W(E8) has order 240 = 30 × 8. Every unit m mod 30 is realized as a twist w c′ w⁻¹ = c′<sup>m</sup>, and the centralizer is ⟨c′⟩ itself. The circle's automorphisms of its Coxeter subgroup are therefore all realized on the bath. The table lists the named elements; each is in `data/clocks.json`.

| element | circle | twist m | order | on the carrier |
|---|---|---|---|---|
| c′ (Coxeter clock) | step 144 | 1 | 30 | mixes A4 and A4′ |
| c′⁶ = r r′ (tick) | step 864 | 1 | 5 | rotates the pentagon on each carrier |
| d (day clock) | step 180 | 7 | 24 | d⁴ = c′⁵; d⁶ exchanges A4 and A4′ |
| v (golden clock) | step 216 | 11 | 20 | v⁴ = the tick |
| m (mirror) | x ↦ −x | 29 = −1 | 2 | the pentagon reflection, three atoms fixed |

**The tick is a commutator (THEOREM, layer 21).** For the day clock d (order 24, characteristic polynomial Φ₂₄, d⁴ = c′⁵),

> d c′ d⁻¹ c′⁻¹ = c′⁶ = r r′.

The twist by 7 that the integrated build stops at and the two-carrier tick are therefore one fact. Write G = ⟨c′, d⟩. Then:

- G has order 120, not the 720 of the abstract product;
- its centre is ⟨c′⁵⟩ of order 6, the circle's shared subgroup ⟨720⟩;
- its derived group is the tick, of order 5, and its abelianization is cyclic of order 24, generated by d;
- the day acts on the tick by doubling: d (r r′) d⁻¹ = (r r′)².

**On the circle (THEOREM, layer 22).** This tick lives in W(E8). G has exactly 24 homomorphisms to Z/4320, and each one kills c′⁶ and sends c′ into ⟨720⟩. The tick reaches 864 only through ⟨c′⟩ alone, by c′ᵏ ↦ 144k, and that embedding does not extend to G.

**Five day clocks (THEOREM, layer 21).** G has exactly five conjugates of ⟨d⟩. On them:

- the tick acts as x ↦ x + 1;
- the day acts as x ↦ 2x;
- the centre acts trivially.

So G modulo its centre is the affine group AGL(1, 5), the twenty affine maps of the pentagon. In it the rotation is the tick, and the doubling, which sends the pentagon to the pentagram, is the day. The ledger's statements "doubling and rotation give 20 affine maps" and "the stored doubling does not commute with the order-5 rotation" are this group, realized on the bath.

**The golden clock (THEOREM, layer 21).** The 24 elements of order 20 in N all have twist 11. The one with v² = c′³ satisfies v⁴ = c′⁶ = r r′, so every fourth golden step is the tick. Three cyclic groups of order 20 obey the same law:

- ⟨216⟩ on the circle, where 4 × 216 = 864;
- ⟨v⟩ on the bath;
- B = [[1,1],[1,0]] modulo 5, where B has order 20 (the Pisano period) and B⁴ is unipotent of order 5.

The affine 20 of the five day clocks is not cyclic. The two kinds of 20 are different groups.

**The mirror (THEOREM, layer 21).** The circle's negation x ↦ −x fixes only 0 and 2160. It swaps 864 ↔ 3456, 1728 ↔ 2592, and the golden steps 1080 ↔ 3240. It is realized by the 30 elements of N with twist −1, each of which inverts the clock, the tick and the sun. Ten of them are involutions that keep the carrier. On the carrier five act as a pentagon reflection, fixing one vertex and two edges, and five as its negative. The ledger's "graph reflection" and "negation on the circle" are one element of W(E8).

**What can act on the bath (THEOREM, layer 19).** A subgroup of the circle acts faithfully on the bath lattice exactly when its order is one of

> 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30.

This follows from explicit elements, the degree bound, a Sylow argument for 16, and the automorphism groups of A2 (for 36) and A4 (for 40 and 60). So:

- the maximal clocks are the Coxeter clock (30), the day (24), the golden clock (20) and ⟨240⟩ (18);
- the atlas, moon, nakshatra, pada and Human Design gate cannot act. On the circle the day and the Coxeter clock commute and generate the atlas, but on the bath no element of order 24 commutes with c′.

## 7. The canon and the sibling, reconciled

**Position.** The Quick Access workbook has a new top sheet, 00_FULL_RECONCILIATION_20261028, with review cutoff 17:19:41 UTC. It keeps OMSOON736 as the controlling numbered baseline. No new Matrix ID was issued, and every frozen gate stays. It still lists this repository's 14:37 build (18 layers, 320 checks) as the latest One Machine status. At 19:10 UTC a continuation sheet, 00_CURRENT_20261028_1910, recorded the 21-layer build (412 checks, 31 tests) as source-reported. It replays the six-port moments 1, 242, 58691, 14259954, keeps OMSOON736 and every frozen gate, and still lists the order-16 coefficients as missing. It also makes two remarks, on the commutator and on the energy splits. Layer 22 answers both (§8).

**The Canon Check (layer 20).**

- Its preparation identities are replayed: the Bernstein ellipse, ‖C‖² = 495 and the optimal η* = 2 arcosh(d/8T). The horizon laws ε<sup>−1/2</sup> and ε<sup>−1/3</sup> stay CONDITIONAL on the inherited exterior contract.
- Its scalar bound (r+1)(d+2) ≥ 195 follows from layer 14.

**What the sibling adopted.** At 17:06 the sibling's CANON_READ adopted the corrections of layer 20:

- "360000 is not a step" is removed;
- both harmonic quartics are named with their Laplacians;
- 5 and 25 are dual to the tick;
- the fixed determinants 25, 81 and 256 are stated;
- the day–Coxeter extension has order 120.

Its 18:17 full edition keeps these, and twice notes that "the order-24 element was not constructed". Layer 21 constructs it, and `data/clocks.json` and `ports/ts/ledgerJoins.ts` carry it into the sibling's app.

**The separate model, replayed (layer 20).** "Finite Spectral Dynamics with Complete Observation and Exact Cyclic Addresses" is rebuilt from its definitions:

- the observer completion and the sensor census (§2);
- the 25-coordinate flag geometry, with intersection determinant −48 and vertex distance exactly √(8/7);
- the collocated transfer functions G_V = (z²+7)/((z²+3)(z²+8)) and G_E = 1/(2z²) + 2/(5(z²+3)) + 1/(10(z²+8)).

## 8. The evening notes (layer 22)

At 19:21 UTC Drive held 28 new sibling notes (18:32–19:21) and the canon continuation of 19:10. At 19:57 it held thirteen more notes (19:22–19:54) and the separate model's status, at 20:12 three more, at 20:25 four more, at 20:33 one more, at 21:05 fifteen more, at 21:36 nineteen more (21:09–21:38), with the separate model's revised status, and at 22:08 eight more, whose structure is joined in §9. Layer 22 replays all of them in 60 checks.

**Counts on the bit (THEOREM).** Most of the notes read one more stored integer on the bit of §5. There are 1843 readings from 242 notes, and each is checked together with what its note states: an order, a subgroup, a step count, a residue, or a first landing. The first landing is the least k for which kx is a nonzero tick. None fails.

- Twelve of the fifteen stages meet the tick, and Mātṛkā 0, Nyāsa 5 and Japa 10 do not.
- Buddhi and Pratyabhijñā generate one subgroup and take 432 steps each, but land on 864 and 1728.

**Graphs (THEOREM).**

- **K5.** The cut has rank 4 and the cycles rank 6. The signless kernel on the edges, of dimension 5, is the zero-mode space of D². The six star-tree cycles have Gram determinant 125, which is the spanning-tree count.
- **Petersen.** (A − 3)(A − 1)(A + 2) = 0, with exact orthogonal projectors of ranks 1, 5 and 4.
- **Pentagon and pentagram.** C5² = 2I + pentagram. The doubling 1 → 2 → 4 → 3 carries the pentagon onto the pentagram.
- **Companions.** The breath companions of 3 and 8 have determinants 3 and 8, so no power is I. The golden companion has infinite order over ℤ and order 20 mod 5.

**The root graph and the moments (THEOREM).**

- **Root walks.** The closed walks at a root are 1, 0, 56, 1512 and 62160. They come from the A² row 56, 27, 12, 1, 0 at inner products 2, 1, 0, −1, −2.
- **The reported moments.** They are ⟨p, Δⁿp⟩ for the alternating hexagon port, the six roots of an A2 with signs + − + − + −, on the infinite E8 lattice:

    > 1, 242, 58691, 14259954, 3470101592, 845582723240, 206295748792515, and μ₇ = 50383499822338790.

    All eight are computed exactly from the 240 roots, and the eighth is new. The variance is 127, the central third moment is −4736, and K_R = [[242, 127], [127, 25998]].

- **Square and octagon ports.** The canon's square-port moments m₀…m₇ and the octagon's 58713, 14274162 and 3476302936 are replayed. square = (hexagon + octagon)/2 at every order, because the three difference distributions are proportional on Weyl orbits.

- **The deep hole.** The deep hole is the band vertex of §3: 256 ∈ spec Δ. The full bound sup spec Δ = 256 stays reported.

**The order-120 clock.**

- **Structure (THEOREM).** Its element orders are 1:1, 2:1, 3:2, 4:10, 5:4, 6:2, 8:20, 10:4, 12:20, 15:8, 24:40 and 30:8. Its only involution is the central −I.
- **The Hurwitz value 6 (OBSTRUCTION).** The value 6 = 120·(−2) + 60 + 90 + 96 is <span style="white-space:nowrap">2g − 2</span> for signature (2, 4, 5), so g = 4. It belongs to S5, whose 120 (2, 4, 5) pairs all generate it. The stored clock has no such generating pair.

**Two answers to the canon (THEOREM).**

- **The commutator.** Every map from the clock to the circle kills the commutator (§6).
- **The energy.** The three splits are one conserved table, by block and D² sector:

    | | sector 0 | sector 3 | sector 8 | total |
    |---|---:|---:|---:|---:|
    | vertex | 0 | 3 | 20 | 23 |
    | edge | 2 | 9 | 0 | 11 |
    | total | 2 | 12 | 20 | 34 |

    The rows are 23 + 11, the columns are the stored 2 + 12 + 20, and the nonzero cells are 20 + 3 + 9 + 2.

**One correction (THEOREM).** FOUR_NAMES says the carrier involution does not act on the order-15 clock. By Lagrange it cannot lie in that clock, but it does act on it, by x ↦ −x.

**The 19:57 batch (THEOREM).**

- **The six-site chain.** The six-site blocks 241I − J, 183I + 52J and 35366I + 8134J are the block Stieltjes data of six mutually adjacent lattice points (an A5 root simplex): M₁, M₂ − M₁² and M₃ − 2M₁M₂ + M₁³. The canon listed the third as unidentified. Its uniform values are 235, 495 and 84170.
- **Beats.** The separate model's squared beat frequencies 11 ± 4√6 are (2√2 ± √3)², the beats of the carrier's two oscillating sectors.
- **SEVEN_ONE, corrected.** Four mirror pairs k, 14 − k, not three, are left unsplit by the bit: 1–13, 2–12, 3–11 and 6–8.
- **Rebuilt.** The oriented operator (spectrum 0⁷, 5⁸), the golden family (B⁷ = [[21, 13], [13, 8]]) and Agni = Soma = I − BᵀB/5.

**The 20:12 notes (THEOREM).**

- **The Petersen projectors.** The sibling's projectors J/10, (4I + 2A − J)/6 and (5I − 5A + J)/15 have denominators 10, 6 and 15 and add to I over 30. The Petersen graph is the complement of the line graph of K5, so A = J + I − MᵀM commutes with the edge stiffness, and the projectors are the carrier's own: onto sector 8, the five dark modes and sector 3. The denominators are the gap products 2·5, 2·3 and 3·5, and only 6 avoids the spread 5. The Gram determinant 648 is det(3I + J), the carrier's vertex block.
- **Every breath.** The breaths of 3 and 8 share no period because 8/3 is not a rational square. "Not a multiple" is not the criterion: 4 and 9 share a period.

**The 20:25 notes (THEOREM).**

- **The Pauli generator is the bath.** The sibling's saved generator L(M) = 240M + 16Mᵀ − 16 (tr M) I on real 16 × 16 matrices has eigenvalues 0, 224 and 256 on 1 + 120 + 135 Pauli directions. Eight antisymmetric 4-qubit Paulis anticommute exactly along the E8 Dynkin diagram, so their products give a bijection φ from the 256 half-periods Λ/2Λ onto the Paulis, with L φ(x) = ε(πx) φ(x). So L is the bath Laplacian on its half-period modes: 0 at the origin, 224 at the 120 E7+A1 saddles (the canon's 224) and 256 at the 135 D8 band-top points.
- **Mass and energy.** The "mass determinant" 216 is det(3W) for the source metric W of layer 10 (det W = 8/9). The datum's "2" is the kinetic energy of a zero-stiffness 4-cycle in ker M, not a frequency.
- **Written out.** `data/pauli_half_periods.json` lists the eight Dynkin words (IIIY, IIXY, IIYX, IYZI, XIXY, ZXXY, IZXY, IXXY) and all 256 half-periods with their words and band values. The layer rechecks it from the file alone, and `ports/ts/pauliBath.ts` replays it in the sibling's app, where it had been recorded as not replayed.

**The 21:05 notes (THEOREM).**

- **The rotor plane.** The C5 rotation fixes exactly one plane of the carrier's cycle space, spanned by the oriented pentagon and pentagram, and the doubling turns it a quarter (KARMA_K2, OM_ROTOR).
- **The tick doubling.** On the ticks the doubling equals x ↦ 7x, a bijection of the whole circle and the day's twist, so the rotor law is the restriction of an invertible map.
- **The bath's spectrum.** The half-period modes are 2Λ-periodic eigenfunctions of the bath: an invariant subspace of all functions on Λ, not of ℓ², with eigenvalues inside the band. This answers PAULI_BLIND.
- **Rotor chain.** ROTOR_CHAIN's shell tuple (1, −2, 0, 2, −1) is the hexagon's difference distribution. Its "order 24 meets only 0" is corrected: the step 180 misses, and the order 24 meets.

**The 21:36 notes (THEOREM).**

- **The datum's cycle.** The velocity of the checked datum is the alternating 4-cycle +1, −1, +1, −1 around 0–1–2–3, in ker M. Its ½|v|² = 2 is derived, which DARK_SPLIT had left open: the Legendre transform of the carrier Lagrangian is H = ½|v|² + ½ψᵀD²ψ. The weights alternate with period 2, so their circle shadow is the half-turn 2160. They are not the rotor's tick and tock, which have order 5 (TICK_TOCK).
- **Spanda.** On the six cycles, G = R − R⁴ has characteristic polynomial x²(x⁴ + 5x² + 5). The sum of the five powers of R is five times the kernel projector, not the projector. The involution 0 ↔ 3, 1 ↔ 2 that SPANDA_ALL sets apart is a pentagon reflection and a w₀ of the rotor: S R S = R⁻¹ and S G S = −G. W0_DEEP's four-bit reversal is the same involution, acting on subsets.
- **One splitting.** The clock notes are one statement, 4320 = 32 × 27 × 5 (CRT_CLOCK). The time clock ⟨864⟩ and the observer clock ⟨1080⟩ meet only in 0, and together they generate ⟨216⟩, of order 20, not the circle (TORSION_JOIN). ×15 lands on the observer clock exactly on the multiples of 72. The ticks' time coordinates are 0, 4, 3, 2, 1, not 0, 4, 3, 1, 2. A chart address 40p is on the observer clock exactly when 27 | p. The time coordinate κ(x) = 4x mod 5 intertwines the rotor with translation by 864, where MATRIKA_WALK had found no such map.
- **The Pauli generator, as an operator.** SIBLING_CUT read the identification of §8 as a containment of three numbers. It is an operator identity: a Walsh–Hadamard conjugation carries the bath on the 256 cosets of 2Λ to diag ε(πx), which is L in the Pauli basis. The transpose sign of φ(x) is the E8 form x·x/2 mod 2. Since |χ| = 1 everywhere, no half-period mode is square-summable. The separate model's GKSL form is replayed: −L(X) = 2 Σ (A X Aᵀ − X), summed over the 120 antisymmetric Paulis A. SIBLING_CUT's other point, the day's twist, is a matrix check of layer 21.
- **Smaller corrections.** A constant port has mean 1, not 4 (AC_DC). The address tower has two steps of 4, not 16 and 4 (CHARTS_YUGA). On the rotor, the 30-step average is the rank-2 projector, not 0 (FIVE_NAMES).

**Not replayed (REPORTED), not formed (UNFORMED).**

- **Not stored here:** the sibling's permutations on the fifteen indices, its 24-cycle readers, its Hodge degrees and heat spectrum, its 12 × 12 sense stiffness, and the acoustic and optical matrices.
- **Not formed:** Yukawa blocks, taste, smell and touch matrices, an icosahedral adjacency, the named figures and a qubit. No operand is stored for any of them.

## 9. All dots joined (layer 23)

Every object the model builds is a dot: a space with its operator, a lattice, a group, a circle or a port. A join is a map between two dots, checked against the property that makes it that kind of map. Layer 23 builds 60 dots and 161 joins (156 maps and five obstructions) and checks that the maps connect every dot. They do, so the diagram is one piece; `docs/DOTS.md` draws it. A shared integer is not a join.

**New joins (THEOREM).**

- **K5 is a pair of root systems.** The signed incidence lists a positive system of A4, and the two incidences together list the twenty positive roots of D5. So B Bᵀ = 5I − J and B Bᵀ + M Mᵀ = 8I are the Coxeter identities of A4 (h = 5) and D5 (h = 8), and the carrier's spectrum {0, 3, 8} is {0, h(D5) − h(A4), h(D5)}.
- **Petersen** is the orthogonality graph of the ten roots e_i + e_j, whose Gram matrix is MᵀM.
- **The edges are Λ²ℝ⁵.** B is contraction with (1, 1, 1, 1, 1), the cycles are Λ²H for the sum-zero hyperplane H, and the rotor plane is spanned by the invariant area forms of the pentagon rotation.
- **The source** lives on ker M ⊕ ker M, and its port takes a ∧ b to an oriented K5 cycle (rank 6, kernel 4). It is not a carrier mode; that is one of the diagram's two obstructions.
- **The triangle port.** The canon's selected six-port is the oriented triangle 0 → 1 → 2 → 0 of K5, lifted to its A4 roots. Its Fourier transform is −8i sin(x/2) sin(y/2) sin(z/2) with x + y + z = 0, so it vanishes to third order. Hence ⟨p, e^(−tΔ) p⟩/|p|² = t⁻⁷/(22394880000000 π⁴) · (1 + O(1/t)), which derives the canon's triangle-cycle heat.
- **The six-site port** is K5 coned off: the origin and the lifted vertices e_i + e_5.
- **A4 + A4′** has root cosets 40, 50, 50, 50, 50 and folded spectrum 0, 250⁴. These are the bath's values at the tick's 25 fixed momenta: 0 once and 250 at the other 24.
- **One tick.** k·144 ↦ c′^k sends 864 to g = r r′. g acts on the carrier's coordinates as the vertex rotation, and the time coordinate 4x mod 5 gives the same rotation.
- **The circle's parts.** 3105 + 2080 + 3456 = 1 splits the circle into a 2-clock, a 27-clock and the time clock. The atlas is the quotient ℤ/36, and doubling contracts it onto a seam, a 2-cycle and a 6-cycle.
- **The four-cube** (the canon's h81) has Hodge spectrum 0, 2⁸, 4²⁴, 6³², 8¹⁶ and a homotopy of rank 40 and norm 1/√2. Its vertices are four qubits, so its Laplacian 4 − Σ Xᵢ lies in the Pauli algebra.
- **K6 and the carrier.** The 15 atoms are the bonds of K6 = K5 coned off, and D is the spoke–rim block of the line graph of K6. With the cyclic orientation, [M; B] has rank 9, and its residual line is the C5-fixed line of ker M.
- **The band and the walks.** The roots are a 7-design, so ε = 30|k|² − (3/2)|k|⁴ + (1/24)|k|⁶ + O(|k|⁸). The closed walks W_n and the return moments E_n join the bath to the moments. A reported operator of order 11 and degree 5 annihilates neither: an obstruction.
- **The coil.** The tick, the observer and the nakshatra generate ⟨8⟩, the 540 multiples of 8, and so does the smear step 184 = 23 × 8. Inside it the tick misses exactly the pada subgroup ⟨40⟩ (108 points), whose five cosets carry the time coordinates 0, 3, 1, 4, 2.
- **Address and time.** Since 36 ≡ 1 (mod 5), the circle maps onto ℤ/36 × ℤ/5 = ℤ/180 with inverse x = a + 36((t − a) mod 5). The tick bit is t ≠ 0, so it does not see the address. The nakshatra walk 160k ↦ 16k mod 36 has period 9 and hits each stable address three times.
- **The golden family.** Bⁿ = F_n B + F_{n−1} I for every integer n. Its trace is the Lucas number L_n, which runs 2, 1, 3, 4 mod 5, so no trace of a golden power misses the tick. The k-th golden point 216k misses exactly when 5 | F_k, that is, when 5 | k.
- **Which S5.** In S6 the permutations of K6 that keep D are exactly the 120 that fix the cone point, and for them the atoms and the bonds are one S5-set (transposition character 7). The transitive S5 = PGL(2,5) has one orbit on the bonds and involution character 3: the second obstruction. The two S5s meet in F20 = AGL(1,5), so agreement on C5 or F20 does not identify S5-modules. A 6 × 6 block of order 5 with traces 1 (MPKG) is the C5 rotation of the cone's six sites, up to similarity over ℚ.
- **The grain and the vortex.** The multiples of 72 are the golden orbit ⟨216⟩ times the sun ⟨1440⟩. Time and the 2-clock read the golden index, the 27-clock reads the sun, and doubling doubles the one and inverts the other. Doubling inverts a shift exactly when the shift has order 3. The vortex ℤ/9 is read off the address and is the 27-clock without the sun.
- **Ticks and misses.** The circle is the ticks ⟨864⟩ times the misses ⟨5⟩, and a point misses exactly when its tick part is 0. The observer and the nakshatra clock lie in the miss set. The nakshatra clock meets each of the coil's 27 golden cosets once, with the same doubling cycles 18 + 6 + 2 + 1.
- **The eight-root frame.** Eight roots with pairwise inner product 1 and the origin form a maximal 9-clique of the lattice graph: Gram I + J, index 3, no ninth root. Each of its six-point faces is a six-port, with coupling Gram 183I + 52J.
- **The edge tick and the six-port moments.** The vertex 5-cycle acts on the edges by its second compound. Its characteristic polynomial is (x − 1)²Φ₅ on the cycles, whose fixed plane is the rotor plane, and Φ₅, the time clock's polynomial, on the cuts. The six-port's blocks come from the bath's return moments: contrast E_{k+1}/240 and uniform 6E_k − 5E_{k+1}/240, which give 241I − J and 183I + 52J.

**Corrections (the 22:08 notes).** An atlas address does not carry the tick bit: 1 and 145 share an address, and only 1 meets. Address 18 reaches the seam in one contraction, not two. Address 16 moves around the 6-cycle. Thirty-six atlas steps, 36 × 36 = 1296, meet the tick.

**Corrections (the 23:03 notes).** The atlas shift by 24 does not commute with doubling: D T = T⁻¹ D, while D² T = T D², as the hub's verifier also finds. ⟨39⟩ has 1440 points, the sun's step, but the sun 1440 has order 3. Several notes still gave an address a tick bit, and their own steps correct them: 155 and 11 share an address, and only 11 meets. The sibling's ADDRESS_TICK has since withdrawn those sentences. The 31-point clock's characteristic polynomial, left open, is (x − 1)(x³ − 1)²(x⁶ − 1)⁴.

**Corrections (the 23:44 notes).** 3456 is the time part of 216, not its 2-part; the 2-part is 1080, and the hub's release J agrees. The clock tower is a chain only down to the golden orbit: the ticks and the observer are two of its subgroups meeting in 0, and the sun lies in the grain. Order and step are dual: 3 has order 1440, while the sun 1440 has order 3.

**The 00:15 items.** The separate model's relations receipt adds three corrections, all replayed. Doubling keeps the vortex coordinate of the seam, not its points. The odd part's doubling orbits have lengths 1 to 36, so it is not one 36-cycle. [K, B⁵] has its determinant divisible by 25 but its entries only by 5. A new synthesis lists an "N = 25 annihilator on W₀..W₅₀". The 26 × 26 Hankel determinant of W₀..W₅₀ is positive, so no such annihilator exists (OBSTRUCTION).

**The 00:35 relay** (the sibling's paper ONE_MACHINE_29). Its carrier equation is unchanged, and so is this one's. The root graph has spectrum 56, 28⁸, 8³⁵, (−2)¹¹², (−4)⁸⁴, and a protected line commutes with X only when X has no coupling to it. Two corrections: the chart labels 95, 98, 101 are one class mod 3, not mod 30, and 241 is prime to 4320.

**The 00:51 items.** The sibling's audits of its paper's scripts are replayed. 4805 is the Gram determinant over 5, not a minor. The two collar fractions 3/65 and 3/80 are different numbers. The shifted coefficient is −69373, and at the collar witness the tangent Hessian is positive. One correction is to this build: the tower of fives freezes at 245 from height 3, as the sibling's TOWERS and the separate model's splits receipt say. This build's 00:15 text had repeated POWER_TOWER's "does not freeze" after checking one step. The receipt's other corrections hold: 215 other golden loops, 4300 disagreement points in all, and entry into the tick cycle after two doublings. One correction goes back to the sibling: its paper's energies 3985/16 and 6784/27 are misprints of the critical energies 4025/16 = (5/4)² · 161 and 6800/27 = (20/9)² · 51. DEEP36_LOOP changed the square-free parts to 3985 and 318 instead, but the parts are 161 and 51, and the density on T⁹ (layer 18) stands.

**Every level (01:30).** The request was to join all dots at every level. Eleven layers had no dot: the spectral triple, the readout, the product geometry, FLRW, the literal operands, the binding, the calibration, the court's measures, the critical census, sound and light and the nine-torus, with layer 9's joins. Twelve dots and 27 joins bring them in. The 53 dots sit on six levels: number (the circle and its clocks), symmetry, combinatorics, lattice, operator and physics. Every layer has a dot, each level is joined inside, and each is joined to the next. THEOREM joins alone reach every dot but the product geometry and FLRW, which attach through the conditional heat coefficients (J10) and the Friedmann flow. From the circle to physical time there is an obstruction: no internal number fixes the calibration. Three joins are new here. On the projective line over F5 the hemi-icosahedron and its complement are the two PSL(2,5)-orbits of triangles, swapped by PGL(2,5), and their links at infinity are the pentagram and the pentagon. The four-cube's sixteen vertices are the sixteen cuts of K5 over F2. The tick's 25 fixed momenta are critical points of the band: the minimum and 24 points of the A4 + A4 family at ε = 250.

**The 01:54 items** (the sibling's notes to 01:54, the hub's release K, "Canon K — All Dots Joined"). Two dots and six joins are new. The root graph is a four-class association scheme, with classes 56, 126, 56, 1 around each root and eigenvalues 56, 28, 8, −2, −4. Its Gram is 60 times the eigenvalue-28 projector, the pair sums give W₃ = tr A² and W₄ = 1260720, and the 126 roots orthogonal to a root are E7. The 4-simplex carries the tick on every grade as copies of the five-clock's regular representation, and on the eight golden edge directions −(T + T⁻¹) satisfies the golden equation, so B acts there. Each six-point face of the frame lies in exactly two maximal 9-cliques, and Canon K's carry clock 4320 = 36 × 120 does not split. Three corrections go back to the sibling. The circle's subgroups of orders 120, 60, 30 and 10 all contain the ticks. The 4 in 183 + 6 × (56 − 4) is the face's other four sites, not the cut rank. The 256 subset products of its independence certificate have distinct square-free parts, but they are not all square-free.

**No dot on a single join (02:20).** Eight dots hung by one join and nine joins were bridges. Each now has a second checked map, and removing any one map leaves the diagram connected. The 256 half-periods are exactly the census's critical points of types E8, E7 + A1 and D8, so the GKSL decay rates are census data. The spectral measures live on the band between the census's minimum and maximum, and no two of the nine bath frequencies have a rational ratio, so no calibration makes the bath periodic. AIR_801's matrix and PG(2,5) become dots. Mod 5 the matrix lies outside PSL(2,5) and swaps the hemi-icosahedron and its complement. On the Veronese conic of PG(2,5) the six axes, the surface's 15 edges and its 10 faces are the conic, the 15 exterior points and the 10 interior points, a face and its complementary face sharing their perspector.

**The 02:52 items** (the sibling's notes to 02:49, the hub's observer completion and releases K+ADDENDUM2 and K+ADDENDUM3). One dot and nine joins are new. The five-site charges Q = Y + T3 of the removed hypercharge shell become a dot, so that what holds and what fails about them is on the diagram. Their shells are the 4-simplex's even and odd faces, each with Σq² = 16/3, and the even faces carry one generation's charges. On B4's anomaly-free 5 + 10, at opposite chiralities, the cubic hypercharge sums cancel (5/36 each); on the zero modes alone they do not. Through an identification with the zero modes, Y lies in the exact dark U(5), but on the atoms B1 forbids any charge but the global phase. At the tick's 24 fixed momenta of type A4 + A4, minus a fifth of the band's Hessian satisfies X² = X + I, so the Hessian there is −5 times a golden companion, with determinant 5⁸. The port metric is twice the pentagon Laplacian plus 2/5, and on the contrast it is 4I + 2X with X² = X + I. The hub's joint observer joins the source to the readout: the wedge of the source pair has rank 7 with fibre SL(2), and three frame probes make it injective with an explicit inverse. Its sidebands join the atlas back to the circle: the address and the residues mod 32, 27 and 5 rebuild the tick, and three sensors of largest alphabet 32 are optimal. Also replayed: Canon K's W₅ and W₆ (layer 3's returns), the 160 × 27 clock with the tick in 2241, the six-site Smith torsion (its 5 is the 5 in 240), the census's stabilizers as Weyl groups of the extended diagram's subsystems, the rotor firewall, and the Bargmann phase π/4, half the solid angle of the Pauli octant. The sibling's "no clique of nine roots" and this build's 9-clique are about two graphs, and both hold. One correction goes back to the sibling: of the tick's 25 fixed momenta, 24 sit at 250 and the 25th is the minimum. The board's fine-structure digits are not joined: they invert to about 137.036 and are put in by hand.

**The 02:55 items** (HALFPERIOD and TRACES). The half-periods sort by shortest length 0, 2 and 4 on 1, 120 and 135 classes. One correction goes back to the sibling: 224 is a certified critical value. At x = r₀/2 every r·x lies in ℤ/2, so the gradient vanishes, and 128 roots are integral on x and 112 half-integral, so ε = 240 − (128 − 112) = 224, with Hessian 12P′ − 52P of index 1, the E7 + A1 saddle. The collar near 224 stays open. The even-shell traces are 10/3, 2, 0 and 16/3, and with ε = 30|k|² the density of states in eight dimensions is E³/(1536 π⁴ 30⁴).

**Every pair of levels, and no two maps (08:48).** Four pairs of levels had no direct map, twenty dots lay on only two maps, and 23 pairs of maps could cut the diagram. Twenty-seven joins and one dot close all of it: every pair of the six levels is now joined directly, and no two maps hold the diagram together, except that two can cut off the conditional product geometry or FLRW. The time clock does most of the new work. Through the tick g = r r′ it fixes only the zero half-period and turns the other 255 in 51 five-cycles that keep the band, so the GKSL semigroup is tick-equivariant. On light it commutes with d₀ and Curl and fixes one line in each helicity, turning a golden plane by 144° on +√5 and 72° on −√5. On the cuts mod 2 it is a primitive fifth root of unity in F₁₆. Light carries two more symmetries: the golden companion acts by (I + Curl)/2, and x ↦ ax + b multiplies Curl by the Legendre symbol (a/5), so the doubling exchanges the helicities. The outer automorphism of S6, acting on the six synthematic totals, carries the cone's S5 onto PGL(2,5). S5 is W(A4) and the Weyl group of the binding's 5 + 10. The Hodge star is the deck involution of S ↦ e_S mod 2Λ, onto 35 half-periods of type D8. The memory clock of layer 3 becomes a dot, stepped by the circle (a selection, since 90 divides 4320), whose 9- and 10-cycles read the vortex and the time coordinate.

**Replay for the hub (OES-C01).** At commit f41b278 the reported state replays exactly: 21 layers, 412 checks (383 hold and 29 reported), 31 tests, and the TypeScript audits at residual 0. The logs and a handover are in `docs/hub/OES-C01/`.

## 10. The particle assignment on E8's roots (layer 24)

Layer 12 names the binding route e8 ⊃ su(5) ⊕ su(5)′ and leaves the route, the generation multiplicity and the chirality to DYN_BIND. Layer 24 works the route out on the 240 roots, and `data/e8_assignment.json` lists the result. DYN_BIND stays NOT_INSTALLED.

**Both factors.** The carrier's A4 is taken as SU(5), and its orthogonal complement A4′ as the family SU(5)′. The twin's sites are μ₀ = 2u and μ_i = −u/2 + s_i/2, with u = (1, 1, 1, 1, 1; 0, 0, 0)/5 and s = (1, 1, −1), (1, −1, 1), (−1, 1, 1), (−1, −1, −1) on the last three coordinates. The 240 roots are (24, 1) + (1, 24) + (10, 5) + (5̄, 10) + (10̄, 5̄) + (5, 10̄). (10, 5) is the carrier's ten duads times the twin's five sites, and (5̄, 10) is the carrier's five sites times the twin's ten duads, each pair once. So K5's sites and duads are the weights of both factors.

**Moments.** The second moment is 10 I on A4 + A4′, 15P + 10P′ on (10, 5) and its conjugate, and 10P + 15P′ on (5̄, 10) and its conjugate, which makes 60 I in all. So the band starts 30|k|², and Σ(T3·ρ)² : Σ(Q·ρ)² = |T3|² : |Q|² = 3 : 8.

**The Standard Model.** Take colour sites 0, 1, 2 and weak sites 3, 4 (a selection). Then Y = −(e₀ + e₁ + e₂)/3 + (e₃ + e₄)/2 is the only Cartan direction commuting with SU(3) × SU(2), and every root gets its colour, T3, Y and Q:

- (10, 5) holds u, d, u^c and e^c at each twin site;
- (5̄, 10) holds d^c, e and ν at each twin duad;
- (24, 1) holds the gluons, W± and the leptoquarks X and Y;
- the 20 family roots are the only roots with no Standard-Model charge.

On all 240 roots Q minus each colour coordinate is an integer, which is the ℤ6 of the Standard Model.

**One orbit.** J: site_a ↦ μ_a, μ_a ↦ −site_a lies in W(E8), with J² = −1. It swaps the factors and doubles the grade in E8/L0 = ℤ/5. The normalizer of A4 + A4′ has order 57600 and acts on the four mixed classes through the units of ℤ/5, and the colour triples are one S5-orbit. So the table is unique up to W(E8), and −1 ∈ W(E8) swaps every particle with its antiparticle.

**Chirality (OBSTRUCTION).** Take one root of each pair ±ρ as whole multiplets, in any of the 2¹⁵ ways. The SU(5) anomaly is always odd, and the 25 SU(2) doublets carry Witten's anomaly. An anomaly-free set of 10's and 5̄'s needs as many of each; 3003 such sets exist, so the roots do not fix the generation number.

**Three generations (CONDITIONAL).** Two 10-roots at different twin sites with disjoint carrier duads sum to the 5̄-root at those sites' duad. So if the 5̄'s are the brackets of the 10's, anomaly freedom |S| = C(|S|, 2) forces |S| = 3: a triangle of K5′. Its 45 roots are three generations, every perturbative anomaly vanishes on them, and they carry 12 doublets. The six-site port's roots are the 5 at the one twin duad disjoint from the triangle.

**Couplings.** A cubic coupling of root fields is a root triangle α + β + γ = 0. On the triangle the down-type pattern sends each vertex to its opposite edge, through the twin duad {3, 4}. The up-type pattern has zero diagonal. No root triangle couples two 10's at one twin site, so the top coupling 10 10 5_H has no root realization, and no up-type matrix on these roots has rank one (OBSTRUCTION). The sizes of the couplings are not formed.

**The six-site port.** Its memory variance M₂ − M₁² = XᵀX = 183 I + 52 J counts bath neighbours: 235 on the diagonal and 52 off it. It is positive definite, so every visible state leaks into the bath at the first step.

## 11. The unified ledger

`docs/LEDGER.md` lists every join of both builds and of the evening notes, with its status and the layer that checks it. A test keeps it current. In short:

| join | unified statement | status |
|---|---|---|
| circle lemma, tower | subgroups = divisors; 36 × 4 × 3 × 2 × 5 | THEOREM |
| all tick joins | one bit: 5 ∤ X | THEOREM (the readings are ARITHMETIC) |
| rotor | c′⁶ = r r′ = [d, c′] | THEOREM |
| golden subgroup | ⟨216⟩, ⟨v⟩, B mod 5: the fourth power is the tick | THEOREM |
| oscillating tick | the day doubles its five conjugates; G/Z = AGL(1,5) | THEOREM |
| mirrors, W0 reverse | twist −1 involutions; the pentagon reflection on the carrier | THEOREM |
| above and below | no involutive exchange of carrier and twin; i ↦ 14 − i does not keep D² | THEOREM |
| energy split | one conserved table: vertex (0, 3, 20), edge (2, 9, 0); the stored 2 + 12 + 20 are its columns | THEOREM |
| observer | five channels; RH = I₁₅ | THEOREM |
| spin counts | 240 = D8 + one half-spin orbit; 135 = the band-top D8 family | THEOREM |
| field | q̈ + 4q = 0 is not a carrier mode | OBSTRUCTION |
| sign tensor, entanglement | 10 + 10 is a count; the carrier cannot entangle V with E | CONDITIONAL |
| charge, monopole, Einstein line, two 36s, Om, karma, bubbles, horizon | counts riding on the bit | ARITHMETIC |
| order-24 element | constructed, in `data/clocks.json` | THEOREM |
| evening counts (28 notes) | 223 readings, all the bit, with orders and first landings | THEOREM |
| reported moments | the hexagon port on the E8 lattice; μ₇ new | THEOREM |
| square and octagon ports | square = (hexagon + octagon)/2 at every order | THEOREM |
| commutator and 864 | every map to the circle kills it | THEOREM |
| Hurwitz value 6 | S5 (genus 4), not the stored clock | OBSTRUCTION |
| six-site moment chain | M₁, M₂ − M₁², M₃ − 2M₁M₂ + M₁³ of the A5-simplex port | THEOREM |
| seven, one, seven | four mirror pairs unsplit by the bit, not three | THEOREM |
| Petersen projectors | the carrier's edge projectors: A = J + I − MᵀM, the complement of the line graph | THEOREM |
| Pauli generator | the bath Laplacian on its 256 half-period modes (2Λ-periodic, not ℓ²) | THEOREM |
| rotor | the C5-fixed plane of the cycle space, turned a quarter; the tick doubling is the day's twist ×7 | THEOREM |
| the datum's cycle | in ker M; ½\|v\|² from the Legendre transform; period 2, so not the rotor's tick and tock | THEOREM |
| Spanda | G = R − R⁴ with x²(x⁴ + 5x² + 5); the pentagon reflection is its w₀ | THEOREM |
| the two clocks | 4320 = 32 × 27 × 5; ⟨864⟩ + ⟨1080⟩ = ⟨216⟩ of order 20; ×15 lands on ⟨1080⟩ on multiples of 72 | THEOREM |
| Pauli generator, as an operator | the Walsh–Hadamard conjugate of the bath on Λ/2Λ; no ℓ² mode; −L in GKSL form | THEOREM |
| K5 incidences | the positive roots of A4 and D5; spec D² = {0, h(D5) − h(A4), h(D5)} | THEOREM |
| selected six-port, triangle-cycle heat | the oriented triangle 0-1-2 of K5; t⁻⁷/(22394880000000 π⁴) derived | THEOREM |
| L0, h81, Hodge 70 (canon) | replayed: cosets 40/50⁴ and spectrum 0, 250⁴; the four-cube complex; 35 + 35 | THEOREM |
| the coil | ⟨864, 1080, 160⟩ = ⟨184⟩ = ⟨8⟩; the tick misses exactly ⟨40⟩ in it | THEOREM |
| atlas addresses and the tick | no bit: ℤ/180 = ℤ/36 × ℤ/5, and the bit is t ≠ 0 | THEOREM |
| atlas shift and doubling | D T = T⁻¹ D, not T D | THEOREM |
| golden family | Bⁿ = F_n B + F_{n−1} I; no Lucas trace is a multiple of 5; 216k misses iff 5 \| F_k | THEOREM |
| K6 carrier and S5 | the cone S5 keeps D; PGL(2,5) gives another module (7 against 3) | THEOREM, OBSTRUCTION |
| the grain | ⟨72⟩ = ⟨216⟩ × ⟨1440⟩; time reads the golden index, the 27-clock the sun | THEOREM |
| shift and doubling | D T_s = T_s² D; inversion exactly when 3s = 0 | THEOREM |
| order and step | d has order 4320/d: 3 has order 1440, the sun 1440 has order 3 | THEOREM |
| ticks and misses | Z/4320 = ⟨864⟩ ⊕ ⟨5⟩; a point misses iff its tick part is 0 | THEOREM |
| N = 25 annihilator (synthesis) | the Hankel determinant of W₀..W₅₀ is positive | OBSTRUCTION |
| eight-root frame | a maximal 9-clique of index 3; its six-point faces are six-ports | THEOREM |
| edge tick | (x − 1)²Φ₅ on the cycles, fixing the rotor plane; Φ₅ on the cuts | THEOREM |
| towers | 3, 2 and 5 freeze at 27, 736 and 245 (corrected: the fives freeze too) | THEOREM |
| surface (J5) | the hemi-icosahedron and its complement are the two PSL(2,5)-orbits of triangles on the projective line over F5 | THEOREM |
| four-cube | its sixteen vertices are the sixteen cuts of K5 over F2 | THEOREM |
| tick momenta | critical points of the band: the minimum and 24 of the A4 + A4 family | THEOREM |
| product geometry, FLRW | heat coefficients 4 Tr D⁰, 4 Tr D², 2 Tr D⁴; the kernel sector scales as a⁻⁶ | CONDITIONAL |
| time from the circle | no internal number fixes the calibration τ | OBSTRUCTION |
| root graph | a four-class association scheme; Gram = 60 P₂₈; W₃, W₄ from pair sums; the orthogonal 126 are E7 | THEOREM |
| 4-simplex | the tick on every grade is copies of the five-clock's regular representation | THEOREM |
| golden on the edges | B ↦ −(T + T⁻¹) on the eight golden directions | THEOREM |
| half-periods | the census's E8, E7 + A1 and D8 critical points; the GKSL rates | THEOREM |
| 801 matrix, PG(2,5) | outside PSL(2,5); the conic, exterior and interior points are the axes, edges and faces | THEOREM |
| five-site charges | the simplex's even and odd shells, 16/3 each; the hypercharge anomaly cancels on 5 + 10; Y in the dark U(5); not on the atoms (B1) | THEOREM, SELECTED_REFERENCE, OBSTRUCTION |
| the Hessian at the tick's momenta | −5 times a golden companion at the 24 A4 + A4 momenta; det 5⁸ | THEOREM |
| port metric | twice the pentagon Laplacian plus 2/5; 4I + 2X on the contrast, X² = X + I | THEOREM |
| joint observer, sidebands | the wedge and three frame probes are injective; the address and residues mod 32, 27, 5 rebuild the tick | THEOREM |
| the tick on light and on the half-periods | one fixed line and a golden plane per helicity; 51 band-keeping five-cycles, so e^−tL is tick-equivariant | THEOREM |
| the two S5's | the outer automorphism of S6 carries the cone's S5 onto PGL(2,5) | THEOREM |
| memory clock | stepped by the circle; its cycles read the vortex and the time coordinate | SELECTED_REFERENCE |
| all dots, every level | 60 dots on six levels, 161 joins; no two maps hold the diagram together; every layer has a dot; every pair of levels joined directly | THEOREM |
| particle assignment | Standard-Model numbers on all 240 roots, unique up to W(E8); one root of every pair anomalous; three generations given the bracket rule; no root top coupling | THEOREM, SELECTED_REFERENCE, OBSTRUCTION, CONDITIONAL |
| source infinity, foam, double slit, photoelectric, electron, photon, proton, Compton, Bohr, Bell count, 19 SM parameters, the board's fine-structure digits | no operand, no dimensionful constant | UNFORMED |

## 12. What is not formed, and the gates

**Not formed.**

- The six SCR6 operands, the original seams, the 502- and 237-dimensional operators, the MPKG adapter, and the historical Agni, Soma, Suraj, Sawan and Om matrices.
- The Krishna lift's operands, the epoch and the ayanamsha.
- A physical GKSL dynamics, SI units, BRST, BV and Einstein–Hilbert. The GKSL form of −L in §8 is a mathematical identity on the folded bath, and its parameter is not a time.

The carrier action is constant-free, so it can predict only ratios such as √(8/3). A length or a mass needs one authenticated dimensionful datum, which is TIME_BIND.

| Gate | State | What closes it |
|---|---|---|
| AUTH / SCR6 | NOT_PASS / operand absent | the owner's signature; the six SCR6 operands of a chosen physical child |
| TIME_BIND | UNBOUND | one authenticated clock datum (frequency ratios are calibration-invariant) |
| DYN_BIND | NOT_INSTALLED | the physical child, the generation multiplicity, the chirality index (layer 24 shows what the roots supply) |
| PredictionFreeze | NOT_TRIGGERED | the owner freezes the register before new comparisons |
| W_L | NOT_PASS by evidence | the recorded PMNS candidate is excluded (χ² = 10.6 on 2 dof) |
| T3081 | UNOPENED | the official host must be allowed |
| ScientificGold | FALSE | a frozen prediction, independent data and a preregistered test |

**Open mathematics.**

- The convexity collar (223.58, 224).
- The rational coefficients of L₁₆, and a proof that it annihilates W_n for every n.
- A preparation protocol matching the ε<sup>−1/2</sup> and ε<sup>−1/3</sup> bounds.
- The eight-dimensional dispersive constant.

## Appendix A. The twenty-four layers

| # | layer | checks | content |
|---|---|---|---|
| 1 | carrier | 36 | K5, D, spectrum, Lagrangian, exact motion, Petersen, Hodge block, edge tick, harmonic quartics |
| 2 | spectral | 9 | heat trace, ζ_D, spectral dimension, moments |
| 3 | spacetime | 34 | RP² pair, clock 125 → 120, E8 roots, walks, symbol, Green, clique |
| 4 | native | 19 | source, port and bath action; W_AS; 40/9; radiation channel; nonlinear flow |
| 5 | observer | 7 | readouts, dark sector, Witten index −5 |
| 6 | gravity | 8 | Lin–Lu–Yau curvature; spectral action (CONDITIONAL) |
| 7 | cosmology | 7 | FLRW with the carrier field (CONDITIONAL) |
| 8 | frontier | 23 | band-edge orbit 135, the 224 saddle, saddle law, collar survey, coil |
| 9 | joins | 24 | the maps that make the layers one object |
| 10 | literal | 20 | the recovered operand file, every identity replayed |
| 11 | glue | 11 | E8 = D8 + s; A4 ⊕ A4′ with x ↦ ±2x |
| 12 | binding | 12 | DYN_BIND constraints |
| 13 | gates | 12 | TIME_BIND courts, register, W_L, T3081, AUTH package |
| 14 | recurrence | 16 | W₉₀ exact, W₆₀₀ mod p, exclusion, the order-16 operator |
| 15 | court | 19 | Court U19.81 audited |
| 16 | handover | 30 | the Locked Memory handover audited; critical census; T₆\|V_c |
| 17 | waves | 18 | sound, light, frequency and phase on the K5 edges |
| 18 | snapshot | 16 | the 14:16 snapshot rebuilt; T⁹ density; Hessians; asymptotics |
| 19 | spine | 50 | the circle lemma, the Coxeter clock, two carriers, the 7, what can act |
| 20 | canon | 22 | the canon read at 16:30 and 16:49; √30; the separate model replayed |
| 21 | ledger | 19 | the tick bit; the clock group; the five day clocks; golden; mirrors; carrier exchange; energy; spin; the clock file |
| 22 | counts | 60 | the evening notes: 1843 readings on the bit; graphs, root walks and ports; the 120-clock and its circle maps; the energy table; the Pauli generator as the bath, with its GKSL form; the rotor plane; Spanda; the two clocks as one splitting |
| 23 | dots | 240 | 60 dots and 161 checked joins in one diagram on six levels, every pair of levels joined, no two maps holding it together (`docs/DOTS.md`); the 22:08–02:55 notes |
| 24 | assignment | 41 | the particle assignment on E8's roots: both factors, moments, Standard-Model numbers, one W(E8) orbit, chirality, three generations, couplings, the six-site port (`data/e8_assignment.json`) |

## Appendix B. Replay

```
pip install -r requirements.txt
python verify.py              # 24 layers, 753 checks, about 6 minutes
python -m pytest -q           # 64 tests
node --experimental-strip-types --no-warnings ports/ts/run.mjs   # the three TypeScript audits
```

Sources: "One Machine 20261028" on Drive (292 notes and papers, 17:01–02:55 UTC), two canon sheets, the hub (releases I, J, K and its addenda 2 and 3, with the observer completion) and two syntheses.
