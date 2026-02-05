```
test_14_setComprehensionSquares.py:24: in test_set_comprehension_squares
    raise AssertionError(f"expected output\n{expected}actual output\n{out}")
E   AssertionError: expected output
E   {0, 1, 16, 4, 9}
E   actual output
E   {0, 1, 4, 9, 16}

```

can you assess the error above and check why the below code is failing?

```
# Goal: Use a set comprehension to generate unique squares for numbers in a list.
# Expected outcome: It prints a set containing exactly {0, 1, 4, 9, 16} (order may vary).

nums = [0, 1, 2, 2, 3, 4, 4]
squares = {n * n for n in nums} # TODO: set comprehension of n*n for each n in nums
print(squares)




```

for better idea check the test cases file below and see if there is any issue with that.

```
import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path, capsys):
    if not path.exists():
        raise AssertionError(f"expected output\n<file exists>\nactual output\n<missing file: {path.name}>")
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
    except Exception as e:
        raise AssertionError(f"expected output\n<program runs successfully>\nactual output\n{type(e).__name__}: {e}")
    return capsys.readouterr().out


def test_set_comprehension_squares(capsys):
    path = Path(__file__).resolve().parent / "14_setComprehensionSquares.py"
    out = _run_script(path, capsys)
    expected_set = {0, 1, 4, 9, 16}
    expected = f"{expected_set}\n"
    if out != expected:
        raise AssertionError(f"expected output\n{expected}actual output\n{out}")



```

i want you to return concise answer in bullet point. evaluate in below mentioned flow.

1. check if my answer written in code file is correct as per given problem instructions.
2. if i'm getting expected output then check whats wrong with terminal output. am i missing any potential test cases or edge case?
3. if my code still seems correct then evaluate test file and see if test are written in incorrect way.

you need to return answer in simple English and concise way and direct to the point mentioning whats the issue. no need to return your analysis but the direct response in single para with minimum possible bullet points. i want very short and crisp answer and not lengthy analysis.

i want you to return solution either fixed correct code or test file based on what is actually causing the issue so the test cases can pass.