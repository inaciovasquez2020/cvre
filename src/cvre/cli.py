import sys
import argparse
import json
from pathlib import Path
from cvre.verify import verify_certificate

def main():
    ap = argparse.ArgumentParser(prog="cvre")
    sub = ap.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("verify", help="Verify a CVRE certificate")
    v.add_argument("cert", help="Path to certificate JSON")

    args = ap.parse_args()

    if args.cmd == "verify":
        cert_path = Path(args.cert)
        if not cert_path.exists():
            sys.stderr.write(f"error: certificate not found: {cert_path}\n")
            return 2
        cert = json.loads(cert_path.read_text(encoding="utf-8"))
        verify_certificate(cert)
        return 0

    return 1
