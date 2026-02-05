# Goal: Invert a dictionary where values are unique.
# Expected outcome when run:
# {'A': 1, 'B': 2, 'C': 3}

original = {1: "A", 2: "B", 3: "C"}
inverted = {}
for k, v in original.items():
    inverted[v] = k

# TODO: invert original into inverted

print(inverted)
