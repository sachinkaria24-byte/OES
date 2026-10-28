// Drop-in audit for the sibling model (src/lib/model): the 28 October ledger joins,
// unified. No imports. Same convention as the other audits: auditLedgerJoins()
// returns { residual: 0 } when every row holds.
//
// Python reference: oes/ledger.py (layer 21 of `python verify.py`) in
// sachinkaria24-byte/OES, branch claude/lagrangian-spectral-spacetime-model-t2253b.
// The matrices below are data/clocks.json: elements of W(E8) in standard E8
// coordinates, scaled by 4, so products stay integral: (4A)(4B)/4 = 4(AB).

type Mat = number[][];
type Row = { name: string; ok: boolean; value?: unknown };

const N = 4320;
const TICK = 864;
const gcd = (a: number, b: number): number => (b === 0 ? Math.abs(a) : gcd(b, a % b));
const holdsTick = (x: number) => TICK % gcd(((x % N) + N) % N, N) === 0;
const order = (a: number) => N / gcd(((a % N) + N) % N, N);

const eye4 = (): Mat => Array.from({ length: 8 }, (_, i) => Array.from({ length: 8 }, (_, j) => (i === j ? 4 : 0)));
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
const inv = (A: Mat): Mat => A[0].map((_, j) => A.map((row) => row[j])); // orthogonal
const eq = (A: Mat, B: Mat) => A.every((row, i) => row.every((v, j) => v === B[i][j]));
const neg = (A: Mat): Mat => A.map((row) => row.map((v) => -v));
const key = (A: Mat) => A.map((row) => row.join(",")).join(";");
const matOrder = (A: Mat, cap = 200) => {
  let P = A;
  for (let k = 1; k <= cap; k += 1) {
    if (eq(P, eye4())) return k;
    P = mul(P, A);
  }
  return 0;
};
const closure = (gens: Mat[]): Mat[] => {
  const seen = new Map<string, Mat>([[key(eye4()), eye4()]]);
  let frontier = [eye4()];
  while (frontier.length) {
    const next: Mat[] = [];
    for (const M of frontier)
      for (const g of gens) {
        const P = mul(M, g);
        const k = key(P);
        if (!seen.has(k)) {
          seen.set(k, P);
          next.push(P);
        }
      }
    frontier = next;
  }
  return [...seen.values()];
};

// data/clocks.json (x 4)
const COXETER = [[0,2,-2,0,2,2,0,0],[2,0,0,-2,0,0,2,2],[0,2,-2,0,-2,-2,0,0],[-2,0,0,-2,0,0,2,-2],[2,0,0,2,0,0,2,-2],[2,0,0,-2,0,0,-2,-2],[0,-2,-2,0,-2,2,0,0],[0,2,2,0,-2,2,0,0]];
const TICKM = [[-1,-1,-1,-1,3,1,1,-1],[3,-1,-1,-1,-1,1,1,-1],[-1,3,-1,-1,-1,1,1,-1],[-1,-1,3,-1,-1,1,1,-1],[-1,-1,-1,3,-1,1,1,-1],[1,1,1,1,1,-1,-1,-3],[-1,-1,-1,-1,-1,1,-3,-1],[1,1,1,1,1,3,-1,1]];
const CARRIER = [[0,0,0,0,4,0,0,0],[4,0,0,0,0,0,0,0],[0,4,0,0,0,0,0,0],[0,0,4,0,0,0,0,0],[0,0,0,4,0,0,0,0],[0,0,0,0,0,4,0,0],[0,0,0,0,0,0,4,0],[0,0,0,0,0,0,0,4]];
const TWIN = [[3,-1,-1,-1,-1,1,1,-1],[-1,3,-1,-1,-1,1,1,-1],[-1,-1,3,-1,-1,1,1,-1],[-1,-1,-1,3,-1,1,1,-1],[-1,-1,-1,-1,3,1,1,-1],[1,1,1,1,1,-1,-1,-3],[-1,-1,-1,-1,-1,1,-3,-1],[1,1,1,1,1,3,-1,1]];
const DAY = [[2,2,0,0,2,0,2,0],[0,0,2,2,0,-2,0,-2],[2,2,0,0,-2,0,-2,0],[0,0,-2,2,0,2,0,-2],[-2,2,0,0,-2,0,2,0],[0,0,-2,2,0,-2,0,2],[0,0,2,2,0,2,0,2],[-2,2,0,0,2,0,-2,0]];
const GOLDEN = [[-1,1,1,1,-1,1,3,-1],[-1,1,1,1,3,1,-1,-1],[1,-1,-1,-1,1,3,1,1],[1,3,-1,-1,1,-1,1,1],[-1,1,1,-3,-1,1,-1,-1],[3,1,1,1,-1,1,-1,-1],[-1,1,-3,1,-1,1,-1,-1],[-1,1,1,1,-1,1,-1,3]];
const MIRROR = [[4,0,0,0,0,0,0,0],[0,0,0,0,4,0,0,0],[0,0,0,4,0,0,0,0],[0,0,4,0,0,0,0,0],[0,4,0,0,0,0,0,0],[0,0,0,0,0,4,0,0],[0,0,0,0,0,0,-4,0],[0,0,0,0,0,0,0,-4]];

