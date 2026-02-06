# Goal: Build a list of (index, value) tuples using enumerate.
# Expected outcome:
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]

letters = ["A", "B", "C", "D"]
indexed = []

# TODO: Append (i, letter) for each element using enumerate.

for i, letter in enumerate(letters):
    indexed.append((i, letter))

print(indexed)