import re
import sys

import networkx as nx

G = nx.grid_2d_graph(71, 71)
for line in sys.stdin.readlines():
    G.remove_node(tuple(map(int, re.findall(r'-?\d+', line))))
    try:
        nx.shortest_path_length(G, min(G), max(G))
    except:
        print(line)
        break
