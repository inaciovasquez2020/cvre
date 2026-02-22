import json
from pathlib import Path
from jsonschema import validate, ValidationError

v1 = json.loads(Path("schemas/cvre-cert-v1.schema.json").read_text())
v2 = json.loads(Path("schemas/cvre-cert-v2.schema.json").read_text())

def load(p): return json.loads(Path(p).read_text())

def test_v1_instance_rejected_by_v2():
    inst = load("tests/test_toy_cert_pos_r1.json")
    try:
        validate(instance=inst, schema=v2)
        assert False
    except ValidationError:
        assert True
