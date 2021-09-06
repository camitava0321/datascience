#!/usr/bin/env python
# coding: utf-8

# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *


# In[18]:


from qiskit import BasicAer
from qiskit.aqua import QuantumInstance
from qiskit.aqua import Operator, run_algorithm
from qiskit.aqua.input import EnergyInput
from qiskit.aqua.translators.ising import portfolio
from qiskit.aqua.translators.data_providers import RandomDataProvider
from qiskit.aqua.algorithms import VQE, QAOA, ExactEigensolver
from qiskit.aqua.components.optimizers import SPSA, COBYLA
from qiskit.aqua.components.variational_forms import RY
import qiskit.aqua.translators.ising.vehicle_routing as vr
import numpy as np
import datetime
import networkx as nx
import matplotlib.pyplot as plt
import math


# In[19]:


# Initialize the problem by defining the parameters
n = 4  # number of nodes + depot (n+1)
K = 1  # number of vehicles


# In[20]:


#DataPrep
#Number of zones
no_zones=20
#Hub Coordinates
x0 = 1079; y0 = 507
#Customer coordinates
xs_orig = np.array([1148,1093,1014,951,971,1035,978,958,873,797,861,780,702,775,659,647,577,550,552,621,431,405,340,190,128,189,352,289,284,152,90,71,89,123,158,381,377,438,528,599,598,860,814,894,1070,1129,1071,1291,1333,1388,1426,1411,1363,1491,1568,1570,1481,1430,1367,1360])
ys_orig = np.array([539,572,587,585,518,744,771,710,741,722,674,632,568,569,712,775,773,678,612,638,654,722,721,726,697,648,510,518,454,413,465,387,220,147,204,181,118,153,54,42,105,104,36,27,27,50,95,122,71,111,167,244,285,490,492,555,696,733,722,715])
print (len(ys))
XS = np.split(xs,no_zones)
YS = np.split(ys,no_zones)
print ("XS:",XS,'\n')
print ("YS:",YS,'\n')
#Create nodes dictionary
nodes = {0:{'x':x0, 'y':y0, 'color':'#bbbb00','id':0}}
zones = [[]] * no_zones
zonecount=0; nodecount=0
for xzone in XS:
    yzone=YS[zonecount]
    zones[zonecount] = [0]
    #print("zone: ",zonecount," : ",xzone,yzone)
    i=0
    for x in xzone:
        nodes[nodecount+1] = {'x':x,'y':yzone[i], 'color':'#00bbee', 'id':(nodecount+1)}
        zones[zonecount].append(nodecount+1)
        i = i+1
        nodecount=nodecount+1
    print(zones[zonecount])
    zonecount=zonecount+1
print(nodes)


# In[21]:


def get_xs_and_ys_for_a_zone (zone_id):
    xs=[] ; ys=[]
    i=0
    for node in zones[zone_id]:
        xs.append(nodes.get(node).get('x'))
        ys.append(nodes.get(node).get('y'))
        i=i+1
    return xs,ys

