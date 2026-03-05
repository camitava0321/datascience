The Optimization Problem : ARA Property cheduling by Cost_Minimization

We have M properties, distributed across 24 timezones (1 hr span for each TZ).
Each property has different number of rooms.
ARA application(takes C minutes) to run. 
It needs to run in each of these M properties at a specific time of that property (say 1 AM). 
The maximum number of properties that can run this application simultaneously in a timezone is M/24. 
Cost of running ARA is proportional to the number of rooms in a property. 

Our objective is to reduce this cost, subject to
Constraints:
a) if the number of properties in a TZ is more than M/24, shift the excess number of properties in the other timezones allowed for this property. 

The output will be a schedule per timezone depicting which properties to run in that timezone.

Solution:
We use Integer Linear Programming (ILP) combined with a scheduling algorithm. 

Steps:

1. Model the Problem:
        Let R_i​ be the number of rooms in property i (where i∈{1,2,…,M}).
        Let T_i​ be the given initial timezone for property i.
        The cost of running ARA at property i is proportional to R_i​.
        Let x_i_t​ be a binary decision variable where x_i_t=1 if property i runs ARA in timezone t, otherwise x_i_t=0.

    Constraints:
        ARA must run at each property exactly once: ∑_t x_i_t=1 for each property i.
        The maximum number of properties that can run ARA simultaneously in any timezone t is M/24: 
		∑_i x_i_t≤M/24  for each timezone t.
        Properties initially assigned to timezone t can shift to t-1 or t+1 if needed to ensure the constraint.

    Objective Function:
        Minimize the total cost of running ARA:
		∑_i_t R_i * x_i_t .

2. Formulate the Integer Linear Programming Model

Define:
    R_i​ as the number of rooms in property i.
    x_i_t​ as the binary decision variable for property i in timezone t.

Objective:
Minimize ∑_i(=1 to M) ∑_t(=0 to T−1) R_i * x_i_t​

Subject to:

    ∑_t(=0 to T−1) x_i_t=1 for each property i (each property runs ARA exactly once).
    ∑_i(=1 toM) x_i_t≤M/24 for each timezone t (maximum simultaneous runs in each timezone).

Solving the ILP Model
We can solve this ILP model using various optimization solvers like Gurobi, CPLEX, or open-source solvers like CBC or GLPK. We have used PuLP with Python