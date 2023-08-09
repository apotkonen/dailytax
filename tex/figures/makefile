#!/usr/bin/make -f

# Definitions:
DIA2EPS = dia -t eps
FIG2EPS = fig2dev -L eps
SVG2EPS = inkscape -o
GPL2EPS = gnuplot -c

# Find out what original files you have on directory and
# create needed temporary files for typesetting program.
diafiles = $(wildcard *.dia)
figfiles = $(wildcard *.fig)
svgfiles = $(wildcard *.svg)
gplfiles = $(wildcard *.gpl)
diatoeps = $(patsubst %.dia,%.eps,$(diafiles))
figtoeps = $(patsubst %.fig,%.eps,$(figfiles))
svgtoeps = $(patsubst %.svg,%.eps,$(svgfiles))
gpltoeps = $(patsubst %.gpl,%.eps,$(gplfiles))
epsfiles = $(diatoeps) $(figtoeps) $(svgtoeps) $(gpltoeps)

# Clear suffixlist
.SUFFIXES:
# Add suffixrules supported suffixes to suffixes list.
.SUFFIXES: .dia .fig .svg .gpl

# Define implicit rules for added suffixes:
%.eps: %.dia
	$(DIA2EPS) $<
%.eps: %.fig
	$(FIG2EPS) $< $@
%.eps: %.svg
	$(SVG2EPS) $@ $<
%.eps: %.gpl
	$(GPL2EPS) $<

# Target: Create typesetting program needed input files.
all: $(epsfiles)

# Clean: Remove temporary typesetting program input files.
.PHONY: clean
clean:
	rm -f clean all *.eps *.pdf

