#!/usr/bin/env python3

import sys
from pdf2docx import Converter

filename = input('What is the full path of the PDF file to convert? ')
pdf_file = filename
docx_file = filename + '_converted.docx'

# Check filename
if filename == "":
    print("The path can't be empty")
    sys.exit()

# convert pdf to docx
try:
    cv = Converter(pdf_file)
    cv.convert(docx_file) 
    cv.close()
except:
    print("File not found")
