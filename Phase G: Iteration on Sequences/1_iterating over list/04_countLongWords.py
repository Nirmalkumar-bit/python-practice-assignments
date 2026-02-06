# Count how many words have length >= 5 and print the count.
# Expected outcome:
# 3

words = ["tree", "apple", "sun", "water", "stone"]

count = 0
for w in words:
    if len(w)>= 5:
        count += 1

print(count)
