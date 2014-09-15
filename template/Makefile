TEX = xelatex

PARSER = 2>&1 | grep "\\\.box\|\!\|^l\.\|^  " | grep -v "Overfull\|Rotate 90" 

####################################################

main.pdf : *.tex slides.tex ../imgAndTables/*
	@$(TEX) -interaction=nonstopmode main.tex $(PARSER); cp main.pdf ../slides.pdf

slides.tex : ../slides.ltex
	python lighTexParser.py > slides.tex

pdf : main.pdf

clean :
	rm -f *.nav *.svm *.toc *.aux *.log *.out *.dvi *.pdf slides.tex

