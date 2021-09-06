# -*- coding: utf-8 -*-
#author : Amitava Chakraborty
# quandl for financial data
import quandl
# pandas for data manipulation
import pandas as pd
import matplotlib.pyplot as plt

#quandl.ApiConfig.api_key = 'getyourownkey!'

# Retrieve TSLA data from Quandl
tesla = quandl.get('WIKI/TSLA')

# Retrieve the GM data from Quandl
gm = quandl.get('WIKI/GM')
gm.head(5)

#%% - Exploratory Plots
# The adjusted close accounts for stock splits, so that is what we should graph
plt.plot(gm.index, gm['Adj. Close'])
plt.title('GM Stock Price')
plt.ylabel('Price ($)');
plt.show()

plt.plot(tesla.index, tesla['Adj. Close'], 'r')
plt.title('Tesla Stock Price')
plt.ylabel('Price ($)');
plt.show();

#%% - Which company is more valuable
#total value of a company (market capitalization) 
#depends on the number of shares (Market cap= share price * number of shares). 

# Yearly average number of shares outstanding for Tesla and GM
tesla_shares = {2018: 168e6, 2017: 162e6, 2016: 144e6, 2015: 128e6, 2014: 125e6, 2013: 119e6, 2012: 107e6, 2011: 100e6, 2010: 51e6}

gm_shares = {2018: 1.42e9, 2017: 1.50e9, 2016: 1.54e9, 2015: 1.59e9, 2014: 1.61e9, 2013: 1.39e9, 2012: 1.57e9, 2011: 1.54e9, 2010:1.50e9}

# Create a year column 
tesla['Year'] = tesla.index.year
gm['Year'] = gm.index.year

# Take Dates from index and move to Date column 
tesla.reset_index(level=0, inplace = True)
tesla['cap'] = 0   #placeholder to hold market capitalization values

gm.reset_index(level=0, inplace = True)
gm['cap'] = 0   #placeholder to hold market capitalization values


# Calculate market cap for tesla for all years
for i, year in enumerate(tesla['Year']):
    # Retrieve the shares for the year
    shares = tesla_shares.get(year)
    
    # Update the cap column to shares times the price
    tesla.loc[i, 'cap'] = shares * tesla.loc[i, 'Adj. Close']

# Calculate market cap for gm for all years
for i, year in enumerate(gm['Year']):
    # Retrieve the shares for the year
    shares = gm_shares.get(year)
    
    # Update the cap column to shares times the price
    gm.loc[i, 'cap'] = shares * gm.loc[i, 'Adj. Close']

#%% -  Merging - join datasets on a shared column - date 
#We have stock prices for two different companies on the same dates
#Hence join the data on the date column. 

# Merge the two datasets
#We perform an ‘inner’ merge to save only Date entries that are present in both dataframes. 
cars = gm.merge(tesla, how='inner', on='Date')

#After merging, we rename the columns so we know which one goes with which car company.
cars.rename(columns={'cap_x': 'gm_cap', 'cap_y': 'tesla_cap'}, inplace=True)

# Select only the relevant columns
cars = cars.loc[:, ['Date', 'gm_cap', 'tesla_cap']]

# Divide to get market cap in billions of dollars
cars['gm_cap'] = cars['gm_cap'] / 1e9
cars['tesla_cap'] = cars['tesla_cap'] / 1e9

cars.head()

#%% - In 2010 GM started off with a market cap about 30 times that of Tesla! 
#Do things stay that way over the entire timeline?

plt.figure(figsize=(10, 8))
plt.plot(cars['Date'], cars['gm_cap'], 'b-', label = 'GM')
plt.plot(cars['Date'], cars['tesla_cap'], 'r-', label = 'TESLA')
plt.xlabel('Date'); plt.ylabel('Market Cap (Billions $)'); plt.title('Market Cap of GM and Tesla')
plt.legend();

#%% - We observe a meteoric rise for Tesla and a minor increase for GM
#Tesla even surpasses GM in value during 2017
import numpy as np

# Find the first and last time Tesla was valued higher than GM
first_date = cars.loc[np.min(list(np.where(cars['tesla_cap'] > cars['gm_cap'])[0])), 'Date']
last_date = cars.loc[np.max(list(np.where(cars['tesla_cap'] > cars['gm_cap'])[0])), 'Date']

print("Tesla was valued higher than GM from {} to {}.".format(first_date.date(), last_date.date()))

#%% - Modeling with Prophet
#Facebook Prophet - designed for analyzing time series with daily observations 
#that display patterns on different time scales. 
#has advanced capabilities for modeling the effects of holidays on a time-series and 
#implementing custom changepoints
import fbprophet

#We rename the columns in our data to the correct format. 
#The Date column must be called ‘ds’ and the value column we want to predict ‘y’. 
#We then create prophet models and fit them to the data

