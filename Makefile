.PHONY: all build serve clean docx pdf

all: build

build: clean
	mkdocs build

serve:
	mkdocs serve

clean:
	rm -rf site/

docx:
	python3 build_docx.py docx

pdf:
	python3 build_docx.py pdf
