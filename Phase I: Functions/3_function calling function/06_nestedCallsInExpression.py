# Task: Implement add(a, b) that returns a + b.
# Implement double(n) that returns n * 2.
# Implement compute(a, b, c) that returns double(add(a, b)) + c.
# Expected outcome: print(compute(2, 3, 4)) outputs exactly: 14

def add(a, b):
    return a + b
    # TODO
    pass


def double(n):
    return n * 2
    # TODO
    pass


def compute(a, b, c):
    return double(add(a, b)) + c
    
    # TODO: return double(add(a, b)) + c



print(compute(2, 3, 4))
