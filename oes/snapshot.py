"""Layer 18. The 14:16 snapshot (one-machine-20261028, oes-model-20261028), rebuilt.

The sibling snapshot was saved to Drive at 14:16 UTC on 28 Oct. It adds the
cube, the 24-step readout, two Hankel matrices, the Spanda action on the 31
subsets, the frequency squares on the 4320-circle and the Agni-clock-doubling
chain. Its TypeScript audits mostly compare typed constants (`251 === 251`).
Here each item is recomputed from matrices, and three items the snapshot left
open are settled:

* density on the nine-torus. The nine positive critical energies of the bath
  have distinct square-free parts, so by Besicovitch their square roots are
  linearly independent over Q. The flow of the nine bath frequencies is
  therefore dense on T^9 (Kronecker);
* the Hessians. All eleven critical families are recomputed (layer 16), and
  their coherent coefficients count * i^index / sqrt|det H| reproduce the ten
  values printed in the snapshot paper;
* the walk asymptotics. Laplace's method at the maximum, using only the
  7-design moments of the E8 roots, gives
  W_n = (16/pi^4) 240^n n^-4 (1 - 2/n + (23/15)/n^2 + O(n^-3)),
  and the exact W_n of layer 14 follow it.

It also identifies Agni = 5I - G with the light operator Curl^2 of layer 17.
"""

import itertools
from fractions import Fraction
from math import gcd

import mpmath as mp
import numpy as np
import sympy as sp

from . import carrier, gates, handover, recurrence, waves
from .record import Report

# coherent coefficients printed in the snapshot paper (count * i^index / sqrt|det H|), magnitudes
PRINTED_COHERENT = {
    "E8": sp.Rational(1, 12960000), "E7+A1": 5 * sp.sqrt(39) / 11232, "E6+A2": sp.Rational(40, 81),
    "D5+A3": 105 * sp.sqrt(3) / 16, "A4+A4": sp.Rational(48384, 625), "A5+A2+A1": 1120 * sp.sqrt(3) / 9,
    "A6+A1": 16777216 * sp.sqrt(15) / 234375, "A7": 4782969 * sp.sqrt(15) / 156250,
    "A8": sp.Rational(640, 27), "A7+A1": sp.Rational(135, 4), "D8": sp.Rational(135, 256),
}
CUBE_LABELS = ["580", "085", "980", "089", "570", "075", "970", "079"]


def squarefree_part(q):
    """Square-free d with sqrt(q) in Q * sqrt(d), for a positive rational q."""
    q = sp.Rational(q)
    n = int(q.p * q.q)
    return int(sp.prod([p for p, e in sp.factorint(n).items() if e % 2]))


def bath_frequencies():
    fam = handover.critical_census()
    eps = {Fraction(240 - f["lambda"]).limit_denominator(1000) for f in fam.values()} - {0}
    return [sp.Rational(e.numerator, e.denominator) for e in sorted(eps)]


def independence_certificate(eps):
    """Prime-exponent vectors of the square-free parts over F_2: distinct vectors are
    distinct characters of Gal(Q(sqrt p : p)/Q), hence Q-independent square roots."""
    parts = [squarefree_part(e) for e in eps]
    primes = sorted({p for d in parts for p in sp.factorint(d)})
    vecs = [tuple(int(d % p == 0) for p in primes) for d in parts]
    return parts, primes, vecs


