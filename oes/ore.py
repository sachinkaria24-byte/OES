"""Shift (Ore) operators with coefficients in F_p[n], for the W_n recurrence.

An operator L = sum_j a_j(n) E^j acts on sequences by (L W)(n) = sum_j a_j(n) W(n+j).
Polynomials are int64 arrays mod p, lowest degree first; an operator is the list
[a_0, ..., a_r]. Products obey E a(n) = a(n+1) E.

The annihilators of a sequence form a left ideal of F_p(n)[E], which is principal.
So the greatest common right divisor (GCRD) of annihilators is again an
annihilator, of order no larger than any of them. It is computed here by the
primitive right pseudo-remainder sequence. The characteristic polynomial
chi(z) = sum_j [n^D] a_j(n) z^j (D the top degree) carries the exponential growth
rates of the solutions. At a simple root v, a solution v^n n^alpha has
alpha = -chi_1(v) / (v chi'(v)), where chi_1 is built from the n^(D-1)
coefficients in the same way.
"""

import numpy as np


def trim(a, p):
    a = np.asarray(a, dtype=np.int64) % p
    nz = np.nonzero(a)[0]
    return a[:nz[-1] + 1] if len(nz) else np.zeros(0, dtype=np.int64)


def mul(a, b, p):
    if len(a) == 0 or len(b) == 0:
        return np.zeros(0, dtype=np.int64)
    if min(len(a), len(b)) * (p - 1) ** 2 < 2 ** 62:
        return trim(np.convolve(a, b), p)
    lo, hi = a % 1024, a // 1024
    return trim((np.convolve(hi, b) % p * 1024 + np.convolve(lo, b)) % p, p)


def sub(a, b, p):
    x = np.zeros(max(len(a), len(b)), dtype=np.int64)
    x[:len(a)] += a
    x[:len(b)] -= b
    return trim(x, p)


def shift(a, s, p):
    """a(n + s)."""
    if len(a) == 0 or s == 0:
        return a.copy()
    m = len(a) - 1
    C = np.zeros((m + 1, m + 1), dtype=np.int64)
    C[0, 0] = 1
    for i in range(1, m + 1):
        C[i, 0] = 1
        C[i, 1:i + 1] = (C[i - 1, :i] + C[i - 1, 1:i + 1]) % p
    spow = np.ones(m + 1, dtype=np.int64)
    for i in range(1, m + 1):
        spow[i] = spow[i - 1] * (s % p) % p
    out = np.zeros(m + 1, dtype=np.int64)
    for j in range(m + 1):
        if a[j]:
            out[:j + 1] = (out[:j + 1] + a[j] * (C[j, :j + 1] * spow[j::-1] % p)) % p
    return trim(out, p)


def pdivmod(a, b, p):
    a, b = trim(a, p).copy(), trim(b, p)
    inv = pow(int(b[-1]), p - 2, p)
    q = np.zeros(max(len(a) - len(b) + 1, 1), dtype=np.int64)
    while len(a) >= len(b) and len(a):
        c = a[-1] * inv % p
        k = len(a) - len(b)
        q[k] = c
        a[k:] = (a[k:] - c * b) % p
        a = trim(a, p)
    return trim(q, p), a


def gcd(a, b, p):
    a, b = trim(a, p), trim(b, p)
    while len(b):
        a, b = b, pdivmod(a, b, p)[1]
    return a * pow(int(a[-1]), p - 2, p) % p if len(a) else a


def order(L):
    return len(L) - 1


def degree(L):
    return max(len(c) - 1 for c in L if len(c))


def _strip(L):
    L = list(L)
    while L and len(L[-1]) == 0:
        L.pop()
    return L


def primitive(L, p):
    """Divide out the polynomial content and make the top coefficient monic."""
    L = _strip(L)
    g = None
    for c in L:
        if len(c):
            g = c if g is None else gcd(g, c, p)
            if len(g) == 1:
                break
    if g is not None and len(g) > 1:
        L = [pdivmod(c, g, p)[0] if len(c) else c for c in L]
    inv = pow(int(L[-1][-1]), p - 2, p)
    return [c * inv % p for c in L]


