# Goal: Print the FizzBuzz sequence from 1 to 15 (inclusive), one per line.
# Rules:
# - divisible by 3 -> Fizz
# - divisible by 5 -> Buzz
# - divisible by both -> FizzBuzz
# - otherwise print the number

for n in range(1, 16):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

    # TODO: complete the conditional logic
    

# Expected outcome (15 lines):
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
