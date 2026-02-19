import json
import sys
import pathlib

required_base = {
    "run_id","family","algo","n","m","k",
    "degree_var_target","degree_clause_target",
    "alpha","seed","t","event","time_ms"
}

step_extra = {
    "flipped_var","unsat","delta_unsat",
    "local_odd_count","stagnant_steps",
    "H_proxy_bits","H_proxy_kind"
}

terminate_extra = {
    "t_final","reason","unsat_final",
    "H_proxy_bits_final","wall_time_s"
}

def validate_file(path):
    seen_terminate = False
    with open(path) as f:
        for line in f:
            obj = json.loads(line)
            if not required_base.issubset(obj):
                raise ValueError(f"missing base fields in {path}")
            if obj["event"] == "step":
                if not step_extra.issubset(obj):
                    raise ValueError(f"missing step fields in {path}")
            if obj["event"] == "terminate":
                if not terminate_extra.issubset(obj):
                    raise ValueError(f"missing terminate fields in {path}")
                seen_terminate = True
    if not seen_terminate:
        raise ValueError(f"no terminate event in {path}")

if __name__ == "__main__":
    for p in pathlib.Path("runs").rglob("*.jsonl"):
        validate_file(p)

