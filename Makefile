define TASKS
letter  make letter-sized version
a4      make a4-sized version
ipad    make ipad-sized version
all     make all versions
update  update neovim help from repository
cleanbuild   delete intermediate files
cleandoc delete output pdfs
clobber delete all files
endef
export TASKS

SHELL=/bin/bash

docdir = doc
helpfiles = $(wildcard $(docdir)/*.txt)

letter: neovimhelp.pdf
a4: neovimhelp-a4.pdf
ipad: neovimhelp-ipad.pdf
all: letter a4 ipad

update:
	./update.sh

$(docdir):
	./update.sh

%.pdf: %.tex body.tex FORCE
	xelatex $<

body.tex: $(helpfiles) $(docdir) contents.txt
	python3 neovim.py

cleanbuild:
	-rm body.tex *.log *.aux *.toc *.out
cleandoc:
	-rm -r $(docdir)

clobber: cleanbuild
	-rm neovimhelp{,-ipad,-a4}.pdf

help:
	@echo "$$TASKS"

.PHONY: letter a4 ipad all update help clean clobber FORCE
