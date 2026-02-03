# Goal: Combine comparisons with 'and'/'or' and parentheses.
# Expected outcome:
# It prints exactly:
# can_enter: True
# needs_parent: False

age = 17
has_ticket = True
with_parent = True

# Rules:
# - can_enter is True if has_ticket AND (age >= 18 OR with_parent)
# - needs_parent is True if has_ticket AND age < 18 AND NOT with_parent

# TODO: Write boolean expressions that follow the rules.
# Rules:
can_enter = has_ticket and (age >= 18 or with_parent)
needs_parent = has_ticket and age < 18 and not with_parent

print("can_enter:", can_enter)
print("needs_parent:", needs_parent)
