#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT="${SCRIPT_DIR}/Информатика_конспект.docx"
COMBINED="/tmp/combined_notes.md"
TMP_DIR="/tmp/md2docx_$$"

cleanup() {
    rm -rf "$TMP_DIR" "$COMBINED"
}
trap cleanup EXIT

echo "==> Сборка единого DOCX из всех конспектов..."

# -- Порядок секций (только note.md и task.md, без python.md/spravochnik)
# -- Каждый элемент: "Заголовок|относительный_путь"
SECTIONS=(
    "Приложение. Bash|docs/0. Appendix/bash.md"
    "Приложение. C|docs/0. Appendix/clang.md"
    "Приложение. Git|docs/0. Appendix/git.md"
    "Приложение. How to Solve|docs/0. Appendix/HowToSolve.md"
    "Приложение. Логарифмы|docs/0. Appendix/log.md"
    "Приложение. Python (справочник)|docs/0. Appendix/python.md"
    "Приложение. Настройка IDE|docs/0. Appendix/simple-ide.md"
    "1. Введение. Конспект|docs/1. Intro/note.md"
    "1. Введение. Задачи|docs/1. Intro/task.md"
    "2. Основы. Конспект|docs/2. Start/note.md"
    "2. Основы. Задачи|docs/2. Start/task.md"
    "2. Основы. Python|docs/2. Start/python.md"
    "3. Алгоритмы. Конспект|docs/3. Algo/note.md"
    "3. Алгоритмы. Задачи|docs/3. Algo/task.md"
    "3. Алгоритмы. Python|docs/3. Algo/python.md"
    "4. Структуры данных. Конспект|docs/4. Data Types/note.md"
    "4. Структуры данных. Задачи|docs/4. Data Types/task.md"
    "4. Структуры данных. Python|docs/4. Data Types/python.md"
    "5. Стратегии. Конспект|docs/5. Strategy/note.md"
    "5. Стратегии. Задачи|docs/5. Strategy/task.md"
    "6. Лабораторная 1. UNO|docs/6. Lab 1 UNO/task.md"
    "7. Деревья. Конспект|docs/7. Balanced Tree/note.md"
    "7. Деревья. Задачи|docs/7. Balanced Tree/task.md"
    "8. Лабораторная 2. Maze|docs/8. Lab 2 Maze/task.md"
    "9. Криптография. Конспект|docs/9. Crypto/note.md"
    "9. Криптография. Задачи|docs/9. Crypto/task.md"
    "Тест 1|docs/Tests/2025_test_1.md"
    "Тест 2|docs/Tests/2025_test_2.md"
    "Экзамен|docs/Exam/exam_2025.md"
)

mkdir -p "$TMP_DIR"

# -- Собираем единый .md, подменяя пути к картинкам
> "$COMBINED"

for entry in "${SECTIONS[@]}"; do
    title="${entry%%|*}"
    relpath="${entry##*|}"

    if [[ ! -f "$SCRIPT_DIR/$relpath" ]]; then
        echo "  [пропущен] $relpath — файл не найден"
        continue
    fi

    # Путь к родительской директории секции для подстановки картинок
    section_dir="$(dirname "$relpath")"

    echo "  + $title"

    {
        echo ""
        echo "# $title"
        echo ""
        # Подменяем ![alt](images/...) → ![alt](<section_dir>/...)
        # и ![alt](/graphics/...) → оставляем как есть или убираем (это внешние/мёртвые ссылки)
        sed -E "s|!\[([^]]*)\]\(images/|![\1]($section_dir/images/|g" "$SCRIPT_DIR/$relpath"
        echo ""
        echo "\\newpage"
        echo ""
    } >> "$COMBINED"
done

echo "==> Конвертация через pandoc..."
pandoc "$COMBINED" \
    -o "$OUTPUT" \
    --from markdown-yaml_metadata_block \
    --to docx \
    --resource-path="$SCRIPT_DIR" \
    --metadata title="Информатика — конспект курса" \
    --metadata author="ТУСУР, ИСиТ" \
    --metadata lang="ru" \
    --toc \
    --toc-depth=2 \
    --number-sections

echo "==> Готово: $OUTPUT"
ls -lh "$OUTPUT"
