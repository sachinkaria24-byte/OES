// node --experimental-strip-types --no-warnings ports/ts/run.mjs
const url = new URL("./coxeterSpine.ts", import.meta.url);
const { auditCoxeterSpine } = await import(url.href);
const out = auditCoxeterSpine();
for (const row of out.rows) console.log(row.ok ? "OK " : "BAD", row.name, row.ok ? "" : JSON.stringify(row.value));
console.log("residual", out.residual, "rows", out.rows.length);
process.exitCode = out.residual === 0 ? 0 : 1;
