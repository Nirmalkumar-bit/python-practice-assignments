import sys
import importlib.util
from pathlib import Path

def _run_script(path: Path):
    if not path.exists():
        raise AssertionError(f"expected output: ['a', 'b', 'c']\nactual output: <file not found: {path.name}>")

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)

    captured = []

    class _Cap:
        def write(self, s):
            captured.append(s)
        def flush(self):
            pass

    old_stdout = sys.stdout
    sys.stdout = _Cap()
    try:
        spec.loader.exec_module(module)
    finally:
        sys.stdout = old_stdout

    return "".join(captured)


def test_stdout_exact_match():
    script_path = Path(__file__).resolve().parent / '08_splitAndFilterEmpty.py'
    expected = "['a', 'b', 'c']\n"
    actual = _run_script(script_path)
    if actual != expected:
        raise AssertionError(f"expected output: {expected}actual output: {actual}")
