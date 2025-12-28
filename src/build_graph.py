import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches

# =========================
# Load Dataset
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "system_logs.csv")

df = pd.read_csv(data_path)
print("Dataset loaded for graph construction.")

# =========================
# Build Graph
# =========================
G = nx.DiGraph()

for _, row in df.iterrows():
    G.add_edge(
        row["source_service"],
        row["destination_service"],
        weight=row["response_time"],
        status=row["status"]
    )

print("Graph created successfully.")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

# =========================
# Graph Analysis
# =========================
# Node importance
centrality = nx.degree_centrality(G)

# Node size based on importance
node_sizes = [3000 * centrality[node] for node in G.nodes()]

# Edge color based on failure or success
edge_colors = [
    "red" if G[u][v]["status"] == "failure" else "gray"
    for u, v in G.edges()
]

# =========================
# Visualization
# =========================
plt.figure(figsize=(12, 8))

pos = nx.spring_layout(G, k=1.3, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=node_sizes,
    edge_color=edge_colors,
    font_size=10,
    font_weight="bold"
)

# Legend
failure_patch = mpatches.Patch(color='red', label='Failure')
success_patch = mpatches.Patch(color='gray', label='Success')
plt.legend(handles=[failure_patch, success_patch])
# Visualization
plt.title("Graph-Based Analysis of Distributed System Behavior")
plt.tight_layout()
# Ensure visuals folder exists
visuals_dir = os.path.join(BASE_DIR, "..", "visuals")
os.makedirs(visuals_dir, exist_ok=True)

# Save image
image_path = os.path.join(visuals_dir, "system_graph.png")
plt.savefig("src/../visuals/system_graph.png", dpi=300)
plt.show()


# CODE: Graph Metrics Analysis
print("\n===== GRAPH METRICS =====\n")

# Degree Centrality
degree_centrality = nx.degree_centrality(G)

# In-degree & Out-degree
in_degree = dict(G.in_degree())
out_degree = dict(G.out_degree())

# Betweenness Centrality
betweenness = nx.betweenness_centrality(G)

# PageRank
# pagerank = nx.pagerank(G)

# Failure count per service
failure_count = {}
for u, v, data in G.edges(data=True):
    if data["status"] == "failure":
        failure_count[v] = failure_count.get(v, 0) + 1

# Print results
print("🔹 Degree Centrality:")
for k, v in degree_centrality.items():
    print(f"{k}: {v:.3f}")

print("\n🔹 In-Degree (Dependency Load):")
for k, v in in_degree.items():
    print(f"{k}: {v}")

print("\n🔹 Out-Degree (Service Calls):")
for k, v in out_degree.items():
    print(f"{k}: {v}")

print("\n🔹 Betweenness Centrality (Bottlenecks):")
for k, v in betweenness.items():
    print(f"{k}: {v:.3f}")

# print("\n🔹 PageRank (Overall Importance):")
# for k, v in pagerank.items():
#     print(f"{k}: {v:.3f}")

print("\n🔹 Failure Count:")
for k, v in failure_count.items():
    print(f"{k}: {v}")

