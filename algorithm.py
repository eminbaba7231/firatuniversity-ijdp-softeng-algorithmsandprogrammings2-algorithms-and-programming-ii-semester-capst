import networkx as nx
import matplotlib.pyplot as plt
import time

# Graf ve kenarlar (örnek)
edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", -2)
]

# Düğümler
nodes = list(set([u for u, v, w in edges] + [v for u, v, w in edges]))

# Kaynak düğüm
source = "A"

# Graph oluştur
G = nx.DiGraph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Mesafeler başlangıçta sonsuz, kaynak 0
dist = {node: float('inf') for node in nodes}
dist[source] = 0

def draw_graph(G, dist, iteration):
    plt.clf()
    pos = nx.spring_layout(G, seed=42)  # Düğümlerin konumu sabit olsun
    labels = {node: f"{node}\n({dist[node]:.1f})" if dist[node] != float('inf') else f"{node}\n(∞)" for node in G.nodes()}
    edge_labels = {(u,v): f"{G[u][v]['weight']}" for u,v in G.edges()}
    
    # Düğümleri çiz (renk mesafeye göre)
    node_colors = []
    for node in G.nodes():
        if dist[node] == float('inf'):
            node_colors.append('lightgray')
        elif node == source:
            node_colors.append('lightgreen')
        else:
            node_colors.append('lightblue')
    
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors, node_size=1500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title(f"Bellman-Ford Algorithm - Iteration {iteration}")
    plt.pause(1)  # 1 saniye bekle

plt.figure(figsize=(8,6))
draw_graph(G, dist, 0)

# Bellman-Ford algoritması (adım adım)
for i in range(len(nodes) - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            updated = True
    draw_graph(G, dist, i+1)
    if not updated:
        break

# Negatif döngü kontrolü
negative_cycle = False
for u, v, w in edges:
    if dist[u] + w < dist[v]:
        negative_cycle = True
        break

plt.show()

if negative_cycle:
    print("Negative weight cycle detected!")
else:
    print("No negative weight cycle detected.")
    print("Shortest distances from source:")
    for node in nodes:
        print(f"{source} -> {node}: {dist[node]}")

