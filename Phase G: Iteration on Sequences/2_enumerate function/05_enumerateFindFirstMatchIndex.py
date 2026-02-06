# Goal: Find the index of the first occurrence of a target using enumerate.
# Expected outcome:
# 1

nums = [5, 8, 2, 8, 9]
target = 8
found_index = None

# TODO: Use enumerate to set found_index to the first index where value == target, then stop looping.

for index, value in enumerate(nums):
    if value == target:
        found_index = index
        break

print(found_index)
