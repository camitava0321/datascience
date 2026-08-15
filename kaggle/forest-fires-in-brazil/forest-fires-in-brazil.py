# -*- coding: utf-8 -*-
"""
@Amitava Chakraborty
"""
"""
Forest Fires are a serious problem in Brazil. Understanding the frequency of forest fires in a time series 
can help to take action to prevent them. Being able to pin-point where and when that frequency is most 
observed should give some clarity on what is the scope we are looking at.

Data Source
A small dataset - around 6,500 observations and 5 features - a mix between categorical and numeric values.
"""
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
import plotly.express as px
import plotly
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


sns.set_style('whitegrid')

#%% - Read Data File 
original_df=pd.read_csv('amazon.csv', encoding='latin1')

#Good Practice : Copy the initial dataframe
df = original_df.copy()
nRow, nCol = df.shape
print(f'There are {nRow} rows and {nCol} columns')
#Length of the dataset
print(len(df))

#examining head of the dataset
print(df.head(10))

#%% - Understanding Data - Preliminary Exploratory Analysis with data corrections

print(df.info())
#'date' is not datetime like - change it to a datetime like object
df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')
original_df.info()

df.describe()

#Good Practice : Is there are any nulls we are dealing with (missing data)
print (df.isna().sum())

#checking unique values in the month column
df.month.unique()
#Note: months in the data are not in English. 
#So, we need to change months into English for global viewers
#creating a dictionary with translations of months
month_map={'Janeiro': 'January', 'Fevereiro': 'February', 'Março': 'March', 'Abril': 'April', 'Maio': 'May',
           'Junho': 'June', 'Julho': 'July', 'Agosto': 'August', 'Setembro': 'September', 'Outubro': 'October',
          'Novembro': 'November', 'Dezembro': 'December'}
