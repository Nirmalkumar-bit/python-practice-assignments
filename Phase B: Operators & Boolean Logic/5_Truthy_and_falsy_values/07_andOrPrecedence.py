# Task: Use parentheses to get the intended result.
# Fill in the expression so it prints exactly:
# "ACCESS GRANTED"

is_admin = False
has_ticket = True
is_banned = False

# Rule: grant access if (is_admin OR has_ticket) AND NOT is_banned
if (is_admin or has_ticket) and not is_banned:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
