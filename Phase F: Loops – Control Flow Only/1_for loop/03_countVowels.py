# Count vowels in the given text using a for loop.
# Vowels are: a, e, i, o, u (both lowercase and uppercase).
# Expected outcome for the given text: print 5

text = "Education"
vowels = "aeiouAEIOU"
count = 0

# TODO: Loop through each character and count vowels
for ch in text:
    if ch in vowels:
        count = count + 1

print(count)
