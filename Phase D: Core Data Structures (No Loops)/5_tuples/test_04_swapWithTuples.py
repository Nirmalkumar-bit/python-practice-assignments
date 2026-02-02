import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    old_stdout = sys.stdout
    try:
        from io import StringIO
        buf = StringIO()
        sys.stdout = buf
        spec.loader.exec_module(module)
        return buf.getvalue()
    finally:
        sys.stdout = old_stdout


def test_stdout_exact():
    script_path = Path(__file__).resolve().parent / "04_swapWithTuples.py"
    assert script_path.exists(), "expected output: (file exists)\nactual output: (missing file)"

    out = _run_script(script_path)
    expected = "9\n3\n"
    assert out == expected, f"expected output:\n{expected}actual output:\n{out}"
