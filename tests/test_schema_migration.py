import json
from importlib import resources
from jsonschema import validate, ValidationError

with resources.files("cvre.schemas").joinpath("cvre-cert-v1.schema.json").open() as f:
    v1 = json.load(f)

with resources.files("cvre.schemas").joinpath("cvre-cert-v2.schema.json").open() as f:
    v2 = json.load(f)

def test_v1_rejected_by_v2():
    inst = json.loads(open("tests/test_toy_cert_pos_r1.json").read())
    try:
        validate(instance=inst, schema=v2)
        assert False
    except ValidationError:
        assert True
