# TypeScript port of layer 19 (the spine)

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

## Running it here

```
node --experimental-strip-types --no-warnings ports/ts/run.mjs   # Node 22.6 or later
```

It takes about 2 seconds, and `python -m pytest` runs it when Node is available.
