# Goal: Step through the list and stop when the first 0 is found.
# Expected outcome (exact lines):
# checking 3
# checking 7
# checking 0
# found 0 at index 2

nums = [3, 7, 0, 9, 0]
for i in range(len(nums)):
    print("checking", nums[i])
    if nums[i] == 0:
        print("found 0 at index", i)
        break