import json, hashlib
from pathlib import Path
from jsonschema import validate

SCHEMA_PATH = Path("schemas/cvre-cert-v1.schema.json")
SCHEMA_HASH = Path("schemas/cvre-cert-v1.schema.sha256").read_text().strip()
SCHEMA = json.loads(SCHEMA_PATH.read_text())

def load(p):
    return json.loads(p.read_text())

def test_schema_hash_matches():
    h = hashlib.sha256(SCHEMA_PATH.read_bytes()).hexdigest()
    assert h == SCHEMA_HASH

def test_pos_certificate_validates():
    d = load(Path("tests/test_toy_cert_pos_r1.json"))
    validate(instance=d, schema=SCHEMA)
    assert d["polarity"] == "POS"
    assert d["status"] == "VALID"

def test_neg_certificate_validates():
    d = load(Path("tests/test_toy_cert_neg_r0.json"))
    validate(instance=d, schema=SCHEMA)
    assert d["polarity"] == "NEG"
    assert d["status"] == "IMPOSSIBLE"
