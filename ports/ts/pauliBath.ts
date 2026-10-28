// Drop-in audit for the sibling model (src/lib/model): the saved Pauli generator
// L(M) = 240 M + 16 M^T - 16 tr(M) I on real 16 x 16 matrices is the E8 bath Laplacian
// on its 256 half-period modes, and -L is a GKSL generator with the 120 antisymmetric
// Paulis as jump operators. No imports. auditPauliBath() returns { residual: 0 } when
// every row holds.
//
// Python reference: oes/counts.py (pauli_bath, check_pauli_file, pauli_quotient; layer 22 of
// `python verify.py`) and data/pauli_half_periods.json in sachinkaria24-byte/OES,
// branch claude/lagrangian-spectral-spacetime-model-t2253b.
//
// The map: x = sum c_i alpha_i over the simple roots (Bourbaki order) goes to the product
// of the Dynkin words with c_i = 1. Each word is a tensor product of four real Paulis,
// with Y = X Z the antisymmetric one. Then L(phi(x)) = eps(pi x) phi(x), where
// eps(k) = 240 - sum over roots cos(k . rho) is the bath band function.

type Mat = number[][];
type Row = { name: string; ok: boolean; value?: unknown };

const LETTERS: Record<string, Mat> = {
  I: [[1, 0], [0, 1]],
  X: [[0, 1], [1, 0]],
  Z: [[1, 0], [0, -1]],
  Y: [[0, -1], [1, 0]],
};
const DYNKIN = ["IIIY", "IIXY", "IIYX", "IYZI", "XIXY", "ZXXY", "IZXY", "IXXY"]; // alpha_1 .. alpha_8
const EDGES = [[0, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [1, 3]];
const ALPHA2 = [ // the simple roots, doubled
  [1, -1, -1, -1, -1, -1, -1, 1],
  [2, 2, 0, 0, 0, 0, 0, 0],
  [-2, 2, 0, 0, 0, 0, 0, 0],
  [0, -2, 2, 0, 0, 0, 0, 0],
  [0, 0, -2, 2, 0, 0, 0, 0],
  [0, 0, 0, -2, 2, 0, 0, 0],
  [0, 0, 0, 0, -2, 2, 0, 0],
  [0, 0, 0, 0, 0, -2, 2, 0],
];

const kron = (A: Mat, B: Mat): Mat => A.flatMap((ra) => B.map((rb) => ra.flatMap((a) => rb.map((b) => a * b))));
const word = (w: string): Mat => [...w].map((c) => LETTERS[c]).reduce(kron);
const mul = (A: Mat, B: Mat): Mat => A.map((row) => B[0].map((_, j) => row.reduce((s, v, k) => s + v * B[k][j], 0)));
const eye = (n: number): Mat => Array.from({ length: n }, (_, i) => Array.from({ length: n }, (_, j) => (i === j ? 1 : 0)));
const eq = (A: Mat, B: Mat) => A.every((row, i) => row.every((v, j) => v === B[i][j]));
const scale = (A: Mat, s: number): Mat => A.map((row) => row.map((v) => s * v));
const generator = (M: Mat): Mat => {
  const t = M.reduce((s, row, i) => s + row[i], 0);
  return M.map((row, i) => row.map((v, j) => 240 * v + 16 * M[j][i] - (i === j ? 16 * t : 0)));
};
const dot = (a: number[], b: number[]) => a.reduce((s, v, k) => s + v * b[k], 0);
const adjacent = (i: number, j: number) => EDGES.some(([a, b]) => (a === i && b === j) || (a === j && b === i));
const anticommute = (u: string, v: string) =>
  [...u].filter((a, i) => a !== "I" && v[i] !== "I" && a !== v[i]).length % 2 === 1;
const even = (n: number) => ((n % 2) + 2) % 2 === 0;
const transpose = (A: Mat): Mat => A[0].map((_, j) => A.map((row) => row[j]));
const CARTAN = ALPHA2.map((a) => ALPHA2.map((b) => dot(a, b) / 4));

const roots2 = (): number[][] => {
  const R: number[][] = [];
  for (let i = 0; i < 8; i += 1)
    for (let j = i + 1; j < 8; j += 1)
      for (const si of [2, -2])
        for (const sj of [2, -2]) {
          const v = Array(8).fill(0);
          v[i] = si;
          v[j] = sj;
          R.push(v);
        }
  for (let m = 0; m < 256; m += 1) {
    const v = Array.from({ length: 8 }, (_, k) => ((m >> k) & 1 ? -1 : 1));
    if (v.filter((x) => x < 0).length % 2 === 0) R.push(v);
  }
  return R;
};

export function auditPauliBath() {
  const rows: Row[] = [];
  const R = roots2();
  rows.push({ name: "the 240 roots of E8", ok: R.length === 240 && R.every((r) => dot(r, r) === 8) });

  const gramOk = ALPHA2.every((a, i) =>
    ALPHA2.every((b, j) => dot(a, b) === (i === j ? 8 : adjacent(i, j) ? -4 : 0)),
  );
  rows.push({ name: "the simple roots form the E8 Dynkin diagram", ok: gramOk });

  const pattern = DYNKIN.every((u, i) => DYNKIN.every((v, j) => i === j || anticommute(u, v) === adjacent(i, j)));
  const odd = DYNKIN.every((w) => [...w].filter((a) => a === "Y").length % 2 === 1);
  rows.push({ name: "eight antisymmetric Paulis anticommute exactly along the diagram", ok: pattern && odd });

  const P = DYNKIN.map(word);
  const spectrum: Record<number, number> = {};
  const images = new Set<string>();
  const anti: Mat[] = [];
  let intertwines = true;
  let signs = true;
  for (let m = 0; m < 256; m += 1) {
    const c = Array.from({ length: 8 }, (_, k) => (m >> k) & 1);
    const x2 = ALPHA2[0].map((_, k) => c.reduce((s, ci, i) => s + ci * ALPHA2[i][k], 0));
    const eps = 240 - R.reduce((s, r) => s + (even(dot(r, x2) / 4) ? 1 : -1), 0);
    let M = eye(16);
    c.forEach((ci, i) => {
      if (ci) M = mul(M, P[i]);
    });
    const flat = M.flat();
    const lead = Math.sign(flat.find((v) => v !== 0) ?? 1);
    images.add(flat.map((v) => v * lead).join(","));
    intertwines = intertwines && eq(generator(M), scale(M, eps));
    spectrum[eps] = (spectrum[eps] ?? 0) + 1;
    const half = c.reduce((s, ci, i) => s + c.reduce((t, cj, j) => t + ci * cj * CARTAN[i][j], 0), 0) / 2;
    const odd = !even(half); // the E8 form x.x/2 mod 2
    signs = signs && eq(transpose(M), scale(M, odd ? -1 : 1)) && odd === (eps === 224);
    if (odd) anti.push(M);
  }
  rows.push({ name: "the 256 products are distinct up to sign: a bijection from the half-periods", ok: images.size === 256 });
  rows.push({ name: "L(phi(x)) = eps(pi x) phi(x) at every half-period", ok: intertwines });
  rows.push({
    name: "eps = 0, 224 (the E7+A1 saddles), 256 (the D8 band top) on 1, 120, 135 half-periods",
    ok: spectrum[0] === 1 && spectrum[224] === 120 && spectrum[256] === 135,
    value: spectrum,
  });

  rows.push({
    name: "phi(x)^T = (-1)^(x.x/2) phi(x): the 120 antisymmetric products sit at the 120 saddles (eps = 224)",
    ok: signs && anti.length === 120,
  });

  // GKSL: on every matrix unit E_ij, sum_A A E_ij A^T = 8 tr(E_ij) I - 8 E_ij^T, so by linearity
  // -L(X) = 2 sum_A (A X A^T - X) for every X, with the 120 antisymmetric A as jump operators.
  let twirl = anti.length === 120;
  for (let i = 0; i < 16 && twirl; i += 1)
    for (let j = 0; j < 16 && twirl; j += 1)
      for (let k = 0; k < 16; k += 1)
        for (let l = 0; l < 16; l += 1) {
          const s = anti.reduce((acc, A) => acc + A[k][i] * A[l][j], 0);
          if (s !== 8 * (i === j && k === l ? 1 : 0) - 8 * (k === j && l === i ? 1 : 0)) twirl = false;
        }
  rows.push({ name: "GKSL: sum over the 120 antisymmetric A of A X A^T = 8 tr(X) I - 8 X^T, so -L(X) = 2 sum (A X A^T - X)", ok: twirl });

  const residual = rows.filter((r) => !r.ok).length;
  return { residual, rows };
}
