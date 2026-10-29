"""Layer 25. One object: the whole model from E8 and a Coxeter element.

E8 is the only even unimodular lattice of rank 8 (cited), and its Coxeter elements are all conjugate (cited; layer 19
exhibits the conjugator of c to c'). So the pair (E8, c') has no parameters. This layer shows that it builds every
structural dot of the diagram, and that the remaining dots are the canon's own inputs, each meeting the derived part
at a named interface.

The seed. E8 with c' is the cyclotomic line Z[zeta30] with the trace form Tr(alpha x ybar) (oes/cyclotomic.py (a)).

The derivation (DERIVATION) builds 49 dots from the seed, each by one THEOREM join of layer 23 whose check holds:
  - the trunk: E8 -> the cyclotomic line -> the clocks (the Galois group) -> the tick's residue plane F25 -> one
    residue line, the carrier's A4 + A4' -> either factor, A4 -> K5 (its positive roots) -> the vertices, the zero
    modes, the cycles and the source;
  - the residue plane's other branches: PGL(2,5) on the six lines (and from it the synthemes), the surface's six axes
    and PG(2,5);
  - the other primes (layer 26): the regular clocks from the clocks, and the sun's decad F81 = F9^2 from the
    cyclotomic line, from which the 360 parent is the sun's A6 on its ten 4A2 frames;
  - the arithmetic: the golden companion is the tick's Gauss sum;
  - the lattice's harmonic analysis: the bath, the walks, the moments and measures, the half-periods with the Pauli
    algebra and GKSL, the Hodge 70, the momenta, the census and its torus, the root graph and its frame;
  - the carrier: the shadows of the mixed roots, then the triple, the readout, the binding, sound and light, the
    simplex, the cube, the ports and the six-site cone.
Each choice on the trunk is unique up to the symmetry already built. The six lines are one orbit of the tick's
normalizer, the line's stabilizer exchanges its two factors, and the circle's selection 144 -> c' is one of eight
choices that the Galois clocks permute.

The inputs (INPUTS) are ten: the circle Z/4320 with its stages and memory clock, the datum, the literal operands, the
words, the integers of the 801 matrix, the Standard-Model split of the five sites, the time unit and the product
geometry. Ten more dots are built from them (FROM_INPUTS). Two of the inputs meet the seed exactly: mod 5 the 801
matrix is minus the day, and the circle's order-30 subgroup is <c'>.
"""

from . import cyclotomic, dots, gates
from .record import Report

T, SR, OB, CN = gates.THEOREM, gates.SELECTED_REFERENCE, gates.OBSTRUCTION, gates.CONDITIONAL
SEED = "E8"

# dot: (the dot it is built from, the check of the layer 23 join that builds it)
DERIVATION = {
    "cyclo": ("E8", "cyclotomic_line"), "clocks": ("cyclo", "galois_clocks"), "G120": ("clocks", "clock_joins"),
    "AGL": ("G120", "clock_joins"), "residue": ("clocks", "residue_plane"), "pgl": ("residue", "tick_normalizer"),
    "L0": ("residue", "residue_plane"), "A4": ("L0", "tick_normalizer"), "E": ("A4", "k5_roots"),
    "V": ("E", "exterior"), "D5": ("A4", "k5_roots"), "S5": ("A4", "s5_weyl"), "kerM": ("E", "k5_roots"),
    "cycles": ("E", "exterior"), "rotor": ("cycles", "exterior"), "petersen": ("E", "petersen_roots"),
    "carrier": ("L0", "carrier_shadows"), "sixsite": ("V", "cone"), "source": ("kerM", "source_port"),
    "triple": ("carrier", "triple"), "readout": ("triple", "readout"), "binding": ("triple", "binding_joins"),
    "waves": ("E", "sound_light"), "simplex": ("E", "simplex_grades"), "cube": ("E", "cube_cuts"),
    "triangle": ("cycles", "triangle_port"), "golden": ("cyclo", "golden_gauss"), "bath": ("E8", "triangle_port"),
    "walks": ("bath", "walks_join"), "moments": ("walks", "walks_join"), "measure": ("moments", "measure"),
    "halfper": ("cyclo", "primes.half_turn"), "pauli": ("halfper", "counts.pauli_quotient"),
    "gksl": ("pauli", "counts.pauli_quotient"), "hodge": ("E8", "hodge70"), "momenta": ("residue", "places.band_at_places"),
    "census": ("E8", "census"), "torus": ("census", "nine_torus"), "rootgraph": ("E8", "root_scheme"),
    "frame": ("E8", "eight_roots"), "surface": ("residue", "tick_normalizer"), "pg25": ("surface", "projective_plane"),
    "synthemes": ("pgl", "syntheme_bridge"), "parent": ("sun", "primes.decad"),
    "regular": ("clocks", "primes.regular_clocks"), "sun": ("cyclo", "primes.prime_clocks"),
    "goldenport": ("cycles", "golden_root_port"), "wedgeport": ("cycles", "wedge_port"), "darkport": ("L0", "dark_port"),
}

