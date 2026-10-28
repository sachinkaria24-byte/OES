"""Exact closed-walk counts W_n on the E8 root lattice (steps in the 240 roots).

W_n = number of length-n walks from 0 back to 0. The walk-count function
c_k(x) (walks of length k from 0 to x) is W(E8)-invariant, so it is stored
only on dominant weights, and

    c_{k+1}(nu) = sum_{alpha in roots} c_k(dom(nu - alpha)),
    W_{2k}   = sum_{nu dominant} |W nu| c_k(nu)^2,
    W_{2k+1} = sum_{nu dominant} |W nu| c_k(nu) c_{k+1}(nu).

All counts are carried modulo several 31-bit primes and recombined by the
Chinese remainder theorem, so every printed W_n is an exact integer. The
orbit size |W nu| = |W(E8)| / |W_nu| uses the parabolic stabiliser read off
from the simple roots orthogonal to nu.
"""

from itertools import combinations, product
from math import factorial, prod

import numpy as np

WE8 = 696729600
PRIMES = [2147483647, 2147483629, 2147483587, 2147483579, 2147483563, 2147483549,
          2147483543, 2147483497, 2147483489, 2147483477, 2147483423, 2147483399,
          2147483353, 2147483323, 2147483269, 2147483249, 2147483237, 2147483179,
          2147483171, 2147483137, 2147483123, 2147483077, 2147483069, 2147483059,
          2147483053, 2147483033, 2147483029, 2147482951, 2147482949, 2147482943]


def roots_doubled():
    R = []
    for i, j in combinations(range(8), 2):
        for s, t in product((2, -2), repeat=2):
            v = [0] * 8
            v[i], v[j] = s, t
            R.append(v)
    for signs in product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            R.append(list(signs))
    return np.array(R, dtype=np.int64)


def simple_roots(R):
    """Simple system for the generic direction t0; doubled coordinates."""
    t0 = np.array([1, 3, 7, 15, 31, 63, 127, 1000], dtype=np.int64)
    pos = [r for r in R if r @ t0 > 0]
    P = {tuple(r) for r in pos}
    simple = [r for r in pos
              if not any(tuple(r - a) in P for a in pos if not np.array_equal(a, r))]
    S = np.array(simple, dtype=np.int64)
    assert len(pos) == 120 and len(S) == 8
    return S


def weyl_order(names):
    out = 1
    for t, n in names:
        if t == "A":
            out *= factorial(n + 1)
        elif t == "D":
            out *= 2 ** (n - 1) * factorial(n)
        elif t == "E":
            out *= {6: 51840, 7: 2903040, 8: 696729600}[n]
    return out


def component_types(nodes, adj):
    """Dynkin types of the subdiagram on `nodes` (a forest of simply-laced trees)."""
    nodes = set(nodes)
    seen, types = set(), []
    for s in nodes:
        if s in seen:
            continue
        comp, stack = [], [s]
        seen.add(s)
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if w in nodes and w not in seen:
                    seen.add(w)
                    stack.append(w)
        deg = {u: sum(1 for w in adj[u] if w in nodes) for u in comp}
        n = len(comp)
        branch = [u for u in comp if deg[u] == 3]
        if not branch:
            types.append(("A", n))
            continue
        b = branch[0]
        arms = []
        for w in adj[b]:
            if w not in nodes:
                continue
            length, prev, cur = 1, b, w
            while True:
                nxt = [x for x in adj[cur] if x in nodes and x != prev]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
                length += 1
            arms.append(length)
        arms.sort()
        if arms[0] == 1 and arms[1] == 1:
            types.append(("D", n))
        elif arms == [1, 2, 2]:
            types.append(("E", 6))
        elif arms == [1, 2, 3]:
            types.append(("E", 7))
        elif arms == [1, 2, 4]:
            types.append(("E", 8))
        else:
            raise ValueError(arms)
    return types


