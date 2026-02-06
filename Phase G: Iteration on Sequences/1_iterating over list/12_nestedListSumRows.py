# For each row (sub-list), compute its sum and collect into a new list, then print.
# Expected outcome:
# [6, 9, 6]

matrix = [
    [1, 2, 3],
    [4, 5],
    [6]
]
row_sums = []

for row in matrix:
    s = 0
    for value in row:
        s += value 
    row_sums.append(s)
print(row_sums)