# input: (what the canon supplies, the derived dot it meets, the check of that interface join)
INPUTS = {
    "circle": ("the canon's circle Z/4320; its step 144 goes to c', one of eight choices, all conjugate under the "
               "Galois clocks", "clocks", "clock_joins"),
    "stages": ("the canon's fifteen stage indices on the circle", "circle", "counts.check_claims"),
    "memory": ("the 120-state memory clock, stepped by the circle (a selection)", "circle", "memory_clock"),
    "datum": ("the canon's datum (psi0, v0), a vector on the zero modes of energy 34", "kerM", "counts.tick_tock"),
    "literal": ("the owner's native source matrices", "source", "literal_port"),
    "words": ("the canon's words 088, 086 and 980", "A4", "words_c5"),
    "air801": ("the integers of AIR_801; mod 5 it is minus the day on the residue plane", "residue", "clock_residues"),
    "charges": ("the Standard-Model split of the five sites, colour 0, 1, 2 and weak 3, 4", "V", "charges"),
    "calibration": ("the time unit tau of t = tau u (TIME_BIND unbound)", "readout", "calibration"),
    "gravity": ("the product geometry M4 x F with M4, f, L and m free (conditional)", "triple", "product_geometry"),
}

# input: why it stays an input
WHY = {
    "circle": "psi(4320) = 38 > 8, so no lattice clock runs Z/4320; its part <144> is the Coxeter clock (layer 27)",
    "stages": "the canon's fifteen indices on the circle",
    "memory": "order 90 and psi(90) = 10 > 8, so no lattice clock of the seed runs it (layer 27)",
    "datum": "a vector the canon chooses on the zero modes; its S5-orbit is regular (layer 23)",
    "literal": "the owner's matrices; they match the derived source up to an explicit isometry (layer 10)",
    "words": "the canon's words; isometric to the oriented duads of K6 only over Q(sqrt2) (layer 23)",
    "air801": "determinant 12402, so no lattice clock; only its residue mod 5 is the seed's (layer 27)",
    "charges": "the 3 + 2 split chooses the Standard-Model gauge group; once chosen it is unique up to W(E8) (layer 24)",
    "calibration": "no internal number binds physical time (an obstruction, layer 23)",
    "gravity": "M4, f, L and m are free parameters; conditional (layer 6)",
}

# dot built from an input: (the dot it is built from, the check of the join that builds it)
FROM_INPUTS = {
    "time": ("circle", "primary_split"), "observer": ("circle", "primary_split"), "c27": ("circle", "primary_split"),
    "atlas": ("circle", "atlas"), "coil": ("circle", "coil"), "grain": ("coil", "grain"), "vortex": ("atlas", "vortex"),
    "miss": ("circle", "tick_miss"), "assignment": ("charges", "assignment.standard_model"),
    "cosmology": ("gravity", "friedmann"),
}


def _join(a, b, check):
    """The layer 23 join between a and b (either way) with this check, or None."""
    return next((j for j in dots.JOINS if {j[0], j[1]} == {a, b} and j[5] == check), None)


