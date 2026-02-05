# Goal: Find and print the first number in the list that is divisible by 7, then stop searching.
# Expected outcome:
# 21

nums = [10, 13, 21, 28, 35]

for n in nums:
    if n%7 == 0:
        print(n)
        break
    # TODO: if n is divisible by 7, print it and break
    
