# Goal: Use frozenset as an immutable set.
# Expected outcome:
# - Prints: "contains 2? True"
# - Prints: "union size: 4"

fs = frozenset({1, 2, 3})

# TODO: set has_two to whether 2 is in fs
has_two = 2 in fs

# TODO: create new_fs as union of fs with {4}
new_fs = fs | {4}

print("contains 2?", has_two)
print("union size:", len(new_fs))
