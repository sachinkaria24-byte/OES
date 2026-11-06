# The binding solution: TIME_BIND and DYN_BIND as closed-form maps

*6 Nov 2026. Layer 23 checks `bind_time_map`, `bind_time_units`, `bind_dynamics_dyadic` and `bind_selections`; the joins are in [`DOTS.md`](DOTS.md) and the rows in [`LEDGER.md`](LEDGER.md).*

The two gates stay as they are: **TIME_BIND = UNBOUND**, **DYN_BIND = NOT_INSTALLED**. No physical datum exists in the model, and no mathematics supplies one (layer 13's countermodel A: τ and 2τ give identical native records; the join "no internal clock"). What the model can do, and now does, is reduce each gate to its minimal physical input and give the exact map from that input to the bound model, together with dimensionless invariants that any realisation must satisfy before a single second is assigned. The maps are theorems; the inputs are not.

Throughout, ρ is the time conversion t − t₀ = ρu from the model's time u to physical time (the separate model's ρ_t). It is not a source intensity, and the spectral variable z below is a positive squared-rate parameter, not a source vector.

## 1. Time

**The scale.** A physical realisation has the generator (κ/τ²)K in physical time t, where τ is the time unit and κ the kinetic normalisation. Every observable depends on (τ, κ) only through ρ = τ/√κ: the response C(t) = Yᵀcos(t√(κK)/τ)Y is invariant under (τ, κ) → (cτ, c²κ), equals its own value at (ρ, 1), and is annihilated by τ∂_τ + 2κ∂_κ (`video_ten_fisher`, `chiral_time`; checked symbolically in `bind_time_map`). So TIME_BIND is exactly one real number, ρ, and the SI second enters nowhere else.

**The convention.** With the whole generator scaled, R(s) = ρ²G(ρ²s²) for G(z) = (z + A − Σ(z))⁻¹, the measured excess secant E(s) = [R(2s)⁻¹ − R(s)⁻¹]/(3s²) − I equals e(ρ²s²) exactly, with e(z) = [Σ(z) − Σ(4z)]/(3z). In the other convention (the hidden block alone in physical units, B/ρ, C/ρ²) it is ρ²e(ρ²s²). Both are checked in `bind_dynamics_dyadic`; a crossover binds ρ only once the convention is declared. The tables below use the first.

**Three certified routes to the same ρ.**

