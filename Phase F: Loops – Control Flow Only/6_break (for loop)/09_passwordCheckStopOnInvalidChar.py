# Goal: Scan the password and stop at the first invalid character.
# Valid characters are letters and digits only.
# Print the first invalid character found.
# Expected outcome:
# #

pwd = "abC12#xy"

for ch in pwd:
    if not ch.isalnum():
        print(ch)
        break
    # TODO: if ch is not alphanumeric, print ch and break
    
