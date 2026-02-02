import io
import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path):
    if not path.exists():
        raise AssertionError(f"expected output:\n<file exists>\nactual output:\n<missing file: {path.name}>")

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    return output


def test_stdout_exact():
    script_path = Path(__file__).resolve().parent / '02_listAppendAndLength.py'
    expected = "['milk', 'bread', 'eggs']\n3\n"
    actual = _run_script(script_path)
    if actual != expected:
        raise AssertionError(f"expected output:\n{expected}actual output:\n{actual}")
