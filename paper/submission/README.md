# CVRE Submission Bundle

This bundle contains the complete materials for evaluating the
Certified Vector Retrieval Engine (CVRE).

The core contribution is **certified vector retrieval**:
every retrieval attempt yields either a verifier-checkable success
certificate or a verifier-checkable impossibility certificate.

---

## Contents

- `cvre_short.pdf`  
  4–6 page paper (systems + theory audience).

- `DEMO.md`  
  Deterministic NEG → POS demonstration.

- `GOVERNANCE.md`  
  Regulator-facing walkthrough: how to audit a retrieval claim.

- `ARTIFACTS.md`  
  What artifacts exist, what they guarantee, and how to verify them.

---

## What to Review First

1. Read `cvre_short.pdf`
2. Skim `DEMO.md` (Figure 1 in concrete form)
3. Read `GOVERNANCE.md` if auditing or safety-focused

---

## Claims at a Glance

- Retrieval success is certified under explicit constraints
- Retrieval failure can be certified as structural impossibility
- Certificates are backend-independent and offline-verifiable
- No semantic, fairness, or privacy claims beyond declared bounds

---

## Verification (Optional)

To verify any certificate:

cvre verify <certificate.json>

No access to embeddings, ANN backend, or runtime system is required.

---

## Status

Version: v0.2.0 (frozen)  
All claims are final and non-speculative.
