# CVRE — Certified Vector Retrieval Engine

A certification layer for vector retrieval. Every query returns (results, certificate), where the certificate is independently verifiable and asserts either success under declared admissibility constraints (POS) or impossibility with a structural obstruction (NEG).

## Overview

CVRE wraps any vector search backend as a constrained oracle. It enforces explicit admissibility rules on how the oracle may be queried and emits a verifier-checkable certificate describing what was done and why the outcome is valid.

CVRE is not a vector database. It is a certification and verification layer.

## Core Idea

Each run declares:
- Objective (e.g., ε-ANN)
- Admissibility constraints (locality, capacity, non-amplification)
- Transcript commitments and capacity ledger

Return value:
- results
- certificate.json

## Objectives

Baseline objective: ε-Approximate Nearest Neighbor (ε-ANN)

A result v is valid if:
dist(q, v) ≤ (1 + ε) · d*(q)

Objectives are explicit and verifier-checked.

## Certificates

POS certificates assert the objective was achieved under the declared constraints.
NEG certificates assert impossibility under those constraints and include an obstruction witness.

Certificates are standalone JSON artifacts verifiable offline.

## Structural Obstructions

CVRE distinguishes algorithmic failure from structural impossibility.
NEG certificates name an obstruction class and include the minimal witness required by the verifier.

## Repository Structure

cvre/
  cvre/
  demos/
  docs/
  paper/
  schemas/
  tests/
  tools/

README.md
STATUS.md
CITATION.cff

## Quickstart

git clone https://github.com/inaciovasquez2020/cvre.git
cd cvre

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
pytest -q

## Verification

Schemas live in schemas/.
Certificates validate deterministically against the schemas.

## Status

See STATUS.md for canonical state and freeze policy.

## Relationship to URF

CVRE is aligned with URF admissibility principles.
Upstream references:
https://github.com/inaciovasquez2020/urf-core
https://github.com/inaciovasquez2020/scientific-infrastructure

## Citation

@software{Vasquez_CVRE_2026,
  author = {Vasquez, Inacio F.},
  title  = {CVRE: Certified Vector Retrieval Engine},
  year   = {2026},
  url    = {https://github.com/inaciovasquez2020/cvre}
}

## License

MIT

## Maintainer

Inacio F. Vasquez
Independent Researcher
