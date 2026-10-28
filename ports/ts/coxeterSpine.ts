// Drop-in audit for the sibling model (src/lib/model): the integrated spine with
// checks that can fail. No imports. Same convention as the other audits:
// auditCoxeterSpine() returns { residual: 0 } when every row holds.
//
// Python reference: oes/spine.py (layer 19 of `python verify.py`) in
// sachinkaria24-byte/OES, branch claude/lagrangian-spectral-spacetime-model-t2253b.
//
// Matrices of W(E8) are kept in standard E8 coordinates scaled by 4. Every
// element of W(E8) has entries in Z/4 there, so products stay integral:
// (4A)(4B)/4 = 4(AB).

type Mat = number[][];
type Row = { name: string; ok: boolean; value?: unknown };

const N = 4320;
const gcd = (a: number, b: number): number => (b === 0 ? Math.abs(a) : gcd(b, a % b));
const lcm = (a: number, b: number) => (a / gcd(a, b)) * b;
const gen = (a: number) => gcd(((a % N) + N) % N, N);
const order = (a: number) => N / gen(a);
const contains = (a: number, b: number) => gen(b) % gen(a) === 0; // <b> inside <a>
const meet = (a: number, b: number) => lcm(gen(a), gen(b)) % N;
const join = (a: number, b: number) => gcd(gen(a), gen(b)) % N;
const subgroup = (a: number) => Array.from({ length: order(a) }, (_, k) => (k * gen(a)) % N);

const zeros = (n: number): Mat => Array.from({ length: n }, () => Array(n).fill(0));
const eye4 = (): Mat => zeros(8).map((row, i) => row.map((_, j) => (i === j ? 4 : 0)));
const mul = (A: Mat, B: Mat): Mat =>
  A.map((row) =>
    B[0].map((_, j) => {
      const s = row.reduce((acc, v, k) => acc + v * B[k][j], 0);
      if (s % 4 !== 0) throw new Error("not in W(E8): entry outside Z/4");
      return s / 4;
    }),
  );
const pow = (A: Mat, k: number): Mat => {
  let P = eye4();
  for (let i = 0; i < k; i += 1) P = mul(P, A);
  return P;
};
const eq = (A: Mat, B: Mat) => A.every((row, i) => row.every((v, j) => v === B[i][j]));
const neg = (A: Mat): Mat => A.map((row) => row.map((v) => -v));
const scale = (A: Mat, s: number): Mat => A.map((row) => row.map((v) => v * s));
const apply = (A: Mat, v: number[]) => A.map((row) => row.reduce((acc, a, k) => acc + a * v[k], 0) / 4);
const matOrder = (A: Mat, cap = 200) => {
  let P = A;
  for (let k = 1; k <= cap; k += 1) {
    if (eq(P, eye4())) return k;
    P = mul(P, A);
  }
  return 0;
};

// Bareiss determinant with BigInt.
const det = (source: Mat): bigint => {
  const m = source.map((row) => row.map((v) => BigInt(v)));
  const n = m.length;
  let sign = 1n;
  let prev = 1n;
  for (let p = 0; p < n - 1; p += 1) {
    if (m[p][p] === 0n) {
      const r = m.findIndex((row, i) => i > p && row[p] !== 0n);
      if (r < 0) return 0n;
      [m[p], m[r]] = [m[r], m[p]];
      sign = -sign;
    }
    for (let i = p + 1; i < n; i += 1)
      for (let j = p + 1; j < n; j += 1) m[i][j] = (m[p][p] * m[i][j] - m[i][p] * m[p][j]) / prev;
    prev = m[p][p];
  }
  return sign * m[n - 1][n - 1];
};

// The 240 roots, doubled to integers: +-2e_i +- 2e_j and (+-1, ..., +-1) with an even number of minus signs.
const roots2 = (() => {
  const out: number[][] = [];
  for (let i = 0; i < 8; i += 1)
    for (let j = i + 1; j < 8; j += 1)
      for (const a of [2, -2])
        for (const b of [2, -2]) {
          const v = Array(8).fill(0);
          v[i] = a;
          v[j] = b;
          out.push(v);
        }
  for (let mask = 0; mask < 256; mask += 1) {
    const v = Array.from({ length: 8 }, (_, i) => ((mask >> i) & 1 ? -1 : 1));
    if (v.filter((x) => x < 0).length % 2 === 0) out.push(v);
  }
  return out;
})();
const rootKey = (v: number[]) => v.join(",");
const rootSet = new Set(roots2.map(rootKey));
const isWeyl = (A: Mat) => roots2.every((r) => rootSet.has(rootKey(apply(A, r))));

