# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:57:09 2018

@author: Amitava Chakraborty
Matplotlib - 3D Surface plot
"""
"""
Bokeh is a data visualization library for Python. Unlike Matplotlib and Seaborn, they are also Python packages for data visualization, Bokeh renders its plots using HTML and JavaScript. Hence, it proves to be extremely useful for developing web based dashboards.

The Bokeh project is sponsored by NumFocus https://numfocus.org/. NumFocus also supports PyData, an educational program, involved in development of other important tools such as NumPy, Pandas and more. Bokeh can easily connect with these tools and produce interactive plots, dashboards and data applications.
Features

Bokeh primarily converts the data source into a JSON file which is used as input for BokehJS, a JavaScript library, which in turn is written in TypeScript and renders the visualizations in modern browsers.

Some of the important features of Bokeh are as follows −
Flexibility

Bokeh is useful for common plotting requirements as well as custom and complex use-cases.
Productivity

Bokeh can easily interact with other popular Pydata tools such as Pandas and Jupyter notebook.
Interactivity

This is an important advantage of Bokeh over Matplotlib and Seaborn, both produce static plots. Bokeh creates interactive plots that change when the user interacts with them. You can give your audience a wide range of options and tools for inferring and looking at data from various angles so that user can perform “what if” analysis.
Powerful

By adding custom JavaScript, it is possible to generate visualizations for specialised use-cases.
Sharable

Plots can be embedded in output of Flask or Django enabled web applications. They can also be rendered in

Jupyter
notebooks.

Open source

Bokeh is an open source project. It is distributed under Berkeley Source Distribution (BSD) license. Its source code is available on https://github.com/bokeh/bokeh.
"""
#Creating a simple line plot between two numpy arrays is very simple. 
#To begin with, import following functions from bokeh.plotting modules −
from bokeh.plotting import figure, output_file, show

#The figure() function creates a new figure for plotting.
#The output_file() function is used to specify a HTML file to store output.
#The show() function displays the Bokeh figure in browser on in notebook.

#Next, set up two numpy arrays where second array is sine value of first.

import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

#To obtain a Bokeh Figure object, specify the title and x and y axis labels as below −
p = figure(title = "sine wave example", x_axis_label = 'x', y_axis_label = 'y')

#The Figure object contains a line() method that adds a line glyph to the figure. It needs data series for x and y axes.
p.line(x, y, legend = "sine", line_width = 2)

#Finally, set the output file and call show() function.
output_file("001-getting started.html")
show(p)
