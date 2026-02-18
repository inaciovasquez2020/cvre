# CVRE Artifacts and Verifiability

This document enumerates all artifacts produced by CVRE and what each guarantees.

---

## Certificate Types

### POS Certificate
Guarantees:
- Objective achieved
- Under declared admissibility constraints
- Without silent amplification

Verifiable offline.

---

### NEG Certificate
Guarantees:
- Objective impossible under constraints
- Structural obstruction identified

Not a failure; a proof of impossibility.

---

## What Is Verifiable

- Certificate structure
- Obstruction validity
- Constraint consistency
- Transcript commitments

---

## What Is Explicitly Out of Scope

- Embedding semantics
- Fairness or bias
- Privacy beyond capacity bounds
- Performance claims

---

## Reproducibility

All certificates are deterministic artifacts.
Verification requires only the public verifier.

