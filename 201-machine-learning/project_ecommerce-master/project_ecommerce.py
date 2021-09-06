"""
Project Ecommerce

An Ecommerce company based in New York City sells clothing online but 
they also have in-store style and clothing advice sessions. 
Customers come in to the store, have sessions/meetings with a personal stylist, 
then they can go home and order either on a mobile app or website 
for the clothes they want. 
The company is trying to decide whether to focus their efforts on their 
mobile app experience or their website. 

#%% - Imports
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

os.chdir("C:\\Amitava\\DevelopmentWorkspaces\\Python\\Canopy\\machine-learning\\project_ecommerce-master")

#%% - Get the Data
"""
Data Source - Ecommerce Customers csv file from the company. 
It has Customer info, suchas Email, Address, and their color Avatar. 
Then it also has numerical value columns:

    Avg. Session Length: Average session of in-store style advice sessions.
    Time on App: Average time spent on App in minutes
    Time on Website: Average time spent on Website in minutes
    Length of Membership: How many years the customer has been a member.

Read in the Ecommerce Customers csv file as a DataFrame.
"""
customers = pd.read_csv('EcommerceCustomers.csv')

#%% - check the head of customers
customers.head()

#%% - check the info of customers
customers.info()

#%% - check the statistics of customers
customers.describe()

#%% - Exploratory Data Analysis
"""
Let's explore the data!

For the rest of the exercise we'll only be using the numerical data of the csv file.

