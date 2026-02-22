import json
import hashlib
from importlib import resources
from jsonschema import validate

def _load_schema_v1() -> dict:
    schema_bytes = resources.files("cvre.schemas").joinpath("cvre-cert-v1.schema.json").read_bytes()
    expected = resources.files("cvre.schemas").joinpath("cvre-cert-v1.schema.sha256").read_text().strip()
    actual = hashlib.sha256(schema_bytes).hexdigest()
    if actual != expected:
        raise RuntimeError("schema hash mismatch")
    return json.loads(schema_bytes.decode("utf-8"))

def verify_certificate(cert: dict) -> None:
    schema = _load_schema_v1()
    validate(instance=cert, schema=schema)
