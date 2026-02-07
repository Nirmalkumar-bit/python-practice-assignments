# Task: Complete two functions so one calls the other.
# You will create a second file named "utils_math.py" (not provided here) with:
#   def multiply(a, b):
#       ...
# In THIS file, import multiply and create area_rectangle(w, h) that calls multiply(w, h).
# Expected outcome: After you also create utils_math.py, running this file prints exactly: 35

# TODO: import multiply from utils_math
def multiply(a, b):
    return a * b


    from utils_math import multiply

def area_rectangle(w, h):
    return multiply(w, h)



    # TODO: call multiply(w, h)
    


print(area_rectangle(5, 7))
