import sys

import networkx as nx

ls = [l.strip() for l in sys.stdin.readlines()]
G = nx.Graph()
for l in ls:
    G.add_edge(*l.split('-'))
t = 0
for c in nx.enumerate_all_cliques(G):
    if len(c) != 3:
        continue
    if any(x[0] == 't' for x in c):
        t += 1
print(t)
