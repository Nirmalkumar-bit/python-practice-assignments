# Goal: Build a username from the string until a space is found.
# Only include lowercase letters a-z; ignore digits and punctuation.
# Stop at the first space using break.
# Print the resulting username.
# Expected outcome:
# alice

raw = "Alice99! Bob"

username = ""
for ch in raw:
    if ch == " ":
        break
    ch = ch.lower()
    if "a" <= ch <= "z":
        username += ch

    # TODO: if ch is a space, break
    # TODO: convert ch to lowercase
    
    # TODO: if it's a letter a-z, append to username
    

print(username)
