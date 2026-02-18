import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: cvre verify path/to/cert.json")
        return 2

    cert_path = Path(sys.argv[1])
    cert = json.loads(cert_path.read_text(encoding="utf-8"))

    if "kind" not in cert:
        print("FAIL missing:kind")
        return 1

    kind = cert["kind"]

    allowed_kinds = {
        "POS",
        "NEG",
        "POS-G4",
        "NEG-G4",
    }

    if kind not in allowed_kinds:
        print("FAIL bad:kind")
        return 1

    for k in ("capacity_ledger_hash", "transcript_hash"):
        if k not in cert:
            print(f"FAIL missing:{k}")
            return 1

    if kind in ("POS", "POS-G4"):
        if "claim" not in cert:
            print("FAIL missing:claim")
            return 1

    if kind == "NEG":
        if "obstruction" not in cert:
            print("FAIL missing:obstruction")
            return 1

    if kind == "POS-G4":
        if "agreement" not in cert:
            print("FAIL missing:agreement")
            return 1

        ag = cert["agreement"]
        for k in ("backends", "results", "tolerance", "equivalence_class"):
            if k not in ag:
                print(f"FAIL missing:agreement.{k}")
                return 1

        backends = ag["backends"]
        results = ag["results"]
        eq = ag["equivalence_class"]

        for b in backends:
            if b not in results:
                print("FAIL missing:agreement.results.backend")
                return 1
            if results[b] != eq:
                print("FAIL bad:agreement.mismatch")
                return 1

    if kind == "NEG-G4":
        if "divergence" not in cert:
            print("FAIL missing:divergence")
            return 1

        dv = cert["divergence"]
        for k in ("backends", "results"):
            if k not in dv:
                print(f"FAIL missing:divergence.{k}")
                return 1

        backends = dv["backends"]
        results = dv["results"]

        vals = [results[b] for b in backends]
        if all(v == vals[0] for v in vals):
            print("FAIL bad:divergence.no_divergence")
            return 1

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

