"""Инфраструктура автоматической проверки решений.

Решения студента лежат отдельными файлами в папке, которая по умолчанию
называется `solutions` и находится в корне репозитория. Путь можно
переопределить:

    pytest --solutions=path/to/dir
    SOLUTIONS=path/to/dir pytest

Каждая задача --- отдельный файл с функцией, имя которой указано в условии.
Если файла нет, тесты этой задачи помечаются как пропущенные (skipped),
а не как упавшие: студент, решивший половину задач, должен видеть
зелёные точки за решённое, а не стену красного.
"""

import importlib.util
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

# Папки data/ разделов кладём в путь поиска модулей: часть задач импортирует
# готовые данные (например `from morse import morse` в занятии 2).
for _data_dir in sorted(ROOT.glob("docs/*/data")):
    if str(_data_dir) not in sys.path:
        sys.path.append(str(_data_dir))


def pytest_addoption(parser):
    parser.addoption(
        "--solutions",
        action="store",
        default=None,
        help="Папка с решениями студента (по умолчанию: ./solutions)",
    )


@pytest.fixture(scope="session")
def solutions_dir(pytestconfig):
    raw = pytestconfig.getoption("--solutions") or os.environ.get("SOLUTIONS")
    path = Path(raw).expanduser() if raw else ROOT / "solutions"
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    return path


def _load_module(directory: Path, name: str):
    """Импортирует <directory>/<name>.py как модуль. Пропускает тест, если файла нет."""
    path = directory / f"{name}.py"
    if not path.exists():
        pytest.skip(f"нет файла {path.name} в {directory}")

    spec = importlib.util.spec_from_file_location(f"solution_{name}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # noqa: BLE001 --- показываем студенту любую поломку
        pytest.fail(f"{path.name} не импортируется: {type(exc).__name__}: {exc}")
    return module


@pytest.fixture(scope="session")
def solution(solutions_dir):
    """Фикстура-загрузчик.

    Использование в тесте:

        def test_something(solution):
            f = solution("task_01", "meters_to_centimeters")
            assert f(5) == 500
    """

    cache = {}

    def _get(module_name: str, func_name: str | None = None):
        if module_name not in cache:
            cache[module_name] = _load_module(solutions_dir, module_name)
        module = cache[module_name]
        if func_name is None:
            return module
        if not hasattr(module, func_name):
            pytest.fail(
                f"в {module_name}.py нет функции {func_name}(). "
                f"Имя функции должно совпадать с указанным в условии задачи."
            )
        return getattr(module, func_name)

    return _get


@pytest.fixture(scope="session")
def data_dir():
    """Путь к папке с данными раздела.

        def test_something(data_dir):
            path = data_dir("02-logic") / "morse.py"
    """

    def _get(section: str) -> Path:
        path = ROOT / "docs" / section / "data"
        if not path.is_dir():
            pytest.skip(f"нет папки с данными: {path}")
        return path

    return _get


def pytest_report_header(config):
    raw = config.getoption("--solutions") or os.environ.get("SOLUTIONS")
    path = Path(raw) if raw else ROOT / "solutions"
    marker = "" if path.exists() else "  [папки нет --- все тесты будут пропущены]"
    return f"решения: {path}{marker}"
