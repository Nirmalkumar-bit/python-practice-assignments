``` 
During handling of the above exception, another exception occurred:
test_06_passwordAttempts.py:38: in test_password_access_denied_after_three_failures
    _run_script_with_inputs(path, monkeypatch, ["x", "y", "z"], "Access denied\n")
test_06_passwordAttempts.py:18: in _run_script_with_inputs
    spec.loader.exec_module(module)
<frozen importlib._bootstrap_external>:995: in exec_module
    ???
<frozen importlib._bootstrap>:488: in _call_with_frames_removed
    ???
06_passwordAttempts.py:15: in <module>
    entered = input("Py:15: in <module>
    entered = input("Password: ")
test_06_passwordAttempts.py:12: in fake_input
    raise AssertionError(f"expected output\n{expected_for_errors}actual output\n<program requested more input>")
E   AssertionError: expected output
E   Access denied
E   actual output
E   <program requested more input>



```
can you assess the error above and check why the below code is failing?

```
# Goal: Allow up to 3 attempts to enter the correct password.
# If the correct password is entered, print 'Access granted'. Otherwise, after 3 failures, print 'Access denied'.
# Use a while loop.
# With inputs: a, b, secret
# Expected outcome (exact line):
# Access granted

correct = "secret"
attempts = 0

# TODO: loop while attempts remain and password not correct
entered = input("Password: ")
while attempts < 3 and entered != correct:
    attempts = attempts + 1
    entered = input("Password: ")

# TODO: print the correct final message
if entered == correct:
    print("Access granted")
else:
    print("Access denied")







```

for better idea check the test cases file below and see if there is any issue with that.

```
import importlib.util
from pathlib import Path

def _run_script_with_inputs(path, monkeypatch, inputs, expected_for_errors):
    import builtins
    it = iter(inputs)

    def fake_input(prompt=""):
        try:
            return next(it)
        except StopIteration:
            raise AssertionError(f"expected output\n{expected_for_errors}actual output\n<program requested more input>")

    monkeypatch.setattr(builtins, "input", fake_input)

    spec = importlib.util.spec_from_file_location("student_module", str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def test_password_access_granted_on_third_try(capsys, monkeypatch):
    path = Path(__file__).resolve().parent / "06_passwordAttempts.py"
    if not path.exists():
        raise AssertionError("expected output\nAccess granted\nactual output\n<missing file>")

    _run_script_with_inputs(path, monkeypatch, ["a", "b", "secret"], "Access granted\n")
    out = capsys.readouterr().out
    expected = "Access granted\n"
    if out != expected:
        raise AssertionError(f"expected output\n{expected}actual output\n{out}")


def test_password_access_denied_after_three_failures(capsys, monkeypatch):
    path = Path(__file__).resolve().parent / "06_passwordAttempts.py"
    if not path.exists():
        raise AssertionError("expected output\nAccess denied\nactual output\n<missing file>")

    _run_script_with_inputs(path, monkeypatch, ["x", "y", "z"], "Access denied\n")
    out = capsys.readouterr().out
    expected = "Access denied\n"
    if out != expected:
        raise AssertionError(f"expected output\n{expected}actual output\n{out}")








```

i want you to return concise answer in bullet point. evaluate in below mentioned flow.

1. check if my answer written in code file is correct as per given problem instructions.
2. if i'm getting expected output then check whats wrong with terminal output. am i missing any potential test cases or edge case?
3. if my code still seems correct then evaluate test file and see if test are written in incorrect way.

you need to return answer in simple English and concise way and direct to the point mentioning whats the issue. no need to return your analysis but the direct response in single para with minimum possible bullet points. i want very short and crisp answer and not lengthy analysis.

i want you to return solution either fixed correct code or test file based on what is actually causing the issue so the test cases can pass.