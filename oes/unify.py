"""Layer 25. One object: the whole model from E8 and a Coxeter element.

E8 is the only even unimodular lattice of rank 8 (cited), and its Coxeter elements are all conjugate (cited; layer 19
exhibits the conjugator of c to c'). So the pair (E8, c') has no parameters. This layer shows that it builds every
structural dot of the diagram, and that the remaining dots are the canon's own inputs, each meeting the derived part
at a named interface.

The seed. E8 with c' is the cyclotomic line Z[zeta30] with the trace form Tr(alpha x ybar) (oes/cyclotomic.py (a)).

The derivation (DERIVATION) builds 53 dots from the seed, each by one THEOREM join of layer 23 whose check holds:
  - the trunk: E8 -> the cyclotomic line -> the clocks (the Galois group) -> the tick's residue plane F25 -> one
    residue line, the carrier's A4 + A4' -> either factor, A4 -> K5 (its positive roots) -> the vertices, the zero
    modes, the cycles and the source;
  - the residue plane's other branches: PGL(2,5) on the six lines (and from it the synthemes), the surface's six axes
    and PG(2,5);
  - the other primes (layer 26): the regular clocks from the clocks, and the sun's decad F81 = F9^2 from the
    cyclotomic line, from which the 360 parent is the sun's A6 on its ten 4A2 frames;
  - the arithmetic: the golden companion is the tick's Gauss sum;
  - the principal circle (layer 28): the Weyl vector's circle of momenta, into which the canon's circle embeds; it is
    unique up to W(E8), which keeps the band;
  - the number level (30 Oct): the time clock and the observer clock are the principal circle's critical steps of
    order 5 and 4, and the grain is the subgroup the critical steps generate (order 60), inside the seam Z/120 that
    the regular steps generate; the 27-clock, the coil, the miss set, the atlas and the vortex are the circle's
    subgroup lattice over the canon's cofactor 36 and stay built from the circle;
  - the lattice's harmonic analysis: the bath, the walks, the moments and measures, the half-periods with the Pauli
    algebra and GKSL, the Hodge 70, the momenta, the census and its torus, the root graph and its frame;
  - the carrier: the shadows of the mixed roots, then the triple, the readout, the binding, sound and light, the
    simplex, the cube, the ports and the six-site cone.
Each choice on the trunk is unique up to the symmetry already built, with one recorded selection. The six lines are
one orbit of the tick's normalizer, the line's stabilizer exchanges its two factors, and the circle's selection
144 -> c' is one of eight choices that the Galois clocks permute. But the stored day and golden clock are each one
of two conjugacy classes of the normalizer <c', d, v> over their Galois automorphisms (10 + 10 of order 24, 12 + 12
of order 20), with one characteristic polynomial, so conjugate in W(E8) but not relative to c'; the mirror's class
is unique (30 Oct).

The inputs (INPUTS) are ten: the circle Z/4320 with its stages and memory clock, the datum, the literal operands, the
words, the integers of the 801 matrix, the Standard-Model split of the five sites, the time unit and the product
geometry. Seven more dots are built from them (FROM_INPUTS): the 27-clock, the coil, the miss set, the atlas and the
vortex from the circle's cofactor 36 (their orders 27, 540, 864 and quotient sizes 36, 9 do not divide 120), the root
assignment from the split and FLRW from the product geometry. Two of the inputs meet the seed exactly: the circle is
the principal circle k -> k rho/4320, sampled at 4320 = 36 x 120 points, and mod 5 the 801 matrix is minus the day.
The memory clock meets the circle through the circle's 24 maps onto it, all conjugate under its symmetry, so its
stepping is unique up to that symmetry.

Unification at all levels (levels_unified, 30 Oct): every level holds derived dots, and inside every level they are
joined by THEOREM maps with both ends in the level; the derived part stands without the inputs, since the THEOREM
maps between derived dots connect it, no one such map and no one derived dot holds it together, and every derived
dot lies on at least three of them; every pair of levels is joined by at least two of them; and the derivation tree
is THEOREM to depth 8.
"""

