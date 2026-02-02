import sys
import importlib.util
from pathlib import Path

def _load_module_and_capture_stdout(module_path: Path):
    if not module_path.exists():
        raise FileNotFoundError(f"Missing assignment file: {module_path}")

    spec = importlib.util.spec_from_file_location(module_path.stem, str(module_path))
    module = importlib.util.module_from_spec(spec)

    old_stdout = sys.stdout
    try:
        from io import StringIO
        buf = StringIO()
        sys.stdout = buf
        spec.loader.exec_module(module)
        output = buf.getvalue()
    finally:
        sys.stdout = old_stdout

    return module, output

def test_is_even_stdout_and_behavior():
    assignment_path = Path(__file__).resolve().parent / "08_booleanFunctionReturn.py"
    module, out = _load_module_and_capture_stdout(assignment_path)

    expected_out = "True\nFalse\nTrue\n"
    if out != expected_out:
        raise AssertionError(f"expected output:\n{expected_out}actual output:\n{out}")

    assert hasattr(module, "is_even"), "is_even function is missing"
    assert module.is_even(10) is True
    assert module.is_even(7) is False
    assert module.is_even(0) is True
    assert type(module.is_even(2)) is bool
