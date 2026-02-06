# Goal: Replace a range of items using slice assignment.
# Expected outcome: printing the list shows ['a', 'X', 'Y', 'e']

letters = ['a', 'b', 'c', 'd', 'e']

# TODO: replace the middle three items (b, c, d) with 'X', 'Y' using slice assignment.
letters[1:4] = ['X', 'Y']
print(letters)
