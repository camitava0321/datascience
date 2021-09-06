# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#Decision Tree
#Classifiers
#We’ll use simple arrays as data - In practice we will have large datasets to make good predictions.

#At every node of the tree, we can turn left or right. 
#Based on numbers we walk the branches. At the end of branches are outcomes. 
#Once the classifier is trained based on this data. 
#We can then use the classifier to make predictions.

import pydotplus
from sklearn.datasets import load_iris
from sklearn import tree
import collections

#The training data for the decision tree classifier
#[height, hair-length, voice-pitch]                                             
X = [ [180, 15,0],                                                              
      [167, 42,1],                                                              
      [136, 35,1],                                                              
      [174, 15,0],                                                              
      [141, 28,1]]                                                              

Y = ['man', 'woman', 'woman', 'man', 'woman']

data_feature_names=['height','hair length','voice pitch']


clf = tree.DecisionTreeClassifier()    
clf = clf.fit(X, Y)                                                             

#Visualize Data
dot_data = tree.export_graphviz(clf,
                                feature_names=data_feature_names,
                                out_file=None,
                                filled=True,
                                rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)

colors = ('turquoise', 'orange')
edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

for edge in edges:
    edges[edge].sort()    
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png('tree.png')



prediction = clf.predict([[133, 37,1]])                                         
print(prediction)    
