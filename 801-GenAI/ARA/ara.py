# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:40:18 2024
@author: AMITAVA

The most basic solver - demonstrating, given a cost matrix involving reservations and rooms
how Hungarian solver can solve it
"""

from generators import generateCostMatrix, generateReservationData, generateRoomData, prepareCostMatrix
from araMlModel import predict_score, tune_and_evaluate
from solvers import assignRoomsUsingHungarianSolver
from modelSelection import selectModel
import pandas as pd
import time

#%%
# Specify the number of reservations and rooms
num_reservations = 8500
num_rooms = 8000

# Generate the cost matrix
cost_matrix = generateCostMatrix(num_reservations, num_rooms)

# Display the generated cost matrix
print("Generated Cost Matrix:")
print(cost_matrix)

# Record the start time
start_time = time.time()

# Assign rooms using the Hungarian Method
assignments = assignRoomsUsingHungarianSolver(cost_matrix)
# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Display the assignment DataFrame
print("Room Assignments:")
print(assignments)
# Print the elapsed time
print(f"Time taken to assign rooms: {elapsed_time:.6f} seconds")

#%%
data = generateReservationData(200)
print(data.head(5))
#%%
modelType=110
# Call the predict_score function
X, predicted_score = predict_score(data,selectModel(modelType))
# Combine X_test and predictions into a new DataFrame
result_df1 = pd.concat([X.reset_index(drop=True), pd.Series(predicted_score, name='predicted_cost')], axis=1)
reservations = pd.concat([X.reset_index(drop=True), pd.Series(predicted_score, name='cost')], axis=1)

# Display the result DataFrame
print("\nPredicted Results : 1")
print(result_df1)
#%%
# Call the predict_score function
X, predicted_score = predict_score(data,None)
# Combine X_test and predictions into a new DataFrame
result_df1 = pd.concat([X.reset_index(drop=True), pd.Series(predicted_score, name='predicted_cost')], axis=1)

print("\nTuning Model - it might take some time, ~50 seconds")
model = tune_and_evaluate(data)
X, predicted_score = predict_score(data,model)
# Combine X_test and predictions into a new DataFrame
result_df2 = pd.concat([X.reset_index(drop=True), pd.Series(predicted_score, name='predicted_cost')], axis=1)

# Display the result DataFrame
print("\nPredicted Results : 1")
print(result_df1)
print("\nPredicted Results : 2")
print(result_df2)

#%%
data.to_csv('data/reservations.csv')
result_df1.to_csv('output/output1.csv')
#%%
result_df2.to_csv('output/output2.csv')

#%%
rooms = generateRoomData(50)
print(rooms.head(5))
#%%
reservations = reservations.sort_values(by='cost')
rooms = rooms.sort_values(by='costToAssign')
cost_matrix = prepareCostMatrix(reservations, rooms)
# Record the start time
start_time = time.time()

# Assign rooms using the Hungarian Method
assignments = assignRoomsUsingHungarianSolver(cost_matrix)
# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Display the assignment DataFrame
print("Room Assignments:")
print(assignments)
# Print the elapsed time
print(f"Time taken to assign rooms: {elapsed_time:.6f} seconds")

# Join the two DataFrames based on the 'reservationId' column
merged_df = pd.merge(reservations, assignments, on='reservationId', how='inner')

# Display the merged DataFrame
print(merged_df)
#%%
cost_matrix.to_csv("output/cost_matrix.csv")
reservations.to_csv("data/reservations.csv")
rooms.to_csv("data/rooms.csv")
merged_df.to_csv("output/results.csv")

