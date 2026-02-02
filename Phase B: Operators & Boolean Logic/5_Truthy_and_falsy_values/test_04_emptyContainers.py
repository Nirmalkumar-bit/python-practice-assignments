import sys
import importlib.util
from pathlib import Path
import pytest


def _run_file(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    old_stdout = sys.stdout
    try:
        from io import StringIO
        buf = StringIO()
        sys.stdout = buf
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
        return buf.getvalue()
    finally:
        sys.stdout = old_stdout


def test_stdout_exact():
    assignment_path = Path(__file__).resolve().parent / "04_emptyContainers.py"
    if not assignment_path.exists():
        pytest.fail("expected output: NO ITEMS\n\nactual output: (missing file)")

    expected = "NO ITEMS\n"
    actual = _run_file(assignment_path)
    if actual != expected:
        pytest.fail(f"expected output: {expected}actual output: {actual}")
