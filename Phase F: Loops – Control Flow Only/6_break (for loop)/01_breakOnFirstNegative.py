# Goal: Print numbers from the list until the first negative number appears (do not print the negative).
# Expected outcome:
# 4
# 2
# 7

nums = [4, 2, 7, -1, 9]

for n in nums:
    if n < 0:
        break
    # TODO: if n is negative, stop the loop
    # TODO: otherwise print n
    print(n)
