# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:20:07 2024

@author: AMITAVA
"""

from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
import Property

T = 24  # Timezones range from 0 to 23
N = 5000  # Number of properties
#Generate the properties
properties = Property.generate_properties(N)
print("A typical property: \n"+str(properties[0]))

#%%
import gurobipy as gp
from gurobipy import GRB
import random
import math

# Optimization Function - 
# Takes the list of properties as input.
# Defines and solves the ILP problem using Gurobi.
# Collects and returns the schedule.
def optimize_schedules(properties):
    M = len(properties)
    max_properties_per_timezone = math.ceil(M / T)
    print("max_properties_per_timezone: " + str(max_properties_per_timezone))

    # Create a new Gurobi model
    model = gp.Model("ARA_Property_Scheduling_by_Cost_Minimization")

    # Decision variables
    y = {}
    for property in properties:
        for t in property.allowedTimezones:
            y[(property.property_code, t)] = model.addVar(vtype=GRB.BINARY, name=f"x_{property.property_code}_{t}")

    # Set the objective function
    model.setObjective(gp.quicksum(property.num_rooms * y[(property.property_code, t)] for property in properties for t in property.allowedTimezones), GRB.MINIMIZE)

    # Add constraints
    # Each property must run the application exactly once
    for property in properties:
        model.addConstr(gp.quicksum(y[(property.property_code, t)] for t in property.allowedTimezones) == 1)

    # Maximum properties running simultaneously in each timezone
    for property in properties:
        model.addConstr(gp.quicksum(y[(property.property_code, t)] for t in property.allowedTimezones) <= max_properties_per_timezone)

    # Write the problem in LP format
    model.write("problem.lp")

    # Solve the problem using Gurobi
    model.optimize()

    # Write results in output file
    total_cost = 0
    with open("output.txt", "w") as file1:
        for property in properties:
            for t in property.allowedTimezones:
                var = y[(property.property_code, t)]
                file1.write(f"{var.VarName}: {var.X}, ")
                total_cost += property.num_rooms * var.X
            file1.write("\n")

    print(f"Total cost: {total_cost}")

    # Collect results and create the schedules
    schedule = {t: [] for t in range(T)}
    for property in properties:
        for t in property.allowedTimezones:
            if y[(property.property_code, t)].X > 0.5:  # Since y is binary, checking if the variable is 1
                schedule[t].append(property)
    return schedule

def print_schedules(schedule):
    # Print the detailed schedule and run schedule
    with open("schedule.csv", "w") as file1, open("detailed_schedule.csv", "w") as file2:
        file1.write("Timezone,properties,num_properties\n")
        file2.write("Timezone,properties,num_properties\n")
        for t in sorted(schedule.keys()):
            print(f"Timezone {t} - {len(schedule[t])}")
            file1.write(f"{t},")
            file2.write(f"{t},")
            properties = schedule.get(t)
            for property in properties:
                temp = f"{property.property_code}({property.allowedTimezones}) & "
                temp = temp.replace(",", " ")
                print(f"{property.property_code}({property.allowedTimezones})")
                file1.write(f"{property.property_code} ")
                file2.write(temp)
            file1.write(f",{len(schedule[t])}")
            file2.write(f",{len(schedule[t])}")
            file1.write("\n")
            file2.write("\n")
    
# Example usage:
# Assuming you have a list of properties as 'properties'
# T = 24  # Define the number of timezones
# schedule = optimize_schedules(properties)
# print_schedules(schedule)
