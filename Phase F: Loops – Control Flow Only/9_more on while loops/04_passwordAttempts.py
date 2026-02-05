# Ask for a password up to 3 attempts using a while loop.
# Correct password is: "opensesame"
# If correct within 3 attempts, print: Access granted
# Otherwise print: Access denied
# Input: up to 3 lines, each a password attempt
# Output: exactly one line.

CORRECT = "opensesame"
max_attempts = 3
attempts = 0
success = False

# TODO: loop while attempts < max_attempts
# - read attempt
# - if correct, print Access granted and stop early
# - otherwise increment attempts and continue

# TODO: if loop ends without success, print Access denied
# Ask for a password up to 3 attempts using a while loop.
# Correct password is: "opensesame"
# If correct within 3 attempts, print: Access granted
# Otherwise print: Access denied
# Input: up to 3 lines, each a password attempt
# Output: exactly one line.

while attempts < max_attempts:
    attempt = input().strip()
    if attempt == CORRECT:
        print("Access granted")
        success = True
        break
    attempts += 1

if not success:
    print("Access denied")
