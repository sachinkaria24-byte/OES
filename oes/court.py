"""Layer 15. Court U19.81 (the 064 -> 490 inverse-problem architecture), audited.

The court arrived on 28 Oct with a script marked "pre-verified". Here each claim
is run against the literal operands and the exact walk data, and given a status.

Stage 1, the 8-port (5, 2, 1) moments, envelopes and Loewner-Pick test.
  The sector eigenvalues are right: A_bb = 241 on V5 and 235 on V1, BB* = 183 on
  V5 and 495 on V1. The script's walk generator is wrong from W_4 on (7,772,208
  against 1,260,720). The moment sequences it builds are not positive definite
  (beta^2 <= 0 at the third Lanczos step), so they are not the moments of any
  measure. Its uniform-sector formula m_k - m_{k+1}/288 is wrong too, and its own
  assert fails. The uniform moment over the six clique sites is
  6 m_k - m_{k+1}/48, because <delta_0, Delta^k delta_alpha> = m_k - m_{k+1}/240
  for every root alpha. Here the envelopes are rebuilt from the true moments
  M_0..M_49: a 25-node Gauss rule for G_-, and a 26-node Lobatto rule pinned at 0
  and 256 for G_+. The true moments pass the Hausdorff test on [0, 256] exactly.
  The court's claim that (G_-(s1), G_+(s2)) cannot be realized together is
  correct (Markov-Krein uniqueness), but the script's certificate for it, the
  sign of a 6-moment Loewner difference quotient, gives a positive slope for that
  pair on the true moments, so the script never shows it.
Stage 2, H90 as a [9, 3, 7]_11 code. The Cauchy code is MDS and corrects 3
  errors. Nothing in the canon or this repository identifies it with H90.
Stage 3, observability. ker O is the 4-dim cross block and tomography completes
  it. The claimed reduction to 2 parameters under C5 fails for every V2 the court
  names. C5 has prime order, so every C5-invariant 2-site probe carries the
  trivial action, and so does the 8^2 doublet of D^2. Then
  dim Hom_C5(V2, U2) is 0 or 4, never 2.
Stage 4. omega = Omega_* sqrt(x) is homogeneous in Omega_*, so TIME_BIND stays
  UNBOUND.
The "complete expanded scalar polynomial annihilator" is not given anywhere.
Layer 14 forms one mod four primes: order 16, degree 58, first kernels at
(r+1)(d+2) = 456.

The same message (28 Oct) adds three remarks. The literal adapter's largest
cofactor is 68, so 4805 is not a 5x5 minor of it. The scalar bound
(r+1)(d+2) >= 195 is replayed and strengthened in layer 14. The preparation-time
bounds are recorded as REPORTED.
"""

from fractions import Fraction
from itertools import combinations, product
from math import comb

import numpy as np
import sympy as sp

from . import carrier, gates, literal, native, recurrence
from .record import Report

BAND = 256

# W_0..W_16 as printed by the court's own generator (fast_mu_table_fraction ...).
SCRIPT_W = [1, 0, 240, 13440, 7772208, 190068480, 86091345920, 7628349657600,
            592608522233728560, 14578011697637767680, 3513371810049782892288,
            498317105595766965150720, 3217165443483043809841953792,
            224365676038561700121035741184, 699703817574199557243184637710848,
            49503328225909140383007680208992256,
            50665719673415217490159891045368733251120]


def laplacian_moments(W, kmax):
    """m_k = <delta_0, (240 I - A)^k delta_0> from the closed-walk counts W_j."""
    return [sum(comb(k, j) * 240 ** (k - j) * (-1) ** j * W[j] for j in range(k + 1))
            for k in range(kmax + 1)]


def sector_moments(m, K):
    """Port-sector moments of the six-site clique, k = 0..K.

    Distinct clique sites differ by a root, so <delta_x, Delta^k delta_y> is
    c_k = m_k - m_{k+1}/240 for x != y. A unit contrast vector has m_k - c_k,
    the unit uniform vector m_k + 5 c_k, a single site m_k.
    """
    return {"V5 contrast": [Fraction(m[k + 1], 240) for k in range(K + 1)],
            "V1 uniform": [6 * Fraction(m[k]) - Fraction(m[k + 1], 48) for k in range(K + 1)],
            "site (script V2)": [Fraction(m[k]) for k in range(K + 1)]}


