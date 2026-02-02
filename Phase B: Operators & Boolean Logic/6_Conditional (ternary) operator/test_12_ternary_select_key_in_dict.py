import importlib.util
from pathlib import Path


def _run_script(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)


def test_stdout_exact(capsys):
    script_path = Path(__file__).resolve().parent / "12_ternary_select_key_in_dict.py"
    assert script_path.exists(), f"expected output: token=BK-999\n\nactual output: <missing file {script_path}>"

    _run_script(script_path)
    captured = capsys.readouterr()
    expected = "token=BK-999\n"
    actual = captured.out
    assert actual == expected, f"expected output: {expected}actual output: {actual}"
