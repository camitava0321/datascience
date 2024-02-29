# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 12:13:16 2023
@author: AMITAVA

A Basic Recommendation System in Python

There are a lot of applications where websites collect data from their users and 
use that data to predict the likes and dislikes of their users. 
This enables people to suggest the material that interests them. 
Recommender systems are a means of making suggestions for products and concepts that 
align with a user’s particular perspective.

Python Recommendation Systems employs a data-driven methodology to offer customers tailored recommendations. 
It uses user data and algorithms to forecast and suggest goods, services, or content that a user is probably 
going to find interesting. These systems are essential in applications where users may become overwhelmed by 
large volumes of information, such as social media, streaming services, and e-commerce. 
Building recommendation systems is a common use for Python because of its modules and machine learning frameworks. 

The two main kinds are 
content-based filtering (which takes into account the characteristics of products and user profiles) and 
collaborative filtering (which generates recommendations based on user behaviour and preferences). 
Hybrid strategies that integrate the two approaches are also popular. 
These kinds of systems improve user experiences, boost user involvement, and propel corporate expansion.

Recommender System is of different types:
    Content-Based Recommendation: It is supervised machine learning used to induce a classifier 
                                  to discriminate between interesting and uninteresting items for the user.
    Collaborative Filtering: Collaborative Filtering recommends items based on similarity measures between 
                                  users and/or items. The basic assumption behind the algorithm is that users 
                                  with similar interests have common preferences.

Content-Based Recommendation System
Content-based systems recommend items to the customer similar to previously high-rated items by the customer. 
It uses the features and properties of the item. From these properties, it can calculate the similarity between 
the items.

In a content-based recommendation system, first, we need to create a profile for each item, 
which represents the properties of those items. The user profiles are inferred for a particular user. 
We use these user profiles to recommend the items to the users from the catalog.

Item profile
In a content-based recommendation system, we need to build a profile for each item, 
which contains the important properties of each item. For Example, If the movie is an item, 
then its actors, director, release year, and genre are its important properties, and for the document, 
the important property is the type of content and set of important words in it.

Let’s have a look at how to create an item profile. First, we need to perform the TF-IDF vectorizer, 
here TF (term frequency) of a word is the number of times it appears in a document and 
The IDF (inverse document frequency) of a word is the measure of how significant that term is in the whole corpus.

TF-IDF Vectorizer

    Term Frequency(TF) : Term frequency, or TF for short, is a key idea in information retrieval and natural language processing. It displays the regularity with which a certain term or word occurs in a text corpus or document. TF is used to rank terms in a document according to their relative value or significance.
    The term-frequency can be calculated by:
    TF_{ij} = \frac{f_{ij}}{max_k f_{kj}}
    where fij is the frequency of term(feature) i in document(item) j. 
    For a variety of text analysis tasks, such as information retrieval, document classification, and sentiment analysis, the yielded TF value can be used to identify important terms in a document. It offers a framework for figuring out how relevant a word is in a particular situation.
    Inverse-document Frequency(IDF): The measure known as Inverse Document Frequency (IDF) is employed in text analysis and information retrieval to evaluate the significance of phrases within a set of documents. IDF measures how uncommon or unique a term is in the corpus. To compute it, take the reciprocal of the fraction of documents that include the term and logarithmize it. Common terms have lower IDF values, while rare terms have higher values. IDF is an essential part of the TF-IDF (Term Frequency-Inverse Document Frequency) method, which uses it to assess the relative importance of terms in different documents. To improve information representation and retrieval from massive text datasets, IDF is used in tasks including document ranking, categorization, and text mining.
    The inverse-document frequency can be calculated with:
    IDF_{i} = log_e \frac{N}{n_i}
    where, ni number of documents that mention term i. N is the total number of docs.

A numerical statistic called Term Frequency-Inverse Document Frequency (TF-IDF) is employed in information retrieval and natural language processing. The term’s significance within a document is assessed in relation to a group of documents (the corpus). TF emphasizes terms with greater frequencies by measuring a term’s frequency of occurrence in a document. IDF evaluates a term’s rarity within the corpus, emphasizing terms that are distinct. A weighted score is produced for each term in a document by multiplying TF and IDF together to compute TF-IDF.

Therefore, the total formula is:

TF-IDF score (w_{ij}) = TF_{ij} * IDF_i
User profile

