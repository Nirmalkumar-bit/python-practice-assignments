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


def test_custom_comparator_versions_sorted_and_stdout_exact():
    target = Path(__file__).resolve().parent / "08_customComparatorWithCmpToKey.py"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod = load_module_from_path("a08", target)
    expected_list = ['1.2', '1.9', '1.10', '2.0']
    expected_out = f"{expected_list}\n"
    actual_out = buf.getvalue()
    if actual_out != expected_out:
        raise AssertionError(f"expected output: {expected_out}actual output: {actual_out}")
    if getattr(mod, "versions_sorted", None) != expected_list:
        raise AssertionError(f"expected output: {expected_out}actual output: {actual_out}")
