#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Amitava Chakraborty
#Extract text from image - with image processing.
#Optical Character Recognition (OCR).
#A popular OCR engine is named tesseract.
import os
import tempfile
import subprocess

def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r') as handle:
        contents = handle.read()

    os.remove(temp.name + '.txt')
    os.remove(temp.name)

    return contents

str = ocr('wordle.jpg')
print(str)

#Besides calling the OCR engine directly, one can use one of these modules:
#    pytesseract
#    pyocr
#    tesserwrap
#    pytesser
#They all use the same OCR engine beneath: tesseract.