#mapping translated months
df['month']=df['month'].map(month_map)
#checking the month column for the second time after the changes were made
df.month.unique()
months={'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 
        'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
df['monthNumber'] = df.month.map(months)

#Good Practice : No. of obs. with "date" year not matching with "year" variable
df['date'].dt.day.nunique()
print('No. of obs. with "date" year not matching with "year" variable (out of {} obs.) = {}'.\
      format(df.shape[0], sum(df['year'] != df['date'].dt.year)))
#we are already given the year column, however for good practice we can also extract it from the date one
df['Year']=pd.DatetimeIndex(df['date']).year
#cheking unique years in new created column 
df.Year.unique()

#We won't use old year column and date column as they serve no significant purpose anymore 
df.drop(columns=['date', 'year'], axis=1, inplace=True)
#changing order of columns for preffered format
df=df[['state','number','month','monthNumber','Year']]
#changing names of columns for preffered format
#df.rename(columns={'state': 'State', 'number': 'Fire_Number', 'month': 'Month'}, inplace=True)
df.rename(columns={'number': 'numOfFires'}, inplace=True)
#checking changes made

#Good Practice : Remove Duplicates
print('No. of duplicate obs. = {}'.format(df.duplicated().sum()))
df.loc[df.duplicated(), ].head()
df.loc[(df['Year'] == 2017) & (df['state'] == 'Alagoas') & (df['month'] == 'January'), ]
df.loc[(df['Year'] == 1998) & (df['state'] == 'Mato Grosso') & (df['month'] == 'January'), ]

#So drop duplicate observations from the data set.
df.drop_duplicates(inplace = True)
df.reset_index(inplace = True, drop = True)
print('No. of duplicate obs. = {}'.format(df.duplicated().sum()))

print('No. of obs. with -ve values in number field = {}'.format(df['numOfFires'].lt(0).sum()))

#Visualization - a simple histogram
plt.figure(figsize = (15,8))
df.numOfFires.hist()
plt.xlabel('Nos. of Fires')
plt.ylabel('Freqncy of occurence')
plt.show()

#How many unique states?
df.state.unique()
print('Nos. of unique states = {}'.format(df['state'].nunique()))

#cheking the numeric percentile distribution for the fires reported
df.numOfFires.describe()
#Interesting observation - 50% percentile from all observations (across all months, years and regions) 
#sums up to 24 fire reports.

#But, how many fires were reported in 20 years?
df.numOfFires.sum()

#%% - Direct Analysis - The quick and dirty visualization
#Statewise num of fires for all years & months
df.groupby('state')['numOfFires'].sum().sort_values(ascending=False)

plt.figure(figsize=(20,5))
sns.barplot(x=df['state'], y=df['numOfFires'], estimator=sum)
plt.xticks(fontsize=11, rotation=65)
sns.palplot(sns.color_palette("hls", 8))
#Yearwise num of fires for all states & months
plt.figure(figsize=(16,5))
sns.barplot(x=df['Year'], y=df['numOfFires'], estimator=sum)
plt.xticks(fontsize=11, rotation=90)

#State vs Year Heatmap
heat = df.pivot_table(index='Year', columns='state', values='numOfFires', aggfunc=sum)
plt.figure(figsize=(16,11))
sns.heatmap(heat)

#Month Number vs. State Heatmap
df.pivot_table(values='numOfFires',index='state', columns='monthNumber', aggfunc=sum)
plt.figure(figsize=(16,11))
sns.heatmap(df.pivot_table(values='numOfFires',index='state', columns='monthNumber', aggfunc=sum))

plt.figure(figsize = (15,5))
sns.swarmplot(x= 'Year', y= 'numOfFires', data = df)
plt.show()

#%% - Adding additional data - average temperature in Brazil from web and setting it for each month
avg_temp={1:-3.1, 2:-0.8, 3:4.9, 4:11.4, 5:17, 6:22, 7:24, 8:22.8, 9:19.1, 10:12.7, 11:5.9,12:0.3}
df['temparature'] = df['monthNumber'].map(avg_temp)

#%% - More Visualizations
#Is there is a link between avg. monbthly temperature and number of fires
#It seems that the fires increase as the temperatures increase
fig = plt.figure(figsize = (15,5))
sns.set_style('white')
sns.set_context('notebook', font_scale = 1.2)
month_chart = sns.lineplot(x = 'monthNumber', y = 'numOfFires', color = 'orange',data = df, legend = 'full')
ax2 = month_chart.twinx()
sns.lineplot(x = 'monthNumber', y = 'temparature',ax = ax2, color = 'red',  data = df,  legend = 'full')
month_chart.set(title = 'Relation between the Temperature and Number of Fires in a month', xlabel = 'month', ylabel = 'Count of Fires')
sns.despine(left = True)

#Distribution of Fires acorss months and years
#Size and intensity indicates the number of fires reported
#This graph is just to get a top level view of the pattern of fires 
#Helps us identify data that stand out. For example, fires in the month 2-5 are getting worse by the year
fig = plt.figure(figsize = (15,8))
sns.set_style('dark')
sns.set_context('talk', font_scale = 0.9)
year_month_matrix = sns.heatmap(df.pivot_table(index = 'monthNumber', columns = 'Year',values = 'numOfFires',aggfunc='sum'), cmap = 'Reds')
year_month_matrix.set(title = 'Fire Matrix - Year vs. month')
plt.xticks(rotation=30)
sns.despine()

tmp_df = pd.DataFrame(df.groupby(['state', 'Year'])['state'].count())
tmp_df.rename(index = str, columns = {'state':'count'}, inplace = True)
tmp_df.reset_index(inplace = True)
tmp_df.groupby('state')['Year'].count()
tmp_df.groupby('state')['Year'].count().count()
#Observation: From this we can conclude that we have 20 years of data for Amazon Forest Fire complaints for all 23 states.

tmp_df = pd.DataFrame(df.groupby(['state', 'Year'])['month'].count())
tmp_df.reset_index(inplace = True)
tmp_df.rename(index = str, columns = {'month':'count'}, inplace = True)
tmp_df.loc[tmp_df['count'] < 12, ]
tmp_df.loc[tmp_df['count'] < 12, 'state'].count()
#Observations: Except for year 2017, we have data on Amazon forest fire complaints for all entire year for all 23 states. 
#For year 2017, we have data for 11 months only for these states.

print('No. of obs. with whole values in "number" variable = {}'.format(df['numOfFires'].apply(lambda x : x.is_integer()).sum()))
print('No. of obs. with float values in "number" variable = {}'.format(df['numOfFires'].apply(lambda x : not x.is_integer()).sum()))
df.loc[df['numOfFires'].apply(lambda x : not x.is_integer()), ].head()
# Round "number" values to zero decimal places.
df['numOfFires'] = df['numOfFires'].round()
#%% - Functions
# Distribution graphs (histogram/bar graph) of column data
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()

# Correlation matrix
def plotCorrelationMatrix(df, graphWidth):
    #filename = df.name
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix', fontsize=15)
    plt.show()    

# Scatter and density plots
def plotScatterMatrix(df, plotSize, textSize):
    df = df.select_dtypes(include =[np.number]) # keep only numerical columns
    # Remove rows and columns that would lead to df being singular
    df = df.dropna('columns')
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    columnNames = list(df)
    if len(columnNames) > 10: # reduce the number of columns for matrix inversion of kernel density plots
        columnNames = columnNames[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show()
#%% - Exploring and Visualizing Data
#Exploring the data by analyzing its statistics and 
#visualizing the values of features and correlations between different features. 

#Exploration 1: Distribution graphs (histogram/bar graph) of sampled columns
plotPerColumnDistribution(df, 10, 5)
#Exploration 2: Correlation Matrix of sampled columns
plotCorrelationMatrix(df, 8)
#Scatter and density plots:
plotScatterMatrix(df, 6, 15)

#Maximum number of forestfire recorded in a month. 
df[df['numOfFires'] == df['numOfFires'].max()]

#Exploration 1: Trend of fires beings reported over 20 years.
#creating a list of years we have 
years=list(df.Year.unique())
#creating an empty list, which will be populated later with amount of fires reported
sub_fires_per_year=[]
#using for loop to extract sum of fires reported for each year and append list above
for i in years:
    y=df.loc[df['Year']==i].numOfFires.sum().round(0)
    sub_fires_per_year.append(y)
#creating a dictionary with results     
fire_year_dic={'Year':years,'Total_Fires':sub_fires_per_year}
#creating a new sub dataframe for later plot 
time_plot_1_df=pd.DataFrame(fire_year_dic)
#checking the dataframe
time_plot_1_df.head(5)

#using plotly Scatter 
time_plot_1=go.Figure(go.Scatter(x=time_plot_1_df.Year, y=time_plot_1_df.Total_Fires,
                                 mode='lines+markers', line={'color': 'red'}))
#layout changes
time_plot_1.update_layout(title='Brazil Fires per 1998-2017 Years',
                   xaxis_title='Year',
                   yaxis_title='Fires')
#showing the figure
time_plot_1.show()
#For Spyder
plotly.offline.plot(time_plot_1)
#Hover over the graph to explore the dynamic features of Plotly. 


year_mo_state = df.groupby(by = ['Year','state', 'month']).sum().reset_index()
from matplotlib.pyplot import MaxNLocator, FuncFormatter
plt.figure(figsize=(14,8))
ax = sns.lineplot(x = 'Year', y = 'numOfFires', data = year_mo_state, estimator = 'sum', color = 'orange', lw = 3, 
                  err_style = None)

plt.title('Total Fires in Brazil : 1998 - 2017', fontsize = 18)
plt.xlabel('Year', fontsize = 14)
plt.ylabel('Number of Fires', fontsize = 14)

ax.xaxis.set_major_locator(plt.MaxNLocator(19))
ax.set_xlim(1998, 2017)

ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
#We can definetly see a growth of fires reported throughout 20 years with couple ups and downs. 


#View by months - Number of fires per month
#Initial - quick check
df.groupby(by='month').sum()['numOfFires'].plot(kind='bar')

#There are many more fires occuring in the second half of the year than the first one, 
#especially in the late summer to beginning of autumn - it is expected because the latter part of the year is drier
monthOrder = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 
              'November', 'December']
sns.boxplot(x = 'month', order = monthOrder, 
            y = 'numOfFires', data = year_mo_state)

plt.title('Fires in Brazil by month', fontsize = 18)
plt.xlabel('month', fontsize = 14)
plt.ylabel('Number of Fires', fontsize = 14)

#But which regions (states) contribute the most and generate those spikes and 
#when those reports are most likely to be at its highest.
df.groupby(by='state').sum()['numOfFires'].sort_values(ascending=True).plot(kind='bar')

#Amazon state is most discussed in the media.
#But, if we look more closely to the dataset, 
#Amazon isn't by far the place where most of the fires in Brazil occur. 
#Top 3 states are Mato Grosso (an outlier, with a total sum of wildfires in the analysed period of 96k), 
#followed by Paraiba (52k) and Sao Paulo (51k). Amazon has the 10th place in this ranking
df.groupby(by = 'state')['numOfFires'].sum().sort_values(ascending = False).head(10)

year_mo_state_top_states = df[df['state'].isin(['Amazonas','Mato Grosso','Paraiba','Sao Paulo','Rio'])].groupby(by = ['Year','state', 'month']).sum().reset_index()
ax = sns.lineplot(x = 'Year', y = 'numOfFires', data = year_mo_state_top_states, hue = 'state', 
                  estimator = 'sum', color = 'orange', lw = 3, err_style = None, palette = 'YlGnBu')
plt.title('Total Fires in Amazon : 1998 - 2017', fontsize = 18)
plt.xlabel('Year', fontsize = 14)
plt.ylabel('Number of Fires', fontsize = 14)
ax.xaxis.set_major_locator(plt.MaxNLocator(19))
ax.set_xlim(1998, 2017)
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.xticks(rotation=75)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), prop={'size': 14})


