# Goal: Allow up to 3 attempts to enter the correct password.
# If the correct password is entered, print 'Access granted'. Otherwise, after 3 failures, print 'Access denied'.
# Use a while loop.
# With inputs: a, b, secret
# Expected outcome (exact line):
# Access granted

correct = "secret"
attempts = 0

# TODO: loop while attempts remain and password not correct
while attempts < 3:
    entered = input()
    if entered == correct:
        print("Access granted")
        break
    attempts += 1
else:
    print("Access denied")


# TODO: print the correct final message
