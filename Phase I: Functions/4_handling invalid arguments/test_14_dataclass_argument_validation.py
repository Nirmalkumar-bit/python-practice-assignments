import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "14_dataclass_argument_validation.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_14_dataclass_argument_validation", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_userinput_valid_constructs():
    m = load_module()
    u = m.UserInput("alice_1", 30, "a@b.com")
    assert (u.username, u.age, u.email) == ("alice_1", 30, "a@b.com"), f"expected output: ('alice_1', 30, 'a@b.com')\nactual output: {(u.username, u.age, u.email)!r}"


@pytest.mark.parametrize("username", [None, 123, True, ["a"], {"u": "x"}])
def test_userinput_username_type_error(username):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.UserInput(username, 30, "a@b.com")
    assert str(ei.value) == "username must be a str", f"expected output: username must be a str\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("username", ["ab", "a!", "this_username_is_way_too_long_123", "space name", "dash-name", ""])
def test_userinput_invalid_username(username):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.UserInput(username, 30, "a@b.com")
    assert str(ei.value) == "invalid username", f"expected output: invalid username\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("age", [True, False, 20.0, "20", None])
def test_userinput_age_type_error(age):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.UserInput("alice_1", age, "a@b.com")
    assert str(ei.value) == "age must be an int", f"expected output: age must be an int\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("age", [12, 0, -1, 121, 999])
def test_userinput_invalid_age_value(age):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.UserInput("alice_1", age, "a@b.com")
    assert str(ei.value) == "invalid age", f"expected output: invalid age\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("email", [None, 123, True, ["a@b.com"], {"e": "a@b.com"}])
def test_userinput_email_type_error(email):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.UserInput("alice_1", 30, email)
    assert str(ei.value) == "email must be a str", f"expected output: email must be a str\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("email", ["", "a@b", "a@@b.com", "ab.com", "a@.com", "a@b.", "@b.com", "a@bcom"])
def test_userinput_invalid_email(email):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.UserInput("alice_1", 30, email)
    assert str(ei.value) == "invalid email", f"expected output: invalid email\nactual output: {str(ei.value)}"
