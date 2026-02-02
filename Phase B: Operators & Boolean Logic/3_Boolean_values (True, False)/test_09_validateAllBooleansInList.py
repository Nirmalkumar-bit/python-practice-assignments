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

def test_all_bools_stdout_and_edge_cases():
    assignment_path = Path(__file__).resolve().parent / "09_validateAllBooleansInList.py"
    module, out = _load_module_and_capture_stdout(assignment_path)

    expected_out = "True\nFalse\nFalse\n"
    if out != expected_out:
        raise AssertionError(f"expected output:\n{expected_out}actual output:\n{out}")

    assert hasattr(module, "all_bools"), "all_bools function is missing"
    assert module.all_bools([True, False, True]) is True
    assert module.all_bools([True, 1, False]) is False
    assert module.all_bools([]) is False
    assert module.all_bools([False, 0]) is False
