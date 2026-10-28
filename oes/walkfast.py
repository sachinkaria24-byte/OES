"""Walk counts W_n on the E8 root lattice modulo a prime, far past the Weyl-orbit DP.

E8 = D8 u (D8 + s). On the torus, with c_i = cos(theta_i), the root sum is

    lambda = 4 e2(c) + 128 prod cos(theta_i / 2) + 128 prod sin(theta_i / 2),

and odd powers of the two spinor products have zero constant term. Their squares
are 64 prod(1 + c_i) and 64 prod(1 - c_i), so

    W_n = sum_q C(n, 2q) 4^(n-2q) 64^q sum_m C(2q, 2m) S_qm(n - 2q),
    S_qm(p) = E[ e2(c)^p prod_i (1 + c_i)^(q-m) (1 - c_i)^m ],

with c_1..c_8 independent, each the cosine of a uniform angle. The coupling e2 is
removed by e2 = (e1^2 - p2)/2 and one Gaussian variable z (Hubbard-Stratonovich):

    S(p) / p! = [t^(2p)] E_z[ K(t, z)^8 ],   K = sum_k mu_f(k) He_k(z) t^k / k!,

where mu_f(k) = E[c^k f(c)] and He_k are the probabilists' Hermite polynomials.
Every step is exact over F_p: E_z is applied through the nodes z = 0..P with
Lagrange weights that integrate every even polynomial of degree <= 2P, and the
eighth power is taken pointwise on L-th roots of unity with L > 16P, so no kept
coefficient aliases. Floating-point matrix products are used only where every
partial sum is an integer below 2^53.
"""

from math import comb

import numpy as np
import sympy as sp

PRIMES = (1769473, 1376257)          # p - 1 divisible by 2^16, p < 2^21


def _mm(A, B, p):
    """A @ B mod p for residue arrays, exact: every partial sum is an integer below 2^53."""
    assert A.shape[1] * (p - 1) ** 2 < 2 ** 53
    return (A.astype(np.float64) @ B).astype(np.int64) % p


