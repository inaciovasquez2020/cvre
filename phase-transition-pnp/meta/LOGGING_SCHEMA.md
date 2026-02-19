LOGGING SCHEMA — PHASE-TRANSITION PNP

Purpose
This repository records empirical phase-transition experiments supporting
locality-based complexity results. Logs are empirical witnesses only and do not
contain theoretical claims.

All data must be machine-readable, append-only, and reproducible.

------------------------------------------------------------
DIRECTORY STRUCTURE
------------------------------------------------------------

runs/
  planted_xor/
    parity_flip_v1/
      *.jsonl
  planted_ksat/
    parity_flip_v1/
      *.jsonl

summary/
  runs.csv
  aggregates.csv

meta/
  LOGGING_SCHEMA.md
  MANIFEST.json
  ENVIRONMENT.txt

------------------------------------------------------------
RUN IDENTIFICATION
------------------------------------------------------------

Each run MUST have a globally unique run_id.

Format:
<family>_<algo>_n<n>_alpha<a>_deg<d>_seed<s>

Example:
planted_xor_parity_flip_v1_n20000_alpha1.20_deg3_seed7

------------------------------------------------------------
PER-RUN TRACE FORMAT (JSONL)
------------------------------------------------------------

Each file contains one JSON object per line.
Each line corresponds to a single algorithmic event.

Required fields on every line:

{
  "run_id": string,
  "family": "planted_xor" | "planted_ksat",
  "algo": string,
  "n": integer,
  "m": integer,
  "k": integer,
  "degree_var_target": integer,
  "degree_clause_target": integer,
  "alpha": number,
  "seed": integer,
  "t": integer,
  "event": "step" | "checkpoint" | "terminate",
  "time_ms": integer
}

------------------------------------------------------------
STEP EVENT
------------------------------------------------------------

event = "step"

Additional required fields:

{
  "flipped_var": integer,
  "unsat": integer,
  "delta_unsat": integer,
  "local_odd_count": integer,
  "stagnant_steps": integer,
  "H_proxy_bits": number,
  "H_proxy_kind": string
}

H_proxy_kind MUST be one of:
- "rank_gap_lb"
- "constraint_residual_lb"
- "frozen_fraction_lb"

------------------------------------------------------------
CHECKPOINT EVENT
------------------------------------------------------------

event = "checkpoint"

Additional required fields:

{
  "unsat": integer,
  "H_proxy_bits": number,
  "checkpoint_reason": "interval" | "plateau" | "diagnostic"
}

------------------------------------------------------------
TERMINATION EVENT
------------------------------------------------------------

event = "terminate"

Additional required fields:

{
  "t_final": integer,
  "reason": "solved" | "max_steps" | "cycle_detected" | "timeout",
  "unsat_final": integer,
  "H_proxy_bits_final": number,
  "wall_time_s": number
}

Exactly one terminate event MUST appear per run.

------------------------------------------------------------
SUMMARY TABLE — runs.csv
------------------------------------------------------------

One row per run.

Header (fixed order):

run_id,family,algo,n,m,k,degree_var_target,degree_clause_target,alpha,seed,t_final,reason,unsat0,unsat_final,H0_bits,H_final_bits,wall_time_s

------------------------------------------------------------
AGGREGATE TABLE — aggregates.csv
------------------------------------------------------------

Aggregated statistics across runs.

Header:

family,algo,alpha,n_mean,n_min,n_max,runs,median_t_final,mean_t_final,std_t_final,median_H_slope

H_slope is estimated from linear regression of H_proxy_bits vs t.

------------------------------------------------------------
MANDATORY EXPERIMENTS
------------------------------------------------------------

The following experiments are REQUIRED for empirical sufficiency:

1. planted_xor, parity_flip_v1
   n >= 10^4
   bounded degree (3 or 4)
   alpha in {1.0, 1.1, 1.2, 1.3}
   >= 5 seeds per configuration

2. planted_ksat, parity_flip_v1
   k = 3
   n >= 10^4
   alpha above freezing threshold
   >= 3 seeds per configuration

------------------------------------------------------------
OPTIONAL EXPERIMENTS
------------------------------------------------------------

Optional but recommended:

- alternative local rules
- different parity heuristics
- higher degree variants
- random initial assignments
- noise injection

Optional experiments MUST still follow the same schema.

------------------------------------------------------------
REPRODUCIBILITY REQUIREMENTS
------------------------------------------------------------

meta/ENVIRONMENT.txt must record:
- OS
- CPU
- RAM
- compiler/interpreter versions
- commit hash of code

meta/MANIFEST.json must list:
- all run files
- SHA256 of each file
- generation timestamp

------------------------------------------------------------
STATUS
------------------------------------------------------------

This schema is frozen.
Any change requires a new schema version file.

