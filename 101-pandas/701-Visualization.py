# -*- coding: utf-8 -*-
"""
Created on Mar 13 01:08:05 2017
@author: Amitava
"""
"""
Visualization with pandas
"""
#%% - imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% - descriptive statistics and other related operations on DataFrame
"""
#All calls to np.random are seeded with 123456.
"""
#%% - Basic Plotting: plot
#The plot method on Series and DataFrame is a simple wrapper around plt.plot():
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
#If the index consists of dates, it calls gcf().autofmt_xdate() to try to format the x-axis

#%% - On DataFrame
#plot() is a convenience to plot all of the columns with labels:
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure() 
df.plot()


#%% - plot one column versus another using the x and y keywords in plot():
df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
df3['A'] = pd.Series(list(range(len(df))))
df3.plot(x='A', y='B')

#%% - A bar plot

plt.figure()
df.iloc[5].plot(kind='bar')
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
#%% - Bar plots, For labeled, non-time series data
plt.figure()
df.iloc[5].plot.bar()
plt.axhline(0, color='k')


#%% - Calling a DataFrame’s plot.bar() method produces a multiple bar plot:
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar();

#%% - To produce a stacked bar plot, pass stacked=True:
df2.plot.bar(stacked=True);

#%% - To get horizontal bar plots, use the barh method:
df2.plot.barh(stacked=True);

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

#%% - Box Plots can be drawn calling Series.plot.box() and DataFrame.plot.box(), 
#or DataFrame.boxplot() to visualize the distribution of values within each column.

#A boxplot representing five trials of 10 observations of a uniform random variable on [0,1).
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()

#%% - Boxplot can be colorized by passing color keyword. 
#One can pass a dict whose keys are boxes, whiskers, medians and caps. 
#If some keys are missing in the dict, default colors are used for the corresponding artists. 
#Also, boxplot has sym keyword to specify fliers style.

#When you pass other type of arguments via color keyword, 
#it will be directly passed to matplotlib for all the boxes, whiskers, medians and caps colorization.

#The colors are applied to every boxes to be drawn. 
#If you want more complicated colorization, you can get each drawn artists by passing return_type.
color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
df.plot.box(color=color, sym='r+')

#%% - One can also pass other keywords supported by matplotlib boxplot. 
#For example, horizontal and custom-positioned boxplot can be drawn by vert=False and positions keywords.
df.plot.box(vert=False, positions=[1, 4, 5, 6, 8])

#%% - The existing interface DataFrame.boxplot to plot boxplot still can be used.
df = pd.DataFrame(np.random.rand(10,5))
plt.figure();
bp = df.boxplot()

#%% - One can create a stratified boxplot using the by keyword argument to create groupings. For instance,
df = pd.DataFrame(np.random.rand(10,2), columns=['Col1', 'Col2'] )
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B'])
plt.figure();
bp = df.boxplot(by='X')

#%% - One may pass a subset of columns to plot, as well as group by multiple columns:
df = pd.DataFrame(np.random.rand(10,3), columns=['Col1', 'Col2', 'Col3'])
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B'])
df['Y'] = pd.Series(['A','B','A','B','A','B','A','B','A','B'])
plt.figure();
bp = df.boxplot(column=['Col1','Col2'], by=['X','Y'])

#Warning The default changed from 'dict' to 'axes' in version 0.19.0.

#In boxplot, the return type can be controlled by the return_type, keyword. 
#The valid choices are {"axes", "dict", "both", None}. 
#Faceting, created by DataFrame.boxplot with the by keyword, will affect the output type as well:
"""
return_type=	Faceted	Output type
None	No	axes
None	Yes	2-D ndarray of axes
'axes'	No	axes
'axes'	Yes	Series of axes
'dict'	No	dict of artists
'dict'	Yes	Series of dicts of artists
'both'	No	namedtuple
'both'	Yes	Series of namedtuples
"""
#%% - Groupby.boxplot always returns a Series of return_type.
np.random.seed(1234)
df_box = pd.DataFrame(np.random.randn(50, 2))
df_box['g'] = np.random.choice(['A', 'B'], size=50)
df_box.loc[df_box['g'] == 'B', 1] += 3
bp = df_box.boxplot(by='g')

