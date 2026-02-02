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

def test_comparisons_outputs_and_types():
    assignment_path = Path(__file__).resolve().parent / "05_comparisonsToBooleans.py"
    module, out = _load_module_and_capture_stdout(assignment_path)

    expected_out = "False\nTrue\n"
    if out != expected_out:
        raise AssertionError(f"expected output:\n{expected_out}actual output:\n{out}")

    assert hasattr(module, "is_adult"), "is_adult variable is missing"
    assert hasattr(module, "passed"), "passed variable is missing"
    assert type(module.is_adult) is bool
    assert type(module.passed) is bool
    assert module.is_adult is False
    assert module.passed is True
