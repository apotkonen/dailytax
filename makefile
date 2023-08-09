#!/usr/bin/make -f
#
# make -h
# man make
# info make
# /usr/share/doc/make-doc/make.pdf.gz
# file:///usr/share/doc/make-doc/make.html/index.html
#
# pdf	Postscript Document File
#
# USAGE: make
#

# Definitions:
SUBM = tex
DOC = dailytax
CLEAN = rm -f $(DOC).pdf clean all

# Targets:
.PHONY: all
all: $(DOC).pdf

$(DOC).pdf :
	make -C $(SUBM) all
	make -C $(SUBM) clean

# Clean : Remove temporary files.
.PHONY : clean 
clean :
	$(CLEAN)

