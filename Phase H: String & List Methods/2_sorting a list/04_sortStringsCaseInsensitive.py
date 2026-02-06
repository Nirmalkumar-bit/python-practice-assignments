# Goal: Sort strings alphabetically ignoring case.
# Expected outcome: names must become ['alice', 'Bob', 'carol', 'Dave'].

names = ['Bob', 'alice', 'Dave', 'carol']

# TODO: sort names in-place, case-insensitive
# Hint: use key=...

names.sort(key=str.lower)
print(names)

