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
# http://wikipedia.org/wiki/Comparison_of_graphics_file_formats
# http://wikipedia.org/wiki/List_of_file_formats#Font_file
# http://ftp.math.utah.edu/pub/tex/doc/luamult.pdf
# http://wikipedia.org/wiki/PostScript_fonts
# http://wikipedia.org/wiki/Linux_Libertine
# http://wikipedia.org/wiki/GNU_FreeFont
# http://wikipedia.org/wiki/Unicode_font # This include license information
# http://wikipedia.org/wiki/GNU_Unifont
# http://wikipedia.org/wiki/Noto_fonts
# http://wikipedia.org/wiki/Typeface
# http://wikipedia.org/wiki/Unicode
# http://wikipedia.org/wiki/UTF-8
# http://wikipedia.org/wiki/List_of_CJK_fonts # Include license information
# http://wikipedia.org/wiki/List_of_typefaces
# http://wikipedia.org/wiki/Open-source_Unicode_typefaces # License information
# http://tex.stackexchange.com/questions/7770/file-extensions-related-to-latex-etc
# https://tug.org/FontCatalogue/mathfonts.html # Fonts with math support
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
# ind	Index file
# lof	List Of Figures
# log	latex LOG file
# out	Bookmark file
# pdf	Postscript Document File
# run.xml logreq request file /usr/share/doc/texlive-doc/latex/logreq/README
# tex	TeX, LaTeX TEXt file
# toc	babel Table Of Content

# FontForge (fontforge) etc.
# abf   Adobe Binary screen Font
# afm   Adobe Font Metrics (afm2afm, afm2tfm)
# base	? TeX/Metafont/MetaPost file
# bdf   Bitmap Distribution Format
# bmf   ByteMap Font
# bin   Mac resource font
# brfnt Binary Revolution Font Format
# cff	Compact Font Format container
# cfg   ConFiGuration ? (hbf2gf)
# cid   Collection/Character IDentifier - postscipt font
# cjk   Chinese Japanese Korean bitmap font
# dfont Mac resource font
# fond	FONt Description resource Mac 
# eps   Encapsulated PostScript
# fmt	Font MeTric
# fon   bitmepped FONt
# fontspec	
# gf    Generic Font (hbf2gf)
# hbf   Hanzi Bitmap Font/File (hbf2gf)
# hqx   Mac resource font
# mem	? tex/MEtafont/MEtapost Metrics? file
# mf    MetaFont (mktexmf)
# mgf   MicroGrafx Font
# ocp	Omega Compiled Process file
# ofm	Omega Font Metric
# otb	Open Type Bitmap font
# otc	Open Type Collection
# otf   Open Type Font (fontforge) http://wikipedia.org/wiki/OpenType
# pcf   Portable Compiled Font/Format (X11) bitmap 
# pfa   Printer Font Ascii adobe type 1
# pfb   Printer Font Binary adobe type 1
# pfm   Printer Font Metrics adobe type 1
# pgf	Portable Graphics Format
# pk    PacKed tex bitmap font (mktexpk, ttf2pk)
# pl    Property List (afm2pl)
# ps    PostScript
# pst	PostScript Trik macro file
# sfd   Spline Font Database (fontforge)
# snf   Server Normal Font
# svg   Scaled Vector Graphics
# t1	adobe postscript font Type 1 http://wikipedia.org/wiki/PostScript_fonts#Type_1
# tdf	TheDraw Font
# tfm   Tex Font Metrics (mktextfm, afm2tfm)
# ttf   True Type Font (ttf2pk) http://wikipedia.org/wiki/TrueType
# ttc   True Type Collection http://wikipedia.org/wiki/TrueType
# ufo	Unified Font Object
# woff	Web Open Font Format
#
# Serching and using fonts:
# fc-list
# kpsewhich --help-formats --show-path=FMT
# info dvips
#   -bitmapfontenc strict
#   -j*  Download fonts partially
#   -V*  Send downloadable PS fonts as PK
#   -d32
# more /etc/texmf/web2c/texmf.cnf
# update-texmf
# Find out what original files you have on directory
texfiles = $(wildcard *.tex)

# Definitions:
DOC = dailytax
SUBM = figures
#LATEX = latex
#LATEX = xelatex
LATEX = lualatex
#LATEX = lualatex -output-format=dvi
#DVIPS = dvips -d-1 -bitmapfontenc strict -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -o
#/usr/share/texlive/texmf-dist
#/usr/share/texlive/texmf-dist/fonts/TYPE/MODE/SUPPLIER/TYPEFACE/dpiNNN
# ls -la ~/texmf ~/.texlive*
# info kpathsea
# man fmtutil.cnf
# man update-texmf
# man luaotfload-tool
#/etc/texmf/web2c/texmf.cnf
#/etc/texmf/web2c/mktex.cnf
#/usr/share/texmf/web2c/texmf.cnf
#/usr/share/texmf/web2c/fmtutil.cnf
#/usr/share/texlive/texmf-dist/web2c/texmf.cnf
#/usr/share/texlive/texmf-dist/web2c/fmtutil.cnf
#updmap -sys || updmap -user
#/var/lib/texmf/fonts/map/dvips/updmap/psfonts.map
#/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map
#https://library.psfc.mit.edu/publishing/fonts_epub/tex.html
#DVIPS = dvips -d32 -sDEVICE=pdfwrite -o
#DVIPS = dvips -d32 -bitmapfontenc strict -sDEVICE=pdfwrite -o
#PS2PDF = gs -q -P- -dSAFER -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -sstdout=%stderr -sOutputFile=
#PS2PDF = gs -q -dSAFER -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -sstdout=%stderr -sOutputFile=

BIBTEX = bibtex # nbibtex, bibtexu aux->bbl
BIBER = biber # bcf->bbl
CLEAN =	lintex -o -k && rm -f clean all *.xml
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

#$(DOC).dvi : $(DOC).bbl $(DOC).ind $(DOC).tex ; $(LATEX) $(DOC).tex

#$(DOC).ps : $(DOC).dvi ; $(DVIPS) $(DOC).ps $(DOC).dvi

#$(DOC).pdf : $(DOC).ps ; $(PS2PDF)$(DOC).pdf $(DOC).ps

# Clean : Remove temporary files.
.PHONY : clean 
clean :
	touch $(DOC).pdf
	mv -f $(DOC).pdf ..
	$(CLEAN)
	make -C $(SUBM) clean


