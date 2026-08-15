#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Amitava Chakraborty
#Google Translate
#Goslate module
#Apart from translation, it supports
#language detection, batch translation, dictionary lookup and more.

#The goslate module connects with the Google Translate API.
import goslate

text = "Hello World"
gs = goslate.Goslate()
translatedText = gs.translate(text,'fr')

print(translatedText)