# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - Figure and Axes Class
"""
"""
matplotlib.figure module contains the Figure class. 
It is a top-level container for all plot elements. 

Following are the additional parameters −
Figsize 	(width,height) tuple in inches
Dpi 	    Dots per inches
Facecolor 	Figure patch facecolor
Edgecolor 	Figure patch edge color
Linewidth 	Edge line width

Matplotlib - Axes Class
Axes object is the region of the image with the data space. 
A given figure can contain many Axes, but a given Axes object can only be in one Figure. 
The Axes contains two (or three in the case of 3D) Axis objects. 
The Axes class and its member functions are the primary entry point to working with the OO interface.

"""
import matplotlib.pyplot as plt
#Data Points
#advertisement expenses and sales figures of TV and smartphone in the form of line plots. 
#Line representing TV is a solid line with yellow colour and square markers whereas 
#smartphone line is a dashed line with green colour and circle marker.
y = [1, 4, 9, 16, 25,36,49, 64]
x_TV = [1, 16, 30, 42,55, 68, 77,88]
x_Smartphone = [1,6,12,18,28, 40, 52, 65]

#The Figure object is instantiated by calling the figure() function from the pyplot module −
fig = plt.figure()


#Axes object is added to figure by calling the add_axes() method. 
#It returns the axes object and adds an axes at position rect [left, bottom, width, height] 
#where all quantities are in fractions of figure width and height.
#Following is the parameter for the Axes class −
#rect − A 4-length sequence of [left, bottom, width, height] quantities.
ax=fig.add_axes([0,0,1,1])
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('Product')
ax.set_ylabel('Sales')

#The following member functions of axes class add different elements to plot −

#Legend
#The legend() method of axes class adds a legend to the plot figure. It takes three parameters −
ax.legend(labels = ('TV', 'Smartphone'), loc = 'lower right') # legend placed at lower right

"""
ax.legend(handles, labels, loc)

Where labels is a sequence of strings and handles a sequence of Line2D or Patch instances. 
loc can be a string or an integer specifying the legend location.
Location string 	Location code
Best 	0
upper right 	1
upper left 	2
lower left 	3
lower right 	4
Right 	5
Center left 	6
Center right 	7
lower center 	8
upper center 	9
Center 	10
"""

"""
axes.plot()

This is the basic method of axes class that plots values of one array versus another as lines or markers. 
The plot() method can have an optional format string argument to specify color, style and size of line and marker.
Color codes
Character 	Color
‘b’ 	Blue
‘g’ 	Green
‘r’ 	Red
‘b’ 	Blue
‘c’ 	Cyan
‘m’ 	Magenta
‘y’ 	Yellow
‘k’ 	Black
‘b’ 	Blue
‘w’ 	White
Marker codes
Character 	Description
‘.’ 	Point marker
‘o’ 	Circle marker
‘x’ 	X marker
‘D’ 	Diamond marker
‘H’ 	Hexagon marker
‘s’ 	Square marker
‘+’ 	Plus marker
Line styles
Character 	Description
‘-‘ 	Solid line
‘—‘ 	Dashed line
‘-.’ 	Dash-dot line
‘:’ 	Dotted line
‘H’ 	Hexagon marker
"""
l1 = ax.plot(x_TV,y,'ys-') # solid line with yellow colour and square marker
l2 = ax.plot(x_Smartphone,y,'go--') # dash line with green colour and circle marker
plt.show()


#%% - Matplotlib - Formatting Axes
#Sometimes, one or a few points are much larger than the bulk of data. 
#In such a case, the scale of an axis needs to be set as logarithmic rather than the normal scale. 
#In Matplotlib, it is possible by setting xscale or vscale property of axes object to ‘log’.

#It is also required sometimes to show some additional distance between axis numbers and axis label. 
#The labelpad property of either axis (x or y or both) can be set to the desired value.

#Both the above features are demonstrated with the help of the following example. 

import numpy as np
fig, axes = plt.subplots(1, 2, figsize=(10,4))
x = np.arange(1,5)

#The subplot on the left has its x axis having label at more distance.
axes[0].plot( x, np.exp(x))
axes[0].plot(x,x**2)
axes[0].set_title("Normal scale")
axes[0].set_xlabel("x axis")
axes[0].set_ylabel("y axis")
axes[0].xaxis.labelpad = 10

#The subplot on the right has a logarithmic scale
axes[1].plot (x, np.exp(x))
axes[1].plot(x, x**2)
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")
axes[1].set_xlabel("x axis")
axes[1].set_ylabel("y axis")
plt.show()

#%% - Formatting Axes
#Axis spines are the lines connecting axis tick marks demarcating boundaries of plot area. 
#The axes object has spines located at top, bottom, left and right.

#Each spine can be formatted by specifying color and width. 
#Any edge can be made invisible if its color is set to none.

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.plot([1,2,3,4,5])
plt.show()

#%% - Matplotlib - Setting Limits
#Matplotlib automatically arrives at the minimum and maximum values of variables to be displayed along x, y 
#(and z axis in case of 3D plot) axes of a plot. 
#However, it is possible to set the limits explicitly by using set_xlim() and set_ylim() functions.

#In the following plot, the autoscaled limits of x and y axes are shown −
fig = plt.figure()
a1 = fig.add_axes([0,0,1,1])
x = np.arange(1,10)
a1.plot(x, np.exp(x))
a1.set_title('exp')
plt.show()

#%% - Setting Limits
#Now we format the limits on x axis to (0 to 10) and y axis (0 to 10000) −

fig = plt.figure()
a1 = fig.add_axes([0,0,1,1])

x = np.arange(1,10)
a1.plot(x, np.exp(x),'r')
a1.set_title('exp - custom limits')
a1.set_ylim(0,10000)
a1.set_xlim(0,10)
plt.show()

#%% - Matplotlib - Setting Ticks and Tick Labels
#Ticks are the markers denoting data points on axes. Matplotlib has so far - in all our previous examples - 
#automatically taken over the task of spacing points on the axis.
#Matplotlib's default tick locators and formatters are designed to be generally sufficient in many common situations. 
#Position and labels of ticks can be explicitly mentioned to suit specific requirements.

#The xticks() and yticks() function takes a list object as argument. 
#The elements in the list denote the positions on corresponding action where ticks will be displayed.
#e.g., ax.set_xticks([2,4,6,8,10])
#This method will mark the data points at the given positions with ticks.

#Similarly, labels corresponding to tick marks can be set by set_xlabels() and set_ylabels() functions respectively.
#e.g., ax.set_xlabels([‘two’, ‘four’,’six’, ‘eight’, ‘ten’])
#This will display the text labels below the markers on the x axis.

#Following example demonstrates the use of ticks and labels.
import math
x = np.arange(0, math.pi*2, 0.05)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
y = np.sin(x)
ax.plot(x, y)
ax.set_xlabel('angle')
ax.set_title('sine')
ax.set_xticks([0,2,4,6])
ax.set_xticklabels(['zero','two','four','six'])
ax.set_yticks([-1,0,1])
plt.show()