def rprem(L1, L2, p):
    """Primitive right pseudo-remainder of L1 by L2 (order < ord L2)."""
    L1, L2 = _strip(L1), _strip(L2)
    r2 = order(L2)
    while L1 and order(L1) >= r2:
        s = order(L1) - r2
        lc1, lc2 = L1[-1], shift(L2[-1], s, p)
        new = [mul(lc2, c, p) for c in L1]
        for j, c in enumerate(L2):
            new[j + s] = sub(new[j + s], mul(lc1, shift(c, s, p), p), p)
        new = _strip(new)
        L1 = primitive(new, p) if new else new
    return L1


def gcrd(ops, p):
    G = primitive(ops[0], p)
    for L in ops[1:]:
        A, B = G, primitive(L, p)
        if order(A) < order(B):
            A, B = B, A
        while B:
            A, B = B, rprem(A, B, p)
        G = primitive(A, p)
    return G


def residual(L, W, p):
    """(L W)(n) mod p for every n the data reach."""
    W = np.array([w % p for w in W], dtype=np.int64)
    r = order(L)
    n = np.arange(len(W) - r, dtype=np.int64)
    out = np.zeros(len(n), dtype=np.int64)
    for j, c in enumerate(L):
        v = np.zeros(len(n), dtype=np.int64)
        for x in reversed(c):
            v = (v * n + int(x)) % p
        out = (out + v * W[j:j + len(n)]) % p
    return out


def nullspace(A, p):
    """Basis of {x : A x = 0} over F_p (reduced row echelon form)."""
    A = np.array(A, dtype=np.int64) % p
    rows, cols = A.shape
    piv = []
    r = 0
    for c in range(cols):
        if r == rows:
            break
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0:
            continue
        k = r + nz[0]
        if k != r:
            A[[r, k]] = A[[k, r]]
        A[r] = A[r] * pow(int(A[r, c]), p - 2, p) % p
        f = A[:, c].copy()
        f[r] = 0
        idx = np.nonzero(f)[0]
        if len(idx):
            A[idx] = (A[idx] - np.outer(f[idx], A[r]) % p) % p
        piv.append(c)
        r += 1
    pset = set(piv)
    basis = []
    for fc in (c for c in range(cols) if c not in pset):
        x = np.zeros(cols, dtype=np.int64)
        x[fc] = 1
        for i, pc in enumerate(piv):
            x[pc] = (-A[i, fc]) % p
        basis.append(x)
    return basis


def kernel_operators(V, r, d, p):
    """The recurrences of shape (r, d) in the kernel of the shape matrix V."""
    return [_strip([trim(x[j * (d + 1):(j + 1) * (d + 1)], p) for j in range(r + 1)])
            for x in nullspace(V, p)]


def peval(c, z, p):
    v = 0
    for x in reversed(c):
        v = (v * z + int(x)) % p
    return v


def deriv(c, p):
    return [(k * int(c[k])) % p for k in range(1, len(c))]


def charpoly(L, p, s=0):
    """chi_s(z) = sum_j [n^(D-s)] a_j(n) z^j, D the top degree of L."""
    D = degree(L)
    return [int(c[D - s]) if len(c) > D - s else 0 for c in L]


def integer_roots(c, p, lo=-1000, hi=1000):
    """{z: multiplicity} for the integer roots of c mod p in [lo, hi]."""
    out = {}
    for z in range(lo, hi + 1):
        m, q = 0, list(c)
        while q and peval(q, z % p, p) == 0:
            m += 1
            q = deriv(q, p)
        if m:
            out[z] = m
    return out


def exponent_at(L, vp, p):
    """alpha mod p at a simple characteristic root given by its residue vp."""
    chi, chi1 = charpoly(L, p), charpoly(L, p, 1)
    den = vp * peval(deriv(chi, p), vp, p) % p
    return (-peval(chi1, vp, p)) * pow(den, p - 2, p) % p


def indicial_double(L, v, p):
    """Monic indicial polynomial alpha^2 + b alpha + c at a double root v, as (b, c) mod p."""
    chi, chi1, chi2 = charpoly(L, p), charpoly(L, p, 1), charpoly(L, p, 2)
    vp = v % p
    A = vp * vp % p * peval(deriv(deriv(chi, p), p), vp, p) % p * pow(2, p - 2, p) % p
    B = (vp * peval(deriv(chi1, p), vp, p) - A) % p
    C = peval(chi2, vp, p)
    ia = pow(A, p - 2, p)
    return B * ia % p, C * ia % p
