# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Logistic Regression 
#Spam filter
#Classify messages to be either good or spam. 
#The dataset we’ll use is the SMSSpamCollection dataset. 
#The dataset contains messages, which are either spam or good.

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score

#Logistic regression - a classification algorithm:
#Given an example, we try to predict the probability that it belongs to “0” class or “1” class.
#A logisitic function always returns a value between one and zero.

#Load the dataset using pandas. 
df = pd.read_csv('SMSSpamCollection', delimiter='\t',header=None)

#Then we split in a training and test set. 
X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1],df[0])

#We extract text features known as TF-IDF features, because we need to work with numeric vectors.
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_raw)

#Now we create the logistic regression object and 
#train it with the training data. 
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

#Finally we create a set of messages to make predictions.
X_test = vectorizer.transform( ['URGENT! Your Mobile No 1234 was awarded a Prize', 'Hey honey, whats up?'] )
predictions = classifier.predict(X_test)
print(predictions)