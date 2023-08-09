#!/usr/bin/make -f
#
# make -h
# man make
# info make
# /usr/share/doc/make-doc/make.pdf.gz
# file:///usr/share/doc/make-doc/make.html/index.html
#
# http://ctan.org
# http://latex-project.org
# http://wikibooks.org/wiki/LaTeX
# http://wikibooks.org/wiki/LaTeX/Bibliography_Management
# http://wikibooks.org/wiki/LaTeX/Bibliographies_with_biblatex_and_biber
# http://www.ctan.org/tex-archive/info/bibtex/tamethebeast/ttb_en.pdf
# http://mirrors.ctan.org/macros/latex/contrib/biblatex/doc/biblatex.pdf
# http://mirrors.ctan.org/macros/latex/contrib/jurabib/docs/english/jbendoc.pdf
# http://mirrors.ctan.org/macros/latex/contrib/natbib/natbib.pdf
#
# aux	AUXliary file for temporary data
# bcf	Biber Control File
# blg	Bibtex LoG file
# bbl	Bibtex BibLiography
# bbx	Biblatex Bibliography style eXtension?
# bib	BIBliography database file
# bst	Bibliography STyle file
# cbx	Citation style BibteX
# cfg	latex ConFiGuration file
# dvi	DeVice Independent file
# lbx	Language definition file BibteX
# idx	InDeX entrys
# ilg	makeIndex LoG
# lof	List Of Figures
# log	latex LOG file
# pdf	Postscript Document File
# run.xml
# tex	TeX, LaTeX TEXt file
# toc	babel Table Of Content

# Find out what original files you have on directory
texfiles = $(wildcard *.tex)

# Definitions:
DOC = dailytax
SUBM = figures
LATEX = lualatex # latex
#BIBTEX = bibtex # nbibtex, bibtexu aux->bbl
BIBER = biber # bcf->bbl
CLEAN =	lintex && rm -f clean all *.xml
MAKEINDEX = makeindex
#LATEXMK = latexmk

# Clear suffixlist
.SUFFIXES:
# Add suffixrule supported suffix to suffixes list.
.SUFFIXES: .pdf

# Define implicit rule for added suffix:
#%.pdf: %.tex $(texfiles)
#	make -C $(SUBM)
#	$(LATEXMK) $< $@

# Targets:
.PHONY: all
all: $(DOC).pdf

$(DOC).aux $(DOC).bcf $(DOC).idx : $(DOC).tex $(texfiles)
	make -C $(SUBM)
	$(LATEX) $(DOC).tex

#$(DOC).bbl : $(DOC).aux ; $(BIBTEX) $(DOC).aux

$(DOC).bbl : $(DOC).bcf ; $(BIBER) $(DOC).bcf

$(DOC).ind : $(DOC).idx ; $(MAKEINDEX) $(DOC).idx

$(DOC).pdf : $(DOC).bbl $(DOC).ind $(DOC).tex ; $(LATEX) $(DOC).tex

# Clean : Remove temporary files.
.PHONY : clean 
clean :
	mv -f $(DOC).pdf ..
	$(CLEAN)
	make -C $(SUBM) clean

