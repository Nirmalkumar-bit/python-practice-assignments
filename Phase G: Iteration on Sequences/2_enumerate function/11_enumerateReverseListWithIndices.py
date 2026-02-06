# Goal: Print original indices while iterating values in reverse.
# Expected outcome:
# 3 d
# 2 c
# 1 b
# 0 a

letters = ["a", "b", "c", "d"]

# TODO:
# Iterate over the list in reverse but show the original index.
# Hint: use enumerate(reversed(letters)) and compute original index.
n = len(letters)
for rev_index, letter in enumerate(reversed(letters)):
    original_index = n - 1 - rev_index
    print(f"{original_index} {letter}")