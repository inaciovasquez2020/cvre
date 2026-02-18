POS Verifier Math (CVRE v0.2)

Given a POS certificate with:
- query hash commitment
- returned ids R = {j_1,...,j_k}
- declared eps
- declared metric rho

Verifier checks (sound, conservative):
1) Distance integrity
   Recompute rho(q, v_{j_t}) for each returned id j_t.

2) Local-Oracle Witness Lower Bound
   Certificate must include a lower bound LB on d*(q):
     LB <= d*(q)
   computed only from admissible local evidence (radius r).

3) Approx condition (checkable)
   For at least one returned id j in R:
     rho(q, v_j) <= (1 + eps) * UB
   where UB is any certified upper bound on d*(q).
   Minimal UB is min_{j in R} rho(q, v_j).

Soundness note
Without a certified LB or UB derived from admissible evidence, only distance integrity can be verified, not approximation quality.