#The subplots above are split by the numeric columns first, then the value of the g column. 

#Below the subplots are first split by the value of g, then by the numeric columns.
bp = df_box.groupby('g').boxplot()

#%% - Area Plot - created with Series.plot.area() and DataFrame.plot.area(). 
#Area plots are stacked by default. 
#To produce stacked area plot, each column must be either all positive or all negative values.

#When input data contains NaN, it will be automatically filled by 0. 
#If you want to drop or fill by different values, use dataframe.dropna() or dataframe.fillna() before calling plot.
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area();

#%% - To produce an unstacked plot, pass stacked=False. Alpha value is set to 0.5 unless otherwise specified:
df.plot.area(stacked=False);

#%% - Scatter Plot - the DataFrame.plot.scatter() method. 
#Scatter plot requires numeric columns for the x and y axes. These can be specified by the x and y keywords.
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b');

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


#%% - Hexagonal Bin Plot - DataFrame.plot.hexbin(). 
#Hexbin plots can be a useful alternative to scatter plots 
#if your data are too dense to plot each point individually.
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df['b'] = df['b'] + np.arange(1000)
df.plot.hexbin(x='a', y='b', gridsize=25)

#%% - A useful keyword argument is gridsize
#It controls the number of hexagons in the x-direction, and defaults to 100. 
#A larger gridsize means more, smaller bins.
#By default, a histogram of the counts around each (x, y) point is computed. 
#You can specify alternative aggregations by passing values to the C and reduce_C_function arguments. 
#C specifies the value at each (x, y) point and reduce_C_function is a function of one argument that 
#reduces all the values in a bin to a single number (e.g. mean, max, sum, std). 
#In this example the positions are given by columns a and b, while the value is given by column z. 
#The bins are aggregated with NumPy’s max function.
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df['b'] = df['b'] = df['b'] + np.arange(1000)
df['z'] = np.random.uniform(0, 3, 1000)
df.plot.hexbin(x='a', y='b', C='z', reduce_C_function=np.max, gridsize=25)


#%% - Pie plot - with DataFrame.plot.pie() or Series.plot.pie(). 
#If your data includes any NaN, they will be automatically filled with 0. 
#A ValueError will be raised if there are any negative values in your data.
series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
series.plot.pie(figsize=(6, 6))

#%% - For pie plots it’s best to use square figures, i.e. a figure aspect ratio 1. 
#You can create the figure with equal width and height, or 
#force the aspect ratio to be equal after plotting by calling ax.set_aspect('equal') on the returned axes object.
#Note that pie plot with DataFrame requires that you either specify a target column 
#by the y argument or subplots=True. 
#When y is specified, pie plot of selected column will be drawn. 
#If subplots=True is specified, pie plots for each column are drawn as subplots. 
#A legend will be drawn in each pie plots by default; specify legend=False to hide it.
df = pd.DataFrame(3 * np.random.rand(4, 2), index=['a', 'b', 'c', 'd'], columns=['x', 'y'])
df.plot.pie(subplots=True, figsize=(8, 4))

#%% - You can use the labels and colors keywords to specify the labels and colors of each wedge.
#Warning Most pandas plots use the label and color arguments (note the lack of “s” on those). 
#To be consistent with matplotlib.pyplot.pie() you must use labels and colors.
#If you want to hide wedge labels, specify labels=None. 
#If fontsize is specified, the value will be applied to wedge labels. 
#Also, other keywords supported by matplotlib.pyplot.pie() can be used.
series.plot.pie(labels=['AA', 'BB', 'CC', 'DD'], colors=['r', 'g', 'b', 'c'], autopct='%.2f', fontsize=20, figsize=(6, 6))

