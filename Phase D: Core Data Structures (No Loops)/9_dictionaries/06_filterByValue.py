# Goal: Create a new dict containing only entries meeting a condition.
# Expected outcome when run:
# {'b': 12, 'd': 9}

scores = {"a": 3, "b": 12, "c": 5, "d": 9}
passed = {}

for k, v in scores.items():
    if v >= 8:
        passed[k] = v

# TODO: copy into passed only items with value >= 8

print(passed)
