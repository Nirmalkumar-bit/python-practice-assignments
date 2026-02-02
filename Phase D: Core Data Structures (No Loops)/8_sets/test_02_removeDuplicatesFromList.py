import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path, capsys):
    if not path.exists():
        raise AssertionError(f"expected output\n<file exists>\nactual output\n<missing file: {path.name}>")
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)  # type: ignore[attr-defined]
    except Exception as e:
        raise AssertionError(f"expected output\n<program runs successfully>\nactual output\n{type(e).__name__}: {e}")
    return capsys.readouterr().out


def test_prints_unique_numbers_set(capsys):
    path = Path(__file__).resolve().parent / "02_removeDuplicatesFromList.py"
    out = _run_script(path, capsys)
    expected_set = {1, 2, 3, 4, 5}
    expected = f"{expected_set}\n"
    if out != expected:
        raise AssertionError(f"expected output\n{expected}actual output\n{out}")
