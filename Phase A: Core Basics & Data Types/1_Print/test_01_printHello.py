import importlib.util
import io
import os
import re
import sys
import types
import pytest


def import_assignment_module(file_name: str) -> types.ModuleType:
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_name)
    assert os.path.exists(file_path), f"Assignment file not found: {file_path}"

    module_name = re.sub(r"\W+", "_", os.path.splitext(file_name)[0])
    if not re.match(r"^[A-Za-z_]\w*$", module_name):
        module_name = f"m_{module_name}"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec is not None and spec.loader is not None, "Failed to create module spec"
    module = importlib.util.module_from_spec(spec)

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        spec.loader.exec_module(module)
    finally:
        sys.stdout = old_stdout

    return module


def run_assignment_and_capture_stdout(file_name: str) -> str:
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_name)
    assert os.path.exists(file_path), f"Assignment file not found: {file_path}"

    module_name = re.sub(r"\W+", "_", os.path.splitext(file_name)[0])
    if not re.match(r"^[A-Za-z_]\w*$", module_name):
        module_name = f"m_{module_name}"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec is not None and spec.loader is not None, "Failed to create module spec"
    module = importlib.util.module_from_spec(spec)

    buf = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf
    try:
        spec.loader.exec_module(module)
    finally:
        sys.stdout = old_stdout

    return buf.getvalue()


def test_prints_exact_line():
    expected = "Hello, world!\n"
    actual = run_assignment_and_capture_stdout("01_printHello.py")
    if actual != expected:
        print(f"expected: {expected!r}")
        print(f"actual: {actual!r}")
    assert actual == expected


def test_no_extra_output_lines():
    expected_lines = ["Hello, world!"]
    actual = run_assignment_and_capture_stdout("01_printHello.py")
    actual_lines = actual.splitlines()
    if actual_lines != expected_lines:
        print(f"expected: {expected_lines!r}")
        print(f"actual: {actual_lines!r}")
    assert actual_lines == expected_lines


def test_module_imports_without_error():
    try:
        import_assignment_module("01_printHello.py")
        actual = "imported"
        expected = "imported"
    except Exception as e:
        actual = f"{type(e).__name__}: {e}"
        expected = "imported"
        print(f"expected: {expected!r}")
        print(f"actual: {actual!r}")
        raise
    assert actual == expected