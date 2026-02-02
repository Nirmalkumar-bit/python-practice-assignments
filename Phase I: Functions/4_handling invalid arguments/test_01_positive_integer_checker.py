import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "01_positive_integer_checker.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_01_positive_integer_checker", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_validate_positive_int_valid():
    m = load_module()
    out = m.validate_positive_int(3)
    assert out is True, f"expected output: True\nactual output: {out!r}"


@pytest.mark.parametrize(
    "val",
    ["3", 3.0, None, [], {}, (3,), True, False],
)
def test_validate_positive_int_type_errors(val):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.validate_positive_int(val)
    assert str(ei.value) == "n must be an int", f"expected output: n must be an int\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("val", [0, -1, -100])
def test_validate_positive_int_value_errors(val):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_positive_int(val)
    assert str(ei.value) == "n must be positive", f"expected output: n must be positive\nactual output: {str(ei.value)}"
