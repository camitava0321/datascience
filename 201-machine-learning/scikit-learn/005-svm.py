# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:36:20 2019

@author: AMITAVA

Support vector machines (SVMs) are a particularly powerful and flexible class of supervised algorithms 
for both classification and regression. 
In this section, we will develop the intuition behind support vector machines and 
their use in classification problems.
"""

#The standard imports:
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# use seaborn plotting defaults
import seaborn as sns; sns.set()

#discriminative classification: 
#rather than modeling each class, 
#we simply find a line or curve (in two dimensions) or manifold (in multiple dimensions) 
#that divides the classes from each other.
#Example : 
#Simple classification task - two classes of points are well separated:
training_data = np.array([[40.0, 2088139.0],
  [68.0, 927650.0],
  [71.0, 1133323.0],
  [68.0, 859230.0],
  [75.0, 1668323.0],
  [70.0, 104659.0],
  [88.0, 2032140.0],
  [60.0, 1200924.0], 
  [42.0, 2709112.1825882355],
  [42.0, 3724968.1825882364],
  [42.0, 3716432.1825882364],
  [22.0, 3402745.286117647],
  [44.0, 5300792.572235294],
  [22.0, 3530238.286117647],
  [45.0, 3785055.2670588233],
  [43.0, 3300664.877411765]])
labels = np.array([1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1])

X = training_data
y = labels
print(X)
print(y)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='winter')

#A linear discriminative classifier would attempt to draw a straight line 
#separating the two sets of data, and thereby create a model for classification. 
#For two dimensional data this is a task we could do by hand. 
#But immediately we see a problem: 
#there is more than one possible dividing line that can perfectly discriminate between the two classes!
#We can draw them as follows:
xfit = np.linspace(-1, 3.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plt.plot([53], [2500000], 'x', color='red', markeredgewidth=2, markersize=10)

for m, b in [(30, 0.65), (90, 5000000), (-0.2, 2.9)]:
    plt.plot(xfit, m * xfit + b, '-k')

plt.xlim(-1, 3.5);

#These are three very different separators which, nevertheless, 
#perfectly discriminate between these samples. 
#Depending on which you choose, a new data point (e.g., the one marked by the "X" in this plot) 
#will be assigned a different label! 
#Evidently our simple intuition of "drawing a line between classes" is not enough, 
#and we need to think a bit deeper.

#Support vector machines offer one way to improve on this. 
#The intuition is this: rather than simply drawing a zero-width line between the classes, 
#we can draw around each line a margin of some width, up to the nearest point. 
#Here is an example of how this might look:
xfit = np.linspace(-1, 3.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
    yfit = m * xfit + b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor='none',
                     color='#AAAAAA', alpha=0.4)

plt.xlim(-1, 3.5);

#In support vector machines, the line that maximizes this margin is the one 
#we will choose as the optimal model. 
#Support vector machines are an example of such a maximum margin estimator.

#Fitting a support vector machine
#Let's see the result of an actual fit to this data: 
#we will use Scikit-Learn's support vector classifier to train an SVM model on this data. 
#For the time being, we will use a linear kernel and set the C parameter to a very large number 
#(we'll discuss the meaning of these in more depth momentarily).
from sklearn.svm import SVC # "Support vector classifier"
model = SVC(kernel='linear', C=1E10)
model.fit(X, y)

#To better visualize what's happening here, 
#let's create a quick convenience function that will plot SVM decision boundaries for us:
def plot_svc_decision_function(model, ax=None, plot_support=True):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)
    
    # plot decision boundary and margins
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])
    
    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   s=300, linewidth=1, facecolors='none');
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)


plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plot_svc_decision_function(model);

training_data = np.array([[40.0, 2088139.0],
  [68.0, 927650.0],
  [71.0, 1133323.0],
  [68.0, 859230.0],
  [75.0, 1668323.0],
  [70.0, 104659.0],
  [88.0, 2032140.0],
  [60.0, 1200924.0], 
  [42.0, 2709112.1825882355],
  [42.0, 3724968.1825882364],
  [42.0, 3716432.1825882364],
  [22.0, 3402745.286117647],
  [44.0, 5300792.572235294],
  [22.0, 3530238.286117647],
  [45.0, 3785055.2670588233],
  [43.0, 3300664.877411765]])

labels = np.array([1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1])
print(training_data.shape)
print(labels.shape)

model = SVC(kernel='linear', C=1E10)
model.fit(training_data, labels)



result1 = model.predict(training_data)
print (result1)
print(labels)

new_test_data = np.array([[40.0, 2088139.0],
  [38.0, 6927650.0],
  [71.0, 1133323.0],
  [68.0, 859230.0],
  [75.0, 1668323.0],
  [70.0, 104659.0],
  [88.0, 2032140.0],
  [60.0, 1200924.0], 
  [42.0, 2709112.1825882355],
  [42.0, 3724968.1825882364],
  [42.0, 3716432.1825882364],
  [22.0, 3402745.286117647],
  [44.0, 5300792.572235294],
  [22.0, 3530238.286117647],
  [45.0, 3785055.2670588233],
  [43.0, 3300664.877411765]])

result1 = model.predict(new_test_data)
print (result1)
print(labels)
