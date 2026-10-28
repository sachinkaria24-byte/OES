# Addendum to "LOCKED MEMORY — OES End-to-End & Spectral Model Handover — 28 Oct 2026"

**Class:** additive corrections, non-promoting. The locked handover itself is unchanged. Every item below is replayed by `oes/handover.py` (layer 16 of `python verify.py`) unless it is marked REPORTED.

**Gate banner:** unchanged, and identical to the standing ledger. AUTH = NOT_PASS · ScientificGold = FALSE · TIME_BIND = UNBOUND · no gate moves.

## 1. Confirmed as written

- **Stage equation q̈ + 4q = 0.** The quadratic port has zero Jacobian at q = 0, so ω₀ = 2.
- **Carrier spectrum.** spec D² = {0⁵, 3⁸, 8²}, Tr = 40, Tr² = 200, and the kernel is P5.
- **Clique weights.** P_u = J/6 has entries 1/6, and P_c has diagonal 5/6.
- **One exterior algebra.** dim Λ•(ℝ⁵) = 2⁵ = 32 = 16 + 16 < 48, so a single carrier holds one generation (as in layer 12).
- **9/40 tower identity.** It holds. 40/9 is the literal sharp quartic constant (layer 10).
- **Coil.** All four expressions for 540 are arithmetically correct.
- **7-design expansion.** ε(k) = 30|k|² − (3/2)|k|⁴ + (1/24)|k|⁶ + O(|k|⁸), exact.
- **11 critical families, 243,600 critical points, Morse alternating sum 0.** Replayed on the vertices and edges of the E8 alcove:

  | type | λ = 240 − ε | ε | points | Morse index of ε |
  |---|---|---|---|---|
  | E8 | 240 | 0 | 1 | 0 |
  | E7+A1 | 16 | 224 | 120 | 1 |
  | E6+A2 | −3 | 243 | 2,240 | 2 |
  | D5+A3 | −8 | 248 | 15,120 | 3 |
  | A4+A4 | −10 | 250 | 48,384 | 4 |
  | A5+A2+A1 | −11 | 251 | 80,640 | 5 |
  | A6+A1 (edge) | −185/16 | 251.5625 | 69,120 | 6 |
  | A7 (edge) | −320/27 | 251.85… | 17,280 | 7 |
  | A7+A1 | −12 | 252 | 8,640 | 7 |
  | A8 | −12 | 252 | 1,920 | 8 |
  | D8 | −16 | 256 | 135 | 8 |

  These 11 values are exactly the in-band characteristic roots of the W_n recurrence (§3 below), which was found independently from W_n alone. The double root at ε = 252 comes from A8 and A7⊕A1, as the handover says.
- **Dispersive identities.** Both root-line identities hold for Φ_v(s) = ε(√2 s v) = 114 − 112 cos(√2 s) − 2 cos(2√2 s), with θ = √2 s in the second.
- **Schur boundary.** A_bb = 235P_u + 241P_c and BB* = 183P_c + 495P_u.
- **156-coordinate realization through M₅₀.** It exists: every sector's Hankel form is positive definite through M₅₀ (exact).
- **[9,3,7]₁₁ MDS facts.** All 84 minors are nonzero mod 11, and 3 errors are corrected.
- **W₀…W₈₄ exact with W₆ = 17,141,798,400.** This is contained in the repository's exact W₀…W₉₀.
- **Stoplines.** The SCR6 operands, physical selection, SI clock, area map and Wald coefficient stay external.

## 2. Corrections (replacement text)

**§1, carrier.** "15-edge K6 carrier" → "15-atom K5 carrier (5 vertices + 10 edges)". The spectrum (0⁵, 3⁸, 8²) belongs to D² = MMᵀ ⊕ MᵀM on K5. The signless operator on the edges of K6 has spectrum (0⁹, 4⁵, 10¹).

**§2, the 5×5 operand.** Replace "Literal 5×5 Integer Operand" with:
- *Constructed* T5×5 = (2I₄ − C_A4) ⊕ [5], where C_A4 is the vertex 5-cycle written in the A4 root basis. It is integral, with det 155 and trace 14, and is conjugate to 2I₅ − R₅ + (4/5)J₅ by S₅ (det 5). Status SELECTED_REFERENCE: it is not in the literal operand file (no 5×5 matrix there has det 155), and it is not a block of the printed chart T₆, whose characteristic polynomial is different.
- The literal operand on the five-dimensional contrast lattice is **T₆|V_c**, and it is a candidate for the missing five-dimensional operand (owner to confirm). Every column sum of T₆ is 5, so T₆ preserves V_c = {x ∈ ℤ⁶ : Σx = 0}. In the root basis eᵢ − eᵢ₊₁ it is

  T₆|V_c = [[1,−1,1,0,−1], [1,−1,3,−2,−2], [1,−2,4,−3,0], [1,0,3,−1,0], [2,0,1,−1,0]],

  with det 31 and irreducible characteristic polynomial x⁵ − 3x⁴ + 12x³ − 20x² + 31x − 31.
