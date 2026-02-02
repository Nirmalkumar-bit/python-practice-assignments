import sys
import importlib.util
from pathlib import Path


def _run_script_capture_stdout(script_path: Path):
    if not script_path.exists():
        raise FileNotFoundError(f"Missing assignment file: {script_path}")

    spec = importlib.util.spec_from_file_location(script_path.stem, str(script_path))
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


def test_stdout_exact_match():
    script_path = Path(__file__).resolve().parent / "06_exponentiationPowers.py"
    expected = "2^10 = 1024\n"
    actual = _run_script_capture_stdout(script_path)
    assert actual == expected, f"expected output:\n{expected}\nactual output:\n{actual}"
