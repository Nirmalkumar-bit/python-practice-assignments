# Goal: Count vowels in each word using nested loops.
# Expected outcome for the given sentence:
# [('I', 1), ('love', 2), ('Python', 1)]

sentence = "I love Python"
vowels = "aeiouAEIOU"

words = sentence.split()
results = []
for word in words:
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
    results.append((word, count))

# TODO: Use an outer loop over words and an inner loop over characters.
# Count characters that are in vowels.
# Append (word, count) tuples to results.


print(results)