# Goal: Complete the function using a conditional (ternary) expression in the return statement.
# If x is divisible by 3, return "fizz" else return the string form of x.
# Expected outcome: Prints exactly: fizz

def fizz_or_number(x: int) -> str:
     return "fizz"if x % 3 == 0 else str(x)

print(fizz_or_number(9))
