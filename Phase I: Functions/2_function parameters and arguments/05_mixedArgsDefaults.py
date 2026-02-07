# Goal: Practice mixing positional args, keyword args, and defaults.
# Expected outcome: Running the file prints exactly:
# Hi, Sam.
# Hello, Sam!

# TODO: Define welcome(name, greeting="Hi", punctuation=".") returning "<greeting>, <name><punctuation>"

def welcome(name, greeting="Hi", punctuation="."):
    return f"{greeting}, {name}{punctuation}"
    

print(welcome("Sam"))
print(welcome("Sam", greeting="Hello", punctuation="!"))
