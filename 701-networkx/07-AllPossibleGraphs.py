import networkx as nx
import matplotlib.pyplot as plot
import itertools

#nodes are linearly connected by n-1 edges
G = nx.path_graph(100)
color_map = ['yellow','#00aaaa','#aaaa00','red','#555577','#00FF00','blue','#00FFFF','#00aa00']
plot.figure(1, figsize=(10,10))

G.add_edge(0,51)
G.add_edge(1,61)
G.add_edge(2,71)
G.add_edge(4,81)
G.add_edge(7,91)
G.add_edge(8,99)
#nx.draw_spring(G,node_color = color_map,with_labels = True, node_size=800)

graphs = list(nx.connected_component_subgraphs(G))
print(len(graphs))


for L in graphs:
    print (L.nodes)
    #nx.draw(L)
    nx.draw(L,node_color = color_map,with_labels = True, node_size=1000)

"""
for SG in (G.subgraph(s) for s in itertools.combinations(G, 3)):
    print(SG.nodes(), SG.edges())
"""
plot.show()




