import importlib.util
import io
import os
import re
import sys
from contextlib import redirect_stdout


def _load_module_from_path(path):
    module_name = re.sub(r"\W+", "_", os.path.splitext(os.path.basename(path))[0])
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _run_and_capture_stdout(path):
    buf = io.StringIO()
    with redirect_stdout(buf):
        _load_module_from_path(path)
    return buf.getvalue()


def test_print_aligned_table_exact_output():
    target_path = os.path.join(os.path.dirname(__file__), "08_printAlignedTable.py")
    actual = _run_and_capture_stdout(target_path)

    expected = "Item      Qty\nApples      3\nBananas    12\n"

    if actual != expected:
        print("expected:", repr(expected))
        print("actual:", repr(actual))
    assert actual == expected


def test_print_aligned_table_no_extra_lines_or_spaces():
    target_path = os.path.join(os.path.dirname(__file__), "08_printAlignedTable.py")
    actual = _run_and_capture_stdout(target_path)

    lines = actual.splitlines()

    expected_lines = ["Item      Qty", "Apples      3", "Bananas    12"]
    if lines != expected_lines:
        print("expected:", repr(expected_lines))
        print("actual:", repr(lines))
    assert lines == expected_lines

    for i, (a, e) in enumerate(zip(lines, expected_lines), start=1):
        if a != e:
            print("expected:", repr(e))
            print("actual:", repr(a))
        assert a == e

    if not actual.endswith("\n"):
        print("expected:", repr("output to end with a single trailing newline"))
        print("actual:", repr("output missing trailing newline"))
    assert actual.endswith("\n")