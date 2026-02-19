import json
import hashlib
import pathlib
from datetime import datetime

files = []
for p in pathlib.Path("runs").rglob("*.jsonl"):
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    files.append({"path": str(p), "sha256": h})

manifest = {
    "schema": "LOGGING_SCHEMA_v1",
    "generated_at": datetime.utcnow().isoformat(),
    "files": files
}

with open("meta/MANIFEST.json","w") as f:
    json.dump(manifest,f,indent=2)

