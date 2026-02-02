import sys
import importlib.util
from pathlib import Path
import pytest


def _run_script(script_path: Path):
    if not script_path.exists():
        pytest.fail(f"expected output:\n<file exists>\nactual output:\nMissing file: {script_path}")

    spec = importlib.util.spec_from_file_location(script_path.stem, str(script_path))
    module = importlib.util.module_from_spec(spec)

    captured = []

    def _fake_print(*args, **kwargs):
        sep = kwargs.get("sep", " ")
        end = kwargs.get("end", "\n")
        captured.append(sep.join(str(a) for a in args) + end)

    old_print = __builtins__["print"] if isinstance(__builtins__, dict) else __builtins__.print
    try:
        if isinstance(__builtins__, dict):
            __builtins__["print"] = _fake_print
        else:
            __builtins__.print = _fake_print
        spec.loader.exec_module(module)
    finally:
        if isinstance(__builtins__, dict):
            __builtins__["print"] = old_print
        else:
            __builtins__.print = old_print

    return "".join(captured)


def test_output_exact():
    script_path = Path(__file__).resolve().parent / "03_sumNumbers.py"
    actual = _run_script(script_path)
    expected = "15\n"
    if actual != expected:
        pytest.fail(f"expected output:\n{expected}\nactual output:\n{actual}")