#%% - If you pass values whose sum total is less than 1.0, matplotlib draws a semicircle.
series = pd.Series([0.1] * 4, index=['a', 'b', 'c', 'd'], name='series2')
series.plot.pie(figsize=(6, 6))


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
#%% - Plotting Tools
#These functions can be imported from pandas.plotting and take a Series or DataFrame as an argument.
#Scatter Matrix Plot
#You can create a scatter plot matrix using the scatter_matrix method in pandas.plotting:
from pandas.plotting import scatter_matrix
df = pd.DataFrame(np.random.randn(1000, 4), columns=['a', 'b', 'c', 'd'])
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')

#%% - Density Plot
#You can create density plots using the Series.plot.kde() and DataFrame.plot.kde() methods.
ser = pd.Series(np.random.randn(1000))
ser.plot.kde()

#%% - Andrews Curves
#Andrews curves allow one to plot multivariate data as a large number of curves that are created using the attributes of samples as coefficients for Fourier series, see the Wikipedia entry for more information. By coloring these curves differently for each class it is possible to visualize data clustering. Curves belonging to samples of the same class will usually be closer together and form larger structures.
from pandas.plotting import andrews_curves
data = pd.read_csv('iris.csv')
plt.figure()
andrews_curves(data, 'Name')

#%% - Parallel Coordinates
#Parallel coordinates is a plotting technique for plotting multivariate data, see the Wikipedia entry for an introduction. Parallel coordinates allows one to see clusters in data and to estimate other statistics visually. Using parallel coordinates points are represented as connected line segments. Each vertical line represents one attribute. One set of connected line segments represents one data point. Points that tend to cluster will appear closer together.
from pandas.plotting import parallel_coordinates
data = pd.read_csv('iris.csv')
plt.figure()
parallel_coordinates(data, 'Name')

#%% - Lag Plot
#Lag plots are used to check if a data set or time series is random. 
#Random data should not exhibit any structure in the lag plot.
#Non-random structure implies that the underlying data are not random. 
#The lag argument may be passed, and when lag=1 the plot is essentially data[:-1] vs. data[1:].
from pandas.plotting import lag_plot
plt.figure()
data = pd.Series(0.1 * np.random.rand(1000) +
    0.9 * np.sin(np.linspace(-99 * np.pi, 99 * np.pi, num=1000)))

lag_plot(data)

#%% - Autocorrelation Plot
#Autocorrelation plots are often used for checking randomness in time series. 
#This is done by computing autocorrelations for data values at varying time lags. 
#If time series is random, such autocorrelations should be near zero for any and all time-lag separations. 
#If time series is non-random then one or more of the autocorrelations will be significantly non-zero. 
#The horizontal lines displayed in the plot correspond to 95% and 99% confidence bands. 
#The dashed line is 99% confidence band. See the Wikipedia entry for more about autocorrelation plots.
from pandas.plotting import autocorrelation_plot
plt.figure()
data = pd.Series(0.7 * np.random.rand(1000) +
    0.3 * np.sin(np.linspace(-9 * np.pi, 9 * np.pi, num=1000)))

autocorrelation_plot(data)

#%% - Bootstrap Plot
#Bootstrap plots are used to visually assess the uncertainty of a statistic, 
#such as mean, median, midrange, etc. 
#A random subset of a specified size is selected from a data set, 
#the statistic in question is computed for this subset and the process is repeated a specified number of times. 
#Resulting plots and histograms are what constitutes the bootstrap plot.
from pandas.plotting import bootstrap_plot
data = pd.Series(np.random.rand(1000))
bootstrap_plot(data, size=50, samples=500, color='grey')

#%% - RadViz
#RadViz is a way of visualizing multi-variate data. 
#It is based on a simple spring tension minimization algorithm. 
#Basically you set up a bunch of points in a plane. 
#In our case they are equally spaced on a unit circle. 
#Each point represents a single attribute. 
#You then pretend that each sample in the data set is attached to each of these points by a spring, 
#the stiffness of which is proportional to the numerical value of that attribute 
#(they are normalized to unit interval). 
#The point in the plane, where our sample settles to 
#(where the forces acting on our sample are at an equilibrium) is where a dot representing our sample will be drawn. 
#Depending on which class that sample belongs it will be colored differently. 
from pandas.plotting import radviz
data = pd.read_csv('iris.csv')

plt.figure()

radviz(data, 'Name')