// The 240 roots, doubled.
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
const apply = (A: Mat, v: number[]) => A.map((row) => row.reduce((acc, a, k) => acc + a * v[k], 0) / 4);
const rootSet = new Set(roots2.map((v) => v.join(",")));
const isWeyl = (A: Mat) => roots2.every((r) => rootSet.has(apply(A, r).join(",")));

// (value, holds the tick) for the tick sentences of FULL_UPDATE_20261028 and its join notes.
const CLAIMS: [number, boolean][] = [
  [12, true], [20, false], [32, true], [2, true], [34, true], [40, false], [200, false], [24, true],
  [27, true], [216, true], [21, true], [13, true], [8, true], [55, false], [2160, false], [3240, false],
  [1620, false], [5, false], [1080, false], [1440, false], [2880, false], [3, true], [10, false],
  [98, true], [62, true], [113, true], [101, true], [118, true], [160, false], [492, true], [2740, false],
  [2720, false], [3443, true], [960, false], [30, false], [6, true], [4, true], [84, true], [112, true],
  [128, true], [9000, false], [120, false], [60, false], [14400, false], [15, false], [36, true],
  [18, true], [16, true], [736, true], [155, false], [11, true], [192, true], [0, false], [14, true],
  [9, true], [1, true], [7, true], [77, true], [105, false], [224, true], [256, true], [243, true],
  [248, true], [252, true], [250, false], [640, false], [1280, false], [6400, false], [28, true],
  [92, true], [184, true], [481, true], [180, false], [137, true], [1370, false], [96, true],
  [768, true], [232, true], [280, false], [774, true],
];

