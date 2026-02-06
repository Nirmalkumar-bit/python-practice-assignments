# Print each item with a 1-based index prefix.
# Expected outcome:
# 1: red
# 2: green
# 3: blue

colors = ["red", "green", "blue"]

# TODO: iterate using a counter starting at 1
index = 1
for color in colors:
    print(str(index) + ": " + color)
    index +=1
