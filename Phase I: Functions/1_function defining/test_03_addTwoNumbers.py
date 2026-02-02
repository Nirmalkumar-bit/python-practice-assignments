import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing assignment file: {path.name}")

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)

    captured = []

    def fake_print(*args, **kwargs):
        sep = kwargs.get("sep", " ")
        end = kwargs.get("end", "\n")
        captured.append(sep.join(str(a) for a in args) + end)

    old_print = __builtins__["print"] if isinstance(__builtins__, dict) else __builtins__.print
    try:
        if isinstance(__builtins__, dict):
            __builtins__["print"] = fake_print
        else:
            __builtins__.print = fake_print
        spec.loader.exec_module(module)
    finally:
        if isinstance(__builtins__, dict):
            __builtins__["print"] = old_print
        else:
            __builtins__.print = old_print

    return "".join(captured)


def test_output_exact():
    script_path = Path(__file__).resolve().parent / "03_addTwoNumbers.py"
    expected = "12\n"
    actual = _run_script(script_path)
    assert actual == expected, f"expected output:\n{expected}\nactual output:\n{actual}"
