import io
import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path):
    if not path.exists():
        raise AssertionError(f"expected output\n<file {path.name} to exist>\nactual output\n<file missing>")

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    if spec is None or spec.loader is None:
        raise AssertionError(f"expected output\n<module to load>\nactual output\n<failed to load>")

    module = importlib.util.module_from_spec(spec)
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        spec.loader.exec_module(module)
        return sys.stdout.getvalue()
    except Exception as e:
        raise AssertionError(f"expected output\n['c', 'a', 'b']\nactual output\n<exception: {type(e).__name__}: {e}>")
    finally:
        sys.stdout = old_stdout


def test_output_exact():
    script_path = Path(__file__).resolve().parent / "11_sortByValue.py"
    actual = _run_script(script_path)
    expected = "['c', 'a', 'b']\n"
    if actual != expected:
        raise AssertionError(f"expected output\n{expected}actual output\n{actual}")
