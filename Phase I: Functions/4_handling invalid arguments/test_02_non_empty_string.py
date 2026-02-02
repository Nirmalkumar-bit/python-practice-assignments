import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "02_non_empty_string.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_02_non_empty_string", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_require_non_empty_string_strips_and_returns():
    m = load_module()
    out = m.require_non_empty_string("  hi ")
    assert out == "hi", f"expected output: 'hi'\nactual output: {out!r}"


@pytest.mark.parametrize("s", ["", "   ", "\n\t  "])
def test_require_non_empty_string_rejects_empty_or_whitespace(s):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.require_non_empty_string(s)
    assert str(ei.value) == "s must be a non-empty string", f"expected output: s must be a non-empty string\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("s", [None, 1, 3.14, [], {}, True, ("x",)])
def test_require_non_empty_string_type_error(s):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.require_non_empty_string(s)
    assert str(ei.value) == "s must be a str", f"expected output: s must be a str\nactual output: {str(ei.value)}"
