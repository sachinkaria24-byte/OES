"""Layer 21. The ledger, unified (28 Oct 2026; canon re-read 18:20 UTC).

Sources read before this layer (Google Drive, folder One Machine 20261028):

* the sibling's full edition, one-machine-20261028-full.typ / .pdf and FULL_UPDATE_20261028 (18:17 UTC),
  with its forty join notes of 17:01-18:17 (TORUS_FIXED, MOON_NINE, PRIMARY_FIXED, TICK_BOUNDS,
  GRAVITY_DOTS, K5_CHAIN, TICK_COSET, ROLE_CLOCK, LEVEL_JOIN, PADA_JOIN, MANTRA_JOIN, SANSKRIT_DOTS,
  SM_TIME, VEDIC_JOIN, CAKRA_JOIN, SMEAR_JOIN, NEST_LOOP, BREATH_TICK, READOUT_JOIN, LIGHT_JOIN,
  ALPHA_JOIN, HUBBLE_JOIN, HEIGHT_JOIN, OAK_TICKS, OSCILLATE_TICKS, ROTOR_JOIN, GOLDEN_TICKS,
  OBSERVER_LOOP, ALL_SUBGROUPS, MIRROR_SOLVE, ENERGY_JOIN, PHASE_JOIN, CHARGE_JOIN, FIELD_JOIN,
  EINSTEIN_JOIN, SLIT_JOIN, OBSERVE_JOIN, OM_JOIN, HORIZON_JOIN, ABOVE_JOIN);
* CANON_READ_20261028 (17:06 UTC), in which the sibling adopts the corrections of layer 20 and notes
  that "the order-24 element inside the Weyl group was not constructed";
* the canon Quick Access workbook, sheet 00_FULL_RECONCILIATION_20261028 (review cutoff 17:19:41 UTC):
  OMSOON736 stays the controlling baseline, no new Matrix ID, every frozen gate retained.

The sibling's ledger has about forty joins. They are of three kinds, and each kind collapses here.

(a) Tick joins. Every sentence "X contains every tick" or "X misses every nonzero tick" is one bit,
    the residue of X mod 5: the tick 864 = 2^5 3^3 lies in <x> iff gcd(x, 4320) divides 864 iff
    5 does not divide x. The 129 such sentences of the ledger are checked against that one line,
    with their step counts and indices. The bit is not additive: 2 and 3 contain the tick, 5 misses it.
(b) Clock joins (rotor, golden subgroup, observer loop, mirrors, above and below). All of them sit in
    one group, the normalizer of the Coxeter clock in W(E8), of order 240:
    - the tick is the commutator of the day and the Coxeter clock, [d, c'] = c'^6 = r r';
    - the day-Coxeter group (order 120) has centre <c'^5> (the shared <720>) and derived group the tick.
      It permutes its five conjugate day clocks as the affine group of the pentagon: the tick rotates
      them and the day doubles them (pentagon to pentagram). This is the sibling's "doubling and
      rotation give 20 affine maps", on the bath;
    - the golden clock v (order 20, twist 11) has v^4 = the tick;
    - the circle's mirror x -> -x is realized by involutions with twist -1. Ten of them keep the carrier
      and act on it as the pentagon reflection, which fixes three atoms;
    - the carrier A4 and its twin A4' are exchanged only by elements of order 4, 8, 12 or 20, never by an
      involution. Every exchange doubles the index-5 glue, and every element keeping them acts by +-1.
(c) Physical names (energy, charge, spin, field, Einstein, double slit, entanglement, Om, karma,
    bubbles, horizon). What the model holds is proved: the energy splits into four conserved pieces
    because D^2 is block diagonal; the vertex and edge sectors never exchange energy, so canonical
    quantization never entangles them; the 240 roots are D8 plus one half-spin orbit, and the 135
    D8 subsystems are the 135 band-top critical points. The rest is not formed, and the reason is stated.

Explicit matrices for the sibling's app are in data/clocks.json (standard coordinates, scaled by 4).
This layer re-reads that file and checks every relation from the file alone.
"""

import itertools
import json
from collections import Counter
from math import gcd
from pathlib import Path

import numpy as np
import sympy as sp

from . import carrier, gates, glue, handover, spine
from .record import Report

N = spine.N
TICK = 864
LEVELS = (0, 864, 1728, 2592, 3456)
E5 = 3456                                   # the CRT idempotent of the 5-part
CLOCKS = Path(__file__).resolve().parent.parent / "data" / "clocks.json"


# ------------------------------------------------------------------ (a) the tick bit

def contains_tick(x):
    """864 lies in <x> (Lemma 1)."""
    return TICK % gcd(x % N, N) == 0


def steps_to_tick(x):
    """Least k >= 1 with k x = 864 mod 4320, or None."""
    return next((k for k in range(1, N + 1) if k * x % N == TICK), None)


