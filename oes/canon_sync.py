"""Layer 20. The latest canon, read and synchronized (28 Oct 2026, 16:30 UTC, re-read 16:49).

Sources read before this build (Google Drive):

* the canon Quick Access workbook, sheet 00_POST_OM736_SOURCE_DELTA_1028 (updated 15:05 UTC,
  source cutoff 14:59:48 UTC). OMSOON736 and the 10:04 Canon Check stay controlling. This
  repository's 14:37 build is listed as a SELECTED REFERENCE and its replay as SOURCE-REPORTED
  EXECUTION. Layer 19 and everything below arrived after the cutoff;
* the controlling Canon Check (OES_Canon_Check_and_Open_Items_20261028.txt, 10:04 UTC). It proves
  the growing-time preparation laws P1-P6 and the combined scalar bound S1, (r+1)(d+2) >= 195;
* the 12:32 OES_CANON_UPDATE. The workbook marks its collar-to-224, t^-9/4 upper bound and
  "maximum group speed exactly sqrt30" claims SOURCE-CLAIMED ONLY;
* COURT_CORRECTION (14:29 UTC);
* the sibling's later notes and build (15:57-16:18 UTC: CLOSURE_234, JOIN_234, MORE_DOTS,
  NORMALIZE, ORBIT, UPGRADE_JOIN, CRT_JOIN, IDEMPOTENTS, PRIMARY_SPLIT, CURRENT and
  one-machine-20261028-current.pdf);
* a separate model, "Finite Spectral Dynamics with Complete Observation and Exact Cyclic
  Addresses" (finite-spectral-model-major-upgrade-20261028, 16:07 UTC, 17,914 checks reported);
* the sibling's notes posted while this layer was built (16:31-16:43 UTC: SPINE_CORRECTIONS,
  COXETER_POWERS, ATLAS_FACTOR, SUN_MOON) and its paper one-machine-20261028-sun.pdf (16:43);
  the 16:47 consolidation CURRENT_20261028_2046 restates them, with the same paper text.

Synchronized here:

(a) A correction to this repository, made in layer 1. 3|x|^4 - 7 sum x^4 is harmonic for the
    ambient Laplacian of R^5. For the contrast plane's own Laplacian the harmonic line is
    2|x|^4 - 5 sum x^4, as the canon now says.
(b) A canon claim proved. The bath's group speed |grad sqrt(eps)| is at most sqrt30
    everywhere, with supremum sqrt30 approached as k -> 0 and never attained. The proof is
    |u.grad eps|^2 = |sum (u.a) 2 sin(a.k/2) cos(a.k/2)|^2 <= sum (u.a)^2 cos^2 * 4 sum sin^2
    <= 60 * 2 eps, using the frame sum a a^T = 60 I.
(c) The Canon Check's preparation theorem. Its algebraic identities are replayed (the Bernstein
    ellipse, ||C|| = sqrt495, the optimal eta* and exponent). The theorem stays CONDITIONAL on
    the inherited exterior contract, which layers 3-4 confirm.
(d) The scalar frontier. S1 and its table follow from layer 14, which excludes every shape
    with (r+1)(d+2) <= 455 on W_0..W_600 mod p.
(e) The circle notes. The CRT idempotents, primary split, 234/522 joins and orbit indices
    hold. Two duality errors are corrected: the step 5 and the step 25 generate the
    order-864 subgroup, not the tick.
(f) NORMALIZE refined. In W(E8) the day and Coxeter clocks generate a group of order exactly
    120 (d^4 = c'^5). The abstract semidirect product C30 x| C24 of order 720 cannot embed,
    because the normalizer of <c'> has order 240.
(g) The separate model replayed:
    - five channels are necessary and sufficient, with H^T W H = K + P0;
    - the 252 five-edge sensor designs split 162 complete + 90 rank 4. 72 are optimal,
      with minimum eigenvalue (3 - sqrt5)/6, and every complete design has det 1/162;
    - the 25-coordinate flag geometry, with intersection det -48;
    - the vertex distance sqrt(8/7), shown exact by a symmetry reduction;
    - the collocated transfer functions.
(h) The 16:31-16:43 notes. They adopt the six circle corrections of layer 19, and every
    circle statement in them holds. Three things are added here:
    - the named Coxeter powers fix no root, but on the momentum torus c^k fixes
      Phi_n(1)^(8/phi(n)) points, n = 30/gcd(k, 30): 1, 1, 1, 25, 81, 25, 256. These are the
      fixed momenta the notes leave unreplayed;
    - "the circle still makes the day and Coxeter clocks commute" holds on the circle only.
      On the bath no two such clocks commute, because the centralizer of c' is <c'>;
    - one remnant is left in the 16:43 paper: "360000 is not a step".
"""

