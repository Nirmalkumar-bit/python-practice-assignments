import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "13_command_dispatcher.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_13_command_dispatcher", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_dispatch_add():
    m = load_module()
    out = m.dispatch("add", 2, 3)
    assert out == 5, f"expected output: 5\nactual output: {out!r}"


def test_dispatch_add_numeric_types():
    m = load_module()
    out = m.dispatch("add", 2.5, 1)
    assert out == pytest.approx(3.5), f"expected output: 3.5\nactual output: {out!r}"


def test_dispatch_pow_valid():
    m = load_module()
    out = m.dispatch("pow", 2, 3)
    assert out == 8, f"expected output: 8\nactual output: {out!r}"


def test_dispatch_echo_valid():
    m = load_module()
    out = m.dispatch("echo", "hi")
    assert out == "hi", f"expected output: 'hi'\nactual output: {out!r}"


@pytest.mark.parametrize("command", [None, 1, True, [], {}])
def test_dispatch_command_must_be_str(command):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.dispatch(command, 1, 2)
    assert str(ei.value) == "command must be a str", f"expected output: command must be a str\nactual output: {str(ei.value)}"


def test_dispatch_unknown_command():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.dispatch("noop")
    assert str(ei.value) == "unknown command", f"expected output: unknown command\nactual output: {str(ei.value)}"


@pytest.mark.parametrize(
    "command,args",
    [
        ("add", (1,)),
        ("add", (1, 2, 3)),
        ("pow", (2,)),
        ("pow", (2, 3, 4)),
        ("echo", ()),
        ("echo", ("a", "b")),
    ],
)
def test_dispatch_wrong_number_of_arguments(command, args):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.dispatch(command, *args)
    assert str(ei.value) == "wrong number of arguments", f"expected output: wrong number of arguments\nactual output: {str(ei.value)}"


@pytest.mark.parametrize(
    "command,args",
    [
        ("add", (True, 2)),
        ("add", (2, False)),
        ("add", ("2", 3)),
        ("pow", (True, 2)),
        ("pow", (2, 3.0)),
        ("pow", (2, "3")),
        ("echo", (1,)),
        ("echo", (True,)),
    ],
)
def test_dispatch_invalid_argument_type(command, args):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.dispatch(command, *args)
    assert str(ei.value) == "invalid argument type", f"expected output: invalid argument type\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("exp", [-1, -10])
def test_dispatch_pow_exponent_non_negative(exp):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.dispatch("pow", 2, exp)
    assert str(ei.value) == "exponent must be a non-negative int", f"expected output: exponent must be a non-negative int\nactual output: {str(ei.value)}"


def test_dispatch_pow_exponent_bool_invalid_type():
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.dispatch("pow", 2, True)
    assert str(ei.value) == "invalid argument type", f"expected output: invalid argument type\nactual output: {str(ei.value)}"
