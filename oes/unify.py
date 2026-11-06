"""Layer 25. One object: the whole model from E8 and a Coxeter element.

E8 is the only even unimodular lattice of rank 8 (cited), and its Coxeter elements are all conjugate (cited; layer 19
exhibits the conjugator of c to c'). So the pair (E8, c') has no parameters. This layer shows that it builds every
structural dot of the diagram, and that the remaining dots are the canon's own inputs, each meeting the derived part
at a named interface.

The seed. E8 with c' is the cyclotomic line Z[zeta30] with the trace form Tr(alpha x ybar) (oes/cyclotomic.py (a)).

The derivation (DERIVATION) builds 61 dots from the seed, each by one THEOREM join of layer 23 whose check holds:
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
    the regular steps generate; the 27-clock is the seed's singular 3-primary points <rho/27> and gives the vortex and
    the coil (1 Nov); the miss set and the atlas stay built from the circle's 2-part 2^5;
  - the lattice's harmonic analysis: the bath, the walks, the moments and measures, the half-periods with the Pauli
    algebra and GKSL, the Hodge 70, the momenta, the census and its torus, the root graph and its frame;
  - the carrier: the shadows of the mixed roots, then the triple, the readout, the binding, sound and light, the
    simplex, the cube, the ports and the six-site cone;
  - the Standard-Model frame (1 Nov): the five-site charges from the carrier's A4 (T3 = alpha/2 for a root alpha,
    the colour the A2 of the carrier roots orthogonal to it, Y the commutant line of A1(alpha) + A2, Q = T3 + Y
    vanishing on a site: 40 triples, one S5 x {+-1}-orbit; the 967680 frames of E8 are one W(E8)-orbit, with
    stabilizer S3 x W(A4') of order 720), and from them the root assignment.
Each choice on the trunk is unique up to the symmetry already built, with one recorded selection. The six lines are
one orbit of the tick's normalizer, the line's stabilizer exchanges its two factors, and the circle's selection
144 -> c' is one of eight choices that the Galois clocks permute. But the stored day and golden clock are each one
of two conjugacy classes of the normalizer <c', d, v> over their Galois automorphisms (10 + 10 of order 24, 12 + 12
of order 20), with one characteristic polynomial, so conjugate in W(E8) but not relative to c'; the mirror's class
is unique (30 Oct). The Standard-Model frame is unique up to W(E8) too (sm_frame); what it records is its Levi type,
3 + 2 (weak = a root A1, colour = its orthogonal A2) against 4 + 1, two different Aut(A4)-orbits: a recorded
selection, like the day and the golden clock, that carries no number (1 Nov).

The inputs (INPUTS) are ten: the circle Z/4320 with its stages and memory clock, the datum, the literal operands, the
words, the integers of the 801 matrix, the time unit, the product geometry and the declared action with its
reference completion (6 Nov; a family: its selections are recorded). Four more dots are built from them
(FROM_INPUTS): the miss set and the atlas from the circle's 2-part 2^5 (the 27-clock, the vortex and the coil, once
built from the cofactor 36, are derived since 1 Nov), FLRW from the product geometry, and the one spectrum from the
action (its one loop, spc_oneloop). The time unit is one
positive real tau, and the product geometry's mass scale is the same scale, m = 1/tau (cosmos_calibration); the
rest of the product geometry is M4 and the dimensionless l = L/m, F0, F1 and F2, of which only G m^2 and
Lambda/m^2 are observable at this order (native_onset). Four of the inputs split into a derived part and a part the
canon adds (1 Nov), a recorded selection for three and external integers for AIR_801: the datum's type and
representative are the seed's and only its S5-orbit (one of five) is selected;
the literal operands are the derived port in the time clock's integral chart up to one sign and the owner's basis; the
words are the seed's Coxeter frames up to one of 18 identifications; AIR_801's residue is forced by the day and only
its integers are external. Two of the inputs meet the seed exactly: the circle is
the principal circle k -> k rho/4320, sampled at 4320 = 36 x 120 points, and mod 5 the 801 matrix is conjugate to minus the day.
The memory clock meets the circle through the circle's 24 maps onto it, all conjugate under its symmetry, so its
stepping is unique up to that symmetry.

Unification at all levels (levels_unified, 30 Oct): every level holds derived dots, and inside every level they are
joined by THEOREM maps with both ends in the level; the derived part stands without the inputs, since the THEOREM
maps between derived dots connect it, no one such map and no one derived dot holds it together, and every derived
dot lies on at least three of them; every pair of levels is joined by at least two of them; and the derivation tree
is THEOREM to depth 8.
"""

import collections
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
    "icosians": ("E8", "icosians"), "penrose": ("A4", "penrose_planes"),
    "time": ("principal", "principal.critical_steps"), "observer": ("principal", "principal.critical_steps"),
    "grain": ("principal", "grain_steps"),
    "c27": ("principal", "principal.singular_primary"), "vortex": ("c27", "principal.singular_primary"),
    "coil": ("grain", "principal.singular_primary"),
    "charges": ("A4", "sm_frame"), "assignment": ("charges", "assignment.standard_model"),
    "chiral": ("carrier", "chiral_closures"),
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
    "literal": ("the owner's native source matrices: the derived port in the time clock's integral chart, up to one "
                "sign and the basis N_source", "source", "literal_chart"),
    "words": ("the canon's words 088, 086 and 980", "A4", "words_c5"),
    "air801": ("the integers of AIR_801; mod 5 it is conjugate to minus the day on the residue plane", "residue", "clock_residues"),
    "calibration": ("the time unit tau of t = tau u, one positive real (TIME_BIND unbound)", "readout", "calibration"),
    "gravity": ("the product geometry M4 x F: M4, the cutoff's moments F0, F1, F2 and l = L/m, with m = 1/tau "
                "(conditional)", "triple", "product_geometry"),
    "action": ("the declared native action of layer 4 (native.NativeSystem: q = (a, b) on ker M + ker M, the six-site port "
               "Pi with iota = I6, M_s, W_p and the adapter) with its port multiplier, plus the reference completion "
               "K_theta = H + theta (eps + J V J^T), theta = 1 the reference (master_response): a family, not one action",
               "source", "act_native"),
}

