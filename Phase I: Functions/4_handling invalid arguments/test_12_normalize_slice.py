import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "12_normalize_slice.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_12_normalize_slice", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_normalize_slice_expected_example():
    m = load_module()
    out = m.normalize_slice(10, 2, None, 2)
    assert out == (2, 10, 2), f"expected output: (2, 10, 2)\nactual output: {out!r}"


def test_normalize_slice_matches_python_indices_various():
    m = load_module()
    cases = [
        (5, None, None, 1),
        (5, -10, 10, 1),
        (5, 1, 4, 1),
        (5, None, None, -1),
        (5, 4, None, -1),
        (0, None, None, 1),
    ]
    for seq_len, start, stop, step in cases:
        expected = slice(start, stop, step).indices(seq_len)
        out = m.normalize_slice(seq_len, start, stop, step)
        assert out == expected, f"expected output: {expected!r}\nactual output: {out!r}"


@pytest.mark.parametrize("seq_len", [True, False, -1, 1.0, "5", None])
def test_normalize_slice_seq_len_invalid(seq_len):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.normalize_slice(seq_len)
    assert str(ei.value) == "seq_len must be a non-negative int", f"expected output: seq_len must be a non-negative int\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("start", [True, 1.0, "1", [], {}])
def test_normalize_slice_start_invalid_type(start):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.normalize_slice(5, start=start)
    assert str(ei.value) == "start/stop must be int or None", f"expected output: start/stop must be int or None\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("stop", [False, 2.0, "2", [], {}])
def test_normalize_slice_stop_invalid_type(stop):
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.normalize_slice(5, stop=stop)
    assert str(ei.value) == "start/stop must be int or None", f"expected output: start/stop must be int or None\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("step", [0, True, False, 1.0, "1", None])
def test_normalize_slice_step_invalid(step):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.normalize_slice(5, 0, 5, step)
    assert str(ei.value) == "step must be a non-zero int", f"expected output: step must be a non-zero int\nactual output: {str(ei.value)}"