// Reflection in a root given doubled (r2 = 2r, |r|^2 = 2): 4(I - r r^T) = 4I - r2 r2^T.
const reflect = (r2: number[]): Mat => eye4().map((row, i) => row.map((v, j) => v - r2[i] * r2[j]));

// Bourbaki simple roots, doubled.
const simple2 = [
  [1, -1, -1, -1, -1, -1, -1, 1],
  [2, 2, 0, 0, 0, 0, 0, 0],
  ...Array.from({ length: 6 }, (_, k) => {
    const v = Array(8).fill(0);
    v[k + 1] = 2;
    v[k] = -2;
    return v;
  }),
];

// Selected data from oes/spine.py: 2c' (c' a Coxeter element with c'^6 = r r'),
// 2d (the day clock), and the twin A4' simple roots (doubled).
const C2 = [
  [0, 1, -1, 0, 1, 1, 0, 0], [1, 0, 0, -1, 0, 0, 1, 1], [0, 1, -1, 0, -1, -1, 0, 0],
  [-1, 0, 0, -1, 0, 0, 1, -1], [1, 0, 0, 1, 0, 0, 1, -1], [1, 0, 0, -1, 0, 0, -1, -1],
  [0, -1, -1, 0, -1, 1, 0, 0], [0, 1, 1, 0, -1, 1, 0, 0],
];
const D2 = [
  [1, 1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, -1, 0, -1], [1, 1, 0, 0, -1, 0, -1, 0],
  [0, 0, -1, 1, 0, 1, 0, -1], [-1, 1, 0, 0, -1, 0, 1, 0], [0, 0, -1, 1, 0, -1, 0, 1],
  [0, 0, 1, 1, 0, 1, 0, 1], [-1, 1, 0, 0, 1, 0, -1, 0],
];
const TWIN2 = [
  [0, 0, 0, 0, 0, 2, 2, 0], [1, 1, 1, 1, 1, -1, -1, 1],
  [-1, -1, -1, -1, -1, 1, -1, 1], [0, 0, 0, 0, 0, -2, 2, 0],
];

const orbitSizes = (A: Mat) => {
  const seen = new Set<string>();
  const sizes: number[] = [];
  for (const r of roots2) {
    if (seen.has(rootKey(r))) continue;
    let v = r;
    let k = 0;
    do {
      seen.add(rootKey(v));
      v = apply(A, v);
      k += 1;
    } while (rootKey(v) !== rootKey(r));
    sizes.push(k);
  }
  return sizes;
};

