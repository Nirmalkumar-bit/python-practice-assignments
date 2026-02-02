import io
import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Missing assignment file: {path}")

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        spec = importlib.util.spec_from_file_location(path.stem, str(path))
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)  # type: ignore[attr-defined]
        except Exception:
            raise
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    return output


def test_output_exact():
    assignment_path = Path(__file__).resolve().parent / "08_removeItemsMatchingConditionInPlace.py"
    expected = "nums: [3, 0, 2, 5]\n"
    actual = _run_script(assignment_path)
    assert actual == expected, f"expected output:\n{expected}\nactual output:\n{actual}"
