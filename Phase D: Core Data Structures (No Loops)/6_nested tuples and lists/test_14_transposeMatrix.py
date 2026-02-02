import sys
import importlib.util
from pathlib import Path


def _run_script(path: Path):
    if not path.exists():
        raise AssertionError(f"expected output\n[[1, 4], [2, 5], [3, 6]]\n\nactual output\n<missing file: {path.name}>\n")

    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)

    captured = []

    class _Cap:
        def write(self, s):
            captured.append(s)
        def flush(self):
            pass

    old_stdout = sys.stdout
    try:
        sys.stdout = _Cap()
        spec.loader.exec_module(module)
    finally:
        sys.stdout = old_stdout

    return "".join(captured)


def test_14_transposeMatrix_stdout_exact():
    script = Path(__file__).resolve().parent / "14_transposeMatrix.py"
    expected = "[[1, 4], [2, 5], [3, 6]]\n"
    actual = _run_script(script)
    if actual != expected:
        raise AssertionError(f"expected output\n{expected}\nactual output\n{actual}")