def chebyshev(M):
    """Chebyshev algorithm on all of M_0..M_L: (alpha, beta^2, k_fail).

    beta^2_k comes out for 2k <= L and alpha_k for 2k + 1 <= L. k_fail is the
    first step with beta^2_k <= 0 (a leading Hankel minor of M is not positive),
    or None.
    """
    L = len(M) - 1
    cur = [Fraction(x) for x in M]
    prev = [Fraction(0)] * (L + 1)
    alpha, b2 = [cur[1] / cur[0]], [Fraction(0)]
    k = 1
    while 2 * k <= L:
        nxt = [Fraction(0)] * (L + 1)
        for j in range(k, L - k + 1):
            nxt[j] = cur[j + 1] - alpha[k - 1] * cur[j] - b2[k - 1] * prev[j]
        bk = nxt[k] / cur[k - 1]
        if bk <= 0:
            return alpha, b2[1:], k
        b2.append(bk)
        if 2 * k + 1 <= L:
            alpha.append(nxt[k + 1] / nxt[k] - cur[k] / cur[k - 1])
        prev, cur = cur, nxt
        k += 1
    return alpha, b2[1:], None


def eigen_count_below(alpha, b2, x):
    """Sturm count of eigenvalues of the Jacobi matrix (alpha, b2) below x."""
    cnt, d = 0, None
    for k, a in enumerate(alpha):
        d = a - x if k == 0 else a - x - b2[k - 1] / d
        if d == 0:
            d = Fraction(1, 10 ** 80)
        cnt += d < 0
    return cnt


def hausdorff(M):
    """Hankel positivity of M, xM, (B - x)M and x(B - x)M as far as M reaches."""
    B = BAND
    seqs = {"M": M, "xM": M[1:], "(256-x)M": [B * M[k] - M[k + 1] for k in range(len(M) - 1)],
            "x(256-x)M": [B * M[k + 1] - M[k + 2] for k in range(len(M) - 2)]}
    out = {}
    for name, s in seqs.items():
        out[name] = {"order": (len(s) - 1) // 2 + 1, "fails_at": chebyshev(s)[2]}
    return out


def gauss_value(M, n, s):
    """n-node Gauss value of int dSigma/(s + x) from M_0..M_{2n-1}."""
    a, b2, _ = chebyshev(M[:2 * n])
    r = Fraction(0)
    for k in range(n - 1, -1, -1):
        r = (b2[k - 1] if k else 1) / (s + a[k] - r)
    return Fraction(M[0]) * r


def lobatto_value(M, n, s):
    """(n+1)-node Lobatto value (nodes 0 and B pinned) from M_0..M_{2n-1}."""
    B = BAND
    Mt = [B * M[k + 1] - M[k + 2] for k in range(2 * n - 2)]
    gt = gauss_value(Mt, n - 1, s) if n > 1 else Fraction(0)
    return ((B + s) * Fraction(M[0]) - M[1] - gt) / (s * (B + s))


def envelopes(M, n, s):
    return gauss_value(M, n, s), lobatto_value(M, n, s)


def script_loewner(M):
    """The court's own certificate, rebuilt: N_ord = 3, 'G_true' = 7-node Gauss,
    R6 remainder slopes between s = 100 and 100.001."""
    s1, s2 = Fraction(100), Fraction(100001, 1000)

    def R6(s, G):
        return s ** 6 * (G - sum((-1) ** k * Fraction(M[k]) / s ** (k + 1) for k in range(6)))

    gm1, _ = envelopes(M, 3, s1)
    _, gp2 = envelopes(M, 3, s2)
    gt1, gt2 = gauss_value(M, 7, s1), gauss_value(M, 7, s2)
    bad = (R6(s1, gm1) - R6(s2, gp2)) / (s2 - s1)
    good = (R6(s1, gt1) - R6(s2, gt2)) / (s2 - s1)
    return float(bad), float(good)


def cauchy_code(q=11, x=(0, 1, 2), y=(3, 4, 5, 6, 7, 8)):
    A = [[pow((xi - yj) % q, q - 2, q) for yj in y] for xi in x]
    return [[int(i == j) for j in range(3)] + A[i] for i in range(3)]


def mds_check(G, q=11):
    def det3(cols):
        a, b, c = cols
        return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
                + a[2] * (b[0] * c[1] - b[1] * c[0])) % q
    n = len(G[0])
    minors = [det3([[G[r][c] for r in range(3)] for c in cs]) for cs in combinations(range(n), 3)]
    msg = [4, 9, 2]
    code = [sum(msg[r] * G[r][c] for r in range(3)) % q for c in range(n)]
    recv = list(code)
    for c, e in ((1, 5), (4, 8), (7, 3)):
        recv[c] = (recv[c] + e) % q
    dec = [list(m) for m in product(range(q), repeat=3)
           if sum(sum(m[r] * G[r][c] for r in range(3)) % q != recv[c] for c in range(n)) <= 3]
    return len(minors), all(minors), dec == [msg]