| route | observable | map | certificate |
|---|---|---|---|
| protected mass clock | the first half-return T_half of r(t) = c_m((t − t₀)/ρ) | ρ = T_half / u_half | u_half ∈ (892853037828096677, 892854727289957321)/11529215046068469760, relative width 1.9 × 10⁻⁶; (0.0774426666, 0.0774426679) with the P10 bracket (`refclock_halfreturn`, `refclock_calibration`) |
| fourth jet | Ξ = C⁗(0) − C″(0)² on the 45 channels | Ξ = D45/ρ⁴, tr Ξ = 21061/ρ⁴; on the 19-source, tr Ξ₁₉ = 10791/ρ⁴ | D45 = 2117 ⊕ 967⁸ ⊕ 389²⁶ ⊕ 127⁶ ⊕ 83⁴, D19 = 967⁸ ⊕ 389⁷ ⊕ 83⁴ (`master_readout`, `deep_observer_algebra`, `refclock_gain`) |
| excess-secant crossover | the rate s* at which E(s) = 1/200 on the quadratic source | ρ = √z* / s* | z* ∈ (12200402860332943, 12200405718556069)/2⁴⁸, 6.583656896344280 < √z* < 6.583657667530262 (the separate model's 2 Nov certificate, read as data; it needs m₀..m₁₇) |

**The ρ-free invariants.** Four readings of one ρ (T_half, Ξ_mass, Ξ_q, s*) leave three independent dimensionless numbers. One is exact and needs no bracket: Ξ_mass/Ξ_q = 2117/389 (and tr Ξ₁₉/Ξ_q = 10791/389, tr Ξ/Ξ_q = 21061/389). The other two carry certified brackets, and the quadratic-only combination I₂ follows from them (I₂ = (389/2117) I₁/I₃⁴ identically):

| invariant | value | certified bracket |
|---|---|---|
| I₁ = Ξ_mass · T_half⁴ | 2117 · u_half⁴ | (0.07614507, 0.07614566); (0.07614511, 0.07614513) with the P10 bracket |
| I₃ = T_half · s* | u_half · √z* | (0.50985587, 0.50985691); (0.50985594, 0.50985602) with P10 |
| I₂ = Ξ_q / s*⁴ (derived) | 389 / z*² | (0.20705257, 0.20705268); exactly 389/z_hi² and 389/z_lo² |

Here 2117 = m₂ − m₁² of the mass clock (moments 1, 184, 35973, …) and 389 = m₂ − m₁² of the quadratic source (1, 232, 54213, 12740592, …), the two hidden variances of `master_readout`'s sectors. A realisation that fails any of these is not a realisation of this model, whatever its clock says. A realisation that passes them, and reports T_half in seconds, binds ρ.

The separate model's three-route note (6 Nov 08:44) adds a dressed source clock with half-return u_s ∈ (0.3699205238490600, 0.3699253084202434), its own certificate read as data. From the stated endpoints its brackets T_s/T_m ∈ (4.77669338477, 4.77676420538), s*·T_m ∈ (0.509855877996, 0.509856902472) and s*·T_s ∈ (2.435429807938, 2.435461593195) are outward roundings of the exact products, its 19-source bands at z* sum to its trace bracket (0.156177870151860420, 0.156177924862627664) to the last digit, and its receipt's exact I₂ fractions equal the model's. Nothing in it moves the gates.

**A fourth route, not a second number.** For the gauge-covariant generator (κ/τ²)(K + δ_model eeᵀ) a load's inverse-response shift is (δ_model/ρ²)eeᵀ at every rate, so a measured shift d (in s⁻²) reads ρ² = δ_model/d and never τ and κ apart (`bind_time_units`); in the κ = 1 gauge of the T1–T5 audit this is τ² = δ_model/d, τ = ρ. With Ξ_q = 389/ρ⁴ the ratio d²/Ξ_q = δ_model²/389 is a fourth ρ-free relation, 64/389 at the note's static gap 8, a test and not a definition of ρ (the model's own dressed gap at α = 1 is (5 − √5)/2, `deep_zero_pole`'s floor, not 8). A stiffness step in N/m divided by d is a mass, not a time (the 6 Nov T1–T5 audit's repair). τ and κ separately are a gauge choice and stay unidentified.

## 2. Dynamics

**The content.** The dynamics is the declared native action (layer 4, the `source` dot: q″ + 4q = 0 on ker M + ker M) and its reference completion K_θ = H + θ(ε + JVJᵀ) = (1 − θ)H + θK₁₉. Everything beyond E8 is one of the named selections, each fixed or recorded by a named check (`bind_selections`):

| selection | where it is fixed or recorded |
|---|---|
| θ | `flower_homotopy` (the convex family at the note's five θ) |
| ε, α, J | `schur_zero_mode` (ε = 1, α = 1 on the root-site instance; J19 into the 45-channel section) |
| the mark | `mgm_marks` (the twelve Golden marks, their zero lines and their average) |
| W_p, the adapter | `literal_port`, `parent_readers` (the owner's W_p in boundary order; the reconstructed port up to a commutant element) |
| ι | `canon_flower_pullback` (the cycles' inclusion into the edge block of ℝ¹⁹) |
| the parity | `zero_pole_parity` (the D10 parity of the zero-mode line) |
| the readout | `master_readout` (the 45 channels and D45) |

DYN_BIND is "installed" when one member of that family is physically signed; mathematics cannot sign it.

**The recovery certificate.** For Σ(z) = B(z + C)⁻¹Bᵀ with C ≥ 0 and e(z) = [Σ(z) − Σ(4z)]/(3z),

  Σ(z) − 3z Σ_{j<N} 4ʲ e(4ʲz) = Σ(4ᴺz),  0 ≤ Σ(4ᴺz) ≤ BBᵀ/(4ᴺz)

exactly, in Loewner order (the 6 Nov P01 theorem; `bind_dynamics_dyadic` checks it symbolically and on `master_response`'s root-site instance, the tail bound by exact inertia). The static block A cancels. For the 19-source the tail constant is D19 = 967P₈ + 389P₇ + 83P₄, norm 967 (`refclock_gain`); the three-route doc's odd-ten port value 127P₆ + 392P₄ is its own reader (392 is no model number) and does not substitute for it.

**The scale-free form.** With E(s) = e(ρ²s²) and x = s/s*, the dyadic sum reads the memory in model units from rate ratios alone, ρ cancelling: 3z*x² Σ_{n<N} 4ⁿE(2ⁿs*x) = Σ(z*x²) − Σ(4ᴺz*x²). So the shape of the hidden memory is testable before a second is assigned; the absolute Σ_phys(s) = ρ⁻²Σ(ρ²s²) still needs ρ. Time is bound first and dynamics second.

**One anchor.** One full normalised G(z₀) then fixes A = G(z₀)⁻¹ − z₀I + Σ(z₀) and G(z)⁻¹ = G(z₀)⁻¹ + (z − z₀)I + Σ(z₀) − Σ(z) for every z: the compressed Green function on the visible block, never the hidden realisation (the model's comparator non-uniqueness is `notes_1418`'s). The exact load identity G_L⁻¹ − G₀⁻¹ = L on the visible block is the falsifier of any finite emulator.

**The noise floor.** With errors ≤ ε_j on the j-th dyadic sample, ‖Σ(z) − Σ_N^meas(z)‖ ≤ 3z Σ_{j<N} 4ʲε_j + ‖D‖/(4ᴺz): the tail falls and the error grows with N, so a finite N is chosen from a declared budget (recorded from the notes; the blind t → 0 limit's obstruction is `tdc_leakage`'s).

## 3. What the Drive adds, and what it does not

Read as data, nothing run: TIME_BIND_RESOLUTION (2 Nov), the TIME DYN P01–P20 audit (6 Nov 08:06), the five gate-pinching theorems T1–T5 (08:03), the G1–G6 corrective audit (08:32), the 08:28 model receipt (SHA-256 ce49eddea0246212d1b6a558e76ef590716a6970ce25f4fcced5264eb4d41693), and the three-route note with its txt and exact receipt (08:44; OES_CLOCK_RHO_DYADIC_THREE_ROUTE_20261106, 65 checks all_pass by its receipt, its verifier not run). All of them keep the gates shut and agree with the maps above. None contains a measured interval.

## 4. What would move the gates

Each is an external input; none is a computation:

1. one measured T_half, Ξ or s* in SI units, on a preparation that passes the ρ-free invariants, binds ρ (TIME_BIND);
2. one measured shift d of a declared load is a fourth route to ρ, and against the jet a fourth ρ-free check;
3. a full normalised secant curve at dyadic rates with one anchor G(z₀) recovers Σ and A on the visible block, and a physically signed member of the completion family installs the dynamics (DYN_BIND).