# Visualisation 5 - total fires in 5 top
# Rio, Paraiba, Mato Grosso, Alagoas
df1 = pd.DataFrame(data=df[df['state'] =='Rio'])
df2 = pd.DataFrame(data=df[df['state'] =='Paraiba'])
df3 = pd.DataFrame(data=df[df['state'] =='Mato Grosso'])
df4 = pd.DataFrame(data=df[df['state'] =='Alagoas'])
plt.figure(figsize=(15,8))

df_list = [df1, df2, df3, df4]
df_group = []
for x in df_list:
    x.groupby('Year')['numOfFires'].sum().reset_index()
    df_group.append(x)

for x in df_group:
    sns.lineplot(x='Year', y='numOfFires', data=x, lw=1, label=x['state'].iloc[0])
    plt.title('Fires in top 5 states', fontsize=15)
    plt.xlabel('Year')
    plt.ylabel('Number of fires')
    plt.xticks(np.arange(1997,2017,1), rotation=80)
    plt.xlim(1998,2017)

plt.legend(fontsize=13)

# Visualisation 6 - pivot table
data_pivot = df.pivot_table(values='numOfFires', index='Year', columns='month', aggfunc=np.sum)
data_pivot = data_pivot.loc[:,monthOrder]

plt.figure(figsize=(15,8))
sns.heatmap(data_pivot, linewidths=0.05, vmax=9000, cmap='Oranges', fmt="1.0f", annot=True)
plt.title('Heatmap of number of fires in states in every month in years', fontsize=15)
plt.xlabel('month')
plt.ylabel('Year')