def observation_rank():
    """Two overlapping 6-port blocks on Sym(8) (order U2 + V4 + V2), then 4 polarizations."""
    basis = [(i, j) for i in range(8) for j in range(i, 8)]

    def row(f):
        return [f(i, j) for i, j in basis]

    rows = []
    for lo, hi in ((0, 6), (2, 8)):
        for a in range(lo, hi):
            for b in range(a, hi):
                rows.append(row(lambda i, j, a=a, b=b: float((i, j) == (a, b))))
    O = np.array(rows)
    rO = np.linalg.matrix_rank(O)
    ker = [(i, j) for k, (i, j) in enumerate(basis) if not O[:, k].any()]
    pol = []
    for u, v in product(range(2), repeat=2):
        p = np.zeros(8)
        p[u], p[6 + v] = 1, 1
        pol.append(row(lambda i, j, p=p: p[i] * p[j] * (1 if i == j else 2)))
    return rO, ker, np.linalg.matrix_rank(np.vstack([O, pol]))


def c5_isotypic():
    """C5 on the six clique sites (apex fixed): orthonormal bases of the trivial, rho_1, rho_2 parts."""
    S = native.boundary_rotation()
    pw = [np.linalg.matrix_power(S, k) for k in range(5)]
    parts = {"trivial": sum(pw) / 5}
    for j in (1, 2):
        parts[f"rho_{j}"] = 2 / 5 * sum(np.cos(2 * np.pi * j * k / 5) * pw[k] for k in range(5))
    out = {}
    for name, Pj in parts.items():
        w, V = np.linalg.eigh((Pj + Pj.T) / 2)
        B = V[:, w > 0.5]
        out[name] = (B, B.T @ S @ B)
    return out


def doublet_action():
    """C5 (vertex 5-cycle) on the 8^2 eigenspace of D^2 on the 15 atoms."""
    M = np.array(carrier.signless_incidence(), float)
    D = np.array(carrier.dirac(M), float)
    w, V = np.linalg.eigh(D @ D)
    E8 = V[:, np.isclose(w, 8)]
    E = carrier.edges()
    idx = {e: k for k, e in enumerate(E)}
    p = (1, 2, 3, 4, 0)
    P = np.zeros((15, 15))
    for i in range(5):
        P[p[i], i] = 1
    for k, (i, j) in enumerate(E):
        P[5 + idx[tuple(sorted((p[i], p[j])))], 5 + k] = 1
    return E8.T @ P @ E8, np.allclose(P @ D, D @ P)


def hom_dim(RU, RV):
    """dim {B : RU B = B RV}."""
    n, m = len(RU), len(RV)
    L = np.kron(np.eye(m), RU) - np.kron(RV.T, np.eye(n))
    return n * m - np.linalg.matrix_rank(L, tol=1e-9)


