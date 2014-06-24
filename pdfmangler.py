#!/usr/bin/env python

import sys
import argparse
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict, errors
from pyPdf import PdfFileReader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A tool to alter PDF metadata.')

    parser.add_argument("-f", "--filename", help="The PDF file to open",
                        required=True)
    parser.add_argument("-a", "--author",
                        help="The 'author' tag to be written to the file")
    parser.add_argument("-t", "--title",
                        help="The 'title' tag to be written to the file")

    args = parser.parse_args()

    if args.filename is "":
        print "No filename supplied, bailing out."
        sys.exit(-1)

    info = PdfFileReader(file(args.filename)).getDocumentInfo()

    if args.author is "":
        author = info.author
    else:
        author = args.author

    if args.title is "":
        title = info.title
    else:
        title = args.title

    try:
        writer = PdfWriter()
        writer.addpages(PdfReader(args.filename).pages)

        writer.trailer.Info = IndirectPdfDict(Title=args.title,
                                              Author=args.author)
        writer.write(filename)
    except errors.PdfParseError as error:
        print "Error parsing input file", args.filename
        print "Error message was:", error.msg
        sys.exit(-1)

    sys.exit(0)
