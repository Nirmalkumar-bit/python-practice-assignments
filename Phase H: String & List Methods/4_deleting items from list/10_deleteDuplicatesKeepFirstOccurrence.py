# Delete duplicates in place, keeping the first occurrence
# Goal: Remove duplicates from nums IN PLACE while preserving order of first occurrences.
# Example: [2, 1, 2, 3, 1, 4, 3] -> [2, 1, 3, 4]
# Constraint: Do NOT create a second list of numbers (no new list like unique = []).
# You may use a set to track seen values.
# Expected output:
# nums: [2, 1, 3, 4]

nums = [2, 1, 2, 3, 1, 4, 3]
seen = set()
i = 0
# TODO: remove duplicates in place using deletions (del or pop)
# Hint: manage an index variable carefully as you delete.
while i < len(nums):
    if nums[i] in seen:
        del nums[i]      # remove duplicate
        # do NOT increment i here
    else:
        seen.add(nums[i])
        i += 1           
print('nums:', nums)
