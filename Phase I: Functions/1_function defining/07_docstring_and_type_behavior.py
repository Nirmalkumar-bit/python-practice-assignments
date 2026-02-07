# Define a function named clamp that takes three integers: x, low, high.
# It returns:
# - low if x < low
# - high if x > high
# - otherwise x
# Add a docstring that describes parameters and return behavior.
# Then print clamp(5, 0, 10), clamp(-3, 0, 10), clamp(99, 0, 10) each on its own line.

# TODO: define clamp(x, low, high) with a docstring
def clamp(x, low, high):
    if x < low:
        return low
    if x > high:
        return high
    return x    
    
print(clamp(5, 0, 10))
print(clamp(-3, 0, 10))
print(clamp(99, 0, 10))

# Expected outcome (exact):
# 5
# 0
# 10
