
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms import community

# read edge list
g = nx.read_edgelist("C:/Users/aayesha/Desktop/DiscreteProject/OUTFILE.txt")
ug = nx.to_undirected(g)

# print basic info (is the graph ok?)
print(nx.info(ug))

# basic analysis

# number of nodes
print("number of nodes:",nx.number_of_nodes(ug))

#number of edges
print("number of edges:",nx.number_of_edges(ug))

#average clustering
print(nx.average_clustering(ug))

## diameter
#print("Diameter:",nx.diameter(ug))
# this diameter shows ...

# average degree
sum = 0
for n in ug.nodes():
    sum = sum + ug.degree(n)
print("Average degree:", sum/ug.number_of_nodes())

options = {
    'node_color': 'green',
    'node_size': 12,
    'line_color': 'black',
    'linewidths': 0,
    'width': 1,
}
nx.draw(ug,with_labels= True,**options)
plt.show()

