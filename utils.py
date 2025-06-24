import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(vertices, edges, distances):
    G = nx.DiGraph()

    # Tüm düğümleri açıkça ekle
    for i in range(vertices):
        G.add_node(i)

    # Kenarları ekle
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)

    # Kenar ağırlıkları
    edge_labels = {(u, v): str(w) for u, v, w in edges}
    # Düğüm etiketleri (mesafeler)
    node_labels = {
        i: f"{i}\n{distances[i] if distances[i] != float('inf') else '∞'}"
        for i in range(vertices)
    }

    plt.figure(figsize=(7, 5))
    nx.draw(G, pos, with_labels=True, labels=node_labels,
            node_color='skyblue', node_size=1500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    st.pyplot(plt)
