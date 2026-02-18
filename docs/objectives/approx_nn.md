Approx-NN Objective (CVRE v0.2)

Domain
Vectors v_i in R^d, query q in R^d, metric rho (default: l2).

Exact NN distance
d*(q) := min_i rho(q, v_i).

(k, eps)-approx NN condition
A returned id j is (eps)-approx if:
rho(q, v_j) <= (1 + eps) d*(q).

Objective claim format (POS)
claim.objective = "approx-nn"
claim.metric = "l2" | "cosine" | "ip"
claim.eps >= 0
claim.k >= 1
claim.returned = [ids]
claim.distances = [rho(q, v_id)]
