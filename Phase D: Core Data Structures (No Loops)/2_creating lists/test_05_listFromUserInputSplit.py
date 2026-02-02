import io
import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path, monkeypatch, input_value: str):
    if not path.exists():
        raise AssertionError(f"expected output: <file exists>\nactual output: missing file {path.name}")

    captured = io.StringIO()
    monkeypatch.setattr(sys, "stdout", captured)
    monkeypatch.setattr("builtins.input", lambda _prompt="": input_value)

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        raise AssertionError(f"expected output: script runs without error\nactual output: {type(e).__name__}: {e}")

    return captured.getvalue()


def test_splits_and_strips_colors(monkeypatch):
    path = Path(__file__).resolve().parent / "05_listFromUserInputSplit.py"
    out = _run_script(path, monkeypatch, "red, blue, green")
    expected = "['red', 'blue', 'green']\n"
    if out != expected:
        raise AssertionError(f"expected output: {expected}actual output: {out}")


def test_splits_without_spaces(monkeypatch):
    path = Path(__file__).resolve().parent / "05_listFromUserInputSplit.py"
    out = _run_script(path, monkeypatch, "cyan,magenta,yellow")
    expected = "['cyan', 'magenta', 'yellow']\n"
    if out != expected:
        raise AssertionError(f"expected output: {expected}actual output: {out}")
