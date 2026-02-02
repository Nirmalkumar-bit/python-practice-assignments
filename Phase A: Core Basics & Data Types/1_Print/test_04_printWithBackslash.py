import importlib.util
import os
import re
import sys


def _load_module_from_filename(filename):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)
    assert os.path.exists(file_path), f"Target file not found: {file_path}"

    module_name = re.sub(r"\W+", "_", os.path.splitext(os.path.basename(filename))[0])
    module_name = f"assignment_{module_name}"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec is not None and spec.loader is not None, "Failed to create import spec"

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _normalize_output(s):
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    return s


def test_print_windows_path_exact(capsys):
    filename = "04_printWithBackslash.py"
    _load_module_from_filename(filename)
    captured = capsys.readouterr()
    actual = _normalize_output(captured.out)
    expected = "C:\\Users\\Ava\\Documents\n"
    if actual != expected:
        print(f"expected value: {expected!r}")
        print(f"actual value: {actual!r}")
    assert actual == expected


def test_no_extra_stdout(capsys):
    filename = "04_printWithBackslash.py"
    _load_module_from_filename(filename)
    captured = capsys.readouterr()
    actual = _normalize_output(captured.out)
    expected = "C:\\Users\\Ava\\Documents\n"
    if actual != expected:
        print(f"expected value: {expected!r}")
        print(f"actual value: {actual!r}")
    assert actual == expected