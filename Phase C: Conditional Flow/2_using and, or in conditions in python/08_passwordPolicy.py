# Goal: Validate a password with multiple requirements.
# Requirements:
# - length >= 8
# - must contain at least one digit OR at least one special character from '!@#'
# - must NOT contain spaces
# Print exactly: VALID or INVALID
# Expected outcome:
# With password='abcde1fg' => VALID
# With password='abcd e1fg' => INVALID

# Do NOT override password if it already exists
try:
    password
except NameError:
    password = "abcde1fg"

has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in "!@#" for ch in password)
has_space = " " in password
has_min_length = len(password) >= 8

if has_min_length and (has_digit or has_special) and not has_space:
    print("VALID")
else:
    print("INVALID")