import functools
import itertools
from collections import Counter
from math import gcd

import numpy as np
import sympy as sp

from . import cyclotomic, dots, gates, primes, principal, spine
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
    "principal": ("E8", "principal.circle"),
    "time": ("principal", "principal.critical_steps"), "observer": ("principal", "principal.critical_steps"),
    "grain": ("principal", "grain_steps"),
}

# input: (what the canon supplies, the derived dot it meets, the check of that interface join)
INPUTS = {
    "circle": ("the canon's circle Z/4320: the principal circle k -> k rho/4320 sampled at 4320 = 36 x 120 points, the seam "
               "Z/120 its regular steps generate refined by the cofactor 36 = 2^2 3^2; its step 144 goes to c', one of "
               "eight choices, all conjugate under the Galois clocks", "principal", "principal.circle"),
    "stages": ("the canon's fifteen stage indices on the circle", "circle", "counts.check_claims"),
    "memory": ("the 120-state memory clock; the circle maps onto it in 24 ways, all conjugate under its symmetry, and the "
               "canon's stepping is one of them (a selection)", "circle", "memory_quotients"),
    "datum": ("the canon's datum (psi0, v0) of energy 34: psi0 = (r + u, M^T r) for the A4 root r = e0 - e1 and the all-ones "
              "u (psi0 D^2 psi0 = 64, not a zero mode), and v0 the alternating 4-cycle 0-1-2-3, a zero mode of norm 4",
              "kerM", "counts.tick_tock"),
    "literal": ("the owner's native source matrices", "source", "literal_port"),
    "words": ("the canon's words 088, 086 and 980", "A4", "words_c5"),
    "air801": ("the integers of AIR_801; mod 5 it is minus the day on the residue plane", "residue", "clock_residues"),
    "charges": ("the Standard-Model split of the five sites, colour 0, 1, 2 and weak 3, 4", "V", "charges"),
    "calibration": ("the time unit tau of t = tau u (TIME_BIND unbound)", "readout", "calibration"),
    "gravity": ("the product geometry M4 x F with M4, f, L and m free (conditional)", "triple", "product_geometry"),
}

# input: why it stays an input
WHY = {
    "circle": "psi(4320) = 38 > 8, so no lattice clock runs Z/4320 (layer 27); but it is the principal circle k -> k rho/4320 "
              "of the seed's momenta, whose step 144 is the Coxeter clock's lift, whose steps of order 2 to 5 are the "
              "band's critical vertices (the time and observer clocks) and whose regular steps generate the seam Z/120; "
              "only the cofactor 36 = 4320/120 (the 27-clock, the coil, the miss set, the atlas and the vortex) and the "
              "stage indices are the canon's (layer 28, 30 Oct)",
    "stages": "the canon's fifteen indices on the circle",
    "memory": "order 90 and psi(90) = 10 > 8, so no lattice clock of the seed runs it (layer 27); 90 = 2 x 3^2 x 5 does not "
              "divide 120, so like the 27-clock it needs the canon's 3^2",
    "datum": "the relative position of an A4 root and a 4-cycle of K5, chosen by the canon; its S5-orbit is regular (layer 23)",
    "literal": "the owner's matrices; they match the derived source up to an explicit isometry (layer 10)",
    "words": "the canon's words; isometric to the oriented duads of K6 only over Q(sqrt2) (layer 23)",
    "air801": "determinant 12402, so no lattice clock; only its residue mod 5 is the seed's (layer 27)",
    "charges": "the 3 + 2 split chooses the Standard-Model gauge group; once chosen it is unique up to W(E8) (layer 24)",
    "calibration": "no internal number binds physical time (an obstruction, layer 23)",
    "gravity": "M4, f, L and m are free parameters; conditional (layer 6)",
}

