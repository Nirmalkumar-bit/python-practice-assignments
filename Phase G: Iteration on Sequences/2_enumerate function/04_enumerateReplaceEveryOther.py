# Goal: Replace every other word (odd index) with "_" using enumerate.
# Expected outcome:
# ['keep', '_', 'keep', '_', 'keep']

words = ["keep", "remove", "keep", "remove", "keep"]

# TODO: Modify the list in-place: if index is odd, set words[index] = "_".
for index, word in enumerate(words):
    if index % 2 == 1:
        words[index] = "_"


print(words)
