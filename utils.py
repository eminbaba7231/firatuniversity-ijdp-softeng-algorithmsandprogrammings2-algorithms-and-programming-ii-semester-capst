import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, dist, source, iteration):
    plt.clf()
    pos = nx.spring_layout(G, seed=42)

    labels = {
        node: f"{node}\n({dist[node]:.1f})" if dist[node] != float('inf') else f"{node}\n(∞)"
        for node in G.nodes()
    }

    edge_labels = {
        (u, v): f"{G[u][v]['weight']}" for u, v in G.edges()
    }

    node_colors = []
    for node in G.nodes():
        if dist[node] == float('inf'):
            node_colors.append('lightgray')
        elif node == source:
            node_colors.append('lightgreen')
        else:
            node_colors.append('lightskyblue')

    nx.draw(
        G, pos, with_labels=True, labels=labels,
        node_color=node_colors, node_size=1500,
        font_size=10, font_weight='bold'
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title(f"Bellman-Ford Algorithm - Iteration {iteration}")
    plt.pause(1)

