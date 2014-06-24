#!/usr/bin/env python

import sys
import argparse
from pyPdf import PdfFileReader

parser = argparse.ArgumentParser(description='A tool to alter PDF metadata.')

filename = sys.argv[1]

if filename is "":
    print "No filename specified."
    sys.exit(-1)

info = PdfFileReader(file(filename)).getDocumentInfo()

print "Author:", info.author
print "Title:", info.title
