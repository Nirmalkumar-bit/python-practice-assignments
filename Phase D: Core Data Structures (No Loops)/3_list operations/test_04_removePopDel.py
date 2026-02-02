import sys
import importlib.util
from pathlib import Path

import pytest


def _run_script(script_path: Path):
    if not script_path.exists():
        pytest.fail(f"expected output:\n(removed=3\\nremaining=[1, 2, 4]\\n)\nactual output:\n<missing file: {script_path.name}>")

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
    script_path = Path(__file__).resolve().parent / "04_removePopDel.py"
    expected = "removed=3\nremaining=[1, 2, 4]\n"
    actual = _run_script(script_path)
    assert actual == expected, f"expected output:\n{expected}actual output:\n{actual}" 
