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


def test_difference_and_symdiff_prints(capsys):
    path = Path(__file__).resolve().parent / "07_differenceAndSymmetricDifference.py"
    out = _run_script(path, capsys)
    expected_diff = {"a", "b"}
    expected_sym = {"a", "b", "e"}
    expected = f"A-B: {expected_diff}\nsymdiff: {expected_sym}\n"
    lines = out.strip().splitlines()
    diff = eval(lines[0].split(": ")[1])
    sym = eval(lines[1].split(": ")[1])

    assert diff == expected_diff
    assert sym == expected_sym