#%% - Plot Formatting - Setting the plot style
#From version 1.5 and up, matplotlib offers a range of preconfigured plotting styles. 
#Setting the style can be used to easily give plots the general look that you want. 
#Setting the style is as easy as calling matplotlib.style.use(my_plot_style) before creating your plot. 
#For example you could write matplotlib.style.use('ggplot') for ggplot-style plots.

#You can see the various available style names at matplotlib.style.available

#General plot style arguments
#Most plotting methods have a set of keyword arguments that control the layout and formatting of the returned plot:
plt.figure()
ts.plot(style='k--', label='Series')

#For each kind of plot (e.g. line, bar, scatter) any additional arguments keywords are passed along 
#to the corresponding matplotlib function (ax.plot(), ax.bar(), ax.scatter()). 
#These can be used to control additional styling, beyond what pandas provides.

#%% - Controlling the Legend
#You may set the legend argument to False to hide the legend, which is shown by default.
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot(legend=False)

#%% - Scales - One may pass logy to get a log-scale Y axis.
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = np.exp(ts.cumsum())
ts.plot(logy=True)
#See also the logx and loglog keyword arguments.

#%% - Plotting on a Secondary Y-axis
#To plot data on a secondary y-axis, use the secondary_y keyword:
df.A.plot()
df.B.plot(secondary_y=True, style='g')

#%% - To plot some columns in a DataFrame, give the column names to the secondary_y keyword:
plt.figure()
ax = df.plot(secondary_y=['A', 'B'])
ax.set_ylabel('CD scale')

ax.right_ax.set_ylabel('AB scale')

#Note that the columns plotted on the secondary y-axis is automatically marked with “(right)” in the legend. To turn off the automatic marking, use the mark_right=False keyword:
plt.figure()
df.plot(secondary_y=['A', 'B'], mark_right=False)

#%% - Suppressing Tick Resolution Adjustment
#pandas includes automatic tick resolution adjustment for regular frequency time-series data. 
#For limited cases where pandas cannot infer the frequency information (e.g., in an externally created twinx), 
#you can choose to suppress this behavior for alignment purposes.

#Here is the default behavior, notice how the x-axis tick labeling is performed:
plt.figure()
df.A.plot()

#Using the x_compat parameter, you can suppress this behavior:
plt.figure()
df.A.plot(x_compat=True)

#If you have more than one plot that needs to be suppressed, the use method in pandas.plotting.plot_params can be used in a with statement:
plt.figure()
with pd.plotting.plot_params.use('x_compat', True):
    df.A.plot(color='r')
    df.B.plot(color='g')
    df.C.plot(color='b')
#Automatic Date Tick Adjustment (New in version 0.20.0)
#TimedeltaIndex now uses the native matplotlib tick locator methods, 
#it is useful to call the automatic date tick adjustment from matplotlib for figures whose ticklabels overlap.

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

#You can pass multiple axes created beforehand as list-like via ax keyword. 
#This allows more complicated layouts. The passed axes must be the same number as the subplots being drawn.

#When multiple axes are passed via the ax keyword, layout, sharex and sharey keywords don’t affect to the output. You should explicitly pass sharex=False and sharey=False, otherwise you will see a warning.
fig, axes = plt.subplots(4, 4, figsize=(6, 6));
plt.subplots_adjust(wspace=0.5, hspace=0.5);
target1 = [axes[0][0], axes[1][1], axes[2][2], axes[3][3]]
target2 = [axes[3][0], axes[2][1], axes[1][2], axes[0][3]]

df.plot(subplots=True, ax=target1, legend=False, sharex=False, sharey=False);
(-df).plot(subplots=True, ax=target2, legend=False, sharex=False, sharey=False);

#Another option is passing an ax argument to Series.plot() to plot on a particular axis:
fig, axes = plt.subplots(nrows=2, ncols=2)
df['A'].plot(ax=axes[0,0]); axes[0,0].set_title('A');
df['B'].plot(ax=axes[0,1]); axes[0,1].set_title('B');
df['C'].plot(ax=axes[1,0]); axes[1,0].set_title('C');
df['D'].plot(ax=axes[1,1]); axes[1,1].set_title('D');
#%% - Plotting With Error Bars - supported in DataFrame.plot() and Series.plot().
#Horizontal and vertical error bars can be supplied to the xerr and yerr keyword arguments to plot(). 
#The error values can be specified using a variety of formats:

