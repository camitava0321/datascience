__all__ = ['printBetweennessCentrality', 'printAdjacencyMatrix']


#Test Graph
#G=nx.barabasi_albert_graph(100,3)

def printBetweennessCentrality(graph, csvFileName):
    import networkx as nx
    import numpy
    import csv
    numpy.set_printoptions(threshold=numpy.nan, linewidth=1000)
    C=nx.algorithms.centrality.betweenness_centrality(graph)
    #print(C)
    outcsv = csv.writer(open(csvFileName, 'w'))

    for node in graph.nodes():
        J=C[node]
        outcsv.writerow([node, J])
        
def printAdjacencyMatrix(graph,filename):
    import networkx as nx
    import numpy
    import csv
    numpy.set_printoptions(threshold=numpy.nan, linewidth=1000)
    B=nx.to_numpy_matrix(graph, dtype=int)

    # Open a file in write mode
    fo = open(filename, "w")
    fo.seek(0)
    line = fo.write( str(B) )

    # Close opend file
    fo.close()





#Tests
#printBetweennessCentrality(G,"centrality.csv")