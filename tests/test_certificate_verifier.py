import json
from pathlib import Path
import cvre

def test_pos_certificate_schema_loads():
    p = Path("tests/test_toy_cert_pos_r1.json")
    data = json.loads(p.read_text())
    assert isinstance(data, dict)

def test_neg_certificate_schema_loads():
    p = Path("tests/test_toy_cert_neg_r0.json")
    data = json.loads(p.read_text())
    assert isinstance(data, dict)
