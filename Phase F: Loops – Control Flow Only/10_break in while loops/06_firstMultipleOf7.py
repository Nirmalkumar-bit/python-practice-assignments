# Goal: Find the first multiple of 7 within a range using a while loop and break.
# Read two integers: start and end (inclusive). Assume start <= end.
# Expected outcome:
# - Input: 10 then 30 -> print exactly: 14
# - Input: 1 then 6 -> print exactly: None

start = int(input())
end = int(input())

x = start
result = None
    
while x <= end:
    if x % 7 == 0:
        result = x
        break
    x += 1

    # TODO: if x is a multiple of 7, set result to x and break
print(result) 

# TODO: print result (prints "None" if no multiple was found)
