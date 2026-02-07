# Task: Implement min_max(nums) that returns a tuple (min_value, max_value).
# Implement range_width(nums) that calls min_max(nums) and returns max_value - min_value.
# Expected outcome: print(range_width([10, 2, 8, 3])) outputs exactly: 8

def min_max(nums):
     return min(nums), max(nums)
    # TODO
    


def range_width(nums):
    min_value, max_value = min_max(nums)
    return max_value - min_value

    # TODO: call min_max(nums), unpack result
    pass

print(range_width([10, 2, 8, 3]))
