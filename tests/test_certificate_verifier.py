import json, hashlib
from pathlib import Path
from importlib import resources
from jsonschema import validate

def load_schema():
    with resources.files("cvre.schemas").joinpath("cvre-cert-v1.schema.json").open("rb") as f:
        schema_bytes = f.read()
    with resources.files("cvre.schemas").joinpath("cvre-cert-v1.schema.sha256").open("r") as f:
        expected = f.read().strip()
    assert hashlib.sha256(schema_bytes).hexdigest() == expected
    return json.loads(schema_bytes.decode())

def test_pos_semantics():
    d = json.loads(Path("tests/test_toy_cert_pos_r1.json").read_text())
    schema = load_schema()
    validate(instance=d, schema=schema)
    assert d["polarity"] == "POS"
    assert d["status"] == "VALID"

def test_neg_semantics():
    d = json.loads(Path("tests/test_toy_cert_neg_r0.json").read_text())
    schema = load_schema()
    validate(instance=d, schema=schema)
    assert d["polarity"] == "NEG"
    assert d["status"] == "IMPOSSIBLE"
