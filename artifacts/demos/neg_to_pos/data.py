# Two points equidistant from the query under radius 0
# Distinguishable only with additional neighborhood context

VECTORS = {
    1: [0.0, 0.0],
    2: [0.0, 0.0],  # identical at radius 0
}

QUERY = [0.0, 0.0]

# Extra structure revealed at radius 1
NEIGHBORS = {
    1: [[1.0, 0.0]],
    2: [[0.0, 1.0]],
}
