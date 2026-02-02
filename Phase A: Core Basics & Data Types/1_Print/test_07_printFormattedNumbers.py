import importlib.util
import io
import os
import re
import sys
from contextlib import redirect_stdout


def _import_assignment_module(file_name):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, file_name)
    assert os.path.exists(file_path), f"Assignment file not found at: {file_path}"
    module_name = re.sub(r"\W+", "_", os.path.splitext(os.path.basename(file_name))[0])
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec is not None and spec.loader is not None, "Failed to create module spec"
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _run_and_capture_stdout(file_name):
    buf = io.StringIO()
    with redirect_stdout(buf):
        _import_assignment_module(file_name)
    return buf.getvalue()


def test_prints_total_with_two_decimals_and_exact_format():
    expected = "Total: 19.90\n"
    actual = _run_and_capture_stdout("07_printFormattedNumbers.py")
    if actual != expected:
        print(f"expected: {expected!r}")
        print(f"actual:   {actual!r}")
    assert actual == expected


def test_does_not_print_extra_lines_or_whitespace_variations():
    expected = "Total: 19.90\n"
    actual = _run_and_capture_stdout("07_printFormattedNumbers.py")
    if actual.strip("\n") != expected.strip("\n") or actual.count("\n") != 1:
        print(f"expected: {expected!r}")
        print(f"actual:   {actual!r}")
    assert actual == expected