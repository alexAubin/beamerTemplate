MAIN = main

TEX = xelatex

PARSER = 2>&1 | grep "\\\.box\|\!\|^l\.\|^  " | grep -v "Overfull\|Rotate 90" 

$(MAIN).pdf : $(MAIN).tex ../slides.tex ../title.tex
	$(TEX) -interaction=nonstopmode $(MAIN).tex $(PARSER); cp $(MAIN).pdf ../slides.pdf

pdf : $(MAIN).pdf

clean :
	rm -f *.aux *.log *.out *.dvi *.pdf

