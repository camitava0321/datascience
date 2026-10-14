##Time Series Tutorial

# Time Series - Introduction
A time series is a sequence of observations over a certain period. 

The simplest example - change in temperature throughout the day or week or month or year.

A univariate time series consists of the values taken by a single variable at periodic time instances over a period.
A multivariate time series consists of the values taken by multiple variables at the same periodic time instances over a period. 

The analysis of temporal data is capable of giving us useful insights on how a variable changes over time, or how it depends on the change in the values of other variable(s). This relationship of a variable on its previous values and/or other variables can be analyzed for time series forecasting and has numerous applications in artificial intelligence.

Time Series - Python Libraries

Python has an established popularity among individuals who perform machine learning because of its easy-to-write and easy-to-understand code structure as well as a wide variety of open source libraries. A few of such open source libraries that we will be using.

NumPy
Numerical Python is a library used for scientific computing. It works on an N-dimensional array object and provides basic mathematical functionality such as size, shape, mean, standard deviation, minimum, maximum as well as some more complex functions such as linear algebraic functions and Fourier transform. 

Pandas - provides highly efficient and easy-to-use data structures such as series, dataframes and panels. It has enhanced Pythons functionality from mere data collection and preparation to data analysis. The two libraries, Pandas and NumPy, make any operation on small to very large dataset very simple. 

SciPy
Science Python is a library used for scientific and technical computing. It provides functionalities for optimization, signal and image processing, integration, interpolation and linear algebra. This library comes handy while performing machine learning.

Scikit Learn - This library is a SciPy Toolkit widely used for statistical modelling, machine learning and deep learning, as it contains various customizable regression, classification and clustering models. It works well with Numpy, Pandas and other libraries which makes it easier to use.

Statsmodels
Like Scikit Learn, this library is used for statistical data exploration and statistical modelling. It also operates well with other Python libraries.

Matplotlib
This library is used for data visualization in various formats such as line plot, bar graph, heat maps, scatter plots, histogram etc. It contains all the graph related functionalities required from plotting to labelling. We will discuss these functionalities as we move ahead in this tutorial.

These libraries are very essential to start with machine learning with any sort of data.

Beside the ones discussed above, another library especially significant to deal with time series is −
Datetime - this library, with its two modules − datetime and calendar, provides all necessary datetime functionality for reading, formatting and manipulating time.

Time Series - Modeling

A time series has 4 components as given below −
Level − It is the mean value around which the series varies.
Trend − It is the increasing or decreasing behavior of a variable with time.
Seasonality − It is the cyclic behavior of time series.
Noise − It is the error in the observations added due to environmental factors.

Time Series Modeling Techniques
To capture these components, there are a number of popular time series modelling techniques. This section gives a brief introduction of each technique, however we will discuss about them in detail in the upcoming chapters −

Naive Methods
These are simple estimation techniques, such as the predicted value is given the value equal to mean of preceding values of the time dependent variable, or previous actual value. These are used for comparison with sophisticated modelling techniques.

Auto Regression
Auto regression predicts the values of future time periods as a function of values at previous time periods. Predictions of auto regression may fit the data better than that of naive methods, but it may not be able to account for seasonality.

ARIMA Model
An auto-regressive integrated moving-average models the value of a variable as a linear function of previous values and residual errors at previous time steps of a stationary timeseries. However, the real world data may be non-stationary and have seasonality, thus Seasonal-ARIMA and Fractional-ARIMA were developed. ARIMA works on univariate time series, to handle multiple variables VARIMA was introduced.

Exponential Smoothing
It models the value of a variable as an exponential weighted linear function of previous values. This statistical model can handle trend and seasonality as well.

LSTM
Long Short-Term Memory model (LSTM) is a recurrent neural network which is used for time series to account for long term dependencies. It can be trained with large amount of data to capture the trends in multi-variate time series.

The said modelling techniques are used for time series regression. 



Time Series - Parameter Calibration

Any statistical or machine learning model has some parameters which greatly influence how the data is modeled. For example, ARIMA has p, d, q values. These parameters are to be decided such that the error between actual values and modeled values is minimum. Parameter calibration is said to be the most crucial and time-consuming task of model fitting. Hence, it is very essential for us to choose optimal parameters.

Methods for Calibration of Parameters
There are various ways to calibrate parameters. This section talks about some of them in detail.

Hit-and-try
One common way of calibrating models is hand calibration, where you start by visualizing the time-series and intuitively try some parameter values and change them over and over until you achieve a good enough fit. It requires a good understanding of the model we are trying. 

