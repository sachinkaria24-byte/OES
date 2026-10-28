# TypeScript ports of layers 19 and 21 (the spine and the ledger joins)

`coxeterSpine.ts` is a self-contained audit for the sibling model
(`oes-integrated-20261028.zip`, `src/lib/model/`). It has no imports, and it uses
the same convention as the other audits: `auditCoxeterSpine()` returns
`{ residual: 0, rows }` when every row holds.

In the integrated model, the stops are integer tests such as `4 + 5 !== 4`.
This port checks things that can fail:

- the circle lemma against brute force;
- the tower 36 × 4 × 3 × 2 × 5 as a bijection on all 4320 elements;
- the E8 Coxeter element (order 30, 8 root orbits of 30);
- the fixed Bloch momenta 25 / 81 / 256;
- the tick as two carriers, c′⁶ = r r′;
- the sun's 80 triangles;
- the day clock's twist d c′ d⁻¹ = c′⁷;
- the degree bound on what can act on the bath.

The reference implementation is `oes/spine.py` (layer 19 of `python verify.py`).

`ledgerJoins.ts` (`auditLedgerJoins()`, reference `oes/ledger.py`, layer 21) adds the 28 October
ledger joins:

- the tick bit, checked on all 4320 elements: 864 lies in ⟨x⟩ iff 5 does not divide x, and the ledger's
  tick values agree with it;
- the explicit order-24 day element of W(E8) (from `data/clocks.json`), with d⁴ = c′⁵ and d c′ d⁻¹ = c′⁷;
- the tick as the commutator of the day and the Coxeter clock, d c′ d⁻¹ c′⁻¹ = c′⁶ = r r′;
- the day-Coxeter group of order 120 with centre ⟨c′⁵⟩, and its five conjugate day clocks, which the tick
  rotates and the day doubles;
- the golden clock (order 20, v⁴ = the tick, twist 11) and the golden matrix modulo 5;
- the mirror, an involution inverting the clock that acts on the carrier as the pentagon reflection;
- the day's quarter d⁶, which exchanges the carrier with its twin, with (d⁶)² = −I;
- the energy split 34 = 20 + (3 + 9) + 2 of the checked datum.

## Wiring into the sibling model

1. Copy `coxeterSpine.ts` into `src/lib/model/`.
2. In `residual.ts`, add the import:

   ```ts
   import { auditCoxeterSpine } from "./coxeterSpine";
   ```

3. Next to the other audits in `residual.ts`, add:

   ```ts
   const coxeterSpine = auditCoxeterSpine().residual === 0;
   ```

4. Append `&& coxeterSpine` to the conjunction that ends with `&& integrate`.
5. Do the same for `ledgerJoins.ts`: import `auditLedgerJoins`, add
   `const ledgerJoins = auditLedgerJoins().residual === 0;` and append `&& ledgerJoins`.

## Running it here

```
node --experimental-strip-types --no-warnings ports/ts/run.mjs   # Node 22.6 or later
```

It runs both audits in about 2 seconds, and `python -m pytest` runs it when Node is available.
