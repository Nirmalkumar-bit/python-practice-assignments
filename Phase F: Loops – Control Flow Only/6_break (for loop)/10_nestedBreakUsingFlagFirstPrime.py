# Goal: Find the first prime number in the list and print it.
# Use a nested for-loop to test divisibility.
# Use break to stop checking divisors when a divisor is found.
# Use a flag variable to decide if the number is prime.
# Once the first prime is printed, stop the outer loop using break.
# Expected outcome:
# 29

nums = [1, 21, 25, 29, 35, 37]

for n in nums:
    if n < 2:
        continue
    # TODO: skip numbers less than 2
    is_prime = True

    # TODO: test divisors from 2 up to n-1 (or a smarter limit if you want)
    for d in range(2, n):
         if n % d == 0:
            is_prime = False
            break
        # TODO: if n % d == 0, set is_prime to False and break
        

    # TODO: if is_prime is True, print n and break out of the outer loop
    if is_prime:
        print(n)
        break
