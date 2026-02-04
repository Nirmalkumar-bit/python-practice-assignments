# Goal: Validate a login attempt.
# Rule: access granted if username is not empty AND (password matches OR has_reset_token)

if __name__ != "__main__":
    username = "sam"
    password = "secret"
    expected_password = "secret"
    has_reset_token = False

if username != "" and (password == expected_password or has_reset_token):
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