export function auditLedgerJoins(): { residual: number; rows: Row[] } {
  const rows: Row[] = [];
  const add = (name: string, ok: boolean, value?: unknown) => rows.push({ name, ok, value });

  // (a) the tick bit
  let bit = true;
  for (let x = 0; x < N; x += 1) bit &&= holdsTick(x) === (x % 5 !== 0);
  add("the tick bit: 864 lies in <x> iff 5 does not divide x (all 4320 x)", bit);
  const divisors = Array.from({ length: N }, (_, k) => k + 1).filter((g) => N % g === 0);
  const levels = [0, 864, 1728, 2592, 3456];
  const holding = divisors.filter((g) => TICK % g === 0);
  add("24 of the 48 subgroups hold the tick, each with all five levels or only 0",
    divisors.length === 48 && holding.length === 24 &&
      divisors.every((g) => { const k = levels.filter((t) => t % g === 0).length; return k === 1 || k === 5; }));
  const wrong = CLAIMS.filter(([x, c]) => holdsTick(x) !== c || (x % 5 !== 0) !== c);
  add(`the ${CLAIMS.length} tick values of the sibling ledger are that bit`, wrong.length === 0, wrong);
  add("the bit is not additive: 2 and 3 hold the tick, 2 + 3 = 5 does not",
    holdsTick(2) && holdsTick(3) && !holdsTick(5));

  // (b) the clocks
  const c = COXETER, d = DAY, t = TICKM, v = GOLDEN, m = MIRROR;
  add("all seven matrices lie in W(E8)", [c, t, CARRIER, TWIN, d, v, m].every(isWeyl));
  add("tick = c'^6 = r r' (two carrier rotations)", eq(pow(c, 6), t) && eq(mul(CARRIER, TWIN), t));
  add("the day d: order 24, d^4 = c'^5, d c' d^-1 = c'^7 (the order-24 element in W(E8))",
    matOrder(d) === 24 && eq(pow(d, 4), pow(c, 5)) && eq(mul(mul(d, c), inv(d)), pow(c, 7)));
  add("the tick is the commutator: d c' d^-1 c'^-1 = c'^6", eq(mul(mul(mul(d, c), inv(d)), inv(c)), t));
  add("the day doubles the tick: d (r r') d^-1 = (r r')^2", eq(mul(mul(d, t), inv(d)), mul(t, t)));
  const G = closure([c, d]);
  const has = (H: Mat[], M: Mat) => H.some((X) => eq(X, M));
  const centre = G.filter((z) => eq(mul(z, c), mul(c, z)) && eq(mul(z, d), mul(d, z)));
  add("the day-Coxeter group has order 120 and centre <c'^5> (order 6)",
    G.length === 120 && centre.length === 6 && centre.every((z) => [0, 5, 10, 15, 20, 25].some((k) => eq(z, pow(c, k)))));
  const D = closure([d]);
  const conjugates: Mat[][] = [];
  for (const x of G) {
    const H = D.map((y) => mul(mul(x, y), inv(x)));
    if (!conjugates.some((K) => H.every((h) => has(K, h)))) conjugates.push(H);
  }
  const act = (x: Mat) =>
    conjugates.map((K) => {
      const H = K.map((y) => mul(mul(x, y), inv(x)));
      return conjugates.findIndex((L) => H.every((h) => has(L, h)));
    });
  const pt = act(t);
  const pd = act(d);
  const base = conjugates.findIndex((K) => D.every((y) => has(K, y)));
  const label = new Map<number, number>();
  let cur = base;
  for (let k = 0; k < 5; k += 1) {
    label.set(cur, k);
    cur = pt[cur];
  }
  const ok5 = conjugates.length === 5 &&
    [0, 1, 2, 3, 4].every((i) => label.get(pt[i]) === ((label.get(i) ?? 0) + 1) % 5 &&
      label.get(pd[i]) === (2 * (label.get(i) ?? 0)) % 5);
  add("five conjugate day clocks: the tick rotates them (x -> x + 1), the day doubles them (x -> 2x)", ok5);
  add("the golden clock: order 20, v^4 = the tick, v c' v^-1 = c'^11",
    matOrder(v) === 20 && eq(pow(v, 4), t) && eq(mul(mul(v, c), inv(v)), pow(c, 11)));
  const B = [[1, 1], [1, 0]];
  let P = [[1, 0], [0, 1]];
  let goldenOrder = 0;
  let B4: number[][] = P;
  for (let k = 1; k <= 20; k += 1) {
    P = [[(P[0][0] * B[0][0] + P[0][1] * B[1][0]) % 5, (P[0][0] * B[0][1] + P[0][1] * B[1][1]) % 5],
      [(P[1][0] * B[0][0] + P[1][1] * B[1][0]) % 5, (P[1][0] * B[0][1] + P[1][1] * B[1][1]) % 5]];
    if (k === 4) B4 = P;
    if (!goldenOrder && P[0][0] === 1 && P[0][1] === 0 && P[1][0] === 0 && P[1][1] === 1) goldenOrder = k;
  }
  const N4 = [[B4[0][0] - 1, B4[0][1]], [B4[1][0], B4[1][1] - 1]];
  const N4sq = [[(N4[0][0] * N4[0][0] + N4[0][1] * N4[1][0]) % 5, (N4[0][0] * N4[0][1] + N4[0][1] * N4[1][1]) % 5],
    [(N4[1][0] * N4[0][0] + N4[1][1] * N4[1][0]) % 5, (N4[1][0] * N4[0][1] + N4[1][1] * N4[1][1]) % 5]];
  add("B = [[1,1],[1,0]] has order 20 mod 5 and B^4 is unipotent; <216> has order 20 with 4 x 216 = 864",
    goldenOrder === 20 && N4sq.flat().every((x) => x === 0) && N4.flat().some((x) => x !== 0) &&
      order(216) === 20 && 4 * 216 === TICK);
  add("the mirror: an involution inverting the clock and the tick, the pentagon reflection i -> -i on the carrier",
    eq(mul(m, m), eye4()) && eq(mul(mul(m, c), m), inv(c)) && eq(mul(mul(m, t), m), inv(t)) &&
      [0, 1, 2, 3, 4].every((i) => m[(5 - i) % 5][i] === 4));
  const q = pow(d, 6);
  const carrierRoots = roots2.filter((r) => r.slice(5).every((x) => x === 0) && r.slice(0, 5).reduce((a, b) => a + b, 0) === 0);
  const inTwin = (u: number[]) => carrierRoots.every((a) => a.reduce((s, x, i) => s + x * u[i], 0) === 0);
  add("the day's quarter d^6 exchanges the carrier A4 and its twin, and (d^6)^2 = -I",
    carrierRoots.length === 20 && carrierRoots.every((a) => inTwin(apply(q, a))) && eq(mul(q, q), neg(eye4())));

  // (c) the energy split of the checked datum
  const E = [] as number[][];
  for (let i = 0; i < 5; i += 1) for (let j = i + 1; j < 5; j += 1) E.push([i, j]);
  const M = Array.from({ length: 5 }, (_, i) => E.map(([a, b]) => (a === i || b === i ? 1 : 0)));
  const MT = (x: number[]) => E.map(([a, b]) => x[a] + x[b]);
  const Mv = (y: number[]) => Array.from({ length: 5 }, (_, i) => E.reduce((s, [a, b], k) => s + (a === i || b === i ? y[k] : 0), 0));
  const dot = (a: number[], b: number[]) => a.reduce((s, x, i) => s + x * b[i], 0);
  const contrast = [1, -1, 0, 0, 0];
  const x0 = contrast.map((u) => u + 1);
  const y0 = MT(contrast);
  const vel = E.map(([a, b]) => ({ "0,1": 1, "1,2": -1, "2,3": 1, "0,3": -1 } as Record<string, number>)[`${a},${b}`] ?? 0);
  const quad = (z: number[]) => dot(z, Mv(MT(z)));                // <x, M M^T x>
  const uniform = 5 * 8;                                            // |1|^2 x 8
  const vertexContrast = 3 * dot(contrast, contrast);              // 3 |c|^2
  const edgeImage = dot(y0, MT(Mv(y0)));                            // <y, M^T M y>
  add("energy 34 = 20 + (3 + 9) + 2: quadratic form 64 = 40 + 6 + 18 and the cycle 4, E_V = 23, E_E = 11",
    M.length === 5 && quad(x0) === uniform + vertexContrast && edgeImage === 18 && dot(vel, vel) === 4 &&
      Mv(vel).every((x) => x === 0) && (quad(x0) + edgeImage + dot(vel, vel)) / 2 === 34 &&
      quad(x0) / 2 === 23 && (edgeImage + dot(vel, vel)) / 2 === 11);

  const residual = rows.filter((row) => !row.ok).length;
  return { residual, rows };
}
