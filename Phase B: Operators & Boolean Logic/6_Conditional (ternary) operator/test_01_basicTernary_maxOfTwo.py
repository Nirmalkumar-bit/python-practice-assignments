import importlib.util
from pathlib import Path


def _run_script(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def test_stdout_exact(capsys):
    script_path = Path(__file__).resolve().parent / "01_basicTernary_maxOfTwo.py"
    assert script_path.exists(), f"expected output: max=10\n\nactual output: <missing file {script_path}>"

    _run_script(script_path)
    captured = capsys.readouterr()
    expected = "max=10\n"
    actual = captured.out
    assert actual == expected, f"expected output: {expected}actual output: {actual}"
