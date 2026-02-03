# Goal: Use 'not' correctly.
# Expected outcome:
# It prints exactly:
# True
# False
# True

is_raining = False
has_umbrella = False

# TODO: Replace ??? to match expected output.
print(not is_raining )  # should be True when it's NOT raining
print(has_umbrella)  # should be False when NOT having an umbrella
print(not(is_raining or has_umbrella))  # should be True when NOT (raining OR has_umbrella) given current values
