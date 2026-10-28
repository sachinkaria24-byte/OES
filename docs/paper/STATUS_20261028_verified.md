# One Machine, verified build: 28 October 2026

Selected mathematical build, replayed from matrices. Not a source admission. Not a change to the canon matrices.

AUTH = NOT_PASS. ScientificGold = FALSE. TIME_BIND = UNBOUND. The six SCR6 operands stay absent. No gate moves.

**Model:** GitHub `sachinkaria24-byte/OES`, branch `claude/lagrangian-spectral-spacetime-model-t2253b`.

- `python verify.py` runs 18 layers and 320 checks. Of these, 300 hold: THEOREM 214, ARITHMETIC 26, OBSTRUCTION 22, CONDITIONAL 15, UNFORMED 15, SELECTED_REFERENCE 6, REMOVED 2. The other 20 are REPORTED records.
- `pytest` runs 22 tests.

**Paper:** `one-machine-20261028-verified.md`, plus the PDF in `docs/paper/` of the repository.

New over the 14:16 snapshot, each computed from matrices:
- **The W_n recurrence**, formed mod four primes. It has order 16 and degree 58, and its characteristic polynomial factors exactly over ℚ. The first kernel is at (r+1)(d+2) = 456.
- **The 11 critical families** of the bath (243,600 points, Morse sum 0) are exactly the 11 in-band characteristic roots.
- **Density on T⁹.** The nine bath frequencies have distinct square-free parts 14, 3, 62, 10, 251, 161, 51, 7, 1, so they are ℚ-independent (Besicovitch). The snapshot left this open.
- **All eleven Hessians** are recomputed, and every printed coherent coefficient is reproduced. The snapshot left this open.
- **Walk asymptotics.** W_n = (16/π⁴)·240ⁿ·n⁻⁴·(1 − 2/n + (23/15)/n² + O(n⁻³)), from the 7-design alone. The exact W₅₀…W₉₀ follow it.
- **Sound, light, frequency and phase on the K5 edges:**
  - the Hodge Laplacian is 5I, so sound and light share the frequency √5;
  - the canon's Hodge block A is −curl;
  - the light helicities are the icosahedral 3 and 3′;
  - Agni = 5I − G is Curl²;
  - sound converts to light only through the C5 clock.
- **The literal 5-dim operand.** T₆ preserves V_c, and T₆|V_c has det 31, so 155 = 5 × 31.

Corrections:
- **Spanda.** (I + S)/2 is a Markov projector of rank 19 (7 fixed subsets plus 12 symmetrized pairs), not 7.
- **Recurrence order.** "The recurrence order is 11" should read: order 16, with an in-band characteristic part of degree 11.
- **Locked Memory handover:**
  - the digest b5590733… matches none of the three One Machine PDFs;
  - 15/13 should be 15/16;
  - ker O ⊆ ker C is reversed;
  - H90 is unsupported;
  - T5×5 is a construction;
  - an order-11, degree-5 exact recurrence is excluded.

Not formed: GKSL, SI, BRST, BV, Einstein–Hilbert, BassForge, Sawan's intertwiner, the six SCR6 operands, the rational coefficients of the order-16 operator, and the collar.