- So det T₆ = 155 = 5 × 31: 5 on the uniform quotient, 31 on the contrast lattice. 4805 = 5·31² = cofactor₄₄(TTᵀ), the sum of the squared row-4 cofactors of T₆. The largest |cofactor| of T₆ is 68.

**§2, 9/40.** Add: "dim V9 / Tr K15 = 9/40 is a numerical coincidence. 9/40 stays on the canon's REMOVED list as a physical constant."

**§2, coil.** Add: "ARITHMETIC. The four expressions are coincidences. The theorem is the coil: order 540 and index 8 in ℤ/4320 (layer 8)."

**§3, walk annihilators.** Replace "Order-11, Degree-5 continuum operator … and N = 25 … P25(E_n) expanded in full" with:
- W₀…W₉₀ are exact, from two independent engines, and W₀…W₆₀₀ are known modulo primes.
- Every recurrence with (r+1)(d+2) ≤ 455 is excluded. An order-11 recurrence needs degree ≥ 49, and shape (11, 5) is excluded outright by the exact W₀…W₉₀.
- The exact annihilator found, the same mod four primes, has **order 16 and degree 58**. Built from W₀…W₅₀₀, it predicts W₅₀₁…W₆₀₀. This is a THEOREM on the data. The rational coefficients are UNFORMED, and there is no proof yet that it holds for every n.
- Its characteristic polynomial is

  (z−240)(z−16)(z+3)(z+8)(z+10)(z+11)(z+185/16)(z+320/27)(z+12)²(z+16) · (z−340)(z+660)(z+20)(z+35)(z+120/7).

  The local exponent is −4 at every simple root, and (α+4)(α+5) at −12.
- The first ten factors (11 roots) are the 11 critical families of §1 above. An "order-11 continuum operator" can only be this in-band (asymptotic) part.
- P25 is the 25-node Gauss–Jacobi polynomial. It annihilates the quadrature sequence, which equals the moments only through M₄₉. It does not annihilate the moments themselves (their 26×26 Hankel matrices are positive definite), and it does not annihilate W_n.

**§3, collar.** "(15/13) r²" → "(15/16) r²". Only 15/16 gives the stated 3/80 at r = 1/5 (15/13 gives 3/65), and 15/16 is the saddle law of layer 8. "Mediant monotonicity certifies strict positivity … up to E = 224" → "REPORTED along Curves I and II". The 8-dim collar stays open. The 0.0298 agrees with the repository's survey floor of 0.030.

**§3, dispersive bound.** The identities stand (see above). sup|K(t, x−y)| ≤ min(1, 3.65 t^(−9/4)) is REPORTED: the two 1D identities do not by themselves bound the 8-dim kernel, and the 0741 paper lists the dispersive constants as open.

**§4, 064 → 490.**
- "Stieltjes–Krein envelopes … and Möbius–Pick multi-frequency criterion verified" → "The envelopes and the multi-frequency incompatibility are true, rebuilt from the true M₀…M₄₉ (layer 15). The court script's walk counts are wrong from W₄ on, its moment sequences are not positive definite, and its multi-frequency certificate gives the wrong sign on the true moments. The incompatibility holds by Markov–Krein uniqueness."
- "H90 identified as a [9,3,7]_q MDS code" → "UNFORMED. The MDS facts hold, but nothing selects this code as H90."
- "exact separation theorem ker O ⊆ ker C" → "ker O ⊄ ker C". ker O is the 4-dim cross block. Only the completed map (with the 4 polarization rows) has zero kernel.
- "B_geom = diag(−2, 2)" → REPORTED: the sites and basis are not given. On a C5-invariant pair, a nonzero B lies in the C5-trivial part, where it has 4 parameters, not 2.

## 3. Still REPORTED (not replayable here)

- The primary paper digest b5590733…. It is not the SHA-256 of `One_Machine_20261028_0741.typ` (64dfe66e…), of the 0741 model zip (a834dd88…), or of any file inside them. The PDF is not in the repository.
- Tr₁ = 24 and Tr₂ = 84: the operands are not defined.
- The bivariate J.C.P. Miller recurrence: not given. The walk counts it produced agree with the repository.
- The transverse Floquet monodromy and the Legendre–Rodrigues preparation constant: no operands are given.
- The preparation-time bounds ε^(−1/2) and ε^(−1/3) (U19.81 remarks).

## 4. Missing from the handover

- The U19.81 audit (layer 15): five obstructions in the court and its script.
- The W_n recurrence of order 16 above, with its exact characteristic polynomial.
- Custody: repository sachinkaria24-byte/OES, branch `claude/lagrangian-spectral-spacetime-model-t2253b`. `python verify.py` replays every layer.
