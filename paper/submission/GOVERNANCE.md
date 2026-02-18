# CVRE Regulator Walkthrough
## How to Audit a Vector Retrieval Claim End-to-End

This document explains how an independent auditor or regulator verifies a
vector retrieval claim using the Certified Vector Retrieval Engine (CVRE).
It assumes no trust in the operator and requires only the certificate files
and the public verifier.

---

## 1. What Is Being Audited?

A retrieval claim states that a system:
- attempted a specific retrieval objective (e.g., approximate nearest neighbor),
- under explicit admissibility constraints (locality, capacity, steps),
- and either succeeded legitimately or could not succeed by design.

CVRE produces a certificate for each claim. The certificate—not the system—
is the object of audit.

---

## 2. Inputs Required for Audit

An auditor needs only:
- the certificate file (JSON),
- the public CVRE verifier,
- the declared specification (embedded in the certificate).

No access to:
- the ANN backend,
- the embeddings,
- the dataset,
- or the runtime system
is required.

---

## 3. Certificate Types

### 3.1 Positive Certificate (POS)

A POS certificate asserts:
- the objective was achieved,
- within the declared admissibility constraints.

It includes:
- controller specification,
- capacity ledger commitment,
- transcript commitment,
- explicit objective claim.

### 3.2 Negative Certificate (NEG)

A NEG certificate asserts:
- no admissible process could achieve the objective,
- under the declared constraints.

It includes:
- the same commitments as POS,
- a structural obstruction witness.

NEG certificates are formal impossibility statements.

---

## 4. Audit Procedure (Mechanical)

### Step 1 — Verify the Certificate

Run:

cvre verify path/to/certificate.json

Outcome:
- `OK` → certificate is structurally valid
- `FAIL` → certificate is invalid and rejected

No interpretation is needed at this step.

---

## 5. Interpreting a NEG Certificate (Impossibility)

### Example: Radius Indistinguishability

Certificate:
demos/neg_to_pos/cert_neg.json

Declared constraint:
- locality radius r = 0

Obstruction:
- OBSTR_RADIUS_INDIFF

Interpretation:
- All candidates are locally identical at r = 0
- No algorithm respecting the constraint can distinguish them
- Failure is structural, not algorithmic

Conclusion:
- The system is compliant
- The task is impossible under the declared limits

---

## 6. Interpreting a POS Certificate (Bounded Success)

Certificate:
demos/neg_to_pos/cert_pos.json

Declared constraint:
- locality radius r = 1

Claim:
- approximate nearest neighbor identified

Interpretation:
- Additional neighborhood information is admissible
- Distinguishing structure becomes visible
- The objective is achieved legitimately

Conclusion:
- The system succeeded without violating constraints

---

## 7. Certified Transition: NEG → POS

This audit demonstrates a critical governance feature:

- At r = 0: NEG certificate (impossibility)
- At r = 1: POS certificate (success)

Only one constraint changed.
This rules out:
- hidden amplification,
- backend tricks,
- adaptive leakage.

---

## 8. Backend Independence

The auditor does not inspect:
- Faiss,
- zvec,
- or any ANN implementation.

The certificate outcome is invariant under backend choice.
This prevents vendor-specific loopholes.

---

## 9. What CVRE Does *Not* Certify

CVRE does not certify:
- semantic correctness,
- fairness or bias properties,
- privacy beyond declared capacity bounds,
- dataset quality,
- embedding quality.

CVRE certifies *legitimacy of inference*, not desirability.

---

## 10. Regulatory Interpretation

From a regulatory standpoint, CVRE provides:
- explicit inference limits,
- verifiable success claims,
- formal impossibility statements,
- auditability without system access.

This enables:
- defensible failure explanations,
- independent compliance checks,
- reproducible audits.

---

## 11. Compliance Decision Guide

| Certificate | Meaning | Regulatory Action |
|------------|--------|-------------------|
| POS | Objective achieved within bounds | Accept |
| NEG | Objective impossible within bounds | Accept (no violation) |
| FAIL | Invalid or malformed claim | Reject |

---

## 12. Summary

CVRE converts vector retrieval from an opaque heuristic into a governed,
auditable process. Regulators audit certificates—not implementations—enabling
clear compliance decisions without overreach.