#Mato Grosso is quite disticnt from the other states in terms of wildfires. 
#It is also the only one increasing, while the others have an ~ "white noise" distribution, like that of Amazonas.
#Mato Grosso is Brazil’s third largest state. 
#This state has a small weight of people from total population of Brazil, about 1.5%, but a very strong agricultural industry.
#In the past, the state of Mato Grosso has been one of Brazil’s largest emitters of CO², 
#due to forest fires and deforestation, driven by its strong agriculture based economy.
#However, they reduced the massive deforestation starting 2004. 

#Yearly and state wise ForestFire Calculation and Visualization
pd.crosstab(df['Year'],df['state'],values=df['numOfFires'],aggfunc='sum').plot.bar(stacked=True,figsize=(20, 10))
plt.legend()

#monthly and state wise Forestfire incident Calculation and Visualization
pd.crosstab(df['month'],df['state'],values=df['numOfFires'],aggfunc='sum').plot.bar(stacked=True,figsize=(20, 10))


#We can see that we have sparse data, regarding the number of fires. 
#The standard deviation is very high, so for the next analysis I will be using only the median, 
#beacause using average values could lead to false conclusions.
x = df.groupby(df.Year).numOfFires.median()
ax = plt.figure(figsize=(15,10))
ax = plt.plot(x.index.values,x.values) 
ax = plt.title('Median of number of fires reported')
ax = plt.xlabel('Year')
ax = plt.ylabel('Median')
z = np.polyfit(x.index.values, x.values, 1)
p = np.poly1d(z)
ax = plt.plot(x.index.values,p(x.index.values),"r--")
ax = plt.legend(['Real Data','Trend Line'])


