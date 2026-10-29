# One Machine, the unified edition: 28 October 2026

This puts the whole model in one text with one ledger: the verified build (layers 1–18), the integrated spine (layer 19), the canon synchronization (layer 20), the sibling's 28 October ledger of joins (layer 21), the sibling's evening notes with the canon's 19:10 continuation (layer 22), and one diagram that joins all the dots (layer 23). It is a selected mathematical build replayed from matrices. It is not a source admission and not a change to the canon matrices.

AUTH = NOT_PASS. ScientificGold = FALSE. TIME_BIND = UNBOUND. The six SCR6 operands stay absent. No gate moves, and no term is added to the action.

**Model:** GitHub `sachinkaria24-byte/OES`, branch `claude/lagrangian-spectral-spacetime-model-t2253b`.

- `python verify.py` runs 24 layers and 782 checks. Of these, 701 hold: THEOREM 543, OBSTRUCTION 51, ARITHMETIC 41, UNFORMED 24, CONDITIONAL 23, SELECTED_REFERENCE 17, REMOVED 2. The other 81 are REPORTED records.
- `pytest` runs 66 tests.
- The newest layers are `oes/dots.py` (layer 23, 269 checks) and `oes/assignment.py` (layer 24, 41 checks).
- `ports/ts/ledgerJoins.ts` and `ports/ts/pauliBath.ts` carry layers 21 and 22 into the sibling's app. Together with `coxeterSpine.ts` that is 43 rows, residual 0.
- `data/clocks.json` holds the explicit clock matrices. `docs/LEDGER.md` lists every join with its status, and `docs/DOTS.md` draws the 62 dots and 175 checked joins as one diagram on six levels, every pair of levels joined and no two maps holding it together.

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

