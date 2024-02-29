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
warnings.simplefilter(action='ignore', category=FutureWarning)

#loading roomRating dataset
roomRatings = pd.read_csv("data/roomRatings.csv")
print(roomRatings.head())

# loading room dataset
rooms = pd.read_csv("data/rooms.csv")
print(rooms.head())

n_roomRatings = len(roomRatings)
n_rooms = len(roomRatings['roomId'].unique())
n_guests = len(roomRatings['guestId'].unique())

print(f"Number of roomRatings: {n_roomRatings}")
print(f"Number of unique roomId's: {n_rooms}")
print(f"Number of unique guests: {n_guests}")
print(f"Average roomRatings per guest: {round(n_roomRatings/n_guests, 2)}")
print(f"Average roomRatings per room: {round(n_roomRatings/n_rooms, 2)}")

guest_freq = roomRatings[['guestId', 'roomId']].groupby(
	'guestId').count().reset_index()
guest_freq.columns = ['guestId', 'n_roomRatings']
print(guest_freq.head())

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

# Now, we create guest-item matrix using scipy csr matrix
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

def create_matrix(df):
	
	N = len(df['guestId'].unique())
	M = len(df['roomId'].unique())
	
	# Map Ids to indices
	guest_mapper = dict(zip(np.unique(df["guestId"]), list(range(N))))
	room_mapper = dict(zip(np.unique(df["roomId"]), list(range(M))))
	
	# Map indices to IDs
	guest_inv_mapper = dict(zip(list(range(N)), np.unique(df["guestId"])))
	room_inv_mapper = dict(zip(list(range(M)), np.unique(df["roomId"])))
	
	guest_index = [guest_mapper[i] for i in df['guestId']]
	room_index = [room_mapper[i] for i in df['roomId']]

	X = csr_matrix((df["roomRating"], (room_index, guest_index)), shape=(M, N))
	
	return X, guest_mapper, room_mapper, guest_inv_mapper, room_inv_mapper
	
X, guest_mapper, room_mapper, guest_inv_mapper, room_inv_mapper = create_matrix(roomRatings)

"""
Find similar rooms using KNN
"""
def find_similar_rooms(room_id, X, k, metric='cosine', show_distance=False):
	
	neighbour_ids = []
	
	room_ind = room_mapper[room_id]
	room_vec = X[room_ind]
	k+=1
	kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
	kNN.fit(X)
	room_vec = room_vec.reshape(1,-1)
	neighbour = kNN.kneighbors(room_vec, return_distance=show_distance)
	for i in range(0,k):
		n = neighbour.item(i)
		neighbour_ids.append(room_inv_mapper[n])
	neighbour_ids.pop(0)
	return neighbour_ids


room_roomNumbers = dict(zip(rooms['roomId'], rooms['roomNumber']))

room_id = 3

similar_ids = find_similar_rooms(room_id, X, k=10)
room_roomNumber = room_roomNumbers[room_id]

print(f"Since you had chosen room {room_roomNumber} before")
for i in similar_ids:
	print(room_roomNumbers[i])


def recommend_rooms_for_guest(guest_id, X, guest_mapper, room_mapper, room_inv_mapper, k=10):
	df1 = roomRatings[roomRatings['guestId'] == guest_id]
	
	if df1.empty:
		print(f"guest with ID {guest_id} does not exist.")
		return

	room_id = df1[df1['roomRating'] == max(df1['roomRating'])]['roomId'].iloc[0]

	room_roomNumbers = dict(zip(rooms['roomId'], rooms['roomNumber']))

	similar_ids = find_similar_rooms(room_id, X, k)
	room_roomNumber = room_roomNumbers.get(room_id, "room not found")

	if room_roomNumber == "room not found":
		print(f"room with ID {room_id} not found.")
		return

	print(f"Since you had chosen room {room_roomNumber}, you might also like:")
	for i in similar_ids:
		print(room_roomNumbers.get(i, "room not found"))


guest_id = 150 # Replace with the desired guest ID
recommend_rooms_for_guest(guest_id, X, guest_mapper, room_mapper, room_inv_mapper, k=10)


guest_id = 2300 # Replace with the desired guest ID
recommend_rooms_for_guest(guest_id, X, guest_mapper, room_mapper, room_inv_mapper, k=10)


