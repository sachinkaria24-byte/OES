# One Machine: the verified build

**OES end-to-end model, 28 October 2026.** This is a selected mathematical build, replayed from matrices. It is not a source admission and not a change to the canon matrices.

**AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND · DYN_BIND = NOT_INSTALLED · SCR6 = NOT_RUN_OPERAND_ABSENT · PredictionFreeze = NOT_TRIGGERED.** No gate moves.

**Custody.**

- Repository `sachinkaria24-byte/OES`, branch `claude/lagrangian-spectral-spacetime-model-t2253b`.
- `python verify.py` replays all 18 layers: **320 checks**. Of these, 300 are statements that hold: THEOREM 214, ARITHMETIC 26, OBSTRUCTION 22, CONDITIONAL 15, UNFORMED 15, SELECTED_REFERENCE 6, REMOVED 2. The other 20 are REPORTED: they are recorded, not counted.
- `python -m pytest` runs 22 tests.

## 0. What this build adds

The 14:16 snapshot (`one-machine-20261028.pdf`, `oes-model-20261028.zip`) checks its joins by comparing typed constants (`251 === 251`). Here every statement is computed from explicit matrices by a check that can fail. On top of everything the snapshot covers, this build proves:

1. **The scalar walk recurrence, formed.** W₀…W₉₀ are exact from two independent engines, and W₀…W₆₀₀ are known modulo primes. The annihilator is one shift operator of **order 16 and degree 58**, the same mod four primes. Built from W₀…W₅₀₀, it predicts W₅₀₁…W₆₀₀. Its characteristic polynomial factors exactly over ℚ.
2. **The band and the walks agree.** The 11 critical families of the E8 band (243,600 points, Morse sum 0) have exactly the 11 in-band characteristic roots of that operator as their values.
3. **Density on the nine-torus.** The nine positive bath energies have distinct square-free parts, so their frequencies are linearly independent over ℚ and their flow is dense on T⁹. The snapshot left this open.
4. **All eleven Hessians.** Recomputing them reproduces every coherent coefficient the snapshot prints. The snapshot said they were not recomputed.
5. **The walk asymptotics.** W_n = (16/π⁴)·240ⁿ·n⁻⁴·(1 − 2/n + (23/15)/n² + O(n⁻³)), derived from the 7-design moments alone and followed by the exact W₅₀…W₉₀.
6. **Sound, light, frequency and phase on the K5 edges.** The Hodge Laplacian is 5·I, so sound and light share one frequency. The canon's Hodge block A is the curl, and the two light helicities are the icosahedral 3 and 3′. Agni = 5I − G is the light operator Curl².
7. **The literal five-dimensional operand.** The printed chart T₆ preserves the contrast lattice V_c. T₆|V_c is a 5×5 integer operator with determinant 31, which explains 155 = 5 × 31.
8. **Corrections** to the snapshot, the Locked Memory handover and Court U19.81 (§6).

## 1. The carrier and its Lagrangian (layers 1–3)

