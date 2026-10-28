# OES — the end-to-end model

Lagrangian, spectral triple, spacetime, observer, energy, motion, gravity and cosmology, in one checked chain.

Research owner: Sachin Karia. Built 28 October 2026 against the canon cut **OMSOON736** (the "One Machine" 28 Oct edition), the 28 Oct consolidated Locked Memory, the 28 Oct collar/localization note, and the Through724 integrated model. This is an additive, unnumbered build. It mints no OMSOON or Matrix identifier and does not edit any workbook.

**AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND · DYN_BIND = NOT_INSTALLED · SCR6 absent · R6/A40/A52 frozen.**

Each statement below has one status, and `python verify.py` re-checks every one of them. The statuses are the canon's five: THEOREM, ARITHMETIC, OBSTRUCTION, REMOVED and UNFORMED. Two more are added here:

- **SELECTED_REFERENCE**: rebuilt from a stated definition because the saved original operand is absent.
- **CONDITIONAL**: needs an input the canon marks external.

A passing check is a statement about constructed matrices. It is not AUTH.

---

## 0. How the layers join

```
 K5 signless incidence M  ──►  D = [[0,M],[Mᵀ,0]] on ℓ²(V⊔E), dim 15        (layer 1, 2)
        │                         │
        │                         ├─► S[ψ] = ∫ ½|ψ̇|² − ½⟨ψ,D²ψ⟩ dt           carrier Lagrangian
        │                         ├─► heat trace, ζ_D, spectral dimension      spectral model
        │                         └─► readouts / hidden sectors                observer (layer 5)
        │
        ├─► P5 = ker M (source), L6 = cycles (port) ──► native action on E8 bath (layer 4)
        │                                                   │
        ├─► RP² on icosahedral axes, RP²×S¹, clock 125→120 ─┤   spacetime (layer 3)
        │                                                   │
        └─► E8 roots ──► Λ, Δ = 240I − A, ε(k), walks ──────┘
                                   │
     external M⁴, f, Λ, m  ───────►  spectral action of M⁴×F  ──► G, Λ_cc     gravity (layer 6, CONDITIONAL)
                                   └──► FLRW with homogeneous ψ               cosmology (layer 7, CONDITIONAL)
```

---

## 1. The carrier (`oes/carrier.py`)

**Datum.** K_n has the signless incidence M : ℝ^E → ℝ^V, where an edge maps to the sum of its two endpoints.

**Selection (THEOREM).** For n > 2, rank M = n, so dim ker M = n(n−3)/2. Setting dim ker M = |V| gives exactly n = 5. The signed incidence never satisfies this: its quadratic has discriminant 17. Checked for n = 3…12.

**Gram (THEOREM).**
- M Mᵀ = 3I + J, with (3I+J)⁻¹ = I/3 − J/24.
- The Smith invariants of M are 1, 1, 1, 1, 2.
- The S₅-equivariant maps ℝ^E → ℝ^V form a 2-dimensional space, spanned by M and J. Flag support kills J, and the remaining coefficient is the unit of time.

**Dirac and spectrum (THEOREM).** D = [[0, M], [Mᵀ, 0]] is self-adjoint and odd, with {D, γ} = 0 for γ = (+1 on V, −1 on E).
- D²(D² − 3)(D² − 8) = 0, so spec D² = {0⁵, 3⁸, 8²}.
- Tr D² = 40 and Tr D⁴ = 200. All odd traces vanish, and rank D² = 10.
- The signed Dirac has spectrum {0⁷, 5⁸}. It is not the carrier.

**The Lagrangian (THEOREM).** The action is

  S[ψ] = ∫ ( ½⟨ψ̇, ψ̇⟩ − ½⟨ψ, D²ψ⟩ ) dt,  with Euler–Lagrange equation ψ̈ + D²ψ = 0.

No second intertwiner, quartic or laboratory unit enters. It is fifteen oscillators: five with coefficient 0, eight with coefficient 3 and two with coefficient 8. The frequencies are 0, √3 and 2√2, and their squared ratio 8/3 is not the square of a rational.

**Energy and motion (THEOREM).** The energy is E = ½|ψ̇|² + ½⟨ψ, D²ψ⟩.

The canon datum has:
- vertex part (1,−1,0,0,0) + (1,1,1,1,1);
- edge part Mᵀ applied to the contrast;
- velocity the alternating 4-cycle on edges 01, 12, 23, 03.

On this datum ⟨ψ, D²ψ⟩ = 64, and E = 12 + 20 + 2 = 34 across the sectors λ = 3, 8 and 0. The closed form is

  ψ(t) = Σ_λ P_λ [ cos(√λ t) ψ₀ + sin(√λ t)/√λ · v₀ ]  (λ = 0: ψ₀ + t v₀),

where the P_λ are exact Lagrange-interpolation projectors. It conserves E to 1e−13, and a leapfrog integrator agrees with it.

**Joined finite objects (THEOREM).**
- Petersen graph, the disjointness graph on the 10 edges: A² + A − 2I = J, girth 5, projector ranks 1, 5, 4.
- Cycle Gram for the star tree: (G − I)(G − 5I) = 0 and det G = 125.
- Hodge block A = (6I − G)σ, with σ the signed opposite-edge exchange: A² = 5I.
- Signed edge Gram: G² = 5G.
- Edge tick: order 5, ∂T = R∂. Its unsigned form commutes with the Petersen adjacency, and it preserves the cycle space, where it acts as the order-5 rotor.

**Moments and harmonic obstruction (THEOREM).** On the contrast plane, summing over the 20 oriented edges (the A4 roots), M₂ = 10|x|² and M₄ = 6|x|⁴ + 10Σx⁴; over the 10 unordered pairs each sum is half. The line 3|x|⁴ − 7Σx⁴ is harmonic for the ambient Laplacian of ℝ⁵. For the contrast plane's own Laplacian, Δ|x|⁴ = 24|x|² and ΔΣx⁴ = (48/5)|x|², so the harmonic line is 2|x|⁴ − 5Σx⁴ (canon correction, 28 Oct; §21). A quartic is not in the action (OBSTRUCTION).

> **Correction to the printed text.** The canon writes M₂ and M₄ as sums over the ten pairs i < j. The identities hold over the **twenty oriented roots** e_i − e_j. Over the ten pairs each sum is half: for example Σ_{i<j}(x_i − x_j)² = 5|x|². The check suite verifies both forms.

## 2. The spectral model (`oes/spectral.py`)

The finite spectral triple is (A = C^V ⊕ C^E, H = ℓ²(V⊔E), D, γ), with dim H = 15. All of its spectral content comes from {0⁵, 3⁸, 8²} (THEOREM):

- **Heat trace:** Z(β) = Tr e^{−βD²} = 5 + 8e^{−3β} + 2e^{−8β}.
- **Moments:** Tr D^{2k} = 15, 40, 200, 1240, 8840 for k = 0…4. These are all that a spectral action Tr f(D²/Λ²) can read.
- **Spectral zeta:** ζ_D(s) = 8·3^{−s} + 2·8^{−s}, with ζ_D(0) = 10 = rank D² and ζ_D(1) = 35/12.
- **Spectral dimension:** d_s(β) = −2 d log Z / d log β tends to 0 in both the UV and the IR, and peaks at 0.843 near β = 0.42.

The carrier has no emergent continuum dimension. This agrees with the canon's removal of "4 from 5 − 1" and of imported NC dimensions (REMOVED).

## 3. Spacetime (`oes/spacetime.py`)

The canon keeps three objects separate. None of them is a physical spacetime.

**(a) Surface and time-circle (THEOREM).**
- The six icosahedral axes carry the hemi-icosahedron and its complementary 10 triples. Both are closed RP² triangulations with χ = 1.
- H₀ = ℤ, H₁ = ℤ/2, H₂ = 0. rank ∂₂ is 10 over F₂₄₁ and 9 over F₂; the gap is the Bockstein of the 2-torsion.
- The 20-face union kills the torsion.
- The mapping torus of id is RP² × S¹, with H = ℤ, ℤ ⊕ ℤ/2, ℤ/2, 0 and F₂ Betti numbers 1, 2, 2, 1.
- The algebraic torus of −id is pure 2-torsion, with free Betti numbers 0, 0, 0, 0. It is a chain map and not a self-map (OBSTRUCTION).
- A₅ has element orders {1, 2, 3, 5}, with census 60 = 1 + 15 + 20 + 24. No rotation has order 4.
- The Hodge Laplacian on the 31 cells has nullity 1.
- K₄₀₃ = K_G ⊗ I₃₁ + I₁₃ ⊗ Δ has rank 400, and K_G has characteristic polynomial z³(z−4)²(z²−5z+5)²(z²−3z+1)².

**(b) Clock (THEOREM / OBSTRUCTION).**
- T on ℝ¹²⁵ is a Jordan block J₆(1) plus a permutation of order 90 (eleven 10-cycles and one 9-cycle).
- πσ = I₁₂₀, πT = Aπ, and A has order 90.
- g₁₂₀ = diag(I₁₁₉ + 11ᵀ, 1) is positive definite and A-invariant.
- (T − I)⁵ ≠ 0 on the chain, so T has no invariant positive metric. The memory lives upstairs and the metric clock lives on the quotient.

**(c) E8 lattice "space" with action time t (THEOREM).**
- **Roots and graph:** 240 roots (112 + 128) with Σαα^T = 60 I₈. The root graph is 56-regular, with spectrum 56¹ 28⁸ 8³⁵ (−2)¹¹² (−4)⁸⁴ and Gosset walks 1, 0, 56, 1512, 62160.
- **Returns:** lattice returns N₀…N₆ = 1, 0, 240, 13440, 1260720, 137813760, 17141798400, computed by exact walk convolution.
- **Symbol:** ε(k) = 240 − Σcos(α·k), with ε(0) = 0 and ε(π(1,1,1,1,0,0,0,0)) = 256.
- **Band range:** 20,000 random samples never exceed 256. That is ARITHMETIC evidence; the range proof is the canon's census.
- **Long waves:** ε ≈ 30|k|², so the bath sound speed is √30 in lattice units. No SI length or time is bound.
- **Ball:** the shells of |x|² ≤ 8 are 1, 240, 2160, 6720, 17520.
- **Green identity:** 240(G(0) − G(α)) = 1, exactly. It follows from ΔG = δ and the root-transitivity of W(E8); the solver confirms it on the W-symmetric ball.
- **Six-site clique** x₀ = 0, x_j = e₁ − e_{j+1}:
  - block A = 241I − J;
  - exterior coupling BB* = 183I + 52J = 183P_c + 495P_u, where 52 = 56 − 4 common neighbours.

## 4. The native action: source, port, bath (`oes/native.py`)

The declared boundary-pullback action, from Through724 and the collar note, is

```
L = ½ q̇ᵀM_s q̇ + ½|d g(q)/dt|² + ½|ẏ|² − 2 qᵀM_s q − ½ gᵀ(W_p + A) g − gᵀB y − ½⟨y, D y⟩
```

Its equations of motion are

```
M_s q̈ + 4 M_s q + J(q)ᵀ [ g̈ + (W_p + A) g + B y ] = 0,     ÿ + D y = −Bᵀ g,
```

where q = (a, b) ∈ P5 ⊕ P5, P5 = ker M, g is the six-port boundary value and y is the bath off the clique.

**Reconstructed parts (SELECTED_REFERENCE).** The saved native_source_matrices (SHA-256 73e07429…) are absent, so the port is rebuilt from its stated definition:

- **Source matrices.** A(a) is the symmetric zero-diagonal matrix with entries a_e. Since Ma = 0 its rows sum to zero, so [A(a), A(b)] is skew with zero row sums, which is an oriented cycle. This is W_AS : Λ²P5 → L6.
- **Source mass.** M_s = I/4 in an orthonormal basis of P5. P5 is the irreducible 5 of S₅, so this metric is unique up to an amplitude unit. The canon's det 8/9 refers to its saved basis.
- **Port metric.** W_p is the canon's explicit boundary metric: circulant (22, −8, 2, 2, −8)/5 on x₁…x₅ and 2/5 on x₀.
- **Adapter.** T : L6 → boundary intertwines the cycle rotor with x_j → x_{j+1}, and satisfies (TW_AS)ᵀ W_p (TW_AS) = (320/9) G P with G = Λ²M. It is fixed by a deterministic Reynolds average. The source and port energetics do not depend on that choice; the bath coupling does.

**Checked.**
- W_AS has rank 6 and kernel 4 (THEOREM).
- W_ASᵀW_AS = (10/9)P, by Schur (THEOREM).
- W_AS is rotor-equivariant (THEOREM).
- spec W_p = {2/5, 2, 5 ± √5 (×2)} and det W_p = 320 (THEOREM).
- Sharp quartic (THEOREM): max Q₄/ρ² = **40/9**, attained by a balanced visible pair; random sources stay below it. The maximisers form the degree-5 del Pezzo section Gr(2,5) ∩ ℙ⁵, as Through724 states.
- The port is quadratic: g(0) = 0, Dg(0) = 0 and Jq = 2g. At linear order the source equation is q̈ + 4q = 0, with frequency 2 and no linear channel into the bath (THEOREM).

