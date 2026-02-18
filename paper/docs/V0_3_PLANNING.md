# CVRE v0.3 Planning
## New Guarantees Only (Non-Overlapping with v0.2)

This document specifies the scope, guarantees, and acceptance criteria for
CVRE v0.3. It explicitly excludes features already provided by v0.2.

v0.2 is frozen. v0.3 introduces only guarantees that are strictly stronger or
orthogonal, with no semantic overlap.

---

## 1. v0.2 Baseline (What Is Already Solved)

v0.2 provides:
- POS/NEG certificates for retrieval objectives
- Explicit admissibility constraints (locality, capacity, steps)
- Structural obstructions (radius indistinguishability, capacity insufficiency)
- Backend invariance
- Offline verification via a public CLI
- Governance and audit documentation

v0.3 MUST NOT repackage or restate these.

---

## 2. v0.3 Design Principle

Each v0.3 feature must satisfy ALL of the following:
- Introduces a strictly new guarantee
- Is independently verifiable
- Produces a new certificate field or certificate type
- Has a clear NEG counterpart (impossibility or violation)
- Can be audited without backend access

---

## 3. New Guarantee G1: Transcript Non-Adaptivity Certification

### Motivation
v0.2 prevents amplification by design but does not certify that a transcript
was non-adaptive in practice.

### Guarantee
v0.3 certifies that query parameters did not adapt to intermediate results.

### Artifact
- Transcript hash + non-adaptivity proof
- Deterministic replay witness

### Certificates
- POS-G1: transcript is provably non-adaptive
- NEG-G1: detected adaptive dependency

### Acceptance Criteria
- Verifier reconstructs transcript dependency graph
- Confirms acyclic, input-only dependence

---

## 4. New Guarantee G2: Cross-Objective Consistency

### Motivation
A system may succeed on one objective but implicitly contradict another
(e.g., nearest neighbor vs. cluster membership).

### Guarantee
v0.3 certifies that multiple declared objectives are mutually consistent
under the same admissibility constraints.

### Artifact
- Objective set specification
- Consistency witness or contradiction witness

### Certificates
- POS-G2: objectives jointly satisfiable
- NEG-G2: objectives mutually inconsistent

### Acceptance Criteria
- Verifier checks logical compatibility of objectives
- NEG includes minimal contradiction set

---

## 5. New Guarantee G3: Dataset-Size Lower Bound Certification

### Motivation
Some retrieval objectives are impossible below a minimum dataset size,
independent of algorithm.

### Guarantee
v0.3 certifies that the dataset cardinality meets the minimum size required
to satisfy the declared objective under the constraints.

### Artifact
- Dataset size commitment
- Lower-bound function reference

### Certificates
- POS-G3: dataset size sufficient
- NEG-G3: dataset size provably insufficient

### Acceptance Criteria
- Verifier checks size commitment against bound
- Bound is explicit and objective-specific

---

## 6. New Guarantee G4: Cross-Backend Agreement Certificate

### Motivation
Backend invariance in v0.2 is existential. v0.3 strengthens this to empirical
agreement across backends.

### Guarantee
v0.3 certifies that multiple independent backends produce compatible outcomes
under the same constraints.

### Artifact
- Backend set declaration
- Agreement witness (or divergence witness)

### Certificates
- POS-G4: backends agree within tolerance
- NEG-G4: backend divergence detected

### Acceptance Criteria
- Verifier checks result equivalence class
- NEG includes explicit disagreement evidence

---

## 7. New Guarantee G5: Constraint Tightness Certification

### Motivation
Operators may over-relax constraints. v0.3 certifies minimality.

### Guarantee
v0.3 certifies that constraints are near-minimal for success.

### Artifact
- Constraint sweep witness
- Tightness margin

### Certificates
- POS-G5: constraints are tight within margin
- NEG-G5: constraints unnecessarily loose

### Acceptance Criteria
- Verifier checks monotonic constraint relaxation
- Identifies minimal feasible boundary

---

## 8. Explicit Non-Goals for v0.3

v0.3 will NOT:
- add new ANN algorithms
- address embedding semantics
- claim privacy, fairness, or ethics
- optimize performance
- introduce learning or adaptation

---

## 9. Acceptance Checklist (v0.3 Release Gate)

v0.3 is complete if and only if:
- Each G1–G5 has POS and NEG certificates
- Verifier supports all new checks
- Each guarantee has a demo case
- No v0.2 certificate format changes are required
- Documentation clearly distinguishes v0.2 vs. v0.3 guarantees

---

## 10. Versioning and Compatibility

- v0.2 certificates remain valid forever
- v0.3 certificates are strictly additive
- No retroactive reinterpretation of v0.2

---

## 11. Summary

CVRE v0.3 extends certification from single-run legitimacy to
cross-run, cross-objective, and cross-backend guarantees.
It strengthens governance without expanding scope or ambiguity.
