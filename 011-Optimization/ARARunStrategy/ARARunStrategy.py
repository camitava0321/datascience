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
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
import random
import math

# Optimization Function - 
# Takes the list of properties as input.
# Defines and solves the ILP problem using PuLP.
# Collects and returns the schedule.
def optimize_schedules(properties):
    M = len(properties)
    max_properties_per_timezone = (int) (math.ceil(M/T))
    print("max_properties_per_timezone: "+str(max_properties_per_timezone))

    # Create the LP problem
    prob = LpProblem("ARA Property cheduling by Cost_Minimization", LpMinimize)

    # Decision variables
    items = [(property.property_code, t) for property in properties for t in property.allowedTimezones]
    #print(items)
    y = LpVariable.dicts("x", items, cat='Binary')
    #print(y.keys())

    # Create the Objective function
    prob += lpSum(property.num_rooms * y[(property.property_code, t)] for property in properties for t in property.allowedTimezones)
    
    # Constraints
    # Each property must run the application exactly once
    for property in properties:
        prob += lpSum(y[(property.property_code, t)] for t in property.allowedTimezones) == 1

    # Maximum properties running simultaneously in each timezone
    for property in properties:
        prob += lpSum(y[(property.property_code, t)] for t in property.allowedTimezones) <= max_properties_per_timezone

    # Write the problem in two format that cann be loaded in a different solver    
    prob.writeMPS("problem.mps")
    prob.to_json("problem.json")
    # Solve the problem using PuLP
    prob.solve(PULP_CBC_CMD(msg=False))

    # Write results in output file
    total_cost=0
    file1 = open("output.txt", "w")
    for property in properties:
        for t in property.allowedTimezones:
            A=y[(property.property_code, t)]
            B=A.varValue
            file1.write(str(A)+": "+ str(B)+", ")
            total_cost = total_cost + property.num_rooms * B
        file1.write("\n");
    file1.close()
    
    print(f"Total cost: {total_cost}")

    # Collect results and create the schedules
    schedule = {t: [] for t in range(T)}
    for property in properties:
        for t in property.allowedTimezones:
            if y[(property.property_code, t)].varValue == 1:
                schedule[t].append(property)
    return schedule

def print_schedules(schedule):
    # Print the detailed schedule and run schedule
    file1 = open("schedule.csv", "w")
    file2 = open("detailed_schedule.csv", "w")
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
        file1.write("\n");
        file2.write("\n");
    file1.close()
    file2.close()
    
#%%
schedule = optimize_schedules(properties)
print_schedules(schedule)
