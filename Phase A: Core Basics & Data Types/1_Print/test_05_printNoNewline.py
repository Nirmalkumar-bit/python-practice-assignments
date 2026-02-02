import importlib.util
import io
import os
import re
import sys
import pytest
from contextlib import redirect_stdout


def _load_module_from_filename(filename):
    path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(path):
        raise AssertionError(f"Target file not found: {path}")
    module_name = re.sub(r"\W+", "_", os.path.splitext(os.path.basename(filename))[0])
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise AssertionError("Failed to create import spec for target module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _run_and_capture_stdout(filename):
    buf = io.StringIO()
    with redirect_stdout(buf):
        _load_module_from_filename(filename)
    return buf.getvalue()


def _normalize_newlines(s):
    return s.replace("\r\n", "\n").replace("\r", "\n")


def test_print_no_newline_exact_output():
    expected = "Hello there\n"
    actual = _normalize_newlines(_run_and_capture_stdout("05_printNoNewline.py"))
    if actual != expected:
        print(f"expected: {expected!r}")
        print(f"actual:   {actual!r}")
    assert actual == expected


def test_print_no_newline_no_extra_whitespace_or_lines():
    expected = "Hello there\n"
    actual = _normalize_newlines(_run_and_capture_stdout("05_printNoNewline.py"))

    if actual != expected:
        print(f"expected: {expected!r}")
        print(f"actual:   {actual!r}")
    assert actual == expected

    assert actual.count("\n") == 1
    assert actual.startswith("Hello ")
    assert "  " not in actual
    assert actual.strip("\n") == "Hello there"


def test_print_no_newline_no_additional_output():
    expected = "Hello there\n"
    actual = _normalize_newlines(_run_and_capture_stdout("05_printNoNewline.py"))

    if actual != expected:
        print(f"expected: {expected!r}")
        print(f"actual:   {actual!r}")
    assert actual == expected

    assert actual == expected
    assert actual.splitlines() == ["Hello there"]