import itertools
from collections import Counter
from math import ceil, gcd

import numpy as np
import sympy as sp

from . import carrier, gates, handover, spine
from .record import Report

N = spine.N


# ------------------------------------------------------------------- (b) group speed

def group_speed(samples=20000, seed=30):
    """max |grad eps|^2 / (120 eps) over random Bloch momenta, and its small-k limit."""
    R = handover.e8_roots()
    frame = np.round(4 * R.T @ R).astype(int)
    rng = np.random.default_rng(seed)
    worst = 0.0
    for th in rng.uniform(-np.pi, np.pi, size=(samples, 8)):
        ph = R @ th
        eps = float((1 - np.cos(ph)).sum())
        grad = np.sin(ph) @ R
        worst = max(worst, float(grad @ grad) / (120 * eps))
    u = rng.standard_normal(8)
    u /= np.linalg.norm(u)
    small = []
    for t in (1e-1, 1e-2, 1e-3):
        ph = R @ (t * u)
        small.append(float((np.sin(ph) @ R) @ (np.sin(ph) @ R)) / (120 * float((1 - np.cos(ph)).sum())))
    return np.array_equal(frame, 240 * np.eye(8, dtype=int)), worst, small


# ------------------------------------------------------- (c) the preparation identities

def preparation_identities():
    v, eta, phi, T, c = sp.symbols("v eta phi T c", positive=True)
    w = v ** 2
    ellipse = sp.simplify(128 + 64 * (w + 1 / w) - 64 * (v + 1 / v) ** 2) == 0
    vv = sp.exp(eta / 2 + sp.I * phi)
    im = sp.simplify((sp.im(sp.expand_complex(8 * (vv + 1 / vv))) - 16 * sp.sinh(eta / 2) * sp.sin(phi))
                     .rewrite(sp.exp)) == 0
    CC = 183 * sp.eye(6) + 52 * sp.ones(6, 6)
    norm = max(CC.eigenvals()) == 495
    d = 8 * T * c                                   # c = d / (8T) > 1
    f = 16 * T * sp.sinh(eta / 2) - d * eta
    star = 2 * sp.acosh(c)
    crit = sp.simplify(sp.diff(f, eta).subs(eta, star)) == 0
    convex = sp.simplify(sp.diff(f, eta, 2) - 4 * T * sp.sinh(eta / 2)) == 0
    value = sp.simplify(f.subs(eta, star) - (2 * sp.sqrt(d ** 2 - 64 * T ** 2) - 2 * d * sp.acosh(c)))
    value_ok = value == 0 or abs(float(value.subs({T: 1.3, c: 2.7}))) < 1e-12
    return {"ellipse": ellipse, "imaginary part": im, "norm": norm, "critical point": crit,
            "convex": convex, "minimum": value_ok}


# -------------------------------------------------------------- (e) the circle notes

CRT = {32: 3105, 27: 2080, 5: 3456}


