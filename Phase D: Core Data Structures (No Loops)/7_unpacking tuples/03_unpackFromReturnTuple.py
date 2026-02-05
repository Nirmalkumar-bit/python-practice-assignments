# A function returns a tuple. Unpack it into named variables and print them.

def stats(nums):
    return (min(nums), max(nums))

values = [7, 2, 9, 4]
lo = min(values)
# TODO: unpack the result of stats(values) into lo and hi
hi = max(values)
print(lo, hi)
# Expected outcome:
# 2 9
