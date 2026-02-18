CVRE Toy Demo

This demo shows a structural impossibility (NEG certificate) that disappears
when locality constraints are relaxed.

Dataset
Six points in R^2:
- Three identical points at (0,0)
- Three identical points at (10,0)

Query
q = (0,0)

Result
- radius = 0:
  All nearest candidates are locally indistinguishable.
  CVRE emits a NEG certificate (OBSTR_RADIUS_INDIFF).

- radius = 1:
  Local context breaks symmetry.
  CVRE emits a POS certificate for approx-NN.

Key Point
The backend does not matter.
The certificate depends only on admissibility constraints.
