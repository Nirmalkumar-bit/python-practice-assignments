# Create a new list with duplicates removed, preserving the first occurrence order.
# Print the resulting list.
# Expected outcome:
# ["a", "b", "c", "d"]

items = ["a", "b", "a", "c", "b", "d", "d"]

unique = []
seen = set()
for item in items:
    if item not in seen:
        unique.append(item)
        seen.add(item)

print(unique)

