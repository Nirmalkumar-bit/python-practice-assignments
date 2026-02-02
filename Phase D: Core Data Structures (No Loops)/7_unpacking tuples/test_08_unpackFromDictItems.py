import sys
import importlib.util
from pathlib import Path
import pytest


def _run_script(script_path: Path):
    if not script_path.exists():
        pytest.fail(f"Missing assignment file: {script_path}")

    spec = importlib.util.spec_from_file_location(script_path.stem, script_path)
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
    script_path = (Path(__file__).resolve().parent / "08_unpackFromDictItems.py").resolve()
    actual = _run_script(script_path)
    expected = "apple=1.25, banana=0.75, cherry=2.50\n"
    assert actual == expected, f"expected output:\n{expected}\nactual output:\n{actual}"