**Energy and motion in the bath.**
- **Radiation channel (ARITHMETIC).** A port oscillating at frequency 4 (eigenvalue 16) lies inside the band [0, 256]. The bath density seen by the uniform channel at λ = 16 is 2.24×10⁻⁷ (Monte Carlo), against 2.03×10⁻⁷ from the long-wave estimate. The contrast channel sees 2.7×10⁻⁹. The channel is open but very thin, which fits the canon's long-lived periodic families.
- **Nonlinear flow (SELECTED_REFERENCE).** The full nonlinear system was integrated on the |x|² ≤ 8 ball (26,635 bath sites, Dirichlet outside) with RK4 to t = 4. Total energy is conserved to a relative 2×10⁻¹⁰ (r = 0.05) and 1×10⁻⁷ (r = 0.2).

  | preparation | r | bath gain / E₀ | source E ratio |
  |---|---|---|---|
  | circular (static port) | 0.05 | 9.0×10⁻⁵ | 1.12 |
  | breathing (port ∝ sin 4t) | 0.05 | 1.16×10⁻³ | 0.98 |
  | circular | 0.2 | 8.3×10⁻² | 3.61 (orbit breaks up) |
  | breathing | 0.2 | 1.0×10⁻² | 0.93 |

  At small amplitude the breathing source feeds the bath 13 times more than the circular one. At r = 0.2 the circular orbit falls apart. That matches the canon's statement that the rotating family is guaranteed only at tiny amplitude (|a| ≤ 8×10⁻⁶) and is nonlinearly unstable. The ball is a cavity, so these numbers are energy exchange, not a far-field rate.
- **Static tails (OBSTRUCTION, canon 28 Oct).** A nonzero port mean forces a non-ℓ¹ static tail, with annular lower bounds T1–T4. A zero-mean periodic source above frequency 2 with high port harmonics cannot be ℓ¹-localized (F5).

## 5. Observer (`oes/observer.py`)

The system is x = (ψ, ψ̇) with x' = Ax and A = [[0, I], [−D², 0]]. Observable subspaces come from iterated orthonormal Krylov spaces.

**Structure (THEOREM).**
- D² = diag(MMᵀ, MᵀM), so the vertex and edge systems never exchange energy. D intertwines them as a supersymmetric pair.
- The Witten index is Tr γ e^{−βD²} = −5 for every β.

**Observable dimensions out of 30 (THEOREM).**

| readout | observable | readout | observable |
|---|---|---|---|
| vertex positions | 10 | one vertex | 4 |
| edge positions | 20 | one edge | 6 |
| D ψ | 20 | vertex sum | 2 |
| all positions | 30 | | |

A scalar readout sees at most 6 dimensions, two for each of the three spectral lines. This is the canon's Firefly remark.

**Hidden controllable sector H = Ran K ∩ ker O (THEOREM).**
- Edge force with a Dψ observer gives **10**: the five kernel (cycle-drift) modes are reachable but invisible. This is the carrier's dark sector.
- Edge force with a vertex observer gives 20, and vertex force with an edge observer gives 10. All other pairings give 0.
- The finite-time Gramian W_o(6) of Dψ has rank 20.

The original Sākṣin operator and the 237-dimensional fiber observer remain **UNFORMED**.

## 6. Gravity (`oes/gravity.py`)

**Intrinsic (ARITHMETIC).** These are Lin–Lu–Yau (optimal-transport) Ricci curvatures:
- K5: **5/4**;
- the Petersen graph: **0**;
- the E8 root-lattice graph: **0**, so the bath space is discretely flat.

They are curvatures of discrete metric spaces, not Einstein gravity. The canon's integers (Einstein–Hilbert power 4 = cut rank, vacuum power 6 = cycle rank, 2 + 7 = 9) are shared integers only.

**Conditional: the spectral action of M⁴ × F (CONDITIONAL).** Take D = D_M ⊗ 1 + γ₅ ⊗ m D_F on a closed spin 4-manifold. Then

  Tr e^{−tD²} = Tr e^{−tD_M²} · Tr e^{−t m² D_F²},

and the expansion up to O(t²) reads

  (4πt)⁻² ∫√g [ 60 − t(160m² + 5R) + t²(400m⁴ + 40m²R/3) ].

This is checked symbolically. It uses only 15, 40, 200 and the spinor rank 4.

With f-moments F₀ = f(0), F₁ = ∫f and F₂ = ∫xf:

  1/(16πG) = 5F₁Λ²/(16π²),   Λ_cc = 6(F₂/F₁)Λ² − 16m² + 40(F₀/F₁)m⁴/Λ².

- For f = e^{−x} and Λ = 10m: G = π/(500m²) and Λ_cc = 584.4m².
- Choosing F₂/F₁ = 0.026 instead makes Λ_cc = 0. Λ_cc·G can take any value.

This is the canon's "physical scales and Wald coefficient underdetermined", made explicit. The inputs M⁴, f, Λ and m are external, so the Newton constant in SI units, the Wald coefficient and any horizon/area map stay **UNFORMED**. Curvature-squared a₄ terms are omitted.

## 7. Cosmology (`oes/cosmology.py`, CONDITIONAL)

Place the carrier field homogeneously on flat FLRW, with G and Λ_cc from layer 6:

  ψ̈ + 3Hψ̇ + m²D²ψ = 0,  H² = (8πG/3)ρ + Λ_cc/3,  Ḣ = −4πG|ψ̇|².

Integrated with DOP853 from the canon datum, with Λ = 10m and Λ_cc tuned to 0:
- the Friedmann constraint holds to 4×10⁻¹²;
- the kernel sector goes as ρ ∝ a^{−6.000} (stiff, massless);
- the λ = 3 and λ = 8 sectors go as ρ ∝ a^{−3.000} (dust);
- the scale factor grows as a ∝ t^{0.665}.

With the natural cutoff (f = e^{−x}), the evolution goes straight to de Sitter with H → √(Λ_cc/3) = 13.96m. That is the vacuum-energy problem, not a prediction.

No observed parameter (H₀, Ω, w) is produced. IceCube/LHAASO scales and the vacuum amplitude (27/5)³e^{−280} stay **REMOVED**.

## 8. Residual front (`oes/frontier.py`)

This section records the sibling update received after the 01:27 UTC Drive cut. Drive showed nothing newer at the time of the check.

**Replayed here.**
- **Band vertex (THEOREM).** At v* = π(1,1,1,1,0,0,0,0), every root gives cos = ±1: 112 give +1 and 128 give −1, so ε(v*) = 256.
- **Band-edge orbit (THEOREM).** The W(E8)-orbit of v* has 2160 points in ℝ⁸ and **135** classes modulo 2πΛ.
- **Local bound (ARITHMETIC, sampled).** S(v*+δ) ≥ −16 + |δ|²(2 − |δ|²) holds for |δ| ≤ √2. The minimum slack is −3×10⁻¹⁵, so the bound is attained.
- **224 saddle at πα (THEOREM, exact).** The expansion is ε = 224 + 6ρ² − 26z² − ρ⁴/2 + 3ρ²z² + (5/6)z⁴. On the cone 6ρ² = 26z² the quartic is exactly **(40/169)ρ⁴ > 0**, so the level set bends the convex way at the saddle.
- **Agni–Soma (THEOREM).** (5I − G)/5 is the cycle projector and fixes the image of W_AS. The two are not rival operators; only the naming needs settling.

**Reported, not replayed** (status REPORTED; the certificates and operands are not in this repository):
- the band is exactly [0, 256] by an alcove branch-and-bound (247,920 pieces);
- ε > 100 outside |k|² ≤ 6 (7,523 pieces);
- the W_n recurrence has order **11**, with (x+12)² dividing the leading coefficient, so the page line "at least 10, not 11" should be deleted (§15: the operator found has order 16; its characteristic polynomial has 11 roots in the band, (z+12)² among them, and 5 outside);
- 155 vs 4805 is a label error (155 = det T and 4805 = 5·31², the 4th cofactor of TTᵀ);
- rotor hex6 has m₁ = 242 ≥ 241.36;
- for the collar, the alcove reduction gives numerically positive curvature up to 223.999;
- 223.25 < 223.5 < 223.53 < 223.58 are successive lower bounds, so the standing value is the largest replayed one.

**Added at the 0741 cut (28 Oct, One_Machine_20261028_0741).**
- **Saddle law (THEOREM).** On the 224 level at distance d from the saddle πα, the tangent curvature is exactly **(15/16)d² + O(d⁴)**. It follows from the order-4 expansion, which is E7-isotropic to that order. On the true symbol the ratio is 0.937 at d = 0.1 and 0.932 at d = 0.3. The level set is convex near the saddle, but the margin vanishes there quadratically.
- **Collar survey (ARITHMETIC, evidence).** The open set is 218.9323 < ε < 224, √(313/20) < |k| < 35/8. I took 8×10⁶ samples and ran constrained optimisation from the worst points. The tangent curvature stays positive everywhere checked. Outside saddle caps of radius d₀ its minimum is 0.030, 0.083, 0.225, 0.424, 0.665 and 0.928 for d₀ = 0.2, 0.3, 0.5, 0.7, 0.9 and 1.1, always at ε → 224. This agrees numerically with U19.74's claimed floor.
- **Why a grid cannot close it (OBSTRUCTION, quantitative).** The Hessian moves at rate ≤ 85 per unit distance. Even outside a radius-1 cap, a first-order box certificate needs box radius < 0.011, which means more than 10¹³ boxes in a single Weyl chamber. Closing the collar needs two things: an analytic cap of radius about 1, built on the 15/16 law plus an explicit O(d⁴) remainder, and a bound outside the cap that does not use a grid.
- **Coil (THEOREM).** In ℤ/4320 the pada step 40 (order 108) and the yuga step 1728 (order 5) generate a cyclic subgroup of order 540 and index 8. The two cyclic subgroups meet only at 0. The Fibonacci recurrence mod 5 has period 20, and 20 divides 540.
- **U19.74 (REPORTED).** The note is not on Drive; the latest court note there is U19.56. Its r² = 9/40 sum-of-squares lock cannot be replayed without its definition. The 0741 paper also says 9/40 = 3²/(5·8) is not a count of the carrier.
- **Walk counts.** U19.53–U19.55 printed W₅ = 152697600 and W₆ = 22508998080. U19.56 corrected these to 137813760 and 17141798400, and layer 3 of this repository reproduces the corrected values.

**Still open.**
- A certified curvature bound away from the 224 saddle. This is the next step: a certified saddle analysis with an explicit radius.
- The complete scalar W_n recurrence.
- The five-port and the −8/9 moment operands.
- The decay-rate and prefactor conflicts.

## 9. Joining the dots (`oes/joins.py`)

A **join** is an identity between matrices built in different layers. Each one below is checked by `verify.py`. A **shared integer** is the same number appearing on two objects with no map between them. The canon is strict that "equal ranks are not the same maps", so the two are listed apart.

```mermaid
graph LR
  K5["K5 incidence M"] -->|"D = [[0,M],[Mᵀ,0]]"| D["carrier D, spec 0⁵ 3⁸ 8²"]
  K5 -->|"J1: R_aᵀR_a = MᵀM"| E8["E8 roots: 5 D5 layers, 120 roots"]
  K5 -->|"J2: MᵀM = I + J − A_Pet"| PET["Petersen / del Pezzo lines"]
  K5 -->|"J4: MMᵀ = Gram(clique) + 2I"| CLQ["E8 six-site clique"]
  D -->|"J5: off-diagonal block of L(K6)"| RP2["RP² on 6 axes (1-skeleton K6)"]
  D -->|"J7: ker D² = P5, index −5"| P5["P5 = ker M"]
  P5 -->|"J6: hidden sector P5 ⊕ P5"| OBS["observer: dark sector"]
  P5 -->|"source q = (a,b)"| NAT["native action"]
  PET -->|"J2: P5 = eigenvalue-1 space"| P5
  PET -->|"J9: 40/9 maximisers = del Pezzo"| NAT
  NAT -->|"W_AS into the cycles L6"| L6["cycle space L6, Hodge A² = 5I"]
  L6 -->|"J3: W_p = 2L(C5) + (2/5)J, golden petals"| PORT["port metric W_p"]
  PORT --> CLQ
  CLQ -->|"Δ = 240I − A, BB* = 183I + 52J"| BATH["E8 bath"]
  E8 --> BATH
  D -->|"J10: traces 15/40/200 (CONDITIONAL)"| GRAV["G, Λ_cc, FLRW"]
  ROT(("C5")) -.->|"J8: one rotation through every layer"| D
  ROT -.-> L6
  ROT -.-> PORT
  ROT -.-> BATH
```

**Joins (THEOREM unless marked).**

| # | Join | What it says |
|---|---|---|
| J1 | r_(ij),a = μ_ij + ν_a are E8 roots, R_aᵀR_a = MᵀM, ker R_a = P5. Each layer with A4 is a 40-root D5, and the union has 120 roots. | The carrier edge gram *is* an E8 root gram. The part that disappears in E8 is exactly P5. |
| J2 | MᵀM = I + J − A_Petersen | The carrier edge spectrum {0⁵, 3⁴, 8} is the Petersen spectrum {1⁵, (−2)⁴, 3} under λ = 1 − θ (with +10 on the uniform line). P5 is the Petersen eigenvalue-1 space and the kernel of the del Pezzo line matrix. |
| J3 | W_p = 2L(C5) + (2/5)(J₅ ⊕ 1) | The port metric is twice the 5-cycle Laplacian. Its moving eigenvalues are 2(φ + 2) and 2(3 − φ), which are the golden petals (5 ± √5)/2 doubled. |
| J4 | Gram(x₁…x₅) = I + J, so MMᵀ = Gram + 2I | The carrier vertex gram is the bath clique gram shifted by 2. |
| J5 | The RP² 1-skeleton is K6, and D = A_L(K6) − diag(J − I, MᵀM − 2I) | Coning makes the 15 carrier atoms the 15 edges of the surface. D is the star/non-star block of the K6 line graph. |
| J6 | hidden(edge force, Dψ) = P5 ⊕ P5 | The carrier's dark sector is exactly the native source space. |
| J7 | Witten index −5 = −index(M) = −dim P5 | The count of dark modes is a topological index. |
| J8 | vertex rotation → tick → cycle rotor → W_AS → T → S → coordinate cycle in W(E8) | One C5 runs through every layer. The full nonlinear native vector field is equivariant to 8×10⁻¹⁵ (SELECTED_REFERENCE, because T was chosen equivariant). |
| J9 | The 40/9 maximisers are visible decomposable wedges, a locus of projective dimension 2 | This is the degree-5 del Pezzo surface whose line matrix appears in J2. |
| J10 | 15, 40, 200 → heat coefficients 60, 160m², 400m⁴ | The only route from the carrier to G and Λ_cc (CONDITIONAL). |

