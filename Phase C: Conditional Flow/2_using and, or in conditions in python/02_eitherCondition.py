# Goal: Print whether a user is eligible based on age OR having a parent permission.
# Expected outcome:
# With age=16 and has_permission=True, print exactly: ELIGIBLE
# With age=16 and has_permission=False, print exactly: NOT ELIGIBLE

age = age if 'age' in globals() else 16
has_permission = has_permission if 'has_permission' in globals() else True


# TODO: Use 'or' to decide eligibility: eligible if age >= 18 OR has_permission is True.
if age >= 18 or has_permission:
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")
