import io
import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path):
    if not path.exists():
        raise AssertionError(f"expected output: file to exist at {path}\nactual output: file missing")

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        spec = importlib.util.spec_from_file_location(path.stem, str(path))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    return output


def test_output_exact():
    script_path = Path(__file__).resolve().parent / "01_replaceSingleItemByIndex.py"
    actual = _run_script(script_path)
    expected = "['red', 'blue', 'green']\n"
    if actual != expected:
        raise AssertionError(f"expected output: {expected}actual output: {actual}")
