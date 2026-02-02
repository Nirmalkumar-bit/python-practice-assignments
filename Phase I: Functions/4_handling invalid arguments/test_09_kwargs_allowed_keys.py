import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "09_kwargs_allowed_keys.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_09_kwargs_allowed_keys", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_build_query_valid_minimal():
    m = load_module()
    out = m.build_query(q="cats", page=1)
    assert out == {"q": "cats", "page": 1}, f"expected output: {{'q': 'cats', 'page': 1}}\nactual output: {out!r}"


def test_build_query_strips_q():
    m = load_module()
    out = m.build_query(q="  dogs  ")
    assert out == {"q": "dogs"}, f"expected output: {{'q': 'dogs'}}\nactual output: {out!r}"


def test_build_query_unexpected_key_type_error():
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.build_query(sort="asc")
    assert str(ei.value) == "unexpected parameter: sort", f"expected output: unexpected parameter: sort\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("q", ["", "   ", "\n\t "])
def test_build_query_invalid_q(q):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.build_query(q=q)
    assert str(ei.value) == "q must be a non-empty string", f"expected output: q must be a non-empty string\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("page", [0, -1])
def test_build_query_page_must_be_positive(page):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.build_query(page=page)
    assert str(ei.value) == "page must be a positive int", f"expected output: page must be a positive int\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("page", [True, False, 1.0, "1", None])
def test_build_query_page_wrong_type_or_bool(page):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.build_query(page=page)
    assert str(ei.value) == "page must be a positive int", f"expected output: page must be a positive int\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("limit", [0, -5])
def test_build_query_limit_must_be_positive(limit):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.build_query(limit=limit)
    assert str(ei.value) == "limit must be a positive int", f"expected output: limit must be a positive int\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("limit", [True, False, 10.0, "10", None])
def test_build_query_limit_wrong_type_or_bool(limit):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.build_query(limit=limit)
    assert str(ei.value) == "limit must be a positive int", f"expected output: limit must be a positive int\nactual output: {str(ei.value)}"


def test_build_query_all_keys_valid():
    m = load_module()
    out = m.build_query(q="cats", page=2, limit=10)
    assert out == {"q": "cats", "page": 2, "limit": 10}, f"expected output: {{'q': 'cats', 'page': 2, 'limit': 10}}\nactual output: {out!r}"
