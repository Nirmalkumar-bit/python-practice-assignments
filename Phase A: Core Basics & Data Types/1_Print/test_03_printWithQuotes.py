import importlib.util
import io
import os
import re
import sys
from contextlib import redirect_stdout

import pytest


def _load_module_from_filename(filename):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)
    if not os.path.isfile(file_path):
        file_path = os.path.abspath(filename)
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Assignment file not found: {filename}")

    module_name = os.path.splitext(os.path.basename(filename))[0]
    module_name = re.sub(r"\W+", "_", module_name)
    if not re.match(r"^[A-Za-z_]\w*$", module_name):
        module_name = f"m_{module_name}"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for: {filename}")

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


def test_prints_exact_sentence_with_double_quotes(capsys):
    expected = 'She said, "Python is fun!"\n'
    actual = _normalize_newlines(_run_and_capture_stdout("03_printWithQuotes.py"))
    if actual != expected:
        print(f"expected: {expected!r}")
        print(f"actual:   {actual!r}")
    assert actual == expected


def test_prints_only_one_line_no_extra_output(capsys):
    expected_line = 'She said, "Python is fun!"'
    actual = _normalize_newlines(_run_and_capture_stdout("03_printWithQuotes.py"))
    lines = actual.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    if lines != [expected_line]:
        print(f"expected: {[expected_line]!r}")
        print(f"actual:   {lines!r}")
    assert lines == [expected_line]