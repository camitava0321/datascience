"""
Amitava Chakraborty
"""
#Time Series - Auto Regression
#For a stationary time series, an auto regression models sees the value of a variable at time t as a 
#linear function of values p time steps preceding it. Mathematically it can be written as −

#y_t=C+ϕ_1*y_(t−1)+ϕ_2*Y_(t−2)+...+ϕ_p*y_(t−p)+ϵ_t
#Where,
#p is the auto-regressive trend parameter
#ϵ_t is white noise, and
#y_(t−1),y_(t−2)...y_(t−p) denote the value of variable at previous time periods.

#The value of p can be calibrated using various methods. One way of finding the apt value of p is plotting 
#the auto-correlation plot.

#Note − We should separate the data into train and test at 8:2 ratio of total data available prior to 
#doing any analysis on the data because test data is only to find out the accuracy of our model and 
#assumption is, it is not available to us until after predictions have been made. 
#In case of time series, sequence of data points is very essential so one should keep in mind not to 
#lose the order during splitting of data.

#An auto-correlation plot or a correlogram shows the relation of a variable with itself at prior time 
#steps. It makes use of Pearsons correlation and shows the correlations within 95% confidence interval. 
#Lets see how it looks like for temperature variable of our data.

#Showing ACP
from ts import getDataFrame
df = getDataFrame()
split = len(df) - int(0.2*len(df))
train, test = df['T'][0:split], df['T'][split:]

import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

plot_acf(train, lags = 100)
plt.show()
#All the lag values lying outside the shaded blue region are assumed to have a correlation.
#%%
#Time Series - Moving Average
#For a stationary time series, a moving average model sees the value of a variable at time t as a 
#linear function of residual errors from q time steps preceding it. The residual error is calculated by 
#comparing the value at the time t to moving average of the values preceding.

#Mathematically it can be written as −
#y_t=c+ϵ_t+θ_1*ϵ_(t−1)+θ_2*ϵ_(t−2)+...+θ_q*ϵ_(t−q)
#Where q is the moving-average trend parameter
#ϵ_t is white noise, and
#ϵ_(t−1),ϵ_(t−2)...ϵ_(t−q) are the error terms at previous time periods.

#Value of q can be calibrated using various methods. One way of finding the apt value of q is plotting 
#the partial auto-correlation plot.

#A partial auto-correlation plot shows the relation of a variable with itself at prior time steps with 
#indirect correlations removed, unlike auto-correlation plot which shows direct as well as 
#indirect correlations, lets see how it looks like for temperature variable of our data.

#Showing PACP
from statsmodels.graphics.tsaplots import plot_pacf

plot_pacf(train, lags = 100)
plt.show()
#A partial auto-correlation is read in the same way as a correlogram.import matplotlib.pyplot as plt
#%%
#Time Series - ARIMA
#We have already understood that for a stationary time series a variable at time t is a linear 
#function of prior observations or residual errors. Hence it is time for us to combine the two 
#and have an Auto-regressive moving average (ARMA) model.

#However, at times the time series is not stationary, i.e the statistical properties of a series like 
#mean, variance changes over time. And the statistical models we have studied so far assume the 
#time series to be stationary, therefore, we can include a pre-processing step of differencing the 
#time series to make it stationary. Now, it is important for us to find out whether the time series 
#we are dealing with is stationary or not.

#Various methods to find the stationarity of a time series are looking for seasonality or trend 
#in the plot of time series, checking the difference in mean and variance for various time periods, 
#Augmented Dickey-Fuller (ADF) test, KPSS test, Hursts exponent etc.

#Let us see whether the temperature variable of our dataset is a stationary time series or not using ADF test.
from statsmodels.tsa.stattools import adfuller

result = adfuller(train)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
   print('\t%s: %.3f' % (key, value))
#%%
#Now that we have run the ADF test, let us interpret the result. 
#First we will compare the ADF Statistic with the critical values, a lower critical value tells us the 
#series is most likely non-stationary. Next, we see the p-value. A p-value greater than 0.05 also 
#suggests that the time series is non-stationary.

#Alternatively, p-value less than or equal to 0.05, or ADF Statistic less than critical values suggest 
#the time series is stationary.

