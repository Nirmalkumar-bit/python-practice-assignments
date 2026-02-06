# Group consecutive equal values into runs (a list of lists) and print it.
# Example: [1,1,2,2,2,3,1,1] -> [[1,1],[2,2,2],[3],[1,1]]
# Expected outcome:
# [[1, 1], [2, 2, 2], [3], [1, 1]]

nums = [1, 1, 2, 2, 2, 3, 1, 1]

runs = []
current_run = []


for n in nums:
    if current_run == [] or n == current_run[-1]:
        current_run.append(n)
    else:
        runs.append(current_run)
        current_run = [n]
# TODO: after the loop, append the last run if needed
if current_run:
    runs.append(current_run)

print(runs)
