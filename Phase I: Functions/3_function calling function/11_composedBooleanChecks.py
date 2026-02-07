# Task: Implement has_length_between(s, low, high) inclusive.
# Implement is_alpha_only(s) to return True if all characters are letters A-Z/a-z.
# Implement is_valid_username(s) that calls both helpers and returns True only if both pass.
# Expected outcome: print(is_valid_username("AdaLovelace")) outputs exactly: True

def has_length_between(s, low, high):
     return low <= len(s) <= high


    # TODO
    


def is_alpha_only(s):
    return s.isalpha()

    # TODO
    


def is_valid_username(s):
    return has_length_between(s, 3, 20) and is_alpha_only(s)
    
    # TODO: call both helpers
    


print(is_valid_username("AdaLovelace"))
