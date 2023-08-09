#!/usr/bin/bash
# This script is used to convert archimate-view-svg-export to black and white.
# Script is hand tailored to one use case. You may need to tailor it.
# USAGE: ./archi2bw.sh archi_export_file.svg
ex $1 -c "%s/white/none/g"\
 -c "%s/rgb(255,255,181)/none/g"\
 -c "%s/rgb(178,178,178)/black/g"\
 -c "%s/rgb(178,178,126)/black/g"\
 -c "w"\
 -c "q"
