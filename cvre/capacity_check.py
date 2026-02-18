import json
from pathlib import Path

def check_ledger(path: Path) -> tuple[bool, str]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if "C" not in obj or "steps" not in obj:
        return False, "missing:C_or_steps"
    C = obj["C"]
    total = 0.0
    for s in obj["steps"]:
        if "delta_I" not in s:
            return False, "missing:delta_I"
        total += float(s["delta_I"])
        if float(s["delta_I"]) > float(C) + 1e-12:
            return False, "delta_I_exceeds_C"
    if total > float(C) * len(obj["steps"]) + 1e-12:
        return False, "sum_exceeds_CT"
    return True, "OK"
