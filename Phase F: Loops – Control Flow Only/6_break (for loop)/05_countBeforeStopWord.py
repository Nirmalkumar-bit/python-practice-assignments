# Goal: Count how many words appear before the word 'STOP' (not included).
# Print the count.
# Expected outcome:
# 3

words = ["go", "north", "now", "STOP", "later"]

count = 0
for w in words:
    if w == "STOP":
        break
    # TODO: if w is 'STOP', break
    # TODO: otherwise increment count
    count+=1

print(count)
