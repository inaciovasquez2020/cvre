from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional, Sequence

@dataclass(frozen=True)
class ZvecConfig:
    path: str
    collection_name: str = "cvre"
    vector_field: str = "embedding"
    dim: int = 0
    metric: str = "l2"

class ZvecANN:
    """
    Optional pure-oracle adapter for zvec.
    Requires zvec to be installed from source.
    """
    def __init__(self, cfg: ZvecConfig):
        try:
            import zvec
        except ImportError as e:
            raise RuntimeError(
                "zvec backend requested but zvec is not installed. "
                "Install from source or use FaissANN instead."
            ) from e

        if cfg.dim <= 0:
            raise ValueError("ZvecConfig.dim must be set > 0")

        self._zvec = zvec
        self._cfg = cfg

        schema = zvec.CollectionSchema(
            name=cfg.collection_name,
            vectors=zvec.VectorSchema(cfg.vector_field, zvec.DataType.VECTOR_FP32, cfg.dim),
        )

        self._col = zvec.create_and_open(path=cfg.path, schema=schema)

    def insert(self, ids: Sequence[int], vectors: Sequence[Sequence[float]], meta: Optional[Sequence[dict[str, Any]]] = None) -> None:
        zvec = self._zvec
        docs = []
        for t, (i, v) in enumerate(zip(ids, vectors)):
            payload = meta[t] if meta is not None else None
            docs.append(zvec.Doc(id=str(i), vectors={self._cfg.vector_field: list(v)}, payload=payload))
        self._col.insert(docs)

    def query(self, q: list[float], r: int, k: int) -> list[int]:
        zvec = self._zvec
        res = self._col.query(
            zvec.VectorQuery(self._cfg.vector_field, vector=list(q)),
            topk=int(k),
        )
        return [int(row["id"]) for row in res]
