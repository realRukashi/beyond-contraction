.PHONY: all clean
all:
	latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf preprint.pdf
clean:
	latexmk -C main.tex
