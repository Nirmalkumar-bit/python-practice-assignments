# Goal: Understand chaining comparisons and membership precedence.
# Fill in missing values so that the script prints exactly: True
# Do NOT change the structure of the expression.

# Expected outcome:
# When you run this file, it must print exactly:
# True

nums = [ 2, 2 ,5  ,4 ]
x = 2
# Expression uses a chained comparison plus membership test:
result = 1 < x <= 3 and x in nums
print(result)