def circle_notes():
    o = spine.order
    e2, e3, e5 = CRT[32], CRT[27], CRT[5]
    comp = lambda x, e: x * e % N
    out = {
        "idempotents": all(e * e % N == e for e in CRT.values())
        and e2 * e3 % N == e2 * e5 % N == e3 * e5 % N == 0 and (e2 + e3 + e5) % N == 1
        and [o(e) for e in (e2, e3, e5)] == [32, 27, 5]
        and (e2, e3, e5) == (23 * 135, 13 * 160, 4 * 864),
        "primary split": (2160 + 1440 + 864) % N == 144
        and all(comp(x, e5) == x for x in (864, 1728, 3456))
        and all(comp(x, e3) == x for x in (160, 1440)) and all(comp(x, e2) == x for x in (1080, 2160))
        and all(comp(x, e5) == 0 for x in (180, 360, 40, 720))
        and (comp(432, e2), comp(432, e3), comp(432, e5)) == (2160, 0, 2592)
        and (comp(1296, e2), comp(1296, e3), comp(1296, e5)) == (2160, 0, 3456)
        and (comp(234, e5), comp(234, e3)) == (864, 2 * 1440),
        "234 joins": spine.gen(234) == spine.gen(522) == 18 and o(234) == 240
        and spine.contains(18, 36) and o(18) // o(36) == 2
        and [o(x) for x in (756, 672, 112, 162, 72, 360)] == [40, 45, 270, 80, 60, 12]
        and 168 * 234 % N == 432 and o(168) == 180 and 4 * 10 + 8 * 9 == 112
        and 2 * 45 + 4 * 36 == 234 and 6 * 112 == 240 + 432,
        "orbit indices": [o(g) // 6 for g in (144, 180, 36, 18, 1)] == [5, 4, 20, 40, 720]
        and [pow(7, k, 30) for k in (1, 2, 3, 4)] == [7, 19, 13, 1],
        "address 1234": (10 + 36 * 10 + 432 * 0 + 864 * 1, 1234 % 32, 1234 % 27, 1234 % 5) == (1234, 18, 19, 4)
        and (e2 * 18 + e3 * 19 + e5 * 4) % N == 1234,
        "seven-clock register C30240": (25921 % 4320, 25921 % 7, 4320 % 7) == (1, 0, 1),
    }
    return out


# ------------------------------------------------------------------ (f) the clock group

def clock_group_order():
    _, cp, *_ = spine.spine_clock()
    d = spine.day_clock()
    seen = {spine.I8.tobytes(): spine.I8}
    frontier = [spine.I8]
    while frontier:
        new = []
        for M in frontier:
            for g in (cp, d):
                P = M @ g
                key = P.tobytes()
                if key not in seen:
                    seen[key] = P
                    new.append(P)
        frontier = new
        if len(seen) > 1000:
            break
    return len(seen)


# ------------------------------------------------------- (g) the separate model replayed

def observer_completion():
    M = carrier.signless_incidence()
    D = carrier.dirac(M)
    K = D * D
    Nb = sp.Matrix.hstack(*D.nullspace())
    G = Nb.T * Nb
    L = G.inv() * Nb.T
    P0 = Nb * L
    Dplus = (11 * D - D ** 3) / 24
    H = sp.Matrix.vstack(D, L)
    Rm = sp.Matrix.hstack(Dplus, Nb)
    W = sp.diag(sp.eye(15), G)
    I15 = sp.eye(15)
    return {
        "dark sector dim 5": Nb.shape[1] == 5,
        "P0 = I - 11K/24 + K^2/24": P0 == I15 - 11 * K / 24 + K ** 2 / 24,
        "D+ is the pseudo-inverse": D * Dplus * D == D and Dplus * D * Dplus == Dplus,
        "R H = I15": Rm * H == I15,
        "H^T W H = K + P0": H.T * W * H == K + P0,
    }, P0


def sensor_census(P0):
    """All 252 choices of five edge coordinates: I_A = C_A P0 C_A^T."""
    edge_idx = list(range(5, 15))
    x = sp.symbols("x")
    classes = Counter()
    rank4 = 0
    best = None
    dets = set()
    opt_example = None
    for A in itertools.combinations(range(10), 5):
        rows = [edge_idx[a] for a in A]
        IA = P0.extract(rows, rows)
        if IA.rank() < 5:
            rank4 += IA.rank() == 4
            continue
        cp = sp.factor(IA.charpoly(x).as_expr())
        classes[cp] += 1
        dets.add(IA.det())
        lam_min = float(np.linalg.eigvalsh(np.array(IA, dtype=float)).min())
        if best is None or lam_min > best + 1e-12:
            best, opt_example = lam_min, A
    stated = [edge_idx[a] for a in (0, 1, 2, 4, 6)]                # edges 01, 02, 03, 12, 14
    stated_min = float(np.linalg.eigvalsh(np.array(P0.extract(stated, stated), dtype=float)).min())
    return classes, rank4, dets, best, stated_min


def flag_geometry():
    """The 25-coordinate ordered-flag triple on C^5 x C^5 and its embedding of the carrier."""
    n = 5
    idx = {(i, j): i * n + j for i in range(n) for j in range(n)}
    s = 1 / np.sqrt(2)
    D = np.zeros((25, 25))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[idx[(i, j)], idx[(i, i)]] += s
                D[idx[(j, i)], idx[(i, i)]] += s
                D[idx[(i, i)], idx[(i, j)]] += s
                D[idx[(j, j)], idx[(i, j)]] += s
    Jm = np.zeros((25, 25))
    for (i, j), k in idx.items():
        Jm[idx[(j, i)], k] = 1
    Gam = np.diag([1.0 if i == j else -1.0 for i in range(n) for j in range(n)])
    E = np.zeros((25, 15))
    for i in range(n):
        E[idx[(i, i)], i] = 1
    for k, (i, j) in enumerate(carrier.edges()):
        E[idx[(i, j)], 5 + k] = s
        E[idx[(j, i)], 5 + k] = s
    Dc = np.array(carrier.dirac(carrier.signless_incidence()), float)
    pi = lambda a: np.diag([a[i] for i in range(n) for j in range(n)])
    rho = lambda b: np.diag([b[j] for i in range(n) for j in range(n)])
    rng = np.random.default_rng(7)
    a, b = rng.standard_normal(5), rng.standard_normal(5)
    first_order = np.allclose((D @ pi(a) - pi(a) @ D) @ rho(b) - rho(b) @ (D @ pi(a) - pi(a) @ D), 0)
    ev = np.round(np.linalg.eigvalsh(D @ D), 9)
    Q = np.array([[np.trace(Gam @ pi(np.eye(5)[i]) @ rho(np.eye(5)[j])) for j in range(n)] for i in range(n)])
    # distance between vertices 0 and 1: by convexity and the symmetries (permute the other three,
    # swap 0 and 1 with a -> -a), an optimal a is s(e0 - e1); so d = 2 / ||[D, pi(e0 - e1)]||.
    Dsym = sp.zeros(25, 25)
    for r_ in range(25):
        for c_ in range(25):
            if D[r_, c_]:
                Dsym[r_, c_] = sp.sqrt(2) / 2
    a01 = [1, -1, 0, 0, 0]
    piS = sp.diag(*[a01[i] for i in range(n) for j in range(n)])
    Cm = Dsym * piS - piS * Dsym
    norm2 = max(sp.Matrix(Cm.T * Cm).applyfunc(sp.nsimplify).eigenvals())
    dist = 2 / sp.sqrt(norm2)
    return {
        "E^T E = I": np.allclose(E.T @ E, np.eye(15)),
        "D E = E D_carrier": np.allclose(D @ E, E @ Dc),
        "spec D^2 = {0^15, 3^8, 8^2}": sorted(Counter(ev).items()) == [(0.0, 15), (3.0, 8), (8.0, 2)],
        "J^2 = I, JD = DJ, Gamma D = -D Gamma": np.allclose(Jm @ Jm, np.eye(25)) and np.allclose(Jm @ D, D @ Jm)
        and np.allclose(Gam @ D, -D @ Gam),
        "first-order condition": first_order,
        "intersection Q = 2I - J, det -48": np.allclose(Q, 2 * np.eye(5) - 1) and round(np.linalg.det(Q)) == -48,
        "vertex distance sqrt(8/7)": sp.simplify(dist - sp.sqrt(sp.Rational(8, 7))) == 0,
    }, str(dist)


def collocated_transfer():
    z = sp.symbols("z")
    P = carrier.spectral_projectors()
    Gz = P[0] / z ** 2 + P[3] / (z ** 2 + 3) + P[8] / (z ** 2 + 8)
    GV = sp.simplify(Gz[0, 0] - (z ** 2 + 7) / ((z ** 2 + 3) * (z ** 2 + 8))) == 0
    GE = sp.simplify(Gz[5, 5] - (1 / (2 * z ** 2) + sp.Rational(2, 5) / (z ** 2 + 3)
                                 + sp.Rational(1, 10) / (z ** 2 + 8))) == 0
    K = carrier.D2()
    same = all(sp.simplify(Gz[i, i] - Gz[0, 0]) == 0 for i in range(5)) and \
        all(sp.simplify(Gz[i, i] - Gz[5, 5]) == 0 for i in range(5, 15))
    inv = sp.simplify(Gz * (z ** 2 * sp.eye(15) + K) - sp.eye(15)) == sp.zeros(15, 15)
    return GV and GE and same and inv


# ---------------------------------------------------------- (h) the 16:31-16:43 notes

POWERS = {1: (8, 30), 3: (24, 10), 5: (40, 6), 6: (48, 5), 10: (80, 3), 12: (48, 5), 15: (120, 2)}


def coxeter_powers():
    """COXETER_POWERS: cycles of c^k on the 240 roots, and the momenta c^k fixes on the torus."""
    c = spine.coxeter()
    fixed = lambda k: round(abs(np.linalg.det(spine.mpow(c, k) - spine.I8)))
    closed = lambda n: int(sp.cyclotomic_poly(n, 1)) ** (8 // int(sp.totient(n)))
    rows = {}
    for k, (cycles, length) in POWERS.items():
        sizes = spine.root_orbits(spine.mpow(c, k))
        n = 30 // gcd(k, 30)
        rows[144 * k % N] = {
            "table": len(sizes) == cycles and set(sizes) == {length} == {n} == {spine.order(144 * k)},
            "fixed momenta": fixed(k),
            "closed form": closed(n),
        }
    every_k = all(fixed(k) == closed(30 // gcd(k, 30)) for k in range(1, 30))
    return rows, every_k


def atlas_factor():
    o = spine.order
    return {
        "tower in atlases 1, 4, 12, 24, 120": [s // 36 for s in (36, 144, 432, 864, N)] == [1, 4, 12, 24, 120]
        and spine.contains(36, 144) and spine.contains(144, 432) and spine.contains(432, 864)
        and [o(s) for s in (36, 144, 432, 864)] == [120, 30, 10, 5],
        "12 + 24 = 36, i.e. 432 + 864 = 36^2": 432 + 864 == 36 ** 2,
        "sun, half-turn, 3456 = 40, 60, 96 atlases": all(spine.contains(36, s) for s in (1440, 2160, 3456))
        and (1440 // 36, 2160 // 36, 3456 // 36) == (40, 60, 96),
        "3105, 2080, 1 leave 9, 28, 1": (CRT[32] % 36, CRT[27] % 36, 1 % 36) == (9, 28, 1)
        and not spine.contains(36, CRT[32]) and not spine.contains(36, CRT[27]),
    }


def sun_moon():
    o = spine.order
    part = lambda x, p: x * CRT[p] % N
    return {
        "12 x 120 = 1440 = 4 x 360, 3 x 1440 = 4320": 12 * 120 == 1440 == 4 * 360 and 3 * 1440 == N,
        "sun = c^10, pure of order 3": 10 * 144 == 1440 and o(1440) == 3 and part(1440, 27) == 1440,
        "moon: order 36, remainder 12, not a Coxeter power": o(120) == 36 and 120 % 36 == 12
        and not spine.contains(144, 120),
        "moon parts 1080 + 3360 + 0": (part(120, 32), part(120, 27), part(120, 5)) == (1080, 3360, 0),
        "moon meets atlas in the signs, which hold the sun": spine.meet(120, 36) == 360 and o(360) == 12
        and spine.contains(360, 1440),
        "2880 has order 3, 240 order 18 in the moon, 7 moons generate": o(2880) == 3 and o(240) == 18
        and spine.contains(120, 240) and spine.gen(7 * 120) == spine.gen(120),
    }


def commuting_clocks():
    """On the circle the day and Coxeter clocks commute and generate the atlas; W(E8) has neither."""
    _, cp, *_ = spine.spine_clock()
    centralizer = [w for m, w in spine.normalizer() if m == 1]
    powers = [spine.mpow(cp, j) for j in range(30)]
    return {
        "on the circle they generate the atlas, order 120": spine.join(180, 144) == 36 and spine.order(36) == 120,
        "order 120 needs GL_10(Z)": spine.min_dimension(120) == 10,
        "centralizer of c' = <c'>, no element of order 24": len(centralizer) == 30
        and all(any(np.array_equal(w, P) for P in powers) for w in centralizer)
        and 24 not in {spine.mat_order(w) for w in centralizer},
    }


# ----------------------------------------------------------------------------- run

def run():
    rep = Report("20-canon")
    T, AR, OB, CD, RP = (gates.THEOREM, gates.ARITHMETIC, gates.OBSTRUCTION,
                         gates.CONDITIONAL, gates.REPORTED)

    rep.add("canon position (Quick Access, 15:05 UTC, cutoff 14:59:48): OMSOON736 and the 10:04 Canon Check "
            "are controlling; the 14:37 build of this repository is a SELECTED REFERENCE and its replay "
            "SOURCE-REPORTED; layers 19-20 arrived after the cutoff", RP, True,
            note="read 28 Oct 16:30 UTC and again at 16:49; nothing here changes a canon grade")

    # (a) -------------------------------------------------------------------------------
    cm = carrier.contrast_moments()
    rep.add("correction absorbed in layer 1: the contrast plane's harmonic quartic is 2|x|^4 - 5 sum x^4; "
            "3|x|^4 - 7 sum x^4 is harmonic only for the ambient Laplacian of R^5", OB,
            all(cm.values()) and any("2|x|^4-5sum" in k for k in cm),
            note="the 16:43 sibling paper keeps both: its section 13 calls 3|p|^4 - 7 sum p^4 the primitive "
                 "harmonic line on the contrast plane, computed with the ambient Laplacian; its moment theorem "
                 "calls 2 s2^2 - 5 s4 invariant-harmonic and 3 s2^2 - 7 s4 not")

    # (b) -------------------------------------------------------------------------------
    frame_ok, worst, small = group_speed()
    rep.add("maximal group speed of the bath is sqrt30, as a supremum: |grad eps|^2 <= 120 eps everywhere "
            "(frame sum a a^T = 60 I and Cauchy-Schwarz), with equality only as k -> 0. The 12:32 claim "
            "'maximum group speed exactly sqrt30' holds in this sense", T,
            frame_ok and worst < 1 and small[-1] > 0.999999, {"max ratio (20000 samples)": worst,
                                                               "ratio as k -> 0": small})

    # (c) -------------------------------------------------------------------------------
    ids = preparation_identities()
    rep.add("Canon Check P1/P2 identities replayed: 128 + 64(w + 1/w) = 64(v + 1/v)^2, |Im sqrt E| = "
            "16 sinh(eta/2)|sin phi|, ||C||^2 = 495, eta* = 2 arcosh(d/8T) with exponent "
            "2 sqrt(d^2 - 64T^2) - 2d arcosh(d/8T), strictly convex", T, all(ids.values()), ids)
    rep.add("growing-time preparation (Canon Check P2): at polynomial port budget the horizon grows at least "
            "like eps^(-1/2) for the monopole families and eps^(-1/3) for a dipole target", CD, True,
            note="proof received in the controlling Canon Check; its algebra is replayed above; it rests on "
                 "the inherited exterior contract 0 <= D <= 256, C*C = 183P_c + 495P_u (layers 3-4) and on "
                 "the static-tail asymptotics; necessary only, no matching protocol")

    # (d) -------------------------------------------------------------------------------
    table = {2: 48, 3: 38, 4: 32, 5: 27, 6: 24, 7: 21, 8: 19, 9: 17, 10: 16, 11: 14, 12: 13, 13: 12, 14: 12}
    ours = {d: ceil(456 / (d + 2)) - 1 for d in table}
    rep.add("Canon Check S1 ((r+1)(d+2) >= 195, r = 11 needs d >= 15) and its whole table follow from layer 14, "
            "which excludes every shape with (r+1)(d+2) <= 455 on W_0..W_600 mod p (so r = 11 needs d >= 36); "
            "the order-16, degree-58 operator has product 1020", T,
            all(ours[d] >= table[d] for d in table) and ceil(456 / 12) - 2 >= 15 and 17 * 60 == 1020,
            {d: [table[d], ours[d]] for d in table})

    # (e) -------------------------------------------------------------------------------
    notes = circle_notes()
    rep.add("circle notes of 15:57-16:18 replayed: CRT idempotents 3105, 2080, 3456 (squares, zero products, "
            "sum 1, orders 32, 27, 5), the primary split, the 234/522 joins, the orbit indices 5, 4, 20, 40, 720, "
            "the address 1234, and the C30240 register", T, all(notes.values()), notes)
    rep.add("correction: CRT_JOIN 'the five added channels are the step 5, which generates the tick' and "
            "UPGRADE_JOIN 'the step 25 generates the tick subgroup, order 864'. <5> = <25> is the subgroup of "
            "order 864 (index 5); the tick <864> has order 5. The step 5 is dual to the tick", OB,
            spine.gen(5) == spine.gen(25) == 5 and spine.order(5) == 864 and spine.order(864) == 5
            and spine.subgroup(5) != spine.subgroup(864))

    # (f) -------------------------------------------------------------------------------
    order_g = clock_group_order()
    rep.add("NORMALIZE refined: in W(E8) the day clock and the Coxeter clock generate a group of order exactly "
            "120 (d^4 = c'^5, d c' d^-1 = c'^7). The abstract semidirect product C30 x| C24 of order 720 does "
            "not embed: the normalizer of <c'> has order 240", T,
            order_g == 120 and len(spine.normalizer()) == 240, order_g)

    # (g) -------------------------------------------------------------------------------
    obs, P0 = observer_completion()
    rep.add("separate model, Theorem 2: five fixed channels are necessary (dim ker D = 5, and the dark sector "
            "moves freely) and sufficient: R H = I15, P0 = I - 11K/24 + K^2/24, D+ = (11D - D^3)/24, "
            "H^T W H = K + P0", T, all(obs.values()), obs)
    classes, rank4, dets, best, stated_min = sensor_census(P0)
    x = sp.symbols("x")
    opt = sp.factor((x - sp.Rational(1, 2)) * (x ** 2 - x + sp.Rational(1, 9)) ** 2)
    oth = sp.factor((x - 1) * (x - sp.Rational(1, 3)) ** 2 * (x ** 2 - sp.Rational(5, 6) * x + sp.Rational(1, 18)))
    rep.add("separate model, Theorem 3: of the 252 five-edge designs 162 are complete and 90 have rank 4; "
            "all complete designs have det 1/162; 72 are optimal with minimum eigenvalue (3 - sqrt5)/6, "
            "e.g. edges {01, 02, 03, 12, 14}", T,
            sum(classes.values()) == 162 and rank4 == 90 and dets == {sp.Rational(1, 162)}
            and classes.get(opt) == 72 and classes.get(oth) == 90
            and abs(best - (3 - np.sqrt(5)) / 6) < 1e-9 and abs(stated_min - best) < 1e-12,
            {"classes": {str(k): v for k, v in classes.items()}, "best": best})
    flags, dist = flag_geometry()
    rep.add("separate model, flag geometry: E: C^15 -> C^25 is an isometry with DE = ED, spec D^2 = "
            "{0^15, 3^8, 8^2}, real structure and grading, first-order condition, intersection det -48, and "
            "vertex distance exactly sqrt(8/7)", T, all(flags.values()), {**flags, "d(0,1)": dist},
            note="the distance is exact: by convexity and symmetry an optimal a is s(e0 - e1)")
    rep.add("separate model, falsifiable transfer: every vertex has G_V = (z^2+7)/((z^2+3)(z^2+8)) and every "
            "edge G_E = 1/(2z^2) + 2/(5(z^2+3)) + 1/(10(z^2+8)) from the spectral projectors", T,
            collocated_transfer())
    rep.add("COURT_CORRECTION: (16/5, -11/5, -1, 1/5, 0, 0, 0, 0) has square 403/25 (402/25 with fourth "
            "coordinate 0); 3 x 17280 + 2160 x 128 = 328320 and 17280 + 2160 x 128 = 293760", AR,
            sp.Rational(16, 5) ** 2 + sp.Rational(11, 5) ** 2 + 1 + sp.Rational(1, 5) ** 2 == sp.Rational(403, 25)
            and 3 * 17280 + 2160 * 128 == 328320 and 17280 + 2160 * 128 == 293760)

    # (h) -------------------------------------------------------------------------------
    rep.add("re-read 16:49 UTC: the sibling's 16:31-16:43 notes (SPINE_CORRECTIONS, COXETER_POWERS, ATLAS_FACTOR, "
            "SUN_MOON) and paper adopt the six circle corrections of layer 19. They leave the fixed momenta "
            "25/81/256 and the list of orders that act on the bath unreplayed; layers 19-20 hold both as THEOREM",
            RP, True)
    pw, every_k = coxeter_powers()
    rep.add("COXETER_POWERS replayed: c^k for the steps 144, 432, 720, 864, 1440, 1728, 2160 acts on the 240 roots "
            "as 8 x 30, 24 x 10, 40 x 6, 48 x 5, 80 x 3, 48 x 5, 120 x 2 cycles and fixes no root. On the momentum "
            "torus the same c^k fixes |det(c^k - I)| = Phi_n(1)^(8/phi(n)) points, n = 30/gcd(k, 30), for every "
            "k = 1..29; for these steps 1, 1, 1, 25, 81, 25, 256. That is a different set from the roots, and it "
            "is nontrivial exactly when n is a prime power", T,
            every_k and all(r["table"] and r["fixed momenta"] == r["closed form"] for r in pw.values())
            and [r["fixed momenta"] for r in pw.values()] == [1, 1, 1, 25, 81, 25, 256],
            {step: r["fixed momenta"] for step, r in pw.items()})
    af, sm = atlas_factor(), sun_moon()
    rep.add("ATLAS_FACTOR and SUN_MOON replayed: the refined tower is 1, 4, 12, 24, 120 atlases, and 12 + 24 = 36 "
            "is 432 + 864 = 36^2. The sun, half-turn and 3456 are atlas multiples; 3105 and 2080 are not. Twelve "
            "moons make the sun, the sun is c^10 and pure of order 3, and the moon (order 36) is no Coxeter power. "
            "Its primary parts are 1080 + 3360 + 0, and it meets the atlas in the signs", T,
            all(af.values()) and all(sm.values()), {**af, **sm})
    rep.add("shared integers (no map joins them): the cycle counts 24, 40, 48, 80, 120 are the day order, the pada "
            "step, the number of subgroups, the order of 162 and the atlas order. The sun is 40 atlases, the "
            "pada step. The half-turn is 60 atlases, the frame constant. The squared stiffness ratio 8/3 is "
            "Coxeter cycles over the sun cycle length", AR,
            [spine.order(180), 4320 // 108, len(spine.divisors(N)), spine.order(162), spine.order(36)]
            == [24, 40, 48, 80, 120] and 1440 // 36 == N // 108 and 2160 // 36 == 60
            and sp.Rational(240 // 30, 3) == sp.Rational(8, 3))
    cc = commuting_clocks()
    rep.add("SPINE_CORRECTIONS 'the circle still makes the day and Coxeter clocks commute' holds on the circle "
            "only. There the two clocks generate the atlas, of order 120. In W(E8) no element of order 24 commutes "
            "with c', because the centralizer of c' is <c'>, and no element has order 120. So a realized day "
            "clock must twist the Coxeter clock (layer 19: by 7)", T, all(cc.values()), cc)
    rep.add("remnant in the 16:43 paper: its circle-subgroup theorem still says '360000 is not a step', while "
            "its spine theorem says 'the scalar 360000 reduces to 1440'. Since 360000 = 83 x 4320 + 1440, the "
            "W0 scalar is the sun step", OB, 360000 % N == 1440 and spine.order(360000) == 3)

    # still open in the canon -----------------------------------------------------------
    rep.add("12:32 claims not replayed here and SOURCE-CLAIMED in the canon: strict convexity through E = 224 "
            "(collar 223.58 < E < 224 open) and a matching uniform t^(-9/4) upper bound", RP, True)
    rep.add("the separate model's 17,914 checks were not rerun; the items above were rebuilt from its "
            "definitions", RP, True)
    return rep
