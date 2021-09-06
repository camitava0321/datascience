# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:49:10 2019

@author: AMITAVACHAKRABORTY
"""

from PyPDF2 import PdfFileReader
pdf = PdfFileReader(open('abc.pdf','rb'))
pdf.getNumPages()