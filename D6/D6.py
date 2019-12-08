import networkx as nx
from time import time
t0 = time()
star_map = open(r'C:\Users\Panos\Google Drive\ECE\Python Files\Advent of Code 2019\D6\input.txt','r')

G = nx.DiGraph() # Change to nx.Digraph() for Part 1

for line in star_map:
    parent, child = line.strip().split(')')
    G.add_edge(parent, child)

leafs = [x for x in G.nodes() if G.out_degree(x)==0 and G.in_degree(x)==1]
num_of_paths = 0
orbits = set()
for leaf in leafs:
    for path in nx.all_simple_paths(G,'COM',leaf):
        while len(path) > 1:
            orbits.add(tuple(path))
            path.pop()
 
for orbit in orbits:
    num_of_paths += len(orbit) - 1
print(num_of_paths)

G = G.to_undirected()
print(len(nx.shortest_path(G,'YOU','SAN'))-3)
print(time() - t0)