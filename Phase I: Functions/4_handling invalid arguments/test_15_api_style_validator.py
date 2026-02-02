import importlib.util
from pathlib import Path
import pytest

ASSIGNMENT_FILE = Path(__file__).resolve().parent / "15_api_style_validator.py"


def load_module():
    if not ASSIGNMENT_FILE.exists():
        pytest.fail(f"expected output: file to exist at {ASSIGNMENT_FILE}\nactual output: file not found")
    spec = importlib.util.spec_from_file_location("mod_15_api_style_validator", ASSIGNMENT_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_validate_payload_valid_create():
    m = load_module()
    out = m.validate_payload({"action": "create", "data": {"name": "Pen", "price": 1.5}})
    assert out is True, f"expected output: True\nactual output: {out!r}"


def test_validate_payload_payload_must_be_dict():
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.validate_payload([("action", "create")])
    assert str(ei.value) == "payload must be a dict", f"expected output: payload must be a dict\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("missing_key", ["action", "data"])
def test_validate_payload_missing_required_keys(missing_key):
    m = load_module()
    payload = {"action": "create", "data": {"name": "Pen", "price": 1.5}}
    payload.pop(missing_key)
    with pytest.raises(KeyError) as ei:
        m.validate_payload(payload)
    assert str(ei.value) == f"'missing key: {missing_key}'", f"expected output: 'missing key: {missing_key}'\nactual output: {str(ei.value)}"


def test_validate_payload_no_extra_top_level_keys():
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.validate_payload({"action": "create", "data": {"name": "Pen", "price": 1.5}, "extra": 1})
    assert str(ei.value) == "unexpected key: extra", f"expected output: unexpected key: extra\nactual output: {str(ei.value)}"


def test_validate_payload_invalid_action():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "read", "data": {}})
    assert str(ei.value) == "invalid action", f"expected output: invalid action\nactual output: {str(ei.value)}"


def test_validate_payload_data_must_be_dict():
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.validate_payload({"action": "create", "data": "notadict"})
    assert str(ei.value) == "data must be a dict", f"expected output: data must be a dict\nactual output: {str(ei.value)}"


def test_validate_payload_meta_must_be_dict_if_present():
    m = load_module()
    with pytest.raises(TypeError) as ei:
        m.validate_payload({"action": "create", "data": {"name": "Pen", "price": 1.5}, "meta": "x"})
    assert str(ei.value) == "meta must be a dict", f"expected output: meta must be a dict\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("name", ["", "   ", None, 123])
def test_validate_payload_create_invalid_name(name):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "create", "data": {"name": name, "price": 1.5}})
    assert str(ei.value) == "invalid name", f"expected output: invalid name\nactual output: {str(ei.value)}"


@pytest.mark.parametrize("price", [0, -1, "1.5", None, True])
def test_validate_payload_create_invalid_price(price):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "create", "data": {"name": "Pen", "price": price}})
    assert str(ei.value) == "invalid price", f"expected output: invalid price\nactual output: {str(ei.value)}"


def test_validate_payload_update_valid_minimal():
    m = load_module()
    out = m.validate_payload({"action": "update", "data": {"id": 1}})
    assert out is True, f"expected output: True\nactual output: {out!r}"


def test_validate_payload_update_valid_with_fields():
    m = load_module()
    out = m.validate_payload({"action": "update", "data": {"id": 2, "name": "Book", "price": 10.0}})
    assert out is True, f"expected output: True\nactual output: {out!r}"


@pytest.mark.parametrize("id_val", [0, -1, "1", None, True])
def test_validate_payload_update_invalid_id(id_val):
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "update", "data": {"id": id_val}})
    assert str(ei.value) == "invalid id", f"expected output: invalid id\nactual output: {str(ei.value)}"


def test_validate_payload_update_invalid_name_if_present():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "update", "data": {"id": 1, "name": "   "}})
    assert str(ei.value) == "invalid name", f"expected output: invalid name\nactual output: {str(ei.value)}"


def test_validate_payload_update_invalid_price_if_present():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "update", "data": {"id": 1, "price": 0}})
    assert str(ei.value) == "invalid price", f"expected output: invalid price\nactual output: {str(ei.value)}"


def test_validate_payload_delete_valid():
    m = load_module()
    out = m.validate_payload({"action": "delete", "data": {"id": 2}})
    assert out is True, f"expected output: True\nactual output: {out!r}"


def test_validate_payload_delete_disallows_other_keys():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "delete", "data": {"id": 2, "name": "x"}})
    assert str(ei.value) == "invalid data keys", f"expected output: invalid data keys\nactual output: {str(ei.value)}"


def test_validate_payload_delete_invalid_id():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "delete", "data": {"id": 0}})
    assert str(ei.value) == "invalid id", f"expected output: invalid id\nactual output: {str(ei.value)}"


def test_validate_payload_create_invalid_data_keys():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "create", "data": {"name": "Pen", "price": 1.5, "id": 1}})
    assert str(ei.value) == "invalid data keys", f"expected output: invalid data keys\nactual output: {str(ei.value)}"


def test_validate_payload_update_invalid_data_keys():
    m = load_module()
    with pytest.raises(ValueError) as ei:
        m.validate_payload({"action": "update", "data": {"id": 1, "extra": 1}})
    assert str(ei.value) == "invalid data keys", f"expected output: invalid data keys\nactual output: {str(ei.value)}"
