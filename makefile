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
# USAGE:	make
#		make distclean
# 		make clean

# Definitions:
SUBM = tex
DOC = dailytax
CLEAN = rm -f $(DOC).pdf clean all
DISTCLEAN = rm -rf clean all ~/.texlive*
PDFFONTS = pdffonts

# Targets:
.PHONY: all
all: $(DOC).pdf

$(DOC).pdf :
	make -C $(SUBM) all && make -C $(SUBM) clean
	echo "With the document bundled fonts:"
	$(PDFFONTS) $(DOC).pdf

# Clean : Remove temporary files.
.PHONY : clean distclean 
clean :
	$(CLEAN) && make -C $(SUBM) clean && rm $(DOC).pdf

distclean :
	$(DISTCLEAN) && make -C $(SUBM) distclean

