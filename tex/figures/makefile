#!/usr/bin/make -f

# Definitions:
CAT = cat
DIA2EPS = dia -t eps
#https://gitlab.com/zachrwolfe/inkscape/-/commit/903303ef96e80dc97bb905f409276e348265c972
#EPS2SVG = inkscape --without-gui --batch-process -D -l -o
EPS2SVG = inkscape --batch-process -D -l -o
FIG2EPS = fig2dev -L eps
FIG2SVG = fig2dev -L svg
#Default->Times, Times Roman->Times, SansSerif->AvantGarde
#FONT2FO = sed -e 's/Times/Noto/g'
FONT2FO = sed -e 's/Times/FreeSerif/g'
#FONT2FO = sed -e 's/Times/LinLibertineO/g'
#FONT2FO = sed -e 's/Times/LinLibertineO/g' | sed -e 's/Helvetica/LinLibertineO/g'
#FONT2FO = sed -e 's/Helvetica/LinLibertineO/g'
SVG2EPS = inkscape -o
GPL2EPS = gnuplot -c
EPS2PDF = epstopdf
PDFFONT = pdffonts

# Find out what original files you have on directory and
# create needed temporary files for typesetting program.
diafiles = $(wildcard *.dia)
figfiles = $(wildcard *.fig)
svgfiles = $(wildcard *.svg)
gplfiles = $(wildcard *.gpl)
diatoeps = $(patsubst %.dia,%.eps,$(diafiles))
figtoeps = $(patsubst %.fig,%.eps,$(figfiles))
figtosvg = $(patsubst %.fig,%.svg,$(figfiles))
svgtoeps = $(patsubst %.svg,%.eps,$(svgfiles))
gpltoeps = $(patsubst %.gpl,%.eps,$(gplfiles))
epsfiles = $(diatoeps) $(figtoeps) $(svgtoeps) $(gpltoeps)
pdffiles = $(patsubst %.eps,%.pdf,$(epsfiles))
epstosvg = basecofi.eps evensufi.eps soctaxfi.eps

# Clear suffixlist
.SUFFIXES:
# Add suffixrules supported suffixes to suffixes list.
.SUFFIXES: .dia .fig .svg .gpl

# Define implicit rules for added suffixes:
%.eps: %.dia
	$(DIA2EPS) $<
%.svg: %.fig
	$(FIG2SVG) $< | $(FONT2FO) > $@
#	$(FIG2SVG) $< $@
%.eps: %.svg
	$(SVG2EPS) $@ $<
%.eps: %.gpl
	$(GPL2EPS) $<
#%.eps: %.fig
#	$(FIG2EPS) $< $@
#	$(FIG2EPS) $< | $(FONT2FO) > $@
%.pdf: %.eps
	$(EPS2PDF) $< $@
#	$(PDFFONT) $@
#	$(CAT) $< | $(EPS2PDF) -f | $(PDFFONT) -

# Targets to control immediate files processing
#IMMEDIATE: $(figtosvg)
#NOTIMMEDIATE: $(figtosvg)
#NOTIMMEDIATE: verotus.svg
#	ls -la $(figtosvg)
pdf: $(pdffiles)
	find . -type f -name "*.pdf" -print -exec pdffonts {} \;

# Target: Create typesetting program needed input files, and convert selected.
all: $(epsfiles)
	$(EPS2SVG) basecofi.svg basecofi.eps
	$(EPS2SVG) evensufi.svg evensufi.eps
	$(EPS2SVG) soctaxfi.svg soctaxfi.eps

# Clean: Remove temporary typesetting program input files.
.PHONY: clean
clean:
	rm -f clean all *.eps *.pdf
	rm -f $(figtosvg)
#	rm -f $(epstosvg) verotus.svg

