# -*- coding: utf-8 -*-
# Author: Amitava Chakraborty
#%% - Loading Data
#scikit-learn comes with a few standard datasets
#the iris and digits datasets for classification and 
#the boston house prices dataset for regression.

from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

#A dataset is a dictionary-like object that 
#holds all the data and some metadata about the data. 
#This data is stored in the .data member, which is a n_samples, n_features array. 
#In the case of supervised problem, one or more response variables are stored in the .target member. 

#For digits dataset, digits.data gives access to the features that can be used to classify the digits samples:
print(digits.data)  

#digits.target gives the ground truth for the digit dataset, 
#that is the number corresponding to each digit image that we are trying to learn:
digits.target

#Shape of the data arrays
#The data is always a 2D array, shape (n_samples, n_features), 
#although the original data may have had a different shape. 
#In the case of the digits, each original sample is an image of shape (8, 8) and can be accessed using:
digits.images[0]

#The simple example on this dataset illustrates how starting from the original problem 
#one can shape the data for consumption in scikit-learn.

#%% - Loading from external datasets
#scikit-learn works on any numeric data stored as numpy arrays or scipy sparse matrices. 
#Other types that are convertible to numeric arrays such as pandas DataFrame are also acceptable.

#Some recommended ways to load standard columnar data into a format usable by scikit-learn:
#pandas.io - provides tools to read data from common formats including CSV, Excel, JSON and SQL. DataFrames may also be constructed from lists of tuples or dicts. Pandas handles heterogeneous data smoothly and provides tools for manipulation and conversion into a numeric array suitable for scikit-learn.
#scipy.io - specializes in binary formats often used in scientific computing context such as .mat and .arff
#numpy/routines.io - for standard loading of columnar data into numpy arrays
#scikit-learn’s datasets.load_svmlight_file - for the svmlight or libSVM sparse format
#scikit-learn’s datasets.load_files - for directories of text files where the name of each directory is the name of each category and each file inside of each directory corresponds to one sample from that category

#For some miscellaneous data such as images, videos, and audio, you may wish to refer to:
#skimage.io or Imageio - for loading images and videos to numpy arrays
#scipy.misc.imread (requires the Pillow package) - to load pixel intensities data from various image file formats
#scipy.io.wavfile.read - for reading WAV files into a numpy array

#Categorical (or nominal) features stored as strings (common in pandas DataFrames) will need converting to integers, and 
#integer categorical variables may be best exploited when encoded as one-hot variables 
#(sklearn.preprocessing.OneHotEncoder) or similar.

#Note: if you manage your own numerical data 
#it is recommended to use an optimized file format such as HDF5 to reduce data load times. 
#Various libraries such as H5Py, PyTables and pandas 
#provides a Python interface for reading and writing data in that format.