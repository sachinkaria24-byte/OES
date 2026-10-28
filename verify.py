"""Run every layer of the OES end-to-end model and write results.json.

    python verify.py           # full run, including the nonlinear E8-bath flow
    python verify.py --fast    # skip the nonlinear flow (about 1 minute faster)

Exit code is nonzero if any check fails. A pass is a mathematical check on
constructed matrices. It is not AUTH, and no gate in oes/gates.py moves.
"""

import json
import sys
import time

from oes import carrier, cosmology, gates, gravity, native, observer, spacetime, spectral


def main(argv):
    fast = "--fast" in argv
    layers = [
        ("1-carrier", carrier.run),
        ("2-spectral", spectral.run),
        ("3-spacetime", spacetime.run),
        ("4-native", lambda: native.run(simulate=not fast)),
        ("5-observer", observer.run),
        ("6-gravity", gravity.run),
        ("7-cosmology", cosmology.run),
    ]
    checks, timing = [], {}
    for name, fn in layers:
        t = time.time()
        rep = fn()
        timing[name] = round(time.time() - t, 2)
        checks += rep.checks
        bad = [c for c in rep.checks if not c.passed]
        print(f"{name:13s} {len(rep.checks) - len(bad):3d}/{len(rep.checks):<3d} "
              f"({timing[name]}s)")
        for c in bad:
            print(f"   FAIL [{c.status}] {c.name}: {c.value}")
    by_status = {}
    for c in checks:
        by_status.setdefault(c.status, [0, 0])
        by_status[c.status][0] += c.passed
        by_status[c.status][1] += 1
    print("by status: " + ", ".join(f"{k} {p}/{n}" for k, (p, n) in by_status.items()))
    print("AUTH =", gates.GATES["AUTH"], "| ScientificGold =", gates.GATES["ScientificGold"])
    out = {"ledger": gates.ledger(), "timing_s": timing, "fast": fast,
           "summary": {k: {"passed": p, "total": n} for k, (p, n) in by_status.items()},
           "checks": [c.as_dict() for c in checks]}
    with open("results.json", "w") as f:
        json.dump(out, f, indent=1)
    return 0 if all(c.passed for c in checks) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
