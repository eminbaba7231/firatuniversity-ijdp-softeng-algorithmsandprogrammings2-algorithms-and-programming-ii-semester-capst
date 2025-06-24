import networkx as nx
import matplotlib.pyplot as plt
import time
from utils import draw_graph

edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", -2)
]

nodes = list(set([u for u, v, w in edges] + [v for u, v, w in edges]))
source = "A"

G = nx.DiGraph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

dist = {node: float('inf') for node in nodes}
dist[source] = 0

plt.figure(figsize=(8, 6))
draw_graph(G, dist, source, iteration=0)

for i in range(len(nodes) - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            updated = True
    draw_graph(G, dist, source, iteration=i + 1)
    if not updated:
        break

negative_cycle = False
for u, v, w in edges:
    if dist[u] + w < dist[v]:
        negative_cycle = True
        break

plt.show()

if negative_cycle:
    print("❌ Negative weight cycle detected!")
else:
    print("✅ No negative weight cycle detected.")
    print("\n📊 Shortest distances from source:")
    for node in nodes:
        print(f"{source} -> {node}: {dist[node]}")

