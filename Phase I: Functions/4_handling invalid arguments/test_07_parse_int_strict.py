import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "07_parse_int_strict.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_07_parse_int_strict", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "s,expected",
    [
        ("0", 0),
        ("  -42 ", -42),
        ("+7", 7),
        ("  0010  ", 10),
    ],
)
def test_parse_int_strict_valid(s, expected):
    m = load_module()
    out = m.parse_int_strict(s)
    assert out == expected, f"expected output: {expected!r}\nactual output: {out!r}"


@pytest.mark.parametrize(
    "s",
    [
        "",
        "   ",
        "3.14",
        "- 1",
        "+",
        "--1",
        "1_000",
        "12a",
        "a12",
    ],
)
def test_parse_int_strict_invalid_literal(s):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.parse_int_strict(s)
    assert str(ei.value) == "invalid integer literal", f"expected output: invalid integer literal\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("s", [10, None, 3.14, True, [], {}])
def test_parse_int_strict_type_error(s):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.parse_int_strict(s)
    assert str(ei.value) == "s must be a str", f"expected output: s must be a str\nactual output: {str(ei.value)}"