def _root(dot, parents):
    seen = [dot]
    while seen[-1] in parents:
        seen.append(parents[seen[-1]][0])
        if len(seen) > len(dots.DOTS):
            return None, seen
    return seen[-1], seen


def derivation():
    """The partition of the dots and the derivation tree, with every edge a held join."""
    results = dots.check_results()
    held = {k: all(bool(v) for v in res.values()) for k, res in results.items()}
    names = [set(DERIVATION), set(INPUTS), set(FROM_INPUTS), {SEED}]
    edges = {d: _join(d, p, ck) for d, (p, ck) in DERIVATION.items()}
    built = {d: _join(d, p, ck) for d, (p, ck) in FROM_INPUTS.items()}
    faces = {d: _join(d, m, ck) for d, (_, m, ck) in INPUTS.items()}
    roots = {d: _root(d, DERIVATION) for d in DERIVATION}
    roots_in = {d: _root(d, FROM_INPUTS) for d in FROM_INPUTS}
    depth = {d: len(path) - 1 for d, (_, path) in roots.items()}
    return {
        f"the {len(dots.DOTS)} dots split into the seed, {len(DERIVATION)} derived dots, {len(INPUTS)} canon inputs and "
        f"{len(FROM_INPUTS)} dots built from the inputs, with no dot left over or counted twice":
            set.union(*names) == set(dots.DOTS) and sum(len(n) for n in names) == len(dots.DOTS)
            and (len(DERIVATION), len(INPUTS), len(FROM_INPUTS)) == (49, 10, 10),
        "every derived dot is built by a THEOREM join of layer 23 whose check holds, and its parents lead back to E8 "
        "without a cycle":
            all(j is not None and j[4] == T and held[j[5]] for j in edges.values())
            and all(r == SEED for r, _ in roots.values()),
        "every dot built from an input comes by a held join that is not an obstruction, and leads back to an input":
            all(j is not None and j[4] in (T, CN) and held[j[5]] for j in built.values())
            and all(r in INPUTS for r, _ in roots_in.values()),
        "every input meets the derived part or another input at a held interface join, and two meet the seed exactly: "
        "the circle's selection 144 -> c' and the 801 matrix mod 5":
            all(j is not None and j[4] != OB and held[j[5]] for j in faces.values())
            and faces["circle"][4] == SR and faces["air801"][4] == T,
        f"the trunk E8 -> cyclotomic line -> clocks -> residue plane -> A4 + A4' -> A4 -> K5 edges -> zero modes -> "
        f"source has depth {depth['source']}, and no dot is deeper than {max(depth.values())}":
            roots["source"][1] == ["source", "kerM", "E", "A4", "L0", "residue", "clocks", "cyclo", "E8"]
            and max(depth.values()) == 8,
    }


def uniqueness():
    """Each choice on the trunk is unique up to the symmetry built before it."""
    lines = cyclotomic.tick_normalizer()
    galois = cyclotomic.galois_clocks()
    from . import spine
    c, cp, r, rp, g, w = spine.spine_clock()
    return {
        "the seed has no parameters: E8 is the only even unimodular lattice of rank 8 (cited), and the Coxeter element "
        "c' is a conjugate w c w^-1 of c = s1 ... s8 (layer 19's w)":
            w is not None and spine.is_weyl(w) and not (w @ c @ spine.inverse(w) - cp).any(),
        "the carrier line is any of the six residue lines (they are one orbit of N_W(<g>)), and the carrier's A4 is "
        "either factor of it (the line's stabilizer exchanges them)":
            all(lines.values()),
        "the circle's selection 144 -> c'^k is one of eight, and the normalizer of <c'> realizes every unit k, so all "
        "eight are conjugate":
            all(galois.values()),
    }


