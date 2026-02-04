# Goal: Use 'in' with case-insensitive matching.
# Expected outcome:
# - Prints exactly:
#   True
#   False

sentence = "Learning Python is fun"

# TODO: Make the checks case-insensitive by transforming sentence and/or the query.
print("Python " in sentence)  # should check whether "python" is in the sentence (case-insensitive)
print("JAVA" in  sentence)  # should check whether "JAVA" is in the sentence (case-insensitive)
