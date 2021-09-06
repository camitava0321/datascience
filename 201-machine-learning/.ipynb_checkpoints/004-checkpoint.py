# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Text Clustering - KMeans
#Text documents can be grouped automatically with KMeans, an unsupervised ML algorithm.
#Following are few articles about cats and google. 
#The algorithm will create clusters. 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = ["This little kitty came to play when I was eating at a restaurant.",
             "Merley has the best squooshy kitten belly.",
             "Google Translate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome."]

#Feature extraction
#KMeans works with numbers only
#We do feature extraction to get numbers from text - We use statistics to get to numerical features
#The feature we’ll use is TF-IDF, a numerical statistic - frequency and inverse document frequency. 

#The method TfidfVectorizer() implements the TF-IDF algorithm. 
#It converts a collection of raw documents to a matrix of TF-IDF features.
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

#Text clustering
#After we have numerical features, we initialize the KMeans algorithm with K=2. 
#(K can also be determined automatically)
true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

#Print the top words per cluster.
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")

#Now we give a new document to the clustering algorithm and 
#let it predict its class. 
#In the code below I’ve done that twice.
print("Prediction")
Y = vectorizer.transform(["chrome browser to open."])
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(["My cat is hungry."])
prediction = model.predict(Y)
print(prediction)