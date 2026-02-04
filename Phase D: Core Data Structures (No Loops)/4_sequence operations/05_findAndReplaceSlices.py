# Task: Replace a segment using slicing (do not use .replace()).
# Expected outcome:
# - fixed should be exactly: 'I like Python!'

s = "I like Java!"

# Replace 'Java' with 'Python' using slicing and concatenation.
start = 7# index where 'Java' starts
end = 11   # index right after 'Java'
fixed = s[:start] + "Python" + s[end:]

print(fixed)
