# Task: Implement repeat(s, times).
# Requirements:
# - s must be str else TypeError("s must be a str")
# - times must be int (bool not allowed) else TypeError("times must be an int")
# - times must be >= 0 else ValueError("times must be non-negative")
# - Return s repeated times times
# Expected outcome:
# - repeat("ab", 3) returns "ababab"
# - repeat("ab", -1) raises ValueError("times must be non-negative")


def repeat(s, times):
     if not isinstance(s, str):
        raise TypeError("s must be a str")
    
    # Check times type (bool not allowed)
     if type(times) is not int:
        raise TypeError("times must be an int")
    
    # Check non-negative
     if times < 0:
        raise ValueError("times must be non-negative")
    
     return s * times
    # TODO
    


if __name__ == "__main__":
    print(repeat("ab", 3))