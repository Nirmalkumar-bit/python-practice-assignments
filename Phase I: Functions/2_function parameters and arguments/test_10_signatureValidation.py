import importlib.util
from pathlib import Path
import sys


def _run_script(path: Path):
    if not path.exists():
        raise AssertionError(f"expected output\n<file exists>\nactual output\n<missing file: {path.name}>")
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules.pop(path.stem, None)
    spec.loader.exec_module(module)


def test_stdout_exact(capsys):
    path = Path(__file__).resolve().parent / "10_signatureValidation.py"
    _run_script(path)
    out = capsys.readouterr().out
    expected = "user=ana; role=admin; active=True\nuser=bob; role=member; active=False\n"
    if out != expected:
        raise AssertionError(f"expected output\n{expected}actual output\n{out}")
