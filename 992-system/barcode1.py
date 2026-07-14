# -*- coding: utf-8 -*-
"""
Created on Mon May 07 14:21:51 2018

@author: ibm

A short script to generate barcodes

Modules Needed
python-barcode: This module is used to create bar codes as SVG objects. 
This python-barcode module which is a fork of the pyBarcode module. 
It provides to create different standard types of barcodes such as 
EAN-8, EAN-13, EAN-14, UPC-A, JAN, ISBN-10, ISBN-13, etc. 
installer : pip install python-barcode

Pillow: required to generate barcodes in image formats (such as png or jpg).
installer: pip install pillow
"""
import barcode
print (barcode.PROVIDED_BARCODES)
ISBN13 = barcode.get_barcode_class('isbn13')
#Now we are going to generate a barcode in the EAN-13 format. 
EAN13 = barcode.get_barcode_class('ean13')
isbn13 = ISBN13('9788995317471')
name = isbn13.save('book1')
print (name)

from barcode.writer import ImageWriter
isbn13 = ISBN13('9788995317471', writer=ImageWriter())
name = isbn13.save('book1')

ean13 = EAN13('00100100463252016', writer=ImageWriter())
name = ean13.save('abc')
print (name)