class Engine:
    def __init__(self, nprimes=16):
        self.R = roots_doubled()
        self.S = simple_roots(self.R)
        C = (self.S @ self.S.T) // 4
        self.adj = {i: [j for j in range(8) if j != i and C[i, j] == -1] for i in range(8)}
        self.primes = np.array(PRIMES[:nprimes], dtype=np.int64)

    def dominant(self, X):
        X = X.copy()
        active = np.arange(len(X))
        while len(active):
            Y = X[active]
            changed = np.zeros(len(active), dtype=bool)
            for a in self.S:
                ip = (Y @ a) // 4
                neg = ip < 0
                if neg.any():
                    Y[neg] -= ip[neg, None] * a
                    changed |= neg
            X[active] = Y
            active = active[changed]
        return X

    def stabiliser_order(self, X):
        Z = (X @ self.S.T) == 0
        cache, out = {}, np.empty(len(X), dtype=object)
        for i, row in enumerate(Z):
            key = tuple(row)
            if key not in cache:
                nodes = [j for j in range(8) if row[j]]
                cache[key] = weyl_order(component_types(nodes, self.adj)) if nodes else 1
            out[i] = cache[key]
        return out

    @staticmethod
    def _decode(K):
        X = np.zeros((len(K), 8), dtype=np.int64)
        K = K.copy()
        for j in range(7, -1, -1):
            X[:, j] = (K & np.uint64(255)).astype(np.int64) - 128
            K = K >> np.uint64(8)
        return X

    @staticmethod
    def _rowkeys(X):
        # exact 1-1 key: coordinates in [-128, 127] after doubling, 8 bytes
        Y = (X + 128).astype(np.uint64)
        k = np.zeros(len(X), dtype=np.uint64)
        for j in range(8):
            k = (k << np.uint64(8)) | Y[:, j]
        return k

    def _pair(self, la, lb):
        P = [int(p) for p in self.primes]
        sa, ca = la
        sb, cb = lb
        ka, kb = self._rowkeys(sa), self._rowkeys(sb)
        ob = np.argsort(kb)
        j = np.clip(np.searchsorted(kb[ob], ka), 0, len(kb) - 1)
        hit = kb[ob][j] == ka
        orbit = np.array([WE8 // s for s in self.stabiliser_order(sa)], dtype=object)
        res = []
        for t, p in enumerate(P):
            x = ca[hit, t].astype(object) * cb[ob[j[hit]], t].astype(object)
            res.append(int((orbit[hit] * x).sum() % p))
        return crt(res, P)

    def walk_counts(self, kmax, log=None, sink=None):
        """W_0..W_{2 kmax}; `sink(list)` is called after every new layer."""
        layers = []
        W = []
        for layer in self.layers(kmax, log=log):
            layers.append(layer)
            k = len(layers) - 1
            if k == 0:
                W.append(self._pair(layers[0], layers[0]))
            else:
                W.append(self._pair(layers[k - 1], layers[k]))
                W.append(self._pair(layers[k], layers[k]))
            if sink:
                sink(W)
        return W

    def layers(self, kmax, log=None):
        P = self.primes
        sup = np.zeros((1, 8), dtype=np.int64)
        cnt = np.ones((1, len(P)), dtype=np.int64)
        yield sup, cnt
        chunk = 3000
        for k in range(kmax):
            keys = []
            for s in range(0, len(sup), chunk):
                c = self.dominant((sup[s:s + chunk, None, :] + self.R[None]).reshape(-1, 8))
                keys.append(np.unique(self._rowkeys(c)))
            new = self._decode(np.unique(np.concatenate(keys)))
            ks = self._rowkeys(sup)
            order = np.argsort(ks)
            keys_sorted = ks[order]
            newcnt = np.zeros((len(new), len(P)), dtype=np.int64)
            for s in range(0, len(new), chunk):
                block = new[s:s + chunk]
                prev = self.dominant((block[:, None, :] - self.R[None]).reshape(-1, 8))
                pk = self._rowkeys(prev)
                idx = np.clip(np.searchsorted(keys_sorted, pk), 0, len(keys_sorted) - 1)
                hit = keys_sorted[idx] == pk
                vals = np.zeros((len(prev), len(P)), dtype=np.int64)
                vals[hit] = cnt[order[idx[hit]]]
                newcnt[s:s + chunk] = vals.reshape(len(block), len(self.R), len(P)).sum(1) % P
            sup, cnt = new, newcnt
            if log:
                log(f"k={k + 1} support={len(sup)}")
            yield sup, cnt


def crt(residues, moduli):
    x, M = 0, 1
    for r, m in zip(residues, moduli):
        t = ((r - x) * pow(M, -1, m)) % m
        x += M * t
        M *= m
    return x


KNOWN = [1, 0, 240, 13440, 1260720, 137813760, 17141798400]

if __name__ == "__main__":
    import json
    import sys
    import time
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    out = sys.argv[2] if len(sys.argv) > 2 else "walks.json"
    t0 = time.time()
    eng = Engine(nprimes=min(len(PRIMES), int(np.ceil((2 * kmax) * np.log2(240) / 30.5)) + 2))

    def sink(W):
        with open(out, "w") as f:
            json.dump({"kmax_done": (len(W) - 1) // 2, "W": [str(w) for w in W],
                       "engine": "W(E8) dominant-weight DP, CRT over 31-bit primes"}, f)

    W = eng.walk_counts(kmax, log=lambda s: print(s, f"{time.time() - t0:.1f}s", flush=True), sink=sink)
    assert W[:7] == KNOWN, W[:7]
    print("done", len(W), "terms", f"{time.time() - t0:.1f}s")
