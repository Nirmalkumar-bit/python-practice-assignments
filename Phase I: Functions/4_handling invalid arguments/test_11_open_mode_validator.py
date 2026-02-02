import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "11_open_mode_validator.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_11_open_mode_validator", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_validate_open_args_valid_r_txt():
    m = load_module()
    out = m.validate_open_args("notes.txt", "r")
    assert out == ("notes.txt", "r"), f"expected output: ('notes.txt', 'r')\nactual output: {out!r}"


def test_validate_open_args_valid_w_any_ext():
    m = load_module()
    out = m.validate_open_args("notes.md", "w")
    assert out == ("notes.md", "w"), f"expected output: ('notes.md', 'w')\nactual output: {out!r}"


@pytest.mark.parametrize("path", ["", "   ", None, 123, True, []])
def test_validate_open_args_invalid_path_type_or_empty(path):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.validate_open_args(path, "w")
    assert str(ei.value) == "path must be a non-empty string", f"expected output: path must be a non-empty string\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("mode", ["", "rb", "rw", "x", None, 1])
def test_validate_open_args_invalid_mode(mode):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_open_args("notes.txt", mode)
    assert str(ei.value) == "invalid mode", f"expected output: invalid mode\nactual output: {str(ei.value)}"


def test_validate_open_args_read_requires_txt():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_open_args("notes.md", "r")
    assert str(ei.value) == "read mode requires .txt file", f"expected output: read mode requires .txt file\nactual output: {str(ei.value)}"
