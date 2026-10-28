"""Layer 14. The scalar walk recurrence: which shapes are excluded.

A P-recurrence of order r and degree d is sum_{j<=r} p_j(n) W_{n+j} = 0 with
deg p_j <= d. The canon proves an eventual recurrence holds for every n >= 0
(all-prime congruences), so the exact matrix

    V[n, (j, k)] = n^k W_{n+j},   n = 0..N-r,  j = 0..r,  k = 0..d,

decides it. Full column rank modulo a prime p implies full rank over Q, and
then no recurrence of that shape exists. Only residues W_n mod p are needed for
this, which is what the D8 + spinor engine (oes/walkfast.py) computes far past
the Weyl-orbit DP.

The excluded region is a down-set. A recurrence of shape (r, d) is also one of
shape (r+1, d) and of shape (r, d+1). So it is enough to test the maximal
decidable shapes, the corners of (r+1)(d+2) <= N+2, and there are about
2 sqrt(N) of them. The canon's standing bound (28 Oct) is (r+1)(d+2) > 85.

With W_0..W_600 mod p the first kernels appear, at product (r+1)(d+2) = 456,
shape (23, 17). The kernels are recurrences, and their greatest common right
divisor (oes/ore.py) is one operator of order 16 and degree 58, the same mod
four primes. Built from W_0..W_500 it also annihilates W_501..W_600. Its
characteristic polynomial factors over Q into the 16 growth rates

    240, 16, -3, -8, -10, -11, -185/16, -320/27, -12 (twice), -16   in the band [-16, 240],
    340, -660, -20, -35, -120/7                                     outside it,

with local exponent -4 = -dim/2 at every simple root and (alpha+4)(alpha+5) at
-12. The rational coefficients are not reconstructed yet, and no proof is given
that the operator annihilates W_n for every n.
"""

import json
from pathlib import Path

import numpy as np

import sympy as sp

from . import gates, ore
from .record import Report

ROOT = Path(__file__).resolve().parent.parent
P = 2147483629


def load_walks():
    """The longest exact sequence on file (W_0..W_90 from the Weyl-orbit DP)."""
    best = None
    for name in ("walks90.json", "walks.json"):
        f = ROOT / "data" / name
        if f.exists():
            W = [int(x) for x in json.loads(f.read_text())["W"]]
            if best is None or len(W) > len(best):
                best = W
    return best


def load_modp():
    """{p: [W_n mod p]} from data/walks_modp.json (the D8 + spinor engine)."""
    f = ROOT / "data" / "walks_modp.json"
    if not f.exists():
        return {}
    d = json.loads(f.read_text())
    return {int(p): [int(x) for x in W] for p, W in d["W_mod_p"].items()}


def load_operator():
    """The order-16 annihilator mod each prime, from data/recurrence_modp.json."""
    d = json.loads((ROOT / "data" / "recurrence_modp.json").read_text())
    ops = {int(p): [np.array(c, dtype=np.int64) for c in L]
           for p, L in d["operators_mod_p"].items()}
    return d, ops


def rank_mod_p(A, p=P):
    """Rank over F_p by row echelon form (p < 2^31, so products fit in int64)."""
    A = np.array(A, dtype=np.int64) % p
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        if r == rows:
            break
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0:
            continue
        piv = r + nz[0]
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        A[r, c:] = A[r, c:] * pow(int(A[r, c]), -1, p) % p
        f = A[r + 1:, c].copy()
        if f.any():
            A[r + 1:, c:] = (A[r + 1:, c:] - np.outer(f, A[r, c:]) % p) % p
        r += 1
    return r


def shape_matrix(W, r, d, p=P):
    N = len(W) - 1
    rows = N - r + 1
    Wm = np.array([w % p for w in W], dtype=np.int64)
    n = np.arange(rows, dtype=np.int64)
    npow = np.ones((d + 1, rows), dtype=np.int64)
    for k in range(1, d + 1):
        npow[k] = npow[k - 1] * n % p
    V = np.zeros((rows, (r + 1) * (d + 1)), dtype=np.int64)
    for j in range(r + 1):
        for k in range(d + 1):
            V[:, j * (d + 1) + k] = npow[k] * Wm[j:j + rows] % p
    return V


