book.pdf: book.md
	pandoc $< -o $@ --template=template.tmpl -N --toc -V documentclass:book

book.md: 
	cat *.pd > book.md

all: $(OBJS) Makefile

clean:
	rm -f $(OBJS)
	rm -f *.toc
	rm -f *.tuo
	rm -f book.md
	rm -f book.tex
	rm -f book.pdf
	rm -f *.aux
	rm -f *.log

.PHONY: clean
