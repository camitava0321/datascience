# -*- coding: utf-8 -*-
#%% - imports
import ann_functions
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

#%% - Generate Dataset and visualize
#X - data, y - class
X, y = ann_functions.generate_data()
plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)

#%%
#The dataset has two classes, plotted as red and blue points. 
#blue dots - male patients ; red dots - female patients
#x- and y- axis being medical measurements.

#Goal - train a ML classifier that predicts the correct class (male or female) 
#given the x- and y- coordinates. 

#Note - data is not linearly separable, we can’t draw a straight line that 
#separates the two classes. So, linear classifiers, such as Logistic Regression,  
#won’t be able to fit the data unless one manually engineer non-linear features (such as polynomials) 
#that work well for the given dataset.

#This is one of the major advantages of Neural Networks - One does not need 
#to worry about feature engineering. The hidden layer of a neural network will 
#learn features for us.

#Logistic Regression
#To demonstrate the point 
#let’s train a Logistic Regression classifier. 
#It’s input will be the x- and y-values and 
#output the predicted class (0 or 1). 
#We use the Logistic Regression class from scikit-learn.

# Train the logistic rgeression classifier
clf = linear_model.LogisticRegressionCV()
clf.fit(X, y)


 
# Plot the decision boundary
ann_functions.plot_decision_boundary(clf,X,y)
plt.title("Logistic Regression")


#%%Training a Neural Network
#Let’s now build a 3-layer neural network with 
#one input layer, one hidden layer, and one output layer. 
#The number of nodes in the input layer 
#is determined by the dimensionality of our data, 2. 
#Similarly, the number of nodes in the output layer is determined 
#by the number of classes we have, also 2. 
#(Because we only have 2 classes 
#we could actually get away with only one output node predicting 0 or 1, 
#but having 2 makes it easier to extend the network to more classes later on). 
#The input to the network will be x- and y- coordinates and 
#its output will be two probabilities, 
#one for class 0 (“female”) and one for class 1 (“male”). 

#We can choose the dimensionality (the number of nodes) of the hidden layer.
#The more nodes we put into the hidden layer 
#the more complex functions we will be able fit. 
#But higher dimensionality comes at a cost. 
#1. more computation is required to make predictions and 
#learn the network parameters. 
#2. A bigger number of parameters also means 
#we become more prone to overfitting our data.

#How to choose the size of the hidden layer? 
#While there are some general guidelines and recommendations, 
#it always depends on your specific problem and 
#is more of an art than a science. 
#We will play with the number of nodes in the hidden later later on and 
#see how it affects our output.

#We also need to pick an activation function for our hidden layer. 
#The activation function transforms the inputs of the layer into its outputs. 
#A nonlinear activation function allows us to fit nonlinear hypotheses. 
#Common chocies for activation functions are 
#tanh, 
#the sigmoid function, or 
#ReLUs. 
#We will use tanh, which performs quite well in many scenarios. 
#A nice property of these functions is that 
#their derivate can be computed using the original function value. 
#For example, 
#the derivative of \tanh x is 1-\tanh^2 x. 
#This is useful because it allows us to compute \tanh x  once and 
#re-use its value later on to get the derivative.

#Because we want our network to output probabilities 
#the activation function for the output layer will be the softmax, 
#which is simply a way to convert raw scores to probabilities. 
#If you’re familiar with the logistic function 
#you can think of softmax as its generalization to multiple classes.

#How our network makes predictions
#Our network makes predictions using forward propagation, 
#which is just a bunch of matrix multiplications and 
#the application of the activation function(s) we defined above. 
#If x is the 2-dimensional input to our network then 
#we calculate our prediction \hat{y} (also two-dimensional) as follows:
#\begin{aligned}  z_1 & = xW_1 + b_1 \\  a_1 & = \tanh(z_1) \\  z_2 & = a_1W_2 + b_2 \\  a_2 & = \hat{y} = \mathrm{softmax}(z_2)  \end{aligned}

#z_i is the input of layer i and 
#a_i is the output of layer i after applying the activation function. 
#W_1, b_1, W_2, b_2 are parameters of our network, 
#which we need to learn from our training data. 
#You can think of them as matrices transforming data 
#between layers of the network. 
#Looking at the matrix multiplications above 
#we can figure out the dimensionality of these matrices. 
#If we use 500 nodes for our hidden layer then 
#W_1 \in \mathbb{R}^{2\times500}, 
#b_1 \in \mathbb{R}^{500}, 
#W_2 \in \mathbb{R}^{500\times2}, 
#b_2 \in \mathbb{R}^{2}. 
#Now you see why we have more parameters 
#if we increase the size of the hidden layer.

