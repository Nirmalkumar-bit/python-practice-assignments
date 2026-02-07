# Task: Implement is_even(n) to return True if n is even.
# Implement describe_parity(n) that calls is_even(n) and returns "even" or "odd".
# Expected outcome: print(describe_parity(7)) outputs exactly: odd

def is_even(n):
    return n % 2 == 0

    
    # TODO
    


def describe_parity(n):
    if is_even(n):
        return "even"
    else:
        return "odd"
    
    
    
    # TODO: call is_even(n)
    


print(describe_parity(7))
