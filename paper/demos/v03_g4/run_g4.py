import json
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np


@dataclass(frozen=True)
class G4Config:
    dim: int = 2
    k: int = 1
    seed: int = 0
    hnsw_ef_search_good: int = 64
    hnsw_ef_search_bad: int = 0


def dataset() -> Tuple[Dict[int, List[float]], List[float]]:
    """
    Deterministic dataset engineered to:
      - admit a clear true nearest neighbor (point 1)
      - induce HNSW failure when efSearch is extremely small
    """
    pts = {
        1: [0.0, 0.0],   # true NN
        2: [1.0, 0.0],
        3: [0.0, 1.0],
        4: [1.0, 1.0],
        5: [0.9, 0.9],
        6: [0.8, 0.8],
        7: [0.7, 0.7],
        8: [0.6, 0.6],
    }
    q = [0.05, 0.05]
    return pts, q


def faiss_flat(ids: List[int], vecs: np.ndarray, q: np.ndarray, k: int) -> List[int]:
    import faiss
    index = faiss.IndexFlatL2(vecs.shape[1])
    index.add(vecs.astype(np.float32))
    _, I = index.search(q.astype(np.float32), k)
    return [ids[i] for i in I[0].tolist() if i >= 0]


def faiss_hnsw(
    ids: List[int],
    vecs: np.ndarray,
    q: np.ndarray,
    k: int,
    ef_search: int,
) -> List[int]:
    import faiss
    dim = vecs.shape[1]
    index = faiss.IndexHNSWFlat(dim, 16)
    index.hnsw.efConstruction = 64
    index.hnsw.efSearch = int(ef_search)
    index.add(vecs.astype(np.float32))
    _, I = index.search(q.astype(np.float32), k)
    return [ids[i] for i in I[0].tolist() if i >= 0]


def make_cert_pos_g4(results: Dict[str, List[int]], out_path: str) -> None:
    backends = sorted(results.keys())
    eq = results[backends[0]]

    cert = {
        "kind": "POS-G4",
        "capacity_ledger_hash": "demo",
        "transcript_hash": "demo",
        "controller_spec": {
            "radius": 1,
            "max_steps": 1,
        },
        "agreement": {
            "backends": backends,
            "results": results,
            "tolerance": "exact",
            "equivalence_class": eq,
        },
        "claim": {
            "objective": "approx-NN",
            "epsilon": 0.0,
            "winner": eq[0],
        },
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(cert, f, indent=2, sort_keys=True)


def make_cert_neg_g4(results: Dict[str, List[int]], out_path: str) -> None:
    cert = {
        "kind": "NEG-G4",
        "capacity_ledger_hash": "demo",
        "transcript_hash": "demo",
        "controller_spec": {
            "radius": 1,
            "max_steps": 1,
        },
        "divergence": {
            "backends": sorted(results.keys()),
            "results": results,
        },
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(cert, f, indent=2, sort_keys=True)


def main() -> int:
    cfg = G4Config()
    pts, q = dataset()

    ids = sorted(pts.keys())
    vecs = np.array([pts[i] for i in ids], dtype=np.float32)
    qv = np.array([q], dtype=np.float32)

    # Good case: both backends agree
    res_good = {
        "faiss_flat": faiss_flat(ids, vecs, qv, cfg.k),
        "faiss_hnsw": faiss_hnsw(
            ids, vecs, qv, cfg.k, cfg.hnsw_ef_search_good
        ),
    }

    # Bad case: HNSW under-searches
    res_bad = {
        "faiss_flat": faiss_flat(ids, vecs, qv, cfg.k),
        "faiss_hnsw": faiss_hnsw(
            ids, vecs, qv, cfg.k, cfg.hnsw_ef_search_bad
        ),
    }

    os.makedirs("paper/demos/v03_g4", exist_ok=True)
    make_cert_pos_g4(res_good, "paper/demos/v03_g4/cert_pos_g4.json")
    make_cert_neg_g4(res_bad, "paper/demos/v03_g4/cert_neg_g4.json")

    print("POS-G4 results:", res_good)
    print("NEG-G4 results:", res_bad)

    if res_good["faiss_flat"] != res_good["faiss_hnsw"]:
        raise RuntimeError("POS-G4 invariant violated")

    if res_bad["faiss_flat"] == res_bad["faiss_hnsw"]:
        raise RuntimeError("NEG-G4 divergence not triggered")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

