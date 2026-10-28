# One Machine: the unified edition

**OES end-to-end model, 28 October 2026.** This edition puts the whole model in one text with one ledger. It brings together the verified build (layers 1–18), the integrated spine (layer 19), the canon synchronization (layer 20), the sibling's 28 October ledger of joins (layer 21), and the sibling's evening notes with the canon's 19:10 continuation (layer 22). It is a selected mathematical build replayed from matrices. It is not a source admission and not a change to the canon matrices.

**AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND · DYN_BIND = NOT_INSTALLED · SCR6 = NOT_RUN_OPERAND_ABSENT · PredictionFreeze = NOT_TRIGGERED.** No gate moves, and no term is added to the action.

**Custody.**

- Repository `sachinkaria24-byte/OES`, branch `claude/lagrangian-spectral-spacetime-model-t2253b`.
- `python verify.py` replays 22 layers in **462 checks**. Of these, 422 hold: THEOREM 299, OBSTRUCTION 41, ARITHMETIC 37, CONDITIONAL 17, UNFORMED 18, SELECTED_REFERENCE 8, REMOVED 2. The other 40 are REPORTED records.
- `python -m pytest` runs 39 tests.
- `ports/ts/` holds three drop-in audits for the sibling's app (41 rows, residual 0). `data/clocks.json` holds the explicit clock matrices, and `docs/LEDGER.md` holds the unified ledger.
- This text supersedes `one-machine-20261028-verified.pdf` (layers 1–18) and `one-machine-20261028-spine.pdf` (layers 19–20) as the current paper. Both stay in `docs/paper/` as history.

## Abstract

The model has one datum, the signless incidence of K5. It has one action, fifteen oscillators with stiffness D², and one bath, the E8 root lattice. Everything else is a map between these three objects, a count, or a gate. This edition does four things.

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
| clocks | the normalizer of ⟨c′⟩ in W(E8), order 240 | every circle unit realized; the tick = [day, Coxeter] | 19, 21 |
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

At 19:21 UTC Drive held 28 new sibling notes (18:32–19:21) and the canon continuation of 19:10. At 19:57 it held thirteen more notes (19:22–19:54) and the separate model's status, at 20:12 three more, at 20:25 four more, at 20:33 one more and at 21:05 fifteen more. Layer 22 replays all of them in 50 checks.

**Counts on the bit (THEOREM).** Most of the notes read one more stored integer on the bit of §5. There are 486 readings from 63 notes, and each is checked together with what its note states: an order, a subgroup, a step count, a residue, or a first landing. The first landing is the least k for which kx is a nonzero tick. None fails.

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

**Not replayed (REPORTED), not formed (UNFORMED).**

- **Not stored here:** the sibling's permutations on the fifteen indices, its 24-cycle readers, its Hodge degrees and heat spectrum, its 12 × 12 sense stiffness, and the acoustic and optical matrices.
- **Not formed:** Yukawa blocks, taste, smell and touch matrices, an icosahedral adjacency, the named figures and a qubit. No operand is stored for any of them.

## 9. The unified ledger

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
| source infinity, foam, double slit, photoelectric, electron, photon, proton, Compton, Bohr, Bell count, 19 SM parameters | no operand, no dimensionful constant | UNFORMED |

## 10. What is not formed, and the gates

**Not formed.**

- The six SCR6 operands, the original seams, the 502- and 237-dimensional operators, the MPKG adapter, and the historical Agni, Soma, Suraj, Sawan and Om matrices.
- The Krishna lift's operands, the epoch and the ayanamsha.
- GKSL, SI units, BRST, BV and Einstein–Hilbert.

The carrier action is constant-free, so it can predict only ratios such as √(8/3). A length or a mass needs one authenticated dimensionful datum, which is TIME_BIND.

| Gate | State | What closes it |
|---|---|---|
| AUTH / SCR6 | NOT_PASS / operand absent | the owner's signature; the six SCR6 operands of a chosen physical child |
| TIME_BIND | UNBOUND | one authenticated clock datum (frequency ratios are calibration-invariant) |
| DYN_BIND | NOT_INSTALLED | the physical child, the generation multiplicity, the chirality index |
| PredictionFreeze | NOT_TRIGGERED | the owner freezes the register before new comparisons |
| W_L | NOT_PASS by evidence | the recorded PMNS candidate is excluded (χ² = 10.6 on 2 dof) |
| T3081 | UNOPENED | the official host must be allowed |
| ScientificGold | FALSE | a frozen prediction, independent data and a preregistered test |

**Open mathematics.**

- The convexity collar (223.58, 224).
- The rational coefficients of L₁₆, and a proof that it annihilates W_n for every n.
- A preparation protocol matching the ε<sup>−1/2</sup> and ε<sup>−1/3</sup> bounds.
- The eight-dimensional dispersive constant.

## Appendix A. The twenty-two layers

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
| 22 | counts | 50 | the evening notes: 486 readings on the bit; K5, Petersen and its projectors, pentagon; root walks; the hexagon, square, octagon and six-site ports; the 120-clock; circle maps; the energy table; beats; mirror pairs; breaths; the Pauli generator as the bath, written out; the rotor plane; two Laplacians and the line graph |

## Appendix B. Replay

```
pip install -r requirements.txt
python verify.py              # 22 layers, 462 checks, about 4 minutes
python -m pytest -q           # 39 tests
node --experimental-strip-types --no-warnings ports/ts/run.mjs   # the three TypeScript audits
```

Sources: the Drive folder "One Machine 20261028" (the sibling's full edition, `FULL_UPDATE_20261028.md` and 104 notes of 17:01–21:03 UTC) and the canon sheets 00_FULL_RECONCILIATION_20261028 and 00_CURRENT_20261028_1910.
