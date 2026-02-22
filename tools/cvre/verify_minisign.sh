#!/usr/bin/env bash
set -euo pipefail
PUB="certs/cvre/CVRE_CERT.pub"
minisign -Vm tests/test_toy_cert_pos_r1.json -p "$PUB"
minisign -Vm tests/test_toy_cert_neg_r0.json -p "$PUB"
