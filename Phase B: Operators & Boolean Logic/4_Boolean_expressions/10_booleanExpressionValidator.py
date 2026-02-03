# Goal: Implement a boolean decision function using multiple conditions.
# Expected outcome:
# Running this file prints exactly:
# True
# False
# False
# True

def is_password_acceptable(pw: str) -> bool:
    """Return True only if all rules pass:
    - length is at least 8
    - contains at least one digit
    - does NOT contain any spaces
    - is not exactly "password" (case-sensitive)
    """
    # TODO: Implement using boolean expressions.
    has_min_len = len(pw) >= 8
    has_digit = any(ch.isdigit()for ch in pw)
    has_space = " " in pw
    is_banned = pw == "password"

    acceptable = has_min_len and has_digit and not has_space and not is_banned
    return acceptable

print(is_password_acceptable("tiger123"))     # True
print(is_password_acceptable("password"))     # False
print(is_password_acceptable("no digits"))    # False
print(is_password_acceptable("abc12345"))    # True
