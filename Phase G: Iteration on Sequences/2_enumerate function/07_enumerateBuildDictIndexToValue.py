# Goal: Build a dict mapping index -> value using enumerate.
# Expected outcome:
# {0: 'red', 1: 'green', 2: 'blue'}

colors = ["red", "green", "blue"]
index_map = {}

# TODO: Fill index_map using enumerate.
for index, color in enumerate(colors):
    index_map[index] = color

print(index_map)