#As a DataFrame or dict of errors with column names matching the columns attribute of the plotting DataFrame or 
#matching the name attribute of the Series.
#As a str indicating which of the columns of plotting DataFrame contain the error values.
#As raw values (list, tuple, or np.ndarray). Must be the same length as the plotting DataFrame/Series.
#Asymmetrical error bars are also supported, however raw error values must be provided in this case. 
#For a M length Series, a Mx2 array should be provided indicating lower and upper (or left and right) errors. 
#For a MxN DataFrame, asymmetrical errors should be in a Mx2xN array.

#Example of one way to easily plot group means with standard deviations from the raw data.
# Generate the data
ix3 = pd.MultiIndex.from_arrays([['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'], ['foo', 'foo', 'bar', 'bar', 'foo', 'foo', 'bar', 'bar']], names=['letter', 'word'])

df3 = pd.DataFrame({'data1': [3, 2, 4, 3, 2, 4, 3, 2], 'data2': [6, 5, 7, 5, 4, 5, 6, 5]}, index=ix3)

# Group by index labels and take the means and standard deviations for each group
gp3 = df3.groupby(level=('letter', 'word'))
means = gp3.mean()
errors = gp3.std()
means

errors

# Plot
fig, ax = plt.subplots()
means.plot.bar(yerr=errors, ax=ax)

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

#%% - Colormaps
#A potential issue when plotting a large number of columns is that 
#it can be difficult to distinguish some series due to repetition in the default colors. 
#So DataFrame plotting supports the use of the colormap argument, 
#which accepts either a Matplotlib colormap or a string 
#that is a name of a colormap registered with Matplotlib. 
#A visualization of the default matplotlib colormaps is available here.

#As matplotlib does not directly support colormaps for line-based plots, 
#the colors are selected based on an even spacing determined by the number of columns in the DataFrame. 
#There is no consideration made for background color, 
#so some colormaps will produce lines that are not easily visible.

#To use the cubehelix colormap, we can pass colormap='cubehelix'.
df = pd.DataFrame(np.random.randn(1000, 10), index=ts.index)
df = df.cumsum()
plt.figure()
df.plot(colormap='cubehelix')

#%% - Alternatively, we can pass the colormap itself:
from matplotlib import cm
plt.figure()
df.plot(colormap=cm.cubehelix)

#%% - Colormaps can also be used other plot types, like bar charts:
dd = pd.DataFrame(np.random.randn(10, 10)).applymap(abs)
dd = dd.cumsum()
plt.figure()
dd.plot.bar(colormap='Greens')

#%% - Parallel coordinates charts:
plt.figure()
parallel_coordinates(data, 'Name', colormap='gist_rainbow')

#%% - Andrews curves charts:
plt.figure()
andrews_curves(data, 'Name', colormap='winter')

#%% - Plotting directly with matplotlib
#In some situations it may still be preferable or necessary to prepare plots directly with matplotlib, 
#for instance when a certain type of plot or customization is not (yet) supported by pandas. 
#Series and DataFrame objects behave like arrays and 
#can therefore be passed directly to matplotlib functions without explicit casts.

#pandas also automatically registers formatters and locators that recognize date indices, 
#thereby extending date and time support to practically all plot types available in matplotlib. 
#Although this formatting does not provide the same level of refinement you would get when plotting via pandas, 
#it can be faster when plotting a large number of points.
price = pd.Series(np.random.randn(150).cumsum(), index=pd.date_range('2000-1-1', periods=150, freq='B'))
ma = price.rolling(20).mean()
mstd = price.rolling(20).std()
plt.figure()
plt.plot(price.index, price, 'k')

plt.plot(ma.index, ma, 'b')

plt.fill_between(mstd.index, ma-2*mstd, ma+2*mstd, color='b', alpha=0.2)