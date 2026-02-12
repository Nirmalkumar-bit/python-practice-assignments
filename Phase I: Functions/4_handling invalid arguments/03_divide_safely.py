# Task: Implement divide(a, b) with strict argument handling.
# Requirements:
# - a and b must be int or float (bool is NOT allowed)
#   If invalid, raise TypeError("a and b must be numbers")
# - If b == 0, raise ValueError("b must not be zero")
# - Otherwise return a / b
# Expected outcome:
# - divide(10, 2) returns 5.0
# - divide(10, 0) raises ValueError("b must not be zero")
# - divide(True, 2) raises TypeError("a and b must be numbers")


def divide(a, b):
    if (
        not isinstance(a, (int, float)) or isinstance(a, bool) or
        not isinstance(b, (int, float)) or isinstance(b, bool)
    ):
        raise TypeError("a and b must be numbers")
    
    # Check division by zero
    if b == 0:
        raise ValueError("b must not be zero")
    
    return a / b

    # TODO
    pass


if __name__ == "__main__":
    print(divide(10, 2))