def run():
    rep = Report("15-court")
    T, OB = gates.THEOREM, gates.OBSTRUCTION
    W = recurrence.load_walks()
    m = laplacian_moments(W, 52)

    # Stage 1
    A6 = 241 * np.eye(6) - np.ones((6, 6))
    BB = 183 * np.eye(6) + 52 * np.ones((6, 6))
    u = np.ones(6) / np.sqrt(6)
    c = np.r_[1, -1, 0, 0, 0, 0] / np.sqrt(2)
    vals = [float(c @ A6 @ c), float(u @ A6 @ u), float(c @ BB @ c), float(u @ BB @ u)]
    rep.add("U19.81 (5,2,1) sector eigenvalues: A_bb = 241 on V5, 235 on V1; BB* = 183 on V5, "
            "495 on V1", T, np.allclose(vals, [241, 235, 183, 495]), vals,
            note="matrices 241I - J and 183I + 52J are checked on the lattice in layer 3")
    sec = sector_moments(m, 50)
    rep.add("sector moments at k = 1 equal those eigenvalues: contrast m_2/240 = 241, uniform "
            "6 m_1 - m_2/48 = 235", T,
            sec["V5 contrast"][1] == 241 and sec["V1 uniform"][1] == 235
            and sec["V5 contrast"][0] == sec["V1 uniform"][0] == 1,
            [str(sec["V1 uniform"][k]) for k in range(4)])
    script_M1 = Fraction(6 * m[1], 6) - Fraction(5 * m[2], 1440)
    rep.add("U19.81 script: its uniform moment m_k - m_{k+1}/288 gives 39.17 at k = 1, not 235; "
            "its own assert fails", OB, script_M1 != 235, float(script_M1),
            note="corrected formula 6 m_k - m_{k+1}/48 (previous check)")
    agree = [n for n in range(len(SCRIPT_W)) if SCRIPT_W[n] == W[n]]
    rep.add("U19.81 script: its walk generator agrees with W_n only for n <= 3 "
            "(W_4: 7,772,208 printed, 1,260,720 true)", OB, agree == [0, 1, 2, 3],
            {"agree": agree, "W4_script": SCRIPT_W[4], "W4_true": W[4]})
    ms = laplacian_moments(SCRIPT_W, 16)
    fails = {name: chebyshev(M)[2]
             for name, M in (("contrast", [Fraction(ms[k + 1], 240) for k in range(16)]),
                             ("site", [Fraction(x) for x in ms]))}
    rep.add("U19.81 script: its moment sequences are not positive definite (Lanczos beta^2 <= 0 "
            "at step 3): no measure has them", OB, all(v == 3 for v in fails.values()), fails)
    haus = {k: hausdorff(M) for k, M in sec.items()}
    ok = all(v["fails_at"] is None for h in haus.values() for v in h.values())
    nodes_in = all(eigen_count_below(*chebyshev(M[:50])[:2], Fraction(0)) == 0
                   and eigen_count_below(*chebyshev(M[:50])[:2], Fraction(BAND)) == 25
                   for M in sec.values())
    rep.add("true sector moments M_0..M_50 pass the Hausdorff test on [0, 256]: Hankel forms of "
            "M, xM, (256-x)M, x(256-x)M positive definite (exact); 25 Gauss nodes in (0, 256)",
            T, ok and nodes_in, {k: {n: v["order"] for n, v in h.items()} for k, h in haus.items()})
    env = {}
    for name, M in sec.items():
        for s in (64, 128):
            gm, gp = envelopes(M, 25, Fraction(s))
            env[f"{name} s={s}"] = {"G-": float(gm), "G+": float(gp), "gap": float(gp - gm)}
    rep.add("Markov-Krein envelopes from M_0..M_49 (25-node Gauss G_-, 26-node Lobatto G_+ "
            "pinned at 0 and 256): 0 < G_+ - G_- at s = 64, 128 in every sector", T,
            all(0 < v["gap"] for v in env.values()), env,
            note="the script built these with N_ord = 3 (moments M_0..M_5), not M_0..M_50")
    rep.add("U19.81 Theorem 2 consequence: (G_-(s1), G_+(s2)) is not jointly realizable",
            T, all(0 < v["gap"] for v in env.values()),
            note="Markov-Krein: G_-(s1) is attained only by the Gauss measure, which forces "
                 "G(s2) = G_-(s2) < G_+(s2) (Krein-Nudelman, Markov moment problem, ch. III)")
    bad, good = script_loewner(sec["V5 contrast"])
    rep.add("U19.81 script certificate fails on true moments: the 'incompatible' cross choice "
            "also has positive R6 Loewner slope", OB, bad > 0 and good > 0,
            {"cross_slope": bad, "gauss_slope": good},
            note="R6(s) = int x^6 dSigma/(s+x) decreases for every positive measure; over "
                 "ds = 0.001 the slope swamps the envelope gap")

    # Stage 2
    n_minors, all_nonzero, unique = mds_check(cauchy_code())
    rep.add("U19.81 Stage 2: [9,3,7]_11 Cauchy code [I | A]: all 84 3x3 minors nonzero, a "
            "3-error word decodes uniquely (exhaustive over 1331 messages)", T,
            n_minors == 84 and all_nonzero and unique)
    rep.add("identification of H90 with that code", gates.UNFORMED, True,
            note="any Cauchy matrix with distinct nodes gives an MDS code; no operand in the "
                 "canon or this repository selects this one")

    # Stage 3
    rO, ker, rfull = observation_rank()
    rep.add("U19.81 Stage 3: two overlapping 6-port blocks on Sym(8) have rank 32; ker O is "
            "the 4-dim U2 x V2 cross block; 4 polarizations complete it (rank 36)", T,
            rO == 32 and len(ker) == 4 and all(i < 2 and j >= 6 for i, j in ker) and rfull == 36,
            {"rank_O": int(rO), "ker": ker, "rank_completed": int(rfull)})
    R8, commutes = doublet_action()
    iso = c5_isotypic()
    dims = {name: int(hom_dim(RU, R8)) for name, (B, RU) in iso.items()}
    same = int(hom_dim(iso["rho_1"][1], iso["rho_1"][1]))
    rep.add("U19.81 clock reduction to 2 parameters fails: C5 acts as the identity on the 8^2 "
            "doublet of D^2 (and on any C5-invariant 2-site probe), so dim Hom_C5(V2, U2) is 0 "
            "for U2 = rho_1, rho_2 and 4 for trivial U2", OB,
            commutes and np.allclose(R8, np.eye(2))
            and dims == {"trivial": 4, "rho_1": 0, "rho_2": 0} and same == 2,
            {"Hom(V2, U2)": dims, "Hom(rho_1, rho_1)": same},
            note="the 2-parameter case needs U2 = V2 = rho_j; C5 has prime order, so its "
                 "orbits on lattice sites have 1 or 5 points and a 2-site probe is trivial")

    # Stage 4
    a, Om, x = sp.symbols("a Omega x", positive=True)
    w = Om * sp.sqrt(x)
    rep.add("U19.81 Stage 4: omega = Omega_* sqrt(x) is homogeneous in Omega_*: the spectrum "
            "fixes no clock scale (TIME_BIND stays UNBOUND)", T,
            sp.simplify(w.subs(Om, a * Om) / w - a) == 0)
    rep.add("U19.81 'complete expanded scalar polynomial annihilator' for W_n",
            gates.UNFORMED, True,
            note="not given in the court or its script; layer 14 forms one mod four primes "
                 "(order 16, degree 58); its rational coefficients are not reconstructed")

    # Remarks of the same message
    Tm = literal.load()["T_OMSOON293"]
    C = Tm.adjugate().T
    mx = max(abs(v) for v in C)
    minors = {k: {abs(Tm.extract(list(r), list(cc)).det())
                  for r in combinations(range(6), k) for cc in combinations(range(6), k)}
              for k in range(1, 6)}
    row4 = [C[3, j] for j in range(6)]
    rep.add("literal 6x6 adapter: largest |cofactor| = 68; no minor of size <= 5 equals 155 or "
            "4805; 4805 = sum of the squared row-4 cofactors 21^2+48^2+43^2+11^2+3^2+9^2", T,
            mx == 68 and all(155 not in s and 4805 not in s for s in minors.values())
            and sum(v * v for v in row4) == 4805 == (Tm * Tm.T).cofactor(3, 3),
            {"max_cofactor": int(mx), "row4": [int(v) for v in row4]},
            note="so 'cofactor 4805' supplies no five-dimensional operand")
    rep.add("the missing five-dimensional operand", gates.UNFORMED, True,
            note="not a minor or cofactor of the literal adapter; still absent")
    rep.add("preparation time >= eps^(-1/2) (monopole families) or eps^(-1/3) (dipole target) "
            "for a port budget polynomial in 1/eps", gates.REPORTED, True,
            note="necessary condition from the sibling's preparation argument; constants under "
                 "check there; no matching preparation protocol yet")
    rep.add("sibling scalar replay: all 33 support groups pass; twelve exclusion regions give "
            "(r+1)(d+2) >= 195", gates.REPORTED, True,
            note="independently replayed and strengthened in layer 14")
    return rep