# Prophet requires columns ds (Date) and y (value)
gm = gm.rename(columns={'Date': 'ds', 'cap': 'y'})
tesla = tesla.rename(columns={'Date': 'ds', 'cap': 'y'})

# Put market cap in billions
gm['y'] = gm['y'] / 1e9
tesla['y'] = tesla['y'] / 1e9

# Make the prophet model and fit on the data
gm_prophet = fbprophet.Prophet(changepoint_prior_scale=0.15)
gm_prophet.fit(gm)

tesla_prophet = fbprophet.Prophet(changepoint_prior_scale=0.15)
tesla_prophet.fit(tesla)

#When creating the prophet models, I set the changepoint prior to 0.15, 
#up from the default value of 0.05. 
#This hyperparameter is used to control how sensitive the trend is to changes, 
#higher value means more sensitive
#This value is used to combat one of the most fundamental trade-offs in machine learning: bias vs. variance.

#If we fit too closely to our training data (overfitting), 
#we have too much variance and our model will not be able to generalize well to new data. 
#On the other hand, if our model does not capture the trends in our training data 
#it is underfitting and has too much bias. 
#When a model is underfitting, increasing the changepoint prior allows more flexibility for the model to fit the data, and 
#if the model is overfitting, decreasing the prior limits the amount of flexibility. 
#The effect of the changepoint prior scale can be illustrated by graphing predictions made with a range of values:

#To make forecasts, we need to create a future dataframe. 
#We specify the number of future periods to predict (two years) and 
#the frequency of predictions (daily). 
#We then make predictions with the prophet model we created and the future dataframe:

# Make a future dataframe for 2 years
gm_forecast = gm_prophet.make_future_dataframe(periods=365 * 2, freq='D')
tesla_forecast = tesla_prophet.make_future_dataframe(periods=365 * 2, freq='D')

# Make predictions
gm_forecast = gm_prophet.predict(gm_forecast)
tesla_forecast = tesla_prophet.predict(tesla_forecast)

#future dataframes contain the estimated market cap of Tesla and GM for the next two years. 
#We can visualize predictions with the prophet plot function.
gm_prophet.plot(gm_forecast, xlabel = 'Date', ylabel = 'Market Cap (billions $)')
plt.title('Market Cap of GM');

#black dots -represent the actual values (notice how they stop at the beginning of 2018), 
#blue line - forecasted values, and 
#light blue shaded region - uncertainty (always a critical part of any prediction). 
#The region of uncertainty increases the further out in the future the prediction is made because 
#initial uncertainty propagates and grows over time. 
#This is observed in weather forecasts which get less accurate the further out in time they are made.

#%% - Effect of Changepoint Prior Scale
# Try 6 different changepoints
for changepoint in [0.001, 0.05, 0.1, 0.15, 0.35, 0.5]:
    model = fbprophet.Prophet(daily_seasonality=False, changepoint_prior_scale=changepoint)
    model.fit(tesla)
    
    future = model.make_future_dataframe(periods=365, freq='D')
    future = model.predict(future)
    
    tesla[changepoint] = future['yhat']
    print 'changepoint', changepoint, " done"

# Create the plot
plt.figure(figsize=(10, 8))

# Actual observations
plt.plot(tesla['ds'], tesla['y'], 'ko', label = 'Observations')
colors = {0.001: 'darkviolet', 0.05: 'b', 0.1: 'grey', 0.15: 'g', 0.35: 'orangered', 0.5: 'gold'}

# Plot each of the changepoint predictions
for changepoint in [0.001, 0.05, 0.1, 0.15, 0.35, 0.5]:
    plt.plot(tesla['ds'], tesla[changepoint], color = colors[changepoint], label = '%.3f prior scale' % changepoint)
    
plt.legend(prop={'size': 14})
plt.xlabel('Date'); plt.ylabel('Market Cap (billions $)'); plt.title('Effect of Changepoint Prior Scale');


#%% - Comparison of changepoints and Google Search Trends for Tesla over a time range 
#to see if the changes line up
#plot the changepoints (vertical lines) and search trends on the same graph

# Load in the data 
tesla_search = pd.read_csv('tesla_search_terms.csv')

# Convert month to a datetime
tesla_search['Month'] = pd.to_datetime(tesla_search['Week'])
tesla_changepoints = [str(date) for date in tesla_prophet.changepoints]

# Plot the search frequency
plt.plot(tesla_search['Month'], tesla_search['Search'], label = 'Searches')

# Plot the changepoints
plt.vlines(tesla_changepoints, ymin = 0, ymax= 100, colors = 'r', linewidth=0.6, linestyles = 'dashed', label = 'Changepoints')

# Formatting of plot
plt.grid('off'); plt.ylabel('Relative Search Freq'); plt.legend()
plt.title('Tesla Search Terms and Changepoints');

