# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#%% - Model persistence
#It is possible to save a model in the scikit by using Python’s built-in persistence model, namely pickle:
from sklearn import svm
from sklearn import datasets
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)  

import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])
y[0]

#In the specific case of the scikit, it may be more interesting to use joblib’s replacement of pickle 
#(joblib.dump & joblib.load), which is more efficient on big data, but can only pickle to the disk and not to a string:
from sklearn.externals import joblib
joblib.dump(clf, 'filename.pkl') 

#Later you can load back the pickled model (possibly in another Python process) with:
clf = joblib.load('filename.pkl') 

#Note joblib.dump and joblib.load functions also accept file-like object instead of filenames. 
#Note that pickle has some security and maintainability issues. 