def hessians():
    """(type, lambda, count, index, det H_eps in k-coordinates) for the eleven families."""
    R = handover.e8_roots()
    V = handover.alcove_vertices()
    fam = handover.critical_census()
    pts = {}

    def grad(x):
        return 2 * np.pi * np.sin(2 * np.pi * R @ x) @ R

    def add(x):
        lam = float(np.cos(2 * np.pi * R @ x).sum())
        typ, _ = handover.stabiliser(R, x)
        pts.setdefault((round(lam, 8), typ), x)

    from scipy.optimize import brentq
    for v in V:
        add(v)
    t = np.linspace(1e-4, 1 - 1e-4, 2001)
    for va, vb in itertools.combinations(V, 2):
        d = vb - va
        X = va[None, :] + t[:, None] * d[None, :]
        g = (np.sin(2 * np.pi * X @ R.T) @ R) @ d
        for k in np.nonzero(np.sign(g[:-1]) != np.sign(g[1:]))[0]:
            t0 = brentq(lambda s: grad(va + s * d) @ d, t[k], t[k + 1], xtol=1e-15)
            if np.linalg.norm(grad(va + t0 * d)) < 1e-7:
                add(va + t0 * d)
    out = []
    for key, x in pts.items():
        H = (R.T * np.cos(2 * np.pi * R @ x)) @ R
        w = np.linalg.eigvalsh(H)
        out.append((key[1], key[0], fam[key]["orbit"], int((w < 0).sum()), float(np.linalg.det(H))))
    return out


def laplace_coefficients():
    """Coefficients of W_n n^4 / ((16/pi^4) 240^n) = 1 + c1/n + c2/n^2 + ... from the 7-design moments."""
    s, n = sp.symbols("s n", positive=True)                  # s = |k|^2
    eps = 30 * s - sp.Rational(3, 2) * s**2 + s**3 / 24     # exact through |k|^6 (7-design)
    logl = sp.series(sp.log(1 - eps / 240), s, 0, 4).removeO()
    a1, a2, a3 = [logl.coeff(s, j) for j in (1, 2, 3)]
    d, var = 8, -1 / (2 * a1 * n)                            # Gaussian exp(n a1 s): variance per coordinate

    def Es(m):                                               # E[|k|^(2m)] for the 8-dim Gaussian
        return sp.prod([d + 2 * j for j in range(m)]) * var**m

    c1 = sp.simplify(n * a2 * Es(2) * n)
    c2 = sp.simplify((n * a3 * Es(3) + sp.Rational(1, 2) * (n * a2)**2 * Es(4)) * n**2)
    return a1, a2, a3, c1, c2


