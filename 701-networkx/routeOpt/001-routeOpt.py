import networkx as nx
import matplotlib.pyplot as plot
#print ('networkx version : ', networkx.__version__)
import matplotlib.patches as mpatches

import json
#import flask
from networkx.readwrite import json_graph

import threading
import time
import queue

globalPath=[]
globalEdge=[]
globalLegend=[]
globalExperimentID=0
maxExperiments=4
destDegree=5

def setNodeAttributes(graph):
    # this d3 example uses the name attribute for the mouse-hover value,
    # so add a name to each node
    for n in graph:
        if n==0:
            graph.nodes[n]["name"] = 'HUB'
            graph.nodes[n]['color']='#FFFF00'  #spl color of hub
        else:
            graph.nodes[n]["name"] = n
            graph.nodes[n]['color']='#DDDDDD'  #default color of all nodes

def getNodeColors(graph):
    nodeColors=[]
    colors = nx.get_node_attributes(graph, "color")
    for color in colors:
        nodeColors.append(colors[color])
    return(nodeColors)

def setEdgeAttributes(graph):
    new_edges = []
    for edge in graph.edges():
        u = edge[0]
        v= edge[1]
        weight=u+v #one can use any strategy to assign weights here
        color='#BBBBBB'
        new_edges.append((u,v,{'weight':weight, 'label':weight, 'color':color}))
    graph.update(edges=new_edges)

def getEdgeColors(graph):
    edgeColors=[]
    colors = nx.get_edge_attributes(graph, "color")
    for color in colors:
        edgeColors.append(colors[color])
    return(edgeColors)

def getEdgeLabels(graph, method='list'):
    edgeLabels=[]
    labels = nx.get_edge_attributes(G, "label")
    for label in labels:
        edgeLabels.append(labels[label])
    return_object=edgeLabels
    if method=='string':
        return_object = ','.join(map(str, edgeLabels)) 
    if method=='dict':
        return_object=labels
    return (return_object)
    
    
    return nx.get_edge_attributes(G, "label")


def highlightPath (graph, path):
    count=0
    while count < len(path)-1:
        u=path[count]
        v=path[count+1]
        graph.nodes[u]['color']='#BBBBFF'
        graph.nodes[v]['color']='#BBBBFF'
        graph[u][v]['color']='black'
        count=count+1
    #color the initial node
    graph.nodes[path[0]]['color']='#FFFF00'
    #color the final node
    graph.nodes[path[len(path)-1]]['color']='#00BB00'

    
def writeGraph(graph):
    # print the adjacency list
    for line in nx.generate_adjlist(graph):
        print(line)
        # write edgelist to grid.edgelist
        nx.write_edgelist(graph, path="grid.edgelist", delimiter=":")


def printDetails(graph):
    print(nx.info(graph))
    print(nx.info(graph, n=4))
    print('Number of Nodes: ', graph.number_of_nodes())
    print('Nodes: ', graph.nodes())
    print('Edges: ', graph.edges())
    print('Neighbour of Node 4: ', graph.neighbors(4))
    print('Degree Histogram : ', nx.degree_histogram(graph))

    pathlengths = []
    
    print("source vertex {target:length, }")
    for v in graph.nodes():
        spl = dict(nx.single_source_shortest_path_length(graph, v))
        print(f"{v} {spl} ")
        for p in spl:
            pathlengths.append(spl[p])
    
    print()
    print(f"average shortest path length {sum(pathlengths) / len(pathlengths)}")
    
    # histogram of path lengths
    dist = {}
    for p in pathlengths:
        if p in dist:
            dist[p] += 1
        else:
            dist[p] = 1
    
    print()
    print("length #paths")
    verts = dist.keys()
    for d in sorted(verts):
        print(f"{d} {dist[d]}")
    
    print(f"radius: {nx.radius(graph)}")
    print(f"diameter: {nx.diameter(graph)}")
    print(f"eccentricity: {nx.eccentricity(graph)}")
    print(f"center: {nx.center(graph)}")
    print(f"periphery: {nx.periphery(graph)}")
    print(f"density: {nx.density(graph)}")


def getShortestPaths(graph, source, target, k, weight=None):
    from itertools import islice
    #based on algorithm by Jin Y. Yen 1. Finding the first K paths requires O(KN3) operations.
    return list(
        islice(nx.shortest_simple_paths(G, source, target, weight=weight), k)
    )

    

def runService(graph):
    # write json formatted data
    d = json_graph.node_link_data(graph)  # node-link format to serialize
    # write json
    json.dump(d, open("routeOpt.json", "w"))
    print("Wrote node-link JSON data")
    
    # Serve the file over http to allow for cross origin requests
    '''
    #app = flask.Flask(__name__, static_folder="")
    
    
    @app.route("/")
    def static_proxy():
        return app.send_static_file("force.html")
    
    
    print("\nGo to http://localhost:8000 to see the example\n")
    app.run(port=8000)
    '''

