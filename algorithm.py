import networkx as nx
import matplotlib.pyplot as plt
import time

# Define the graph edges with weights
edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", -2)
]

# Extract unique nodes from edges
nodes = list(set([u for u, v, w in edges] + [v for u, v, w in edges]))

# Define the source node
source = "A"

# Create a directed graph
G = nx.DiGraph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Initialize distances: set all to infinity except the source
dist = {node: float('inf') for node in nodes}
dist[source] = 0

def draw_graph(G, dist, iteration):
    plt.clf()
    pos = nx.spring_layout(G, seed=42)  # Fixed positions for consistency
    labels = {
        node: f"{node}\n({dist[node]:.1f})" if dist[node] != float('inf') else f"{node}\n(∞)"
        for node in G.nodes()
    }
    edge_labels = {(u, v): f"{G[u][v]['weight']}" for u, v in G.edges()}
    
    # Set node colors based on distance status
    node_colors = []
    for node in G.nodes():
        if dist[node] == float('inf'):
            node_colors.append('lightgray')
        elif node == source:
            node_colors.append('lightgreen')
        else:
            node_colors.append('lightblue')
    
    # Draw the graph
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=node_colors,
            node_size=1500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title(f"Bellman-Ford Algorithm - Iteration {iteration}")
    plt.pause(1)  # Pause for 1 second to animate

# Draw initial state
plt.figure(figsize=(8, 6))
draw_graph(G, dist, 0)

# Run Bellman-Ford algorithm step-by-step
for i in range(len(nodes) - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            updated = True
    draw_graph(G, dist, i + 1)
    if not updated:
        break

# Check for negative weight cycles
negative_cycle = False
for u, v, w in edges:
    if dist[u] + w < dist[v]:
        negative_cycle = True
        break

plt.show()

# Output result
if negative_cycle:
    print("Negative weight cycle detected!")
else:
    print("No negative weight cycle detected.")
    print("Shortest distances from source:")
    for node in nodes:
        print(f"{source} -> {node}: {dist[node]}")

