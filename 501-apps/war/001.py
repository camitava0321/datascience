# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2018
@author: Amitava
IO Tools
"""
#read.csv
import pandas as pd
import numpy as np
df=pd.read_csv("War_Battles.csv")
print(df)

#custom index
#This specifies a column in the csv file to customize the index using index_col.
df=pd.read_csv("War_Battles.csv", index_col=['Name'])
print (df)

#Converters
#dtype of the columns can be passed as a dict.
df=pd.read_csv("War_Battles.csv", index_col=['Name'], dtype={'Deaths': np.float64})
print (df.dtypes)
print (df.columns)
#By default, the dtype of the Salary column is int, but the result shows it as float because we have explicitly casted the type.


import matplotlib.pyplot as plt

#%% - plot one column versus another using the x and y keywords in plot():
df.plot(x='Start', y='Deaths')
df.plot.bar(x='Start', y='Deaths')
df.plot.scatter(x='Start', y='Deaths')

#%% - For pie plots it’s best to use square figures, i.e. a figure aspect ratio 1. 
#You can create the figure with equal width and height, or 
#force the aspect ratio to be equal after plotting by calling ax.set_aspect('equal') on the returned axes object.
#Note that pie plot with DataFrame requires that you either specify a target column 
#by the y argument or subplots=True. 
#When y is specified, pie plot of selected column will be drawn. 
#If subplots=True is specified, pie plots for each column are drawn as subplots. 
#A legend will be drawn in each pie plots by default; specify legend=False to hide it.

#SELECT
#In SQL, selection is done using a comma-separated list of columns that you select (or a * to select all columns) −
#SELECT total_bill, tip, smoker, time
#FROM tips
#LIMIT 5;

#With Pandas, column selection is done by passing a list of column names to your DataFrame −
df2 = df[['Deaths', 'WAR']]
print (df2.head())

#GroupBy
#SELECT sex, count(*) FROM tips GROUP BY sex;
#The Pandas equivalent would be −
df2 = df.groupby('WAR').sum()

df2.plot.pie(x='WAR', y='Deaths', figsize=(12,12))
#%% - A bar plot

#One can also create other plots using the methods DataFrame.plot.<kind> 
#instead of providing the kind keyword argument. 
#This makes it easier to discover plot methods and the specific arguments they use:

"""
df.plot.<TAB>
df.plot.area     df.plot.barh     df.plot.density  df.plot.hist     df.plot.line     df.plot.scatter
df.plot.bar      df.plot.box      df.plot.hexbin   df.plot.kde      df.plot.pie
In addition to these kind s, there are the DataFrame.hist(), and 
DataFrame.boxplot() methods, which use a separate interface.

Other Plots
Plotting methods allow for a handful of plot styles other than the default line plot. 
These methods can be provided as the kind keyword argument to plot(), and include:

‘bar’ or ‘barh’ for bar plots
‘hist’ for histogram
‘box’ for boxplot
‘kde’ or ‘density’ for density plots
‘area’ for area plots
‘scatter’ for scatter plots
‘hexbin’ for hexagonal bin plots
‘pie’ for pie plots
"""
#%% - 
"""
Several plotting functions in pandas.plotting that take a Series or DataFrame as an argument. 
These include:

Scatter Matrix
Andrews Curves
Parallel Coordinates
Lag Plot
Autocorrelation Plot
Bootstrap Plot
RadViz