**Read as one sentence:**
1. One incidence M builds D.
2. D's kernel P5 is the source, and that source is invisible to the observer (J6, J7).
3. D's edge block is the Petersen complement (J2), the E8 root gram (J1) and, through coning, the surface (J5).
4. The source talks through the cycle space, with a port metric that is the golden C5 Laplacian (J3), to a clique whose gram is the carrier's vertex gram (J4). That clique is inside the E8 bath.
5. One C5 symmetry is kept from end to end (J8).
6. Gravity and cosmology attach only through the traces (J10), and only conditionally.

**Shared integers, no map (ARITHMETIC):**

| Integer | Where it appears | Map? |
|---|---|---|
| 15 | dim H; edges of K6; duads of 6 | J5 is the only map among these |
| 60 | E8 frame; \|A5\|; the Dirac trace coefficient | none |
| 240 | E8 roots; 6·Tr D²; the corner diagonal | none |
| 20 | five-port visible coordinates; observable dimensions of Dψ; Tr MᵀM | none |
| 125 | det of the cycle Gram; 5³ clock memory states | none |
| 120 | \|S5\|; clock quotient; D5 union | none |
| 9 | gravity's 2 + 7; E8 clique size | none |
| 36 | atlas addresses | none |
| 4320, 108, 69120 | yuga, japa and Human Design counts | integers only |

# Part II — From the mathematics to the operands and the physical gates

The canon's own state machine (S364 master lock) separates four kinds of transition:

> a new theorem head changes what is **known**; an authenticated root changes what can be **executed**; a binary receipt changes what can be **compared**; an independent warrant changes what can be **promoted**.

So "doing the maths to get to the gates" means two things: drive every gate to the edge of its own transition type, and prove exactly what input closes the rest. Layers 10–22 do this.

## 10. Operands recovered or formed

| Operand (canon status before) | What happened | Layer / file |
|---|---|---|
| saved `native_source_matrices`, SHA-256 73e07429… (ABSENT) | **Located** inside `OES_Standing_Model_Integrated_Proof_Packet_20261027.zip`. The bytes hash to the recorded value here, a cross-host byte receipt. | `data/native_matrices_input.json`, layer 10 |
| 6×6 adapter T of eq. 27, "155 vs 4805" (conflict) | Present in the same file as `T_OMSOON293`: det T = 155 = 5·31, cofactor₄₄(TTᵀ) = 4805 = 5·31², (TTᵀ)⁻¹₄₄ = 1/5. One adapter and its cofactor; **replayed**. | layer 10 |
| E8 glue map (ABSENT) | **Constructed** both ways: E8 = D8 ∪ (D8 + s) with isotropic s, and E8 ⊃ A4 ⊕ A4′ of index 5 with glue map x ↦ ±2x on ℤ/5. | layer 11 |
| lattice sequence W₆₀ (ABSENT) | **Computed exactly** to W₉₀ by a W(E8) dominant-weight DP with CRT. All 56 canon values W₀…W₅₅ are reproduced with zero mismatches, including W₂₅…W₅₅, which the canon had never independently regenerated. A second, independent engine (D8 + spinor factorisation) gives W₀…W₆₀₀ modulo primes and agrees with all 91 exact terms. | `data/walks90.json`, `data/walks_modp.json`, `oes/walks.py`, `oes/walkfast.py`, layer 14 |

**The literal operands against the earlier reconstruction (THEOREM, layer 10).**
- Every identity the canon states for the file replays exactly:
  - W = NᵀN with det 8/9, and M = diag(W/4, W/4);
  - W_p = 2FᵀF, with spectrum {2/5, 2, 5 ± √5};
  - WASᵀW_p WAS = (320/9)·Λ²M·P;
  - R⁵ = I, RᵀWR = W, WAS·Λ²R = Q·WAS.
- The printed literal R is exactly the K5 vertex 5-cycle.
- My layer-4 selected reference had the same W_p (exactly), the same metric up to basis, and the same Schur scale. Its adapter differed from the literal only by an explicit W_p-isometry U commuting with the C5 rotation (det U = −1). That is precisely the freedom the uniqueness analysis predicted.
- The native E8 flow was rerun on the **owner's literal operands** (apex 0 and eᵢ − e₆ clique). Energy is conserved to 5×10⁻¹¹, and a breathing source feeds the bath 11.7× more than a circular one (13× in the reference run).

**Uniqueness certificates (THEOREM).** These are why derived operands are not arbitrary surrogates:
- P5 is an irreducible S5-module, so its invariant metric is unique up to scale.
- Hom_S5(Λ²P5, L6) is one-dimensional, so W_AS is forced up to scale.
- No S5- or D5-equivariant isomorphism L6 → boundary exists: the characters agree only on the identity and the 5-cycles (layer 12, B0). So C5 is the maximal symmetry of any port adapter, and its moduli are an explicit commutant group.

**Searched and not present.** The reader packet and the 27 Oct proof packet do not contain:
- the six SCR6 operands;
- the 1401 → 1370 seams;
- the 502-dimensional Hodge–Dirac and the 237-dimensional operators;
- MPKG A_M;
- I6L, Jfix, Sawan or Hemkuver.

## 11. The E8 glue: the carrier sits inside the bath (`oes/glue.py`)

**Decomposition.**
- A4 = ⟨eᵢ − eⱼ⟩ is the carrier's own root system: its 20 roots are the oriented K5 edges.
- Its orthogonal complement in E8 is a second A4′.
- [E8 : A4 ⊕ A4′] = 5, and 240 = 20 + 20 + 200.

**The 200 mixed roots.**
- They project onto span(A4) as exactly the K5 vertex weights eᵢ − ⅕Σe and edge weights eᵢ + eⱼ − ⅖Σe, up to sign.
- A signed vertex pairs with the 10 weights of the twin 10; a signed edge pairs with the 5 weights of the twin 5. That gives 4 × 50 = (5,10′) + (5̄,10̄′) + (10,5̄′) + (10̄,5′).
- In SU(5) × SU(5)′ notation this is 248 = (24,1) + (1,24) + those four bifundamentals.

**Consequence (THEOREM).** ℓ²(V ⊔ E) is ℓ² of the A4 shadows of the mixed E8 roots. The carrier is not merely numerically related to the bath; it is a projection of it.

## 12. What a physical binding can be (`oes/binding.py`)

**Theorems.**
- **B1.** The only atom-diagonal symmetry of D is the global phase. No atom-dependent charge (hypercharge, colour, any diagonal gauge U(1)) commutes with the carrier dynamics. This sharpens the canon's removal of the hypercharge shell.
- **B2.** The commutant of D is M5 ⊕ M4 ⊕ M4 ⊕ ℂ ⊕ ℂ (dimension 59). The dark sector ker D = P5 carries an **exact U(5)** as its fundamental.
- **B3.** The native port breaks that dark O(5) completely: the stabiliser Lie algebra is 0. The only continuous symmetry left is the SO(2) rotating (a, b), whose Noether charge is the canon's angular charge.
- **B4.** The five zero modes have one chirality. Under any SU(5) ⊂ U(5) they are a single 5 with anomaly A(5) = 1 ≠ 0 (OBSTRUCTION). The minimal anomaly-free completion adds Λ²(ker D) = 10 at the opposite chirality, since A(Λ²5) = A(5) = 1. Λ²P5 is exactly where the native port's wedge a ∧ b lives, and 5 + 10 = 15 is the carrier's own state count.

**Conditional consequence (CONDITIONAL).** One carrier supports one anomaly-free 5 + 10, the state content of one Standard-Model generation. Nature has three (LEP N_ν = 2.984 ± 0.008), so the generation multiplicity is an explicit **operand of DYN_BIND**, not a carrier theorem.

**The structural route.** The route the mathematics points to is e8 ⊃ su(5) ⊕ su(5)′ (layer 11). Choosing it, and supplying the multiplicity and the chirality index, is the binding decision.

## 13. The gates, executed to the edge of their type (`oes/gatework.py`)

| Gate | Transition type | Done here | What closes it |
|---|---|---|---|
| **TIME_BIND** | metrology | Countermodel A replayed: τ and 2τ give identical records but frequencies in ratio 2:1. Sufficiency proved: one datum fixes τ uniquely, and frequency ratios are calibration-invariant. The canon's Salina square S·U_native(u) = U_phys(τu)·S holds to 6×10⁻¹⁵ (Prema follows). | **One authenticated clock datum** and the owner's choice of which native mode it labels. CTB9: unbound only for lack of metrology. (U7 recommends the electron Compton mode.) |
| **PredictionFreeze** | owner act | `data/prediction_register.json`: every calibration-invariant number the model fixes, with no fit; its SHA-256 is recorded in results.json. | The owner triggers the freeze, before any new comparison with data. |
| **W_L** (likelihood) | independent warrant | **Executed** on the canon's recorded physical candidate, the PMNS strict branch with sin²θ₁₂ = 1199/3759 and sin²θ₁₃ = 27/1280. The 22 Oct note calls it frozen; the PredictionFreeze gate itself was never triggered. Against the canon-recorded Bari Oct-2026 fit the pulls are +2.59σ and −1.98σ, χ² = 10.6 (2 dof), p = 0.005. Adding the reported NuFIT 6.0 strict-θ₂₃ pull (−4.8σ) gives χ² = 26.3 (3 dof), p ≈ 8×10⁻⁶. | **Result: NOT_PASS by evidence.** The candidate is excluded, which confirms the 28 Oct removal of PMNS from the carrier. |
| **T3081** | binary receipt | Maintainer side replayed on a second host: `dEchorate_room020002_src9_arr6_mics26-30.sofa` gives SHA-256 c39bc27f… and MD5 6f7aa37d… (1,724,358 bytes), identical to the FinalRun 15 Aug receipt. The method is also demonstrated on the native operand file. The official SOFA host (sofacoustics.org) and zenodo.org are denied by this environment's network policy. | Allow those hosts, then compare the maintainer copy `10E4VCAA1…` (SHA c39bc27f…) with the official bytes. |
| **AUTH / SCR6** | authenticated root | `data/owner_transaction.json` packages the canon's minimal ingress antichain {P_cl, SELECT_CERT, ROLE_BIND, G_role}, with SHA-256 for each operand and the uniqueness certificates. | **The research owner's signature.** SCR6 additionally needs its six physical operands, which belong to a chosen physical child. |
| **DYN_BIND** | physical choice | Constraints B1–B6 above. | The choice of physical child (H_sel), the generation multiplicity and the chirality index. |
| **ScientificGold** | independent warrant | Nothing can be promoted internally. | A frozen prediction, independent data and a preregistered test on a declared physical system. |

## 14. The six SCR6 operands

The canon defines them by shape only: H_D2 (2×2), C55 (55×55), F_phys (169×69, complex), Omega24 (24×24, skew), Z7 (31×7) and host_to_OES (5×18). It says they "cannot be filled with similarly shaped constructed matrices".

They are **physical by definition**: they are the interface to a chosen physical system. Mathematics cannot derive them; it can only reduce each to its minimal input. The 26 Oct U7 court did that reduction, and its table stands:
- gauge amplitudes need the scalar spectrum;
- Yukawas need running masses;
- the vacuum needs G_F;
- the M6 coframe needs a one-bit owner choice;
- the SI clock needs m_e;
- atomic H_Z needs α, m_e and nuclear data.

Its flavour benchmark rests on ε = 9/40 with "rationals chosen to fit", and §13 shows the recorded PMNS candidate fails. So the honest physical route is not to refit flavour. It is to declare the physical child, then freeze the register of §13 before testing.

