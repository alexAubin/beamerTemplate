MAIN = main

TEX = latex


$(MAIN).pdf : $(MAIN).tex ../slides.tex ../title.tex
	$(TEX) $(MAIN).tex; dvipdf $(MAIN).dvi $(MAIN).pdf; cp $(MAIN).pdf ../slides.pdf

pdf : $(MAIN).pdf

clean :
	rm -f *.aux *.log *.out *.dvi *.pdf

