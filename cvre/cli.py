import sys
from pathlib import Path
from cvre.verify import main as verify_main

def usage() -> int:
    print("usage: cvre verify <path/to/cert.json>")
    return 2

def main() -> int:
    if len(sys.argv) < 2:
        return usage()

    cmd = sys.argv[1]

    if cmd == "verify":
        if len(sys.argv) != 3:
            return usage()
        sys.argv = ["cvre-verify", sys.argv[2]]
        return verify_main()

    return usage()

if __name__ == "__main__":
    raise SystemExit(main())