The user profile is a vector that describes the user preference. During the creation of the user’s profile, we use a utility matrix that describes the relationship between user and item. From this information, the best estimate we can decide which item the user likes, is some aggregation of the profiles of those items.

Advantages and Disadvantages

     Advantages:
        No need for data on other users when applying to similar users.
        Able to recommend to users with unique tastes.
        Able to recommend new & popular items
        Explanations for recommended items.
    Disadvantages:
        Finding the appropriate feature is hard.
        Doesn’t recommend items outside the user profile.

Collaborative Filtering

Collaborative filtering is based on the idea that similar people (based on the data) generally tend to like similar things. It predicts which item a user will like based on the item preferences of other similar users. 

Collaborative filtering uses a user-item matrix to generate recommendations. This matrix contains the values that indicate a user’s preference towards a given item. These values can represent either explicit feedback (direct user ratings) or implicit feedback (indirect user behavior such as listening, purchasing, watching).

    Explicit Feedback: The amount of data that is collected from the users when they choose to do so. Many of the times, users choose not to provide data for the user. So, this data is scarce and sometimes costs money.  For example, ratings from the user.
    Implicit Feedback: In implicit feedback, we track user behavior to predict their preference.

Rating Predictions

Let rx be the vector of user x’s rating. Let N be the set of k similar users who also rated item i. Then we can calculate the prediction of user x and item i by using following formula:

r_{xi} = \frac{\sum_{y \in N}S_{xy}r_{yi}}{\sum_{y \in N}S_{xy}} \, \, S_{xy} = sim(x,y)
Advantages and Disadvantages

     Advantages:
        No need for the domain knowledge because embedding are learned automatically.
        Capture inherent subtle characteristics.
    Disadvantages:
        Cannot handle fresh items due to cold start problem.
        Hard to add any new features that may improve quality of model