#Hence, the time series we are dealing with is already stationary. In case of stationary time series, 
#we set the d parameter as 0.

#We can also confirm the stationarity of time series using Hurst exponent.
import hurst

H, c,data = hurst.compute_Hc(train)
print("H = {:.4f}, c = {:.4f}".format(H,c))

#The value of H<0.5 shows anti-persistent behavior, and H>0.5 shows persistent behavior or a 
#trending series. H=0.5 shows random walk/Brownian motion. The value of H<0.5, confirming that 
#our series is stationary.

#For non-stationary time series, we set d parameter as 1. Also, the value of the auto-regressive 
#trend parameter p and the moving average trend parameter q, is calculated on the stationary time series 
#i.e by plotting ACP and PACP after differencing the time series.

#ARIMA Model, which is characterized by 3 parameter, (p,d,q) are now clear to us, 
#so let us model our time series and predict the future values of temperature.
#%%
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
from math import sqrt
from sklearn import metrics
model = ARIMA(train.values, order=(5, 0, 2))
model_fit = model.fit()#disp=False)

predictions = model_fit.predict(len(test))
test_ = pd.DataFrame(test)
test_['predictions'] = predictions[0:1871]

plt.plot(df['T'])
plt.plot(test_.predictions)
plt.show()
error = sqrt(metrics.mean_squared_error(test.values,predictions[0:1871]))
print ('Test RMSE for ARIMA: ', error)
#%%
#Time Series - Variations of ARIMA
#In the previous chapter, we have now seen how ARIMA model works, and its limitations that it cannot 
#handle seasonal data or multivariate time series and hence, new models were introduced to include 
#these features.

#A glimpse of these new models is given here −
#Vector Auto-Regression (VAR)
#It is a generalized version of auto regression model for multivariate stationary time series. 
#It is characterized by p parameter.

#Vector Moving Average (VMA)
#It is a generalized version of moving average model for multivariate stationary time series. 
#It is characterized by q parameter.

#Vector Auto Regression Moving Average (VARMA)
#It is the combination of VAR and VMA and a generalized version of ARMA model for multivariate 
#stationary time series. It is characterized by p and q parameters. Much like, 
#ARMA is capable of acting like an AR model by setting q parameter as 0 and as a MA model by 
#setting p parameter as 0, VARMA is also capable of acting like an VAR model by setting q parameter 
#as 0 and as a VMA model by setting p parameter as 0.
df_multi = df[['T', 'C6H6(GT)']]
split = len(df) - int(0.2*len(df))
train_multi, test_multi = df_multi[0:split], df_multi[split:]

from statsmodels.tsa.statespace.varmax import VARMAX

model = VARMAX(train_multi, order = (2,1))
model_fit = model.fit()
"""
We will. get following sort of EstimationWarning:
EstimationWarning: Estimation of VARMA(p,q) models is not generically robust, due especially to 
identification issues.
...warnings.warn("Maximum Likelihood optimization failed to "
"""
#%%
predictions_multi = model_fit.forecast( steps=len(test_multi))
#%%
plt.plot(train_multi['T'])
plt.plot(test_multi['T'])
plt.plot(predictions_multi.iloc[:,0:1], '--')
plt.show()

plt.plot(train_multi['C6H6(GT)'])
plt.plot(test_multi['C6H6(GT)'])
plt.plot(predictions_multi.iloc[:,1:2], '--')
plt.show()

#The above code shows how VARMA model can be used to model multivariate time series, although this model 
#may not be best suited on our data.
#%%
#VARMA with Exogenous Variables (VARMAX)
#It is an extension of VARMA model where extra variables called covariates are used to model the 
#primary variable we are interested it.

#Seasonal Auto Regressive Integrated Moving Average (SARIMA)
#This is the extension of ARIMA model to deal with seasonal data. 
#It divides the data into seasonal and non-seasonal components and models them in a similar fashion. 
#It is characterized by 7 parameters, for non-seasonal part (p,d,q) parameters same as for 
#ARIMA model and for seasonal part (P,D,Q,m) parameters where m is the number of seasonal periods 
#and P,D,Q are similar to parameters of ARIMA model. 
#These parameters can be calibrated using grid search or genetic algorithm.