Lets compare the Time on Website and Yearly Amount Spent columns.
"""
sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)

Out[11]:

<seaborn.axisgrid.JointGrid at 0xad1f518>

Do the same but with the Time on App column instead.
In [13]:

sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)

Out[13]:

<seaborn.axisgrid.JointGrid at 0xad1f4a8>

Lets create a jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.
In [14]:

sns.jointplot(x='Time on App',y='Length of Membership',data=customers,kind='hex')

Out[14]:

<seaborn.axisgrid.JointGrid at 0xad1f1d0>

Let's explore these types of relationships across the entire data set.
In [15]:

sns.pairplot(customers)

Out[15]:

<seaborn.axisgrid.PairGrid at 0xb632358>

Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
In [49]:

# Length of Membership

A linear model plot of Yearly Amount Spent vs. Length of Membership.
In [16]:

sns.lmplot(x='Yearly Amount Spent',y='Length of Membership',data=customers)

Out[16]:

<seaborn.axisgrid.FacetGrid at 0xe4c0550>

In [25]:

sns.distplot(customers['Yearly Amount Spent'])

C:\Users\Sachin\Anaconda3\lib\site-packages\statsmodels\nonparametric\kdetools.py:20: VisibleDeprecationWarning: using a non-integer number instead of an integer will result in an error in the future
  y = X[:m/2+1] + np.r_[0,X[m/2+1:],0]*1j

Out[25]:

<matplotlib.axes._subplots.AxesSubplot at 0xd9e7518>

Heatmap of the customers dataframe to check the correlation.
In [27]:

fig = plt.subplots(figsize=(12,8))
sns.heatmap(customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership','Yearly Amount Spent']].corr(),
annot=True,linewidth=0.5)

Out[27]:

<matplotlib.axes._subplots.AxesSubplot at 0xede6278>

Training and Testing Data

Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
In [17]:

customers.columns

Out[17]:

Index(['Email', 'Address', 'Avatar', 'Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership', 'Yearly Amount Spent'],
      dtype='object')

In [19]:

X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]

In [20]:

y = customers['Yearly Amount Spent']

In [21]:

X.head()

Out[21]:
	Avg. Session Length 	Time on App 	Time on Website 	Length of Membership
0 	34.497268 	12.655651 	39.577668 	4.082621
1 	31.926272 	11.109461 	37.268959 	2.664034
2 	33.000915 	11.330278 	37.110597 	4.104543
3 	34.305557 	13.717514 	36.721283 	3.120179
4 	33.330673 	12.795189 	37.536653 	4.446308
In [22]:

y.head()

Out[22]:

0    587.951054
1    392.204933
2    487.547505
3    581.852344
4    599.406092
Name: Yearly Amount Spent, dtype: float64

Lets split the data into training and testing sets.
In [28]:

from sklearn.model_selection import train_test_split

In [31]:

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=101)

Training the Model

Now its time to train our model on our training data!

Lets Import LinearRegression from sklearn.linear_model
In [32]:

from sklearn.linear_model import LinearRegression

Lets Create an instance of a LinearRegression() model named lm.
In [33]:

lm = LinearRegression()

Now Train/fit lm on the training data.
In [34]:

lm.fit(X_train,y_train)

Out[34]:

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

Lets check the coefficients of the model
In [35]:

lm.coef_

Out[35]:

array([ 25.98154972,  38.59015875,   0.19040528,  61.27909654])

In [36]:

cdf = pd.DataFrame(lm.coef_,X_train.columns,columns=['Coeff'])

In [37]:

cdf

Out[37]:
	Coeff
Avg. Session Length 	25.981550
Time on App 	38.590159
Time on Website 	0.190405
Length of Membership 	61.279097
Predicting Test Data

Now that we have fit our model, let's evaluate its performance by predicting off the test values!

Will use lm.predict() to predict off the X_test set of the data.
In [39]:

predictions = lm.predict(X_test)

In [40]:

predictions

Out[40]:

array([ 456.44186104,  402.72005312,  409.2531539 ,  591.4310343 ,
        590.01437275,  548.82396607,  577.59737969,  715.44428115,
        473.7893446 ,  545.9211364 ,  337.8580314 ,  500.38506697,
        552.93478041,  409.6038964 ,  765.52590754,  545.83973731,
        693.25969124,  507.32416226,  573.10533175,  573.2076631 ,
        397.44989709,  555.0985107 ,  458.19868141,  482.66899911,
        559.2655959 ,  413.00946082,  532.25727408,  377.65464817,
        535.0209653 ,  447.80070905,  595.54339577,  667.14347072,
        511.96042791,  573.30433971,  505.02260887,  565.30254655,
        460.38785393,  449.74727868,  422.87193429,  456.55615271,
        598.10493696,  449.64517443,  615.34948995,  511.88078685,
        504.37568058,  515.95249276,  568.64597718,  551.61444684,
        356.5552241 ,  464.9759817 ,  481.66007708,  534.2220025 ,
        256.28674001,  505.30810714,  520.01844434,  315.0298707 ,
        501.98080155,  387.03842642,  472.97419543,  432.8704675 ,
        539.79082198,  590.03070739,  752.86997652,  558.27858232,
        523.71988382,  431.77690078,  425.38411902,  518.75571466,
        641.9667215 ,  481.84855126,  549.69830187,  380.93738919,
        555.18178277,  403.43054276,  472.52458887,  501.82927633,
        473.5561656 ,  456.76720365,  554.74980563,  702.96835044,
        534.68884588,  619.18843136,  500.11974127,  559.43899225,
        574.8730604 ,  505.09183544,  529.9537559 ,  479.20749452,
        424.78407899,  452.20986599,  525.74178343,  556.60674724,
        425.7142882 ,  588.8473985 ,  490.77053065,  562.56866231,
        495.75782933,  445.17937217,  456.64011682,  537.98437395,
        367.06451757,  421.12767301,  551.59651363,  528.26019754,
        493.47639211,  495.28105313,  519.81827269,  461.15666582,
        528.8711677 ,  442.89818166,  543.20201646,  350.07871481,
        401.49148567,  606.87291134,  577.04816561,  524.50431281,
        554.11225704,  507.93347015,  505.35674292,  371.65146821,
        342.37232987,  634.43998975,  523.46931378,  532.7831345 ,
        574.59948331,  435.57455636,  599.92586678,  487.24017405,
        457.66383406,  425.25959495,  331.81731213,  443.70458331,
        563.47279005,  466.14764208,  463.51837671,  381.29445432,
        411.88795623,  473.48087683,  573.31745784,  417.55430913,
        543.50149858,  547.81091537,  547.62977348,  450.99057409,
        561.50896321,  478.30076589,  484.41029555,  457.59099941,
        411.52657592,  375.47900638])

Scatterplot of the real test values versus the predicted values.
In [41]:

plt.scatter(y_test,predictions)
plt.title("Actual Vs Predicted Yearly Amount Spent")
plt.xlabel("Actual Yearly Amount Spent ")
plt.ylabel("Predicted Yearly Amount Spent")

Out[41]:

<matplotlib.text.Text at 0xed69e48>

Evaluating the Model

Let's evaluate our model performance by calculating the residual sum of squares and the explained variance score (R^2).

Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error.
In [42]:

from sklearn import metrics

In [52]:

# Mean Absolute Error
metrics.mean_absolute_error(y_test,predictions)

Out[52]:

7.228148653430817

In [53]:

# Mean Squared Error
metrics.mean_squared_error(y_test,predictions)

Out[53]:

79.813051650974373

In [54]:

# Root Mean Squared Error
np.sqrt(metrics.mean_squared_error(y_test,predictions))

Out[54]:

8.9338150669786298

In [55]:

# Variance score (R^2)
metrics.explained_variance_score(y_test,predictions)

Out[55]:

0.98907712318896068

Residuals

We have a very good model with a good fit. Let's quickly explore the residuals to make sure everything was okay with our data.

Plot a histogram of the residuals and make sure it looks normally distributed.
In [50]:

sns.distplot((y_test-predictions),bins=50)

C:\Users\Sachin\Anaconda3\lib\site-packages\statsmodels\nonparametric\kdetools.py:20: VisibleDeprecationWarning: using a non-integer number instead of an integer will result in an error in the future
  y = X[:m/2+1] + np.r_[0,X[m/2+1:],0]*1j

Out[50]:

<matplotlib.axes._subplots.AxesSubplot at 0xef05828>

Conclusion

We still want to figure out the answer to the original question, do we focus our efforst on mobile app or website development? Or maybe that doesn't even really matter, and Membership Time is what is really important. Let's see if we can interpret the coefficients at all to get an idea.
In [47]:

cdf = pd.DataFrame(lm.coef_,X_train.columns,columns=['Coefficient'])

In [48]:

cdf

Out[48]:
	Coefficient
Avg. Session Length 	25.981550
Time on App 	38.590159
Time on Website 	0.190405
Length of Membership 	61.279097

How can you interpret these coefficients?

Interpreting the coefficients:

    Holding all other features fixed, a 1 unit increase in Avg. Session Length is associated with an increase of 25.98 total dollars spent.
    Holding all other features fixed, a 1 unit increase in Time on App is associated with an increase of 38.59 total dollars spent.
    Holding all other features fixed, a 1 unit increase in Time on Website is associated with an increase of 0.19 total dollars spent.
    Holding all other features fixed, a 1 unit increase in Length of Membership is associated with an increase of 61.27 total dollars spent.

Do you think the company should focus more on their mobile app or on their website?

Either develop the Website to catch up to the performance of the mobile app, or develop the app more since that is what is working better. We should explore the relationship between Length of Membership and the App or the Website before coming to a conclusion!
