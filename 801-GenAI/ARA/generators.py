# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:38:06 2024
@author: AMITAVA

Generator Module to generate
1) basic cost matrix
2) reservation data
3) room data 
"""

import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

def generateCostMatrix(num_reservations, num_rooms):
    """
    Generates a cost matrix with room numbers as columns and reservation IDs as rows.

    Parameters:
    - num_reservations (int): Number of reservations.
    - num_rooms (int): Number of rooms.

    Returns:
    - pd.DataFrame: Cost matrix DataFrame.
    """
    reservation_ids = [str(random.randint(100000000, 999999999)) for _ in range(num_reservations)]
    room_numbers = [str(random.randint(100, 999)) for _ in range(num_rooms)]

    cost_matrix = np.random.randint(100, 1000, size=(len(reservation_ids), len(room_numbers)))

    cost_df = pd.DataFrame(cost_matrix, index=reservation_ids, columns=room_numbers)

    return cost_df

def scale_input(input_array, min_range=9001, max_range=10000):
    """
    Scale the input array from the range [1, 10] to the specified range.

    Parameters:
    - input_array (numpy.ndarray): Input array with values to be scaled.
    - min_range (float): Minimum value of the output range.
    - max_range (float): Maximum value of the output range.

    Returns:
    - numpy.ndarray: Scaled array with values in the specified range.
    """
    # Calculate the scaled array using linear interpolation
    scaled_array = min_range + (input_array - np.min(input_array)) * (max_range - min_range) / (np.max(input_array) - np.min(input_array))

    return scaled_array

def generateReservationData(num_samples=100):
    """
    Generates random data for arrivalDate, lengthOfStay, reservationScore, and upgradeType.

    Parameters:
    - num_samples (int): Number of samples to generate.

    Returns:
    - pd.DataFrame: DataFrame with generated data.
    """
    # Set a seed for reproducibility
    np.random.seed(42)

    reservation_ids = [str(random.randint(100000000, 999999999)) for _ in range(num_samples)]
    # Set start_date as today
    start_date = datetime.now()

    # Set end_date as 10 days from start_date
    end_date = start_date + timedelta(days=9)

    # Generate random dates within the specified range
    arrival_dates = pd.to_datetime(np.random.choice(pd.date_range(start_date, end_date), num_samples))

    # Generate random length of stay (between 1 and 10 days)
    length_of_stay = np.random.randint(1, 24, size=num_samples)
    # or
    # Generate length of stay based on choice
    length_of_stay = np.random.choice([1,3,7,10], size=num_samples)

    # Generate random reservation scores (between 1 and 5)
    reservation_scores = np.random.uniform(1, 200, size=num_samples)
    # or
    # Generate reservation score based on choice
    reservation_scores = np.random.choice([10,100,500,900], size=num_samples)

    # Generate random upgrade types (1, 5, 10 with specified probabilities)
    upgrade_type_probabilities = [0.10, 0.15, 0.75]
    upgrade_types = np.random.choice([1, 5, 10], size=num_samples, p=upgrade_type_probabilities)
    
    #Logic for Calculation of Cost - a low cost means that reservation to assign a room first
    #lowest by arrival date asc  (range used 50000 - 5000)
    #lowest by LoS desc - high LoS means low cost  (range used 3000 - 300)
    #lowest by reservation score desc  (range used 200 - 0.22)
    #lowest by upgrate type asc (range used )

#    cost = ((arrival_dates-start_date).days+1)*5000 + (1/length_of_stay)*3000 + (1/reservation_scores)*200 + upgrade_types/2000
    cost = scale_input((arrival_dates-start_date).days, min_range=1000000, max_range=1100000) + \
        scale_input((1/length_of_stay),min_range=10001, max_range=20000) + \
        scale_input((1/reservation_scores),min_range=101, max_range=999) + \
        scale_input(upgrade_types,min_range=.01, max_range=1)
        
    # Normalize cost
    #cost = (cost/cost.max())*1000
    arrival_dates_str = arrival_dates.strftime('%Y%m%d')

    # Create a DataFrame
    data = pd.DataFrame({
        'reservationId': reservation_ids,
        'arrivalDate': arrival_dates_str,
        'arrivalDateTime': arrival_dates,
        'lengthOfStay': length_of_stay,
        'reservationScore': reservation_scores,
        'upgradeType': upgrade_types,
        'cost': cost
    })

    return data


def generateRoomData(num_rooms=50):
    """
    Generates random data for roomNumber, costToAssign, and LoSFragmentation.

    Parameters:
    - num_rooms (int): Number of rooms to generate.

    Returns:
    - pd.DataFrame: DataFrame with generated data.
    """
    # Set a seed for reproducibility
    np.random.seed(42)

    # Generate Room Id - serial number
    roomIds = np.arange(1, num_rooms+1, 1)

    # Generate random room numbers (3-character strings)
    #room_numbers = [''.join(np.random.choice(list('0123456789'), size=3)) for _ in range(num_rooms)]
    room_numbers = np.asarray([(int)   (''.join(np.random.choice(list('123456789'), size=3)) ) for _ in range(num_rooms)])
    #room_numbers = np.asarray([''.join(np.random.choice(list('123456789')), size=3) for _ in range(num_rooms)])

    # Generate random costs to assign (between 100 and 1000)
    #costs_to_assign = np.random.randint(100, 1001, size=num_rooms)

    # Generate random LoSFragmentation (between 1 and 5)
    los_fragmentation = np.random.randint(1, 6, size=num_rooms)
    features_choice = ['A','A|B','B|C','C|D|E','E','None']
    features = np.random.choice(features_choice, num_rooms)
    # Room Cost Logic
    # High room number - low cost
    # High LoS_fragmentation - high cost 
    costs_to_assign = (1/room_numbers)*1000000 + los_fragmentation*10 
        
    # Normalize the cost
    costs_to_assign = (costs_to_assign/costs_to_assign.max())*1000
    
    #costs_to_assign = 0

    # Create a DataFrame
    data = pd.DataFrame({
        'roomId': roomIds,
        'roomNumber': room_numbers,
        'LoSFragmentation': los_fragmentation,
        'costToAssign': costs_to_assign,
        'features': features
    })
    
    print(data.dtypes)
    data.to_csv('data/rooms1.csv')
    return data

# Example usage:
if __name__ == "__main__":
    # Generate random room data with 50 rooms
    generated_room_data = generateRoomData(num_rooms=50)

    # Display the generated room data
    print("Generated Room Data:")
    print(generated_room_data.head())

    # Generate random data with 100 samples
    generated_data = generateReservationData(num_samples=100)

    # Display the generated data
    print("Generated Data:")
    print(generated_data.head())


def prepareCostMatrix(reservations, rooms):

    # Perform cross join (cartesian product) between reservations and rooms
    # This will create all possible combinations of reservations and rooms
    cross_join = reservations.assign(key=1).merge(rooms.assign(key=1), on='key').drop('key', axis=1)
    
    # Calculate cost_matrix as the product of 'cost' from reservations and 'costToAssign' from rooms
    cross_join['cost_matrix'] = cross_join['cost'] * cross_join['costToAssign']
    
    # Reshape the DataFrame to have reservationId as index and roomNumber as columns
    cost_matrix = cross_join.pivot_table(index='reservationId', columns='roomNumber', values='cost_matrix')
    maxCost = cost_matrix.max()
    # Normalize the cost_matrix
    #cost_matrix = cost_matrix.div(cost_matrix.max(axis=1), axis=0).mul(100)
    #cost_matrix = cost_matrix.div(maxCost).mul(100)
    
    # Reset index if needed
    # cost_matrix.reset_index(inplace=True)
    
    # Display the result
    print(cost_matrix)
    return cost_matrix
    
#%%    
# # Sample reservations DataFrame
# reservations_data = {
#     'reservationId': [1, 2, 3],
#     'arrivalDate': ['2022-01-15', '2022-02-01', '2022-03-10'],
#     'lengthOfStay': [3, 5, 2],
#     'reservationScore': [8, 7, 9],
#     'upgradeType': ['A', 'B', 'C'],
#     'cost': [100, 150, 200]
# }
reservations = generateReservationData(3)

# # Sample rooms DataFrame
# rooms_data = {
#     'roomId': [101, 102, 103],
#     'roomNumber': ['Room101', 'Room102', 'Room103'],
#     'LoSFragmentation': [2, 3, 1],
#     'costToAssign': [50, 60, 70],
#     'features': ['Feature1', 'Feature2', 'Feature3']
# }
rooms = generateRoomData(3)
prepareCostMatrix(reservations, rooms)

#%%
sample_mat = [np.random.randint(1,10) for _ in range(10)]
print(sample_mat)
# Example usage
scaled_array = scale_input(sample_mat, min_range=9001, max_range=10000)
print("Scaled array:")
print(scaled_array)





