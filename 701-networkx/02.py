import networkx as nx
import matplotlib.pyplot as plot
import netutilities as nu

#threshold=numpy.nan - to print entire matrix - no ..., business
#linewidth=1000 - entire matrix row in one line
#numpy.set_printoptions(threshold=numpy.nan, linewidth=1000)

#n - no of nodes, m - Number of edges to attach from a new node to existing nodes
G=nx.barabasi_albert_graph(n=150,m=10)

print(G.number_of_nodes())
print(G.number_of_edges())
#print(G.nodes())
#print(G.edges())

nx.draw(G)
plot.show()


A=nx.adjacency_matrix(G)
#print(A)
B=nx.to_numpy_matrix(G, dtype=int)
#print(B)

#nx.write_multiline_adjlist(G,path="abc")


nu.printAdjacencyMatrix(G,"adjacencyMatrix.txt")
nu.printBetweennessCentrality(G,"centrality.csv")

