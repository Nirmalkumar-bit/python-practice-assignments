import importlib.util
import io
import os
import sys
import contextlib


def _load_module_from_filename(filename):
    path = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(path):
        raise AssertionError(f"Target file not found: {path}")
    module_name = os.path.splitext(os.path.basename(filename))[0]
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Could not create import spec for: {filename}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _run_and_capture_stdout(filename):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        _load_module_from_filename(filename)
    return buf.getvalue()


def _normalize_output(text):
    return text.replace("\r\n", "\n").replace("\r", "\n")


def test_prints_two_lines_exactly():
    filename = "02_printTwoLines.py"
    actual = _normalize_output(_run_and_capture_stdout(filename))
    expected = "Line 1\nLine 2\n"
    if actual != expected:
        print(f"expected: {expected!r}")
        print(f"actual:   {actual!r}")
    assert actual == expected


def test_no_extra_whitespace_or_blank_lines():
    filename = "02_printTwoLines.py"
    actual = _normalize_output(_run_and_capture_stdout(filename))
    expected_lines = ["Line 1", "Line 2"]
    actual_lines = actual.split("\n")
    if actual_lines and actual_lines[-1] == "":
        actual_lines = actual_lines[:-1]
    if actual_lines != expected_lines:
        print(f"expected: {expected_lines!r}")
        print(f"actual:   {actual_lines!r}")
    assert actual_lines == expected_lines