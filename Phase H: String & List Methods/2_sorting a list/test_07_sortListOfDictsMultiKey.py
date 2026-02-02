import io
import contextlib
import importlib.util
from pathlib import Path


def load_module_from_path(module_name: str, file_path: Path):
    if not file_path.exists():
        raise AssertionError(f"expected output: file to exist at {file_path}\nactual output: file does not exist")
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_sort_dicts_by_last_then_age_and_stdout_exact():
    target = Path(__file__).resolve().parent / "07_sortListOfDictsMultiKey.py"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod = load_module_from_path("a07", target)
    expected_list = [
        {'first': 'Ian', 'last': 'Chen', 'age': 20},
        {'first': 'Mia', 'last': 'Chen', 'age': 22},
        {'first': 'Ava', 'last': 'Ng', 'age': 19},
        {'first': 'Zoe', 'last': 'Ng', 'age': 25}
    ]
    expected_out = f"{expected_list}\n"
    actual_out = buf.getvalue()
    if actual_out != expected_out:
        raise AssertionError(f"expected output: {expected_out}actual output: {actual_out}")
    if getattr(mod, "people", None) != expected_list:
        raise AssertionError(f"expected output: {expected_out}actual output: {actual_out}")
