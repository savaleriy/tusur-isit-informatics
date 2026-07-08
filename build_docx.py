#!/usr/bin/env python3
"""Сборка единого DOCX из всех конспектов через HTML-посредник.

Проблема pandoc: $ в bash-коде парсится как LaTeX math.
Решение: markdown → HTML (Python-markdown не трогает $) → pandoc → DOCX.
"""

import subprocess
import sys
from pathlib import Path
from html import escape as html_escape

import markdown

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "Информатика_конспект.docx"
TEMPLATE = ROOT / "style.docx"

SECTIONS = [
    ("Приложение. Bash",                 "docs/0. Appendix/bash.md"),
    ("Приложение. C",                    "docs/0. Appendix/clang.md"),
    ("Приложение. Git",                  "docs/0. Appendix/git.md"),
    ("Приложение. How to Solve",         "docs/0. Appendix/HowToSolve.md"),
    ("Приложение. Логарифмы",            "docs/0. Appendix/log.md"),
    ("Приложение. Python (справочник)",  "docs/0. Appendix/python.md"),
    ("Приложение. Настройка IDE",        "docs/0. Appendix/simple-ide.md"),
    ("1. Введение. Конспект",           "docs/1. Intro/note.md"),
    ("1. Введение. Задачи",             "docs/1. Intro/task.md"),
    ("2. Основы. Конспект",             "docs/2. Start/note.md"),
    ("2. Основы. Задачи",               "docs/2. Start/task.md"),
    ("2. Основы. Python",               "docs/2. Start/python.md"),
    ("3. Алгоритмы. Конспект",          "docs/3. Algo/note.md"),
    ("3. Алгоритмы. Задачи",            "docs/3. Algo/task.md"),
    ("3. Алгоритмы. Python",            "docs/3. Algo/python.md"),
    ("4. Структуры данных. Конспект",   "docs/4. Data Types/note.md"),
    ("4. Структуры данных. Задачи",     "docs/4. Data Types/task.md"),
    ("4. Структуры данных. Python",     "docs/4. Data Types/python.md"),
    ("5. Стратегии. Конспект",          "docs/5. Strategy/note.md"),
    ("5. Стратегии. Задачи",            "docs/5. Strategy/task.md"),
    ("6. Лабораторная 1. UNO",          "docs/6. Lab 1 UNO/task.md"),
    ("7. Деревья. Конспект",            "docs/7. Balanced Tree/note.md"),
    ("7. Деревья. Задачи",              "docs/7. Balanced Tree/task.md"),
    ("8. Лабораторная 2. Maze",         "docs/8. Lab 2 Maze/task.md"),
    ("9. Криптография. Конспект",       "docs/9. Crypto/note.md"),
    ("9. Криптография. Задачи",         "docs/9. Crypto/task.md"),
    ("Тест 1",                          "docs/Tests/2025_test_1.md"),
    ("Тест 2",                          "docs/Tests/2025_test_2.md"),
    ("Экзамен",                         "docs/Exam/exam_2025.md"),
]

MD = markdown.Markdown(extensions=[
    "fenced_code",
    "tables",
    "codehilite",
    "toc",
    "nl2br",
    "sane_lists",
])

def image_path_replacer(html: str, section_dir: str) -> str:
    """Заменяет относительные пути images/... на section_dir/images/..."""
    old = 'src="images/'
    new = f'src="{section_dir}/images/'
    return html.replace(old, new)

def build():
    print("==> Сборка единого DOCX через HTML...")
    combined_html_parts = []

    for title, relpath in SECTIONS:
        md_path = ROOT / relpath
        if not md_path.exists():
            print(f"  [пропущен] {relpath}")
            continue

        print(f"  + {title}")

        md_text = md_path.read_text(encoding="utf-8")
        html_body = MD.convert(md_text)
        section_dir = relpath.rsplit("/", 1)[0]
        html_body = image_path_replacer(html_body, section_dir)

        combined_html_parts.append(f"""\
<section class="chapter">
<h1>{html_escape(title)}</h1>
{html_body}
</section>
""")

    html_doc = f"""\
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<title>Информатика — конспект курса</title>
<style>
  body {{ font-family: Arial, sans-serif; font-size: 12pt; line-height: 1.5; }}
  code, pre {{ font-family: "Courier New", monospace; font-size: 10pt; }}
  table {{ border-collapse: collapse; width: 100%; }}
  td, th {{ border: 1px solid #ccc; padding: 4px 8px; }}
</style>
</head>
<body>
{chr(10).join(combined_html_parts)}
</body>
</html>
"""

    html_path = Path("/tmp/combined_notes.html")
    html_path.write_text(html_doc, encoding="utf-8")
    print(f"  HTML собран: {html_path} ({html_path.stat().st_size / 1024:.0f} KB)")

    print("==> Конвертация HTML → DOCX через pandoc...")
    subprocess.run([
        "pandoc", str(html_path),
        "-o", str(OUTPUT),
        "--from", "html",
        "--to", "docx",
        "--metadata", "title=Информатика — конспект курса",
        "--metadata", "author=ТУСУР, ИСиТ",
        "--metadata", "lang=ru",
        "--toc", "--toc-depth=2", "--number-sections",
        f"--reference-doc={TEMPLATE}"
    ], check=True)

    print(f"==> Готово: {OUTPUT}")
    print(f"    Размер: {OUTPUT.stat().st_size / 1024 / 1024:.1f} MB")

if __name__ == "__main__":
    build()