def excluded(W, r, d, p=P):
    """True if the data exclude every recurrence of order r, degree d."""
    V = shape_matrix(W, r, d, p)
    if V.shape[0] < V.shape[1]:
        return None                       # underdetermined: data cannot decide
    return rank_mod_p(V, p) == V.shape[1]


def corners(N, K=None):
    """Maximal shapes (r, d) with (r+1)(d+2) <= K (default K = N+2, all decidable shapes)."""
    K = N + 2 if K is None else K
    out = []
    for r in range(1, N // 2 + 1):
        d = K // (r + 1) - 2
        if d < 0:
            break
        if K // (r + 2) - 2 < d:
            out.append((r, d))
    return out


def frontier(W, p=P):
    """For each order r, the largest degree the data exclude, and any kernel shapes.

    Corners are tested first. A corner that is not excluded is a candidate
    recurrence; below it the degrees are scanned down to the largest excluded one.
    """
    N = len(W) - 1
    cs = corners(N)
    status = {c: excluded(W, *c, p=p) for c in cs}
    kernels = [c for c, e in status.items() if not e]
    out = {}
    for r in range(1, N // 2 + 1):
        dmax = (N + 2) // (r + 1) - 2
        if dmax < 0:
            break
        cover = min((c for c in cs if c[0] >= r and c[1] >= dmax), key=lambda c: c[0])
        if status[cover]:
            out[r] = dmax
        else:
            d = dmax
            while d >= 0 and not excluded(W, r, d, p):
                d -= 1
            out[r] = d
    return out, kernels


def run():
    rep = Report("14-recurrence")
    W = load_walks()
    N = len(W) - 1
    from . import walkfast, walks
    canon = [int(x) for x in json.loads((ROOT / "data" / "canon_walks_0_55.json").read_text())["W"]]
    rep.add("W_0..W_55 of the canon ledger replayed exactly by the Weyl-orbit engine "
            "(incl. W_25..W_55, never independently regenerated before)", gates.THEOREM,
            W[:56] == canon, {"terms_compared": 56, "mismatches": sum(a != b for a, b in zip(W, canon))})
    fresh = walks.Engine(nprimes=8).walk_counts(12)
    rep.add("stored walk file re-derived in-suite for W_0..W_24", gates.THEOREM,
            fresh == W[:25])
    rep.add(f"new exact terms W_56..W_{N} (W(E8) dominant-weight DP, CRT)", gates.THEOREM,
            N >= 90 and all(W[n] % 240 == 0 for n in range(1, N + 1)), N)
    canon_cases = [(5, 2), (10, 2), (12, 2), (10, 3)]
    rep.add(f"canon exclusions (5,2), (10,2), (12,2), (10,3) replayed on W_0..W_{N}",
            gates.THEOREM, all(excluded(W, r, d) for r, d in canon_cases))
    fr, kernels = frontier(W)
    rep.add(f"exact data-only bound from W_0..W_{N}: every recurrence has (r+1)(d+2) > {N + 2}",
            gates.THEOREM, not kernels, {"corners_tested": len(corners(N)), "kernels": kernels},
            note=f"canon standing bound (r+1)(d+2) > 85 -> {N + 2}")
    rep.add("canon's minimal admissible shape (10,6), product 88, tested directly",
            gates.THEOREM, bool(excluded(W, 10, 6)),
            note="excluded: no order-10 degree-6 recurrence exists")

    modp = load_modp()
    lengths = {p: len(v) - 1 for p, v in modp.items()}
    rep.add(f"W_n mod {sorted(modp)} from the D8 + spinor engine agree with the exact "
            f"Weyl-orbit W_0..W_{N} (two independent algorithms)", gates.THEOREM,
            len(modp) == 4 and min(lengths.values()) > N
            and all(Wp[n] == W[n] % p for p, Wp in modp.items() for n in range(N + 1)), lengths)
    p0, p1 = sorted((p for p in modp if lengths[p] >= 600), reverse=True)[:2]
    M = 120
    rep.add(f"stored residues re-derived in-suite for W_0..W_{M} mod {p0}", gates.THEOREM,
            walkfast.walk_counts_mod(M, p0) == modp[p0][:M + 1])
    W0 = modp[p0]
    K = 455
    cs = corners(len(W0) - 1, K)
    rep.add(f"W_0..W_600 mod {p0}: every recurrence with (r+1)(d+2) <= {K} is excluded "
            f"({len(cs)} corner shapes, full rank)", gates.THEOREM,
            all(excluded(W0, r, d, p0) for r, d in cs),
            note="order 10 needs degree >= 53, order 11 >= 49, order 15 >= 36 (frontier "
                 "on the same data); the sibling's (r+1)(d+2) >= 195 and 'order 11 needs "
                 "degree >= 15' follow")
    ker = {p: len(ore.nullspace(shape_matrix(modp[p], 23, 17, p), p)) for p in (p0, p1)}
    rows = len(W0) - 23
    rep.add("first kernel: shape (23, 17), product 456, has a 2-dim kernel mod both primes "
            f"with {rows - 24 * 18} more equations than unknowns", gates.THEOREM,
            all(k == 2 for k in ker.values()), ker,
            note="an accidental kernel of an overdetermined system mod p has probability "
                 "~p^-146; this is a recurrence of the data")
    d, stored = load_operator()
    ops = []
    for r, dd in d["shapes"]:
        ops += ore.kernel_operators(shape_matrix(W0[:501], r, dd, p0), r, dd, p0)
    G = ore.gcrd(ops, p0)
    same = len(G) == len(stored[p0]) and all(np.array_equal(a, b) for a, b in zip(G, stored[p0]))
    rep.add(f"GCRD of the kernel recurrences of shapes {d['shapes']} on W_0..W_500 is one "
            f"operator of order {ore.order(G)} and degree {ore.degree(G)} (= stored), and it "
            "annihilates W_501..W_600 as well", gates.THEOREM,
            same and ore.order(G) == 16 and ore.degree(G) == 58
            and not ore.residual(G, W0, p0).any())
    rep.add("the stored order-16 operator annihilates all data mod each of the four primes",
            gates.THEOREM, all(not ore.residual(stored[p], modp[p], p).any() for p in stored),
            {str(p): lengths[p] - 16 + 1 for p in stored})
    z = sp.symbols("z")
    roots = {sp.Rational(k): v for k, v in d["characteristic_roots"].items()}
    chiQ = sp.Poly(sp.prod([(z - r) ** m for r, m in roots.items()]), z).all_coeffs()[::-1]
    ok_chi, ok_exp, ok_ind = True, True, True
    for p, L in stored.items():
        chi = ore.charpoly(L, p)
        inv = pow(chi[-1], p - 2, p)
        ok_chi &= [x * inv % p for x in chi] == [int(c.p) * pow(int(c.q), p - 2, p) % p
                                                 for c in map(sp.Rational, chiQ)]
        for r, m in roots.items():
            if m == 1:
                ok_exp &= ore.exponent_at(L, int(r.p) * pow(int(r.q), p - 2, p) % p, p) == (-4) % p
        ok_ind &= ore.indicial_double(L, -12, p) == (9, 20)
    band = {str(r): m for r, m in roots.items() if -16 <= r <= 240}
    rep.add("characteristic polynomial of the operator, exact over Q (all four primes): 16 "
            "roots, 11 of them (with multiplicity) in the band [-16, 240]", gates.THEOREM,
            ok_chi and sum(band.values()) == 11 and sum(roots.values()) == 16,
            {"in_band": band, "outside": {str(r): m for r, m in roots.items()
                                          if not -16 <= r <= 240}},
            note="240 band top, 16 the 224 saddle, -16 band bottom; 340, -660, -20, -35, "
                 "-120/7 lie outside the real band")
    rep.add("local exponents: -4 = -dim/2 at every simple root; (alpha+4)(alpha+5) at the "
            "double root -12", gates.THEOREM, ok_exp and ok_ind)
    rep.add("the in-band part of the characteristic polynomial has degree 11 and contains "
            "(z+12)^2 (the sibling's 'order 11 with (x+12)^2'); the operator found has order 16",
            gates.THEOREM,
            ok_chi and band.get("-12") == 2 and sum(band.values()) == 11,
            note="an order-11 annihilator is not excluded by the data (it would need degree "
                 ">= 49) but would be a right factor of this operator")
    rep.add("explicit scalar recurrence for W_n over Q", gates.UNFORMED, True,
            note="order 16 and degree 58 mod four primes, characteristic roots exact; the "
                 "rational coefficients need more primes, and a proof for all n needs "
                 "creative telescoping or an a-priori size bound")
    return rep
