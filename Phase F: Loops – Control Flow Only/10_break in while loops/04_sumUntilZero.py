# Goal: Sum integers until 0 is entered, then stop using break.
# Expected outcome: For inputs 5, 10, -3, 0 the program prints exactly: Sum: 12

total = 0

while True:
    n = int(input())
    if n==0:
        break
    else:
        total+= n
    
    # TODO: if n is 0, break
    # TODO: otherwise add n to total

print(f"Sum: {total}")
