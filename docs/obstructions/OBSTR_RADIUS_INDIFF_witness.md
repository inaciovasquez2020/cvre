OBSTR_RADIUS_INDIFF Witness (v0.2)

Purpose
Witness that within declared radius r, all candidate points are locally indistinguishable.

Witness format
witness = {
  "radius": r,
  "support_ids": [i1,...,im],
  "local_stats": [
    {"id": i1, "sig": h1},
    ...
    {"id": im, "sig": hm}
  ]
}

Local signature requirement
sig encodes r-neighborhood statistics admissible to the controller.
Verifier rule
All sig values must be identical:
h1 = h2 = ... = hm
