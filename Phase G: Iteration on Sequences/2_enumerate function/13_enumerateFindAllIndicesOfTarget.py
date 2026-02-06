# Goal: Collect all indices where target occurs.
# Expected outcome:
# [1, 3, 4]

data = ["x", "y", "x", "y", "y", "z"]
target = "y"
indices = []

# TODO: Use enumerate to append every index where value == target.
for index, value in enumerate(data):
    if value == target:
        indices.append(index)

print(indices)
