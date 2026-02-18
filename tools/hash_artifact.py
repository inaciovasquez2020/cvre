import hashlib
import sys
from pathlib import Path

def h(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python tools/hash_artifact.py <file>")
        raise SystemExit(2)
    print(h(Path(sys.argv[1])))
