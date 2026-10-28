// node --experimental-strip-types --no-warnings ports/ts/run.mjs
const audits = [
  ["coxeterSpine", "auditCoxeterSpine"],
  ["ledgerJoins", "auditLedgerJoins"],
  ["pauliBath", "auditPauliBath"],
];
let total = 0;
for (const [file, fn] of audits) {
  const url = new URL(`./${file}.ts`, import.meta.url);
  const mod = await import(url.href);
  const out = mod[fn]();
  for (const row of out.rows) console.log(row.ok ? "OK " : "BAD", row.name, row.ok ? "" : JSON.stringify(row.value));
  console.log(`${file}: residual ${out.residual}, rows ${out.rows.length}`);
  total += out.residual;
}
console.log("residual", total);
process.exitCode = total === 0 ? 0 : 1;