# Modify Graph - update the weight of the last leg
def modifyEdgeWeight(graph, newWeight):
   count = 0
   global globalExperimentID
   while count < maxExperiments:
      time.sleep(5) #in seconds
      print('\n--------------------')
      globalExperimentID=count+1
      print('Experiment : ',globalExperimentID)
      edgeKey=globalEdge
      u=edgeKey[0]
      v=edgeKey[1]
      print(u,v)
      #edges = ((u,v, {'weight':newWeight, 'label':newWeight, 'color':'red'}))
      #global G
      #G.update(edges=edges)
      newWeight1 = graph[u][v]['weight'] + newWeight
      graph[u][v]['weight']=newWeight1
      graph[u][v]['label']=newWeight1
      graph[u][v]['color']='red'
      print(G[u][v])
      count = count+1

#Quantum Solution will be used for this function
def calculateShortestPath(graph, source, destination):
    print('Shortest Paths:')
    for path in getShortestPaths(graph, source, destination, 2, weight='weight'):
        print(path)
    
    print('Shortest Path:A*')
    path = nx.astar_path(graph, source, destination, weight="weight")
    cost = nx.astar_path_length(graph, source, destination, weight='weight')
    print(path, ' cost: ', cost)
    return(path, cost)

def reCalculateShortestPath(graph, source, destination):
   count = 0
   global globalPath
   global globalEdge
   global globalLegend
   while count < maxExperiments:
      time.sleep(5) #in seconds
      print('ReCalculation : ',globalExperimentID)
      globalPath, cost=calculateShortestPath(graph, source, destination)
      print(globalPath,cost)
      setNodeAttributes(graph)
      highlightPath(graph,globalPath)
      globalEdge=globalPath[-2:]
      label=str(globalExperimentID)+': '+'->'.join(str(x) for x in globalPath) \
                                                   + ' : '+str(cost)
      globalLegend.append(mpatches.Patch(lw=0.4, color='black', label=label))
      count = count+1


def plotNetwork(graph, pos, legend=None):
    plot.figure(3,figsize=(15,10)) 
    #nx.draw(G,pos)
    
    # plot nodes
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color=getNodeColors(graph),
        edgecolors='#888888')
    
    # plot edges
    nx.draw_networkx_edges(graph, pos, width=1, edge_color=getEdgeColors(graph)) #edgelist=elarge, 
    #nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed")
    
    # plot labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family="sans-serif")
    nx.draw_networkx_edge_labels(graph, pos, font_size=9, font_family="sans-serif", edge_labels=getEdgeLabels(graph,'dict'))
    
    if legend is not None:
        plot.legend(handles=legend)

    plot.show()
    

def threadPlotNetwork(graph, pos):
   count = 0
   global globalPath
   global globalEdge
   while count < maxExperiments:
      time.sleep(6) #in seconds
      print('Plot : ',globalExperimentID)
      #red_patch = mpatches.Patch(color='red', label='0-2-3-4')
      plotNetwork(graph,pos, globalLegend)
      count = count+1

    
#%% - Initialize Graph
G=nx.Graph()

n=30  #0 - hub, n-1 customers


#Get an arbitrary graph
#n - no of nodes, m - Number of edges to attach from a new node to existing nodes
G=nx.barabasi_albert_graph(n=n,m=3)
setNodeAttributes(G)
setEdgeAttributes(G)

pos = nx.spring_layout(G, weight=getEdgeLabels(G,'string'))

#Print various descriptions of the network
writeGraph(G)
printDetails(G)

#Plot the network
plotNetwork(G,pos)

exitFlag = 0
dest=17 #Default Destination Node
#Find a destination node that has enough approaches
print('Voterank :',nx.voterank(G))
for d in nx.voterank(G):
    if d>15:
        dest=d
        break


destDegree=nx.degree(G,nbunch=dest)
print('destination node: ',dest, ' degree: ',destDegree)    
maxExperiments = min(maxExperiments,destDegree)

#%% - Calculate Shortest Path & Highlight the path
globalPath, cost=calculateShortestPath(G, 0, dest)
highlightPath(G,globalPath)
globalEdge=globalPath[-2:]


#Arrange the threads
class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      print ("Starting " + self.name+'\n')
      if self.name=='modifyWeight':
          modifyEdgeWeight(G, 50)
      if self.name=='plot':
          threadPlotNetwork(G,pos)
      else:
          print('recalculating shortest path')
          reCalculateShortestPath(G,0,dest)
      print ("Exiting " + self.name+'\n')


#First modify cost, then recalculate  alternate route
threadList = ["modifyWeight", "recalculate", "plot"]
nameList = ["One", "Two", "Three", "Four", "Five"]
#queueLock = threading.Lock()
workQueue = queue.Queue(maxExperiments)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1


# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
   

    
#H = nx.read_edgelist(path="06-routeOpt.data", delimiter="!")
#nx.draw(H, with_labels = True, node_size=500) #node_color = color_map,)
#plot.show()

#runService(G)