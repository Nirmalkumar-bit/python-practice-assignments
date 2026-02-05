# Goal: Find all unique index pairs (i, j) with i < j such that nums[i] + nums[j] == target.
# Expected outcome for nums and target below (pairs of indices):
# [(0, 3), (1, 2)]

nums = [2, 7, 5, 0]
target = 2

pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((i, j))

print(pairs)

            

# TODO: Use nested loops with i from 0..len(nums)-1 and j from i+1..len(nums)-1.
# If nums[i] + nums[j] equals target, append (i, j) to pairs.


