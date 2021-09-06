# -*- coding: utf-8 -*-
"""
Created on Mon May 07 14:21:51 2018

@author: ibm
"""

import barcode
print (barcode.PROVIDED_BARCODES)
ISBN13 = barcode.get_barcode_class('isbn13')
EAN13 = barcode.get_barcode_class('ean13')
isbn13 = ISBN13('9788995317471')
name = isbn13.save('book1')
print (name)

from barcode.writer import ImageWriter
isbn13 = ISBN13('9788995317471', writer=ImageWriter())
name = isbn13.save('book1')

ean13 = EAN13('auth:name:en:325:2016', writer=ImageWriter())
name = ean13.save('abc')
print (name)