- The carrier has 15 atoms, the 5 vertices and 10 edges of K5. M is the signless incidence, and D = [[0, M], [Mᵀ, 0]].
- **spec D² = {0⁵, 3⁸, 8²}**, with Tr D² = 40 and Tr D⁴ = 200. The kernel ker D = P5 is the 5-dimensional irreducible [3,2] of S5.
- The Lagrangian is S = ∫ ½|ψ̇|² − ½⟨ψ, D²ψ⟩, with no other term. The frequencies are 0, √3 and 2√2. Their squared ratio 8/3 is not a rational square.
- The signed boundary B (the canon's `boundary_oriented`) satisfies MMᵀ + BBᵀ = 8I: the carrier's vertex frequencies are the complements of the sound frequencies (§4).
- The E8 bath is Δ = 240I − A on the root lattice. Its band is [0, 256], its long-wave dispersion is ε(k) = 30|k|² − (3/2)|k|⁴ + (1/24)|k|⁶ + O(|k|⁸) (exact, from the 7-design), and its sound speed is √30.

## 2. The native action and the operands (layers 4, 10–12)

- **Source.** q = (a, b) ∈ P5 ⊕ P5, with M_s = diag(W/4, W/4). At the origin the source obeys **q̈ + 4q = 0**, so ω₀ = 2.
- **Port.** g = W_AS(a ∧ b), a quadratic map onto the 6-dimensional cycle space L6. The sharp quartic constant is Q₄ ≤ (40/9)ρ², and it is attained.
- **Bath.** The six-site clique has A_bb = 235P_u + 241P_c and BB* = 183P_c + 495P_u.
- **Literal operands.** The native file (SHA-256 73e07429…) was recovered, and every canon identity on it replays. The literal port, in edge coordinates (`Fedge_native_inverse · WAS_native`), is S5-equivariant.
- **The printed 6×6 chart T₆** (det 155):
    - Every column sums to 5, so T₆ preserves V_c = {x ∈ ℤ⁶ : Σx = 0}.
    - On V_c it is the integer matrix [[1,−1,1,0,−1], [1,−1,3,−2,−2], [1,−2,4,−3,0], [1,0,3,−1,0], [2,0,1,−1,0]], with det 31 and irreducible characteristic polynomial x⁵ − 3x⁴ + 12x³ − 20x² + 31x − 31. This is the candidate for the missing five-dimensional operand; the owner must confirm it.
    - The largest |cofactor| is 68. 4805 = cofactor₄₄(TTᵀ) = 21² + 48² + 43² + 11² + 3² + 9², a sum of squared cofactors and not a minor.
    - The handover's "literal" T5×5 = (2I₄ − C_A4) ⊕ [5] is a construction: it is not in the file and not a block of T₆.
- **Glue.** E8 ⊃ A4 ⊕ A4′ has index 5, with glue x ↦ ±2x. The carrier's atoms are the A4 shadows of the 200 mixed roots, and 248 = (24,1) + (1,24) + four bifundamentals.
- **Binding constraints.**
    - The only atom-diagonal symmetry of D is the global phase. ker D carries an exact U(5).
    - The port breaks the dark O(5) completely. The minimal anomaly-free completion is 5 + Λ²5 = 15 states, which is one generation per carrier.
    - The generation multiplicity is an operand of DYN_BIND.

## 3. The walk recurrence and the band geometry (layers 14, 16, 18)

**Data.**

- The Weyl-orbit DP gives exact integers W₀…W₉₀. All 56 canon values W₀…W₅₅ are reproduced.
- A second engine uses E8 = D8 ∪ (D8 + s) and λ = 4e₂(c) + 128∏cos(θᵢ/2) + 128∏sin(θᵢ/2), with Hermite–Gauss quadrature over F_p. It gives W₀…W₆₀₀ mod two primes and W₀…W₅₀₀ mod two more.
- The two engines agree on all 91 exact terms.

**Exclusion and the operator.**

- Every recurrence with (r+1)(d+2) ≤ 455 is excluded. In particular, order 11 needs degree ≥ 49.
- The first kernels appear at shape (23, 17). That kernel is 2-dimensional mod both 600-term primes, with 146 surplus equations.
- The greatest common right divisor of the kernel operators is one operator **L₁₆, of order 16 and degree 58**, the same mod four primes.

**Characteristic polynomial (exact over ℚ).**

> (z−240)(z−16)(z+3)(z+8)(z+10)(z+11)(z+185/16)(z+320/27)(z+12)²(z+16) · (z−340)(z+660)(z+20)(z+35)(z+120/7)

The local exponent is −4 = −dim/2 at every simple root, and the indicial polynomial at −12 is (α+4)(α+5). The first factor group contains the 11 roots in the band [−16, 240]; it is the sibling's "order 11 with (x+12)²". The five roots outside the band are why the operator has order 16.

**The critical census (vertices and edges of the alcove).** The table lists λ = 240 − ε, the number of points, the Morse index of ε, and the exact det of the Hessian of ε:

| family | λ | points | index | det H |
|---|---|---|---|---|
| E8 | 240 | 1 | 0 | 60⁸ |
| E7+A1 | 16 | 120 | 1 | −2¹⁶·3⁷·13 |
| E6+A2 | −3 | 2,240 | 2 | 2⁶·3⁸·7² |
| D5+A3 | −8 | 15,120 | 3 | −2¹⁶·3³ |
| A4+A4 | −10 | 48,384 | 4 | 5⁸ |
| A5+A2+A1 | −11 | 80,640 | 5 | −2⁶·3⁷ |
| A6+A1 (edge) | −185/16 | 69,120 | 6 | 3⁷·5¹⁵/2³⁰ |
| A7 (edge) | −320/27 | 17,280 | 7 | −2¹⁶·5¹⁵/3²³ |
| A7+A1 | −12 | 8,640 | 7 | −2¹⁶ |
| A8 | −12 | 1,920 | 8 | 3⁸ |
| D8 | −16 | 135 | 8 | 2¹⁶ |

- In total there are 243,600 points, and the alternating sum Σ(−1)^index·points = 0 = χ(T⁸).
- The coherent coefficients points · i^index / √|det H| reproduce the snapshot's printed values. The 11 values of λ are exactly the in-band characteristic roots above: band geometry and walk data are one statement.
- The band has no critical value in (0, 224).

**Asymptotics.** At the maximum, log(1 − ε/240) = −s/8 − s²/640 − s³/23040 with s = |k|². Laplace's method then gives

> W_n = (16/π⁴) · 240ⁿ · n⁻⁴ · (1 − 2/n + (23/15)/n² + O(n⁻³)).

The exact W₅₀…W₉₀ follow it. The residual ((R_n − 1 + 2/n)n² − 23/15) falls from −0.0069 at n = 50 to −0.0038 at n = 90.

**Density on T⁹.**

- The nine positive critical energies are 224, 243, 248, 250, 251, 4025/16, 6800/27, 252 and 256 (the two families at 252 share one).
- Their frequencies √ε have the distinct square-free parts 14, 3, 62, 10, 251, 161, 51, 7, 1.
- By Besicovitch these square roots are linearly independent over ℚ. By Kronecker, the joint flow is dense on the nine-torus.

## 4. Sound, light, frequency and phase on the K5 edges (layer 17)

The edges carry one exact Hodge complex: the gradient d₀ = Bᵀ, and the curl Curl = ⋆d₁ through the ten triangles and the Hodge star of the 4-simplex.

- **Sound** is im d₀, the 4 longitudinal modes. Its operator BBᵀ = 5I − J = ½Σ_{A4} ααᵀ is the long-wave Hessian of the carrier's own root lattice.
- **Light** is ker d₀ᵀ, the 6 transverse modes. This is the cycle space L6, the port space. Curl is symmetric with eigenvalues ±√5 on light. In the canon's fundamental-cycle basis it is **exactly −A**, the Hodge block of layer 1.
- **Frequency.** d₀d₀ᵀ + Curl² = 5·I₁₀, so sound and light are isochronous at √5.
- **Agni.** Agni = 5I − G = Curl² is the light operator, and G = BᵀB is the sound operator.
- **Phase.**
    - Sound carries the C5 phases ±72° and ±144°, and none at 0.
    - The two helicities are swapped by odd permutations. Under A5 they are the icosahedral 3 and 3′, with 5-cycle characters 1 − φ and φ; sound is the A5 4.
    - No S5- or A5-symmetric medium turns sound into light. The C5 clock allows exactly 4 phase-matched parameters, and the phase-0 light modes stay dark.
    - With a C5 coupling, conversion is resonant and complete (CONDITIONAL).
- **The chain.**
    - The dark source at ω = 2 drives light through the quadratic port at 0 and 4, doubling frequency and phase. The port's kernel is the A5 4.
    - The adapter carries light to the boundary. There the bath takes it as sound in the smooth acoustic window, at k ≈ 0.740, with phase and group velocities 0.986 and 0.959 of √30.
    - On the carrier's plane the bath speed² splits as 30 = 5 (A4) + 25 (the mixed roots).
- **Frequency ladder.** 0 < √3 < 2 < √5 < 2√2 < 4 < √224 < 16.
    - The squares 3, 4, 5, 8, 16 divide 4320, and no bath energy does.
    - 4b² = 5a² has no solution, so the source and sound frequencies are incommensurable.

Making "sound" and "light" physical needs DYN_BIND and TIME_BIND. The invariant content is the set of ratios.

## 5. The 14:16 snapshot, rebuilt (layer 18)

- **Agni–clock–doubling.** Agni = Curl², as in §4. The edge doubling T (10×20) has TTᵀ = 2I, is isotropic for the pair signature, and has rank BT = 4.
- **Five-port site block** (SELECTED_REFERENCE): masses 1 and 3, springs [[2,−1],[−1,2]].
    - Its moments are 0, 0, 0, 1/3, 0, −8/9, 0, 55/27, with recurrence H_{k+4} + (8/3)H_{k+2} + H_k = 0.
    - Its controllability determinant is −1/3 and its observability determinant −1/27.
    - Its Hankel determinant is 1/81 (6561 cleared), and its frequencies² are (4 ± √7)/3.
- **Cube.**
    - The eight labels 580…079 form the 3-cube, with Laplacian spectrum 0, 2³, 4³, 6.
    - The middle operator L(6I − L) satisfies M² = 8M and has rank 6.
    - The reader pair sees ranks 2 then 4; four third readers reach 6.
    - The decoder has det −1, with noise gains 46 and 66.
- **Spanda** on the 31 subsets: 7 fixed, 24 moved, traces 31, 7, 31, 7, and trace-Hankel determinant 912. On the K5 edges the same double transposition keeps both helicities, with traces 0 on sound and −1 on each helicity.
- **4320-circle.** The day (order 24) and the pada (order 108) meet in the order-12 step, and the order-5 rotor misses the day.

## 6. Corrections to circulating documents

- **14:16 snapshot.**
    - (I + S)/2 is a Markov projector of rank 19 (7 fixed subsets plus 12 symmetrized pairs), not "onto those 7 forms".
    - The front table's "the recurrence order is 11" should read: order 16, with an in-band part of degree 11.
    - Its "not replayed" items (density on T⁹, the Hessians) are settled above.
- **Locked Memory handover.**
    - The "15-edge K6 carrier" is the 15 atoms of K5.
    - An order-11, degree-5 exact recurrence is excluded. P25 annihilates only the quadrature sequence.
    - (15/13)r² should be (15/16)r².
    - "ker O ⊆ ker C" is reversed.
    - "H90 identified" is unsupported.
    - "Multi-frequency criterion verified" is true only as rebuilt.
    - The "literal" T5×5 is a construction.
    - The paper digest b5590733… matches none of the three One Machine PDFs on Drive (77fc5845…, ce509d99…, 714db33d…).
- **Court U19.81.**
    - The walk generator is wrong from W₄ on.
    - Its moment sequences are not positive definite.
    - Its uniform-sector moment formula is wrong.
    - Its Loewner certificate fails on the true moments.
    - Its 2-parameter clock reduction is impossible for the V₂ it names.

## 7. Gates

| Gate | State | What closes it |
|---|---|---|
| AUTH / SCR6 | NOT_PASS / operand absent | the owner's signature on the packaged antichain; the six SCR6 operands of a chosen physical child |
| TIME_BIND | UNBOUND | one authenticated clock datum (frequency ratios are calibration-invariant) |
| DYN_BIND | NOT_INSTALLED | the physical child, the generation multiplicity, the chirality index |
| PredictionFreeze | NOT_TRIGGERED | the owner freezes the register before new comparisons |
| W_L | NOT_PASS by evidence | the recorded PMNS candidate is excluded (χ² = 10.6 on 2 dof, p = 0.005) |
| T3081 | UNOPENED | the maintainer side is replayed; the official host must be allowed |
| ScientificGold | FALSE | a frozen prediction, independent data and a preregistered test |

## 8. What stays open

- The convexity collar inside (223.58, 224), which needs an analytic saddle cap plus a non-grid bound.
- The rational coefficients of L₁₆, and a proof that it annihilates W_n for every n.
- A preparation protocol matching the reported ε^(−1/2) and ε^(−1/3) bounds.
- The 8-dimensional dispersive constant.
- The six SCR6 operands, the 1401 → 1370 seams, the 502- and 237-dimensional operators, MPKG A_M, and the historical Agni, Soma, Suraj and Sawan matrices.
- The owner's choices: signature, physical child, clock datum, freeze.

## Appendix: the eighteen layers

| # | layer | checks | content |
|---|---|---|---|
| 1 | carrier | 35 | K5, D, spec, Lagrangian, exact motion, Petersen, Hodge block, edge tick |
| 2 | spectral | 9 | heat trace, ζ_D, spectral dimension, moments 15/40/200 |
| 3 | spacetime | 34 | RP² pair, clock 125 → 120, E8 roots, walks, symbol, Green, clique coupling |
| 4 | native | 19 | source–port–bath action, W_AS, W_p, 40/9, radiation channel, nonlinear flow |
| 5 | observer | 7 | Kalman/Gramian readouts, Witten index −5 |
| 6 | gravity | 8 | LLY curvature; spectral-action route (CONDITIONAL) |
| 7 | cosmology | 7 | FLRW with the carrier field (CONDITIONAL) |
| 8 | frontier | 23 | band-edge orbit 135, the 224 saddle, saddle law 15/16 d², collar survey, coil |
| 9 | joins | 24 | the maps that make the layers one object |
| 10 | literal | 20 | the recovered operand file, every identity replayed, the flow on the owner's operands |
| 11 | glue | 11 | E8 = D8 + s; A4 ⊕ A4′ with x ↦ ±2x |
| 12 | binding | 12 | DYN_BIND constraints |
| 13 | gates | 12 | TIME_BIND courts, register, W_L, T3081, AUTH package |
| 14 | recurrence | 16 | W₉₀ exact, W₆₀₀ mod p, exclusion, the order-16 operator, characteristic polynomial |
| 15 | court | 19 | Court U19.81 audited |
| 16 | handover | 30 | the Locked Memory handover audited; critical census; T₆|V_c |
| 17 | waves | 18 | sound, light, frequency and phase on the K5 edges |
| 18 | snapshot | 16 | the 14:16 snapshot rebuilt; T⁹ density; Hessians; asymptotics |

To replay: `pip install -r requirements.txt`, then `python verify.py` (about 2.5 minutes), then `python -m pytest -q`.