Conclusion
Developing a Python recommendation system allows for the creation of tailored content recommendations 
that improve user experience and take into account user preferences. 
Through the utilization of collaborative filtering, content-based filtering, and hybrid techniques, 
these systems are able to offer customized recommendations to consumers for content, movies, or items. 
These systems use sophisticated methods such as closest neighbors and matrix factorization to find hidden patterns 
in item attributes and user behavior. 
Recommendation systems are able to adjust and get better over time thanks to the combination of machine learning and 
data-driven insights. 
In the end, these solutions are essential for raising consumer satisfaction, improving user engagement, and 
propelling corporate expansion in a variety of industries.
"""

#Implementation of Recommendation System
# Importing Libraries
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

#sets up the code to suppress future warnings, so that cautions about upcoming library changes don’t clog 
#the output and create a messier, less productive workspace. 
warnings.simplefilter(action='ignore', category=FutureWarning)

#Two datasets are imported into this code to do a movie recommendation study. 
#User ratings for movies are included in the first dataset, “ratings.csv,” which is kept in a Pandas DataFrame 
#named ratings. 
ratings = pd.read_csv("data/ratings.csv")
print(ratings.head())

#This dataset is put into a Pandas DataFrame called “movies” and contains movie metadata like names and genres. 
movies = pd.read_csv("data/movies.csv")
print(movies.head())

#In order to give a preliminary overview of the data and lay the groundwork for further analysis or 
#recommendation system development, the code displays the first few rows of each DataFrame.

#Statistical Analysis of Ratings
n_ratings = len(ratings)
n_movies = len(ratings['movieId'].unique())
n_users = len(ratings['userId'].unique())

#This code computes and reports a number of crucial statistics for a movie ratings dataset. 
#It counts the number of unique movie IDs (n_movies) and user IDs (n_users) as well as the total number of ratings 
#(n_ratings). These metrics provide important information about the properties of the dataset, 
#including its size and the variety of people and movies inside it. 
#To give a more complete picture of the distribution of ratings throughout the dataset, 
#it also calculates and shows the average number of ratings for each user and each movie. 
#Understanding the size and user interaction of the dataset requires knowledge of this information.
print(f"Number of ratings: {n_ratings}")
print(f"Number of unique movieId's: {n_movies}")
print(f"Number of unique users: {n_users}")
print(f"Average ratings per user: {round(n_ratings/n_users, 2)}")
print(f"Average ratings per movie: {round(n_ratings/n_movies, 2)}")


#The movie ratings dataset’s user-specific statistics are computed and shown in this code segment. 
#After classifying the data according to user IDs, it calculates the total number of ratings each user 
#has submitted and saves the results in a new DataFrame named user_freq. 
#With ‘userId’ denoting the user ID and ‘n_ratings’ the number of ratings the user has contributed, 
#the columns are suitably labeled. 
#To facilitate additional user-based analysis and the creation of recommendation systems, 
#this user-level frequency information is crucial for comprehending user engagement and 
#activity inside the rating dataset. 
#The first few rows of this DataFrame are shown for a brief summary of user-specific rating counts by the 
#print(user_freq.head()) line.

#User Rating Frequency
user_freq = ratings[['userId', 'movieId']].groupby(
	'userId').count().reset_index()
user_freq.columns = ['userId', 'n_ratings']
print(user_freq.head())


#Movie Rating Analysis
# Find Lowest and Highest rated movies:
mean_rating = ratings.groupby('movieId')[['rating']].mean()
# Lowest rated movies
lowest_rated = mean_rating['rating'].idxmin()
movies.loc[movies['movieId'] == lowest_rated]
# Highest rated movies
highest_rated = mean_rating['rating'].idxmax()
movies.loc[movies['movieId'] == highest_rated]
# show number of people who rated movies rated movie highest
ratings[ratings['movieId']==highest_rated]
# show number of people who rated movies rated movie lowest
ratings[ratings['movieId']==lowest_rated]

## the above movies has very low dataset. We will use bayesian average
movie_stats = ratings.groupby('movieId')[['rating']].agg(['count', 'mean'])
movie_stats.columns = movie_stats.columns.droplevel()

#To determine which movies in the dataset have the lowest and highest ratings, 
#this algorithm analyzes movie reviews. It determines the average ratings for every film, making it possible 
#to identify which ones have the lowest and greatest average ratings. 
#Subsequently, the algorithm accesses and presents the information about these films from the’movies’ dataset. 
#It also sheds light on the popularity and audience involvement of the movie by displaying the number of users 
#who rated both the highest and lowest-ranked ones. 
#This gives insights into user engagement. Bayesian averages may offer more accurate quality ratings 
#for films with a small number of ratings.

#User-Item Matrix Creation
# Now, we create user-item matrix using scipy csr matrix
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

def create_matrix(df):
	
	N = len(df['userId'].unique())
	M = len(df['movieId'].unique())
	
	# Map Ids to indices
	user_mapper = dict(zip(np.unique(df["userId"]), list(range(N))))
	movie_mapper = dict(zip(np.unique(df["movieId"]), list(range(M))))
	
	# Map indices to IDs
	user_inv_mapper = dict(zip(list(range(N)), np.unique(df["userId"])))
	movie_inv_mapper = dict(zip(list(range(M)), np.unique(df["movieId"])))
	
	user_index = [user_mapper[i] for i in df['userId']]
	movie_index = [movie_mapper[i] for i in df['movieId']]

	X = csr_matrix((df["rating"], (movie_index, user_index)), shape=(M, N))
	
	return X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper
	
X, user_mapper, movie_mapper, user_inv_mapper, movie_inv_mapper = create_matrix(ratings)

"""
A user-item matrix is a basic data structure in recommendation systems, and it is created by the code that is given. This is how it operates:

    To find the number of unique users and unique videos in the dataset, N and M are computed.
    There are four dictionaries produced:
        user_mapper: Maps distinct user IDs to indexes (user ID 1 becomes index 0 for example).
        movie_mapper: Converts distinct movie IDs into indices (movie ID 1 becomes index 0 for example).
        user_inv_mapper: Reverses user_mapper and maps indices back to user IDs.
        movie_inv_mapper: Reverses movie_mapper by mapping indices to movie IDs.
    To map the real user and movie IDs in the dataset to their matching indices, the lists user_index and movie_index are generated.
    A sparse matrix X is created using the SciPy function csr_matrix. The user and movie indices that correspond to the rating values in the dataset are used to generate this matrix. The form of it is (M, N), where M denotes the quantity of distinct films and N denotes the quantity of distinct consumers.

To put it another way, this code makes it easy to do calculations and create recommendation systems based on the structured representation of user ratings for movies in the data.
Movie Similarity Analysis