#%%
#putting all available states in the list
states=list(df.state.unique())
#creating empty list for each state that will be later appended
acre_list=[]
alagoas_list=[] 
amapa_list=[] 
amazonas_list=[] 
bahia_list=[] 
ceara_list=[]
distrito_list=[] 
espirito_list=[] 
goias_list=[] 
maranhao_list=[] 
mato_list=[] 
minas_list=[]
para_list=[] 
paraiba_list=[] 
perna_list=[]
piau_list=[]
rio_list=[]
rondonia_list=[]
roraima_list=[]
santa_list=[]
sao_list=[]
sergipe_list=[]
tocantins_list=[]


#breaking down fires reported for each state throughtout 20 years and appending empty lists
for x in states:
    st=x
    for i in years:
        ye=i
        if st=='Acre':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            acre_list.append(y)
        elif st=='Alagoas':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            alagoas_list.append(y)
        elif st=='Amazonas':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            amazonas_list.append(y)
        elif st=='Amapa':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            amapa_list.append(y)
        elif st=='Bahia':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            bahia_list.append(y)
        elif st=='Ceara':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            ceara_list.append(y)
        elif st=='Distrito Federal':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            distrito_list.append(y)
        elif st=='Espirito Santo':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            espirito_list.append(y)
        elif st=='Goias':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            goias_list.append(y)
        elif st=='Maranhao':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            maranhao_list.append(y)
        elif st=='Mato Grosso':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            mato_list.append(y)
        elif st=='Minas Gerais':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            minas_list.append(y)
        elif st=='Pará':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            para_list.append(y)
        elif st=='Paraiba':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            paraiba_list.append(y)
        elif st=='Pernambuco':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            perna_list.append(y)
        elif st=='Piau':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            piau_list.append(y)
        elif st=='Rio':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            rio_list.append(y)
        elif st=='Rondonia':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            rondonia_list.append(y)
        elif st=='Roraima':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            roraima_list.append(y)
        elif st=='Santa Catarina':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            santa_list.append(y)
        elif st=='Sao Paulo':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            sao_list.append(y)
        elif st=='Sergipe':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            sergipe_list.append(y)
        elif st=='Tocantins':
            y=df.loc[(df['state']== st) & (df['Year']== ye)].numOfFires.sum().round(0)
            tocantins_list.append(y)

#with those lists populated, now creating a powerful dataframe
time_plot_2_df=pd.DataFrame(list(zip(years, acre_list, alagoas_list, amapa_list, amazonas_list,
                                     bahia_list, ceara_list, distrito_list, espirito_list,
                                     goias_list, maranhao_list, mato_list, minas_list, para_list,
                                     paraiba_list, perna_list, piau_list, rio_list, rondonia_list,
                                     roraima_list, santa_list, sao_list, sergipe_list, tocantins_list)),
                            columns =['Year', 'Acre', 'Alagoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara',
                                      'Distrito Federal', 'Espirito Santo', 'Goias', 'Maranhao',
                                      'Mato Grosso', 'Minas Gerais', 'Pará', 'Paraiba', 'Pernambuco',
                                      'Piau', 'Rio', 'Rondonia', 'Roraima', 'Santa Catarina',
                                      'Sao Paulo', 'Sergipe', 'Tocantins'])
#checking the dataframe
time_plot_2_df.head(10)

