# Read two integers start and end (in that order).
# For each integer n in the inclusive range [start, end], print:
# - "FizzBuzz" if n is divisible by 3 and 5
# - "Fizz" if n is divisible by 3
# - "Buzz" if n is divisible by 5
# - otherwise print n
# Print one result per line.
# Example: start=14, end=16 outputs:
# 14
# FizzBuzz
# 16

start = int(input())
end = int(input())


for n in range(start, end + 1):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
