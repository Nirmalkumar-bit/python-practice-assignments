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

def test_and_or_results():
    assignment_path = Path(__file__).resolve().parent / "04_booleanAndOrBasics.py"
    module, out = _load_module_and_capture_stdout(assignment_path)

    expected_out = "False\nTrue\n"
    if out != expected_out:
        raise AssertionError(f"expected output:\n{expected_out}actual output:\n{out}")

    assert hasattr(module, "allowed_in"), "allowed_in variable is missing"
    assert hasattr(module, "needs_help"), "needs_help variable is missing"
    assert type(module.allowed_in) is bool
    assert type(module.needs_help) is bool
    assert module.allowed_in is False
    assert module.needs_help is True
