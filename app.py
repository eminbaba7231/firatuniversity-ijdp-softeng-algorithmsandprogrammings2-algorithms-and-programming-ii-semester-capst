import streamlit as st
from algorithm import bellman_ford
from utils import draw_graph

st.set_page_config("Bellman-Ford Visualizer", layout="centered")

st.title("🔁 Bellman-Ford Algorithm Visualizer")

vertices = st.number_input("Number of vertices", min_value=2, max_value=10, value=5)
source = st.number_input("Source vertex", min_value=0, max_value=vertices-1, value=0)

edge_input = st.text_area("Enter edges (format: from to weight per line)", value="0 1 6\n0 2 7\n1 2 8\n1 3 5\n2 3 -3")
edges = []
for line in edge_input.strip().split('\n'):
    u, v, w = map(int, line.strip().split())
    edges.append((u, v, w))

if st.button("Run Bellman-Ford"):
    steps, has_negative_cycle, final_distances = bellman_ford(vertices, edges, source)

    if has_negative_cycle:
        st.error("⚠️ Negative weight cycle detected!")
    else:
        step = st.slider("View Step", 1, len(steps), 1)
        st.write(f"Step {step}: Distance Table")
        st.json({str(i): (dist if dist != float('inf') else "∞") for i, dist in enumerate(steps[step - 1][1])})
        draw_graph(vertices, edges, steps[step - 1][1])
