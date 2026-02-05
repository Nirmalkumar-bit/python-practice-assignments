# Goal: Build a frequency dictionary for words.
# Expected outcome when run:
# {'red': 2, 'blue': 1, 'green': 2}

text = "red blue green red green"
words = text.split()
counts = {}

for w in words:
     counts[w] = counts.get(w, 0) + 1# TODO: update counts so each word is counted
     pass

print(counts)
