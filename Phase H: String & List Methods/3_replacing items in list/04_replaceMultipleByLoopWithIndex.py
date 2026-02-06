# Goal: Replace all occurrences of a value by iterating with indexes.
# Expected outcome: printing the list shows [1, 0, 2, 0, 3, 0]

nums = [1, -1, 2, -1, 3, -1]

for i in range(len(nums)):
    if nums[i] == -1:
        nums[i] = 0

# TODO: replace every -1 with 0 using a for-loop over indexes.

print(nums)
