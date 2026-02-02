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


def test_stable_sort_by_key_merge_sort_expected_and_stdout_exact():
    target = Path(__file__).resolve().parent / "10_implementStableSortByKey.py"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod = load_module_from_path("a10", target)

    expected_list = [('Ben', 2), ('Dan', 2), ('Ava', 3), ('Cara', 3)]
    expected_out = f"{expected_list}\n"
    actual_out = buf.getvalue()
    if actual_out != expected_out:
        raise AssertionError(f"expected output: {expected_out}actual output: {actual_out}")

    if getattr(mod, "sorted_pairs", None) != expected_list:
        raise AssertionError(f"expected output: {expected_out}actual output: {actual_out}")


def test_stable_sort_by_key_does_not_mutate_input_when_called_directly():
    target = Path(__file__).resolve().parent / "10_implementStableSortByKey.py"
    mod = load_module_from_path("a10b", target)

    items = [('Ava', 3), ('Ben', 2), ('Cara', 3), ('Dan', 2)]
    items_copy = list(items)
    res = mod.stable_sort_by_key(items, key_func=lambda x: x[1])

    expected_res = [('Ben', 2), ('Dan', 2), ('Ava', 3), ('Cara', 3)]
    if res != expected_res or items != items_copy:
        raise AssertionError(f"expected output: {expected_res}\nactual output: {res}")
