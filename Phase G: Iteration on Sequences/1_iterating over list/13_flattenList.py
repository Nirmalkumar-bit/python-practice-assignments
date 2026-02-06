# Flatten a list of lists into a single list in order and print it.
# Expected outcome:
# [1, 2, 3, 4, 5, 6]

nested = [[1, 2], [3], [4, 5, 6]]

flat = []
for sub in nested:
    for x in sub:
        flat.append(x)

print(flat)