New in layer 24 (the particle assignment on E8's roots, 09:00 on 29 October):

- **Both factors.** The carrier's A4 is taken as SU(5) and its complement A4′ as the family SU(5)′. The 240 roots are (24,1) + (1,24) + (10,5) + (5̄,10) + (10̄,5̄) + (5,10̄), where (10,5) is the carrier's ten duads times the twin's five sites and (5̄,10) its five sites times the twin's ten duads, each pair once. Layer 11's (10, 5̄′) is (10,5) with the twin's 5 renamed.
- **Moments.** 10 I on A4 + A4′, 15P + 10P′ and 10P + 15P′ on the mixed classes, 60 I in all: the band starts 30|k|², and Σ(T3·ρ)² : Σ(Q·ρ)² = 3 : 8.
- **The Standard Model (a selection, then theorems).** With colour sites 0, 1, 2 and weak sites 3, 4, Y is the only Cartan direction commuting with SU(3) × SU(2). Every root gets its colour, T3, Y and Q: u, d, u^c, e^c per twin site; d^c, e, ν per twin duad; gluons, W± and the leptoquarks X, Y on the carrier roots; the 20 family roots are the only roots with no Standard-Model charge. Q minus each colour coordinate is an integer on all 240 roots (the ℤ6). The table is `data/e8_assignment.json`.
- **One orbit.** J (site_a ↦ μ_a, μ_a ↦ −site_a) lies in W(E8) with J² = −1, swaps the factors and doubles the grade in E8/L0. The normalizer of A4 + A4′ has order 57600, the colour triples are one S5-orbit, and −1 swaps particles and antiparticles, so the assignment is unique up to W(E8) and the 248 is real.
- **Chirality (OBSTRUCTION).** One root of every pair ±ρ, as whole multiplets, always has an odd SU(5) anomaly and 25 doublets (Witten's anomaly). Anomaly-free sets of 10's and 5̄'s need equal numbers, and 3003 exist.
- **Three generations (CONDITIONAL).** [10_i, 10_j] = 5̄_ij for disjoint carrier duads, so with the bracket rule anomaly freedom forces a triangle of K5′: 45 roots, every anomaly zero, 12 doublets. The six-site port's roots are the 5 at the twin duad opposite the triangle. B6 is sharpened, not discharged.
- **Couplings.** Root triangles α + β + γ = 0. Down-type: vertex to opposite edge through the twin duad {3, 4}. Up-type: zero diagonal, so never rank one. The top coupling 10 10 5_H has no root realization (OBSTRUCTION). No Yukawa sizes (UNFORMED).
- **The six-site port.** M₂ − M₁² = XᵀX = 183 I + 52 J counts bath neighbours (235, 52); it is positive definite, so the six channels cannot evolve without the bath.
- **In layer 23** the result is the dot "root assignment", with seven THEOREM joins (A4 + A4′, E8, the charges, K5's edges, the affine group, S5, the six-site port), one CONDITIONAL join from the binding and one obstruction back to it.

New in layer 23 (all dots joined, with the sibling's notes of 21:40–22:08 and the collaboration hub of 21:46):

- **One diagram.** Every object of the model is a dot, and every checked map between two dots is a join. 62 dots and 175 joins (170 maps, five obstructions) form one connected diagram that no two maps hold together, and a test keeps `docs/DOTS.md` current.
- **K5 is a pair of root systems.** The signed incidence lists a positive system of A4, and the two incidences together list the positive roots of D5. So B Bᵀ = 5I − J and B Bᵀ + M Mᵀ = 8I are Coxeter identities, and spec D² = {0, h(D5) − h(A4), h(D5)} = {0, 3, 8}. Petersen is the orthogonality graph of the roots eᵢ + eⱼ.
- **The canon's selected six-port** is the oriented triangle 0-1-2 of K5 on the lattice. Its Fourier transform vanishes to third order, which gives the canon's triangle-cycle heat t⁻⁷/(22394880000000 π⁴), now derived.
- **A4 + A4′** has root cosets 40/50/50/50/50 and folded spectrum 0, 250⁴, the bath's values at the tick's 25 fixed momenta. **h81** is the four-cube complex, whose vertices are four qubits. **Hodge 70** is 35 + 35, swapped by reflections.
- **The circle** splits as a 2-clock, a 27-clock and the time clock (3105 + 2080 + 3456 = 1), and the atlas is its quotient ℤ/36. The tick bit does not descend to the atlas.
- **Corrections at 22:08.** An atlas address carries no tick bit; address 18 falls to the seam in one contraction; address 16 moves around the 6-cycle; 36 × 36 = 1296 meets the tick.
- **The 22:31 items.** The sibling's joined paper (22:20) adopts the 21:36 corrections. From the Locked Memory synthesis of 29 October: the carrier's 15 atoms are the bonds of K6 = K5 coned, with D the spoke–rim block of its line graph; the paired cyclic response has rank 9 with the C5-fixed line of ker M as its residual; the band expansion 30|k|² − (3/2)|k|⁴ + (1/24)|k|⁶ holds (a 7-design). Its order-11, degree-5 operator L11 is not a recurrence for the walks W_n or the return moments E_n (OBSTRUCTION), and its collar claim is recorded, not replayed.
- **The 23:03 items** (the sibling's 18 notes of 22:08–23:03 and the hub's release I):
  - The coil: the tick, the observer and the nakshatra generate ⟨8⟩ (540 points), and so does the smear step 184. The tick misses exactly ⟨40⟩ inside it.
  - Address and time are independent: ℤ/180 = ℤ/36 × ℤ/5, and the tick bit is t ≠ 0. The sibling's ADDRESS_TICK now proves this too.
  - The golden family: Bⁿ = F_n B + F_{n−1} I for every n. No Lucas trace is a multiple of 5, and the k-th golden point 216k misses exactly when 5 | F_k.
  - Which S5: the permutations of K6 that keep D are exactly the cone point's stabilizer, and for it atoms and bonds are one S5-set. The transitive S5 = PGL(2,5) gives a different module (OBSTRUCTION), as the hub's review asks. MPKG's block of order 5 with traces 1 is the C5 rotation of the cone's six sites.
  - Corrections: D T = T⁻¹ D for the atlas shift and doubling (MORE_DOTS said they commute); ⟨39⟩ has 1440 points, but the sun 1440 has order 3. The 31-point clock's characteristic polynomial is (x − 1)(x³ − 1)²(x⁶ − 1)⁴.
- **The 23:44 items** (the sibling's 29 notes of 23:05–23:43 and the hub's release J):
  - The grain ⟨72⟩ is the golden orbit times the sun. Time reads the golden index and the 27-clock the sun, and doubling doubles the one and inverts the other.
  - The vortex ℤ/9 is read off the address and is the 27-clock without the sun.
  - Doubling inverts a shift exactly when the shift has order 3 (SHIFT_LAW). The golden identities F(2n) = F(n)L(n) and det[K, Bⁿ] = −29F_n² hold for every n.
  - Corrections: 3456 is the time part of 216, not its 2-part; the clock tower is a chain only down to the golden orbit; order and step are dual (3 has order 1440, the sun 1440 has order 3).
- **The 00:15 items** (the sibling's 21 notes of 23:46–00:14, the separate model's relations receipt and a new Locked Memory synthesis, read only):
  - The circle is the ticks ⟨864⟩ times the misses ⟨5⟩. A point misses exactly when its tick part is 0, and in each golden loop the four misses are one observer coset.
  - Doubling cycles the ticks, kills the observer, and splits the nakshatra clock 18 + 6 + 2 + 1. The same cycles appear on the coil's 27 golden cosets.
  - The towers of 3 and 2 freeze at 27 and 736. This note first said the tower of 5 does not; it freezes at 245 (the 00:51 items).
  - The receipt's three further corrections are replayed: vortex points move, the odd-part orbit lengths run 1 to 36, and [K, B⁵] is divisible by 25 only in its determinant.
  - The synthesis's two-tick T12 is not semisimple. Its "N = 25 annihilator" is excluded: the 26 × 26 Hankel determinant of W₀..W₅₀ is positive.
- **The 00:35 relay** (the sibling's 29 October paper ONE_MACHINE_29 and its notes of 00:16–00:29):
  - The grain is the five ticks times the twelve multiples of 360, which are the observer times the sun.
  - Eight roots with pairwise inner product 1 and the origin are a maximal 9-clique of index 3, and its six-point faces are six-ports.
  - The root graph has spectrum 56, 28⁸, 8³⁵, (−2)¹¹², (−4)⁸⁴. A protected line cannot also be the coupling. The commutator court's anchored Gram determinant is 176173056.
  - Corrections: the chart labels 95, 98, 101 are one class mod 3, not mod 30; 241 is prime to 4320.
- **The 00:51 items** (the sibling's ten notes of 00:36–00:51 and the separate model's splits receipt):
  - The edge tick, the second compound of the vertex 5-cycle, is (x − 1)²Φ₅ on the cycles, fixing the rotor plane, and Φ₅, the time clock's polynomial, on the cuts.
  - The six-port's moments come from the bath's: contrast E_{k+1}/240 = 1, 241, 58264 and uniform 6E_k − 5E_{k+1}/240 = 1, 235, 55720. They give 241I − J and 183I + 52J.
  - The sibling's audits of its paper's scripts are replayed: 4805 is the Gram determinant over 5, not a minor; the collar fractions 3/65 and 3/80 differ; the shifted coefficient is −69373; the witness's tangent Hessian is positive.
  - A correction to this build: the tower of 5 freezes at 245 from height 3. The 00:15 text repeated POWER_TOWER's "does not freeze" after one step; the separate model's splits receipt and the sibling's TOWERS caught it. Each frozen value (736, 27, 245) generates the points that are 0 on its own clock.
  - The receipt's other corrections hold: 215 other golden loops, 4300 disagreement points in all, and entry into the tick cycle after two doublings.
  - A correction back to the sibling: its paper's energies 3985/16 and 6784/27 are misprints of 4025/16 and 6800/27. DEEP36_LOOP changed the square-free parts to 3985 and 318 instead; they are 161 and 51, and the density on T⁹ (layer 18) stands.
- **Every level (01:30):**
  - Twelve dots and 27 joins bring in the eleven layers that had none: the spectral triple, the readout, the product geometry, FLRW, layer 9's joins, the literal operands, the binding, the calibration, the court's measures, the critical census, sound and light and the nine-torus.
  - The 53 dots sit on six levels: number, symmetry, combinatorics, lattice, operator and physics. Every layer has a dot, each level is joined inside, and each is joined to the next.
  - THEOREM joins alone reach every dot but the product geometry and FLRW, which attach through the conditional heat coefficients (J10) and the Friedmann flow. From the circle to physical time there is an obstruction: no internal number fixes the calibration.
  - New here: on the projective line over F5 the hemi-icosahedron and its complement are the two PSL(2,5)-orbits of triangles, swapped by PGL(2,5); the four-cube's sixteen vertices are the sixteen cuts of K5 over F2; and the tick's 25 fixed momenta are critical points of the band (the minimum and 24 of the A4 + A4 family).
- **The 01:54 items** (the sibling's notes of 00:53–01:54 and its unified spine, the hub's release K with "Canon K — All Dots Joined", the separate model's unified receipt):
  - The root graph is a four-class association scheme (classes 56, 126, 56, 1; eigenvalues 56, 28, 8, −2, −4). Its Gram is 60 times the eigenvalue-28 projector, the pair sums give W₃ and W₄ (Canon K), and the 126 roots orthogonal to a root are E7.
  - The 4-simplex carries the tick on every grade as copies of the five-clock's regular representation, and the golden companion acts on the eight golden edge directions by B ↦ −(T + T⁻¹).
  - Each six-point face of the frame lies in exactly two maximal 9-cliques. Canon K's carry clock 4320 = 36 × 120 does not split.
  - Three corrections back to the sibling: the circle's subgroups of orders 120, 60, 30 and 10 all contain the ticks (GOLDEN_GRAVITY); the 4 in 183 + 6 × (56 − 4) is the face's other four sites, not the cut rank (CUMULANT_183); the 256 subset products have distinct square-free parts but are not all square-free (HESSIAN_RECOMPUTE).
  - The separate model's three source corrections and the hub's three conflicts are replayed. Its unified build and release K's evidence packages were not opened or run.
- **No dot on a single join (02:20):**
  - Eight dots hung by one join and nine joins were bridges. Each of those dots now has a second checked map, and removing any one map leaves the diagram connected.
  - The 256 half-periods are exactly the census's E8, E7 + A1 and D8 critical points, so the GKSL rates are census data. The spectral measures live on the band between the census's minimum and maximum. The owner's operand file holds the carrier's incidences. No two of the nine bath frequencies have a rational ratio, so no calibration makes the bath periodic.
  - AIR_801's matrix and PG(2,5) are dots. Mod 5 the matrix lies outside PSL(2,5) and swaps the two triangulations. On the Veronese conic of PG(2,5), the six axes, the surface's 15 edges and its 10 faces are the conic, the 15 exterior points and the 10 interior points. The matrix's orbits are conic 6, exterior 3 + 6 + 6 and interior 1 + 3 + 6.
- **The 02:52 items** (the sibling's notes of 01:57–02:49 with its spine29 audit, the hub's observer completion and releases K+ADDENDUM2 and K+ADDENDUM3):
  - The five-site charges Q = Y + T3 of the removed hypercharge shell are a dot. Their shells are the 4-simplex's even and odd faces (Σq² = 16/3 each), the hypercharge anomaly cancels on B4's 5 + 10 at opposite chiralities, Y lies in the dark U(5) through an identification (SELECTED_REFERENCE), and B1 forbids an atom-diagonal charge (OBSTRUCTION).
  - At the tick's 24 fixed momenta of type A4 + A4 the band's Hessian is −5 times a golden companion, with determinant 5⁸; the 25th momentum is the minimum, so 24 of the 25, not all, sit at 250 (a correction to CENSUS_CUBE).
  - The port metric is [2/5] ⊕ (2L_C5 + (2/5)J), twice the pentagon Laplacian plus (2/5)J with the corner 2/5, and 4I + 2X on the contrast with X² = X + I. The canon's (5 ± √5)/10 are the pentagon Laplacian's pseudo-inverse.
  - The joint observer: the wedge of the source pair has rank 7 with fibre SL(2), and three frame probes make it injective with an explicit inverse. The sideband lift: the address and the residues mod 32, 27 and 5 rebuild the tick; three sensors of largest alphabet 32 are optimal.
  - Replayed: Canon K's W₅ and W₆ (layer 3's returns), the 160 × 27 clock, the six-site Smith torsion (its 5 is the 5 in 240), the census's stabilizers (Weyl groups of the extended diagram's subsystems), the rotor firewall and the Bargmann phase π/4 (half the Pauli octant's solid angle). The sibling's "no clique of nine roots" and the 9-clique here are about two graphs, and both hold.
  - Not joined: the board's fine-structure digits, which invert to about 137.036 and are put in by hand (UNFORMED). The hub's verifiers and evidence zips were not downloaded or run.
- **The 02:55 items** (HALFPERIOD, TRACES): the half-periods by shortest length 0, 2, 4 on 1 + 120 + 135 classes; 224 certified exactly as the E7 + A1 saddle's critical value (gradient zero, ε = 240 − (128 − 112), Hessian 12P′ − 52P of index 1), a correction to HALFPERIOD; the even-shell traces 10/3, 2, 0, 16/3; the long-wave density of states E³/(1536 π⁴ 30⁴).
- **Every pair of levels, and no two maps (08:48):**
  - Four pairs of levels had no direct map, twenty dots lay on two maps, and 23 pairs of maps could cut the diagram. Twenty-seven joins and one dot close it: every pair of levels is joined, and no two maps hold the diagram together, except that two can cut off the conditional product geometry or FLRW.
  - The time clock, through the tick g = r r′: it fixes only the zero half-period and turns the other 255 in 51 band-keeping five-cycles, so e^−tL is tick-equivariant; on light it fixes one line per helicity and turns a golden plane (144° on +√5, 72° on −√5); on the cuts mod 2 it is a fifth root of unity in F₁₆.
  - Light: the golden companion acts by (I + Curl)/2, and x ↦ ax + b multiplies Curl by (a/5). The outer automorphism of S6 carries the cone's S5 onto PGL(2,5); S5 is W(A4) and the Weyl group of the binding's 5 + 10. The Hodge star is the deck involution of S ↦ e_S mod 2Λ.
  - The memory clock of layer 3 is a dot, stepped by the circle (a selection); its 9- and 10-cycles read the vortex and the time coordinate.
- **The 08:35–09:28 items (Drive check 09:02):**
  - The 240² ordered sums of two roots fill 9361 points in five shells, 240/56/14/2/1 deep. The walks of length 0 to 4 and Δ⁴ between two roots depend only on their inner product (Δ⁴: 3389062320, −40411056, 3317832, 222708, 228256). A root is a sum of three, four and six roots in 5253, 574224 and 9734696160 ways.
  - The six-port's couplings are walk moments. Its leakage residuals 55487966/183 and 131183830/99 are positive. Both sector measures have positive Hankel determinants through size 11, so the Krylov space grows by 6 at every order through 10.
  - The coordinate five-cycle fixes 16 half-periods and makes 48 five-cycles; the tick g = r r′ is free. On the edges K = I + 2(T + T⁻¹) squares to 5 on the moving edges, and the filled simplex has interior Laplacians 5I. Y is 5/6 of the weak duad's 10-weight, and the charge's edge lift lies in the cuts.
  - Corrections: DEGREE's 4 and 6 count the clique's other sites and the port's sites, not the cut rank and the cycles. INFRARED's fixed plane holds 2 of the all-ones vector's square (both fixed vectors have square 5), and 10 in the cyclic orientation. The port reads [2/5] ⊕ (2L + (2/5)J).
  - Recorded, not run: the separate model's completion, critical-port, connected-model and glue-helicity archives, the KD staging workbooks and MODEL_UPDATE_CHECKPOINT.json.
- **The 09:43–10:07 items (Drive check 10:07):** the coordinate classes (twice the first-five sum mod 5) are twice the grade in E8/L0, with integer and spinor counts 32/8, 10/40, 30/20, 30/20, 10/40. The collar witness (28, 28, 6, 2, 1, 0, 0, 0)/10 replays at ε = 220.6345317313 with least tangent eigenvalue 6.985582. The notes' own ledger corrections (52 orbits, 171 = 271 − 100) are arithmetic. INFRARED's 17/10 stays corrected.
- **The Golden root-site port (Drive check 10:40):**
  - The hub's T_G = F P_cycle maps the cycles isometrically onto ten roots: the near edges to e_i − e_{i+1}, the far edges to the glue roots. It is a dot.
  - Its moment traces are 1442, 347900, 84180666 and 20416532280. Its means are 239, 241 and 481/2 ∓ √5/10, and its variances 371, 171 and (1987 ∓ 31√5)/10, which is MEMORY's block.
  - With the hub's clique it shares two of 14 sites. The cross squared singular values are 4/5 and 2/5, the joint Krylov ranks 12, 24 and 36, and the clique's 4 × 4 Hankels are positive.
  - PLANE adopts the fixed-plane correction. The 10:38 model's charges, root triangles, transposition sums, fivefold map and clock orders replay.
  - The spectral-kernel archive, the hub's exact zip and the checkpoint are recorded, not run.
- **The marked charge map, the infrared channels and the fifteen words (Drive check 11:12):**
  - The hub's marked map L = P_cycle N P_A4 (each site to its outgoing edge) has L Lᵀ = ((5I + K)/10) P_moving and joins the charges to the Golden port. A near and a far mark (34/45, 26/45) decode the two Golden densities: determinant 32√5/675, nonnegative exactly in the window (49 ∓ 12√5)/41, ratio 17/13 at low energy.
  - Averaged over S5 the map is 0 and its square is P_cycle/3. The twelve marked squares, ten times each, sum to 4 P_cycle. Their 66 pairs have conditions 1, 5 and 5 + 2√5 (6, 30 and 30 pairs), and only all twelve together are isotropic.
  - The roots are a 7-design, so the four channels' densities follow from the ten root sites: plus 10E³(1 − E²/1080000), Golden (E⁴/240)(1 + (1/100 ∓ √5/3000)E), minus E⁵/36000. Hence near/far (17/13)(1 − 2E/5525), the marked ensemble (E⁴/360)(1 + 29E/3000) and the twirl (10/9)E³ + E⁴/540 + E⁵/48600. These are the hub's inherited coefficients, now computed.
  - The fifteen words of 088, 086 and 980 are a dot. They are K6's oriented duads with the reflection twisted: O = A + B/√2 is an exact isometry, none is rational (fixed Gram determinants 108 and 54), A + B is integral of index 8, and none is unimodular (mod-2 coinvariants 3 and 4).
  - No rational C5 commutes with D3 on J7 = 1 + 3 std. The least extension with one is 9 = 1 + 4 std, through A4's Coxeter element.
  - The rest of the 10:42–11:19 model replays: closed walks through 2872800, the witness's 19.3654682687 (220.6349198210 is wrong), S5's orders against the cyclic fibre, and the joint window's condition 2 + √5.
  - Recorded, not replayed: the hub's observation chain on the literal J7 (H9, H13, anchors), its own T, A, B, and the sibling's undefined four labelled responses (−64√5/625).
- **Hub task OES-C01, replayed.** At f41b278 the reported 21 layers, 412 checks (383 hold, 29 reported) and 31 tests replay exactly. The evidence is in `docs/hub/OES-C01/`; it has not been filed to the hub.

New in layer 22 (the sibling's notes of 18:32–02:55, the canon's 19:10 continuation and the separate model's status of 19:47–21:05):

- **Counts.** 1843 more readings on the tick bit, from 242 notes, all hold. Each is checked with its stated order, subgroup, steps or first landing.
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
- **Mass and energy.** The "mass determinant" 216 is det(3W) for the source metric of layer 10; the datum's 2 is the kinetic energy of a zero-stiffness 4-cycle in ker M.
- **The Pauli map, written out.** `data/pauli_half_periods.json` holds the eight Dynkin words and all 256 half-periods with their words and band values; `ports/ts/pauliBath.ts` replays it in the sibling's app.
- **The rotor plane and the tick doubling.** The C5-fixed plane of the cycle space (the oriented pentagon and pentagram) is turned a quarter by the doubling, and the tick doubling is the restriction of the day's twist x ↦ 7x.
- **The bath's spectrum.** The 256 half-period modes are 2Λ-periodic eigenfunctions of the bath, not ℓ² vectors; this answers PAULI_BLIND.
- **ROTOR_CHAIN, corrected.** Its shell tuple is the hexagon's difference distribution, and the flash's order 24 meets every tick.
- **The datum's cycle.** The checked datum's velocity is the alternating 4-cycle in ker M. Its kinetic ½|v|² = 2 comes from the Legendre transform of the carrier Lagrangian. Its ±1 alternate with period 2, so they are not the rotor's tick and tock (order 5).
- **Spanda.** On the six cycles, G = R − R⁴ has characteristic polynomial x²(x⁴ + 5x² + 5), and the sum of the five powers of R is five times the kernel projector. The involution 0 ↔ 3, 1 ↔ 2 is a pentagon reflection and a w₀: S R S = R⁻¹ and S G S = −G.
- **The two clocks.** 4320 = 32 × 27 × 5. The time clock ⟨864⟩ and the observer clock ⟨1080⟩ meet only in 0 and generate ⟨216⟩ of order 20, not the circle. ×15 lands on the observer clock exactly on the multiples of 72. The ticks' time coordinates are 0, 4, 3, 2, 1, and the time coordinate 4x mod 5 intertwines the rotor with the tick.
- **The Pauli generator, as an operator.** A Walsh–Hadamard conjugation carries the bath on the 256 cosets of 2Λ to L in the Pauli basis. The transpose sign is the E8 form mod 2, and no half-period mode is square-summable. The separate model's GKSL form −L(X) = 2 Σ (A X Aᵀ − X), over the 120 antisymmetric Paulis, is replayed.
- **Corrections at 21:36.**
  - AC_DC: the constant port's mean is 1.
  - CHARTS_YUGA: the tower's steps are 4 and 4.
  - TORSION_JOIN: the two clocks generate ⟨216⟩, ×15 lands on the observer clock only on multiples of 72, and pada 27 gives 1080.
  - CRT_CLOCK: the time coordinates are 0, 4, 3, 2, 1.
  - SPANDA_ALL: the power sum is five times the projector.
  - FIVE_NAMES: the 30-step average is the projector.
  - MATRIKA_WALK: an intertwiner exists.
  - SIBLING_CUT: the day's twist is a matrix check, and the Pauli identification is an operator identity.

Against the canon:

- **Position.** The Quick Access sheet 00_FULL_RECONCILIATION_20261028 (review cutoff 17:19:41) keeps OMSOON736 controlling. No Matrix ID is new, and the frozen gates stay. That sheet still lists this repository's 14:37 build (18 layers, 320 checks).
- **What the sibling adopted.** The sibling's CANON_READ (17:06) adopted the layer-20 corrections, and its 18:17 full edition keeps them. Its 19:05 ONE_BIT note adopts the commutator [d, c′] = c′⁶ of layer 21.
- **Continuation 3.** The canon sheet 00_CURRENT_20261028_1910 (review cutoff 19:10:16) records the 21-layer build as source-reported. It keeps OMSOON736 and every frozen gate.

Not formed: source infinity, foam, the double slit, entanglement as stored data, a Bell count, the photoelectric effect, a work function, electron, photon, proton, Compton and Bohr lengths, 19 Standard-Model parameters, the six SCR6 operands, the Krishna lift's operands, the epoch, a physical GKSL dynamics (layer 22's GKSL form of −L is a mathematical identity on the folded bath), SI, BRST, BV and Einstein–Hilbert. Still open: the collar (223.58, 224) and the rational coefficients of the order-16 operator.
