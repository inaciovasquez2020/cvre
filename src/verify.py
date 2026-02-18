import json
import sys
from pathlib import Path

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python -m src.verify path/to/cert.json")
        return 2

    cert_path = Path(sys.argv[1])
    cert = json.loads(cert_path.read_text(encoding="utf-8"))

    required = ["kind", "capacity_ledger_hash", "transcript_hash", "claim"]
    for k in required:
        if k not in cert:
            print(f"FAIL missing:{k}")
            return 1

    if cert["kind"] not in ("POS", "NEG"):
        print("FAIL bad:kind")
        return 1

    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
