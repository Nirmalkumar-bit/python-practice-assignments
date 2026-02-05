# Use star-unpacking to capture the middle elements.

nums = (5, 10, 15, 20, 25)

# TODO: unpack so that first=5, last=25, and middle contains the remaining values
first, *middle, last = nums
middle = list(middle)
print(first)
print(middle)
print(last)
# Expected outcome:
# 5
# [10, 15, 20]
# 25
