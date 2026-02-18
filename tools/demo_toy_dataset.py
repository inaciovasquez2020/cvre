import json
from pathlib import Path
import math

def l2(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def write_json(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def main():
    V = {
        1: (0.0, 0.0),
        2: (0.0, 0.0),
        3: (0.0, 0.0),
        4: (10.0, 0.0),
        5: (10.0, 0.0),
        6: (10.0, 0.0),
    }
    q = (0.0, 0.0)

    embedding_spec = { "d": 2, "norm_bound": 10.0, "metric": "l2" }

    controller_r0 = { "radius": 0, "k": 3, "max_steps": 1, "state_bits": 32 }
    controller_r1 = { "radius": 1, "k": 3, "max_steps": 1, "state_bits": 32 }

    ids_sorted = sorted(V.keys(), key=lambda i: l2(q, V[i]))
    top3 = ids_sorted[:3]
    dists = [l2(q, V[i]) for i in top3]

    sig = "(0.0,0.0)"
    neg_cert = {
        "kind": "NEG",
        "embedding_spec": embedding_spec,
        "controller_spec": controller_r0,
        "capacity_ledger_hash": "dummy",
        "transcript_hash": "dummy",
        "obstruction": {
            "id": "OBSTR_RADIUS_INDIFF",
            "witness": {
                "radius": 0,
                "support_ids": [1,2,3],
                "local_stats": [
                    {"id": 1, "sig": sig},
                    {"id": 2, "sig": sig},
                    {"id": 3, "sig": sig}
                ]
            }
        }
    }

    pos_cert = {
        "kind": "POS",
        "embedding_spec": embedding_spec,
        "controller_spec": controller_r1,
        "capacity_ledger_hash": "dummy",
        "transcript_hash": "dummy",
        "claim": {
            "objective": "approx-nn",
            "metric": "l2",
            "eps": 0.0,
            "k": 3,
            "returned": top3,
            "distances": dists,
            "ub_dstar": min(dists)
        }
    }

    write_json("tests/toy_cert_neg_r0.json", neg_cert)
    write_json("tests/toy_cert_pos_r1.json", pos_cert)

    print("NEG at r=0 -> tests/toy_cert_neg_r0.json")
    print("POS at r=1 -> tests/toy_cert_pos_r1.json")

if __name__ == "__main__":
    main()