def unified_page():
    """docs/UNIFIED.md: the derivation as one page."""
    D = dots.DOTS
    name = lambda d: D[d][0]
    lines = ["# One object", "",
             "Layers 25 to 27 (`oes/unify.py`, `oes/cyclotomic.py`, `oes/primes.py`, `oes/places.py`). Generated by "
             "`unified_page()`; "
             "`tests/test_model.py` checks that this file is current.", "",
             "E8 with a Coxeter element c′ has no parameters. It is E8 = Z[ζ₃₀] with the trace form "
             "Tr(α x ȳ), α = (2 + 2η + η²)/15, η = ζ + ζ⁻¹. Every structural dot of the diagram is built from it by "
             "THEOREM joins, and the rest are the canon's inputs, each meeting the derived part at a named interface.", "",
             "## What the seed gives", "",
             "- **The clocks are Galois.** The normalizer of ⟨c′⟩ is μ₃₀ ⋊ Gal(Q(ζ₃₀)/Q), 240 elements. The day is σ₇, "
             "the golden clock σ₁₁ and the mirror σ₂₉.",
             "- **The tick's residue plane is F₂₅.** The tick g = c′⁶ fixes 25 momenta, E8/(1 − g)E8 = F₂₅, and c′ acts "
             "there as a primitive sixth root of unity. The 240 roots lie ten over each of its 24 nonzero points.",
             "- **Six A4 + A4.** The six F₅-lines pull back to six A4 + A4 sublattices that partition the roots. The "
             "carrier's A4 + A4′ is one of them, and its glue classes are the parallel lines.",
             "- **The tick's symmetry.** C_W(g) has 600 elements and acts on the plane as SL(2,5), the binary "
             "icosahedral group, and on the lines as PSL(2,5) = A5, the icosahedron on its six axes. With the day, "
             "N_W(⟨g⟩) acts on the lines as PGL(2,5), the exceptional S5.",
             "- **The day is a Singer cycle.** On F₂₅ the day is 2 + 2ω of order 24, and AIR_801 mod 5 is conjugate to "
             "minus it.",
             "- **The golden ratio is a Gauss sum.** The canon's A(h₀) is r + r⁴ − r² − r³, and on E8 the tick's Gauss "
             "sum squares to 5.",
             "- **The carrier is a shadow.** The mixed roots project onto the carrier's A4 as its five vertices and ten "
             "edges, and their Gram plus 2/5 is the signless incidence M behind D.",
             "- **The tick's hexad does not carry the parent.** The hub's A6 is generated on the tick's six lines by its "
             "PSL(2,5) and t = (23)(45). But the seed acts on those lines only through GL(2,5), so t is not one of its "
             "symmetries. The sun's decad carries the parent (below).",
             "- **The three primes (layer 26).** h = 30 = 2 × 3 × 5, and c′ = (−1)·s·g: the half-turn, the sun s = c′¹⁰ and "
             "the tick. Their fixed momenta are the residue rings of Z[ζ₃₀]: F₁₆ × F₁₆ (256), F₈₁ (81) and F₂₅ (25). The "
             "roots lie 2, 3 and 10 over their points. The centralizers act there as GO₈⁺(2), Sp(4,3) and SL(2,5).",
             "- **The regular clocks.** The regular numbers of E8 are the divisors of 30, 24 and 20, the orders of c′, the "
             "day and the golden clock. Their centralizers have the orders the degrees give, from 20 up to 155520. The "
             "three clocks make E8 a line over Z[ζ₃₀], Z[ζ₂₄] and Z[ζ₂₀]. Q(ζ₁₆) carries Z⁸ instead, since W(E8) has no "
             "element of order 16.",
             "- **The sun's decad.** On the sun's momenta c′ + c′⁻¹ is the golden ratio, so F₈₁ = F₉². The ten F₉-lines "
             "pull back to ten 4A2 frames that partition the roots. The F₉-linear isometries act on them as "
             "PSL(2,9) = A6, the hub's parent, with r the Coxeter clock and the doubling the day.",
             "- **No clock covers A6.** The orbit sizes 5⁴10²20¹⁶ add to 360, but every homomorphism from the circle "
             "to A6 has at most five elements in its image. Every clock group is solvable, and A6 is perfect. The "
             "parent is reached by the sun's symmetry, which is not a clock.", "",
             "## The four places (layer 27)", "",
             "The seed is read at four places, and each carries one sector of the model:", "",
             "| place | what the seed gives there | the sector | band values |", "|---|---|---|---|",
             "| real | E8 ⊗ R with the bath Δ = 240 − Σ T_r | the bath, its walks, moments and measures | [0, 256] |",
             "| 2 | the half-turn's 256 momenta, E8/2E8 = F₁₆ × F₁₆ | four qubits: the real Paulis, GKSL | 0, 224 (120), 256 (135) |",
             "| 3 | the sun's 81 momenta, F₈₁ = F₉² | the decad: the 360 parent, A6 = PSL(2,9) | 0, 243 (80) |",
             "| 5 | the tick's 25 momenta, F₂₅ = F₅² | the hexad: the carrier A4 + A4′, K5, D | 0, 250 (24) |", "",
             "- **One formula joins them.** At a fixed momentum of a prime clock the band is ε = 240 − Σ_r χ(r) for the "
             "matching character χ of the residue space. Ten roots over each of the tick's nonzero points and three over "
             "each of the sun's give ε = 250 and 243. At 2 the quadric's character sums ∓16 give 256 and 224, the band's "
             "top and its saddle.",
             "- **The golden ratio runs through all three primes.** Φ = 1 + g + g⁴ has Φ² = Φ + 1. At 5 it is the "
             "scalar 3 (ramified; 2Φ − 1 is the Gauss sum). At 3 it generates F₉, the decad's field. At 2 it is a cube "
             "root of unity on both primes. The Fibonacci companion has Pisano periods 3, 8 and 20.",
             "- **The qubits.** The two primes over 2 are complementary stabilizer groups of 16 commuting symmetric real "
             "Paulis. c′ keeps both and the mirror swaps them. W(E8)/⟨−1⟩ = GO₈⁺(2) is the real Clifford group of four "
             "qubits modulo the Paulis (cited).",
             "- **What the places cannot give.** An element of order n of GL₈(Z) needs ψ(n) ≤ 8. The memory clock "
             "(order 90, ψ = 10) and the circle (ψ = 38) are run by no lattice clock, and AIR_801 (determinant 12402) is "
             "none. So they stay inputs.", "",
             "## The derivation", "", "```mermaid", "flowchart TB"]
    for d in list(DERIVATION) + [SEED]:
        lines.append(f'    {d}["{name(d)}"]')
    for d, (p, ck) in DERIVATION.items():
        lines.append(f"    {p} --> {d}")
    lines += ["```", "", "| dot | built from | by the join | check | depth |", "|---|---|---|---|---|"]
    for d, (p, ck) in sorted(DERIVATION.items(), key=lambda kv: (len(_root(kv[0], DERIVATION)[1]), kv[0])):
        j = _join(d, p, ck)
        lines.append(f"| {name(d)} | {name(p)} | {j[2]} | `{ck}` | {len(_root(d, DERIVATION)[1]) - 1} |")
    lines += ["", "## The canon's inputs", "", "| input | what the canon supplies | it meets | status | why it stays an input |",
              "|---|---|---|---|---|"]
    for d, (what, m, ck) in INPUTS.items():
        j = _join(d, m, ck)
        lines.append(f"| {name(d)} | {what} | {name(m)} ({j[2]}) | {j[4]} | {WHY[d]} |")
    lines += ["", "Built from the inputs: " + ", ".join(f"{name(d)} (from {name(p)})" for d, (p, _) in FROM_INPUTS.items())
              + ".", ""]
    return "\n".join(lines)


def run():
    rep = Report("25-unify")
    for fn in (cyclotomic.cyclotomic_line, cyclotomic.galois_clocks, cyclotomic.residue_plane,
               cyclotomic.tick_normalizer, cyclotomic.clock_residues, cyclotomic.golden_gauss,
               cyclotomic.carrier_shadows, cyclotomic.parent_hexad):
        for name, ok in fn().items():
            rep.add(name, T, ok)
    for name, ok in derivation().items():
        rep.add(name, T, ok)
    for name, ok in uniqueness().items():
        rep.add(name, T, ok)
    rep.add("cited: E8 is the unique even unimodular lattice of rank 8; Coxeter elements are conjugate; a transitive "
            "A5 on six points is the icosahedral action on the axes", gates.SELECTED_REFERENCE, True)
    return rep
