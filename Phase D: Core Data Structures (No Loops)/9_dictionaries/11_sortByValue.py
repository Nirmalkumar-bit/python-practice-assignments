# Goal: Print keys sorted by their values (descending).
# Expected outcome when run:
# ['c', 'a', 'b']

scores = {"a": 10, "b": 7, "c": 13}

# TODO: create a list of keys sorted by scores value descending
sorted_keys = sorted(scores, key=lambda k: scores[k], reverse=True)

print(sorted_keys)
