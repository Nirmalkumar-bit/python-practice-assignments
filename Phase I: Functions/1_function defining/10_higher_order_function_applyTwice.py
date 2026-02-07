# Define a function named apply_twice that takes:
# - func: a function that takes one argument and returns a value
# - value: any value
# It returns func(func(value)).
# Also define a function named increment that takes an integer n and returns n + 1.
# Then print apply_twice(increment, 3).

# TODO: define apply_twice(func, value)
def apply_twice(func, value):
    return func(func(value))

# TODO: define increment(n)
def increment(n):
    return n + 1

print(apply_twice(increment, 3))

# Expected outcome (exact):
# 5