#examining top 10 states with the most fires reported (please igone the year observation, will be removed later)
time_plot_2_df.sum().nlargest(11)
#Now, we know which states (top 10) are generating the most fire reports. 
#Let's visualize...
#creating a dataframe for bar plot visualization
bar_plot_df=pd.DataFrame(time_plot_2_df.sum().nlargest(11))
#reseting index for first column
bar_plot_df=bar_plot_df.reset_index()
#renaming
bar_plot_df.rename(columns={'index':'state', 0:'Reported_Fires'}, inplace=True)
#removing Year observation
bar_plot_df.drop(bar_plot_df[bar_plot_df.state == 'Year'].index, inplace=True)
#checking dataframe
bar_plot_df

#making barplot
bar_plot=px.bar(bar_plot_df, x='state', y='Reported_Fires', color='Reported_Fires',
           labels={'Reported_Fires':'Count of reported fires ', 'state':'states'}, color_continuous_scale='Reds')
#making layout changes
bar_plot.update_layout(xaxis_tickangle=-45, title_text='Top 10 states for Amount of Reported Fires per 1998-2017 Years')
#outputing plot
bar_plot.show()
#For Spyder
plotly.offline.plot(bar_plot)

#%%
#preparing a figure that will be populated 
time_plot_2 = go.Figure()
#adding individual graphs to the figure
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Mato Grosso'],
                                 mode='lines+markers', name='Mato Grosso', line={'color': 'red'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Paraiba'],
                                 mode='lines+markers', name='Paraiba', line={'color': 'yellow'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Sao Paulo'],
                                 mode='lines+markers', name='Sao Paulo', line={'color': 'green'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Rio'],
                                 mode='lines+markers', name='Rio', line={'color': 'blue'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Bahia'],
                                 mode='lines+markers', name='Bahia', line={'color': 'pink'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Piau'],
                                 mode='lines+markers', name='Piau', line={'color': 'brown'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Goias'],
                                 mode='lines+markers', name='Goias', line={'color': 'grey'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Minas Gerais'],
                                 mode='lines+markers', name='Minas Gerais', line={'color': 'purple'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Tocantins'],
                                 mode='lines+markers', name='Tocantins', line={'color': 'orange'}))
time_plot_2.add_trace(go.Scatter(x=time_plot_2_df.Year, y=time_plot_2_df['Amazonas'],
                                 mode='lines+markers', name='Amazonas', line={'color': 'gold'}))
#making changes to layout
time_plot_2.update_layout(title='Brazil Fires in Top-10 (frequent) regions per 1998-2017 Years',
                   xaxis_title='Year',
                   yaxis_title='Fires')
#outputing plot
time_plot_2.show()
#For Spyder
plotly.offline.plot(time_plot_2)

#%%
#creating subdataframe for visualizing this states geographically
geo_plot_df=pd.DataFrame(time_plot_2_df.sum().nlargest(11))
#formatting new dataframe
geo_plot_df.rename(columns={0:'Count'}, inplace=True)
geo_plot_df.reset_index(inplace=True)
geo_plot_df.rename(columns={'index':'state'}, inplace=True)
geo_plot_df.drop(geo_plot_df.index[5], inplace=True)
#cheking new sub dataframe 
geo_plot_df

#taking my time and adding all coordinates (latitude and longitude) for this top 10 states
lat=[-16.350000, -22.15847, -23.533773, -22.908333, -11.409874, -21.5089, -16.328547,
     -19.841644, -21.175, -3.416843]
long=[-56.666668, -43.29321, -46.625290, -43.196388, -41.280857, -43.3228, -48.953403,
     -43.986511, -43.01778, -65.856064]
#adding new coordinates as columns to subdataframe above
geo_plot_df['Lat']=lat
geo_plot_df['Long']=long
#checking changes in subdataframe for geo visualization
geo_plot_df

#using scatter geo with above created subdataframe
fig = px.scatter_geo(data_frame=geo_plot_df, scope='south america',lat='Lat',lon='Long',
                     size='Count', color='state', projection='hammer')
fig.update_layout(
        title_text = '1998-2017 Top-10 states in Brazil with reported fires')
fig.show()
#For Spyder
plotly.offline.plot(fig)

#%%
#isolating the hottest months by season
month_array_summer=['June','July','August']
month_array_fall=['September','October','November']
#leaving data only for hottest months
box_plot_df_summer=df.loc[df['month'].isin(month_array_summer)]
box_plot_df_fall=df.loc[df['month'].isin(month_array_fall)]
#visualizing reports
box_plot=go.Figure()

box_plot.add_trace(go.Box(y=box_plot_df_summer.numOfFires, x=box_plot_df_summer.month,
                          name='Summer', marker_color='#3D9970',
                          boxpoints='all', jitter=0.5, whiskerwidth=0.2,
                          marker_size=2,line_width=2))
box_plot.add_trace(go.Box(y=box_plot_df_fall.numOfFires, x=box_plot_df_fall.month,
                         name='Fall', marker_color='#FF851B',
                         boxpoints='all', jitter=0.5, whiskerwidth=0.2,
                          marker_size=2,line_width=2))

box_plot.update_layout(
        title_text = 'Distribution of Fire Reports from 1998-2017 in the hottest months')
box_plot.show()
#For Spyder
plotly.offline.plot(time_plot_2)

#Final thoughts on the dataset and Plotly
#Plotly was very fun to use with this dataset. 
#With powerful and dynamic visualizations we discovered couple very interesting means. 
#We found that there is unfortunately a positive trend on fire reports among this 20 years - 
#which, only highlights all the issues and help needed for preserving tropical forests. 
#We found that state like Mato Grosso is an extreme observation and combined with Amazonas region 
#would really raise a red flag on how much frequency it generates; 
#also, with the rest of the states how there is no decline, 
#but a steady distribution of fire reports coming year after year! 
#We imputed approximate coordinates for regions given and visualized it on the 
#geographical scale to identify clusters of regions. 
#Also, we looked at statistical distributions among hottest months in Brazil and 
#were able to pin-point the ones with highest medians. 
#Overall, this dataset could definitely have more features so that more information 
#could be analyzed and correlations identified - which would result in doing powerful predictions and machine learning.

#%% - Prediction
#We can see a that the reported number of fires increased in a very fast rhythm until 2003, then it started to fall. 
#But since 2008, this number started to increase again.
#Let's see if can predict the number of fires in the incoming years using the data available.
#Analysing the data, seems reasonable to fit it into a third degree polynomial function.
training_df = df.groupby(['Year'], as_index=False).sum() 
poly = np.polyfit(training_df['Year'],training_df['numOfFires'],3)
z = np.poly1d(poly)
    
anos = np.linspace(1998, 2017, 20)

plt.figure(figsize=[12,7])
plt.plot(anos, training_df['numOfFires'], '-', label='Real data') 
plt.plot(anos,z(anos), '--', label='Fitted curve')
plt.xlim([1998, 2017])
plt.ylim([17000, 48000])
plt.title('Fitting the real data into a curve (all registered years)')
plt.legend()
plt.show()

#Predicting the number of fires:
import math
for i in range(2019,2024,1):
    print(i, '->', math.trunc(z(i)))

#It is not very optimistic - a third degree polynomial seems to be a bit aggresive, 
#due to the earlier years of the data set and it fast increase. 
#So, let us use only the data after 2006, and fit it into a first degree polynomial function.
new_model = training_df[training_df['Year']>2006]
poly = np.polyfit(new_model['Year'],new_model['numOfFires'],1)
z = np.poly1d(poly)
    
anos = np.linspace(2007, 2017, 11)

plt.figure(figsize=[12,7])
plt.plot(anos, new_model['numOfFires'], '-', label='Real data') 
plt.plot(anos,z(anos), '--', label='Fitted curve')
plt.xlim([2007, 2017])
plt.ylim([17000, 48000])
plt.title('Fitting the real data into a curve (years>2006)')
plt.legend()
plt.show()

#The new prediction:
for i in range(2019,2024,1):
    print(i, '->', math.trunc(z(i)))
#Not so aggressive - since the beginning of 2019 the number of fires in the amazon rainforest has increased again. 
#Therefore, our model to predict the number of fires in the incoming years seems to be correct, unfortunately.

A='1234567'
A[1::2]
