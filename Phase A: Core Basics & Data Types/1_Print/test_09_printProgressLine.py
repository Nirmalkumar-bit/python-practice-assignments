import importlib.util
import io
import os
import re
import sys
import runpy
from contextlib import redirect_stdout

BASE_DIR = os.path.dirname(__file__)

def load_module_for_inspection(file_name: str):
    file_path = os.path.join(BASE_DIR, file_name)
    assert os.path.exists(file_path), f"Assignment file not found: {file_name}"

    module_name = os.path.splitext(file_name)[0]
    module_name = re.sub(r"\W+", "_", module_name)
    if not module_name[0].isalpha() and module_name[0] != "_":
        module_name = "_" + module_name

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec and spec.loader, "Failed to create module spec"

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


def run_file_and_capture_stdout(file_name: str) -> str:
    file_path = os.path.join(BASE_DIR, file_name)
    assert os.path.exists(file_path), f"Assignment file not found: {file_name}"

    buf = io.StringIO()
    with redirect_stdout(buf):
        runpy.run_path(file_path, run_name="__main__")

    return buf.getvalue()


def test_printProgressLine_final_output_exact():
    expected = "Loading... 100%\n"
    actual = run_file_and_capture_stdout("09_printProgressLine.py")
    assert actual == expected, f"expected={expected!r} actual={actual!r}"


def test_printProgressLine_no_extra_output():
    actual = run_file_and_capture_stdout("09_printProgressLine.py")
    assert actual.count("\n") == 1, f"expected_newline_count=1 actual_newline_count={actual.count('\n')}"


def test_printProgressLine_starts_with_loading():
    actual = run_file_and_capture_stdout("09_printProgressLine.py")
    assert actual.startswith("Loading..."), f"expected_prefix={'Loading...':!r} actual_start={actual[:20]!r}"


def test_printProgressLine_ends_with_newline_only_once():
    actual = run_file_and_capture_stdout("09_printProgressLine.py")
    assert actual.endswith("\n"), f"expected_end={'\\n':!r} actual_end={actual[-10:]!r}"
    assert not actual.endswith("\n\n"), f"expected_not_end={'\\n\\n':!r} actual_end={actual[-10:]!r}"