def cube():
    bits = [(int(l[0] == "0"), int("9" in l), int("7" in l)) for l in CUBE_LABELS]
    A = np.array([[int(sum(a != b for a, b in zip(u, v)) == 1) for v in bits] for u in bits])
    L = 3 * np.eye(8) - A
    middle = L @ (6 * np.eye(8) - L)

    def observe(readers):
        F = np.eye(8)[readers]
        r0 = np.linalg.matrix_rank(F @ middle)
        r1 = np.linalg.matrix_rank(np.vstack([F @ middle, (F @ A) @ middle]))
        return r0, r1

    third = {k: observe([0, 1, k])[1] for k in range(2, 8)}
    dec = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
                    [3, -1, -1, 0, -1, 0], [-1, 3, 0, -1, 0, -1], [0, 0, 3, 0, 0, 1]])
    eight = np.array([[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
                      [-1, 3, 3, 0, -1, -1], [3, -1, -1, -1, 0, 0], [0, 0, -3, 0, 0, 1],
                      [0, -3, 0, 0, 1, 0], [-3, 0, 0, 1, 0, 0]])
    inv = np.linalg.inv(dec)
    return {"spectrum": sorted(np.round(np.linalg.eigvalsh(L), 9).tolist()),
            "middle_sq_is_8_middle": bool(np.allclose(middle @ middle, 8 * middle)),
            "middle_rank": int(np.linalg.matrix_rank(middle)), "pair": observe([0, 1]),
            "third": third, "decoder_det": round(float(np.linalg.det(dec)), 9),
            "decoder_inverse_integral": bool(np.allclose(inv, np.round(inv))),
            "six_noise": round(float((inv ** 2).sum()), 9), "eight_noise": int((eight ** 2).sum())}


def spanda():
    """The involution 1 <-> 4, 2 <-> 3 (5 fixed) on the 31 nonempty subsets of five points."""
    swap = {0: 3, 3: 0, 1: 2, 2: 1, 4: 4}
    subsets = [frozenset(i for i in range(5) if m >> i & 1) for m in range(1, 32)]
    idx = {s: k for k, s in enumerate(subsets)}
    S = np.zeros((31, 31))
    for s in subsets:
        S[idx[frozenset(swap[i] for i in s)], idx[s]] = 1
    tr = [int(round(np.trace(np.linalg.matrix_power(S, k)))) for k in range(4)]
    H = np.array([[tr[0], tr[1]], [tr[1], tr[2]]])
    P = (np.eye(31) + S) / 2
    return S, tr, int(round(np.linalg.det(H))), P


def order(step, modulus=4320):
    return modulus // gcd(step, modulus)


def run():
    rep = Report("18-snapshot")
    T, AR, SR, OB, RP, CD = (gates.THEOREM, gates.ARITHMETIC, gates.SELECTED_REFERENCE,
                             gates.OBSTRUCTION, gates.REPORTED, gates.CONDITIONAL)

    eps = bath_frequencies()
    parts, primes, vecs = independence_certificate(eps)
    rep.add("the nine positive critical energies of the bath are 224, 243, 248, 250, 251, 4025/16, "
            "6800/27, 252, 256 (layer 16 census; the two families at 252 share one)", T,
            eps == sorted([224, 243, 248, 250, 251, sp.Rational(4025, 16), sp.Rational(6800, 27),
                           252, 256]), [str(e) for e in eps])
    rep.add("density on the nine-torus: the square-free parts 14, 3, 62, 10, 251, 161, 51, 7, 1 are "
            "distinct, so the nine frequencies sqrt(eps) are linearly independent over Q and their "
            "flow is dense on T^9", T,
            sorted(parts) == sorted([14, 3, 62, 10, 251, 161, 51, 7, 1]) and len(set(vecs)) == 9,
            {"square-free parts": parts, "primes": primes},
            note="Besicovitch 1940: distinct square-free d give Q-independent sqrt d (distinct "
                 "characters of Gal(Q(sqrt 2, sqrt 3, ..., sqrt 251)/Q)); Kronecker then gives "
                 "density. The snapshot left this open")

    hs = hessians()
    ok_c, ok_sign, table = True, True, {}
    for typ, lam, count, ind, det in hs:
        coef = count / np.sqrt(abs(det))
        ok_c &= bool(np.isclose(coef, float(PRINTED_COHERENT[typ]), rtol=1e-9))
        ok_sign &= (det > 0) == (ind % 2 == 0)
        table[typ] = {"lambda": round(lam, 6), "count": count, "index": ind, "det": det}
    rep.add("Hessians of the eleven critical families recomputed: sign det = (-1)^index, and "
            "count * i^index / sqrt|det H| reproduces the snapshot's printed coherent coefficients", T,
            ok_c and ok_sign and len(hs) == 11
            and any(t == "E8" and np.isclose(d, 60.0 ** 8) for t, _, _, _, d in hs), table,
            note="det 60^8 at the maximum, 3^8 (A8), 2^16 (A7+A1, D8), 5^8 (A4+A4); the snapshot "
                 "said the Hessians were not recomputed")

    a1, a2, a3, c1, c2 = laplace_coefficients()
    W = recurrence.load_walks()
    mp.mp.dps = 60
    errs = {}
    for n in (50, 60, 70, 80, 90):
        Rn = mp.mpf(W[n]) * n ** 4 * mp.pi ** 4 / (16 * mp.mpf(240) ** n)
        errs[n] = float((Rn - 1 - mp.mpf(int(c1)) / n) * n ** 2 - mp.mpf(c2.p) / c2.q)
    seq = [abs(errs[n]) for n in sorted(errs)]
    rep.add("walk asymptotics from the 7-design alone: W_n = (16/pi^4) 240^n n^-4 (1 - 2/n + "
            "(23/15)/n^2 + O(n^-3)), and the exact W_50..W_90 follow it", T,
            (a1, a2, a3) == (sp.Rational(-1, 8), sp.Rational(-1, 640), sp.Rational(-1, 23040))
            and c1 == -2 and c2 == sp.Rational(23, 15)
            and all(abs(errs[n]) < 0.5 / n for n in errs) and seq == sorted(seq, reverse=True),
            {str(n): e for n, e in errs.items()},
            note="log(1 - eps/240) = -s/8 - s^2/640 - s^3/23040 with s = |k|^2; the error column "
                 "is ((R_n - 1 + 2/n) n^2 - 23/15), shrinking like 1/n")

    B = carrier.signed_incidence()
    G = B.T * B
    agni = 5 * sp.eye(10) - G
    d0, d1, star, curl = waves.complex_ops()
    rep.add("Agni = 5I - G is the light operator: Agni = Curl^2 = d1^T d1, G = d0 d0^T is the sound "
            "operator, Agni^2 = 5 Agni, and Agni + G = 5I (layer 17)", T,
            agni == curl * curl == d1.T * d1 and G == d0 * d0.T and agni * agni == 5 * agni)
    Td = sp.zeros(10, 20)
    for i in range(10):
        Td[i, 2 * i], Td[i, 2 * i + 1] = 1, -1
    sig = sp.diag(*[(-1) ** c for c in range(20)])
    rep.add("edge doubling T (10 x 20): T T^T = 2I, every row null for the pair signature, and "
            "rank B T = rank B = 4", T,
            Td * Td.T == 2 * sp.eye(10) and all((Td[i, :] * sig * Td[i, :].T)[0] == 0 for i in range(10))
            and (B * Td).rank() == 4,
            note="true and immediate: T has full row rank")

    A4 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, sp.Rational(1, 3)], [-2, 1, 0, 0], [1, -2, 0, 0]])
    b, c = sp.eye(4)[:, 2], sp.eye(4)[:, 1]
    mom = [(c.T * A4 ** k * b)[0] for k in range(8)]
    Hk = sp.Matrix(4, 4, lambda r, q: mom[r + q])
    Cn = sp.Matrix.hstack(*[A4 ** k * b for k in range(4)])
    On = sp.Matrix.vstack(*[c.T * A4 ** k for k in range(4)])
    x = sp.symbols("x")
    rep.add("five-port site block: moments 0, 0, 0, 1/3, 0, -8/9, 0, 55/27 (input p1, output q2), "
            "H_{k+4} + (8/3) H_{k+2} + H_k = 0, controllability det -1/3, observability "
            "det -1/27, Hankel det 1/81 (6561 cleared by 27), frequencies^2 (4 +- sqrt7)/3", SR,
            mom == [0, 0, 0, sp.Rational(1, 3), 0, sp.Rational(-8, 9), 0, sp.Rational(55, 27)]
            and A4 ** 4 + sp.Rational(8, 3) * A4 ** 2 + sp.eye(4) == sp.zeros(4, 4)
            and Cn.det() == sp.Rational(-1, 3) and On.det() == sp.Rational(-1, 27)
            and Hk.det() == sp.Rational(1, 81) and (27 * Hk).det() == 6561
            and sp.expand(3 * A4.charpoly(x).as_expr()) == 3 * x ** 4 + 8 * x ** 2 + 3,
            note="a selected site (masses 1, 3; springs [[2,-1],[-1,2]]), not a canon operand")

    cb = cube()
    rep.add("cube: the eight labels 580..079 are the 3-cube; Laplacian spectrum 0, 2^3, 4^3, 6; the "
            "middle operator L(6I - L) satisfies M^2 = 8M with rank 6; readers 580, 085 see ranks 2 "
            "then 4; four third readers reach 6 and two stay at 4; the decoder has det -1, an integral "
            "inverse, noise gain 46, and the eight-label gain is 66", T,
            cb["spectrum"] == [0.0, 2.0, 2.0, 2.0, 4.0, 4.0, 4.0, 6.0] and cb["middle_sq_is_8_middle"]
            and cb["middle_rank"] == 6 and cb["pair"] == (2, 4)
            and sorted(cb["third"].values()) == [4, 4, 6, 6, 6, 6] and cb["decoder_det"] == -1
            and cb["decoder_inverse_integral"] and cb["six_noise"] == 46 and cb["eight_noise"] == 66,
            {k: v for k, v in cb.items() if k != "spectrum"})

    S, tr, hdet, P = spanda()
    fixed = int(sum(S[k, k] for k in range(31)))
    rep.add("Spanda on the 31 nonempty subsets: 7 fixed, 24 moved; return traces 31, 7, 31, 7; the "
            "2x2 trace Hankel has det 912; W0 = 360000 I commutes", T,
            fixed == 7 and tr == [31, 7, 31, 7] and hdet == 912)
    rank_p = int(round(np.trace(P)))
    rep.add("snapshot: '(I + S)/2 is the Markov projector onto those 7 forms' fails: it is a Markov "
            "projector, but of rank 19 (7 fixed subsets + 12 symmetrized pairs), not 7", OB,
            np.allclose(P @ P, P) and np.allclose(P.sum(0), 1) and rank_p == 19, rank_p,
            note="the snapshot's own count 31 = 19 + 12, 7 = 19 - 12 has the 19")
    Ps, Pl, Hp, Hm, _ = waves.projectors()
    E = waves.edge_action((3, 2, 1, 0, 4))
    trs = {"sound": float(np.trace(E @ Ps)), "helicity+": float(np.trace(E @ Hp)),
           "helicity-": float(np.trace(E @ Hm))}
    rep.add("Spanda on the K5 edges (new join): the double transposition is even, so it keeps both "
            "helicities; its traces are 0 on sound and -1 on each helicity (A5 characters of 4, 3, 3')",
            T, np.allclose(E @ Hp @ E.T, Hp) and np.allclose(list(trs.values()), [0, -1, -1]), trs)

    day, pada, signs, rotor = order(180), order(40), order(360), order(864)
    rep.add("4320-circle: the day (step 180) has order 24, the pada (step 40) 108, they meet in the "
            "order-12 step 360, and the order-5 rotor (step 864) meets the day only at 0", AR,
            (day, pada, signs, rotor) == (24, 108, 12, 5) and gcd(24, 108) == 12 and gcd(5, 24) == 1)
    sq = [3, 4, 5, 8, 16]
    rep.add("frequency squares 3, 4, 5, 8, 16 (carrier, source, sound = light, carrier, port) divide "
            "4320 in steps 1440, 1080, 864, 540, 270; no positive bath energy divides 4320; 4b^2 = 5a^2 "
            "has no positive solution (source and sound incommensurable)", AR,
            [4320 // q for q in sq] == [1440, 1080, 864, 540, 270] and all(4320 % q == 0 for q in sq)
            and not any(e.q == 1 and 4320 % int(e) == 0 for e in eps) and not sp.sqrt(5).is_rational)

    dat, _ = recurrence.load_operator()
    band = sum(m for r, m in dat["characteristic_roots"].items() if -16 <= sp.Rational(r) <= 240)
    rep.add("snapshot paper, front table 'the recurrence order is 11': the operator of layer 14 has "
            "order 16; 11 is the degree of its in-band characteristic part, which contains (z+12)^2",
            OB, dat["order"] == 16 and band == 11)
    rep.add("discrete Maxwell on the K5 2-complex", CD, True,
            note="layer 17's light sector is a Maxwell system (E on edges, F on triangles, omega = "
                 "sqrt5); physical Maxwell needs DYN_BIND, as the snapshot says")
    rep.add("not formed in the snapshot: GKSL, SI, BRST, BV, Einstein-Hilbert, the historical "
            "BassForge file, Sawan's intertwiner, the six absent operands", RP, True,
            note="none of them is built here either")
    return rep
