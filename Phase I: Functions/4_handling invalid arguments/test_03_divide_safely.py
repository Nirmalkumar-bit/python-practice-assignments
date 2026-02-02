import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "03_divide_safely.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_03_divide_safely", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5.0),
        (9.0, 3, 3.0),
        (-6, 2, -3.0),
    ],
)
def test_divide_valid(a, b, expected):
    m = load_module()
    out = m.divide(a, b)
    assert out == expected, f"expected output: {expected!r}\nactual output: {out!r}"


@pytest.mark.parametrize("b", [0, 0.0])
def test_divide_zero_denominator(b):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.divide(10, b)
    assert str(ei.value) == "b must not be zero", f"expected output: b must not be zero\nactual output: {str(ei.value)}"


@pytest.mark.parametrize(
    "a,b",
    [
        (True, 2),
        (2, True),
        (False, 2),
        (2, False),
        ("10", 2),
        (10, "2"),
        (None, 1),
        (1, None),
    ],
)
def test_divide_type_errors(a, b):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.divide(a, b)
    assert str(ei.value) == "a and b must be numbers", f"expected output: a and b must be numbers\nactual output: {str(ei.value)}"
