# Swap items in pairs in-place: (0 with 1), (2 with 3), ... then print the list.
# Expected outcome:
# ["b", "a", "d", "c", "e"]

items = ["a", "b", "c", "d", "e"]

# TODO: swap adjacent pairs using indices
for i in range(0, len(items) -1,2):
    # swap items[i] and items[i+1]
    items[i], items[i + 1] = items[i + 1], items[i]

print(items)
