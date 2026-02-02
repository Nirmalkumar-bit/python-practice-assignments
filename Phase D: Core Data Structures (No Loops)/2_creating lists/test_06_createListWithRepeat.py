import io
import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path, monkeypatch):
    if not path.exists():
        raise AssertionError(f"expected output: <file exists>\nactual output: missing file {path.name}")

    captured = io.StringIO()
    monkeypatch.setattr(sys, "stdout", captured)

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        raise AssertionError(f"expected output: script runs without error\nactual output: {type(e).__name__}: {e}")

    return captured.getvalue()


def test_prints_five_zeros(monkeypatch):
    path = Path(__file__).resolve().parent / "06_createListWithRepeat.py"
    out = _run_script(path, monkeypatch)
    expected = "[0, 0, 0, 0, 0]\n"
    if out != expected:
        raise AssertionError(f"expected output: {expected}actual output: {out}")