# dot built from an input: (the dot it is built from, the check of the join that builds it)
FROM_INPUTS = {
    "c27": ("circle", "primary_split"), "atlas": ("circle", "atlas"), "coil": ("circle", "coil"),
    "vortex": ("atlas", "vortex"), "miss": ("circle", "tick_miss"), "assignment": ("charges", "assignment.standard_model"),
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


def _held():
    return {k: all(bool(v) for v in res.values()) for k, res in dots.check_results().items()}


def derivation(held=None):
    """The partition of the dots and the derivation tree, with every edge a held join."""
    held = _held() if held is None else held
    S = spine.subgroup
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
            and (len(DERIVATION), len(INPUTS), len(FROM_INPUTS)) == (53, 10, 7),
        "every derived dot is built by a THEOREM join of layer 23 whose check holds, and its parents lead back to E8 "
        "without a cycle":
            all(j is not None and j[4] == T and held[j[5]] for j in edges.values())
            and all(r == SEED for r, _ in roots.values()),
        "every dot built from an input comes by a held join that is not an obstruction, and leads back to an input":
            all(j is not None and j[4] in (T, CN) and held[j[5]] for j in built.values())
            and all(r in INPUTS for r, _ in roots_in.values()),
        "every input meets the derived part or another input at a held interface join, and two meet the seed exactly: "
        "the circle is the principal circle sampled at 4320 points, and the 801 matrix mod 5 is minus the day":
            all(j is not None and j[4] != OB and held[j[5]] for j in faces.values())
            and faces["circle"][4] == T and faces["air801"][4] == T,
        "the time clock, the observer clock and the grain are the seed's, at depth 2: the principal circle's points of order "
        "5, of order 4, and the subgroup its critical steps generate, inside the seam <36> = Z/120 that the thirteen regular "
        "steps generate (their gcd is 36); the five dots still built from the circle need its cofactor 36 = 4320/120, since "
        "their orders 27, 540 and 864 and quotient sizes 36 and 9 do not divide 120":
            functools.reduce(gcd, [4320 // d for d in primes.regular()]) == 36 and len(S(36)) == 120
            and all(120 % len(S(x)) == 0 for x in (864, 1080, 72)) and all(120 % n for n in (27, 540, 864, 36, 9))
            and {d: depth[d] for d in ("time", "observer", "grain")} == {"time": 2, "observer": 2, "grain": 2}
            and set(FROM_INPUTS) == {"c27", "coil", "miss", "atlas", "vortex", "assignment", "cosmology"},
        f"the trunk E8 -> cyclotomic line -> clocks -> residue plane -> A4 + A4' -> A4 -> K5 edges -> zero modes -> "
        f"source has depth {depth['source']}, and no dot is deeper than {max(depth.values())}":
            roots["source"][1] == ["source", "kerM", "E", "A4", "L0", "residue", "clocks", "cyclo", "E8"]
            and max(depth.values()) == 8,
    }


def _clock_classes():
    """For each stored clock, the elements of its order over its Galois automorphism and their conjugacy classes under
    the normalizer <c', d, v> of <c'>: how many elements, how many classes and their sizes, whether the two classes share
    a characteristic polynomial, and whether the day's defining condition d^4 = c'^5 picks one class."""
    k = cyclotomic.clocks()
    c, d, v, m = (np.rint(k[n]).astype(np.int64) for n in ("c", "day", "golden", "mirror"))
    P = [spine.mpow(c, j) for j in range(30)]
    key = lambda M: M.tobytes()
    normalizer = {}
    for j in range(30):
        for a in range(4):
            for b in range(2):
                x = P[j] @ spine.mpow(d, a) @ spine.mpow(v, b)
                normalizer[key(x)] = x
    inverses = {key(y): spine.inverse(y) for y in normalizer.values()}
    charpoly = lambda M: sp.Matrix(M.tolist()).charpoly().as_expr()
    out = {"normalizer": len(normalizer)}
    for name, n in (("day", d), ("golden", v), ("mirror", m)):
        o = spine.mat_order(n)
        same = [n @ P[j] for j in range(30) if spine.mat_order(n @ P[j]) == o]          # the same sigma, the same order
        keys = {key(z) for z in same}
        classes, reps, seen = [], [], set()
        for x in same:
            if key(x) in seen:
                continue
            cls = {key(y @ x @ inverses[key(y)]) for y in normalizer.values()}
            seen |= cls
            classes.append(len(cls & keys))
            reps.append(x)
        picked = [x for x in same if np.array_equal(spine.mpow(x, 4), P[5])] if name == "day" else []
        stored = {key(y @ n @ inverses[key(y)]) for y in normalizer.values()}
        out[name] = {"order": o, "elements": len(same), "classes": sorted(classes),
                     "one charpoly": len({charpoly(x) for x in reps}) == 1,
                     "picked": len(picked), "picked in one class": all(key(x) in stored for x in picked)}
    return out


def levels_unified(held=None):
    """Unification at all levels (30 Oct): every level holds derived dots, each level's derived dots are joined inside it
    by THEOREM maps, the derived part stands without the inputs, every pair of levels is joined twice between derived
    dots, and the derivation tree is THEOREM to depth 8. held: check name -> bool, from dots.check_results() when None."""
    if held is None:
        held = {k: all(bool(v) for v in res.values()) for k, res in dots.check_results().items()}
    derived = sorted(set(DERIVATION) | {SEED})
    inside_derived = [j[4] == T and held[j[5]] and j[0] in derived and j[1] in derived for j in dots.JOINS]
    maps = [k for k, ok in enumerate(inside_derived) if ok]
    one = lambda mask, ds=derived: len(dots.components(mask, statuses=(T,), dots=ds)) == 1
    per_level = {name: [d for d in ds if d in derived] for name, _, ds in dots.LEVELS}
    inside = {name: dots.components([ok and dots.JOINS[k][0] in ds and dots.JOINS[k][1] in ds
                                     for k, ok in enumerate(inside_derived)], statuses=(T,), dots=ds)
              for name, ds in per_level.items()}
    degree = Counter(x for k in maps for x in dots.JOINS[k][:2])
    bridges = [k for k in maps if not one([ok and i != k for i, ok in enumerate(inside_derived)])]
    cut_dots = [d for d in derived if not one([ok and d not in dots.JOINS[k][:2] for k, ok in enumerate(inside_derived)],
                                              [x for x in derived if x != d])]
    pairs = Counter(tuple(sorted((dots.LEVEL_OF[dots.JOINS[k][0]], dots.LEVEL_OF[dots.JOINS[k][1]]))) for k in maps
                    if dots.LEVEL_OF[dots.JOINS[k][0]] != dots.LEVEL_OF[dots.JOINS[k][1]])
    level_pairs = list(itertools.combinations(range(len(dots.LEVELS)), 2))
    depth = {d: len(_root(d, DERIVATION)[1]) - 1 for d in DERIVATION}
    tree = {d: _join(d, p, ck) for d, (p, ck) in DERIVATION.items()}
    counts = ", ".join(f"{len(per_level[name])} on the {name} level" for name, _, _ in dots.LEVELS)
    return {
        f"every level holds derived dots: {counts}": all(per_level[name] for name, _, _ in dots.LEVELS),
        "inside every level the derived dots are joined among themselves by THEOREM maps with both ends in the level":
            all(len(c) == 1 for c in inside.values()),
        f"the derived part stands without the inputs: the {len(derived)} derived dots are connected by the "
        f"{len(maps)} THEOREM maps between them, and removing any one such map, or any one derived dot with its maps, "
        "leaves the rest connected":
            one(inside_derived) and not bridges and not cut_dots,
        "every derived dot lies on at least three THEOREM maps to derived dots": all(degree[d] >= 3 for d in derived),
        "every pair of the six levels is joined directly by at least two THEOREM maps between derived dots":
            all(pairs[p] >= 2 for p in level_pairs),
        f"the derivation tree has depth {max(depth.values())}, at most 8, and every derived dot's derivation join is a "
        "THEOREM join of layer 23 whose check holds":
            max(depth.values()) <= 8 and all(j is not None and j[4] == T and held[j[5]] for j in tree.values()),
    }


def uniqueness():
    """Each choice on the trunk, and each stepping of an input by the circle, is unique up to symmetry."""
    lines = cyclotomic.tick_normalizer()
    galois = cyclotomic.galois_clocks()
    memory = dots.memory_quotients()
    circle = principal.principal_uniqueness()
    classes = _clock_classes()
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
        "the memory clock's stepping k -> A^k is one of the circle's 24 maps onto it, and its normalizer in S_120 "
        "realizes every unit mod 90, so all 24 are conjugate":
            all(memory.values()),
        "the principal circle is unique up to W(E8): the Weyl vector determines its positive system, W permutes the "
        "positive systems transitively (cited) and keeps the band, so the conjugate circles have the same band values, "
        "critical steps and types":
            all(circle.values()),
        "the day and the golden clock are recorded selections: over sigma_7 the normalizer <c', d, v> (240 elements) has "
        "20 elements of order 24 in two conjugacy classes of 10, and over sigma_11 24 elements of order 20 in two classes "
        "of 12; each pair of classes shares one characteristic polynomial (conjugate in W(E8), not relative to c'), the "
        "day's defining condition d^4 = c'^5 holds on 10 elements and does not pick a class, and the mirror's 30 "
        "involutions over sigma_29 are one class":
            classes["normalizer"] == 240
            and classes["day"] == {"order": 24, "elements": 20, "classes": [10, 10], "one charpoly": True, "picked": 10,
                                   "picked in one class": False}
            and classes["golden"] == {"order": 20, "elements": 24, "classes": [12, 12], "one charpoly": True, "picked": 0,
                                      "picked in one class": True}
            and classes["mirror"] == {"order": 2, "elements": 30, "classes": [30], "one charpoly": True, "picked": 0,
                                      "picked in one class": True},
    }


def unified_page():
    """docs/UNIFIED.md: the derivation as one page."""
    D = dots.DOTS
    name = lambda d: D[d][0]
    derived = set(DERIVATION) | {SEED}
    maps = sum(1 for j in dots.JOINS if j[4] == T and j[0] in derived and j[1] in derived)
    levels = ", ".join(f"{sum(d in derived for d in ds)} on the {n} level" for n, _, ds in dots.LEVELS)
    lines = ["# One object", "",
             "Layers 25 to 28 (`oes/unify.py`, `oes/cyclotomic.py`, `oes/primes.py`, `oes/places.py`, `oes/principal.py`). "
             "Generated by "
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
             "## The principal circle (layer 28)", "",
             "No lattice clock runs the canon's circle, but a circle of the seed's momenta does. E8 is unimodular, so the "
             "momenta live on ℝ⁸/E8, the maximal torus of the compact group E8, where the band is 248 − χ for the adjoint "
             "character χ. The Weyl vector ρ = (46, 68, 91, 135, 110, 84, 57, 29) is primitive with ⟨r, ρ⟩ = ht(r), so "
             "k ↦ kρ/4320 embeds ℤ/4320 there.", "",
             "- **The Coxeter step is Kostant's.** For each of the thirteen regular numbers d, ρ/d acts on the adjoint "
             "representation with the spectrum of a lift of the regular clock of order d. At d = 30 Kostant's theorem "
             "makes it conjugate to the lift of c′ (cited), so the canon's selection 144 → c′ is that identification. "
             "The steps 180 and 216 carry the day and the golden clock.",
             "- **The band at the regular steps** is 248 − 8μ(d)/φ(d): 256 at the half-turn, 252, 248, 250, 244, 248, "
             "246, 248, 247, 248, 248 and 249 at the Coxeter step.",
             "- **The canon's small clocks are the seed's critical steps.** The band is critical on the circle exactly at its "
             "nine elements of order 2 to 5: the half-turn 2160 (D8, 256), the 27-clock's 1440 and 2880 (A8, 252), the "
             "observer clock's 1080 and 3240 (D5 + A3, 248) and the time clock 864k (A4 + A4, 250, the carrier's root "
             "system). They are the alcove's vertices of marks 2, 3, 4 and 5. Every step of order above 29 is regular.",
             "- **The clocks are its subgroups (30 Oct).** The nine nonzero critical steps are the union of ⟨2160⟩, ⟨1440⟩, ⟨1080⟩ and "
             "⟨864⟩ and generate the grain ⟨72⟩, of order lcm(2, 3, 4, 5) = 60; the time and observer clocks meet in 0 and add "
             "to the golden step's ⟨216⟩ = ℤ/20. The thirteen regular steps are multiples of 36 and generate the seam ⟨36⟩, "
             "of order lcm(30, 24, 20) = 120, so the atlas ℤ/36 is the circle modulo the regular steps. The 27-clock ⟨160⟩ is "
             "the Sylow 3-subgroup, holding the sun's step ρ/3; the coil ⟨8⟩ is the grain plus the 27-clock; the miss set ⟨5⟩ "
             "is the kernel of the time coordinate; the vortex ℤ/9 is the 27-clock modulo the sun. The seed names the orders "
             "5, 4, 60 and 120, so the time clock, the observer clock and the grain are derived; 27, 32, 540, 864 and the "
             "quotient sizes 36 and 9 come from the canon's 4320 = 2⁵3³5 and do not divide 120, so the other five clocks "
             "stay built from the circle's cofactor 36. |⟨36⟩| = 120 = |G120| only numerically: G120 has no element of "
             "order 20 or 120.",
             "- **Unique up to W(E8).** The Weyl vector is the half-sum of the positive roots and is regular, so it determines its "
             "positive system. W(E8) permutes the positive systems transitively (cited) and keeps the band, so every conjugate "
             "circle k ↦ kwρ/4320 has the same band values, critical steps and types.", "",
             "## Unified at all levels (30 Oct)", "",
             "- **The number level is rooted in the principal circle.** Its derived dots are the time clock, the observer clock "
             "and the grain, joined inside the level by the golden step (⟨864⟩ + ⟨1080⟩ = ⟨216⟩) and the sum of the three small "
             "clocks (⟨864⟩ + ⟨1080⟩ + ⟨1440⟩ = ⟨72⟩); the observer clock is the regular class 4, the day's sixth power.",
             "- **The golden companion is joined inside the symmetry level.** It is the tick's negative cosine X = −(g + g⁻¹), "
             "with X² = X + I and characteristic polynomial (x² − x − 1)⁴; E8 has a basis of four roots and their images in "
             "which X is four Fibonacci blocks, so E8 = ℤ[φ]⁴. The day conjugates X to I − X (the Galois conjugation of "
             "Q(√5)), G120 acts on ℤ[X] through Gal(Q(√5)/Q) with kernel ⟨g, d²⟩, and X lies in a regular clock's cosine ring "
             "ℤ[w + w⁻¹] exactly for the orders divisible by 5.",
             "- **The nine-torus is placed.** Six of its nine frequencies are the band at the principal circle's critical steps "
             "(256, 252, 248, 250), at the half-periods (256 on the 135 of type D8, 224 on the 120 of type E7 + A1), at the "
             "sun's 80 momenta (243) and at the tick's 24 (250); √251, √(4025/16) and √(6800/27) are at none of them.",
             f"- **The structure** (`levels_unified`). Every level holds derived dots ({levels}); inside every level they are "
             "joined by THEOREM maps with both ends in the level; the derived part stands without the inputs: the "
             f"{len(DERIVATION) + 1} derived dots are connected by the {maps} THEOREM maps between them, no one such map and "
             "no one derived dot holds them together, and every derived dot lies on at least three of them; every pair of "
             "the six levels is joined directly by at least two of them; and the derivation tree is THEOREM to depth 8.", "",
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
    held = _held()
    for name, ok in derivation(held).items():
        rep.add(name, T, ok)
    for name, ok in levels_unified(held).items():
        rep.add(name, T, ok)
    for name, ok in uniqueness().items():
        rep.add(name, T, ok)
    rep.add("cited: E8 is the unique even unimodular lattice of rank 8; Coxeter elements are conjugate; a transitive "
            "A5 on six points is the icosahedral action on the axes", gates.SELECTED_REFERENCE, True)
    return rep