export function auditCoxeterSpine(): { residual: number; rows: Row[] } {
  const rows: Row[] = [];
  const add = (name: string, ok: boolean, value?: unknown) => rows.push({ name, ok, value });

  // The circle: one lemma, checked against brute force on the subgroups.
  let lemma = true;
  for (let a = 0; a < N; a += 97)
    for (let b = 0; b < N; b += 89) {
      const A = new Set(subgroup(a));
      const B = new Set(subgroup(b));
      const M = new Set(subgroup(meet(a, b)));
      lemma &&= [...A].filter((x) => B.has(x)).length === M.size && [...M].every((x) => A.has(x) && B.has(x));
      lemma &&= contains(a, b) === [...B].every((x) => A.has(x));
    }
  add("one lemma: <b> in <a> iff gcd(a,N) | gcd(b,N); meets are lcms (brute force on a grid)", lemma);
  add("the order-10 subgroup is the multiples of 432 and contains the tick 864",
    subgroup(432).length === 10 && contains(432, 864) && order(864) === 5);
  add("the tower through the Coxeter subgroup: indices 36, 4, 3, 2, 5",
    [N / order(36), order(36) / order(144), order(144) / order(432), order(432) / order(864), order(864)].join() === "36,4,3,2,5");
  const addr = new Set<number>();
  for (let d0 = 0; d0 < 36; d0 += 1)
    for (let d1 = 0; d1 < 4; d1 += 1)
      for (let d2 = 0; d2 < 3; d2 += 1)
        for (let d3 = 0; d3 < 2; d3 += 1)
          for (let d4 = 0; d4 < 5; d4 += 1) addr.add((d0 + 36 * d1 + 144 * d2 + 432 * d3 + 864 * d4) % N);
  add("every element has one address d0 + 36 d1 + 144 d2 + 432 d3 + 864 d4", addr.size === N);
  add("Coxeter step = tick + sun + half-turn: 864 + 1440 + 2160 = 144 mod 4320", (864 + 1440 + 2160) % N === 144);
  add("pada and tick are incomparable and generate the coil <8> (order 540), meeting only at 0",
    !contains(40, 864) && !contains(864, 40) && join(40, 864) === 8 && order(8) === 540 && meet(40, 864) === 0);
  add("correction: <40> n <6> = <120> has order 36 (the moon); the atlas <36> has order 120",
    meet(40, 6) === 120 && order(120) === 36 && order(36) === 120);
  add("correction: 360000 = 1440 mod 4320 (the W0 scalar is the sun step)", 360000 % N === 1440);
  add("correction: 8 x 30 = 240 roots; the positive roots are 8 x 30 / 2 = 120", 8 * 30 === 240);

  // The Coxeter element c = s1 ... s8 (Bourbaki).
  let c = eye4();
  for (const s of simple2) c = mul(c, reflect(s));
  const cOrder = matOrder(c);
  add("c = s1...s8 has order 30 and c^15 = -I", cOrder === 30 && eq(pow(c, 15), neg(eye4())), cOrder);
  const sizes = orbitSizes(c);
  add("c permutes the 240 roots in 8 orbits of 30 (a symmetry of the bath)",
    isWeyl(c) && sizes.length === 8 && sizes.every((k) => k === 30));
  const fixed = Array.from({ length: 29 }, (_, i) => {
    const k = i + 1;
    const M = pow(c, k).map((row, a) => row.map((v, b) => v - (a === b ? 4 : 0)));
    const d = det(M);
    return Number((d < 0n ? -d : d) / 65536n); // det(4X) = 4^8 det(X)
  });
  const expected = Array.from({ length: 29 }, (_, i) => ({ 5: 25, 3: 81, 2: 256 } as Record<number, number>)[30 / gcd(i + 1, 30)] ?? 1);
  add("fixed Bloch momenta |det(c^k - I)|: 25 (tick), 81 (sun), 256 (half-turn), else 1",
    fixed.every((v, i) => v === expected[i]), fixed);

  // The selected c' (tick = two carriers), the sun, the half-turn.
  const cp = scale(C2, 2);
  const r = zeros(8);
  for (let i = 0; i < 5; i += 1) r[(i + 1) % 5][i] = 4;
  for (let i = 5; i < 8; i += 1) r[i][i] = 4;
  let rp = eye4();
  for (const v of TWIN2) rp = mul(rp, reflect(v));
  add("c' is a Coxeter element in W(E8): order 30, 8 root orbits of 30",
    isWeyl(cp) && matOrder(cp) === 30 && orbitSizes(cp).every((k) => k === 30));
  add("the tick turns two carriers: c'^6 = r r' (r the K5 vertex rotation, r' the twin A4' rotation)",
    eq(pow(cp, 6), mul(r, rp)) && matOrder(r) === 5 && matOrder(rp) === 5);
  const sunSizes = orbitSizes(pow(cp, 10));
  add("the sun c'^10 permutes the roots in 80 triangles; c'^15 = -I",
    sunSizes.length === 80 && sunSizes.every((k) => k === 3) && eq(pow(cp, 15), neg(eye4())));
  add("c' = (-I) c'^10 c'^6: the half-turn times the sun times the tick",
    eq(cp, neg(mul(pow(cp, 10), pow(cp, 6)))));

  // The day clock and the exponent 7.
  const d = scale(D2, 2);
  add("the day d: order 24, d^4 = c'^5 (agrees on <720>), d c' = c'^7 d (the twist 7)",
    isWeyl(d) && matOrder(d) === 24 && eq(pow(d, 4), pow(cp, 5)) && eq(mul(d, cp), mul(pow(cp, 7), d)));
  add("d c'^-1 (the atlas 36 = 180 - 144 on the bath) has order 24, not 120",
    matOrder(mul(d, pow(cp, 29))) === 24);

  // Degree bound for orders of lattice automorphisms dividing 4320.
  const phi = (n: number) => Array.from({ length: n }, (_, k) => k + 1).filter((k) => gcd(k, n) === 1).length;
  const minDim = (m: number) => {
    if (m <= 2) return m - 1;
    let total = 0;
    for (const p of [2, 3, 5]) {
      let q = 1;
      while (m % (q * p) === 0) q *= p;
      if (q > 1) total += phi(q);
    }
    return m % 4 === 2 ? total - 1 : total;
  };
  const cand = Array.from({ length: N }, (_, k) => k + 1).filter((m) => N % m === 0 && minDim(m) <= 8);
  add("degree bound: orders m | 4320 possible in GL8(Z) are 1..30 on the list plus 16, 36, 40, 60",
    cand.join() === "1,2,3,4,5,6,8,9,10,12,15,16,18,20,24,30,36,40,60", cand);

  const residual = rows.filter((row) => !row.ok).length;
  return { residual, rows };
}
