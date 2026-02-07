# Task: Implement operation functions and a dispatcher that calls the right one.
# Implement add(a, b), sub(a, b), mul(a, b).
# Implement calculate(op, a, b):
# - if op is "+" call add
# - if op is "-" call sub
# - if op is "*" call mul
# - otherwise return "unsupported"
# Expected outcome: print(calculate("*", 6, 7)) outputs exactly: 42

def add(a, b):
    return a + b
    # TODO
    


def sub(a, b):
    return a - b
    # TODO
    


def mul(a, b):
    return a * b
    # TODO
    


def calculate(op, a, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    else:
        return "unsupported"

    # TODO: dispatch to helper functions
    


print(calculate("*", 6, 7))
