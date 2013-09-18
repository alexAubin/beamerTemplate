MAIN = main

TEX = xelatex


$(MAIN).pdf : $(MAIN).tex ../slides.tex ../title.tex
	$(TEX) -interaction=nonstopmode $(MAIN).tex | grep "\\\.box\|\!\|^l\.\|^  " ; cp $(MAIN).pdf ../slides.pdf

pdf : $(MAIN).pdf

clean :
	rm -f *.aux *.log *.out *.dvi *.pdf