**Choosing the physical child (CONDITIONAL; the owner's decision).** These options are compatible with the theorems above:

| Child | What the model already fixes | What the child adds | Status of its predictions |
|---|---|---|---|
| Particle physics (e8 ⊃ su(5) ⊕ su(5)′) | 5 + 10 per carrier, the glue, the anomaly structure | generation multiplicity 3, chirality index, scalar spectrum, one clock datum | flavour attempt (ε = 9/40) fitted; its recorded PMNS branch is excluded (§13) |
| Engineered network (LC or mechanical realisation of D, port and bath truncation) | every operand; only τ and an amplitude unit are free | fabrication tolerances | the register of §13 becomes directly testable; Gold would certify the model of that device, not of nature |
| Acoustic lane (dEchorate, T3081) | none of the room physics | host_to_OES (5×18) and the calibration chain | data lineage half-established (maintainer side replayed); no prediction frozen |

## 15. The scalar walk recurrence (`oes/recurrence.py`, `oes/walkfast.py`, `oes/ore.py`)

**Two engines.**
- The Weyl-orbit DP (`oes/walks.py`) gives exact integers W₀…W₉₀ (`data/walks90.json`).
- A second engine (`oes/walkfast.py`) uses E8 = D8 ∪ (D8 + s). With cᵢ = cos θᵢ the root sum is λ = 4e₂(c) + 128 ∏cos(θᵢ/2) + 128 ∏sin(θᵢ/2). Only even powers of the two spinor products survive the constant term, so

  W_n = Σ_q C(n,2q) 4^(n−2q) 64^q Σ_m C(2q,2m) E[e₂(c)^(n−2q) ∏ᵢ (1+cᵢ)^(q−m) (1−cᵢ)^m],

  where c₁…c₈ are independent cosines of uniform angles.
- One Gaussian variable removes the coupling e₂ = (e₁² − p₂)/2. Every step is then exact over F_p: Hermite–Gauss weights apply the Gaussian functional, and the eighth power is taken on roots of unity. W₀…W₆₀₀ mod p takes about 18 minutes per prime. `data/walks_modp.json` holds W₀…W₆₀₀ mod two primes and W₀…W₅₀₀ mod two more.
- The two engines agree on all 91 exact terms, mod all four primes.

**Exclusion.**
- A recurrence of shape (r, d) is also one of shape (r+1, d) and of shape (r, d+1). So the excluded region is a down-set, and only its corners need testing.
- Exact W₀…W₉₀: every recurrence has (r+1)(d+2) > 92. The canon's minimal admissible shape (10, 6) is excluded directly.
- W₀…W₆₀₀ mod p: every recurrence with **(r+1)(d+2) ≤ 455** is excluded. Full rank mod p implies full rank over ℚ, so given the residues this is a proof. In particular, order 10 needs degree ≥ 53, order 11 needs degree ≥ 49 and order 15 needs degree ≥ 36. The sibling's scalar-replay bound, (r+1)(d+2) ≥ 195 with order 11 needing degree ≥ 15, follows.

**The recurrence (THEOREM on the data; formed mod four primes).**
- The first kernels appear at product 456, shape (23, 17). Its kernel is 2-dimensional mod both 600-term primes, with 146 more equations than unknowns. Kernels follow at every order from 18 to 36, and at 39.
- These kernels are recurrences, and their greatest common right divisor over F_p(n) (`oes/ore.py`) is **one operator of order 16 and degree 58**, the same mod all four primes. Built from W₀…W₅₀₀, it also annihilates W₅₀₁…W₆₀₀.
- Its characteristic polynomial factors over ℚ. Every simple root has local exponent exactly −4 = −dim/2, the Morse value for a nondegenerate critical point in 8 dimensions. The double root −12 has indicial polynomial (α+4)(α+5). The 16 growth rates are:

  | in the band [−16, 240] (11, with multiplicity) | outside the real band (5) |
  |---|---|
  | 240 (band top), 16 (the 224 saddle), −3, −8, −10, −11, −185/16, −320/27, −12 (double), −16 (band bottom) | 340, −660, −20, −35, −120/7 |

- **The sibling's claims.** "(x+12)² divides the leading coefficient" holds: (z+12)² divides the characteristic polynomial. "Order 11" is the in-band part: 11 roots, counted with multiplicity. The operator found has order 16, because five growth rates lie off the real band. An order-11 annihilator is not excluded by the data (it would need degree ≥ 49), but it would have to be a right factor of this operator.
- **Still UNFORMED:** the rational coefficients (they need more primes), and a proof that the operator annihilates W_n for every n (by creative telescoping, or from an a-priori size bound).

## 16. Court U19.81, audited (`oes/court.py`)

The court (28 Oct) proposes an inverse-problem architecture: an 8-dimensional port split (5, 2, 1), Markov–Krein envelopes from moments through M₅₀, a Loewner–Pick test, H90 as a [9,3,7]₁₁ code, an observability-separation theorem and a clock-scaling obstruction. Its script is marked "pre-verified", but it does not run: its own assert fails. Each claim, checked:

| Claim | Finding | Status |
|---|---|---|
| sector eigenvalues A_bb = 241 on V₅, 235 on V₁; BB* = 183, 495 | correct | THEOREM |
| the script's walk generator | wrong from W₄ on (7,772,208 printed, 1,260,720 true) | OBSTRUCTION |
| the script's moment sequences | not positive definite at Lanczos step 3, so no measure has them | OBSTRUCTION |
| the script's uniform moment m_k − m_{k+1}/288 | wrong (39.17 at k = 1). The uniform moment over the clique is 6m_k − m_{k+1}/48 (= 235), because ⟨δ₀, Δᵏδ_α⟩ = m_k − m_{k+1}/240 for every root α | OBSTRUCTION; correction THEOREM |
| envelopes from M₀…M₅₀ (25 and 26 poles) | the script uses M₀…M₅. Rebuilt here from the true M₀…M₄₉: the true moments pass the Hausdorff test on [0, 256] exactly, and G₊ − G₋ ≈ 5×10⁻²⁸ at s = 64 | THEOREM |
| (G₋(s₁), G₊(s₂)) cannot be realized together | true, by Markov–Krein uniqueness of the extremal measure | THEOREM |
| the script's Loewner certificate for it | fails on the true moments: the "incompatible" cross choice also gives a positive slope (1.69×10⁹) | OBSTRUCTION |
| a [9,3,7]₁₁ MDS code correcting 3 errors | true (Cauchy construction, exhaustive decoding) | THEOREM |
| that code is H90 | nothing in the canon or this repository selects it | UNFORMED |
| ker O is the 4-dim cross block; 4 polarizations complete it | true | THEOREM |
| C5 clock symmetry reduces B to 2 parameters | false for every V₂ the court names. C5 acts as the identity on the 8² doublet of D², and on any C5-invariant 2-site probe (C5 has prime order, so orbits have 1 or 5 sites). So dim Hom_C5(V₂, U₂) is 0 or 4, never 2 | OBSTRUCTION |
| ω = Ω*√x fixes no clock scale | true; TIME_BIND stays UNBOUND | THEOREM |
| "complete expanded scalar polynomial annihilator" | not given anywhere. §15 forms one mod four primes (order 16, degree 58); its rational coefficients are not reconstructed | UNFORMED |

**Remarks in the same message.**
- **Cofactor 68 (THEOREM).** The literal 6×6 adapter's largest |cofactor| is 68, and no minor of size ≤ 5 equals 155 or 4805. By Cauchy–Binet, 4805 = cofactor₄₄(TTᵀ) = 21² + 48² + 43² + 11² + 3² + 9², the sum of the squared row-4 cofactors of T. So "cofactor 4805" supplies no five-dimensional operand, and that operand stays UNFORMED.
- **Scalar bound.** (r+1)(d+2) ≥ 195 is replayed and strengthened in §15, to ≥ 456, and the recurrence itself is then formed.
- **Preparation time (CONDITIONAL, proof received).** With a port budget polynomial in 1/ε, preparation time must grow at least as ε^(−1/2) for the monopole families, or ε^(−1/3) for a specified dipole target. The controlling 10:04 Canon Check proves this (Theorems P1–P6); §21 replays its identities. It is a necessary condition only, on the inherited exterior contract, and there is no matching preparation protocol yet.

## 17. The 28 Oct handover, audited (`oes/handover.py`)

The Locked Memory handover ("OES End-to-End & Spectral Model Handover — 28 Oct 2026") is replayed in layer 16. The paste-ready corrections are in [`HANDOVER_ADDENDUM.md`](HANDOVER_ADDENDUM.md).

- **Confirmed:** the gate banner and stoplines; ω₀ = 2; the carrier spectrum; the 7-design expansion; the root-line dispersive identities; the Schur boundary; the 156-coordinate realization; the MDS facts; and the critical census.
- **Critical census (new, THEOREM).** The vertices and edges of the E8 alcove carry **11 critical families, 243,600 points, Morse alternating sum 0**. Nine are vertices; two lie on edges (A6+A1 at λ = −185/16, A7 at λ = −320/27). Their 11 values are exactly the in-band characteristic roots of the order-16 recurrence of §15, so the band geometry and the walk data agree.
- **The literal five-dimensional operand (new, THEOREM).** Every column sum of the printed chart T₆ is 5, so T₆ preserves the contrast lattice V_c. T₆|V_c is a 5×5 integer operator with det 31 and irreducible characteristic polynomial x⁵ − 3x⁴ + 12x³ − 20x² + 31x − 31, so 155 = 5 × 31. The handover's "literal" T5×5 = (2I₄ − C_A4) ⊕ [5] is a construction (det 155). It is not in the operand file and not a block of T₆.
- **Corrections (OBSTRUCTION):**
  - the K6 wording of the carrier;
  - "order-11, degree-5" as an exact recurrence (excluded; the exact operator has order 16);
  - P25 as an annihilator of the moments or of W_n;
  - (15/13)r², which should be (15/16)r²;
  - ker O ⊆ ker C, which is reversed;
  - "multi-frequency criterion verified" for the court script.
- **UNFORMED:** H90 identified.
- **REPORTED:** the paper digest, Tr₁/Tr₂, the Miller recurrence, the 8-dim dispersive bound, the Floquet monodromy, the preparation constant, B_geom, and the mediant collar.

## 18. Sound, light, frequency and phase on the K5 edges (`oes/waves.py`)

The ten edges of K5 carry one Hodge complex. The canon's oriented boundary is the signed incidence B. The gradient is d0 = Bᵀ (vertices → edges), and the curl is Curl = ⋆d₁ (edges → the ten triangles → edges, by the Hodge star of the 4-simplex). d₁d₀ = 0 and the ranks are 4 + 6 = 10, so the complex is exact.

**Sound and light (THEOREM).**
- **Sound** is im d₀: the 4 longitudinal edge modes, the velocity fields of the acoustic system ṗ = −d₀ᵀu, u̇ = d₀p. Its operator is BBᵀ = 5I − J = ½Σ_{α∈A4} ααᵀ, the long-wave Hessian of the carrier's own root lattice.
- **Light** is ker d₀ᵀ: the 6 transverse edge modes. This is the cycle space L6, which is the native port space. Curl is symmetric, with Curl² = d₁ᵀd₁ and eigenvalues ±√5 (3 each) on light and 0 on sound. In the canon's fundamental-cycle basis, Curl on the cycles is exactly −A, where A = (6I − G)σ is the Hodge block of layer 1. The canon already had the light operator.
- **One frequency.** d₀d₀ᵀ + Curl² = 5·I₁₀, so sound and light are isochronous at ω = √5. The carrier's vertex frequencies are the complements: MMᵀ + BBᵀ = 8I, so ω²_carrier + ω²_sound = 8 on every vertex mode (8 + 0 uniform, 3 + 5 contrast).

**Phase (THEOREM).**
- The order-5 edge tick fixes both sectors. Sound carries the C5 phases ±72° and ±144°, and none at 0 (trace −1).
- The two curl eigenspaces are **helicities**. Odd permutations swap them and even ones keep them.
- Under the rotation group A5, the helicities are the two **icosahedral 3-dim irreps** and sound is the A5 **4**. Curl = −√5 carries the 72° class (5-cycle character φ), and Curl = +√5 carries the 144° class (character 1 − φ). Each also has one phase-0 mode.
- **Selection rules.** No S5- or A5-equivariant map takes sound to light. The C5 clock allows exactly 4 real phase-matched parameters. A 72° sound mode can only become light of the matching helicity, and the two phase-0 light modes stay dark to sound.
- **Resonant conversion (CONDITIONAL).** Because the sectors are isochronous, any C5-equivariant coupling converts a sound mode completely (fraction 0.99999) into its matched helicity. The other helicity and the phase-0 modes stay at 10⁻¹⁶. The coupling itself is not a canon operand.
- **Two C5 actions.** The carrier's edge operator MᵀM commutes with the unsigned tick and not with the signed one. Matter and sound/light carry two different C5 actions on the same ten edges.

**Through the native chain (THEOREM).**
- The literal port (source wedges → light, via `Fedge_native_inverse`) is S5-equivariant and drives each helicity with rank 3. Its 4-dimensional kernel is the A5 4, the same type as sound: the port cannot emit sound directly.
- A source at frequency 2 drives light only at frequencies 0 and 4. A circular source gives pure frequency 4 with doubled phase 2φ.
- The bath's sound speed² on the carrier's 4-plane is 30 = 5 (the A4 roots) + 0 (A4′) + 25 (the 200 mixed roots of layer 11), and it is isotropic.
- The band has no critical value in (0, 224), so the port frequency (ε = 16) radiates into its smooth acoustic part. There k ≈ 0.7404, with phase and group velocities 0.986 and 0.959 of √30 (ARITHMETIC; the directions differ only at order k⁸).

**Frequency ladder (native units).** 0 (dark) < √3 (carrier contrast) < 2 (source) < √5 (K5 sound = light) < 2√2 (carrier uniform) < 4 (port) < √224 (bath saddle) < 16 (band top).

**Physical sound and light (CONDITIONAL).** "Sound" and "light" name the longitudinal and transverse sectors. Binding them to physical fields needs DYN_BIND, and absolute frequencies need TIME_BIND. The calibration-invariant content is the ratios:
- light/sound = 1;
- carrier² + sound² = 8;
- port/source = 2;
- (bath/K5 speed)² = 6.

## 19. The 14:16 snapshot, rebuilt (`oes/snapshot.py`)

The sibling snapshot (`one-machine-20261028.pdf`, `oes-model-20261028.zip`, `STATUS_20261028.md`, Drive, 14:16 UTC) adds the cube, the 24-step readout, two Hankel matrices, the Spanda action on the 31 subsets, the frequency squares on the 4320-circle, and the Agni–clock–doubling chain. Its TypeScript audits mostly compare typed constants. Layer 18 recomputes each item from matrices, and settles three items the snapshot left open.

**Settled here (THEOREM).**
- **Density on the nine-torus.** The nine positive critical energies 224, 243, 248, 250, 251, 4025/16, 6800/27, 252, 256 (the two families at 252 share one) have the distinct square-free parts 14, 3, 62, 10, 251, 161, 51, 7, 1. By Besicovitch, their square roots are linearly independent over ℚ, so by Kronecker the flow of the nine bath frequencies is dense on T⁹.
- **The Hessians.** All eleven critical families are recomputed. sign det H = (−1)^index, and count · i^index/√|det H| reproduces every coherent coefficient printed in the snapshot paper. The determinants are 60⁸ at the maximum, 3⁸ for A8, 2¹⁶ for A7+A1 and D8, and 5⁸ for A4+A4.
- **Walk asymptotics from the 7-design alone.** log(1 − ε/240) = −s/8 − s²/640 − s³/23040 with s = |k|², and Laplace's method gives

  W_n = (16/π⁴)·240ⁿ·n⁻⁴·(1 − 2/n + (23/15)/n² + O(n⁻³)).

  The exact W₅₀…W₉₀ follow it. The residual ((R_n − 1 + 2/n)n² − 23/15) falls from −0.0069 at n = 50 to −0.0038 at n = 90.

**Replayed from matrices.**
- Agni = 5I − G is the light operator: Agni = Curl² = d₁ᵀd₁, G = d₀d₀ᵀ is the sound operator, and Agni + G = 5I (layer 17).
- The edge doubling T (10×20) has TTᵀ = 2I, every row is null for the pair signature, and rank BT = 4. All of this is immediate.
- The five-port site block (SELECTED_REFERENCE) has:
  - moments 0, 0, 0, 1/3, 0, −8/9, 0, 55/27 and recurrence H_{k+4} + (8/3)H_{k+2} + H_k = 0;
  - controllability determinant −1/3 and observability determinant −1/27;
  - Hankel determinant 1/81 (6561 once cleared by 27);
  - frequencies² (4 ± √7)/3.
- The cube:
  - Laplacian spectrum 0, 2³, 4³, 6;
  - middle operator L(6I − L) with M² = 8M and rank 6;
  - the reader pair sees ranks 2 then 4; four of the six third readers reach 6;
  - decoder det −1, with noise gains 46 and 66.
- Spanda on the 31 subsets: 7 fixed, 24 moved, traces 31, 7, and trace-Hankel determinant 912. On the K5 edges the same double transposition is even: it keeps both helicities, with traces 0 on sound and −1 on each helicity.
- The 4320-circle: the day has order 24 and the pada order 108; they meet in the order-12 step; the order-5 rotor misses the day. The squares 3, 4, 5, 8, 16 divide 4320, and no bath energy does.

**Corrections (OBSTRUCTION).**
- (I + S)/2 is a Markov projector of rank **19** (7 fixed subsets plus 12 symmetrized pairs), not 7.
- The snapshot paper's front table still says "the recurrence order is 11". The operator of §15 has order 16; 11 is the degree of its in-band characteristic part.

## 20. The integrated spine, rebuilt (`oes/spine.py`)

The sibling's integrated build (`one-machine-20261028-integrated.pdf`, `oes-integrated-20261028.zip`, `INTEGRATED_20261028.md`, Drive, 15:31 UTC) puts the readings of the 4320-circle on one spine:

> The Coxeter number 30 cuts 4320 into 144. Six of those steps make 864. Five of those close the circle. … Every one of the 4320 elements sits in the tower 36 × 12 × 2 × 5 = 4320. … The path stops where 7 does not divide 4320, the pada step 40 is not in the order-10 subgroup, the Krishna lift is not a sum of 4 and 5, Prema's stage index 13 is not her width 2.

In the sibling model these are integer comparisons (the Krishna stop is `4 + 5 !== 4`). Its paper says that "no stored map sends a yuga tick to a lattice vector or a Morse point". Layer 19 checks every circle statement with one lemma. It then builds the map that the paper says is missing: the E8 Coxeter element, whose order is the 30 the spine starts from.

**One lemma (THEOREM).** Z/4320 has exactly one subgroup ⟨d⟩ for each of its 48 divisors d, of order 4320/d. ⟨b⟩ ⊆ ⟨a⟩ iff gcd(a, 4320) | gcd(b, 4320), meets are lcms and joins are gcds. All 28 circle statements of the integrated build hold under this rule. A name such as sun, moon, pada or Prema is a reading of a step; the step decides every check.

**Corrections (OBSTRUCTION).**
- DOTS_LATTICE calls the meet of the pada and the cycle "36, the atlas". ⟨40⟩ ∩ ⟨6⟩ = ⟨120⟩ has *order* 36 (the moon); the atlas ⟨36⟩ has order 120. The paper itself says "The order 36 is not the atlas".
- "Meet at order 2, whose only element is 2160": the subgroup is {0, 2160}.
- "360000 is not a step": 360000 ≡ 1440 (mod 4320), so the W₀ scalar reduces to the sun step.
- "Siri and Shay, both 4 … Their sum 5 has order 864": Siri + Shay = 8 (Rughnath, order 540). The 5 is Prema + Sai.
- The doubling residues 1, 2, 4, 8, 7, 5 have orders 4320, 2160, 1080, 540, 4320, 864. The paper lists the last two swapped.
- "Rank 8 times the mark sum 30 recovers the 120 positive roots": 8 × 30 = 240 is all the roots; the positive roots are 8 × 30 / 2. (The model code has the /2.)

**The spine refined (THEOREM).**
- The Coxeter subgroup ⟨144⟩ (order 30) lies between the order-10 subgroup ⟨432⟩ and the atlas ⟨36⟩. So the tower is 36 × 4 × 3 × 2 × 5, and the address x = d₀ + 36d₁ + 144d₂ + 432d₃ + 864d₄ is a bijection on all 4320 elements. The integrated tower 36 × 12 × 2 × 5 skips the subgroup the spine starts from.
- There are 504 = 9!/(5! 3! 1!) maximal chains of subgroups, and exactly 6 contain the whole spine.
- The Coxeter step is the sum of the named prime-order steps: 864 + 1440 + 2160 ≡ 144 (mod 4320), i.e. tick + sun + half-turn.
- The pada lies on no chain with the tick (5 and 108 are incomparable). Pada + tick = ⟨8⟩, the coil of §8, an internal direct sum C₁₀₈ ⊕ C₅ (OBSTRUCTION).

**The Coxeter clock (THEOREM).**
- c = s₁s₂⋯s₈ in W(E8) has order 30, c¹⁵ = −I, and characteristic polynomial Φ₃₀ = x⁸ + x⁷ − x⁵ − x⁴ − x³ + x + 1.
- Its exponents are the units mod 30: 1, 7, 11, 13, 17, 19, 23, 29. They sum to 120 (the positive roots), and the degrees m + 1 multiply to |W(E8)|. So 7 is an exponent of E8.
- c permutes the 240 roots in 8 free orbits of 30. It therefore commutes with the bath walk operator and preserves the band λ. It is a symmetry of the existing action, not a new term.
- SELECTED_REFERENCE: 144 ↦ c, one of the φ(30) = 8 isomorphisms ⟨144⟩ → ⟨c⟩. No homomorphism from the whole circle extends it, since φ(27) = 18 > 8 means no element of GL₈(ℤ) has order divisible by 27 (OBSTRUCTION).

**Fixed momenta and Morse points (THEOREM).**
- c^k fixes |det(c^k − I)| Bloch momenta: 25 for the order-5 powers (the tick), 81 for the order-3 powers (the sun), 256 for c¹⁵ (the half-turn 2160), and only the origin for the other 22.
- A fixed momentum of an element without eigenvalue 1 is a critical point of the band, because the gradient there is fixed by that element.
- The tick fixes the origin and 24 points of A4+A4 (ε = 250, index 4).
- The sun fixes the origin and 80 points of E6+A2 (ε = 243, index 2).
- The half-turn fixes all 256 half-periods: the origin, the 120 points of E7+A1 (ε = 224) and the 135 of D8 (ε = 256).
- The fixed groups are (ℤ/5)², (ℤ/3)⁴ and (ℤ/2)⁸.

**Two carriers (THEOREM).**
- A conjugate c′ = wcw⁻¹ satisfies c′⁶ = r r′ exactly. Here r is the K5 vertex rotation, acting on the 20 oriented K5 edges of the carrier's A4 (§11), and r′ is a Coxeter element of the twin A4′. **The tick turns two carriers.**
- In standard coordinates, c′ = M/2 with M a signed 0–1 matrix having four nonzeros per row.
- The sun c′¹⁰ turns four triangles (A2⁴, index 9), and the half-turn flips eight edges (A1⁸, index 16). For p = 2, 3, 5, the order-p Coxeter element rotates 8/(p−1) copies of K_p and fixes p^{8/(p−1)} momenta.
- c′ = (−I)·c′¹⁰·c′⁶, matching 144 = 2160 + 1440 + 864.
- The yuga segments act as 1728 ↦ (rr′)², 864 ↦ rr′, 1296 ↦ −(rr′)⁴ and 432 ↦ −(rr′)³.

**Where 7 enters (THEOREM).**
- The normalizer of ⟨c′⟩ has order 240 = 30 × 8. Every exponent is realized by conjugation, and the centralizer is ⟨c′⟩.
- No element of order 24 commutes with c′, and the order-24 elements that normalize it turn it by 7 or 13 = 7⁻¹.
- The day clock d (order 24, characteristic polynomial Φ₂₄) agrees with the Coxeter clock on the circle's common subgroup ⟨720⟩ (d⁴ = c′⁵) and satisfies d c′ d⁻¹ = c′⁷.
- The circle's atlas 36 = 180 − 144 has order 120, but on the bath d c′⁻¹ has order 24. The 7 at which the sibling's path stops is the exponent through which the day acts on the Coxeter clock.
- The order-20 clock ⟨216⟩ normalizes it with the twist 11. No element of order 18 normalizes it.
- On the circle itself, x ↦ 7x is an automorphism of order 36, and there is no element of order 7.

**What can act on the bath (THEOREM, OBSTRUCTION).**
- A subgroup of the circle acts faithfully on the bath lattice exactly when its order is one of 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30. Each of these is realized by an explicit element of W(E8).
- The exclusions:
  - the degree bound leaves only 16, 36, 40 and 60 above these;
  - 16 falls by Sylow inside W(D8);
  - 36 falls because its fourth power lies in an E6 whose complement A2 has no automorphism of order 4;
  - 40 and 60 fall because their power lies in an A4. All 5,806,080 ordered A4 chains are one orbit, and Aut(A4) has no element of order 8 or 12.
- The maximal clocks are ⟨144⟩ (30), the day ⟨180⟩ (24), ⟨216⟩ (20) and ⟨240⟩ (18).
- The spine acts on the bath up to the Coxeter subgroup and stops at the atlas. The moon (36), nakshatra (27), pada (108) and atlas (120) subgroups cannot act at all.

**Arithmetic and reported.**
- ARITHMETIC: 69120 = |W(E8)|/|W(A6×A1)|, the A6+A1 family, and also the Human Design count. Exactly three families are whole numbers of circles: A6+A1 (16), A7 (4) and A7+A1 (2). The 29 non-identity Coxeter powers fix 540 momenta in all.
- REPORTED: the Krishna lift and Prema's stage index, whose typed operands are not in this repository.
- UNFORMED: the epoch, birth time and ayanamsha.

## 21. The latest canon, synchronized (`oes/canon_sync.py`)

Before building further, layer 20 reads the canon as of 16:30 UTC on 28 Oct, reads it again at 16:49, and reconciles this model with it.

**Canon position.** The Quick Access workbook was updated at 15:05 UTC, with a source cutoff of 14:59:48. In it, OMSOON736 and the 10:04 Canon Check stay controlling. This repository's 14:37 build is listed as a SELECTED REFERENCE, and its replay as SOURCE-REPORTED EXECUTION. Layers 19–20, the sibling's later builds and the separate "major upgrade" model all arrived after the cutoff.

**One correction to this model (now in layer 1).** 3|x|⁴ − 7Σx⁴ is harmonic only for the ambient Laplacian of ℝ⁵. The contrast plane's own harmonic quartic is 2|x|⁴ − 5Σx⁴, as the canon now states.

**A canon claim proved (THEOREM).** The 12:32 update says "maximum group speed exactly √30". It holds as a supremum. |∇ε|² ≤ 120ε everywhere, because

|u·∇ε|² = |Σ (u·α) 2 sin(α·k/2) cos(α·k/2)|² ≤ Σ(u·α)² · 4Σ sin²(α·k/2) ≤ 60 · 2ε,

using the frame Σαα^T = 60I. So |∇√ε| ≤ √30. The bound is approached as k → 0 and never attained. On 20,000 random momenta the ratio |∇ε|²/(120ε) stays below 0.71.

**The controlling Canon Check.**
- *Theorem P1/P2 (preparation).* The identities are replayed:
  - the Bernstein-ellipse identity 128 + 64(w + w⁻¹) = 64(v + v⁻¹)², with |Im √E| = 16 sinh(η/2)|sin φ|;
  - ‖C‖² = 495 from C*C = 183P_c + 495P_u;
  - the optimum η* = 2 arcosh(d/8T), with exponent 2√(d² − 64T²) − 2d·arcosh(d/8T), strictly convex in η.

  The horizon laws ε^(−1/2) (monopole) and ε^(−1/3) (dipole) stay CONDITIONAL on the inherited exterior contract, which layers 3–4 confirm.
- *Theorem S1.* (r+1)(d+2) ≥ 195, r ≥ 11, and "r = 11 needs d ≥ 15", together with its whole table, follow from layer 14. Layer 14 excludes every shape with (r+1)(d+2) ≤ 455, so r = 11 needs d ≥ 36. The order-16, degree-58 operator has product 1020.

**The sibling's notes of 15:57–16:18 (THEOREM unless marked).**
- The following hold:
  - the CRT idempotents 3105 = 23·135, 2080 = 13·160 and 3456 = 4·864: their squares, zero products and sum 1;
  - the primary split, including 144 = 2160 + 1440 + 864, this repository's §20 splitting, which the sibling adopted;
  - the 234/522 joins, the orbit indices 5, 4, 20, 40, 720, the address 1234, and the C30240 register.
- **Correction (OBSTRUCTION).** "The five added channels are the step 5, which generates the tick" and "the step 25 generates the tick subgroup, order 864" are wrong. ⟨5⟩ = ⟨25⟩ is the subgroup of *order* 864, of index 5. The tick ⟨864⟩ has order 5. The step 5 is dual to the tick.
- **NORMALIZE refined.** In W(E8), the day clock and the Coxeter clock generate a group of order exactly 120, with d⁴ = c′⁵ and d c′ d⁻¹ = c′⁷. The abstract semidirect product C₃₀ ⋊ C₂₄ of order 720 cannot embed, because the normalizer of ⟨c′⟩ has order 240.

**The sibling's notes of 16:31–16:43, read at 16:49.** SPINE_CORRECTIONS takes over the six circle corrections of §20, and so does the sibling paper of 16:43. The 16:47 consolidation (CURRENT_20261028_2046) restates these notes, and its paper's text is identical to the 16:43 paper. COXETER_POWERS, ATLAS_FACTOR and SUN_MOON add circle statements. All of them hold (THEOREM):
- c^k for the steps 144, 432, 720, 864, 1440, 1728 and 2160 cycles the 240 roots as 8 × 30, 24 × 10, 40 × 6, 48 × 5, 80 × 3, 48 × 5 and 120 × 2, and fixes no root;
- the refined tower is 1, 4, 12, 24 and 120 atlases. The identity 12 + 24 = 36 is the same statement as 432 + 864 = 36²;
- twelve moons make the sun. The sun is c¹⁰ and pure of order 3. The moon is no Coxeter power, its primary parts are 1080 + 3360 + 0, and it meets the atlas in the signs.

Further results:
- **The fixed momenta, which the notes leave unreplayed (THEOREM).** Fixing no root is not the same as fixing no momentum.
    - On the Brillouin torus, c^k fixes |det(c^k − I)| = Φₙ(1)^(8/φ(n)) points, where n = 30/gcd(k, 30). This holds for every k.
    - The count is 1 at orders 30, 15, 10 and 6, 25 at order 5, 81 at order 3, and 256 at order 2. It is nontrivial exactly when n is a prime power.
    - These are the 25/81/256 Morse points of §20.
- **The commuting clocks (THEOREM).** SPINE_CORRECTIONS says "the circle still makes the day and Coxeter clocks commute".
    - On the circle this is true: the two generate the atlas, of order 120.
    - On the bath it fails. No element of W(E8) of order 24 commutes with c′, because the centralizer of c′ is ⟨c′⟩, and no element has order 120.
    - A realized day clock must therefore twist the Coxeter clock. §20 shows that it twists by 7.
- **Shared integers (ARITHMETIC).** These are equal integers only; no map joins them.
    - The cycle counts 24, 40, 48, 80 and 120 are the day order, the pada step, the number of subgroups, the order of 162 and the atlas order.
    - The sun is 40 atlases, the pada step. The half-turn is 60 atlases, the frame constant.
    - The squared stiffness ratio 8/3 is Coxeter cycles over the sun's cycle length.
- **What remains in the 16:43 paper.**
    - One remnant (OBSTRUCTION). Its circle-subgroup theorem still says "360000 is not a step", while its own spine theorem says 360000 reduces to 1440.
    - The harmonic statement is still doubled. §13 calls 3|p|⁴ − 7Σp⁴ the harmonic line on the contrast plane, computed with the ambient Laplacian. The moment theorem calls 2s₂² − 5s₄ invariant-harmonic and 3s₂² − 7s₄ not. Each is right for its own Laplacian.

**The separate model replayed (THEOREM).** This is "Finite Spectral Dynamics with Complete Observation and Exact Cyclic Addresses" (finite-spectral-model-major-upgrade-20261028). Its claims are rebuilt here from its definitions:
- Five fixed channels are necessary and sufficient. The identities are RH = I₁₅, P₀ = I − 11K/24 + K²/24, D⁺ = (11D − D³)/24 and HᵀWH = K + P₀.
- Of the 252 five-edge sensor designs, 162 are complete and 90 have rank 4. Every complete design has det 1/162. 72 are optimal: their spectrum is (λ − ½)(λ² − λ + 1/9)², with minimum eigenvalue (3 − √5)/6, attained for example by {01, 02, 03, 12, 14}. The other 90 have spectrum (λ − 1)(λ − ⅓)²(λ² − (5/6)λ + 1/18).
- The 25-coordinate flag geometry:
  - E: ℂ¹⁵ → ℂ²⁵ is an isometry with DE = ED;
  - spec D² = {0¹⁵, 3⁸, 8²};
  - the real structure and grading relations and the first-order condition hold;
  - the intersection form has det −48.
- The vertex distance is exactly √(8/7). By convexity and the symmetries of the problem, an optimal a is s(e_p − e_q), and ‖[D, π(e_p − e_q)]‖² = 7/2.
- The collocated transfer functions G_V = (z²+7)/((z²+3)(z²+8)) and G_E = 1/(2z²) + 2/(5(z²+3)) + 1/(10(z²+8)) follow from the spectral projectors.

**Recorded, not replayed (REPORTED).**
- The 12:32 claims that remain SOURCE-CLAIMED in the canon: convexity through E = 224 and a matching t^(−9/4) upper bound.
- The separate model's 17,914 checks.
- COURT_CORRECTION (403/25 versus 402/25; 328320 versus 293760) is arithmetic and holds.

## 22. The ledger, unified (`oes/ledger.py`)

At 18:20 UTC the canon and the sibling's newest build were read again:

- the Quick Access sheet 00_FULL_RECONCILIATION_20261028 (review cutoff 17:19:41), in which OMSOON736 stays controlling, no Matrix ID is new and every frozen gate is kept;
- the sibling's CANON_READ (17:06), which adopts the corrections of §21;
- the sibling's full edition and FULL_UPDATE (18:17), with forty join notes from 17:01–18:17.

The full edition notes twice that "the order-24 element was not constructed". Layer 21 replays every join of that ledger and puts the result in one table, [`docs/LEDGER.md`](LEDGER.md). The paper is `docs/paper/one-machine-20261028-unified.md`.

**The tick bit (THEOREM).** For every x, the tick 864 = 2⁵·3³ lies in ⟨x⟩ iff 5 ∤ x, iff 3456·x ≢ 0 (mod 4320). So:

- 24 of the 48 subgroups hold the tick;
- each subgroup holds all five tick levels or only 0;
- every width prime to 5 satisfies width × index = 864;
- 16 of those 24 have order divisible by 20;
- the bit is not additive: 2 and 3 hold the tick, and 5 does not.

The ledger's 129 tick sentences, from 35 joins (energy, golden, observer loop, mirrors, phase, charge, spin, heat, monopole, field, Einstein, two 36s, sign tensor, Om, karma, japa, mantra, bubbles, horizon, above and below, and the 17:01–18:01 notes), are this bit. The check covers their step counts and indices and 38 stated subgroup orders. The numbers riding on the bit are counts (ARITHMETIC).

**One group for every clock (THEOREM).** All of these sit in the normalizer of ⟨c′⟩ in W(E8), of order 240:

- **The tick is a commutator.** d c′ d⁻¹ c′⁻¹ = c′⁶ = r r′. The twist by 7 and the two-carrier tick are one fact. This is the tick of the Coxeter clock in W(E8). It equals the circle element 864 only through the embedding c′ᵏ ↦ 144k of ⟨c′⟩ alone, and that embedding does not extend to the day–Coxeter group (§23).
- **The day–Coxeter group** G = ⟨c′, d⟩ has order 120. Its centre is ⟨c′⁵⟩, the shared ⟨720⟩. Its derived group is the tick, and its abelianization is cyclic of order 24, generated by d. The day doubles the tick: d (r r′) d⁻¹ = (r r′)².
- **Five day clocks.** G has five conjugates of ⟨d⟩. The tick rotates them (x ↦ x + 1), the day doubles them (x ↦ 2x, pentagon to pentagram), and the centre fixes them. So G/Z(G) is the affine group AGL(1,5): the ledger's "twenty affine maps" and its "the doubling does not commute with the rotation".
- **The golden clock.** The 24 elements of order 20 all have twist 11, and v with v² = c′³ has v⁴ = the tick. The same law holds for ⟨216⟩ on the circle and for B = [[1,1],[1,0]] mod 5, where B has order 20 and B⁴ is unipotent. The affine 20 is not cyclic.
- **Mirrors.** The circle's x ↦ −x is realized by the 30 elements with twist −1. Each inverts the clock and the tick. Ten of them are involutions that keep the carrier: five act on it as the pentagon reflection, which fixes three atoms, and five as its negative. On the fifteen atoms the graph reflection keeps D², and the involution i ↦ 14 − i does not.
- **Carrier exchange.** The stabilizer of {A4, A4′} in W(E8) has 57,600 elements. The 28,800 that keep both act on the glue Z/5 by ±1. The 28,800 that exchange them act by ±2 and have orders 4, 8, 12 or 20. **No involution exchanges the carrier and its twin.** The day's quarter d⁶ is one exchange, with (d⁶)² = −I.
- **Explicit elements.** `data/clocks.json` holds the clock, the tick, r, r′, the day (order 24), the golden clock and the mirror, as 4 × elements of W(E8) in standard coordinates. Every relation is checked again from the file alone. `ports/ts/ledgerJoins.ts` carries them into the sibling's app.

**Physical names.**

- **Energy (THEOREM).** The checked datum has quadratic form 64 = 40 + 6 + 18. Its energy is 34 = 20 (uniform) + 3 (vertex contrast) + 9 (edge image) + 2 (cycle). E_V = 23 and E_E = 11 are conserved separately, because D² is block diagonal (§5). The ledger's stored 12 + 20 + 2 groups these pieces by spectral sector; §23 puts the three splits in one table.
- **Entanglement (CONDITIONAL).** Under canonical quantization the oscillating modes evolve as U_V ⊗ U_E, so the carrier cannot entangle vertices with edges.
- **Spin counts (THEOREM).** The 112 integer roots are D8, and the 128 half-integer roots are one W(D8)-orbit, so 248 = so(16) + 128. [W(E8) : W(D8)] = 135 is the D8 family of the critical census, and the half-turn's 256 fixed momenta are 1 + 120 + 135.
- **Field (OBSTRUCTION).** q̈ + 4q = 0 has frequency 2, but 4 ∉ spec D², so the source is not a carrier mode.
- **SMEAR_JOIN (THEOREM).** The 81-cell 4-cube has Laplacian spectrum 0, 2, 4, 6, 8 with multiplicities 1, 8, 24, 32, 16, and trace 432.
- **Not formed (UNFORMED).** Source infinity, foam, the double slit, a Bell count, the photoelectric effect, a work function, electron, photon, proton, Compton and Bohr lengths, and 19 Standard-Model parameters. No operand is stored, and the action has no dimensionful constant.

## 23. Counts, graphs and moments (`oes/counts.py`)

At 19:21 UTC Drive was checked again. Two sources were new:

- the sibling's 28 notes of 18:32–19:21, each with a paper edition (LEVEL_TICK through MOMENT_BIT);
- the canon sheet 00_CURRENT_20261028_1910 (continuation 3, review cutoff 19:10:16). OMSOON736 stays controlling and every frozen gate is kept. The sheet records this repository's 21 layers, 412 checks and 31 tests as source-reported, and still lists the order-16 coefficients as missing.

Layer 22 replays both. Its rows are in [`docs/LEDGER.md`](LEDGER.md), after the rows of layer 21.

**Counts on the bit (THEOREM).** Most of the notes read one more stored integer on the bit of §22. The table `CLAIMS` holds 412 such readings from 48 notes: 223 from the 19:21 batch, 103 from the 19:57 batch, 26 from 20:12, 46 from 20:25 and 14 from 20:33. Each one is checked together with what the note states about it: an order, a subgroup, a step count, a residue, or a first landing. The first landing is the least k for which kx is a nonzero tick level. None fails.

- Twelve of the fifteen stages (Mālinī 1 … Pratyabhijñā 14) meet the tick, and 0, 5 and 10 do not. Their landings match SANSKRIT_DEEP and EVERY_WORD.
- Buddhi (2) and Pratyabhijñā (14) generate one subgroup and take 432 steps each, but land on 864 and 1728.
- The sums and products riding on the bit are counts (ARITHMETIC). That includes the family quotient 3n² + n + 1, which is 31 only at n = 3.

**Graphs (THEOREM).**

- **K5.** Cut rank 4 and cycle rank 6. The signless kernel on the edges has dimension 5, and it is the zero-mode space of D². The blocks of D² are M Mᵀ = 3I + J and MᵀM. The six star-tree cycles have Gram determinant 125, which is the spanning-tree count. K5 has fifteen 4-cycles.
- **Petersen.** It is the disjointness graph of the ten edges, with degree 3 and 15 edges. (A − 3)(A − 1)(A + 2) = 0, and its exact projectors are orthogonal, have ranks 1, 5 and 4, and add to I.
- **Pentagon and pentagram.** C5² = 2I + pentagram. The doubling (order 4, 0 fixed, 1 → 2 → 4 → 3) carries the pentagon onto the pentagram, and with the rotation it generates the 20 affine maps. Doubling mod 6 is not a permutation.
- **Companions.** The breath companions of 3 and 8 square to −3I and −8I. Their determinants are 3 and 8, so no power is I. The golden companion B has infinite order over ℤ (its powers are Fibonacci matrices) and order 20 mod 5. The hourglass on thirteen points is an involution with ranks 7 + 6.

**The root graph and the moments (THEOREM).**

- **Root walks.** The closed walks at every root are 1, 0, 56, 1512 and 62160. They come from the A² row 56, 27, 12, 1, 0 at inner products 2, 1, 0, −1, −2. The frame identity is Σ ααᵀ = 60 I₈.
- **MOMENT_BIT, replayed.** The sibling read seven reported moments on the bit and said they were not replayed. Their source is the Locked Memory moment notes of 24–25 October. They are ⟨p, Δⁿp⟩ for the alternating hexagon port: the six roots of an A2 with signs + − + − + −, on the infinite E8 lattice, with Δ = 240 − Σ of the root translations.
  - Computed here exactly from the 240 roots, they are 1, 242, 58691, 14259954, 3470101592, 845582723240, 206295748792515.
  - The next one is new: μ₇ = 50383499822338790.
  - §8 records a "rotor hex6" with these properties (m₁ = 242, Hankel determinants positive) but without its operand. This port supplies one.
  - The variance is 127 and the central third moment is −4736. The Jacobi stiffness is K_R = [[242, 127], [127, 25998]], and the Hankel determinants are 1, 127, 15930273, 3540294987045875.
- **Square and octagon ports.** The canon's square port m₀…m₇ (4, 968, 234808, …, 202013532870796200) and the octagon's 58713, 14274162 and 3476302936 are replayed. square = (hexagon + octagon)/2 holds at every order. The reason: the three ports' difference distributions are proportional on the shells 0, roots, norm 4, norm 6 and twice a root, and each shell is one Weyl orbit (240, 2160, 6720, 240). The identity is checked directly through n = 6.
- **The deep hole.** The root-walk note's deep hole is the band vertex v* = π(1,1,1,1,0,0,0,0) of §8, where Δ's symbol is 256, so 256 ∈ spec Δ. The bound sup spec Δ = 256 stays reported. Two sources report it: the alcove branch-and-bound of §8 and the root-walk note of 25 Oct.

**The order-120 clock.**

- **Element orders (THEOREM).** They are 1:1, 2:1, 3:2, 4:10, 5:4, 6:2, 8:20, 10:4, 12:20, 15:8, 24:40 and 30:8. Its only involution is the central −I = c′¹⁵, and it has four elements of order 5.
- **ICOSA's Hurwitz value (OBSTRUCTION).** The value 6 = 120·(−2) + 60 + 90 + 96 is 2g − 2 for signature (2, 4, 5), so g = 4. S5 realizes it: all 120 of its (2, 4, 5) pairs generate it. The stored clock has no (2, 4, 5) generating pair, so it does not realize that surface. Its 24 is 120/5, not a count of five-cycles.

**Three sharper statements (THEOREM).**

- **The commutator and 864.** The canon notes that a commutator is not the circle element 864 without a map. The clock has exactly 24 homomorphisms to the circle. Every one kills c′⁶ = [d, c′] and sends c′ into ⟨720⟩. The Coxeter clock alone embeds by c′ᵏ ↦ 144uk (u a unit mod 30), which sends c′⁶ to a nonzero tick (864 for u = 1). None of these embeddings extends to the clock.
- **The energy table.** The canon notes that equal totals do not make equal decompositions. The three splits are one conserved table, by block and D² sector:

  | | sector 0 | sector 3 | sector 8 | total |
  |---|---:|---:|---:|---:|
  | vertex | 0 | 3 | 20 | 23 |
  | edge | 2 | 9 | 0 | 11 |
  | total | 2 | 12 | 20 | 34 |

  The rows are the model's 23 + 11, the columns are the stored 2 + 12 + 20, and the nonzero cells are 20 + 3 + 9 + 2. Every cell is conserved, because each projector commutes with D².
- **Lagrange is not an action.** FOUR_NAMES says the carrier involution does not act on the order-15 clock. By Lagrange it cannot lie in that clock, but it does act on it, by x ↦ −x.
- **More from FOUR_NAMES.**
  - In ℤ/120, any elements of orders 3 and 5 generate ⟨8⟩.
  - Residues mod 108 and mod 160 fix one point of the circle (lcm 4320), and 27 × 3 ≡ 1 (mod 40).
  - The pada subgroup ⟨40⟩ misses the tick.
  - The stage reflection k ↦ 14 − k fixes only Jīva and does not keep the bit.
  - √3 and 2√2 have no common rational return.

**Recorded, not replayed (REPORTED).** These objects of the sibling build are not stored here:
- the permutations on the fifteen indices;
- the readers on the 24-cycle and their rank law;
- the Hodge degrees 31 and 41;
- the heat spectrum 0, 3, 6, 3 ± √5;
- the opposite-edge block and the graded clock of order 10;
- the 12 × 12 sense stiffness, and the acoustic and optical matrices;
- the J7 and atlas row counts;
- MOMENT_BIT's Hankel minimum of 24, its probes and its cutoff 7.

**Not formed (UNFORMED).** The notes say these are absent, and nothing here forms them:
- Yukawa blocks, and a hypercharge from the action;
- taste, smell and touch matrices;
- an icosahedral adjacency (the root graph has degree 56);
- a swastika, hexagram, yinyang or diamond intertwiner;
- a tesseract;
- a qubit.

**The 19:57 check.** Thirteen more sibling notes (19:22–19:54) and the separate model's status and paper (19:43–19:47) were new. The Quick Access sheet (19:44) only points to continuation 3. Layer 22 gained nine checks:

- **The six-site moment chain (THEOREM).** MOMENT_CHAIN quotes three blocks: 241I − J, 183I + 52J and 35366I + 8134J. The canon's root-walk note lists the last as unidentified. They are the block Stieltjes data of the six-site port on six mutually adjacent lattice points (an A5 root simplex):
  - M₁ = 241I − J;
  - M₂ − M₁² = 183I + 52J;
  - M₃ − 2M₁M₂ + M₁³ = 35366I + 8134J.

  Their contrast and uniform eigenvalues are (241, 235), (183, 495) and (35366, 84170). This is the six-site analogue of the hexagon's K_R entry 25998. Along the way, Δⁿδ₀ has support 1, 241, 9361, 131041. So 9361 = 1 + 240 + 2160 + 6720 + 240 counts the lattice points within two root steps. That is the same integer as the AllMaps row count, not the same object.
- **The oriented operator (THEOREM).** NCG_LAG's oriented operator squared has spectrum 0⁷, 5⁸, with kernel 1 + 6. It shares the multiplicity 8 with D², but not the eigenvalue.
- **Beats (THEOREM).** The separate model reports squared beat frequencies 11 ± 4√6. They are (2√2 ± √3)², the beats of the carrier's two oscillating sectors, and the roots of x² − 22x + 25. Neither is in spec D².
- **Golden family and Agni–Soma (THEOREM).** B² = B + I, det B = −1, and B⁷ = [[21, 13], [13, 8]]. Agni and Soma are one projector, P = I − BᵀB/5 of rank 6 (§8). It kills the cut, and BᵀB = 5(I − P) is the "return scaled by 5".
- **SEVEN_ONE, corrected (THEOREM).** Of the seven mirror pairs k, 14 − k, three are split by the bit (0–14, 4–10, 5–9) and four are not (1–13, 2–12, 3–11, 6–8). The note says three are not split, and names two.
- **The order-120 clock** is not cyclic: its largest element order is 30. So the separate model's correction, that the tick is the 24th power of a generator of C120, concerns a cyclic 120, not this clock.
- **Arithmetic (ARITHMETIC).** The observer returns, the widths, the wings 21 + 77, the collar witness 1609/100, the Cabibbo seeds 27/640, 243/64000 and 3443/9600, and H60's products and determinant 3/10.
- **Recorded, not replayed (REPORTED).**
  - The separate model's 489 presentations, 30,875 validation instances and 623-file clean replay.
  - Its OM–mirror intertwiner and five-reader blind line.
  - The sibling's two curvatures of rank 4, its braid defect, the six golden petals, the Majorana block and the arXiv seed √(3/2) − 1.

**The 20:12 update.** The sibling's message and its notes BREATH_ALL, PETERSEN_GRAM and PETERSEN_PROJ (20:06–20:10) were replayed in four more checks:

- **The Petersen projectors are the carrier's (THEOREM).** The rebuilt adjacency satisfies A² + A − 2I = J. The projectors are J/10, (4I + 2A − J)/6 and (5I − 5A + J)/15. They have denominators 10, 6 and 15 and traces 1, 5 and 4, and they add to I over 30. On the K5 edges MᵀM = J + I − A, so these are the carrier's own edge projectors:
  - J/10 projects onto sector 8;
  - (4I + 2A − J)/6 = I − Mᵀ(MMᵀ)⁻¹M projects onto the five zero modes;
  - (5I − 5A + J)/15 projects onto sector 3.

  The reason is that MᵀM − 2I is the line graph of K5 and the Petersen graph is its complement, so A = J + I − MᵀM. Then A commutes with the edge stiffness: A = 3P₈ + P₀ − 2P₃, while MᵀM = 8P₈ + 3P₃. As a symmetry of the edge motion, A is a scalar on each sector, so the charge it conserves is a combination of the sector energies already in the energy table.

  The denominators are the gap products 2·5, 2·3 and 3·5 of the spectrum 3, 1, −2. Only the middle one avoids the spread 5 = 3 − (−2), which is why only 6 meets the tick. The Gram determinant 648 = 8·3⁴ is det(MMᵀ) = det(3I + J), the carrier's vertex block.
- **The Hodge 5 (THEOREM).** PETERSEN_PROJ writes the Hodge square as "A² = 5I", but the Petersen adjacency has A² = J + 2I − A. The 5 belongs to the Hodge block on the cycles (§18): (5I − BᵀB)/5 is the rank-6 cycle projector.
- **Every breath, sharpened (THEOREM).** The 32 faces of the five-simplex cancel, and the companion of 0 is nilpotent, so that mode drifts. The note concludes correctly that the breaths of 3 and 8 share no period, but its reason ("8 is not a multiple of 3") is not the criterion. Two squared frequencies share a period exactly when their ratio is the square of a rational: 8/3 is not, while 9/4 is, although 9 is not a multiple of 4.
- **Counts.** 26 more readings (352 from 43 notes) and their arithmetic hold.

**The 20:25 update.** The sibling's message and its notes PAULI_178, PAULI_CIRCLE, TICK_DEEP and CHAIN_ENERGY (20:20–20:23) were replayed in four more checks:

- **The Pauli generator is the bath (THEOREM).** PAULI_178's saved generator acts on real 16 × 16 matrices by L(M) = 240M + 16Mᵀ − 16 (tr M) I. Its eigenvalues are 0, 224 and 256, on the identity, the 120 antisymmetric Paulis and the 135 symmetric traceless Paulis (1 + 120 + 135 = 256). The sibling built no map to the model. Here is one:
  - eight antisymmetric real 4-qubit Paulis anticommute exactly along the E8 Dynkin diagram;
  - their products give a bijection φ from Λ/2Λ, the 256 half-periods of the bath, onto the Paulis up to sign, which preserves the mod-2 quadratic form;
  - L φ(x) = ε(πx) φ(x) for every half-period x, where ε is the bath band function.

  So L is the bath Laplacian on its 256 half-period modes. Its eigenvalue 0 is the origin. Its 224 is the band at the 120 E7+A1 saddles, which is the canon's 224 saddle value (§8). Its 256 is the band top at the 135 D8 points. These are the half-turn's 1 + 120 + 135 fixed momenta of §22, and a symmetric reader never sees the 120 antisymmetric directions.
- **Mass and energy (THEOREM).** CHAIN_ENERGY's "stored mass determinant" 216 is det(3W) for the source metric W = NᵀN of §10. 3W is an integer matrix and det W = 8/9 = 216/3⁵. It is the same integer as the golden step, and no mass scale is selected (TIME_BIND is unbound). The note's "the cycle adds the frequency 2" is a different 2: it is the kinetic energy ½|v₀|² of the datum's velocity, a zero-stiffness 4-cycle in ker M. The potential energy 32, half the quadratic form 64, sits in sectors 3 and 8 (12 + 20).
- **Counts.** The one tick in six counts (432·2 = 288·3 = 108·8 = 27·32 = 72·12 = 4·216 = 864), the phase weights (160 = 5·32, 492 ~ 12), and TICK_DEEP's subgroup ⟨32⟩ of order 135 inside ⟨8⟩ (index 4) hold. That is 398 readings from 47 notes in all.

**The 20:33 check.** Two items were new: the sibling's MASS_KERNEL (20:31), and the separate model's revised status and paper (20:28). Three more checks:

- **MASS_KERNEL** adopts the energy split of §23: 2 is kinetic (the 4-cycle in ker M) and 32 is potential (20 + 12). It also records the Pauli map as not replayed in its own build, so it does not yet treat L as the bath Laplacian.
- **The Pauli map, written out (THEOREM).** So that the map can be replayed without this repository's code, `data/pauli_half_periods.json` lists:
  - the four real Paulis (Y = XZ);
  - the eight Dynkin words IIIY, IIXY, IIYX, IYZI, XIXY, ZXXY, IZXY, IXXY (α₁…α₈, Bourbaki order);
  - for each of the 256 half-periods x = Σ cᵢαᵢ, its word and its band value ε(πx).

  Layer 22 checks every relation again from the file alone. `ports/ts/pauliBath.ts` replays the map in the sibling's TypeScript app (six rows, residual 0).
- **The separate model's revised status (REPORTED, with agreements).** It now has Petersen = J + I − MᵀM with the same three projectors. It also has the six-site A = 241I − J and C*C = 183P_c + 495P_u, which is §23's M₂ − M₁² in projector form. It keeps the canon's two-dimensional dark plane apart from the rank-5 kernel, and so does this text: "dark" and "zero modes" here mean ker M = P5, as in §5 and §12. Its 33,003 validation instances and 693-file clean replay are recorded, not rerun.
- **Counts.** MASS_KERNEL's 14 readings hold (412 from 48 notes).

## 24. What stays open

**Unformed operands** (`oes/gates.py`; physical or historical, not derivable):
- the six SCR6 operands;
- the original 31 seam rows and the physical 1401 → 1370 sector;
- the 502-dimensional Hodge–Dirac and the 237-dimensional observer;
- MPKG A_M;
- the 4944- and 5048-dimensional transitions;
- the R1/025/250/Jfix/Sawan/Hemkuver ports;
- the historical Agni/Soma/Suraj and the original Sākṣin;
- I6L;
- the Wald coefficient;
- the physical child H_sel;
- the missing five-dimensional operand ("cofactor 4805" does not supply it, §16).

**Recovered in this build:** the native source matrices, the 155/4805 adapter, the E8 glue map, W₉₀ exactly, W₆₀₀ modulo primes, and the W_n recurrence modulo four primes (order 16, degree 58).

**Formed in this build (SELECTED_REFERENCE, with THEOREM properties):** an action of the circle's Coxeter subgroup ⟨144⟩ on the bath through the E8 Coxeter element, whose tick is two K5 carrier rotations and whose fixed momenta are Morse points (§20). It is the largest part of the circle that can act on the bath; the atlas, moon, nakshatra and pada cannot. Its normalizer (order 240) carries the day, the golden clock and the mirror, and the tick is the commutator of the day and the Coxeter clock (§22).

**Open mathematics:**
- the convexity collar inside (223.58, 224), now reduced to a certified bound away from the 224 saddle (with margin law 15/16·d²);
- the rational coefficients of the order-16 W_n recurrence, and a proof that it holds for every n;
- a preparation protocol matching the ε^(−1/2) and ε^(−1/3) lower bounds (proved in the Canon Check);
- a matching dispersive upper bound;
- maximal branch continuation.

**Owner decisions that would move gates:**
1. sign the transaction (AUTH);
2. name the physical child (DYN_BIND, SCR6);
3. supply one clock datum (TIME_BIND);
4. trigger the freeze (PredictionFreeze);
5. allow sofacoustics.org and zenodo.org (T3081).

## Sources read (Google Drive)

- `00 — OES CANON QUICK ACCESS — CURRENT` (1KZcWbz9cPalear_Ix-cqviNdJziYAw2jOuiH75pcIug)
- `one-machine-20261028-images.pdf` (1YUMCzBlkVw00gG3SnSO1zpH2DXNxArH-), the latest edition of OMSOON736
- `LOCKED_MEMORY_END_TO_END_2026-10-28.md` (1JUsXfoA-qEiieLeYvYy0r7kXjl_6XtgC)
- `LOCKED_MEMORY_OES_CONSOLIDATED_20261028.txt` (1NKSDKdMj5bEC2Dy6r2tSPWrX_uIE8Fq-)
- `OES_736_Collar_Localization_Proof_20261028.txt` (1hqOpJkdwL6unoO7SJmnTHbJp4fzJZ2Qu)
- `OES_All_Dots_Through724_Integrated_Model_20261027.txt` (1BiKs2qxqc1DD7T8fMegjJH01S3PVOF9U): the native action, Appendix A, and D5/del Pezzo
- `One_Machine_20261028_0741.typ` (1mhK9MDOiHVM_a14ItGk3IDRp84pnevr9) and `_model.zip` (12AhKsdq-KtyTUs6N9L7y15bMm5O71RKj): the coil of order 540 and the U19.74 note
- `OES Remaining Mathematical Frontiers — Proofs and Executed Courts — 2026-10-28` (1y1vP2TPAsYP8p_bUe_D_AIi9h1h57Bnou0U-Enzy8-s): the precise open collar set
- `OES_Standing_Model_Integrated_Proof_Packet_20261027.zip` (1ukVZgOnirGVQ1CJslWLmeyKj8ZAVIiGJ, SHA-256 f579e5f9…): the literal native operands, canon W₀…W₅₅, the U7 physical-operand court and the selection reconciliation
- `LOCKED_CANON_ADDENDUM_OMNOW_SCALE_TIME_TIMEBIND…_2026-09-23` (14LStBynVoEqDogWD8YEHhAeE7q2KBgLW): the Salina and Prema courts
- `OES_OM_EK_SACH_S364_…_SCR6_OPERAND_ABSENCE_MASTER_LOCK` (13NJ0DlCTjmHfLcmIds-mRZ9SEiqaReTv): the SCR6 transaction and the four transition types
- `LOCKED MEMORY — TO OMLIKELY1` (1PFlPL4wcK57LKGvDMReG-mInbyoinHH1urIN3-XkiHw): the SCR6 shapes and the Bari PMNS pulls
- `LOCKED_MEMORY_OES_OMTOOM7_…_TIMEBIND_2026-10-19` (1zjJVDyinGUG5oRawJULNZhQm_3-_7H1o): CTB2/CTB3/CTB9
- the dEchorate T3081 court (17_BHvmFJiemYFg5gzgwSYEayZ5p_tU5-i8Qk4tX8egc)
- `one-machine-20261028.pdf`, `oes-model-20261028.zip`, `STATUS_20261028.md` (One Machine 20261028 folder, 14:16 UTC): the snapshot of §19
- `one-machine-20261028-integrated.pdf` (1GytpvBmTEertpkl8WSR7cWUW0EATjI5V), `oes-integrated-20261028.zip` (1RVahq2D-Z2-o8ntfS-1pbzL-d4hSk70w) and `INTEGRATED_20261028.md` (14GahFXr4Qu3rbzt-l6u_te5O2wE-FDAz), with the notes ALL_4320, SIDEREAL_DOTS, SEGMENT_NAMES, YUGA_LATTICE, DOTS_LATTICE, ALL_DOTS and PREMA_SALINA (15:12–15:31 UTC): the integrated spine of §20
- `00 — OES CANON QUICK ACCESS — CURRENT`, sheets 00_POST_OM736_SOURCE_DELTA_1028, 00_CURRENT_OM736_28OCT_SYNC and 00_CURRENT_OM736_AUDIT_1028 (updated 15:05 UTC), `OES_Canon_Check_and_Open_Items_20261028.txt` (1glnnehS0DdUtgMbuQvw1W2zkSvHmB6QS, the controlling 10:04 Canon Check), `OES_CANON_UPDATE_20261028.txt` (1pVIMcs2JYwMNYyzsgN1iL4d6Qy5gCKG1, 12:32) and `COURT_CORRECTION_20261028.md` (1hzX_piGG1ghRnyq_1Dh48nHpv99wX1O2): the canon position of §21
- the sibling's notes CLOSURE_234, JOIN_234, MORE_DOTS, NORMALIZE, ORBIT, UPGRADE_JOIN, CRT_JOIN, IDEMPOTENTS, PRIMARY_SPLIT and CURRENT, with `one-machine-20261028-current.pdf` (15SXt3dvbOQ9z-yu04PnGgVPU3N9S21lY, 16:18), and the separate model `finite-spectral-model-major-upgrade-20261028.pdf` (1gEEaontXS0I9HWCwBsQdJExCSVlJ_xcg, SHA-256 0869e6af…, 16:07): §21
- the sibling's notes SPINE_CORRECTIONS (1JTVWtTwwzFsqFlwRLwVwcIgc0OiWn546), COXETER_POWERS (1wLHRLvSwKiXUjH5UwAGmea8JUdCeCoSS), ATLAS_FACTOR (1yVpWxmIdWSwIuK3MKuveMH-rJZU6Vrxd) and SUN_MOON (1mXN3YvX5Cr4elHVM9d_ipfewBx6n4dat), 16:31–16:43, with `one-machine-20261028-sun.pdf` (1gRY4ja60_mGdpnhZHzIbxvxgcL0Yu4hv, 16:43), and the 16:47 consolidation `CURRENT_20261028_2046.md` (16X9fB1FEUbUpiYCSOCllctIAIWx8OZmg) with `one-machine-20261028-2046.pdf` (1WOGfKAyTKKtD8UOi4ge96L23Zw0NEXti), whose text equals the 16:43 paper: the re-read of §21
- the sibling's full edition `one-machine-20261028-full.typ` (15m9a4MohMky-q6leb23CJLstmkqrWrQy) and `.pdf` (107U4SIduxAJHPvFK7cuLjpNWU3tuf6Ph), `FULL_UPDATE_20261028.md` (1v-uVlvf5jPAJeesXz2oV9xlks7iUXNgU), `CANON_READ_20261028.md` (1rp8CpJzNOWOGfEn1GFhvvqUzXHRCb_Ql) and the forty join notes of 17:01–18:17 UTC; the Quick Access sheet 00_FULL_RECONCILIATION_20261028 (review cutoff 17:19:41): §22
- the sibling's MASS_KERNEL (18lymp6JSyMThdNcNKRhtrgqIDVyZvrX7, 20:31 UTC) and the separate model's revised `unified-spectral-machine-status-20261028.md` and paper (20:28): §23, the 20:33 check
- the sibling's notes PAULI_178 (1fy7xvmXvaOAcM5RuRWlcSHgmqkqQ3f1h), PAULI_CIRCLE (1AEn71GCDTJpEmQb9isQXI3w17ritWHVf), TICK_DEEP (11swlQAFwQw52GeYoFDtl4IMuA5qnBpaA) and CHAIN_ENERGY (1-uXJrmo2dVA-_E1UoQD5pvZGtegJpv86), 20:20–20:23 UTC: §23, the 20:25 update
- the sibling's notes BREATH_ALL (1qdaJLGC2UfMIqMzYInGIY0cwFyEdePax), PETERSEN_GRAM (1cWZmvFRiPHmHgJ-Be3saaQ74Cwz-gTRG) and PETERSEN_PROJ (14sgfv0Q-iMywvsNTXwc9nVa5OmUhy4ZL), 20:06–20:10 UTC: §23, the 20:12 update
- the sibling's 13 notes of 19:22–19:54 UTC (MOMENT_CHAIN 1ndhkNWf-Gur8t1vMZ09g1FyZvBpyxyLf through H60_JOIN 1V5tDB2L9Z286hd4ItmRhLruBmcHzPgRY), the separate model's `unified-spectral-machine-status-20261028.md` (1fIjA7_42Gebq6JknT_xx1JIE8oIYUcOj) and `unified-spectral-machine-20261028.pdf` (1oquto6h1oduN5uo30K3svSANsSpbZ2PN), and the Quick Access sheet as of 19:44: §23, the 19:57 check
- the sibling's 28 notes of 18:32–19:21 UTC in One Machine 20261028 (LEVEL_TICK 1aZUPEJ0uAUpLoCPU3KpyDs-_So_b_Umb through MOMENT_BIT 1bSfrtrrkaDpiSo12sUCyRU-zdzDvra-C), each with a paper edition, and the canon workbook `OES_CANON_REPOSITORY_FULL_RECONCILED_20261028.xlsx` (1qU4VKdQjPTbK_pgWhY_oVRnqcOQgg7o4), sheet 00_CURRENT_20261028_1910 (continuation 3, review cutoff 19:10:16): §23
- read only, for the source of the reported moments: `LOCKED MEMORY — TO OMSOON4 — Full OES K5–E8–Stieltjes–Quantum Observer–F20–Deep36 Source-Graded Handover` (1x_6HVLg17zVtv789vRLlFYpVnNDTT08e29MNo7dZeOM), `… E8 ROOT WALK REPLAYED …` (1XmuGnPDySyQKNrETDYZJxoWpElPGI3LYBgVUAOfti4w) and `… TO OMSOON7 — Claude V168R …` (1CPAaYlykOvFvu0FcjIquUzDUI4VfptziZOFnXuG1CHI): §23
- Sibling handovers in OES › Locked Memory, OMSOON → OMSOON7, 22–25 Oct; titles and summaries only

The only claude.ai Code session visible from this environment is this one. Sibling *chats* are present only through the handover documents they saved to Drive.
