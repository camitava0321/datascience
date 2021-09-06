from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.data)
print(digits.target)
print(digits.images[0])

from sklearn import svm
classifier = svm.SVC(gamma=0.001,C=100)
classifier.fit(digits.data[:-1],digits.target[:-1])
classifier.predict(digits.data[-1:])

import pickle
s=pickle.dumps(classifier)

classifier2 = pickle.loads(s)
classifier2.predict(digits.data[0:1])

#%% - Multilinear Regression
X=np.random.randint(20,size=(10,2))
Y=X.dot([1, 3])+1 + np.random.randn(X.shape[0])*20
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X,Y)
print (lr.coef_)

#%% - Polynomial Regression
#We can extend this to include polynomial regression by using the PolynomialFeatures in the preprocessing sub-module. 
#To keep it simple, let’s go back to our one-dimensional example. 
#First, let’s create some synthetic data,
from sklearn.preprocessing import PolynomialFeatures
X = np.arange(10).reshape(-1,1) # create some data
Y = X+X**2+X**3+ np.random.randn(*X.shape)*80
#Next, we have to create a transformation from X to a polynomial of X,
qfit = PolynomialFeatures(degree=2) # quadratic
Xq = qfit.fit_transform(X)
print (Xq)

lr=LinearRegression() # create linear model
qr=LinearRegression() # create quadratic model
lr.fit(X,Y) # fit linear model
qr.fit(Xq,Y) # fit quadratic model

xi = np.arange(10).reshape(-1,1) # create some data
lp = lr.predict(xi)
qp = qr.predict(qfit.fit_transform(xi))


#%% - Decision Trees
from sklearn import tree
clf = tree.DecisionTreeClassifier()

#Some example data,
import numpy as np
M=np.fromfunction(lambda i,j:j>=2,(4,4)).astype(int)
#fromfunction creates Numpy arrays using the indicies as inputs to a function whose value is the corresponding array entry.
print (M)

#We want to classify the elements of the matrix based on their respective positions in the matrix. 
#i.e., classify as 0 for any positions in the first two columns of the matrix, and classify 1 otherwise.
#The values of the array are the labels for the training set and 
#the indicies of those values are the elements of x. 
#Specifically, the training set has X = {(i, j )} and Y = {0, 1} 
#Now, let’s extract those elements and construct the training set.
i,j = np.where(M==0)
x=np.vstack([i,j]).T # build nsamp by nfeatures
y = j.reshape(-1,1)*0 # 0 elements
print (x)
print (y)

#Thus, the elements of x are the two-dimensional indicies of the values of y. 
#For example, M[x[0,0],x[0,1]] = y[0,0]. 
#Likewise, to complete the training set, we just need to stack the rest of the data to cover all the cases,
i,j = np.where(M==1)
x=np.vstack([np.vstack([i,j]).T,x ]) # build nsamp x nfeatures
y=np.vstack([j.reshape(-1,1)*0+1,y]) # 1 elements

#With all that established, all we have to do is train the classifer,
clf.fit(x,y)

#To evaluate how the classifer performed, we can report the score,
clf.score(x,y)

#Modify the matrix M
M[1,0]=1 # put in different class
print (M) # now contaminated

#recalculate
i,j = np.where(M==0)
x=np.vstack([i,j]).T
y = j.reshape(-1,1)*0
i,j = np.where(M==1)
x=np.vstack([np.vstack([i,j]).T,x])
y = np.vstack([j.reshape(-1,1)*0+1,y])
clf.fit(x,y)

y[x[:,1]>1.5] # first node on the right
#This obviously has a zero Gini coefficient. 
#Likewise, the node on the left contains the following,
y[x[:,1]<=1.5] # first node on the left

#The logical_and in Numpy provides element-wise logical conjuction. 
#It is not possible to accomplish this with something like 0.5 < x[:, 1] <= 1.5 because of the way Python parses this syntax.
np.logical_and(x[:,1]<=1.5,x[:,1]>0.5)
y[np.logical_and(x[:,1]<=1.5,x[:,1]>0.5)]
