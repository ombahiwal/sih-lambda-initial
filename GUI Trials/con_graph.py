import networkx as nx
import matplotlib.pyplot as plt
import csv
import numpy as np
def map():
    def get_csv_to_list(file_name):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            f.close()
        return your_list



    list1 = get_csv_to_list("../Integrated/main_output.csv")
    #print(list1)

    G=nx.Graph()

    x=list1[1][3]
    G.add_node(x)
    for i in range(1, len(list1)):
        y=list1[i][4]
        G.add_node(y)
        G.add_edge(x, y)
    nx.draw_networkx(G)
    plt.title('Genysis NAT')
    plt.show()
