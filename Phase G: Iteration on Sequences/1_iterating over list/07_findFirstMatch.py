# Find the first number greater than 10 and print it.
# Expected outcome:
# 12

nums = [3, 7, 9, 12, 15]

result = None
for n in nums:
    if n > 10:
        result = n
        break

print(result)
