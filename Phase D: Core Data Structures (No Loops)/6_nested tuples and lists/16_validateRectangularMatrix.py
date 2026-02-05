# Goal: Check if a nested list is a rectangular matrix (all rows same length)
# Expected outcome: running this file prints exactly: True False

m1 = [[1, 2], [3, 4], [5, 6]]
m2 = [[1, 2, 3], [4, 5]]

# TODO: set is_rect1 and is_rect2 to booleans
is_rect1 = all(len(row) == len(m1[0]) for row in m1)
is_rect2 = all(len(row) == len(m2[0]) for row in m2)

print(is_rect1, is_rect2)
