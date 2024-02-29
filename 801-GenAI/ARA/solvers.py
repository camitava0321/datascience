# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:45:11 2024
@author: AMITAVA

Solvers
1) Basic Solver - implements Hungarian Solver to solve a cost matrix

"""

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment

def assignRoomsUsingHungarianSolver(cost_matrix):
    """
    Assigns room numbers to reservation IDs using the Hungarian Method, with minimizing cost.

    Parameters:
    - cost_matrix (pd.DataFrame): Unbalanced cost matrix DataFrame.

    Returns:
    - pd.DataFrame: Assignment DataFrame with room numbers assigned to reservation IDs.
    """
    # Negate the cost matrix to convert minimizing cost to maximizing negative cost
    neg_cost_matrix = -cost_matrix
    # Apply Hungarian Method to find optimal assignment
    row_indices, col_indices = linear_sum_assignment(neg_cost_matrix.values)

    print(row_indices)
    print(col_indices)
    # Create an assignment DataFrame
    assignments = pd.DataFrame(index=neg_cost_matrix.index, columns=['Room_Number'])

    # Fill the assigned room numbers
    for row, col in zip(row_indices, col_indices):
        assignments.at[neg_cost_matrix.index[row], 'Room_Number'] = neg_cost_matrix.columns[col]

    return assignments

