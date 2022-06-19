# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Working with Images
"""
"""
The image module in Matplotlib package provides functionalities required for loading, rescaling and displaying image.
Loading image data is supported by the Pillow library. 
Natively, Matplotlib only supports PNG images. The commands shown below fall back on Pillow if the native read fails.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#The image used in this example is a PNG file, 
#but keep that Pillow requirement in mind for your own data. 
#The imread() function is used to read image data in an ndarray object of float32 dtype.

#Assuming that following image named as mtplogo.png is present in the current working directory.
img = mpimg.imread('boichitra.png')

#Any array containing image data can be saved to a disk file by executing the imsave() function. 
#Here a vertically flipped version of the original png file is saved by giving origin parameter as lower.
plt.imsave("boichitra-flipped.png", img, cmap = 'gray', origin = 'lower')

#The new image appears as below if opened in any image viewer.

#Image Viewer
#To draw the image on Matplotlib viewer, execute the imshow() function.
imgplot = plt.imshow(img)