#Create a random customer-customer distance matrix
def create_distance_matrix_for_zone(zone_id):
    xs, ys = get_xs_and_ys_for_a_zone(zone_id)
    print ('xs: ',xs,'ys: ',ys)
    n=len(xs)
    instance = np.zeros([n, n])
    for i in range(0, n):
        for j in range(i + 1, n):
            #print ('nodes = ',(xs[i],ys[i]),(xs[j],ys[j]))
            #Distance squared
            #instance[i, j] = (xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2
            instance[i, j] = math.sqrt((xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2)
            #jith element is made the same as ijth element - so that the matrix is a symmetric
            instance[j, i] = instance[i, j]
            #print (instance[i,j])
    return instance

def plot_nodes (graph, zone_id):
    xs, ys = get_xs_and_ys_for_a_zone(zone_id)
    nodelist=zones[zone_id]
    # plt.gca().invert_yaxis()
    # plt.gca().invert_xaxis()
    n=len(xs)
    keys = range(len(xs))
    i=0
    for k in nodelist:
        pos[k] = (xs[i], ys[i])
        i=i+1
    print(pos)
    plt.figure()
    fig = plt.gcf()
    ax=fig.gca()
    fig.set_size_inches(12,8)
    plt.title('Customer Graph')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Add Edges
    #for i in keys:
    #    for j in range(i+1, n):
    #        X.add_edge(i, j, length=int(instance[i][j]))
    # Add Edges
    i=0;j=1
    for i in range(len(nodelist)):
        for j in range(i+1, n):
            node_a=nodelist[i]; node_b=nodelist[j]
            X.add_edge(node_a, node_b, length=int(instance[i][j]))

    nx.draw_networkx(graph, pos, node_size=350, edge_color='#cccccc',ax=ax,
                     nodelist=nodelist, node_color='#00bbee', alpha=0.7, with_labels=True)
    labels = nx.get_edge_attributes(graph, "length")
    print(labels)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    #plt.xticks((0, 0.5, 1), ("0", "0.5", "1"))
    #plt.grid(True)
    plt.show()

def get_hamiltonian_paths(graph, target):
    allpaths = nx.all_simple_paths(graph, source=0, target=target)
    #Print Hamiltonian Paths
    selectedPaths = [path for path in list(allpaths) if len(path)==4]
    return selectedPaths   

def get_min_cost_function(selectedPaths) :
    min_cost=100000
    min_cost_path = None
    for path in list(selectedPaths):
        total_length=5
        for k in range(len(path)-1):
            x,y = path[k], path[k+1]
            edge = X[x][y]
            length = edge['length']
            total_length += length
        print('{}: {}'.format(path, total_length))
        if min_cost>total_length:
            min_cost=total_length
            min_cost_path = path
    return min_cost, min_cost_path
# Visualize the solution
def draw_tsp_solution(G, order, pos):
    plt.figure()
    fig = plt.gcf()
    fig.set_size_inches(12,8)
    plt.title('Customer Graph : Cost = '+ str(min_cost))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()

    G1 = G.copy()
    edges = list(G1.edges())
    G2 = G1.remove_edges_from(edges)
    G1 = G1.to_directed()
    n = len(order)
    i=0;j=1
    for i in range(len(order)-1):
        j=i+1
        node_a=order[i]; node_b=order[i+1]
        G1.add_edge(node_a, node_b, length=int(instance[i][j]))
    G1.add_edge(order[j], order[0],length=int(instance[j][0]))
    """
    for i in range(n-1):
        j = (i+1)#(i + 1) % n
        print(order[i],order[j])
        G1.add_edge(order[i], order[j],length=int(instance[order[i]][order[j]]))
    G1.add_edge(order[j], order[0],length=int(instance[order[j]][order[0]]))
    """
    #create node colors array
    colors = np.full(n,'#00bbee')
    colors[order[0]]='#bbbb00'
    default_axes = plt.axes(frameon=True)
    ax=fig.gca()
    nx.draw_networkx(G1, pos, node_size=350, edge_color='#cccccc', ax=ax, 
                     node_color=colors, alpha=0.7, arrowsize=20)
    labels = nx.get_edge_attributes(G1, "length")
    print(labels)
    nx.draw_networkx_edge_labels(G1, pos, edge_labels=labels)
    #plt.xticks((0, 0.5, 1), ("0", "0.5", "1"))
    plt.grid(True)
    plt.show()


# In[ ]:


#Classical - Brute force solution
solutions=[]
for zone_id in range(len(zones)):
    nodes_for_zone=zones[zone_id]
    instance=create_distance_matrix_for_zone(zone_id)
    print ("\n----For Zone %s----"%zone_id)
    print ('distance matrix : \n',instance)
    X = nx.Graph()
    pos = {}
    plot_nodes(X,zone_id)
    selectedPaths = get_hamiltonian_paths(X,nodes_for_zone[3])
    print('All Hamiltonian Paths from 0-%s :\n'%nodes_for_zone[3],list(selectedPaths),'\n')
    min_cost, min_cost_path = get_min_cost_function(selectedPaths)
    print('Minimum Cost for Zone {}: {} : {}'.format(zone_id, min_cost_path, min_cost))
    
    #Create the adjacency matrix
    x=np.zeros((n,n), dtype=int)
    #for k in range(len(min_cost_path)-1):
    #    x[min_cost_path[k]][min_cost_path[k+1]]=1
    #x[min_cost_path[k+1]][0]=1
    #x=x.flatten()
    #print(x) 


    draw_tsp_solution(X,min_cost_path,pos)
    solutions.append(min_cost_path)


# In[79]:


def get_coordinates_array(xs,ys):
    coords=[[]] * len(xs)
    for i in range(len(xs)):
        coords[i]=([xs[i],ys[i]])
    return coords

def shift_solution_nodes(z):
    z2 = np.zeros(len(z), dtype=int)
    i = z.index(0)
    roll_by = len(z)-i
    z1 = np.roll(z,roll_by)
    keys = list(pos.keys())
    for i in range(len(z)):
        z2[i] = keys[z1[i]]
    return z2


# In[81]:


from qiskit.aqua.translators.ising import tsp
for zone_id in range(len(zones)):
#n = 3
coord=get_coordinates_array(xs,ys)
print (coord)
#num_qubits = n ** 2
#ins = tsp.random_tsp(n)
#insList = list(ins)
#It is important to real
"""
coord = [[5.5100391375334326, 7.9872448071072135],
    [7.559639370825573, 2.2741572523311104],
    [4.357164910072608, 6.055345738402197],
    [0.4293142250893367, 5.7923100691603135]]
"""
ins = tsp.TspData(name='AMC', dim=4, coord=coord, w=instance)
print(ins)
qubitOp, offset = tsp.get_tsp_qubitops(ins)
algo_input = EnergyInput(qubitOp)
print('Paulis: ',qubitOp.aer_paulis,'\n')
print('Flat Paulis: ',qubitOp.get_flat_pauli_list(),'\n')
#print('\nmatrix: ',qubitOp.matrix,'\n')
print('num qubits: ',qubitOp.num_qubits,'\n')
print('Algorithm Input: ',algo_input,'\n')
#Making the Hamiltonian in its full form and getting the lowest eigenvalue and eigenvector
ee = ExactEigensolver(qubitOp, k=1)
result = ee.run()
print('energy:', result['energy'])
print('tsp objective:', result['energy'] + offset)
import sys
np.set_printoptions(threshold=1000)
print(result['eigvecs'])
x = tsp.sample_most_likely(result['eigvecs'][0])
print('feasible:', tsp.tsp_feasible(x))
z = tsp.get_tsp_solution(x)
print('solution:', z)
print('solution objective:', tsp.tsp_value(z, ins.w))
z2 = shift_solution_nodes(z)
print(z2)
print(pos)
#draw_tsp_solution(G, best_order, colors, pos)
draw_tsp_solution(X, z2, pos)


# In[82]:





# In[95]:





# In[109]:





# In[96]:





# In[106]:


seed = 10598
import logging
from qiskit.aqua import set_qiskit_aqua_logging
set_qiskit_aqua_logging(logging.DEBUG)  # choose INFO, DEBUG to see the log

#Now we use the VQE that needs two algorithms as sub-components
#Sub-Component 1 : a local optimizer, we use SPSA/COBYLA(Constrained Optimization BY Linear Approximation) 
#from qiskit.aqua.components.optimizers
cobyla = COBYLA()
cobyla.set_options(maxiter=250)
spsa = SPSA(max_trials=200)
#Sub-Component 2 : a variational form, we use Ry from qiskit.aqua.components.variational_forms
#ry = RY(qubitOp.num_qubits, depth=3, entanglement='full')
ry = RY(qubitOp.num_qubits, depth=3, entanglement='linear')
vqe = VQE(qubitOp, ry, cobyla, 'matrix')
#vqe = VQE(qubitOp, ry, spsa, 'matrix')
vqe.random_seed = seed

backend = BasicAer.get_backend('statevector_simulator')
quantum_instance = QuantumInstance(backend, seed_transpiler=seed)

import time
start_time=time.time()
result = vqe.run(quantum_instance)
print("Ran For %s seconds" % (time.time() - start_time))
"""
algorithm_cfg = {
    'name': 'VQE',
    'operator_mode': 'matrix'
}

optimizer_cfg = {
    'name': 'SPSA',
    'max_trials': 300
}

var_form_cfg = {
    'name': 'RY',
    'depth': 5,
    'entanglement': 'linear'
}

params = {
    'problem': {'name': 'ising', 'random_seed': seed},
    'algorithm': algorithm_cfg,
    'optimizer': optimizer_cfg,
    'variational_form': var_form_cfg,
    'backend': {'provider': 'qiskit.BasicAer', 'name': 'statevector_simulator'}
}
result = run_algorithm(parahms,algo_input)
"""


# In[110]:


print(result)    
print('energy:', result['energy'])
print('time:', result['eval_time'])
#print('tsp objective:', result['energy'] + offset)
x = tsp.sample_most_likely(result['eigvecs'][0])
print('feasible:', tsp.tsp_feasible(x))
z = tsp.get_tsp_solution(x)
print('solution:', z)
z2 = shift_solution_nodes(z)
print(z2)
print('solution objective:', tsp.tsp_value(z, ins.w))
draw_tsp_solution(X, z2, pos)


# In[1]:


#Aggregation
#You will have 20 z arrays - 
#[[0,1,2,3], [0,7,6,8], [0,9,11,10]...]
#3, 8, 10, .... - with these create an array
edges = []
nodes_to_join = []
k=0
for solution in solutions:
#3 & 8 - whether their distance is less than threshold
    #Select nodes to join
    for i in range(len(solution)-1):
        edges.append([solution[i],solution[i+1],'#555555',1])
    print (solution)
    if k%2==0: #Even
        nodes_to_join.append(solution[3])
    else : #Odd
        nodes_to_join.append(solution[1])
        nodes_to_join.append(solution[3])
    k=k+1

print(nodes_to_join)
continue_joining=True
while(continue_joining):
    deleted=False
    for k in range(len(nodes_to_join)-1):
        nodeA=nodes_to_join[k]
        nodeB=nodes_to_join[k+1]
        distance = math.sqrt((nodes[nodeA]['x'] - nodes[nodeB]['x']) ** 2 + (nodes[nodeA]['y'] - nodes[nodeB]['y']) ** 2)
        print(nodeA,nodeB," --- ",distance)
        if distance < 100:
            edges.append([nodeA,nodeB,'#cc0000',2])
            nodes_to_join.remove(nodeA)
            nodes_to_join.remove(nodeB)
            deleted=True
            break
    print(nodes_to_join)
    if deleted==False:
        continue_joining=False

#if it is - the join 3-8 and remove 3,8 from the array
for k in range(len(nodes_to_join)):
    edges.append([nodes_to_join[k],0,'#0000cc',2])


# In[2]:


def plot_entire_graph (graph):
    xs =[x0]; ys = [y0]
    nodelist=[]
    for i in range(len(xs_orig)):
        xs.append(xs_orig[i])
        ys.append(ys_orig[i])
        nodelist.append(i)
    nodelist.append(60)
    print(nodelist)
    n=len(xs)
    keys = range(n)
    for i in nodelist:
        pos[i] = (xs[i], ys[i])
    print(pos)
    plt.figure()
    fig = plt.gcf()
    ax=fig.gca()
    fig.set_size_inches(30,26)
    plt.title('Customer Graph')
    plt.xlabel('X')
    plt.ylabel('Y')
    graph = graph.to_directed()
    #Add Nodes to graph
    graph.add_nodes_from(nodelist)
    # Add Edges
    for edge in edges:
        graph.add_edge(edge[0], edge[1], color=edge[2], weight=edge[3])
    edges1 = graph.edges()
    colors = [graph[u][v]['color'] for u,v in edges1]
    weights = [graph[u][v]['weight'] for u,v in edges1]
    # Add Edges
    """
    i=0;j=1
    for i in range(len(nodelist)):
        for j in range(i+1, n):
            node_a=nodelist[i]; node_b=nodelist[j]
            X.add_edge(node_a, node_b, length=int(instance[i][j]))
    """
    nx.draw_networkx(graph, pos, node_size=550, ax=ax,
                     edge_color=colors, width=weights,
                     node_color='#00bbee', alpha=0.7, with_labels=True)
    #labels = nx.get_edge_attributes(graph, "length")
    #print(labels)
    #nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    #plt.xticks((0, 0.5, 1), ("0", "0.5", "1"))
    plt.grid(True)
    plt.show()


# In[3]:


X = nx.Graph()
pos = {}
plot_entire_graph(X)


# In[ ]:




