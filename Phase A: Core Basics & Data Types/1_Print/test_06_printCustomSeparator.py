import importlib.util
import io
import os
import re
import sys
import contextlib
import pytest


def _load_module_from_filename(filename):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)
    if not os.path.exists(file_path):
        file_path = os.path.abspath(filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Target file not found: {filename}")

    module_name = os.path.splitext(os.path.basename(filename))[0]
    module_name = re.sub(r"\W+", "_", module_name)
    if not re.match(r"^[A-Za-z_]", module_name):
        module_name = f"m_{module_name}"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for {filename}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _run_and_capture_stdout(filename):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        _load_module_from_filename(filename)
    return buf.getvalue()


def _normalize_output(s):
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    if s.endswith("\n"):
        s = s[:-1]
    return s


def test_print_custom_separator_exact_output(capsys):
    filename = "06_printCustomSeparator.py"
    out = _run_and_capture_stdout(filename)
    actual = _normalize_output(out)
    expected = "1 | 2 | 3"
    if actual != expected:
        print(f"expected: {expected}")
        print(f"actual: {actual}")
    assert actual == expected


def test_print_custom_separator_no_extra_lines():
    filename = "06_printCustomSeparator.py"
    out = _run_and_capture_stdout(filename)
    s = out.replace("\r\n", "\n").replace("\r", "\n")
    lines = s.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    expected_lines = ["1 | 2 | 3"]
    if lines != expected_lines:
        print(f"expected: {expected_lines}")
        print(f"actual: {lines}")
    assert lines == expected_lines


def test_print_custom_separator_no_extra_spaces_or_missing_pipes():
    filename = "06_printCustomSeparator.py"
    out = _run_and_capture_stdout(filename)
    actual = _normalize_output(out)
    expected = "1 | 2 | 3"
    if actual != expected:
        print(f"expected: {expected}")
        print(f"actual: {actual}")
    assert actual == expected
    assert actual.count("|") == 2
    assert "  " not in actual
    assert actual.startswith("1")
    assert actual.endswith("3")