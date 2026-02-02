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


def test_prints_exact_ascii_box_output():
    out = run_file_and_capture_stdout("10_printAsciiBox.py")
    expected = "+----------+\n|  Python  |\n+----------+\n"
    assert out == expected, f"expected={expected!r} actual={out!r}"


def test_does_not_use_triple_quoted_output_string():
    module = load_module_for_inspection("10_printAsciiBox.py")
    src = getattr(module, "__source__", None) or getattr(module, "__file_source__", None) or ""
    assert '"""' not in src and "'''" not in src, f"expected no triple-quoted strings actual source contains triple quotes"


def test_constructs_lines_in_variables_and_are_strings():
    module = load_module_for_inspection("10_printAsciiBox.py")
    for name in ("line1", "line2", "line3"):
        assert hasattr(module, name), f"expected module to define {name} actual missing"
        val = getattr(module, name)
        assert isinstance(val, str), f"expected {name} to be str actual type={type(val)!r}"


def test_line_lengths_and_content_constraints():
    module = load_module_for_inspection("10_printAsciiBox.py")
    line1 = module.line1
    line2 = module.line2
    line3 = module.line3
    assert len(line1) == 12, f"expected len(line1)==12 actual len={len(line1)} line1={line1!r}"
    assert len(line3) == 12, f"expected len(line3)==12 actual len={len(line3)} line3={line3!r}"
    assert line1 == "+----------+", f"expected line1 border '+----------+' actual {line1!r}"
    assert line3 == "+----------+", f"expected line3 border '+----------+' actual {line3!r}"
    assert line2.startswith("|"), f"expected line2 to start with '|' actual {line2!r}"
    assert line2.endswith("|"), f"expected line2 to end with '|' actual {line2!r}"
    assert line2 == "|  Python  |", f"expected middle line '|  Python  |' actual {line2!r}"


def test_text_variable_is_python():
    module = load_module_for_inspection("10_printAsciiBox.py")
    assert hasattr(module, "text"), f"expected module to define text actual missing"
    assert module.text == "Python", f"expected text=='Python' actual {module.text!r}"
