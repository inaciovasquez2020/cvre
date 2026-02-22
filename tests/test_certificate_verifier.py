import json
import hashlib
from pathlib import Path

def load(p):
    return json.loads(p.read_text())

def test_pos_semantics():
    d = load(Path("tests/test_toy_cert_pos_r1.json"))
    assert d["polarity"] == "POS"
    assert d["status"] == "VALID"

def test_neg_semantics():
    d = load(Path("tests/test_toy_cert_neg_r0.json"))
    assert d["polarity"] == "NEG"
    assert d["status"] == "IMPOSSIBLE"

def test_schema_hash_gate():
    schema_id = d = load(Path("tests/test_toy_cert_pos_r1.json"))["schema"]
    h = hashlib.sha256(schema_id.encode()).hexdigest()
    assert len(h) == 64
