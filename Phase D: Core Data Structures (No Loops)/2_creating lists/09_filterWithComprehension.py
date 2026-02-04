# Given the list below, create a new list named long_words containing only words with length >= 5.
# Use a list comprehension.
# Print long_words.
# Expected outcome: ['tiger', 'zebra', 'giraffe']

words = ["ant", "tiger", "cat", "zebra", "ox", "giraffe"]

long_words = [word for word in words if len(word) >= 5]
print(long_words)
