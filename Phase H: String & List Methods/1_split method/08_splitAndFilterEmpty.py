# Split a string by ',' and remove empty fields.
# Expected outcome: prints ['a', 'b', 'c']

s = "a,,b,,,c,"
raw = s.split(",")
filtered = [item for item in raw if item ]
print(filtered)
