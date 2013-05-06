#!/bin/bash

# For a folder of files like This_Is_My_Book.pdf This_Is_Also_A_Nice_Title.pdf
for x in `ls *pdf`
	# What this sed script does is takes the filename, removes the .pdf
	# extension, and replaces _ with spaces, giving you a nice title for your
	# PDF
 	do  python ~/src/pdfmangler/pdfmangler.py -f $x -t "`echo $x | sed s/.pdf//g | sed s/_/\ /g`" -a "Scott Cunningham";
done
