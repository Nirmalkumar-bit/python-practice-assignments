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


def test_add_discard_result(capsys):
    path = Path(__file__).resolve().parent / "04_addAndDiscard.py"
    out = _run_script(path, capsys).strip()

    actual_set = eval(out)
    expected_set = {"a", "c", "d"}

    assert actual_set == expected_set, (
        f"expected output\n{expected_set}\nactual output\n{actual_set}"
    )
