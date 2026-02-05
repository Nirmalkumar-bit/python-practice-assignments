``` 
test_08_nestedLoops_findPairsWithSum.py:29: in test_find_pairs_with_sum_stdout_exact
    pytest.fail(f"expected output:\n{expected}\nactual output:\n{actual}")
E   Failed: expected output:
E   [(0, 3), (1, 2)]
E   
E   actual output:
E   [(0, 3)]
_________________



```
can you assess the error above and check why the below code is failing?

```
# Goal: Find# Goal: Find all unique index pairs (i, j) with i < j such that nums[i] + nums[j] == target.
# Expected outcome for nums and target below (pairs of indices):
# [(0, 3), (1, 2)]

nums = [2, 7, 5, 0]
target = 2

pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((i, j))

print(pairs)

            

# TODO: Use nested loops with i from 0..len(nums)-1 and j from i+1..len(nums)-1.
# If nums[i] + nums[j] equals target, append (i, j) to pairs.


 all unique index pairs (i, j) with i < j such that nums[i] + nums[j] == target.
# Expected outcome for nums and target below (pairs of indices):
# [(0, 3), (1, 2)]

nums = [2, 7, 5, 0]
target = 2

pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((i, j))

print(pairs)

            

# TODO: Use nested loops with i from 0..len(nums)-1 and j from i+1..len(nums)-1.
# If nums[i] + nums[j] equals target, append (i, j) to pairs.







```

for better idea check the test cases file below and see if there is any issue with that.

```
import sys
import importlib.util
from pathlib import Path
import pytest




def _run_script(path: Path):
    if not path.exists():
        pytest.fail(f"Missing assignment file: {path}")

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    if spec is None or spec.loader is None:
        pytest.fail(f"Could not load assignment file: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def test_find_pairs_with_sum_stdout_exact(capsys):
    script_path = Path(__file__).resolve().parent / "08_nestedLoops_findPairsWithSum.py"
    _run_script(script_path)

    captured = capsys.readouterr()
    expected = "[(0, 3), (1, 2)]\n"
    actual = captured.out
    if actual != expected:
        pytest.fail(f"expected output:\n{expected}\nactual output:\n{actual}")
    if captured.err != "":
        pytest.fail(f"expected output:\n{expected}\nactual output:\n{actual}")




```

i want you to return concise answer in bullet point. evaluate in below mentioned flow.

1. check if my answer written in code file is correct as per given problem instructions.
2. if i'm getting expected output then check whats wrong with terminal output. am i missing any potential test cases or edge case?
3. if my code still seems correct then evaluate test file and see if test are written in incorrect way.

you need to return answer in simple English and concise way and direct to the point mentioning whats the issue. no need to return your analysis but the direct response in single para with minimum possible bullet points. i want very short and crisp answer and not lengthy analysis.

i want you to return solution either fixed correct code or test file based on what is actually causing the issue so the test cases can pass.