#We can also inspect changepoints identified by the model. 
#Again, changepoints represent when the time series growth rate significantly changes 
#(goes from increasing to decreasing for example).

#%% - Some of the changepoints in the market value of Tesla align with changes in frequency of Tesla searches, but not all of them. From this, I would say that relative Google search frequency is not a great indicator of stock changes.

#We need to figure out when the market capitalization of Tesla will surpass that of GM 
#We have both predictions for the next two years 
#So we can plot both companies on the same graph after merging the dataframes. 
#Before merging, we rename the columns to keep track of the data.

gm_names = ['gm_%s' % column for column in gm_forecast.columns]
tesla_names = ['tesla_%s' % column for column in tesla_forecast.columns]

# Dataframes to merge
merge_gm_forecast = gm_forecast.copy()
merge_tesla_forecast = tesla_forecast.copy()

# Rename the columns
merge_gm_forecast.columns = gm_names
merge_tesla_forecast.columns = tesla_names

# Merge the two datasets
forecast = pd.merge(merge_gm_forecast, merge_tesla_forecast, how = 'inner', left_on = 'gm_ds', right_on = 'tesla_ds')

# Rename date column
forecast = forecast.rename(columns={'gm_ds': 'Date'}).drop('tesla_ds', axis=1)

ax = forecast.plot(x='Date',y='tesla_yhat')
forecast.plot('Date','gm_yhat', color='722', ax=ax)

#The model thinks the brief surpassing of GM by Tesla in 2017 was just noise, and 
#it is not until early 2018 that Tesla beats out GM for good in the forecast. 
overtake_date = min(forecast.loc[forecast['tesla_yhat'] > forecast['gm_yhat'], 'Date'])
print('Tesla overtakes GM on {}'.format(overtake_date))

#%% - When making the above graph, we left out the most important part of a forecast: the uncertainty
#We can use matplotlib (see notebook) to show the regions of doubt:

#Forecast with Uncertainty Bounds
# Only keep years 2011 onwards and from before 2020
forecast = forecast[forecast['Date'] > '2010-12-31']
forecast = forecast[forecast['Date'] < '2020-01-01']

# Create subplots to set figure size
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# Plot estimate
ax.plot(forecast['Date'], forecast['gm_yhat'], label = 'gm prediction')

# Plot uncertainty values
ax.fill_between(forecast['Date'].dt.to_pydatetime(), forecast['gm_yhat_upper'], forecast['gm_yhat_lower'], alpha=0.6, edgecolor = 'k')

# Plot estimate and uncertainty for tesla
ax.plot(forecast['Date'], forecast['tesla_yhat'], 'r', label = 'tesla prediction')
ax.fill_between(forecast['Date'].dt.to_pydatetime(), forecast['tesla_yhat_upper'], forecast['tesla_yhat_lower'], alpha=0.6, edgecolor = 'k')
plt.legend()
plt.xlabel('Date'); plt.ylabel('Billions $'); plt.title('Market Cap Prediction for GM and Tesla')


#%% - Trends and Patterns
#Last step of market capitalization analysis
#Look at the overall trend and patterns. 
#Prophet allows us to easily visualize the overall trend and the component patterns:

# Plot the trends and patterns
gm_prophet.plot_components(gm_forecast)

#The trend that GM stock is rising and will go on rising. 
#The yearly pattern - suggest GM increases in value at the end of the year with a long slow decline into the summer. 
#We can try to determine if there is a correlation between the yearly market cap and the average monthly sales of GM over the time period.

#Average Sales grouped by months
#Read in the sales data
gm_sales = pd.read_csv('gm_sales.csv')
gm_sales.head(5)

#Melt the sales data and rename columns
gm_sales = gm_sales.melt(id_vars='Year', var_name = 'Month', value_name = 'Sales')
gm_sales.head(8)

# Format the data for plotting
gm_sales = gm_sales[gm_sales['Month'] != 'Total']
gm_sales = gm_sales[gm_sales['Year'] > 2010]
gm_sales['Date'] = ['-'.join([str(year), month]) for year, month in zip(gm_sales['Year'], gm_sales['Month'])]
gm_sales['Date'] = pd.to_datetime(gm_sales['Date'], format = "%Y-%b")
gm_sales.sort_values(by = 'Date', inplace=True)
gm_sales['Month'] = [date.month for date in gm_sales['Date']]

# Plot the sales over the period
plt.plot(gm_sales['Date'], gm_sales['Sales'], 'r')
plt.title('GM Monthly Sales 2011-2017'); plt.ylabel('Sales')



gm_sales_grouped = gm_sales.groupby('Month').mean()
plt.plot(list(range(1, 13)), gm_sales_grouped['Sales'])
plt.xlabel('Month'); plt.ylabel('Sales'); plt.title('GM Average Monthly Sales 2011-2017')

gm_prophet.plot_yearly(); plt.title('GM Yearly Component of Market Cap')