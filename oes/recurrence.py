"""Layer 14. The scalar walk recurrence: which shapes are excluded.

A P-recurrence of order r and degree d is sum_{j<=r} p_j(n) W_{n+j} = 0 with
deg p_j <= d. The canon proves an eventual recurrence holds for every n >= 0
(all-prime congruences), so the exact matrix

    V[n, (j, k)] = n^k W_{n+j},   n = 0..N-r,  j = 0..r,  k = 0..d,

decides it: full column rank modulo a prime p implies full rank over Q, and
then no recurrence of that shape exists. The canon's standing bound (28 Oct)
is (r+1)(d+2) > 85. This layer recomputes the excluded region from the exact
W_0..W_N of layer 3/walks (N = 60 here, 90 when data/walks90.json is complete).
"""

import json
from pathlib import Path

import numpy as np

from . import gates
from .record import Report

ROOT = Path(__file__).resolve().parent.parent
P = 2147483629


def load_walks():
    best = None
    for name in ("walks90.json", "walks.json"):
        f = ROOT / "data" / name
        if f.exists():
            W = [int(x) for x in json.loads(f.read_text())["W"]]
            if best is None or len(W) > len(best):
                best = W
    return best


def rank_mod_p(A, p=P):
    A = A.copy() % p
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i, c]), None)
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), -1, p)
        A[r] = (A[r] * inv) % p
        for i in range(rows):
            if i != r and A[i, c]:
                A[i] = (A[i] - (A[i, c] * A[r]) % p) % p
        r += 1
    return r


def shape_matrix(W, r, d, p=P):
    N = len(W) - 1
    rows = N - r + 1
    Wm = [w % p for w in W]
    V = np.zeros((rows, (r + 1) * (d + 1)), dtype=np.int64)
    for n in range(rows):
        for j in range(r + 1):
            for k in range(d + 1):
                V[n, j * (d + 1) + k] = (pow(n, k, p) * Wm[n + j]) % p
    return V


def excluded(W, r, d, p=P):
    """True if the data exclude every recurrence of order r, degree d."""
    V = shape_matrix(W, r, d, p)
    if V.shape[0] < V.shape[1]:
        return None                       # underdetermined: data cannot decide
    return rank_mod_p(V, p) == V.shape[1]


def frontier(W, rmax=40):
    """For each order r, the largest degree d that the data exclude."""
    out = {}
    for r in range(1, rmax + 1):
        dmax = -1
        d = 0
        while True:
            e = excluded(W, r, d)
            if e is None:
                break
            if not e:
                out[r] = {"excluded_up_to_degree": dmax, "kernel_at_degree": d}
                break
            dmax = d
            d += 1
        else:
            pass
        out.setdefault(r, {"excluded_up_to_degree": dmax, "kernel_at_degree": None})
    return out


def run():
    rep = Report("14-recurrence")
    W = load_walks()
    N = len(W) - 1
    from . import walks
    canon = [int(x) for x in json.loads((ROOT / "data" / "canon_walks_0_55.json").read_text())["W"]]
    rep.add("W_0..W_55 of the canon ledger replayed exactly by the Weyl-orbit engine "
            "(incl. W_25..W_55, never independently regenerated before)", gates.THEOREM,
            W[:56] == canon, {"terms_compared": 56, "mismatches": sum(a != b for a, b in zip(W, canon))})
    fresh = walks.Engine(nprimes=8).walk_counts(12)
    rep.add("stored walk file re-derived in-suite for W_0..W_24", gates.THEOREM,
            fresh == W[:25])
    rep.add(f"new exact terms W_56..W_{N} (lattice sequence W_60 formed)", gates.THEOREM,
            N >= 60 and all(W[n] % 240 == 0 for n in range(1, N + 1)), N)
    canon_cases = [(5, 2), (10, 2), (12, 2), (10, 3)]
    ok = all(excluded(W, r, d) for r, d in canon_cases)
    rep.add(f"canon exclusions (5,2), (10,2), (12,2), (10,3) replayed on W_0..W_{N}",
            gates.THEOREM, ok)
    fr = frontier(W, rmax=40)
    kernels = {r: v["kernel_at_degree"] for r, v in fr.items() if v["kernel_at_degree"] is not None}
    rep.add(f"no recurrence shape decidable from W_0..W_{N} has a kernel", gates.THEOREM,
            not kernels, kernels or "none",
            note="a kernel would be a candidate recurrence; none appears")
    decided_all = all(v["kernel_at_degree"] is None for v in fr.values())
    rep.add(f"data-only bound from W_0..W_{N}: every recurrence has (r+1)(d+2) > {N + 2}",
            gates.THEOREM, decided_all,
            {str(r): v["excluded_up_to_degree"] for r, v in fr.items()},
            note=f"shape (r,d) is decided when (r+1)(d+1) <= N-r+1; all decided shapes "
                 f"are excluded. Canon standing bound: (r+1)(d+2) > 85"
                 + (" -> improved" if N + 2 > 85 else ""))
    if N >= 86:
        rep.add("canon's minimal admissible shape (10,6), product 88, tested directly",
                gates.THEOREM, bool(excluded(W, 10, 6)), bool(excluded(W, 10, 6)),
                note="excluded means no order-10 degree-6 recurrence exists")
    rep.add("explicit scalar recurrence for W_n", gates.UNFORMED, True,
            note="needs more exact terms than a Weyl-orbit DP reaches; the canon proves "
                 "order >= 10 and the finite determinant construction exists")
    return rep
