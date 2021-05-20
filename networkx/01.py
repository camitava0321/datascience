import networkx as nx
import matplotlib.pyplot as plot

G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2,10])
H=nx.path_graph(10)
G.add_nodes_from(H)

G.add_edge(1,2)
e=(2,3)
G.add_edge(*e)

G.add_edges_from([(1,2),(1,3),(2,3),(4,5),(5,10),(5,1)])
G.add_edges_from(H.edges())
print(G.number_of_nodes())
print(G.number_of_nodes())
print(G.nodes())
print(G.edges())
print(G.neighbors(5))

nx.draw(G)
plot.show()