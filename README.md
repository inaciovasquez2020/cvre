CVRE (URF-Certified Vector Engine)

Purpose
Provide vector retrieval with URF-admissibility certificates.

Interface
insert(v, meta)
query(q, r, k) -> {results, certificate}
verify(certificate) -> OK | FAIL

Status
Spec + schemas + verifier skeleton.
