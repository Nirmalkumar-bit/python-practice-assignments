import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "04_percentage_range.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_04_percentage_range", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("p,expected", [(0, 0.0), (100, 100.0), (75, 75.0), (12.5, 12.5)])
def test_clamp_percentage_valid(p, expected):
    m = load_module()
    out = m.clamp_percentage(p)
    assert out == expected, f"expected output: {expected!r}\nactual output: {out!r}"
    assert isinstance(out, float), f"expected output: float\nactual output: {type(out).__name__}"


@pytest.mark.parametrize("p", [-1, -0.0001, 100.0001, 101])
def test_clamp_percentage_range_error(p):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.clamp_percentage(p)
    assert str(ei.value) == "p must be between 0 and 100", f"expected output: p must be between 0 and 100\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("p", [True, False, "50", None, [], {}])
def test_clamp_percentage_type_error(p):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.clamp_percentage(p)
    assert str(ei.value) == "p must be a number", f"expected output: p must be a number\nactual output: {str(ei.value)}"
