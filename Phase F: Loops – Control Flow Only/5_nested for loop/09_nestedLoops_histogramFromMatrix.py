# Goal: Build a frequency dictionary of numbers in a 2D grid using nested loops.
# Expected outcome for grid below:
# {1: 2, 2: 3, 3: 1}

grid = [
    [1, 2, 2],
    [3, 1, 2]
]

freq = {}
for row in grid:
    for val in row:
        freq[val] = freq.get(val, 0) + 1


# TODO: Use nested loops over rows and values.
# Update freq counts for each number.


print(freq)