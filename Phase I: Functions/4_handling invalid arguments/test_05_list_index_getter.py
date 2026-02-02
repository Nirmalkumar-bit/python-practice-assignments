import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "05_list_index_getter.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_05_list_index_getter", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_get_item_at_valid_list_and_tuple():
    m = load_module()
    out1 = m.get_item_at(["a", "b"], 1)
    assert out1 == "b", f"expected output: 'b'\nactual output: {out1!r}"
    out2 = m.get_item_at((10, 20, 30), 0)
    assert out2 == 10, f"expected output: 10\nactual output: {out2!r}"


def test_get_item_at_out_of_range_raises_indexerror():
    m = load_module()
    with pytest.raises(IndexError) as ei:
        m.get_item_at([1], 2)
    assert str(ei.value) == "index out of range", f"expected output: index out of range\nactual output: {str(ei.value)}"


def test_get_item_at_negative_out_of_range_raises_indexerror():
    m = load_module()
    with pytest.raises(IndexError) as ei:
        m.get_item_at([1, 2], -3)
    assert str(ei.value) == "index out of range", f"expected output: index out of range\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("seq", ["abc", 123, None, {"a": 1}, {1, 2}])
def test_get_item_at_seq_type_error(seq):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.get_item_at(seq, 0)
    assert str(ei.value) == "seq must be a list or tuple", f"expected output: seq must be a list or tuple\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("index", [True, False, 1.0, "1", None])
def test_get_item_at_index_type_error(index):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.get_item_at(["x"], index)
    assert str(ei.value) == "index must be an int", f"expected output: index must be an int\nactual output: {str(ei.value)}"
