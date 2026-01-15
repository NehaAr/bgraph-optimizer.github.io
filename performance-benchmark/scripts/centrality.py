# -----------------------------------------------------------------------------
# Copyright (c) 2026 Neha
#
# Licensed under the GPL License. See the LICENSE file for details.
# -----------------------------------------------------------------------------

import nx_cugraph as nxcg
import subprocess
import networkx as nx
import time

def centrality_graph(graph:nx.Graph) -> nx.Graph:
    """
    This custom wrapper visualizes 4 graphs on the basis of various centrality measures, both local and global.

    Arguments: Inputs from the decorated function

    Return: The graph object.
    """
    print("Checkpoint1")

    try:
        result = subprocess.run(
            ["nvidia-smi"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("nvidia-smi not found. Is NVIDIA driver installed?")

    # Convert NetworkX graph to cuGraph graph
    g_cugraph = nxcg.from_networkx(graph)

    # Compute Centrality Measures using cuGraph
    degree_centrality = nxcg.degree_centrality(g_cugraph)
    betweenness_centrality = nxcg.betweenness_centrality(g_cugraph)
    eigen_centrality = nxcg.eigenvector_centrality(g_cugraph, max_iter=1000, tol=1e-06)

    # Prepare the graph data for plotting using NetworkX
    node_list = list(graph.nodes())
    degree, betweenness, eigen = [], [], []

    # Extract centrality values for plotting
    for node in node_list:
        degree.append(degree_centrality[node])
        betweenness.append(betweenness_centrality[node])
        eigen.append(eigen_centrality.get(node, 0))

    node_sizes = [v * 300 for v in degree_centrality.values()]
    node_sizes2 = [v * 300 for v in betweenness_centrality.values()]
    node_sizes3 = [v * 300 for v in eigen_centrality.values()]

    print("******************Graph Properties**************************")
    data = pd.DataFrame({'node': node_list, 'degree': degree, 'betweenness': betweenness, 'eigen': eigen})

    # Set layout and colors for plotting
    pos = nx.spring_layout(graph)
    colors = list(degree_centrality.values())

    fig, ax = plt.subplots(1, 3, figsize=(10, 10))
    
    # Draw Graph with Degree Centrality
    nx.draw(graph, with_labels=True, node_color=colors, ax=ax[0], cmap=plt.cm.viridis, node_size=node_sizes, edge_color='gray', pos=pos)
    ax[0].set_title("Graph with Degree Centrality")

    # Draw Graph with Betweenness Centrality
    nx.draw(graph, with_labels=True, node_color=colors, ax=ax[1], cmap=plt.cm.viridis, node_size=node_sizes2, edge_color='gray', pos=pos)
    ax[1].set_title("Graph with Betweenness Centrality")

    # Draw Graph with Eigen Centrality
    nx.draw(graph, with_labels=True, node_color=colors, ax=ax[2], cmap=plt.cm.viridis, node_size=node_sizes3, edge_color='gray', pos=pos)
    ax[2].set_title("Graph with Eigen Centrality")

    plt.tight_layout()
    plt.show()

    try:
        result = subprocess.run(
            ["nvidia-smi"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("nvidia-smi not found. Is NVIDIA driver installed?")

    return graph