def tick_criterion():
    rows = range(N)
    bit = all(contains_tick(a) == (a % 5 != 0) == (a * E5 % N != 0) for a in rows)
    subs = spine.divisors()
    holding = [g for g in subs if contains_tick(g)]
    all_or_none = all({t for t in LEVELS if t % g == 0} in ({0}, set(LEVELS)) for g in subs)
    width = all(TICK % g == 0 for g in subs if g % 5) and \
        sorted(holding) == spine.divisors(TICK) and len(holding) == 24
    twenty = sum(1 for g in subs if contains_tick(g) and (N // g) % 20 == 0)
    return {"bit": bit, "48 subgroups": len(subs) == 48, "24 hold the tick": len(holding) == 24,
            "all five or none": all_or_none, "width x index = 864": width, "16 of order 20k": twenty == 16,
            "not additive": contains_tick(2) and contains_tick(3) and not contains_tick(5)}


# (join, reading, value, claim) with claim True = contains every tick, False = misses every nonzero
# tick, and an optional ("steps", k): k steps of x are one tick, or ("index", k): 864 = k gcd(x, 4320).
TICK_CLAIMS = [
    ("energy", "contrast and edge piece", 12, True, ("steps", 72)),
    ("energy", "constant-mode piece", 20, False, None),
    ("energy", "their sum", 32, True, None),
    ("energy", "cycle piece", 2, True, ("steps", 432)),
    ("energy", "total energy", 34, True, None),
    ("energy", "Tr D^2", 40, False, None),
    ("energy", "Tr D^4", 200, False, None),
    ("energy", "stiffness product", 24, True, ("steps", 36)),
    ("telescopes", "composite weight", 27, True, ("steps", 32)),
    ("golden", "golden step", 216, True, ("steps", 4)),
    ("golden", "entry 21 of B^7", 21, True, None),
    ("golden", "entry 13 of B^7", 13, True, None),
    ("golden", "entry 8 of B^7", 8, True, ("steps", 108)),
    ("golden", "their sum", 55, False, None),
    ("observer loop", "fifteen tithis, the half-turn", 2160, False, None),
    ("observer loop", "fifteen golden steps", 3240, False, None),
    ("observer loop", "fifteen times the index of frequency 8", 1620, False, None),
    ("observer loop", "the five zero modes", 5, False, None),
    ("mirrors", "fifth golden step", 1080, False, None),
    ("mirrors", "tick level", 1728, True, None),
    ("mirrors", "tick level", 2592, True, None),
    ("mirrors", "tick level", 3456, True, None),
    ("W0 reverse", "reduced W0, the sun", 1440, False, None),
    ("W0 reverse", "its reverse", 2880, False, None),
    ("phase", "source frequency", 2, True, ("steps", 432)),
    ("phase", "stiffness 3", 3, True, ("steps", 288)),
    ("phase", "stiffness 8", 8, True, ("steps", 108)),
    ("phase", "branch-wave energy", 10, False, None),
    ("phase", "weight", 98, True, None),
    ("phase", "weight", 62, True, None),
    ("phase", "weight", 113, True, None),
    ("phase", "weight", 101, True, None),
    ("phase", "weight", 118, True, None),
    ("phase", "first two weights, the nakshatra", 160, False, None),
    ("phase", "all five weights", 492, True, None),
    ("phase", "phase count", 2740, False, None),
    ("phase", "phase count less 20", 2720, False, None),
    ("phase", "CKM numerator", 3443, True, None),
    ("phase", "CKM denominator residue", 960, False, None),
    ("charge", "ledger charge", 30, False, None),
    ("charge", "norm numerator", 5, False, None),
    ("charge", "norm denominator", 6, True, ("steps", 144)),
    ("charge", "bookkeeping charge", 2, True, None),
    ("charge", "stiffness 4", 4, True, ("steps", 216)),
    ("charge", "relation trace", 24, True, ("steps", 36)),
    ("charge", "square-trace", 84, True, None),
    ("spin", "integer roots", 112, True, None),
    ("spin", "half-integer roots", 128, True, None),
    ("heat", "heat factor (reduces to 360)", 9000, False, None),
    ("monopole", "discriminant", 120, False, None),
    ("monopole", "monopole coefficient", 60, False, None),
    ("monopole", "charge", 30, False, None),
    ("monopole", "dipole", 10, False, None),
    ("monopole", "sphere factor", 2, True, None),
    ("monopole", "tail 14400 (the sun)", 14400, False, None),
    ("field", "Cayley scale", 5, False, None),
    ("Einstein line", "Einstein-Hilbert power", 4, True, ("steps", 216)),
    ("Einstein line", "vacuum power", 6, True, ("steps", 144)),
    ("Einstein line", "their sum", 10, False, None),
    ("two 36s", "piece", 15, False, None),
    ("two 36s", "two pieces", 30, False, None),
    ("two 36s", "piece", 6, True, None),
    ("two 36s", "the atlas", 36, True, ("steps", 24)),
    ("two 36s", "piece", 21, True, None),
    ("two 36s", "unused half", 18, True, ("steps", 48)),
    ("sign tensor", "each half", 10, False, None),
    ("sign tensor", "all twenty products", 20, False, None),
    ("sign tensor", "count", 16, True, None),
    ("sign tensor", "combined count", 36, True, None),
    ("observer", "free modes", 5, False, None),
    ("observer", "stiffness-3 modes", 8, True, None),
    ("observer", "stiffness-8 modes", 2, True, None),
    ("Om", "the cut", 736, True, None),
    ("Om", "the determinant", 155, False, None),
    ("karma", "Karma's stage", 8, True, ("steps", 108)),
    ("japa", "Japa's stage", 10, False, None),
    ("mantra", "Mantra's stage", 11, True, None),
    ("bubbles", "bubble width", 6, True, ("steps", 144)),
    ("horizon", "horizon count", 192, True, ("steps", 27)),
    ("above and below", "Matrka 0", 0, False, None),
    ("above and below", "Pratyabhijna 14", 14, True, None),
    ("above and below", "Jnana 4", 4, True, None),
    ("above and below", "Japa 10", 10, False, None),
    ("above and below", "Nyasa 5", 5, False, None),
    ("above and below", "Samskara 9", 9, True, None),
    ("above and below", "Malini 1", 1, True, None),
    ("above and below", "stage 13", 13, True, None),
    ("above and below", "stage 2", 2, True, None),
    ("above and below", "stage 12", 12, True, None),
    ("above and below", "stage 3", 3, True, None),
    ("above and below", "stage 11", 11, True, None),
    ("above and below", "Kriya 6", 6, True, None),
    ("above and below", "Karma 8", 8, True, None),
    ("above and below", "upper wing", 21, True, None),
    ("above and below", "lower wing", 77, True, None),
    ("above and below", "wings and middle", 105, False, None),
    ("tick bounds", "collar top", 224, True, ("index", 27)),
    ("tick bounds", "band edge", 256, True, ("index", 27)),
    ("tick bounds", "level 243", 243, True, ("index", 32)),
    ("tick bounds", "level 248", 248, True, ("index", 108)),
    ("tick bounds", "bath energy 252", 252, True, ("index", 24)),
    ("tick bounds", "level 250", 250, False, None),
    ("gravity dots", "count", 9, True, ("steps", 96)),
    ("gravity dots", "carrier count", 15, False, None),
    ("gravity dots", "carrier count", 40, False, None),
    ("gravity dots", "carrier count", 200, False, None),
    ("K5 chain", "fourth copy start", 18, True, ("steps", 48)),
    ("levels", "width", 1, True, ("steps", 864)),
    ("levels", "width", 7, True, None),
    ("levels", "present", 6, True, ("steps", 144)),
    ("levels", "difference", 12, True, ("steps", 72)),
    ("pada", "pada step", 40, False, None),
    ("SM time", "mixing numerator", 9, True, None),
    ("SM time", "denominator", 640, False, None),
    ("SM time", "denominator", 1280, False, None),
    ("SM time", "6400 (reduces to 2080)", 6400, False, None),
    ("cakra", "crop piece", 28, True, ("index", 216)),
    ("cakra", "crop piece", 92, True, ("index", 216)),
    ("smear", "element", 184, True, None),
    ("smear", "element", 481, True, None),
    ("readout", "flash, the day step", 180, False, None),
    ("alpha", "count", 137, True, None),
    ("alpha", "ten counts", 1370, False, None),
    ("Hubble", "step", 20, False, None),
    ("height", "count", 96, True, ("steps", 9)),
    ("height", "count", 768, True, None),
    ("height", "loop count", 232, True, None),
    ("height", "vacuum count", 280, False, None),
    ("height", "tissue total", 774, True, None),
]

# (value, claimed order of <value>) from the same joins
ORDER_CLAIMS = [(30, 144), (112, 270), (128, 135), (15, 288), (18, 240), (10, 432), (20, 216), (1370, 432),
                (3240, 4), (105, 288), (960, 9), (640, 27), (1280, 27), (28, 1080), (92, 1080), (774, 240),
                (96, 45), (768, 45), (9000, 12), (24, 180), (2, 2160), (12, 360), (32, 135), (40, 108),
                (200, 108), (2880, 3), (2740, 216), (2720, 27), (34, 2160), (21, 1440), (224, 135),
                (256, 135), (2080, 27), (36, 120), (120, 36), (216, 20), (1080, 4), (2160, 2)]


def check_claims():
    bad, seen = [], Counter()
    for join, reading, x, claim, extra in TICK_CLAIMS:
        seen[join] += 1
        ok = contains_tick(x) == claim == (x % 5 != 0)
        if extra:
            kind, k = extra
            ok &= (steps_to_tick(x) == k) if kind == "steps" else (TICK == k * gcd(x % N, N))
        if not ok:
            bad.append((join, reading, x))
    orders_ok = all(spine.order(x) == o for x, o in ORDER_CLAIMS)
    return bad, orders_ok, seen


# ---------------------------------------------------------------- (b) the clock joins

def closure(gens):
    I8 = spine.I8
    seen = {I8.tobytes(): I8}
    frontier = [I8]
    while frontier:
        new = []
        for M in frontier:
            for s in gens:
                P = M @ s
                k = P.tobytes()
                if k not in seen:
                    seen[k] = P
                    new.append(P)
        frontier = new
    return list(seen.values())


def day_coxeter_group():
    _, cp, _, _, g, _ = spine.spine_clock()
    d = spine.day_clock()
    mp, inv = spine.mpow, spine.inverse
    G = closure([cp, d])
    centre = [z for z in G if np.array_equal(z @ cp, cp @ z) and np.array_equal(z @ d, d @ z)]
    comms = {}
    for x in G:
        for y in (cp, d):
            k = x @ y @ inv(x) @ inv(y)
            comms[k.tobytes()] = k
    derived = closure(list(comms.values()))
    powers = lambda M, n: [mp(M, k) for k in range(n)]
    same = lambda H, K: {M.tobytes() for M in H} == {M.tobytes() for M in K}
    # the five conjugate day clocks, and how the tick and the day permute them
    D = closure([d])
    key = lambda H: frozenset(M.tobytes() for M in H)
    lines = {}
    for x in G:
        H = [x @ y @ inv(x) for y in D]
        lines.setdefault(key(H), H)
    names = list(lines)
    perm = lambda x: [names.index(key([x @ y @ inv(x) for y in lines[L]])) for L in names]
    base = names.index(key(D))
    label, cur, pt = {}, base, perm(mp(cp, 6))
    for k in range(5):
        label[cur] = k
        cur = pt[cur]
    pd, pz = perm(d), perm(mp(cp, 5))
    tick_day = d @ g @ inv(d) @ inv(g)
    nonabelian = not any(np.array_equal(tick_day, z) for z in centre)
    affine = {"tick": {label[i]: label[pt[i]] for i in range(5)},
              "day": {label[i]: label[pd[i]] for i in range(5)},
              "centre": {label[i]: label[pz[i]] for i in range(5)}}
    return {
        "[d, c'] = c'^6 = r r'": np.array_equal(d @ cp @ inv(d) @ inv(cp), mp(cp, 6))
        and np.array_equal(mp(cp, 6), g),
        "d (r r') d^-1 = (r r')^2": np.array_equal(d @ g @ inv(d), g @ g),
        "|G| = 120": len(G) == 120,
        "centre <c'^5>, order 6": same(centre, powers(mp(cp, 5), 6)),
        "derived group = the tick": same(derived, powers(mp(cp, 6), 5)),
        "abelianization cyclic of order 24, generated by d": len(G) // len(derived) == 24
        and not any(any(np.array_equal(mp(d, k), t) for t in derived) for k in range(1, 24)),
        "five day clocks": len(names) == 5,
        "tick rotates them": affine["tick"] == {x: (x + 1) % 5 for x in range(5)},
        "day doubles them": affine["day"] == {x: 2 * x % 5 for x in range(5)},
        "centre fixes them": affine["centre"] == {x: x for x in range(5)},
        "G / centre is not abelian (the affine 20, not a cyclic 20)": nonabelian,
    }, affine


def golden_clock():
    _, cp, _, _, g, _ = spine.spine_clock()
    mp = spine.mpow
    N_ = spine.normalizer()
    o20 = [(m, w) for m, w in N_ if spine.mat_order(w) == 20]
    v = next(w for m, w in o20 if np.array_equal(mp(w, 2), mp(cp, 3)))
    B = sp.Matrix([[1, 1], [1, 0]])
    mod5 = lambda M: M.applyfunc(lambda e: e % 5)
    Bk = [mod5(B ** k) for k in range(21)]
    order_B = next(k for k in range(1, 21) if Bk[k] == sp.eye(2))
    U = Bk[4]
    return {
        "24 elements of order 20, all twist 11": len(o20) == 24 and {m for m, _ in o20} == {11},
        "v^4 = c'^6 = r r'": np.array_equal(mp(v, 4), g),
        "B = [[1,1],[1,0]] has order 20 mod 5": order_B == 20,
        "B^4 is unipotent of order 5 mod 5": U != sp.eye(2) and mod5((U - sp.eye(2)) ** 2) == sp.zeros(2, 2),
        "<216> has order 20 and 4 x 216 = 864": spine.order(216) == 20 and 4 * 216 == TICK,
    }, v


def carrier_symmetry_checks():
    """The graph reflection keeps D^2; the fifteen-atom involution i -> 14 - i does not."""
    K = carrier.D2()
    E = carrier.edges()
    refl = [(-i) % 5 for i in range(5)]
    P = sp.zeros(15, 15)
    for i in range(5):
        P[refl[i], i] = 1
    fixed = sum(1 for i in range(5) if refl[i] == i)
    for k, (i, j) in enumerate(E):
        img = tuple(sorted((refl[i], refl[j])))
        P[5 + E.index(img), 5 + k] = 1
        fixed += img == (i, j)
    S = sp.zeros(15, 15)
    for i in range(15):
        S[14 - i, i] = 1
    return {"graph reflection keeps D^2": P * K == K * P, "it fixes three atoms": fixed == 3,
            "the 15-atom involution does not keep D^2": S * K != K * S,
            "it fixes one atom and has eigenspaces 8 + 7": sum(S[i, i] for i in range(15)) == 1
            and S.eigenvals() == {1: 8, -1: 7}}


def mirrors():
    _, cp, _, _, g, _ = spine.spine_clock()
    _, A, Ap = glue.a4_pair()
    PA = glue.projector(A)
    N_ = spine.normalizer()
    inv = spine.inverse
    tw = [w for m, w in N_ if m == 29]
    keep = [w for w in tw if spine.mat_order(w) == 2
            and np.allclose(spine.to_standard(w) @ PA @ spine.to_standard(w).T, PA)]
    Z = np.eye(5) - np.ones((5, 5)) / 5
    refl = [np.eye(5)[[(s - i) % 5 for i in range(5)]].T @ Z for s in range(5)]
    acts = Counter()
    for w in keep:
        B = spine.to_standard(w)[:5, :5] @ Z
        acts["reflection" if any(np.allclose(B, P) for P in refl) else
             "minus a reflection" if any(np.allclose(B, -P) for P in refl) else "other"] += 1
    circle = [x for x in range(N) if (-x) % N == x]
    return {
        "30 elements with twist -1": len(tw) == 30,
        "each inverts the clock and the tick": all(np.array_equal(w @ cp @ inv(w), inv(cp))
                                                    and np.array_equal(w @ g @ inv(w), inv(g)) for w in tw),
        "10 involutions keep the carrier": len(keep) == 10,
        "on the carrier: pentagon reflections (5) and their negatives (5)":
            acts == Counter({"reflection": 5, "minus a reflection": 5}),
        "on the circle x -> -x fixes 0 and 2160 only": circle == [0, 2160],
        "it swaps 864 <-> 3456 and 1728 <-> 2592": (-864) % N == 3456 and (-1728) % N == 2592,
        "it swaps the golden steps 1080 <-> 3240": (-1080) % N == 3240,
    }, acts


def carrier_exchange():
    """The stabilizer of the pair {A4, A4'} in Aut(E8) = W(E8), and its action on the glue Z/5."""
    R, A, Ap = glue.a4_pair()
    PA, PAp = glue.projector(A), glue.projector(Ap)
    SA = np.array([np.eye(8)[i] - np.eye(8)[i + 1] for i in range(4)]).T
    SAp = np.array(glue.chain_order(glue.simple_system(Ap))).T
    iota, iota_inv = SAp @ np.linalg.pinv(SA), SA @ np.linalg.pinv(SAp)
    auts = []
    for p in itertools.permutations(range(5)):
        P = np.zeros((8, 8))
        for i in range(5):
            P[p[i], i] = 1
        auts += [s * P @ PA for s in (1, -1)]
    K = np.array([1, 7, 49, 343, 2401, 16807, 117649, 823543], float)
    key = lambda X: 2 * X @ K
    rkeys = np.sort(np.round(key(R)).astype(np.int64))
    rset = {tuple(t) for t in np.round(2 * R).astype(int)}
    RA, RAp = R @ PA, R @ PAp

    def stab(left, right):
        found = []
        UL = [key(RA @ (left(a)).T) for a in auts]
        UR = [key(RAp @ (right(b)).T) for b in auts]
        URm = np.array(UR)
        for ia, ua in enumerate(UL):
            S = URm + ua
            Sr = np.round(S)
            okm = np.all(np.isclose(S, Sr, atol=1e-6), axis=1)
            idx = np.searchsorted(rkeys, Sr.astype(np.int64))
            idx = np.clip(idx, 0, len(rkeys) - 1)
            okm &= np.all(rkeys[idx] == Sr.astype(np.int64), axis=1)
            for ib in np.nonzero(okm)[0]:
                M = left(auts[ia]) + right(auts[ib])
                Y = 2 * R @ M.T
                if np.allclose(Y, np.round(Y)) and all(t in rset for t in map(tuple, np.round(Y).astype(int))):
                    found.append(M)
        return found

    keeps = stab(lambda a: a, lambda b: iota @ b @ iota_inv)
    swaps = stab(lambda a: iota @ a, lambda b: b @ iota_inv)
    keeps = [M for M in keeps if np.allclose(M.T @ M, np.eye(8))]
    swaps = [M for M in swaps if np.allclose(M.T @ M, np.eye(8))]

    def orders(Ms):
        X = np.array(Ms)
        P = X.copy()
        out = np.zeros(len(Ms), int)
        for k in range(1, 61):
            done = (out == 0) & np.all(np.isclose(P, np.eye(8)), axis=(1, 2))
            out[done] = k
            P = P @ X
        return Counter(out.tolist())

    glue_roots = [x for x in R if not np.allclose(PA @ x, x) and not np.allclose(PAp @ x, x)]

    def gclass(x):
        y = (PA @ x)[:5]
        z = y + (-y[0]) % 1.0
        return int(round(z.sum())) % 5

    gam = glue_roots[0]
    k0 = gclass(gam)
    mult = lambda M: next(m for m in range(1, 5) if m * k0 % 5 == gclass(M @ gam))
    return {
        "keep": len(keeps), "exchange": len(swaps),
        "exchange orders": dict(sorted(orders(swaps).items())),
        "keep acts on the glue by": dict(Counter(mult(M) for M in keeps)),
        "exchange acts on the glue by": dict(Counter(mult(M) for M in swaps)),
        "glue classes of the 200 mixed roots": dict(sorted(Counter(gclass(x) for x in glue_roots).items())),
        "involutive exchange": any(np.allclose(M @ M, np.eye(8)) for M in swaps),
    }


# ------------------------------------------------------------------ clock matrices

def clock_matrices():
    """Explicit elements of W(E8) in standard coordinates, scaled by 4 (integers)."""
    _, cp, r, rp, g, _ = spine.spine_clock()
    d = spine.day_clock()
    _, v = golden_clock()
    _, A, _ = glue.a4_pair()
    PA = glue.projector(A)
    m = next(w for mm, w in spine.normalizer() if mm == 29 and spine.mat_order(w) == 2 and np.allclose(
        spine.to_standard(w)[:5, :5] @ (np.eye(5) - 1 / 5),
        np.eye(5)[[(-i) % 5 for i in range(5)]].T @ (np.eye(5) - 1 / 5))
        and np.allclose(spine.to_standard(w) @ PA @ spine.to_standard(w).T, PA))
    four = lambda M: np.round(4 * spine.to_standard(M)).astype(int).tolist()
    return {"coordinates": "standard E8 coordinates of oes/spine.py (Bourbaki simple roots); "
                           "every matrix is 4 times an element of W(E8)",
            "scale": 4,
            "coxeter": four(cp), "tick": four(g), "carrier_rotation": four(r), "twin_rotation": four(rp),
            "day": four(d), "golden": four(v), "mirror": four(m),
            "relations": ["coxeter^30 = I, coxeter^15 = -I", "tick = coxeter^6 = carrier_rotation twin_rotation",
                          "day^24 = I, day^4 = coxeter^5, day coxeter day^-1 = coxeter^7",
                          "day coxeter day^-1 coxeter^-1 = tick", "golden^20 = I, golden^4 = tick",
                          "golden coxeter golden^-1 = coxeter^11", "mirror^2 = I, mirror coxeter mirror = coxeter^-1",
                          "mirror restricted to coordinates 0..4 is the pentagon reflection i -> -i"]}


def check_clock_file(path=CLOCKS):
    """Re-read data/clocks.json and check every relation from the file alone."""
    data = json.loads(Path(path).read_text())
    s = data["scale"]
    M = {k: np.array(data[k], dtype=np.int64) for k in
         ("coxeter", "tick", "carrier_rotation", "twin_rotation", "day", "golden", "mirror")}
    I = s * np.eye(8, dtype=np.int64)

    def mul(X, Y):
        P = X @ Y
        if np.any(P % s):
            raise ValueError("entry outside Z/4")
        return P // s

    def pw(X, k):
        P = I.copy()
        for _ in range(k):
            P = mul(P, X)
        return P

    inv = lambda X: X.T                          # orthogonal: inverse = transpose (scaled consistently)
    R2 = np.round(2 * handover.e8_roots()).astype(np.int64)
    rset = {tuple(r) for r in R2}
    weyl = lambda X: all(tuple((X @ r) // s) in rset and not np.any((X @ r) % s) for r in R2)
    c, t, d, v, m = M["coxeter"], M["tick"], M["day"], M["golden"], M["mirror"]
    Z = np.eye(5) - np.ones((5, 5)) / 5
    return {
        "all seven preserve the 240 roots": all(weyl(X) for X in M.values()),
        "coxeter: order 30, coxeter^15 = -I": np.array_equal(pw(c, 30), I) and np.array_equal(pw(c, 15), -I)
        and not np.array_equal(pw(c, 10), I) and not np.array_equal(pw(c, 6), I),
        "tick = coxeter^6 = r r'": np.array_equal(pw(c, 6), t)
        and np.array_equal(mul(M["carrier_rotation"], M["twin_rotation"]), t),
        "day: order 24, day^4 = coxeter^5, twist 7": np.array_equal(pw(d, 24), I) and not np.array_equal(pw(d, 12), I)
        and not np.array_equal(pw(d, 8), I) and np.array_equal(pw(d, 4), pw(c, 5))
        and np.array_equal(mul(mul(d, c), inv(d)), pw(c, 7)),
        "[day, coxeter] = tick": np.array_equal(mul(mul(mul(d, c), inv(d)), inv(c)), t),
        "golden: order 20, golden^4 = tick, twist 11": np.array_equal(pw(v, 20), I)
        and not np.array_equal(pw(v, 10), I) and not np.array_equal(pw(v, 4), I)
        and np.array_equal(pw(v, 4), t) and np.array_equal(mul(mul(v, c), inv(v)), pw(c, 11)),
        "mirror: involution inverting the clock": np.array_equal(mul(m, m), I)
        and np.array_equal(mul(mul(m, c), m), inv(c)),
        "mirror on the carrier is the pentagon reflection": np.allclose(
            (m[:5, :5] / s) @ Z, np.eye(5)[[(-i) % 5 for i in range(5)]].T @ Z),
    }


# ------------------------------------------------------------------ (c) physical names

def energy_sectors():
    """The checked datum: quadratic form 64 = 40 + 6 + 18, energy 34 = 20 + (3 + 9) + 2; E_V and E_E conserved."""
    L = carrier.CarrierLagrangian()
    psi0, v0 = carrier.canon_initial_datum()
    K = np.array(carrier.D2(), float)
    block = np.allclose(K[:5, 5:], 0) and np.allclose(K[5:, :5], 0)
    q = psi0 @ K @ psi0
    u = np.ones(5) / np.sqrt(5)
    x, y = psi0[:5], psi0[5:]
    xu = (x @ u) * u
    xc = x - xu
    pieces = {"uniform": 0.5 * xu @ K[:5, :5] @ xu, "vertex contrast": 0.5 * xc @ K[:5, :5] @ xc,
              "edge image": 0.5 * y @ K[5:, 5:] @ y, "cycle": 0.5 * v0 @ v0}
    EV = lambda p, w: 0.5 * w[:5] @ w[:5] + 0.5 * p[:5] @ K[:5, :5] @ p[:5]
    EE = lambda p, w: 0.5 * w[5:] @ w[5:] + 0.5 * p[5:] @ K[5:, 5:] @ p[5:]
    times = [0.0, 0.37, 1.9, 5.3, 11.7]
    traj = [L.solve(psi0, v0, t) for t in times]
    conserved = all(abs(EV(p, w) - 23) < 1e-9 and abs(EE(p, w) - 11) < 1e-9 for p, w in traj)
    sectors = L.sector_energies(psi0, v0)
    return {
        "D^2 is block diagonal (vertices | edges)": block,
        "quadratic form 64 = 40 + 6 + 18": bool(round(q) == 64 and np.isclose(2 * pieces["uniform"], 40)
                                                and np.isclose(2 * pieces["vertex contrast"], 6)
                                                and np.isclose(2 * pieces["edge image"], 18)),
        "energy 34 = 20 + (3 + 9) + 2": bool(np.isclose(L.energy(psi0, v0), 34) and np.allclose(
            [pieces[k] for k in ("uniform", "vertex contrast", "edge image", "cycle")], [20, 3, 9, 2])),
        "sectors 0, 3, 8 carry 2, 12, 20": bool(np.allclose([sectors[0], sectors[3], sectors[8]], [2, 12, 20])),
        "E_V = 23 and E_E = 11 along the motion": conserved,
    }


def spin_structure():
    R = handover.e8_roots()
    integer = [r for r in R if np.allclose(r, np.round(r))]
    half = [r for r in R if not np.allclose(r, np.round(r))]
    I2 = {tuple(np.round(2 * r).astype(int)) for r in integer}
    refl = lambda a, b: b - (a @ b) * a
    d8_closed = all(tuple(np.round(2 * refl(a, b)).astype(int)) in I2 for a in integer for b in integer)
    S = [np.eye(8)[i] - np.eye(8)[i + 1] for i in range(7)] + [np.eye(8)[6] + np.eye(8)[7]]
    orbit = {tuple(np.round(2 * half[0]).astype(int))}
    frontier = [half[0]]
    while frontier:
        new = []
        for x in frontier:
            for a in S:
                y = refl(a, x)
                k = tuple(np.round(2 * y).astype(int))
                if k not in orbit:
                    orbit.add(k)
                    new.append(y)
        frontier = new
    wd8 = 2 ** 7 * int(sp.factorial(8))
    census = {typ: f["orbit"] for (_, typ), f in handover.critical_census().items()}
    return {
        "112 integer roots, closed under their reflections (D8)": len(integer) == 112 == 2 * 8 * 7 and d8_closed,
        "the 128 half-integer roots are one W(D8) orbit (a half-spin weight set)": len(half) == 128
        and len(orbit) == 128,
        "so(16) + 128 = 120 + 128 = 248 = 8 + 240": 8 + 112 + 128 == 248 == 8 + 240,
        "[W(E8) : W(D8)] = 135 = the band-top D8 family of the critical census":
            handover.WE8 // wd8 == 135 == census.get("D8"),
        "half-turn fixed momenta 256 = 1 + 120 (E7+A1) + 135 (D8)":
            1 + census.get("E7+A1", 0) + census.get("D8", 0) == 256 == 2 ** 8,
    }


def tick_arithmetic():
    return {
        "12 + 24 = 36 and 6 + 15 + 15 = 21 + 15 = 36, not 18 + 18": 6 + 15 + 15 == 21 + 15 == 36 != 0,
        "21 + 7 + 77 = 105, wings 0..6 and 8..14": sum(range(7)) == 21 and sum(range(8, 15)) == 77,
        "98 + 62 = 160 and the weights sum to 492 = 41 x 12": 98 + 62 == 160 and 98 + 62 + 113 + 101 + 118 == 492 == 41 * 12,
        "30 / 36 = 5 / 6 and 3 x 4 + 2 x 9 = 30": sp.Rational(30, 36) == sp.Rational(5, 6) and 3 * 4 + 2 * 9 == 30,
        "250 x 4320 = 9000 x 120 = 1080000": 250 * N == 9000 * 120 == 1080000,
        "432 x 2 = 288 x 3 = 108 x 8 = 216 x 4 = 144 x 6 = 864": 432 * 2 == 288 * 3 == 108 * 8 == 216 * 4 == 144 * 6 == TICK,
        "4 x 180 + 144 = 864 and 15 x 144 = 10 x 216 = 2160": 4 * 180 + 144 == TICK and 15 * 144 == 10 * 216 == 2160,
        "1080 + 3240 = 4320, and 27 x 192 = 5184 = 864 mod 4320": 1080 + 3240 == N and 27 * 192 % N == TICK,
        "monopole chain <120> < <60> < <30> < <10>": spine.contains(60, 120) and spine.contains(30, 60)
        and spine.contains(10, 30) and [spine.order(x) for x in (120, 60, 30, 10)] == [36, 72, 144, 432],
        "the five tick levels are 0, 24, 48, 72, 96 atlases": [t // 36 for t in LEVELS] == [0, 24, 48, 72, 96],
        "1296, 432 and 2160 share the coset 432; the sun lies in 576": 1296 % TICK == 432 % TICK == 2160 % TICK == 432
        and 1440 % TICK == 576,
    }


def four_cube_laplacian():
    """SMEAR_JOIN: the 81-cell 4-cube complex has Laplacian spectrum 0, 2, 4, 6, 8 with 1, 8, 24, 32, 16."""
    d0 = sp.Matrix([[-1, 1]])                       # interval: coboundary vertices -> edge
    Lv = d0.T * d0                                   # vertices
    Le = d0 * d0.T                                   # edge
    one = [*Lv.eigenvals().items(), *Le.eigenvals().items()]
    vals = Counter()
    for combo in itertools.product(one, repeat=4):
        lam = sum(v for v, _ in combo)
        mult = 1
        for _, m in combo:
            mult *= m
        vals[lam] += mult
    return dict(sorted(vals.items())), sum(v * m for v, m in vals.items())


# ------------------------------------------------------------------ the unified ledger

JOINS = [
    ("circle lemma", "dozens of circle statements, one at a time", "one lemma: the subgroups are the divisors; meets and joins are lcm and gcd", "THEOREM", "19"),
    ("tower", "36 x 12 x 2 x 5", "36 x 4 x 3 x 2 x 5 through the Coxeter subgroup <144>", "THEOREM", "19"),
    ("Coxeter clock", "the Coxeter number 30 cuts 4320 into 144", "the step 144 acts as a Coxeter element c' of W(E8): order 30, Phi_30, exponents = units mod 30", "SELECTED_REFERENCE", "19"),
    ("fixed momenta", "25, 81, 256 determinants", "|det(c^k - I)| = Phi_n(1)^(8/phi(n)); the Morse points of A4+A4, E6+A2, E7+A1 and D8", "THEOREM", "19, 20"),
    ("what acts on the bath", "the stops at the atlas, moon, nakshatra and pada", "a subgroup acts iff its order is 1-6, 8-10, 12, 15, 18, 20, 24 or 30", "THEOREM", "19"),
    ("harmonic quartic", "3|p|^4 - 7 sum p^4 and 2 s2^2 - 5 s4", "ambient and contrast-plane Laplacians; both recorded", "THEOREM", "1, 20"),
    ("group speed", "maximum group speed exactly sqrt 30", "a supremum, never attained: |grad eps|^2 <= 120 eps", "THEOREM", "20"),
    ("tick joins (all rows)", "X contains / misses every nonzero tick", "one bit: 5 does not divide X", "THEOREM", "21: tick bit"),
    ("oscillating tick", "24 of 48 subgroups hold all five levels; doubling and rotation do not commute",
     "24 = the divisors of 864; the doubling is the day on its five conjugates", "THEOREM", "21: tick bit, five day clocks"),
    ("telescopes", "weight 27 contains every tick; 32 x 27 = 864", "5 does not divide 27", "ARITHMETIC", "21: claims"),
    ("rotor", "six Coxeter steps are one tick", "c'^6 = r r', two carrier rotations; [d, c'] = c'^6", "THEOREM", "19, 21"),
    ("golden subgroup", "20 elements, every fourth a tick", "<216> on the circle, v with v^4 = r r' on the bath, B mod 5 with B^4 unipotent", "THEOREM", "21: golden"),
    ("observer loop", "15 tithis = 10 golden steps; neither a tick", "2160 is the half-turn -I; 5 divides 2160 and 3240", "ARITHMETIC", "21: claims"),
    ("observer", "installed observer D on 15 atoms", "five channels complete it: R H = I15, P0 = I - 11K/24 + K^2/24", "THEOREM", "5, 20"),
    ("mirrors", "negation pairs the tick levels; graph reflection keeps the stiffness", "twist -1 involutions; on the carrier the pentagon reflection (three atoms)", "THEOREM", "21: mirrors"),
    ("energy split", "34 = 12 + 20 + 2", "34 = 20 + (3 + 9) + 2; E_V = 23 and E_E = 11 conserved", "THEOREM", "1, 21: energy"),
    ("W0 reverse", "-1440 = 2880 generates the sun", "x -> -x is the mirror; the sun c'^10 is inverted by it", "THEOREM", "21: mirrors"),
    ("phase weights", "98, 62, 113, 101, 118 contain; 160 misses", "none divisible by 5; 160 is", "ARITHMETIC", "21: claims"),
    ("charge", "30 / 36 = 5 / 6", "5 divides 30; the norm is a ratio of counts, not 1/137", "ARITHMETIC", "21: claims"),
    ("monopole chain", "<120> < <60> < <30> < <10>, none holds a tick", "all multiples of 5", "ARITHMETIC", "21: claims"),
    ("spin counts", "128 inside the subgroup of 112", "240 = D8 (112) + one half-spin orbit (128); 135 D8 subsystems", "THEOREM", "21: spin"),
    ("heat", "250 x 4320 circles", "a count", "ARITHMETIC", "21: claims"),
    ("field", "psi'' + D^2 psi = 0 and q'' + 4 q = 0", "4 is not in spec D^2 = {0, 3, 8}: the source is not a carrier mode", "OBSTRUCTION", "21: field"),
    ("Einstein line", "216 x 4 = 144 x 6 = 864", "a count; Einstein-Hilbert not formed", "ARITHMETIC", "21: claims"),
    ("two 36s", "6 + 15 + 15 and 21 + 15, not 18 + 18", "a count; no interference amplitude", "ARITHMETIC", "21: claims"),
    ("sign tensor", "20 products split 10 + 10", "a count; canonical quantization never entangles V and E", "CONDITIONAL", "21: decoupling"),
    ("Om", "736 contains, 155 misses", "5 divides 155 = 5 x 31", "ARITHMETIC", "21: claims"),
    ("karma, japa, mantra", "108 x 8 = 864; 10 misses; 11 generates", "the bit", "ARITHMETIC", "21: claims"),
    ("bubbles and horizon", "144 x 6 = 864; 27 x 192 = 864", "the bit", "ARITHMETIC", "21: claims"),
    ("above and below", "the stage reflection does not keep the tick; wings 21 and 77", "no involution exchanges the carrier and its twin; every exchange doubles the glue", "THEOREM", "21: exchange"),
    ("day and Coxeter clocks", "the circle makes them commute; an extension of order 120", "on the bath the order-120 group is built; its derived group is the tick", "THEOREM", "19, 20, 21"),
    ("order-24 element", "not constructed in the sibling build", "d in data/clocks.json, checked from the file", "THEOREM", "21: clock file"),
    ("not stored", "source infinity, foam, double slit, entanglement, photoelectric, electron, photon, proton, Compton, Bohr, a work function, a Bell count, 19 SM parameters",
     "no operand and no dimensionful constant", "UNFORMED", "21"),
]


def ledger_markdown():
    lines = ["# The unified ledger", "",
             "Every join of the sibling's 28 October ledger (FULL_UPDATE_20261028, 18:17 UTC), what this "
             "repository proves about it, and where. Generated by `oes/ledger.py` (`ledger_markdown()`); "
             "`tests/test_model.py` checks that this file is current.", "",
             "| join | the sibling's statement | unified statement | status | layer |",
             "|---|---|---|---|---|"]
    cell = lambda x: x.replace("|", "\\|")
    for row in JOINS:
        lines.append("| " + " | ".join(cell(x) for x in row) + " |")
    lines += ["", "AUTH = NOT_PASS. ScientificGold = FALSE. No term is added to the action.", ""]
    return "\n".join(lines)


# ----------------------------------------------------------------------------- run

def run():
    rep = Report("21-ledger")
    T, AR, OB, CD, UF, RP = (gates.THEOREM, gates.ARITHMETIC, gates.OBSTRUCTION, gates.CONDITIONAL,
                             gates.UNFORMED, gates.REPORTED)

    rep.add("canon re-read 18:20 UTC: Quick Access 00_FULL_RECONCILIATION_20261028 (review cutoff 17:19:41) keeps "
            "OMSOON736 controlling, no new Matrix ID, every frozen gate retained; it still lists the 14:37 "
            "build of this repository as the latest One Machine status", RP, True)
    rep.add("the sibling's CANON_READ (17:06) adopts layer 20: '360000 is not a step' removed, both harmonic "
            "quartics named with their Laplacians, 5 and 25 dual to the tick, fixed determinants 25/81/256, the "
            "order-120 extension. It notes the order-24 element was not constructed; it is constructed here", RP, True)

    # (a) ---------------------------------------------------------------------------
    crit = tick_criterion()
    rep.add("the tick bit: for every x mod 4320, 864 lies in <x> iff 5 does not divide x (iff x e5 != 0 with "
            "e5 = 3456). So 24 of the 48 subgroups hold the tick (the divisors of 864), each subgroup holds all "
            "five levels or only 0, width x index = 864 for every width prime to 5, 16 of the 24 have order "
            "divisible by 20, and the bit is not additive (2 and 3 hold it, 5 does not)", T,
            all(crit.values()), crit)
    bad, orders_ok, seen = check_claims()
    rep.add(f"every tick sentence of the sibling's ledger is that bit: {len(TICK_CLAIMS)} sentences from "
            f"{len(seen)} joins (energy, golden, observer loop, mirrors, phase, charge, spin, heat, monopole, "
            "field, Einstein, two 36s, sign tensor, Om, karma, japa, mantra, bubbles, horizon, above and below, "
            "tick bounds, gravity dots, K5 chain, levels, pada, SM time, cakra, smear, readout, alpha, Hubble, "
            "height), with their step counts and indices, and 38 stated subgroup orders", T,
            not bad and orders_ok, {"failures": bad, "joins": dict(seen)})
    rep.add("readings that ride on the bit are counts: 6 + 15 + 15 = 21 + 15 = 36, wings 21 + 7 + 77 = 105, "
            "98 + 62 = 160, 30/36 = 5/6, 250 x 4320 = 1080000, 432 x 2 = 288 x 3 = 108 x 8 = 216 x 4 = 144 x 6 "
            "= 864, 27 x 192 = 864 mod 4320, the monopole chain <120> < <60> < <30> < <10>", AR,
            all(tick_arithmetic().values()), tick_arithmetic())

    # (b) ---------------------------------------------------------------------------
    dc, affine = day_coxeter_group()
    rep.add("the tick is the commutator of the day and the Coxeter clock: d c' d^-1 c'^-1 = c'^6 = r r'. The "
            "day-Coxeter group has order 120, centre <c'^5> (the shared <720>, order 6) and derived group the "
            "tick (order 5); the day acts on the tick by doubling, d (r r') d^-1 = (r r')^2", T,
            all(v for k, v in dc.items() if k not in ("five day clocks", "tick rotates them", "day doubles them",
                                                      "centre fixes them")), dc)
    rep.add("the five conjugate day clocks are permuted as the affine group of the pentagon: the tick rotates "
            "them x -> x + 1, the day doubles them x -> 2x (pentagon to pentagram), the centre fixes them. The "
            "sibling's 'doubling and rotation give 20 affine maps' is the day-Coxeter group modulo its centre", T,
            dc["five day clocks"] and dc["tick rotates them"] and dc["day doubles them"] and dc["centre fixes them"],
            affine)
    gold, _ = golden_clock()
    rep.add("the golden clock: the 24 elements of order 20 in the Coxeter normalizer all have twist 11, and v "
            "with v^2 = c'^3 has v^4 = c'^6 = r r' (every fourth golden step is the tick). Three cyclic 20s "
            "share that law: <216> on the circle, <v> on the bath, B = [[1,1],[1,0]] mod 5 (order 20, B^4 "
            "unipotent of order 5). The affine 20 of the five day clocks is not cyclic", T, all(gold.values()), gold)
    mir, acts = mirrors()
    rep.add("mirrors: the circle's negation x -> -x (fixing 0 and 2160, swapping 864 <-> 3456, 1728 <-> 2592 "
            "and the golden steps 1080 <-> 3240) is realized by the 30 elements with twist -1, each inverting "
            "the clock and the tick; 10 are involutions keeping the carrier, acting on it as the pentagon "
            "reflection i -> -i (five) or its negative (five)", T, all(mir.values()), {**mir, "acts": dict(acts)})
    cs = carrier_symmetry_checks()
    rep.add("on the fifteen atoms the graph reflection keeps D^2 and fixes three atoms; the involution "
            "i -> 14 - i (above and below) fixes one atom, has eigenspaces 8 + 7 and does not keep D^2", T,
            all(cs.values()), cs)
    ex = carrier_exchange()
    rep.add("carrier exchange: the stabilizer of the pair {A4, A4'} in W(E8) has 57600 elements. The 28800 that "
            "keep both act on the index-5 glue by +-1; the 28800 that exchange them act by +-2 (doubling) and "
            "have orders 4, 8, 12 or 20. No involution exchanges the carrier and its twin", T,
            ex["keep"] == ex["exchange"] == 28800 and set(ex["exchange orders"]) == {4, 8, 12, 20}
            and ex["keep acts on the glue by"] == {1: 14400, 4: 14400}
            and ex["exchange acts on the glue by"] == {2: 14400, 3: 14400}
            and ex["glue classes of the 200 mixed roots"] == {1: 50, 2: 50, 3: 50, 4: 50}
            and not ex["involutive exchange"], ex)
    cf = check_clock_file()
    rep.add("data/clocks.json holds explicit elements of W(E8) (standard coordinates, x 4): the Coxeter clock, "
            "the tick r r', the day (order 24), the golden clock (order 20) and the mirror; every relation is "
            "re-checked from the file alone. This is the order-24 element the sibling build lacks", T,
            all(cf.values()), cf)

    # (c) ---------------------------------------------------------------------------
    en = energy_sectors()
    rep.add("energy: D^2 is block diagonal, so the vertex and edge sectors never exchange energy. The checked "
            "datum has quadratic form 64 = 40 + 6 + 18 and energy 34 = 20 + (3 + 9) + 2 (uniform, vertex "
            "contrast, edge image, cycle); E_V = 23 and E_E = 11 are conserved along the motion", T,
            all(en.values()), en)
    rep.add("decoupling: under canonical quantization of S the oscillating modes evolve by U_V(t) x U_E(t), so the "
            "carrier never entangles vertices with edges; entanglement could only sit in initial data. "
            "'Entanglement is not stored' is sharpened to: the carrier cannot create it", CD,
            en["D^2 is block diagonal (vertices | edges)"],
            note="conditional on a quantization the canon does not store; the classical statement (no energy "
                 "exchange) is the THEOREM above")
    sp_ = spin_structure()
    rep.add("spin counts: the 112 integer roots are D8 and the 128 half-integer roots are one W(D8) orbit (a "
            "half-spin weight set), so 248 = so(16) + 128. [W(E8) : W(D8)] = 135 is the band-top D8 family, and "
            "the half-turn's 256 fixed momenta are 1 + 120 + 135. SU(2) is not derived", T, all(sp_.values()), sp_)
    rep.add("field: the stored source equation q'' + 4q = 0 has frequency 2, but 4 is not in spec D^2 = "
            "{0, 3, 8}: the source oscillator is not one of the fifteen carrier modes", OB,
            set(carrier.spectrum_multiplicities()) == {0, 3, 8} and 4 not in carrier.spectrum_multiplicities())
    cube, tr = four_cube_laplacian()
    rep.add("SMEAR_JOIN replayed: the 81-cell complex of the 4-cube has Laplacian spectrum 0, 2, 4, 6, 8 with "
            "multiplicities 1, 8, 24, 32, 16 (tensor power of the interval) and trace 432", T,
            cube == {0: 1, 2: 8, 4: 24, 6: 32, 8: 16} and tr == 432, cube)
    rep.add("not stored and not formed here: source infinity, foam, the double slit, entanglement, a Bell count, "
            "the photoelectric effect, a work function, electron, photon, proton, Compton and Bohr lengths, and "
            "19 Standard-Model parameters. No operand is stored, and the action has no dimensionful constant "
            "(TIME_BIND unbound), so no length can be formed", UF, True)
    rep.add("the sibling's archive counts (17,914 checks, 151 check groups, 22,158 role-chain instances) were "
            "not rerun here", RP, True)
    return rep