#SARIMA with Exogenous Variables (SARIMAX)
#This is the extension of SARIMA model to include exogenous variables which help us to model the 
#variable we are interested in.

#It may be useful to do a co-relation analysis on variables before putting them as exogenous variables.

from scipy.stats.stats import pearsonr
x = train_multi['T'].values
y = train_multi['C6H6(GT)'].values

corr , p = pearsonr(x,y)
print ('Corelation Coefficient =', corr,'\nP-Value =',p)
#%%
#Pearsons Correlation shows a linear relation between 2 variables, to interpret the results, 
#we first look at the p-value, if it is less that 0.05 then the value of coefficient is significant, 
#else the value of coefficient is not significant. For significant p-value, a positive value of 
#correlation coefficient indicates positive correlation, and a negative value indicates a negative correlation.

#Hence, for our data, temperature and C6H6 seem to have a highly positive correlation. 
#Therefore, we will
from statsmodels.tsa.statespace.sarimax import SARIMAX

model = SARIMAX(x, exog = y, order = (2, 0, 2), seasonal_order = (2, 0, 1, 1), \
    enforce_stationarity=False, enforce_invertibility = False)
model_fit = model.fit(disp = False)
#We will get ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals...
#%%
y_ = test_multi['C6H6(GT)'].values
predicted = model_fit.predict(exog=y_)
test_multi_ = pd.DataFrame(test)
test_multi_['predictions'] = predicted[0:1871]
plt.plot(train_multi['T'])
plt.plot(test_multi_['T'])
plt.plot(test_multi_.predictions, '--')
#%%
#The predictions here seem to take larger variations now as opposed to univariate ARIMA modelling.

#Needless to say, SARIMAX can be used as an ARX, MAX, ARMAX or ARIMAX model by setting only the corresponding 
#parameters to non-zero values.

#Fractional Auto Regressive Integrated Moving Average (FARIMA)
#At times, it may happen that our series is not stationary, yet differencing with d parameter 
#taking the value 1 may over-difference it. So, we need to difference the time series using a fractional value.

#In the world of data science there is no one superior model, the model that works on your data 
#depends greatly on your dataset. Knowledge of various models allows us to choose one that work 
#on our data and experimenting with that model to achieve the best results. And results should be 
#seen as plot as well as error metrics, at times a small error may also be bad, hence, plotting and 
#visualizing the results is essential.

#In the next chapter, we will be looking at another statistical model, exponential smoothing.
#%%
#Time Series - Exponential Smoothing
#In this chapter, we will talk about the techniques involved in exponential smoothing of time series.

#Simple Exponential Smoothing
#Exponential Smoothing is a technique for smoothing univariate time-series by assigning exponentially 
#decreasing weights to data over a time period.

#Mathematically, the value of variable at time t+1 given value at time t, y_(t+1|t) is defined as −

#y_(t+1|t)=α*y_t+α*⟮1−α⟯*y_(t−1)+α*⟮1−α⟯^2*y_(t−2)+...+y_1
#where,0≤α≤1 is the smoothing parameter, and
#y_1,....,y_t are previous values of network traffic at times 1, 2, 3, ,t.

#This is a simple method to model a time series with no clear trend or seasonality. But exponential 
#smoothing can also be used for time series with trend and seasonality.

#Triple Exponential Smoothing (TES) or Holt's Winter method, applies exponential smoothing three times - 
#level smoothing l_t, trend smoothing b_t, and seasonal smoothing S_t, with α, β∗ and γ as smoothing 
#parameters with m as the frequency of the seasonality, i.e. the number of seasons in a year.

#According to the nature of the seasonal component, TES has two categories −
#1. Holt-Winter's Additive Method − When the seasonality is additive in nature.
#2. Holt-Winters Multiplicative Method − When the seasonality is multiplicative in nature.

#For non-seasonal time series, we only have trend smoothing and level smoothing, which is called 
#Holts Linear Trend Method.

#Lets try applying triple exponential smoothing on our data.
from statsmodels.tsa.holtwinters import ExponentialSmoothing

