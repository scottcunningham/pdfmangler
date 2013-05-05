#!/usr/bin/env python

import sys
import argparse
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict
from pyPdf import PdfFileReader

parser = argparse.ArgumentParser(description='A tool to alter PDF metadata.')

parser.add_argument("-f", "--filename", help="The PDF file to open")
parser.add_argument("-a", "--author", help="The 'author' tag to be written to the file")
parser.add_argument("-t", "--title", help="The 'title' tag to be written to the file")

args = parser.parse_args()

if args.filename is "":
	print "a"
	sys.exit(-1)

filename = args.filename

info = PdfFileReader(file(filename)).getDocumentInfo()

if args.author is "": 
	author = info.author
else:
	author = args.author

if args.title is "":
	title = info.title
else:
	title = args.title

writer = PdfWriter()
writer.addpages(PdfReader(filename).pages)

writer.trailer.Info = IndirectPdfDict(
    Title = args.title,
    Author = args.author,
)
writer.write(filename)
