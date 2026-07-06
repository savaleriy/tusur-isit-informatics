.PHONY: all build serve clean docx utf8 fix-blocks

all: utf8 fix-blocks build

build:
	mkdocs build

serve:
	mkdocs serve

clean:
	rm -rf site/

docx:
	python3 build_docx.py

utf8:
	python3 scripts/replace_utf8.py

fix-blocks:
	python3 scripts/fix_code_blocks.py
