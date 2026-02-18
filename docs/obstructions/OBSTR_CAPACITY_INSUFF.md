ID
OBSTR_CAPACITY_INSUFF

Description
Capacity Insufficiency Obstruction.

Even if all local neighborhoods are accessible, the declared information
capacity (C, T) is insufficient to resolve the retrieval objective.

This obstruction is independent of locality radius.

Formal Condition
Let H be the minimum information required to certify the objective
(e.g., distinguishing among M equiprobable candidates requires log2(M) bits).

If:
  sum_t ΔI_t ≤ C * T < H
then no admissible process can succeed.

Witness
A lower bound H_min on required information, together with declared (C, T).

Verifier Rule
Check that:
  H_min > C * T
