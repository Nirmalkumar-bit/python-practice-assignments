import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "06_repeat_string.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_06_repeat_string", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_repeat_valid():
    m = load_module()
    out = m.repeat("ab", 3)
    assert out == "ababab", f"expected output: 'ababab'\nactual output: {out!r}"


def test_repeat_zero_times():
    m = load_module()
    out = m.repeat("x", 0)
    assert out == "", f"expected output: ''\nactual output: {out!r}"


def test_repeat_negative_times_value_error():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.repeat("ab", -1)
    assert str(ei.value) == "times must be non-negative", f"expected output: times must be non-negative\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("s", [None, 1, 1.0, [], {}, True])
def test_repeat_s_type_error(s):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.repeat(s, 2)
    assert str(ei.value) == "s must be a str", f"expected output: s must be a str\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("times", [True, False, 2.0, "2", None])
def test_repeat_times_type_error(times):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.repeat("ab", times)
    assert str(ei.value) == "times must be an int", f"expected output: times must be an int\nactual output: {str(ei.value)}"