# input: why it stays an input
WHY = {
    "circle": "psi(4320) = 38 > 8, so no lattice clock runs Z/4320 (layer 27); but it is the principal circle k -> k rho/4320 "
              "of the seed's momenta, whose step 144 is the Coxeter clock's lift, whose steps of order 2 to 5 are the "
              "band's critical vertices (the time and observer clocks) and whose regular steps generate the seam Z/120; "
              "only the 2-part 32 = 2^5 of the sampling (the cofactor's 2^2 over the seam's 2^3; the miss set and the atlas need "
              "it; the 3-part is the seed's singular 3-primary points <rho/27>, which build the 27-clock, the vortex and the coil, "
              "and no single rule of the seed gives 2^5 3^3 5) and the orientation fixed by the "
              "stage indices are the canon's (layer 28, 30 Oct)",
    "stages": "the count fifteen and the one-sided segment: every E8 class on the circle is closed under k -> -k, so the "
              "stages fix an orientation; given it they are the fifteen least-band points of the half-circle, and their landing "
              "pattern is the seed's (stage_frame, 1 Nov)",
    "memory": "order 90 and psi(90) = 10 > 8, so no lattice clock of the seed runs it (layer 27); its group Z/90 = <rho/9> + "
              "<rho/10> is the seed's, but its 120 states are the canon's: A^10 fixes 111 of them, and no Weyl action on the 120 "
              "root lines can (a hyperplane holds at most 63), nor does the seed's own 90-set, the sun's hyperbolic D4 lines "
              "(memory_not_seed, 1 Nov)",
    "datum": "the type and the representative are the seed's: the 600 data of its type (20 A4 roots x 30 norm-4 zero modes) "
             "all have energy 34 and are alike in every D^2 sector, and the stabilizer of their reading in W(E8) is "
             "W(A4) x W(A4') (14400), acting as S5 with five free orbits; the canon picks the orbit with <r, a><r, b> = -1, "
             "one of five (W(E8) leaves 4 Gram classes of the bare root triples, 3 with time reversal): a recorded "
             "selection, and dynamically inert (datum_frame, 1 Nov)",
    "literal": "one sign and one basis: the owner's port is the derived commutator read in the time clock's integral chart "
               "(the pentagon edges and the pentagram circulation, W_p = 2 F^T F), one of 480 integral W_p-charts that S5 and "
               "the 40 symmetries of W_p make one orbit; the bath's 20 site symmetries leave two orbits, so the apex sign "
               "(the pentagram read along R^2, not R^3) is the owner's, and so is the basis N_source of ker M, five of the "
               "fifteen K4 matching modes (literal_chart, 1 Nov)",
    "words": "as a D3-set the words are the seed's fifteen Coxeter frames, but the clocks act on the frames as AGL(1, Z/15) "
             "and only Z/4 = {1, 4, 7, 13} of it commutes with the D3, so the canon's identification is one of 18 classes "
             "of 4 (a recorded selection); the digits 0, 6, 8, 9 and their flip 6 <-> 9 (order 2, against order 4 for the "
             "seed's orbit-swapping maps) are decimal data (word_frames, 1 Nov)",
    "air801": "only its residue is the seed's, and the day forces it (one of the 20 GL(2,5)-conjugates of -d); its integers "
              "are external: trace 1009 and det 12402 != +-1 (no lattice clock), discriminant 968473 squarefree with narrow "
              "class number 4, one class per genus, so even its polynomial leaves four integral classes; its columns are "
              "180-degree digit rotations (air801_classes, 1 Nov)",
    "calibration": "one positive real tau: every derived number is invariant under tau -> lambda tau (calibration; "
                   "notes_1340: the tick is a symmetry of the native flow, not a step of it), one measured rate fixes "
                   "it (an antisymmetric-Pauli rate Gamma gives tau = 224/Gamma, join_e8_calibration), and the product "
                   "geometry's and FLRW's mass scale is the same scale, m = 1/tau (cosmos_calibration)",
    "gravity": "M4 (a closed spin Riemannian 4-manifold), the cutoff's moments F0, F1, F2 and l = L/m are free, with "
               "m = 1/tau the calibration's scale; at this order only G m^2 = pi/(5 F1 l^2) and Lambda/m^2 = "
               "6 (F2/F1) l^2 - 16 + 40 (F0/F1)/l^2 are observable, two numbers from four inputs (native_onset); "
               "conditional (layer 6)",
    "action": "the declared action is the canon's (layer 4; native.run's UNFORMED 'physical action selection' stands) and "
              "its completion is a family: theta (flower_homotopy), eps, alpha and the placement J (schur_zero_mode), the "
              "mark (mgm_marks), the instance (ROOT, BALL r2 = 8 or COMP: master_response, act_native, flower_homotopy), "
              "the port Pi and the cone point (brg_bonds), iota (canon_flower_pullback), the unit of M_s and W_p with the "
              "adapter (literal_chart, literal_port) and the datum F put into V := F - S_eps^-1 (act_no_reduction) are "
              "selections that no join promotes; theta > 0 adds the reference term, so theta = 1 is labelled the "
              "reference completion and no term is added to the declared action",
}

