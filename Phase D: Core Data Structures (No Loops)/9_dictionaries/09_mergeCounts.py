# Goal: Merge two count dictionaries by summing counts for matching keys.
# Expected outcome when run:
# {'apple': 5, 'banana': 2, 'orange': 5}

c1 = {"apple": 2, "banana": 2, "orange": 1}
c2 = {"apple": 3, "orange": 4}
merged = c1.copy()

for k, v in c2.items():
    merged[k] = merged.get(k, 0) + v


# TODO: start merged as a copy of c1
# TODO: add counts from c2 into merged (sum when key exists)

print(merged)
