# Task: Create a function exclaim(text) that returns text with "!" appended.
# Create a function shout(name) that calls exclaim() with "Hi, <name>".
# Expected outcome: print(shout("Ada")) outputs exactly: Hi, Ada!

def exclaim(text):
    return text + "!"

    # TODO: implement
    


def shout(name):
    return exclaim("Hi, " + name)
    # TODO: call exclaim() with the right base message
    


print(shout("Ada"))
