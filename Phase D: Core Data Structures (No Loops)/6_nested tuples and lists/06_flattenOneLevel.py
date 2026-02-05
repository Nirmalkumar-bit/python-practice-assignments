# Goal: Flatten a one-level nested list (list of lists)
# Expected outcome: running this file prints exactly: [1, 2, 3, 4, 5]

nested = [[1, 2], [3], [4, 5]]

# TODO: build flat as a new list with all numbers in order
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)