For ARIMA model, hand calibration is done with the help of auto-correlation plot for p parameter, partial auto-correlation plot for q parameter and ADF-test to confirm the stationarity of time-series and setting d parameter. 

Grid Search
Another way of calibrating models is by grid search, which essentially means you try building a model for all possible combinations of parameters and select the one with minimum error. This is time-consuming and hence is useful when number of parameters to be calibrated and range of values they take are fewer as this involves multiple nested for loops.

Genetic Algorithm
Genetic algorithm works on the biological principle that a good solution will eventually evolve to the most optimal solution. It uses biological operations of mutation, cross-over and selection to finally reach to an optimal solution.

For further knowledge you can read about other parameter optimization techniques like Bayesian optimization and Swarm optimization.


Time Series - Error Metrics

It is important for us to quantify the performance of a model to use it as a feedback and comparison. In this tutorial we have used one of the most popular error metric root mean squared error. There are various other error metrics available. This chapter discusses them in brief.

Mean Square Error
It is the average of square of difference between the predicted values and true values. Sklearn provides it as a function. It has the same units as the true and predicted values squared and is always positive.

MSE=1/n∑_(t=1)_n ⟮y′_t−y_t⟯^2

Where y′_t is the predicted value,
y_t is the actual value, and n is the total number of values in test set.

It is clear from the equation that MSE is more penalizing for larger errors, or the outliers.


Root Mean Square Error
It is the square root of the mean square error. It is also always positive and is in the range of the data.

RMSE=1/sqrt(n)∑_(t=1)_n ⟮y′_t−y_t⟯^2

Where, y′_t is predicted value
y_t is actual value, and
n is total number of values in test set.

It is in the power of unity and hence is more interpretable as compared to MSE. RMSE is also more penalizing for larger errors. We have used RMSE metric in our tutorial.

Mean Absolute Error
It is the average of absolute difference between predicted values and true values. It has the same units as predicted and true value and is always positive.

MAE=1/n∑_(t=1)_(t=n) |y′_t−y_t|

Where, y′_t is predicted value,
y_t is actual value, and
n is total number of values in test set.

Mean Percentage Error
It is the percentage of average of absolute difference between predicted values and true values, divided by the true value.

MAPE=1/n∑_(t=1)_n (y′_t−y_t)/y_t ∗ 100%

Where, y′_t is predicted value,
y_t is actual value and n is total number of values in test set.

However, the disadvantage of using this error is that the positive error and negative errors can offset each other. Hence mean absolute percentage error is used.

Mean Absolute Percentage Error
It is the percentage of average of absolute difference between predicted values and true values, divided by the true value.

MAPE=1/n∑_(t=1)_n |y′_t−y_t|/y_t ∗ 100%

Where y′_t is predicted value
y_t is actual value, and
n is total number of values in test set.

Time Series - Applications

Previous
Quiz
Next
We discussed time series analysis in this tutorial, which has given us the understanding that time series models first recognize the trend and seasonality from the existing observations and then forecast a value based on this trend and seasonality. Such analysis is useful in various fields such as −

Financial Analysis − It includes sales forecasting, inventory analysis, stock market analysis, price estimation.

Weather Analysis − It includes temperature estimation, climate change, seasonal shift recognition, weather forecasting.

Network Data Analysis − It includes network usage prediction, anomaly or intrusion detection, predictive maintenance.

Healthcare Analysis − It includes census prediction, insurance benefits prediction, patient monitoring.

Time Series - Further Scope

Previous
Quiz
Next
Machine learning deals with various kinds of problems. In fact, almost all fields have a scope to be automatized or improved with the help of machine learning. A few such problems on which a great deal of work is being done are given below.

Time Series Data
This is the data which changes according to time, and hence time plays a crucial role in it, which we largely discussed in this tutorial.

Advertisement
-
PlayStream
00:15

Non-Time Series Data
It is the data independent of time, and a major percentage of ML problems are on nontime series data. For simplicity, we shall categorize it further as −

Numerical Data − Computers, unlike humans, only understand numbers, so all kinds of data ultimately is converted to numerical data for machine learning, for example, image data is converted to (r,b,g) values, characters are converted to ASCII codes or words are indexed to numbers, speech data is converted to mfcc files containing numerical data.

Image Data − Computer vision has revolutionized the world of computers, it has various application in the field of medicine, satellite imaging etc.

Text Data − Natural Language Processing (NLP) is used for text classification, paraphrase detection and language summarization. This is what makes Google and Facebook smart.

Speech Data − Speech Processing involves speech recognition and sentiment understanding. It plays a crucial role in imparting computers the human-like qualities.


