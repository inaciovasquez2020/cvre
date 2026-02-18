CVRE v0.2 (URF-Certified Vector Engine)

Goal
Return (results, CERT) where CERT is verifier-checkable for URF-admissibility.

Artifacts
EMBEDDING_SPEC.json
CONTROLLER_SPEC.json
CAPACITY_LEDGER.log
URF_CERT_POS.json / URF_CERT_NEG.json
TRANSCRIPT.log (or hash commitment)

Interface
insert(v, meta)
query(q, r, k, T) -> (R, CERT)
verify(CERT) -> OK | FAIL
