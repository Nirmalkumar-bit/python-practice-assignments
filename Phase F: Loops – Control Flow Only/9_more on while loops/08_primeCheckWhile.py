# Determine if a number is prime using a while loop.
# Input: integer n (n >= 0)
# Output:
# - print "Prime" if n is prime
# - otherwise print "Not prime"
# Expected outcome examples:
# n=2 -> Prime
# n=9 -> Not prime
# n=1 -> Not prime

n = int(input().strip())
if n < 2:
    print("Not prime")
else:
    is_prime = True
    i = 2

    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime")
    else:
        print("Not prime")


# TODO: handle small cases (n < 2)

# TODO: try divisors starting at 2 up to sqrt(n) using while
# Use a flag like is_prime = True/False

# TODO: print Prime or Not prime