# dot built from an input: (the dot it is built from, the check of the join that builds it)
FROM_INPUTS = {
    "atlas": ("circle", "atlas"), "miss": ("circle", "tick_miss"), "cosmology": ("gravity", "friedmann"),
    "spectrum": ("action", "spc_oneloop"),
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
            and (len(DERIVATION), len(INPUTS), len(FROM_INPUTS)) == (61, 10, 4),
        "every derived dot is built by a THEOREM join of layer 23 whose check holds, and its parents lead back to E8 "
        "without a cycle":
            all(j is not None and j[4] == T and held[j[5]] for j in edges.values())
            and all(r == SEED for r, _ in roots.values()),
        "every dot built from an input comes by a held join that is not an obstruction, and leads back to an input":
            all(j is not None and j[4] in (T, CN) and held[j[5]] for j in built.values())
            and all(r in INPUTS for r, _ in roots_in.values()),
        "every input meets the derived part or another input at a held interface join, and two meet the seed exactly: "
        "the circle is the principal circle sampled at 4320 points, and the 801 matrix mod 5 is conjugate to minus the day":
            all(j is not None and j[4] != OB and held[j[5]] for j in faces.values())
            and faces["circle"][4] == T and faces["air801"][4] == T,
        "the time clock, the observer clock and the grain are the seed's, at depth 2: the principal circle's points of order "
        "5, of order 4, and the subgroup its critical steps generate, inside the seam <36> = Z/120 that the thirteen regular "
        "steps generate (their gcd is 36); the 27-clock is the seed's singular 3-primary points <rho/27> at depth 2, with "
        "the vortex (its image on the sun's A8) and the coil (<rho/60> + <rho/27>) at depth 3; only the miss set (864 = "
        "32 x 27 points) and the atlas (36 = (32/8)(27/3)) are still built from the circle, needing its 2-part 32 = 2^5, "
        "and the one spectrum is built from the action (spc_oneloop, 6 Nov)":
            functools.reduce(gcd, [4320 // d for d in primes.regular()]) == 36 and len(S(36)) == 120
            and all(120 % len(S(x)) == 0 for x in (864, 1080, 72)) and all(120 % n for n in (864, 36))
            and {d: depth[d] for d in ("time", "observer", "grain", "c27", "vortex", "coil")}
            == {"time": 2, "observer": 2, "grain": 2, "c27": 2, "vortex": 3, "coil": 3}
            and set(FROM_INPUTS) == {"miss", "atlas", "cosmology", "spectrum"} and 36 == (32 // 8) * (27 // 3),
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


def _theorem_distance(held):
    """THEOREM-join distance from the seed over the joins whose checks hold."""
    adj = {d: set() for d in dots.DOTS}
    for j in dots.JOINS:
        if j[4] == T and held[j[5]]:
            adj[j[0]].add(j[1])
            adj[j[1]].add(j[0])
    dist, frontier = {SEED: 0}, [SEED]
    while frontier:
        nxt = []
        for u in frontier:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    nxt.append(v)
        frontier = nxt
    return dist


# the canon's inputs (and dots built from them) that sat three THEOREM joins from the seed, with their direct joins
DEEP_INPUTS = {"air801": T, "datum": T, "memory": OB}


def deepest_dots(held=None):
    """The deepest dots joined to the seed (1 Nov): every dot of the derivation's last two generations has a direct
    THEOREM join to E8, the deepest of the canon's inputs meet E8 directly, and every dot but the product geometry and
    FLRW is within two THEOREM joins of the seed (`star` sharpens this). held: check name -> bool, from
    dots.check_results() when None."""
    if held is None:
        held = {k: all(bool(v) for v in res.values()) for k, res in dots.check_results().items()}
    depth = {d: len(_root(d, DERIVATION)[1]) - 1 for d in DERIVATION}
    deep = sorted(d for d, k in depth.items() if k >= 7)
    direct = lambda d, status: [j for j in dots.JOINS if {j[0], j[1]} == {SEED, d} and j[4] == status and held[j[5]]]
    dist = _theorem_distance(held)
    rest = [d for d in dots.DOTS if d not in ("gravity", "cosmology")]
    names = ", ".join(dots.DOTS[d][0] for d in deep)
    return {
        f"the {len(deep)} dots of the derivation's last two generations (depth 7 and 8: {names}) each have a direct "
        "THEOREM join to the seed whose check holds":
            len(deep) == 16 and max(depth.values()) == 8 and all(direct(d, T) for d in deep),
        "so every derived dot is within two THEOREM joins of the seed, and the deepest within one":
            max(dist[d] for d in DERIVATION) <= 2 and all(dist[d] == 1 for d in deep),
        "the deepest of the canon's inputs meet the seed directly: AIR_801 (its lattice lifts in the tick's normalizer) "
        "and the datum (three roots of the A4) by THEOREM joins, and the memory clock by an OBSTRUCTION (no Weyl clock of "
        "order 45); the coil, once among them, is now derived (1 Nov)":
            all(direct(d, st) for d, st in DEEP_INPUTS.items()),
        "every dot but the product geometry and FLRW (which attach only through CONDITIONAL joins) is within two "
        "THEOREM joins of the seed; the star at the seed (`star`) brings all but four of them within one":
            all(d in dist and dist[d] <= 2 for d in rest) and "gravity" not in dist and "cosmology" not in dist
            and sorted(d for d in rest if dist[d] == 2) == sorted(STAR_OBSTRUCTED + STAR_SELECTED + ("calibration",)),
    }


# the dots that meet the seed directly only by an obstruction, through the owner's selected operand file, or through a
# binding the model does not supply (1 Nov, the star at the seed)
STAR_OBSTRUCTED = ("memory",)
STAR_SELECTED = ("literal", "words")
STAR_CONDITIONAL = ("calibration", "gravity", "cosmology")

# the one action and the one spectrum (6 Nov). A relation of the completed action K_theta = H + theta (eps + J V J^T) to a
# dot: (id, dot, relation, the domain and the J it is stated on, the identity, the checks that hold it, the identity's
# status, the selection it rests on and that selection's status). The J's: cone-J15 = master_response's 15 bond roots
# e_i + e_5, e_i - e_j; J19 = cone-J15 plus the auxiliaries e_i + e_6 (i < 4, schur_zero_mode's choice); COMP-J19 = the
# first 19 channels of bridge_comparator's 90D comparator in D19's order; glue-J15 = master_readout's invariant injection.
Relation = collections.namedtuple("Relation", "id dot relation domain identity checks identity_status selection selection_status")
ONE_RELATIONS = (
    Relation("R0", "bath", "restriction",
             "q = 0, lambda = 0, theta = 0; on ROOT with cone-J15 (master_response) and on a generic block with Y = [I; 0] "
             "(chiral_time)",
             "L = (1/2)|Phi'|^2 - (1/2)<Phi, H Phi> and Phi'' + H Phi = 0: K_0 = H entry by entry, and the update theta "
             "(eps + Y V Y^T) is invisible to the hidden side for every theta, Q K_theta Y = Q H Y (ran J in ran Y), so the "
             "hidden rows, the first hidden covariance Y^T K Q K Y = B B^T and the Krylov spaces are the bath's",
             ("chiral_time", "master_response"), T,
             "the instance stands in for Delta: ROOT is a compression of the bath (usm_bulk_heat) and the LATTICE instance "
             "is analytic: SELECTED_REFERENCE", SR),
    Relation("R1", "chiral", "completion",
             "theta = 1; cone-J15 at eps = 0, 1 for every symmetric F (act_no_reduction, master_response with F = D^2), "
             "J19 at eps = 1 with F19(alpha = 1) (schur_zero_mode) and regulator-free at eps = 0 (threshold_action, "
             "multipole_k0_threshold), COMP-J19 at eps = 3 (flower_homotopy)",
             "Schur_J(K_1) = F at z = 0, K_1 = L diag(F, C_eps) L^T with an F-independent lift L = [I; -C_eps^-1 B^T], so "
             "nullity K_1 = nullity F (1 for F19 at alpha > 0, 5 for diag(D^2, B2, B2)) and K0 = H + J (F - S0^-1) J^T is "
             "congruent to diag(F, C) without a regulator; the convex family K_theta = (1 - theta) H + theta K_1 is "
             "positive semidefinite with a kernel only at theta = 1",
             ("master_response", "schur_zero_mode", "flower_homotopy", "threshold_action"), T,
             "alpha and the mark: CONDITIONAL (no dot fixes them; unify.uniqueness); the J19 placement e_i + e_6: "
             "SELECTED_REFERENCE (by our choice, schur_zero_mode; brg_symmetry: it breaks C5); eps: CONDITIONAL", CN),
    Relation("R2", "chiral", "reduction: Gaussian elimination of the hidden roots at frequency z, then the limit eps -> infinity",
             "q = 0, lambda = 0, theta = 1; generic blocks symbolic (deep_zero_pole, Theorem 6) and cone-J15 exact at "
             "eps = 1, 10, 100, z = 1 (act_dressing)",
             "S_K(z)^-1 = F + z [I + B C_eps^-1 (z + C_eps)^-1 B^T] = F + z + X(eps) - X(eps + z); the kinetic dressing "
             "M_W(eps) = I + B C_eps^-2 B^T = S_eps^-1 T_eps S_eps^-1 (in this order only) = d/dz S_K(z)^-1 at 0, with "
             "B B^T/(244 + eps)^2 <= M_W - I <= B B^T/(184 + eps)^2 and tr B B^T = 760; as eps -> infinity M_W -> I, V -> "
             "-infinity and the memory -> 0: the bath freezes and the reduced action tends to (1/2)|x'|^2 - (1/2) x^T F x "
             "with whatever datum F was put in",
             ("deep_zero_pole", "act_dressing"), T,
             "eps: CONDITIONAL (at finite eps the kinetic term is dressed); F := D^2: CONDITIONAL (the limit returns every "
             "F, so it derives neither the carrier nor the chiral action: the critique's O2)", CN),
    Relation("R7", "source", "static reduction with the dressed metric (no dynamical equation is compared: the critique's F5)",
             "COMP-J19: Pi = the first 19 channels, iota = the cycles' inclusion into the edge block (R^10 -> R^19, isometric "
             "on L6), W_p = I, M_s = diag(W, W)/4, eps = 3, alpha = 1 (canon_flower_pullback); the model's port g = "
             "W_AS(a ^ b) (flower_source)",
             "the reduced static potential V_s + x^T F19 x/2 (x = iota g) obeys Euler's identity q . grad V = q^T "
             "diag(W, W) q + 2|g|^2 + 2 g^T F_E g, so q = 0 is its only critical point with h* = 0, Hessian diag(W, W), "
             "M_s^-1 diag(W, W) = 4 I10 and a vanishing source-bath cross block; the static dressing graph q -> (x(q), "
             "h*(q)) has metric M_s + Z0 J_g^T J_g with Z0 = 41598/41209, the dressed zero pole's norm, not M_s + J_g^T "
             "J_g; the pullback metric's Christoffel term is 2 J_g^T g(v), and layer 4's native equations are the theta = "
             "0 case with the same term",
             ("canon_flower_pullback", "flower_source"), T,
             "iota, theta = 1 and the six-section E6 containing q0 (flower_sections): CONDITIONAL; R5 = R7, the native "
             "system against the pullback: CONDITIONAL (LEDGER section II.4; W_p against I and the ball bath against the "
             "comparator differ)", CN),
)

# the recorded selections of the one action: (tag, the model function that fixes or records it, what it is); the first
# ten are bind_selections' table, then the instance, the cone point and the datum F (the critique's M7)
ONE_SELECTIONS = (
    ("theta", "flower_homotopy", "the convex family K_theta = (1 - theta) H + theta K19 at the note's five theta"),
    ("eps", "schur_zero_mode", "eps = 1 on the root-site instance (master_response's regulator)"),
    ("alpha", "schur_zero_mode", "the admissible S_alpha at alpha = 1 (chiral_closures' F19 = D19^2 symbolic in alpha)"),
    ("the mark", "mgm_marks", "the twelve Golden marks, their zero lines and their average"),
    ("J", "schur_zero_mode", "J19 into the 45-channel section (master_readout's J15 and the dark four)"),
    ("W_p", "literal_port", "the owner's W_p in boundary order"),
    ("the adapter", "literal_port", "the reconstructed port up to a commutant element (parent_readers' marked adapter)"),
    ("iota", "canon_flower_pullback", "the cycles' inclusion into the edge block of R^19, an isometry on L6"),
    ("the parity", "zero_pole_parity", "the D10 parity of the zero-mode line against the golden time line"),
    ("the readout", "master_readout", "the 45 channels and D45 = (2117, 967^8, 389^26, 127^6, 83^4)"),
    ("the instance", "master_response", "ROOT (the 240-root shell with the 15 bond atoms), BALL r2 = 8 or COMP (the "
                                        "90-channel comparator): act_native, flower_homotopy"),
    ("the cone point", "brg_bonds", "the origin x0 under the bond bridge w, the site W_p's corner 2/5 singles out and "
                                    "boundary_rotation fixes"),
    ("the datum F", "act_no_reduction", "the datum put into V := F - S_eps^-1; Schur_J(K_1) = F for every F, so F = D^2 "
                                        "is data, not a reduction of the bath"),
)

# the dots with no held map (THEOREM, SELECTED_REFERENCE or CONDITIONAL) to the one action or the one spectrum, nor to a
# dot that has one, with the reason (the critique's M7; computed from the joins, then recorded)
ONE_NONE = (
    ("memory", "the memory clock's held maps go to the circle, the 27-clock, the grain, the vortex, the time clock and the "
               "miss set (memory_clock, memory_quotients, join_c27_memory, join_grain_memory, join_memory_miss), none of which "
               "is one held map from the one action or the one spectrum, and it meets the seed only by obstructions "
               "(join_e8_memory, memory_not_seed): three joins from the action, through the circle and the seed"),
)

# the ten D19 joins moved from the triple onto the chiral completion (the critique's M4): (label, check)
M4_JOINS = (
    ("the chiral floor and its completion", "chiral_closures"), ("the one alpha-free ratio", "video_ten_chiral"),
    ("the chiral source's floor", "deep_zero_pole"), ("the convex chiral homotopy", "flower_homotopy"),
    ("the relative heat of the chiral completion", "usm_relheat_comparator"), ("the spine's cubic moment", "usm_spine_cubic"),
    ("the pullback's vacuum misses the chiral zero", "canon_flower_pullback"), ("no golden-to-Hodge intertwiner", "ff5_intertwiner"),
    ("the averaged Golden stiffness", "mgm_marks"), ("the averaged chiral completion", "mgm_dirac20"),
)


def _theorem_graph(held):
    adj = {d: set() for d in dots.DOTS}
    for j in dots.JOINS:
        if j[4] == T and held[j[5]]:
            adj[j[0]].add(j[1])
            adj[j[1]].add(j[0])
    return adj


def _bfs(adj, s):
    dist, frontier = {s: 0}, [s]
    while frontier:
        nxt = []
        for u in frontier:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    nxt.append(v)
        frontier = nxt
    return dist


def star(held=None):
    """Every dot joined directly to the seed (1 Nov, "join all dots"): each of the other 75 dots has a direct join to
    E8 whose check holds, by THEOREM for all but six: the memory clock (an obstruction), the owner's
    operand file and the fifteen words (selected references) and the three dots that need a binding (conditional). held: check name -> bool,
    from dots.check_results() when None."""
    if held is None:
        held = {k: all(bool(v) for v in res.values()) for k, res in dots.check_results().items()}
    others = [d for d in dots.DOTS if d != SEED]
    direct = {d: {j[4] for j in dots.JOINS if {j[0], j[1]} == {SEED, d} and held[j[5]]} for d in others}
    theorem = [d for d in others if T in direct[d]]
    rest = sorted(d for d in others if T not in direct[d])
    adj = _theorem_graph(held)
    dist = _bfs(adj, SEED)
    reach = sorted(dist)
    ecc = {d: max(_bfs(adj, d).values()) for d in reach}
    return {
        f"each of the {len(others)} other dots has a direct join to the seed whose check holds: {len(theorem)} by "
        "THEOREM, the nine-torus among them (its nine frequencies are the band's critical values on E8's roots, though "
        "no periodic lattice E8/mE8 carries its two non-integral ones); the memory clock (no Weyl clock of order 45) "
        "by an OBSTRUCTION; the owner's operand file and the fifteen words (E8 fixes "
        "their frames, not which digit goes where) by SELECTED_REFERENCES; and the calibration, the product geometry "
        "and FLRW by CONDITIONAL joins that name the binding still missing":
            all(direct[d] for d in others) and len(others) == 75 and len(theorem) == 69
            and rest == sorted(STAR_OBSTRUCTED + STAR_SELECTED + STAR_CONDITIONAL)
            and all(OB in direct[d] for d in STAR_OBSTRUCTED) and all(SR in direct[d] for d in STAR_SELECTED)
            and all(gates.CONDITIONAL in direct[d] for d in STAR_CONDITIONAL) and {T, OB} <= direct["torus"],
        "so the THEOREM joins make a star at the seed: 69 dots one join from E8, and the memory clock, "
        "the operand file, the words and the calibration two (the seed's eccentricity in the THEOREM graph is 2)":
            all(dist[d] == 1 for d in theorem)
            and sorted(d for d in dist if dist[d] == 2) == sorted(STAR_OBSTRUCTED + STAR_SELECTED + ("calibration",))
            and ecc[SEED] == 2,
        f"the THEOREM joins reach {len(reach)} of the 76 dots, any two of them at most {max(ecc.values())} joins apart "
        "(the diameter), and the product geometry and FLRW meet the seed only through CONDITIONAL joins":
            len(reach) == 74 and max(ecc.values()) == 3 and "gravity" not in dist and "cosmology" not in dist,
    }


def one_partition(held):
    """The three-way partition of the other dots by their held maps (THEOREM, SELECTED_REFERENCE or CONDITIONAL) to
    the one action or the one spectrum: direct, through one held map to a direct dot, or none."""
    one = {"action", "spectrum"}
    ok = lambda j: j[4] in (T, SR, CN) and held[j[5]]
    direct = {d for j in dots.JOINS if ok(j) for d in j[:2] if d not in one and set(j[:2]) & one}
    via = {}
    for j in dots.JOINS:
        if ok(j):
            for x, y in ((j[0], j[1]), (j[1], j[0])):
                if x not in one and x not in direct and y in direct:
                    via.setdefault(x, (y, j[2], j[5]))
    none = sorted(d for d in dots.DOTS if d not in one and d not in direct and d not in via)
    return sorted(direct), via, none


def one_model(held=None):
    """The one action and the one spectrum (6 Nov): the three dots' classification, the relations of ONE_RELATIONS, the
    M4 re-pointing, the gates and the partition of the dots by their routes to the one action or the one spectrum.
    held: check name -> bool, from dots.check_results() when None."""
    held = _held() if held is None else held
    depth = {d: len(_root(d, DERIVATION)[1]) - 1 for d in DERIVATION}
    e8 = {d: _join(SEED, d, ck) for d, ck in (("action", "brg_bonds"), ("spectrum", "usm_bulk_heat"),
                                              ("chiral", "spc_penrose_chiral"))}
    m4 = {lc: [j for j in dots.JOINS if (j[2], j[5]) == lc] for lc in M4_JOINS}
    tdeg = Counter(x for j in dots.JOINS if j[4] == T and held[j[5]] for x in j[:2])
    direct, via, none = one_partition(held)
    others = [d for d in dots.DOTS if d not in ("action", "spectrum")]
    return {
        "the three dots: action is a canon input meeting source at act_native, spectrum is built from it by spc_oneloop, "
        "chiral is derived from the carrier by chiral_closures at depth 6, and each has a direct THEOREM join to E8 whose "
        "check holds (brg_bonds, usm_bulk_heat, spc_penrose_chiral)":
            INPUTS["action"][1:] == ("source", "act_native") and FROM_INPUTS["spectrum"] == ("action", "spc_oneloop")
            and DERIVATION["chiral"] == ("carrier", "chiral_closures") and depth["chiral"] == 6
            and all(j is not None and j[4] == T and held[j[5]] for j in e8.values()),
        "every row of ONE_RELATIONS holds with its recorded status: each named check is held, the identity is THEOREM, "
        "and each selection carries CONDITIONAL or SELECTED_REFERENCE, so no selection is promoted":
            all(held[c] for r in ONE_RELATIONS for c in r.checks)
            and all(r.identity_status == T and r.selection_status in (CN, SR) for r in ONE_RELATIONS),
        "the ten D19 joins sit on the chiral completion (M4), and the triple still lies on at least three THEOREM maps":
            all(len(js) == 1 and "chiral" in js[0][:2] and "triple" not in js[0][:2] for js in m4.values())
            and tdeg["triple"] >= 3,
        "the one action is a family and the gates stand: TIME_BIND UNBOUND and DYN_BIND NOT_INSTALLED, with "
        "onemodel_gates and bind_selections held":
            gates.GATES["TIME_BIND"] == "UNBOUND" and gates.GATES["DYN_BIND"] == "NOT_INSTALLED"
            and held["onemodel_gates"] and held["bind_selections"],
        "every dot is joined to the one action or the one spectrum directly by a held map, or through one held map to "
        "a dot that is, or lies in ONE_NONE with its reason":
            sorted(list(direct) + list(via) + none) == sorted(others) and len(direct) + len(via) + len(none) == len(others)
            and none == sorted(d for d, _ in ONE_NONE),
        "the recorded selections of the one action (ONE_SELECTIONS: theta, eps, alpha, the mark, J, W_p, the adapter, "
        "iota, the parity, the readout, the instance, the cone point and the datum F) each name a held model function":
            all(f in held and held[f] for _, f, _ in ONE_SELECTIONS) and len(ONE_SELECTIONS) == 13,
    }


def uniqueness(results=None):
    """Each choice on the trunk, and each stepping of an input by the circle, is unique up to symmetry, and so is the
    Standard-Model frame (up to W(E8)); what is left is counted: the recorded selections (the day, the golden clock,
    the datum's orbit, the literal's apex sign, the words' identification) and AIR_801's external integers. With
    results (dots.check_results()), the five frame checks are read from layer 23 instead of being run again."""
    lines = cyclotomic.tick_normalizer()
    galois = cyclotomic.galois_clocks()
    memory = dots.memory_quotients()
    circle = principal.principal_uniqueness()
    classes = _clock_classes()
    c, cp, r, rp, g, w = spine.spine_clock()
    get = (lambda k: results[k]) if results is not None else (lambda k: getattr(dots, k)())
    frame, datum, lit, words, air = (get(k) for k in ("sm_frame", "datum_frame", "literal_chart", "word_frames",
                                                      "air801_classes"))
    chi, marks, d20 = (get(k) for k in ("chiral_closures", "mgm_marks", "mgm_dirac20"))
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
        "the Standard-Model frame is unique up to W(E8) (sm_frame): its 40 triples (T3, Y, Q) in the carrier's A4 are "
        "one S5 x {+-1}-orbit, the 24192 A4 subsystems of E8 are one W(E8)-orbit and the stabilizer of (T3, Y) is "
        "S3 x W(A4'), of order 720, so the 967680 frames are one W(E8)-orbit; its Levi type, 3 + 2 against 4 + 1, is "
        "a recorded selection that carries no number":
            all(frame.values()),
        "the datum's orbit is a recorded selection: the stabilizer of its reading in W(E8) is W(A4) x W(A4') (14400), "
        "acting on the atoms as S5 with five free orbits of 120 on the 600 data of its type (all of energy 34, alike in "
        "every D^2 sector); the canon's is the one with <r, a><r, b> = -1, its representative a frame choice, and W(E8) "
        "leaves 4 Gram classes of the bare root triples, 3 with time reversal":
            all(datum.values()),
        "the literal's apex sign is a recorded selection: the owner's port is the derived commutator in the time clock's "
        "integral chart, one of 480 integral W_p-charts that S5 and the 40 symmetries of W_p make one orbit; the bath's 20 "
        "site symmetries leave two orbits of 240, separated by the apex sign (the pentagram along R^2, not R^3), and "
        "N_source is one of 2652 bases of ker M by K4 matching modes":
            all(lit.values()),
        "the words' identification is a recorded selection: the clocks act on the 15 Coxeter frames as AGL(1, Z/15) "
        "(120 maps), only x -> ax, a = 1, 4, 7, 13, commute with the words' D3, so the canon's 808 -> 0, 086 -> 1, "
        "980 -> 2 is one of 18 classes of 4; the digit flip 6 <-> 9 is conjugate to none of the 120 maps":
            all(words.values()),
        "AIR_801's residue is forced by the day: mod 5 it is one of the 20 GL(2,5)-conjugates of -d, and of the "
        "generators d^k only k = 1, 5 give it; its integers are external (det 12402, discriminant 968473 of narrow class "
        "number 4, one class per genus)":
            all(air.values()),
        "the chiral completion is not a unique derived object (the critique's O6): it needs a mark, one of the twelve "
        "Golden five-cycles over the six order-five subgroups, each with its own zero line (mgm_marks), and a stiffness "
        "alpha that no dot fixes (chiral_closures, symbolic in alpha), and the S5-averaged D20 with five auxiliaries, "
        "nullity 0 and index 0 (mgm_dirac20) is a second completion of the averaged stiffness: the mark and alpha are "
        "recorded selections":
            all(chi.values()) and all(marks.values()) and all(d20.values()),
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
             "5, 4, 60 and 120, so the time clock, the observer clock and the grain are derived. The 27-clock is the seed's "
             "too (1 Nov): the principal points of 3-power order that fix a root are exactly ⟨ρ/27⟩, Galois-dual to E8 > A8 > "
             "A3 + A2 + A1 > A1, so the 27-clock, the vortex (its image on the sun's A8) and the coil (⟨ρ/60⟩ + ⟨ρ/27⟩ = "
             "⟨ρ/540⟩) are derived. Only the miss set (864 = 32 × 27) and the atlas still need the circle, through its 2-part "
             "32 = 2⁵, which no rule of the seed names. |⟨36⟩| = 120 = |G120| only numerically: G120 has no element of order "
             "20 or 120, the seed's group of order 4320 (the decad's stabilizer in C_W(s)) has exponent 120, and W(E8) has no "
             "element of order 36.",
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
             "sun's 80 momenta (243) and at the tick's 24 (250); √251, √(4025/16) and √(6800/27) are at none of them. "
             "All nine are the band's critical values computed from E8's roots, so the torus has a direct THEOREM "
             "join to the seed (1 Nov), and √251 is the hypercharge's: read as torus points Y, Q and T3 are critical "
             "points of orders 6, 3 and 2 with values 251, 243 and 224 (`sm_frame`).",
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
    depth = {d: len(_root(d, DERIVATION)[1]) - 1 for d in DERIVATION}
    lines += ["", "## The deepest dots, one join from the seed (1 Nov)", "",
              "The derivation is a tree of depth 8, but the dots of its last two generations are each joined to E8 "
              "directly by a checked THEOREM map (`deepest_dots`), and so are the deepest of the canon's inputs (the "
              "memory clock by an obstruction). Since the star at the seed (next section) every dot but the product "
              "geometry and FLRW is within two THEOREM joins of the seed.", "", "| dot | depth | its direct join to E8 | check |", "|---|---|---|---|"]
    for d in sorted([d for d, k in depth.items() if k >= 7], key=lambda d: (-depth[d], d)) + list(DEEP_INPUTS):
        for j in dots.JOINS:
            if {j[0], j[1]} == {SEED, d} and j[4] in (T, OB):
                lines.append(f"| {name(d)} | {depth.get(d, 'input')} | {j[2]} ({j[4]}) | `{j[5]}` |")
    others = [d for d in D if d != SEED]
    by_theorem = sum(1 for d in others if any({j[0], j[1]} == {SEED, d} and j[4] == T for j in dots.JOINS))
    lines += ["", "## Every dot one join from the seed (1 Nov)", "",
              f"Each of the other {len(others)} dots has a direct checked join to E8 (`star`): {by_theorem} by THEOREM, the "
              "memory clock by an obstruction, the owner's operand file and the fifteen words by selected references, and the calibration, the "
              "product geometry and FLRW by conditional joins that name the binding still missing. In the THEOREM graph "
              "the seed has eccentricity 2.", "", "| level | dot | its direct join to E8 | status | check |",
              "|---|---|---|---|---|"]
    for lv, _, members in dots.LEVELS:
        for d in members:
            if d == SEED:
                continue
            for j in dots.JOINS:
                if {j[0], j[1]} == {SEED, d}:
                    lines.append(f"| {lv} | {name(d)} | {j[2]} | {j[4]} | `{j[5]}` |")
    lines += ["", "## The one action and the one spectrum (6 Nov)", "",
              "Three dots carry the Lagrangian and the spectral side (`one_model`). The one action, the declared native action "
              "with its port multiplier and the reference completion K_θ = H + θ(ε + J V Jᵀ), is a canon input: a family whose "
              "selections are recorded (θ, ε, α, the mark, the instance, J, Π, ι, the unit of M_s, W_p, the adapter, the "
              "datum F), meeting the source at `act_native`. The one spectrum, the vacuum Hessian 4M_s ⊕ K_θ with its "
              "spectral functionals, is built from the action (`spc_oneloop`: the one loop is the spectral action). The "
              "chiral completion D19 is derived from the carrier (`chiral_closures`, depth 6), and the ten D19 joins sit on "
              "it rather than on the fifteen-dimensional triple. Each of the three has a direct THEOREM join to E8. Every "
              "relation below names its J (cone-J15 = `master_response`'s 15 bond roots; J19 = cone-J15 plus the "
              "auxiliaries e_i + e_6; COMP-J19 = the first 19 channels of `bridge_comparator`'s comparator); its identity "
              "is THEOREM and its selections stay CONDITIONAL or SELECTED_REFERENCE.", "",
              "| id | dot | relation | domain and J | identity | checks | identity status | selection | selection status |",
              "|---|---|---|---|---|---|---|---|---|"]
    cell = lambda x: x.replace("|", "\\|")
    for r in ONE_RELATIONS:
        lines.append(f"| {r.id} | {name(r.dot)} | {cell(r.relation)} | {cell(r.domain)} | {cell(r.identity)} | "
                     + ", ".join(f"`{c}`" for c in r.checks) + f" | {r.identity_status} | {cell(r.selection)} | {r.selection_status} |")
    lines += ["", "The recorded selections (`ONE_SELECTIONS`): " + "; ".join(f"{t} (`{f}`: {w})" for t, f, w in ONE_SELECTIONS)
              + ".", "", "Dots with no held map to the one action or the one spectrum, nor to a dot that has one "
              "(`ONE_NONE`): " + "; ".join(f"{name(d)}: {why}" for d, why in ONE_NONE) + "."]
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
    for name, ok in uniqueness(dots.check_results()).items():
        rep.add(name, T, ok)
    for name, ok in deepest_dots(held).items():
        rep.add(name, T, ok)
    for name, ok in star(held).items():
        rep.add(name, T, ok)
    for name, ok in one_model(held).items():
        rep.add(name, T, ok)
    rep.add("cited: E8 is the unique even unimodular lattice of rank 8; Coxeter elements are conjugate; a transitive "
            "A5 on six points is the icosahedral action on the axes", gates.SELECTED_REFERENCE, True)
    return rep