model = ExponentialSmoothing(train.values)#, trend= )
model_fit = model.fit()
predictions_ = model_fit.predict(len(test))
#%%
plt.plot(test.values)
plt.plot(predictions_[1:1871])
#Here, we have trained the model once with training set and then we keep on making predictions. 
#A more realistic approach is to re-train the model after one or more time step(s). 
#As we get the prediction for time t+1 from training data til time t, the next prediction for 
#time t+2 can be made using the training data til time t+1 as the actual value at t+1 will be known then. 
#This methodology of making predictions for one or more future steps and then re-training the model 
#is called rolling forecast or walk forward validation.
#%%
#Time Series - Walk Forward Validation
#In time series modelling, the predictions over time become less and less accurate and hence it is a 
#more realistic approach to re-train the model with actual data as it gets available for further 
#predictions. Since training of statistical models are not time consuming, walk-forward validation is 
#the most preferred solution to get most accurate results.

#Let us apply one step walk forward validation on our data and compare it with the results we got earlier.
import numpy as np
prediction = []
data = train.values
for t in test.values:
   model = (ExponentialSmoothing(data).fit())
   y = model.predict()
   prediction.append(y[0])
   data = np.append(data, t)

test_ = pd.DataFrame(test)
test_['predictionswf'] = prediction
plt.plot(test_['T'])
plt.plot(test_.predictionswf, '--')
plt.show()
#%%
error = sqrt(metrics.mean_squared_error(test.values,prediction))
print ('Test RMSE for Triple Exponential Smoothing with Walk-Forward Validation: ', error)
#We can see that our model performs significantly better now. In fact, the trend is followed so 
#closely that on the plot predictions are overlapping with the actual values. 
#You can try applying walk-forward validation on ARIMA models too.
#%%
#Time Series - Prophet Model
#In 2017, Facebook open sourced the prophet model which was capable of modelling the time series with 
#strong multiple seasonalities at day level, week level, year level etc. and trend. 
#It has intuitive parameters that a not-so-expert data scientist can tune for better forecasts. 
#At its core, it is an additive regressive model which can detect change points to model the time series.

#Prophet decomposes the time series into components of trend g_t, seasonality S_t and holidays h_t.

#y_t=g_t+s_t+h_t+ϵ_t
#Where, ϵ_t is the error term.

#Similar packages for time series forecasting such as causal impact and anomaly detection were 
#introduced in R by google and twitter respectively.
#%%
#Time Series - LSTM Model
#Now, we are familiar with statistical modelling on time series, but machine learning is all the 
#rage right now, so it is essential to be familiar with some machine learning models as well. 
#We shall start with the most popular model in time series domain − Long Short-term Memory model.

#LSTM is a class of recurrent neural network. So before we can jump to LSTM, 
#it is essential to understand neural networks and recurrent neural networks.

#Neural Networks
#An artificial neural network is a layered structure of connected neurons, inspired by biological 
#neural networks. It is not one algorithm but combinations of various algorithms which allows us to 
#do complex operations on data.

#Recurrent Neural Networks
#It is a class of neural networks tailored to deal with temporal data. The neurons of RNN have a cell 
#state/memory, and input is processed according to this internal state, which is achieved with the help 
#of loops with in the neural network. There are recurring module(s) of tanh layers in RNNs that allow them 
#to retain information. However, not for a long time, which is why we need LSTM models.

#LSTM
#It is special kind of recurrent neural network that is capable of learning long term dependencies 
#in data. This is achieved because the recurring module of the model has a combination of four layers 
#interacting with each other.

#Neural Network
#The picture above depicts four neural network layers in yellow boxes, point wise operators in green 
#circles, input in yellow circles and cell state in blue circles. An LSTM module has a cell state and 
#three gates which provides them with the power to selectively learn, unlearn or retain information from 
#each of the units. The cell state in LSTM helps the information to flow through the units without being 
#altered by allowing only a few linear interactions. Each unit has an input, output and a forget gate 
#which can add or remove the information to the cell state. 
#The forget gate decides which information from the previous cell state should be forgotten for which it 
#uses a sigmoid function. The input gate controls the information flow to the current cell state using a 
#point-wise multiplication operation of sigmoid and tanh respectively. 
#Finally, the output gate decides which information should be passed on to the next hidden state

