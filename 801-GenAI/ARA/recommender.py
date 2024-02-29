# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:13:16 2024

@author: AMITAVA
"""

# Importing Libraries
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import time
warnings.simplefilter(action='ignore', category=FutureWarning)


# loading room dataset
rooms = pd.read_csv("data/rooms1.csv")
print("\nRooms dataset looks like :")
print(rooms.head())

# Generate Guest Id - serial number
guestIds = np.arange(1, 20, 1)
with open('data/roomRatings.csv', 'w') as the_file:
    string = 'guestId,roomId,roomRating,timestamp\n'
    the_file.write(string)
    for index,room in rooms.iterrows():
        for guest in guestIds:
            rating = np.random.randint(0,5)
            #print (guest, room['roomId'], rating, time.time())
            string = str(guest)+','+str(room['roomId'])+','+str(rating)+','+ \
                str(time.time())+'\n'
            the_file.write(string)

the_file.close()
#loading roomRating dataset
roomRatings = pd.read_csv("data/roomRatings.csv")
print("RoomRatings dataset looks like :")
print(roomRatings.head())


# We will recommend rooms based on user-user similarity and item-item similarity. 
# For that, first we need to calculate the number of unique guests and rooms.
n_roomRatings = len(roomRatings)
n_rooms = len(roomRatings['roomId'].unique())
n_guests = len(roomRatings['guestId'].unique())

# Crucial statistics for room ratings dataset 
print(f"\nNumber of roomRatings: {n_roomRatings}")
print(f"Number of unique roomId's: {n_rooms}")
print(f"Number of unique guests: {n_guests}")
print(f"Average roomRatings per guest: {round(n_roomRatings/n_guests, 2)}")
print(f"Average roomRatings per room: {round(n_roomRatings/n_rooms, 2)}")

# We now compute user-specific statistics for the room-ratings dataset.
# We classify the data according to user IDs
# then we calculates the total number of ratings each user has submitted and 
# save the results in a new DF
# To facilitate additional user-based analysis and the creation of recommendation systems, 
# this user-level frequency information is crucial for comprehending user engagement and activity
# in the rating dataset. 
# The first few rows of this DataFrame are shown for a brief summary of 
# user-specific rating counts

# User Rating Frequency
guest_freq = roomRatings[['guestId', 'roomId']].groupby(
	'guestId').count().reset_index()
guest_freq.columns = ['guestId', 'n_roomRatings']
print("\nGuest_Freq dataset looks like :")
print(guest_freq.head())

# Room Rating Analysis
# Find Lowest and Highest rated rooms:
mean_roomRating = roomRatings.groupby('roomId')[['roomRating']].mean()
# Lowest rated rooms
lowest_rated = mean_roomRating['roomRating'].idxmin()
rooms.loc[rooms['roomId'] == lowest_rated]
# Highest rated rooms
highest_rated = mean_roomRating['roomRating'].idxmax()
rooms.loc[rooms['roomId'] == highest_rated]
# show number of people who rated rooms rated room highest
roomRatings[roomRatings['roomId']==highest_rated]
# show number of people who rated rooms rated room lowest
roomRatings[roomRatings['roomId']==lowest_rated]

## the above rooms has very low dataset. We will use bayesian average
room_stats = roomRatings.groupby('roomId')[['roomRating']].agg(['count', 'mean'])
room_stats.columns = room_stats.columns.droplevel()

# To determine which rooms in the dataset have the lowest and highest ratings, 
# this algorithm analyzes room reviews. 
# It determines the average ratings for every room, 
# making it possible to identify which ones have the lowest and greatest average ratings. 
# Subsequently, the algorithm accesses and presents the information about these rooms 
# from the’rooms’ dataset. It also sheds light on the popularity and guest involvement of 
# the room by displaying the number of users who rated both the highest and lowest-ranked ones. 
# This gives insights into user engagement. 
# Bayesian averages may offer more accurate quality ratings for rooms with a 
# small number of ratings.
#%%
# Now, we create guest-item matrix using scipy csr matrix
# A guest-item matrix is a basic data structure in a recommendation systems
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

def create_matrix(df):
	
    # To find the number of unique users and unique videos in the dataset, N and M are computed.
	N = len(df['guestId'].unique())
	M = len(df['roomId'].unique())

    # We will create four dictionaries:
	
	# Map Ids to indices
    # guest_mapper: Maps distinct guest IDs to indexes (guest ID 1 becomes index 0 for example).
	guest_mapper = dict(zip(np.unique(df["guestId"]), list(range(N))))
    
    # room_mapper: Converts distinct room IDs into indices (room ID 1 becomes index 0 for example).
	room_mapper = dict(zip(np.unique(df["roomId"]), list(range(M))))
	
	# Map indices to IDs
    # guest_inv_mapper: Reverses guest_mapper and maps indices back to guest IDs.
	guest_inv_mapper = dict(zip(list(range(N)), np.unique(df["guestId"])))
    # room_inv_mapper: Reverses room_mapper by mapping indices back to room IDs.
	room_inv_mapper = dict(zip(list(range(M)), np.unique(df["roomId"])))
	
    # To map the real guest and room IDs in the dataset to their matching indices, 
    # the lists guest_index and room_index are generated.
	guest_index = [guest_mapper[i] for i in df['guestId']]
	room_index = [room_mapper[i] for i in df['roomId']]

    # We finally create a sparse matrix X (using the SciPy function csr_matrix). 
    # The user and movie indices that correspond to the rating values in the dataset 
    # are used to generate this matrix. The form of it is (M, N), 
    # where M denotes the quantity of distinct rooms and 
    # N denotes the quantity of distinct guests.
    # To put it another way, this code makes it easy to do calculations and 
    # create recommendation systems based on the structured representation of guest ratings 
    # for movies in the data.
	X = csr_matrix((df["roomRating"], (room_index, guest_index)), shape=(M, N))
	
	return X, guest_mapper, room_mapper, guest_inv_mapper, room_inv_mapper
	
X, guest_mapper, room_mapper, guest_inv_mapper, room_inv_mapper = create_matrix(roomRatings)
#%%
"""
Find similar rooms using KNN
it uses the k-Nearest Neighbors (KNN) algorithm to identify rooms that are similar 
to a given room. 
The function takes inputs - 
target room ID, 
a guest-item matrix (X), 
the number of neighbors to consider (k), 
a similarity metric (default is cosine similarity), and 
an option to show distances between rooms. 
"""

def find_similar_rooms(room_id, X, k, metric='cosine', show_distance=False):
	
    # The function begins by initializing a blank list to hold the IDs of rooms that are comparable
	neighbour_ids = []
    # It takes the target movie’s index out of the room_mapper dictionary and 
    # uses the guest-item matrix to acquire the feature vector that goes with it. 
	room_ind = room_mapper[room_id]
	room_vec = X[room_ind]
    # Next, the KNN model is configured using the given parameters.
	k+=1
	kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
	kNN.fit(X)
    # The distances and indices of the k-nearest neighbors to the target room are calculated 
    # once the KNN model has been fitted. 
	room_vec = room_vec.reshape(1,-1)
	neighbour = kNN.kneighbors(room_vec, return_distance=show_distance)
	for i in range(0,k):
		n = neighbour.item(i)
        # Using the room_inv_mapper dictionary, the loop retrieves these neighbor indices and 
        # maps them back to room IDs. 
		neighbour_ids.append(room_inv_mapper[n])

    # Since it matches the desired room, the first item in the list is eliminated. 
	neighbour_ids.pop(0)
    # a list of related rooms and the id of the target room are returned 
    # suggesting rooms based on the KNN model.
	return neighbour_ids


room_roomNumbers = dict(zip(rooms['roomId'], rooms['roomNumber']))

room_id = 3

similar_ids = find_similar_rooms(room_id, X, k=3)
room_roomNumber = room_roomNumbers[room_id]

print(f"Since you had chosen room {room_roomNumber} before")
for i in similar_ids:
	print(room_roomNumbers[i])

#%%
# Room Recommendation with respect to Guest Preference
# A function to recommend rooms based on the guest preferences.
"""
The function accepts the following inputs: 
    1) dictionaries (guest_mapper, room_mapper, and room_inv_mapper) 
    for mapping user and movie IDs to matrix indices; 
    2) the guest_id for which recommendations are desired 
    3) a guest-item matrix X representing room ratings and 
    4) an optional parameter k for the number of recommended rooms (default is 10).

