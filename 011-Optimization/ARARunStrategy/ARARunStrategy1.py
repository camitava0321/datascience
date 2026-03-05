# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:20:07 2024

@author: AMITAVA
"""

from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
import Property

T = 24  # Timezones range from 0 to 23
N = 50  # Number of properties
properties = Property.generate_properties(N)
print(properties[0])

items = [(property.property_code, t) for property in properties for t in property.allowedTimezones]
print(items)

#%%
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
import random
import math

# Optimization Function
def optimize_properties(properties):
    M = len(properties)
    max_properties_per_timezone = (int) (math.ceil(M/T))
    print(max_properties_per_timezone)

    # Create the LP problem
    prob = LpProblem("Cost_Minimization", LpMinimize)

    # Decision variables
    #x = LpVariable.dicts("x", [(i, t) for i in range(M) for t in range(T)], cat='Binary')
    y = LpVariable.dicts("x", items, cat='Binary')
    print(y.keys())
    #print(x.keys())
    #print(y[('CVGNG', 17)])
    #print(x[(0,0)])

    # Objective function
    #prob += lpSum(properties[i].num_rooms * x[(i, t)] for i in range(M) for t in range(T))
    prob += lpSum(property.num_rooms * y[(property.property_code, t)] for property in properties for t in property.allowedTimezones)
    
    # Constraints
    # Each property must run the application exactly once
    #for i in range(M):
    #    prob += lpSum(x[(i, t)] for t in range(T)) == 1
    for property in properties:
        prob += lpSum(y[(property.property_code, t)] for t in property.allowedTimezones) == 1

    # Maximum properties running simultaneously in each timezone
    #for t in range(T):
    #    prob += lpSum(x[(i, t)] for i in range(M)) <= max_properties_per_timezone
    for property in properties:
        prob += lpSum(y[(property.property_code, t)] for t in property.allowedTimezones) <= max_properties_per_timezone
    print(prob)

    prob.writeMPS("test.mps")
    prob.to_json("test.json")
    # Solve the problem
    prob.solve(PULP_CBC_CMD(msg=False))

    # Get results
    total_cost=0
    """
    for i in range(M):
        for t in range(T):
            variables = variables+"X_"+str(i)+"_"+str(t)+": "+str(x[(i, t)].varValue)+","
            total_cost = total_cost + properties[i].num_rooms * x[(i, t)].varValue
        variables = variables+"\n"
        print(variables)
        variables=""
    """
    file1 = open("myfile.txt", "w")
    for property in properties:
        for t in property.allowedTimezones:
            A=y[(property.property_code, t)]
            B=A.varValue
            file1.write(str(A)+": "+ str(B)+", ")
            total_cost = total_cost + property.num_rooms * B
        file1.write("\n");
    file1.close()
    
    #results = [x[(i,t)].varValue for i in range(M) for t in range(T)]
    #total_cost = sum(properties[i].num_rooms * results[i] for i in range(M))
    
    print(f"Total cost: {total_cost}")
    #print(f"Property decisions: {results}")

    # Collect results
    """
    schedule = {t: [] for t in range(T)}
    for i in range(M):
        for t in range(T):
            if x[(i, t)].varValue == 1:
                schedule[t].append(properties[i])

    """
    schedule = {t: [] for t in range(T)}
    for property in properties:
        for t in property.allowedTimezones:
            if y[(property.property_code, t)].varValue == 1:
                print(t)
                schedule[t].append(property)
    return schedule

schedule = optimize_properties(properties)


# Print the schedule
file1 = open("schedule.csv", "w")
file1.write("Timezone,properties,num_properties\n")
for t in sorted(schedule.keys()):
    print(f"Timezone {t} - {len(schedule[t])}")
    file1.write(f"{t},")
    properties = schedule.get(t)
    for property in properties:
        temp = f"{property.property_code}({property.allowedTimezones}) & "
        temp = temp.replace(",", " ")
        print(f"{property.property_code}({property.allowedTimezones})")
        file1.write(temp)
    file1.write(f",{len(schedule[t])}")
    file1.write("\n");
file1.close()