#Now that we have understood the internal working of LSTM model, let us implement it. 
#To understand the implementation of LSTM, we will start with a simple example − a straight line. 
#Let us see, if LSTM can learn the relationship of a straight line and predict it.

#First let us create the dataset depicting a straight line.
x = np.arange (1,500,1)
y = 0.4 * x + 30
plt.plot(x,y)
#%%
trainx, testx = x[0:int(0.8*(len(x)))], x[int(0.8*(len(x))):]
trainy, testy = y[0:int(0.8*(len(y)))], y[int(0.8*(len(y))):]
train = np.array(list(zip(trainx,trainy)))
test = np.array(list(zip(trainx,trainy)))
#Now that the data has been created and split into train and test. Lets convert the time series data into 
#the form of supervised learning data according to the value of look-back period, which is essentially the number of lags which are seen to predict the value at time t.

#So a time series like this −
"""
time variable_x
t1  x1
t2  x2
 :   :
 :   :
T   xT
When look-back period is 1, is converted to −

x1   x2
x2   x3
 :    :
 :    :
xT-1 xT
"""
def create_dataset(n_X, look_back):
   dataX, dataY = [], []
   for i in range(len(n_X)-look_back):
      a = n_X[i:(i+look_back), ]
      dataX.append(a)
      dataY.append(n_X[i + look_back, ])
   return np.array(dataX), np.array(dataY)

look_back = 1
trainx,trainy = create_dataset(train, look_back)
testx,testy = create_dataset(test, look_back)

trainx = np.reshape(trainx, (trainx.shape[0], 1, 2))
testx = np.reshape(testx, (testx.shape[0], 1, 2))
#%%
#Now we will train our model.

#Small batches of training data are shown to network, one run of when entire training data is shown to 
#the model in batches and error is calculated is called an epoch. The epochs are to be run til the 
#time the error is reducing.
from keras.models import Sequential
from keras.layers import LSTM, Dense

model = Sequential()
model.add(LSTM(256, return_sequences = True, input_shape = (trainx.shape[1], 2)))
model.add(LSTM(128,input_shape = (trainx.shape[1], 2)))
model.add(Dense(2))
model.compile(loss = 'mean_squared_error', optimizer = 'adam')
model.fit(trainx, trainy, epochs = 2000, batch_size = 10, verbose = 2, shuffle = False)
model.save_weights('LSTMBasic1.h5')
#%%
model.load_weights('LSTMBasic1.h5')
predict = model.predict(testx)
#Now lets see what our predictions look like.
plt.plot(testx.reshape(398,2)[:,0:1], testx.reshape(398,2)[:,1:2])
plt.plot(predict[:,0:1], predict[:,1:2])
#%%
#Now, we should try and model a sine or cosine wave in a similar fashion. You can run the code given 
#below and play with the model parameters to see how the results change.
x = np.arange (1,500,1)
y = np.sin(x)
plt.plot(x,y)
#%%
trainx, testx = x[0:int(0.8*(len(x)))], x[int(0.8*(len(x))):]
trainy, testy = y[0:int(0.8*(len(y)))], y[int(0.8*(len(y))):]
train = np.array(list(zip(trainx,trainy)))
test = np.array(list(zip(trainx,trainy)))
look_back = 1
trainx,trainy = create_dataset(train, look_back)
testx,testy = create_dataset(test, look_back)
trainx = np.reshape(trainx, (trainx.shape[0], 1, 2))
testx = np.reshape(testx, (testx.shape[0], 1, 2))

model = Sequential()
model.add(LSTM(512, return_sequences = True, input_shape = (trainx.shape[1], 2)))
model.add(LSTM(256,input_shape = (trainx.shape[1], 2)))
model.add(Dense(2))
model.compile(loss = 'mean_squared_error', optimizer = 'adam')
model.fit(trainx, trainy, epochs = 2000, batch_size = 10, verbose = 2, shuffle = False)
model.save_weights('LSTMBasic2.h5')
#%%
model.load_weights('LSTMBasic2.h5')
predict = model.predict(testx)
plt.plot(trainx.reshape(398,2)[:,0:1], trainx.reshape(398,2)[:,1:2])
plt.plot(predict[:,0:1], predict[:,1:2])
#Now you are ready to move on to any dataset.
#%%
