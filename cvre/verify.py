import hashlib, json
from pathlib import Path
from jsonschema import validate

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "cvre-cert-v1.schema.json"
HASH_PATH = Path(__file__).resolve().parent.parent / "schemas" / "cvre-cert-v1.schema.sha256"

def load_schema():
    schema = json.loads(SCHEMA_PATH.read_text())
    expected = HASH_PATH.read_text().strip()
    actual = hashlib.sha256(SCHEMA_PATH.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError("schema hash mismatch")
    return schema

def verify_certificate(cert: dict) -> None:
    schema = load_schema()
    validate(instance=cert, schema=schema)
