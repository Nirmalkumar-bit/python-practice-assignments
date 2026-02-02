import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "10_matrix_dimensions.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_10_matrix_dimensions", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_validate_matrix_valid():
    m = load_module()
    out = m.validate_matrix([[1, 2], [3, 4]])
    assert out == (2, 2), f"expected output: (2, 2)\nactual output: {out!r}"


@pytest.mark.parametrize("matrix", [None, [], [1, 2], [[1, 2], []], [[], []], "x", 123])
def test_validate_matrix_type_and_emptiness(matrix):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.validate_matrix(matrix)
    assert str(ei.value) == "matrix must be a non-empty list of non-empty lists", f"expected output: matrix must be a non-empty list of non-empty lists\nactual output: {str(ei.value)}"


def test_validate_matrix_rows_must_have_same_length():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_matrix([[1, 2], [3]])
    assert str(ei.value) == "matrix rows must have the same length", f"expected output: matrix rows must have the same length\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("matrix", [[[1, True], [3, 4]], [[1, "2"], [3, 4]], [[1, None], [3, 4]]])
def test_validate_matrix_elements_must_be_numbers(matrix):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.validate_matrix(matrix)
    assert str(ei.value) == "matrix elements must be numbers", f"expected output: matrix elements must be numbers\nactual output: {str(ei.value)}"
