import sys
import importlib.util
from pathlib import Path

def _load_module(path: Path):
    if not path.exists():
        raise AssertionError(f"expected output: 19\nactual output: <missing file: {path.name}>")
    spec = importlib.util.spec_from_file_location("student_mod_12", str(path))
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    except Exception as e:
        raise AssertionError(f"expected output: 19\nactual output: <exception: {type(e).__name__}>")
    return mod

def test_stdout_exact(capsys):
    path = Path(__file__).resolve().parent / "12_recursiveHelperUsedByWrapper.py"
    _load_module(path)
    out = capsys.readouterr().out
    expected = "19\n"
    if out != expected:
        raise AssertionError(f"expected output: {expected}actual output: {out}")
