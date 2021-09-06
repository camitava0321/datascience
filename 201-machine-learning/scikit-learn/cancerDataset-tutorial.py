# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#%% - Working With Cancer Dataset
#Exploration of some of the main scikit-learn tools on a single practical task

#load cancer dataset
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

cancer = load_breast_cancer()
print cancer

 