# Define a function named absolute_value that takes an integer n.
# If n is negative, return -n. Otherwise return n.
# Then print absolute_value(-8) and absolute_value(5) on separate lines.

# TODO: define absolute_value(n)
def absolute_value(n):
    if n < 0:
        return -n
    return n
    
    
print(absolute_value(-8))
print(absolute_value(5))

# Expected outcome (exact):
# 8
# 5
