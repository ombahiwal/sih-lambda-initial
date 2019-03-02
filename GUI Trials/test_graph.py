import networkx as nx
import matplotlib.pyplot as plt 
#import csv

#Data  = open('graph.txt', "r", encoding='utf8')
#read = csv.reader(Data)
#G=nx.DiGraph()   # use net.Graph() for undirected graph

#G = nx.read_edgelist(read, create_using=Graphtype, nodetype=str, data=(('weight',float),))
#G = nx.read_edgelist('graph.txt')
"""for x in G.nodes():
      print ("Node:", x, "has total #degree:",G.degree(x), " , In_degree: ", G.out_degree(x)," and out_degree: ", G.in_degree(x))   
for u,v in G.edges():
      print ("Weight of Edge ("+str(u)+","+str(v)+")", G.get_edge_data(u,v))"""
	  
with open("graph.txt") as f:
	G = nx.Graph([line.split()[:2] for line in f])

nx.draw(G)
#nx.draw_circular(G)
plt.show()