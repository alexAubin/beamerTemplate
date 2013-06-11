
DIRECTORY = template

pdf : 
	make -C $(DIRECTORY) pdf

clean : 
	make -C $(DIRECTORY) clean