class Field:
    def __init__(self, p, nmax):
        self.p = p
        f = [1]
        for i in range(1, 2 * nmax + 2):
            f.append(f[-1] * i % p)
        self.fact = np.array(f, dtype=np.int64)
        self.ifact = np.array([pow(x, p - 2, p) for x in f], dtype=np.int64)
        self.g = int(sp.primitive_root(p))
        inv2 = pow(2, p - 2, p)
        # E[c^k] = C(k, k/2) / 2^k for even k
        self.mom = np.zeros(2 * nmax + 2, dtype=np.int64)
        for k in range(0, 2 * nmax + 2, 2):
            self.mom[k] = f[k] * self.ifact[k // 2] % p * self.ifact[k // 2] % p * pow(inv2, k, p) % p
        divs = sorted(int(d) for d in sp.divisors(p - 1))
        self.divisors = divs

    def binom(self, n, k):
        p = self.p
        return int(self.fact[n] * self.ifact[k] % p * self.ifact[n - k] % p)

    def root_order(self, need):
        return next(d for d in self.divisors if d >= need and d % 2 == 0)


class Block:
    """Everything that depends only on P = n_max - 2q."""

    def __init__(self, F, P):
        p = F.p
        self.P = P
        self.L = L = F.root_order(16 * P + 1)
        w = pow(F.g, (p - 1) // L, p)
        powtab = np.ones(L, dtype=np.int64)
        for j in range(1, L):
            powtab[j] = powtab[j - 1] * w % p
        kap = np.arange(2 * P + 1)
        self.Omega = powtab[np.outer(kap, np.arange(L)) % L].astype(np.float64)  # (2P+1) x L
        half = L // 2
        inv = (2 * pow(L, p - 2, p)) % p
        self.Back = powtab[(-np.outer(2 * np.arange(P + 1), np.arange(half))) % L] * inv % p
        z = np.arange(P + 1, dtype=np.int64)
        He = np.zeros((P + 1, 2 * P + 1), dtype=np.int64)
        He[:, 0] = 1
        if P > 0:
            He[:, 1] = z
        for k in range(1, 2 * P):
            He[:, k + 1] = (z * He[:, k] - k * He[:, k - 1]) % p
        self.H = He * F.ifact[:2 * P + 1][None, :] % p
        self.weights = self._weights(F, P)

    @staticmethod
    def _weights(F, P):
        """w_l with sum_l w_l h(l^2) = L'(h) for deg h <= P, L'(y^k) = (2k-1)!!."""
        p = F.p
        y = (np.arange(P + 1, dtype=np.int64) ** 2) % p
        phi = np.array([1], dtype=np.int64)                         # prod (Y - y_i), low first
        for yi in y:
            phi = (np.concatenate([[0], phi]) - np.concatenate([phi * yi % p, [0]])) % p
        m = np.ones(P + 1, dtype=np.int64)
        for k in range(1, P + 1):
            m[k] = m[k - 1] * (2 * k - 1) % p
        Q = np.full(P + 1, phi[P + 1], dtype=np.int64)              # leading quotient coefficient
        acc = m[P] * Q % p
        for k in range(P, 0, -1):
            Q = (phi[k] + y * Q) % p
            acc = (acc + m[k - 1] * Q) % p
        den = np.ones(P + 1, dtype=np.int64)
        for i in range(P + 1):
            d = (y - y[i]) % p
            d[i] = 1
            den = den * d % p
        return acc * np.array([pow(int(x), p - 2, p) for x in den], dtype=np.int64) % p

    def S(self, F, f_coeffs):
        """S(p') for p' = 0..P, where f(c) = sum_j f_coeffs[j] c^j."""
        p, P = F.p, self.P
        j = len(f_coeffs)
        k = np.arange(2 * P + 1)
        mu = np.zeros(2 * P + 1, dtype=np.int64)
        for jj in range(j):
            mu = (mu + f_coeffs[jj] * F.mom[k + jj]) % p
        Khat = _mm(self.H * mu[None, :] % p, self.Omega, p)
        K8 = Khat * Khat % p
        K8 = K8 * K8 % p
        K8 = K8 * K8 % p
        T = (self.weights @ K8) % p                     # int64: (P+1)(p-1)^2 < 2^63
        half = self.L // 2
        Ts = (T[:half] + T[half:]) % p * ((p + 1) // 2) % p
        coef = (self.Back @ Ts) % p
        return coef * F.fact[:P + 1] % p


def spinor_poly(q, m, p):
    """Coefficients of (1 + c)^(q-m) (1 - c)^m, low degree first, mod p."""
    a = [comb(q - m, i) for i in range(q - m + 1)]
    b = [comb(m, i) * (-1) ** i for i in range(m + 1)]
    out = [0] * (q + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return np.array([x % p for x in out], dtype=np.int64)


def walk_counts_mod(N, p, log=None):
    """W_0..W_N modulo p."""
    F = Field(p, N)
    W = np.zeros(N + 1, dtype=np.int64)
    for q in range(N // 2 + 1):
        P = N - 2 * q
        blk = Block(F, P)
        acc = np.zeros(P + 1, dtype=np.int64)
        for m in range(q // 2 + 1):
            sym = 2 if m < q - m else 1
            s = blk.S(F, spinor_poly(q, m, p))
            acc = (acc + sym * F.binom(2 * q, 2 * m) * s) % p
        for pp in range(P + 1):
            n = 2 * q + pp
            c = F.binom(n, 2 * q) * pow(4, pp, p) % p * pow(64, q, p) % p
            W[n] = (W[n] + c * int(acc[pp])) % p
        if log:
            log(f"q={q} P={P} L={blk.L}")
    return [int(x) for x in W]


if __name__ == "__main__":
    import json
    import sys
    import time
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    out = sys.argv[2] if len(sys.argv) > 2 else "walks_modp.json"
    primes = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else PRIMES
    t0 = time.time()
    res = {}
    for p in primes:
        res[str(p)] = walk_counts_mod(N, p, log=lambda s: print(s, f"{time.time() - t0:.1f}s",
                                                                 flush=True))
    with open(out, "w") as f:
        json.dump({"N": N, "W_mod_p": res,
                   "engine": "D8 + spinor factorisation, Hermite-Gauss over F_p"}, f)
    print("done", N, f"{time.time() - t0:.1f}s")
