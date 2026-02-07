# Task: Implement strip_spaces(s) that removes leading/trailing spaces.
# Implement normalize_name(s) that calls strip_spaces(s) and then uppercases the result.
# Expected outcome: print(normalize_name("  grace  ")) outputs exactly: GRACE

def strip_spaces(s):
    return s.strip()
    # TODO: return s without leading/trailing spaces



def normalize_name(s):
    return strip_spaces(s).upper()
    # TODO: call strip_spaces(s) then uppercase
    


print(normalize_name("  grace  "))
