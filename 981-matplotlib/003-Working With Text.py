# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Working With Text
"""
"""
Matplotlib has extensive text support, including support for mathematical expressions, 
TrueType support for raster and vector outputs, newline separated text with arbitrary rotations, 
and unicode support. 
Matplotlib includes its own matplotlib.font_manager which implements a cross platform, 
W3C compliant font finding algorithm.

The user has a great deal of control over text properties 
(font size, font weight, text location and color, etc.). 
Matplotlib implements a large number of TeX math symbols and commands.

The following list of commands are used to create text in the Pyplot interface −
text 	    Add text at an arbitrary location of the Axes.
annotate 	Add an annotation, with an optional arrow, at an arbitrary location of theAxes.
xlabel 	    Add a label to the Axes’s x-axis.
ylabel 	    Add a label to the Axes’s y-axis.
title 	    Add a title to the Axes.
figtext 	Add text at an arbitrary location of the Figure.
suptitle 	Add a title to the Figure.

All of these functions create and return a matplotlib.text.Text() instance.
"""
#Following scripts demonstrate the use of some of the above functions −
import matplotlib.pyplot as plt
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.set_title('axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
ax.text(3, 8, 'boxed italics text in data coords', style='italic', 
bbox = {'facecolor': 'red'})
ax.text(2, 6, r'an equation: $E = mc^2$', fontsize = 15)
ax.text(4, 0.05, 'colored text in axes coords',
verticalalignment = 'bottom', color = 'green', fontsize = 15)
ax.plot([2], [1], 'o')
ax.annotate('annotate', xy = (2, 1), xytext = (3, 4),
arrowprops = dict(facecolor = 'black', shrink = 0.05))
ax.axis([0, 10, 0, 10])
plt.show()