import csv #import the Python CSV library
import networkx as nx #import NetworkX
import numpy as np #import numpy for
import matplotlib.pyplot as plt #import matplotlib for plotting/drawing grpahs
import operator #standard python library used for sorting

g = nx.read_graphml("airlines.graphml")
degree_sequence=sorted(nx.degree(g).values(),reverse=True) # degree sequence
#print "Degree sequence", degree_sequence
dmax=max(degree_sequence)


N = g.order() #G.order(), gives number of nodes 
L = g.size() #G.size(), gives number of edges

avg_deg = 2*float(L)/N #calculate average degree


#print out statistics
print "Nodes: ", N
print "Edges: ", L
print "Average degree: ", avg_deg

if not 'avg_path_length' in globals(): #only calculate this if its not been calculated before
    max_path_length = 0
    total = 0.0
    for n in g: #iterate over all nodes
        path_length=nx.single_source_shortest_path_length(g, n) # generate shortest paths from node n to all others
        total += sum(path_length.values()) #total of all shortest paths from n
    
        if max(path_length.values()) > max_path_length: #keep track of longest shortest path we see.
            max_path_length = max(path_length.values())         
    avg_path_length = total / (N*(N - 1)) #calculate average.

print "Average path length %f" % avg_path_length #print average path
print "Network Diameter %d" % max_path_length #print diameter

plt.loglog(degree_sequence,'b-',marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")

plt.savefig("degree_histogram.png")
plt.show()


if not 'bet_cen' in globals(): #only calculate this if its not been calculated before
    bet_cen = nx.betweenness_centrality(g)
    clo_cen = nx.closeness_centrality(g)
    eig_cen = nx.eigenvector_centrality(g)
#Histogram of in-degrees

print "Betweenness mean: %f" % np.mean(bet_cen.values()) #mean betweenness

