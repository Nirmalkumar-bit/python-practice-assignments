import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "08_sum_n_numbers.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_08_sum_n_numbers", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_sum_n_basic():
    m = load_module()
    out = m.sum_n([1, 2, 3, 4], 2)
    assert out == 3, f"expected output: 3\nactual output: {out!r}"


def test_sum_n_zero():
    m = load_module()
    out = m.sum_n([1, 2, 3], 0)
    assert out == 0, f"expected output: 0\nactual output: {out!r}"


def test_sum_n_all_elements():
    m = load_module()
    out = m.sum_n([1.5, 2.5, -1.0], 3)
    assert out == pytest.approx(3.0), f"expected output: 3.0\nactual output: {out!r}"


@pytest.mark.parametrize("numbers", ["123", (1, 2), None, 123, {"a": 1}])
def test_sum_n_numbers_type_error_numbers_container(numbers):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.sum_n(numbers, 1)
    assert str(ei.value) == "numbers must be a list of numbers", f"expected output: numbers must be a list of numbers\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("numbers", [[1, "2", 3], [True, 2], [1, None]])
def test_sum_n_numbers_type_error_element_types(numbers):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.sum_n(numbers, 2)
    assert str(ei.value) == "numbers must be a list of numbers", f"expected output: numbers must be a list of numbers\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("n", [True, False, 2.0, "2", None])
def test_sum_n_n_type_error(n):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.sum_n([1, 2, 3], n)
    assert str(ei.value) == "n must be an int", f"expected output: n must be an int\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("n", [-1, 4, 10])
def test_sum_n_n_out_of_range(n):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.sum_n([1, 2, 3], n)
    assert str(ei.value) == "n out of allowed range", f"expected output: n out of allowed range\nactual output: {str(ei.value)}"