Find similar movies using KNN
"""
def find_similar_movies(movie_id, X, k, metric='cosine', show_distance=False):
	
	neighbour_ids = []
	
	movie_ind = movie_mapper[movie_id]
	movie_vec = X[movie_ind]
	k+=1
	kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
	kNN.fit(X)
	movie_vec = movie_vec.reshape(1,-1)
	neighbour = kNN.kneighbors(movie_vec, return_distance=show_distance)
	for i in range(0,k):
		n = neighbour.item(i)
		neighbour_ids.append(movie_inv_mapper[n])
	neighbour_ids.pop(0)
	return neighbour_ids


movie_titles = dict(zip(movies['movieId'], movies['title']))

movie_id = 3

similar_ids = find_similar_movies(movie_id, X, k=10)
movie_title = movie_titles[movie_id]

print(f"Since you watched {movie_title}")
for i in similar_ids:
	print(movie_titles[i])


#The above function, “find_similar_movies,” which uses the k-Nearest Neighbors 
#(KNN) algorithm to identify movies that are similar to a given movie. 
#The function takes inputs such as the target movie ID, a user-item matrix (X), the number of neighbors 
#to consider (k), a similarity metric (default is cosine similarity), and 
#an option to show distances between movies. 
#The function begins by initializing a blank list to hold the IDs of films that are comparable. 
#It takes the target movie’s index out of the movie_mapper dictionary and 
#uses the user-item matrix to acquire the feature vector that goes with it. 
#Next, the KNN model is configured using the given parameters.

#The distances and indices of the k-nearest neighbors to the target movie are calculated once the KNN model 
#has been fitted. Using the movie_inv_mapper dictionary, the loop retrieves these neighbor indices and maps 
#them back to movie IDs. Since it matches the desired movie, the first item in the list is eliminated. The 
#code ends with a list of related movie titles and the title of the target film, suggesting movies based on 
#the KNN model.

#Movie Recommendation with respect to Users Preference

#Create a function to recomment the movies based on the user preferences.
def recommend_movies_for_user(user_id, X, user_mapper, movie_mapper, movie_inv_mapper, k=10):
	df1 = ratings[ratings['userId'] == user_id]
	
	if df1.empty:
		print(f"User with ID {user_id} does not exist.")
		return

	movie_id = df1[df1['rating'] == max(df1['rating'])]['movieId'].iloc[0]

	movie_titles = dict(zip(movies['movieId'], movies['title']))

	similar_ids = find_similar_movies(movie_id, X, k)
	movie_title = movie_titles.get(movie_id, "Movie not found")

	if movie_title == "Movie not found":
		print(f"Movie with ID {movie_id} not found.")
		return

	print(f"Since you watched {movie_title}, you might also like:")
	for i in similar_ids:
		print(movie_titles.get(i, "Movie not found"))

"""
The function accepts the following inputs: dictionaries (user_mapper, movie_mapper, and movie_inv_mapper) for mapping user and movie IDs to matrix indices; the user_id for which recommendations are desired; a user-item matrix X representing movie ratings; and an optional parameter k for the number of recommended movies (default is 10).

    It initially filters the ratings dataset to see if the user with the given ID is there. It notifies the user that the requested person does not exist and ends the function if the user does not exist (the filtered DataFrame is empty).
    The code, if it exists, designates the movie that has received the highest rating from that particular user. It finds the movieId of this movie and chooses it based on the highest rating.
    With information from the movies dataset, a dictionary called movie_titles is created to map movie IDs to their titles. The function then uses find_similar_movies to locate films that are comparable to the movie in the user-item matrix that has the highest rating (denoted by movie_id). It gives back a list of comparable movie IDs.
    The code searches the movie titles dictionary for the title of the highest-rated film, and if the film is not found, it sets the title to “Movie not found.” When a movie title is retrieved as “Movie not found,” it means that the highest-rated film (based on movie_id) is not present in the dataset. If the movie is located, the customer is presented with recommendations for other movies based on the highest rated film. The list of comparable movie IDs is iterated over, and the titles are printed. When a movie isn’t discovered in the dataset, the default message is “Movie not found.”
    The function handles situations where the user or movie doesn’t exist in the dataset and is intended to suggest movies for a particular user based on their highest-rated film. The code calls the function with the necessary parameters and sets the user_id to a specific user to show how to utilize the method.
"""
#Reccomment the movies
user_id = 150 # Replace with the desired user ID
recommend_movies_for_user(user_id, X, user_mapper, movie_mapper, movie_inv_mapper, k=10)


user_id = 2300 # Replace with the desired user ID
recommend_movies_for_user(user_id, X, user_mapper, movie_mapper, movie_inv_mapper, k=10)