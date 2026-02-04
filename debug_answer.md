```test_07_dict_membership_keys_vs_values.py:32: in test_stdout_exact
    raise AssertionError(f"expected output:\n{expected}\nactual output:\n{actual}")
E   AssertionError: expected output:
E   key_exists
E   value_missing
E   
E   actual output:
E   key_exists
E   value_exists
 
```

can you assess the error above and check why the below code is failing?

```# Goal: Understand 'in' with dictionaries (keys by default).
# Expected outcome:
# - Prints exactly:
#   key_exists
#   value_missing

prices = {"apple": 1.25, "banana": 0.75}

# TODO: Use membership tests correctly.
if "apple" in prices:
    print("key_exists")

# TODO: Check whether the VALUE 1.25 exists in the dictionary values.
if 1.25 not in prices.values():
    print("value_missing")
else:
    # This branch should NOT run for the expected outcome
    print("value_exists")



```

for better idea check the test cases file below and see if there is any issue with that.

```import importlib.util
from pathlib import Path
import sys


def _run_module_capture_stdout(path: Path):
    if not path.exists():
        raise AssertionError(f"Assignment file does not exist: {path}")

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    if spec is None or spec.loader is None:
        raise AssertionError("Could not load assignment module")

    module = importlib.util.module_from_spec(spec)

    old_stdout = sys.stdout
    try:
        from io import StringIO
        buf = StringIO()
        sys.stdout = buf
        spec.loader.exec_module(module)
        return buf.getvalue()
    finally:
        sys.stdout = old_stdout


def test_stdout_exact():
    assignment_path = Path(__file__).resolve().parent / "07_dict_membership_keys_vs_values.py"
    actual = _run_module_capture_stdout(assignment_path)
    expected = "key_exists\nvalue_missing\n"
    if actual != expected:
        raise AssertionError(f"expected output:\n{expected}\nactual output:\n{actual}")



```

i want you to return concise answer in bullet point. evaluate in below mentioned flow.

1. check if my answer written in code file is correct as per given problem instructions.
2. if i'm getting expected output then check whats wrong with terminal output. am i missing any potential test cases or edge case?
3. if my code still seems correct then evaluate test file and see if test are written in incorrect way.

you need to return answer in simple English and concise way and direct to the point mentioning whats the issue. no need to return your analysis but the direct response in single para with minimum possible bullet points. i want very short and crisp answer and not lengthy analysis.

i want you to return solution either fixed correct code or test file based on what is actually causing the issue so the test cases can pass.