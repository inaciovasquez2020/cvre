CVRE: A Certified Vector Retrieval Engine

Abstract
Modern vector retrieval systems provide fast approximate nearest-neighbor
search but offer no guarantees about what information was used, whether
results are admissible under fixed constraints, or whether failure indicates
algorithmic weakness or fundamental impossibility. CVRE introduces a
certification layer for vector retrieval. Every query returns both results
and a verifier-checkable certificate stating either that the retrieval
objective was achieved under explicit admissibility constraints, or that no
such retrieval is possible without violating those constraints.

---

1. Motivation

Vector databases are increasingly used as retrieval backbones for RAG,
search, and decision systems. However, existing systems suffer from three
structural deficiencies:

1) Silent amplification:
   Adaptive querying can extract more information than intended, without
   detection.

2) Ambiguous failure:
   When retrieval fails, it is unclear whether this is due to index error,
   embedding quality, insufficient search, or fundamental indistinguishability.

3) Non-auditability:
   There is no verifier-checkable artifact explaining what the system was
   allowed to observe or infer.

CVRE addresses these deficiencies by separating retrieval speed from
retrieval legitimacy.

---

2. System Model

CVRE is a governing layer, not a vector database.

- Any ANN backend may be used as a pure oracle.
- CVRE enforces admissibility constraints on how that oracle may be queried.
- CVRE emits certificates describing what was provably achieved or impossible.

A query returns:
  (results, certificate)

Certificates are standalone JSON artifacts verifiable by an independent
checker.

---

3. Admissibility Constraints

Each CVRE run is governed by declared constraints:

- Locality: oracle access is restricted to bounded-radius neighborhoods.
- Capacity: each refinement step injects at most C bits of information.
- Non-amplification: query parameters cannot adaptively increase power.

These constraints are logged in a capacity ledger and enforced by a
finite-state controller.

---

4. Retrieval Objectives

CVRE supports explicit retrieval objectives. In v0.2, the primary objective is:

Approximate Nearest Neighbor (approx-NN)

Given query q and dataset V:
- Let d*(q) be the true nearest-neighbor distance.
- A returned point v is eps-approximate if:
    dist(q, v) <= (1 + eps) * d*(q)

Objectives must be declared and verified; no implicit success criteria exist.

---

5. Certificates

CVRE produces two kinds of certificates.

Positive Certificate (POS)
A POS certificate asserts that the declared objective was achieved within the
admissibility constraints. It includes:
- the embedding contract
- controller parameters
- capacity ledger commitment
- transcript commitment
- an explicit objective claim

Negative Certificate (NEG)
A NEG certificate asserts that, under the declared admissibility constraints,
no algorithm can achieve the objective. It includes:
- the same commitments as POS
- a minimal obstruction witness

---

6. Structural Obstructions

CVRE distinguishes algorithmic failure from structural impossibility.

Example obstruction (v0.2):
OBSTR_RADIUS_INDIFF

If all candidate points are locally indistinguishable within the allowed
radius, then no admissible process can select a unique nearest neighbor.

NEG certificates explicitly identify such obstructions.

---

7. Core Theorem Statements (Informal)

Theorem 1 (Soundness)
If CVRE emits a POS certificate and the verifier accepts it, then the declared
retrieval objective was achieved under the declared admissibility constraints.

Theorem 2 (Impossibility Certification)
If CVRE emits a NEG certificate with a valid obstruction witness, then no
admissible refinement process satisfying the constraints can achieve the
objective.

Theorem 3 (Backend Invariance)
For fixed admissibility constraints, the existence of POS or NEG certificates
is independent of the choice of ANN backend.

---

8. Demonstration

The repository includes a toy dataset demonstrating:
- NEG at locality radius r = 0
- POS at radius r = 1

See docs/DEMO.md.

---

9. Scope and Non-Goals

CVRE does not:
- define embeddings
- guarantee semantic correctness
- replace ANN systems
- optimize retrieval speed

CVRE provides guarantees about legitimacy, not performance.

---

10. Status

Specification: Frozen (v0.2)
Verifier: Reference implementation
Backends: Oracle adapters
Intended use: research, audit, safety, governance

