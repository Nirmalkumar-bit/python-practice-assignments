# Goal: use a list comprehension to filter and transform.
# Expected outcome (print output):
# result=[4, 16]

nums = [1, 2, 3, 4]

# TODO: create a list of squares of even numbers only
result = [n**2 for n in nums if n%2 == 0]

print(f"result={result}")