The function handles situations where the guest or room doesn’t exist in the dataset and 
is intended to suggest rooms for a particular guest based on their highest-rated room. 
"""
def recommend_rooms_for_guest(guest_id, X, guest_mapper, room_mapper, room_inv_mapper, k=10):


    # It initially filters the ratings dataset to see if the given guest is there? 
    # It notifies the user that the requested person does not exist and 
    # ends the function if the guest does not exist (the filtered DataFrame is empty).
	df1 = roomRatings[roomRatings['guestId'] == guest_id]
	
	if df1.empty:
		print(f"guest with ID {guest_id} does not exist.")
		return

    # if the guest exists, then designate the room that has received the highest rating 
    # from that particular guest. It finds the id of this room and 
    # chooses it based on the highest rating.
	room_id = df1[df1['roomRating'] == max(df1['roomRating'])]['roomId'].iloc[0]
    # With information from the rooms dataset, a dictionary called room_roomNumbers is created 
    # to map room IDs to their numbers. 
	room_roomNumbers = dict(zip(rooms['roomId'], rooms['roomNumber']))
    # The function then uses find_similar_rooms to locate rooms 
    # that are comparable to the room in the guest-item matrix that has the highest rating 
    #(denoted by room_id). 
	similar_ids = find_similar_rooms(room_id, X, k)
    # It gives back a list of comparable room IDs.
    # We then search the room_roomNumbers dictionary for the room combination of the 
    # highest-rated room, and 
    # if the room is not found, it sets the title to “room not found.” 
	room_roomNumber = room_roomNumbers.get(room_id, "room not found")
    # When a room is retrieved as “room not found,” 
    # it means that the highest-rated room (based on room_id) is not present in the dataset. 
	if room_roomNumber == "room not found":
		print(f"room with ID {room_id} not found.")
		return
    # If the room is located, the guest is presented with recommendations 
    # for other rooms based on the highest rated room. 
    # The list of comparable room IDs is iterated over, and the rooms are printed. 
    # When a room isn’t discovered in the dataset, the default message is “room not found.”
	print(f"Since you had chosen room {room_roomNumber}, you might also like:")
	for i in similar_ids:
		print(room_roomNumbers.get(i, "room not found"))



guest_id = 12 # Replace with the desired guest ID
recommend_rooms_for_guest(guest_id, X, guest_mapper, room_mapper, room_inv_mapper, k=2)


guest_id = 7 # Replace with the desired guest ID
recommend_rooms_for_guest(guest_id, X, guest_mapper, room_mapper, room_inv_mapper, k=2)


