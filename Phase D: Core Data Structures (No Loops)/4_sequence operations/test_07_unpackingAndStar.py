import io
import sys
import importlib.util
from pathlib import Path
import pytest


def _run_script(path: Path):
    if not path.exists():
        pytest.fail(f"expected output:\n(python file exists)\nactual output:\nmissing file: {path}")

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    if spec is None or spec.loader is None:
        pytest.fail("expected output:\n(script imports)\nactual output:\nimport failure")

    module = importlib.util.module_from_spec(spec)
    old_stdout = sys.stdout
    buf = io.StringIO()
    sys.stdout = buf
    try:
        spec.loader.exec_module(module)
    finally:
        sys.stdout = old_stdout
    return buf.getvalue()


def test_stdout_exact():
    path = Path(__file__).resolve().parent / "07_unpackingAndStar.py"
    out = _run_script(path)
    expected = "red\n['green', 'blue']\nyellow\n"
    assert out == expected, f"expected output:\n{expected}\nactual output:\n{out}" 
