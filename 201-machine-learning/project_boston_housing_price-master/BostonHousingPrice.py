# coding: utf-8
# Predict the housing price in Boston
# The data set  contains information about the housing values in suburbs of Boston.
# The data set is available in sklearn Python module

#%% - imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:

get_ipython().magic(u'matplotlib inline')


# In[7]:

from sklearn.datasets import load_boston


# In[8]:

bt = load_boston()


# In[10]:

# Data is in the form of a dictionary
bt.keys()


# In[13]:

print(bt.DESCR)


# In[14]:

bt.data.shape


# In[19]:

bt.target.shape


# In[20]:

print(bt.feature_names)


# In[22]:

# Lets create the dataframe for the boston data
bt_df = pd.DataFrame(bt.data)


# In[23]:

bt_df.head()


# In[24]:

# Change the column names with feature names
bt_df.columns = bt.feature_names


# In[25]:

bt_df.head()


# In[26]:

# Since target is the y label(or the target house price),Lets add the target to boston dataframe
bt_df['PRICE'] = bt.target


# In[27]:

bt_df.head()


# In[28]:

bt_df.info()


# In[29]:

bt_df.describe()

# In[30]:
sns.pairplot(bt_df)

# In[32]:

sns.distplot(bt_df['PRICE'])


# In[41]:

fig = plt.subplots(figsize=(12,10)) 
sns.heatmap(bt_df.corr(),annot=True,linewidths=.5)


# In[43]:

bt_df.columns


# In[45]:

X = bt_df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']]


# In[46]:

y = bt_df['PRICE']


# In[47]:

X.head()


# In[48]:

y.head()


# In[49]:

from sklearn.model_selection import train_test_split


# In[50]:

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4)


# In[52]:

y_train.count()


# In[53]:

y_test.count()


# In[54]:

from sklearn.linear_model import LinearRegression


# In[55]:

lm = LinearRegression()


# In[56]:

lm.fit(X_train,y_train)


# In[57]:

lm.intercept_


# In[58]:

lm.coef_


# In[59]:

cdf = pd.DataFrame(lm.coef_,X_train.columns,columns=['Coeff'])


# In[60]:

cdf


# In[61]:

predictions = lm.predict(X_test)


# In[62]:

predictions


# In[69]:

plt.scatter(y_test,predictions)
plt.title("Actual Vs Predicted Prices")
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")


# In[64]:

sns.distplot(y_test - predictions)


# In[65]:

from sklearn import metrics


# In[66]:

metrics.mean_absolute_error(y_test,predictions)


# In[67]:

metrics.mean_squared_error(y_test,predictions)


# In[68]:

np.sqrt(metrics.mean_squared_error(y_test,predictions))

