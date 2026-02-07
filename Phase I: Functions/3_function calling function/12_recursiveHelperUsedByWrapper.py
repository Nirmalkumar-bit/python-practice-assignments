# Task: Implement digit_sum(n) recursively using a helper function.
# Requirements:
# - digit_sum(n) must call digit_sum_helper(n) and return its result.
# - digit_sum_helper(n) must be recursive (no loops).
# Expected outcome: print(digit_sum(4096)) outputs exactly: 19

def digit_sum_helper(n):
     if n == 0:
        return 0
     return n % 10 + digit_sum_helper(n // 10)
    # TODO: recursive implementation
    


def digit_sum(n):
     return digit_sum_helper(n)

    # TODO: call digit_sum_helper(n)
    


print(digit_sum(4096))
