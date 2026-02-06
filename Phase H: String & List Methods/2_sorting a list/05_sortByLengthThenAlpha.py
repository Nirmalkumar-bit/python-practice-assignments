# Goal: Sort words by length ascending, then alphabetically for ties.
# Expected outcome: words must become ['an', 'to', 'bee', 'ant', 'zoo', 'apple'].

words = ['apple', 'bee', 'an', 'zoo', 'ant', 'to']

# TODO: sort words with a key that sorts by (length, word)
words.sort(key=lambda w: (len(w), w))
print(words)