Plots may also be adorned with errorbars or tables.
"""

#%% - Histograms - can be drawn by using the DataFrame.plot.hist() and Series.plot.hist() methods.
df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
plt.figure();
df4.plot.hist(alpha=0.5)

#%% - A histogram can be stacked using stacked=True. Bin size can be changed using the bins keyword.
plt.figure()
df4.plot.hist(stacked=True, bins=20)

#%% - One can pass other keywords supported by matplotlib hist. 
#For example, horizontal and cumulative histograms can be drawn by orientation='horizontal' and cumulative=True.
plt.figure();
df4['a'].plot.hist(orientation='horizontal', cumulative=True)

#%% - The existing interface DataFrame.hist to plot histogram still can be used.
plt.figure();
df['A'].diff().hist()

#%% - DataFrame.hist() plots the histograms of the columns on multiple subplots:
plt.figure()
df.diff().hist(color='k', alpha=0.5, bins=50)

#%% - The by keyword can be specified to plot grouped histograms:
data = pd.Series(np.random.randn(1000))
data.hist(by=np.random.randint(0, 4, 1000), figsize=(6, 4))

#%% - To plot multiple column groups in a single axes, 
#repeat plot method specifying target ax. 
#It is recommended to specify color and label keywords to distinguish each groups.
ax = df.plot.scatter(x='a', y='b', color='DarkBlue', label='Group 1');
df.plot.scatter(x='c', y='d', color='DarkGreen', label='Group 2', ax=ax);

#The keyword c may be given as the name of a column to provide colors for each point:
df.plot.scatter(x='a', y='b', c='c', s=50);

#You can pass other keywords supported by matplotlib scatter. 
#The example below shows a bubble chart using a column of the DataFrame as the bubble size.
df.plot.scatter(x='a', y='b', s=df['c']*200);


#%% - Plotting with Missing Data
#Pandas tries to be pragmatic about plotting DataFrames or Series that contain missing data. Missing values are dropped, left out, or filled depending on the plot type.
"""
Plot Type          NaN Handling
Line	            Leave gaps at NaNs
Line (stacked)    Fill 0’s
Bar	               Fill 0’s
Scatter	         Drop NaNs
Histogram	        Drop NaNs (column-wise)
Box	               Drop NaNs (column-wise)
Area	            Fill 0’s
KDE	               Drop NaNs (column-wise)
Hexbin	           Drop NaNs
Pie	              Fill 0’s
If any of these defaults are not what you want, or 
if you want to be explicit about how missing values are handled, consider using fillna() or dropna() before plotting.
"""
#%% - Plotting on a Secondary Y-axis
#To plot data on a secondary y-axis, use the secondary_y keyword:
df.Deaths.plot()
df.Start.plot(secondary_y=True, style='g')

#%% - To plot some columns in a DataFrame, give the column names to the secondary_y keyword:
plt.figure()
ax = df.plot(secondary_y=['A', 'B'])
ax.set_ylabel('CD scale')

ax.right_ax.set_ylabel('AB scale')

#Note that the columns plotted on the secondary y-axis is automatically marked with “(right)” in the legend. To turn off the automatic marking, use the mark_right=False keyword:
plt.figure()
df.plot(secondary_y=['A', 'B'], mark_right=False)

#%% - Subplots - Each Series in a DataFrame can be plotted on a different axis with the subplots keyword:
df.plot(subplots=True, figsize=(6, 6));

#Using Layout and Targeting Multiple Axes
#The layout of subplots can be specified by the layout keyword. 
#It can accept (rows, columns). The layout keyword can be used in hist and boxplot also. 
#If the input is invalid, a ValueError will be raised.

#The number of axes which can be contained by rows x columns specified by layout 
#must be larger than the number of required subplots. If layout can contain more axes than required, blank axes are not drawn. Similar to a NumPy array’s reshape method, you can use -1 for one dimension to automatically calculate the number of rows or columns needed, given the other.
df.plot(subplots=True, layout=(2, 3), figsize=(6, 6), sharex=False);

#The above example is identical to using:
df.plot(subplots=True, layout=(2, -1), figsize=(6, 6), sharex=False);
#The required number of columns (3) is inferred from the number of series to plot and the given number of rows (2).

#%% - Plotting Tables 
#Plotting with matplotlib table is now supported in DataFrame.plot() and Series.plot() with a table keyword. 
#The table keyword can accept bool, DataFrame or Series. 
#The simple way to draw a table is to specify table=True. 
#Data will be transposed to meet matplotlib’s default layout.
fig, ax = plt.subplots(1, 1)
df = pd.DataFrame(np.random.rand(5, 3), columns=['a', 'b', 'c'])
ax.get_xaxis().set_visible(False)   # Hide Ticks
df.plot(table=True, ax=ax)

#One can also a different DataFrame or Series to the table keyword. 
#The data will be drawn as displayed in print method (not transposed automatically). 
#If required, it should be transposed manually as seen in the example below.
fig, ax = plt.subplots(1, 1)
ax.get_xaxis().set_visible(False)   # Hide Ticks
df.plot(table=np.round(df.T, 2), ax=ax)

#There also exists a helper function pandas.plotting.table, 
#which creates a table from DataFrame or Series, and adds it to an matplotlib.Axes instance. 
#This function can accept keywords which the matplotlib table has.
from pandas.plotting import table
fig, ax = plt.subplots(1, 1)
table(ax, np.round(df.describe(), 2), loc='upper right', colWidths=[0.2, 0.2, 0.2])

df.plot(ax=ax, ylim=(0, 2), legend=None)

#Note: You can get table instances on the axes using axes.tables property for further decorations. 

