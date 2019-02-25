import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib notebook
import random as rd
sns.set()

x=float(input("Enter x of 0:"))
G = nx.Graph()
i=0
j=1

G.add_node(i, pos=(x,1))
G.add_node(j, pos=(x,2))
G.add_node(2, pos=(2,4.7))
G.add_node(3, pos=(3,4))
pos = nx.get_node_attributes(G, 'pos')

G.add_edge(i, j,)
G.add_edge(j, 2,)
G.add_edge(i, 2)
G.add_edge(i, 3)

plt.figure()


nx.draw_networkx(G, pos)