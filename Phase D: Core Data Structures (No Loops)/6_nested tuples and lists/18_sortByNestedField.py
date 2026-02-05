# Goal: Sort a list of (name, (age, score)) by score descending
# Expected outcome: running this file prints exactly: [('Bea', (19, 92)), ('Cal', (21, 88)), ('Ada', (20, 75))]

records = [
    ("Ada", (20, 75)),
    ("Bea", (19, 92)),
    ("Cal", (21, 88))
]

# TODO: produce sorted_records sorted by inner score (second item of inner tuple), highest first
sorted_records = sorted(records, key=lambda r: r[1][1], reverse=True)


print(sorted_records)
