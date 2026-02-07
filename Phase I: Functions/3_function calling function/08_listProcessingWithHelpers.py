# Task: Implement clamp(n, low, high) to keep n within [low, high].
# Implement clamp_all(nums, low, high) that calls clamp() for each number and returns a new list.
# Expected outcome: print(clamp_all([0, 5, 10, -3], 1, 8)) outputs exactly: [1, 5, 8, 1]

def clamp(n, low, high):
    if n < low:
        return low
    elif n > high:
        return high
    else:
        return n
    # TODO
    pass


def clamp_all(nums, low, high):
    result = []
    for n in nums:
        result.append(clamp(n, low, high))
    return result
    
    # TODO: build and return a new list
    


print(clamp_all([0, 5, 10, -3], 1, 8))
