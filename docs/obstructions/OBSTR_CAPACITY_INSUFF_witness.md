OBSTR_CAPACITY_INSUFF Witness (v0.2)

Witness format
witness = {
  "H_min": number,
  "capacity_C": number,
  "steps_T": integer
}

Interpretation
- H_min: minimum bits required to certify the objective
- capacity_C: per-step information bound
- steps_T: declared maximum steps

Verifier Rule
Accept iff:
  H_min > capacity_C * steps_T
