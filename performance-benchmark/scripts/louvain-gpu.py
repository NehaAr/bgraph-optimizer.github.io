# -----------------------------------------------------------------------------
# Copyright (c) 2026 Neha
#
# Licensed under the GPL License. See LICENSE file for details.
# -----------------------------------------------------------------------------

import nx_cugraph as nxcg
import subprocess
import networkx as nx
import time
def load_graph(edge_list):
  G=nx.Graph()
  graph=G.add_edges_from(edge_list)
  return graph

def louvain()-> None :
    """
    This module finds the communities using Louvain algorithm.

    Arguments:
      graph: Graph Object

    Return:
     None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--edge", required=True, help="edge_list")
    args = parser.parse_args()

    graph = load_graph(args.edge)
    G=nxcg.from_networkx(graph)

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

    partition = list(nxcg.community.louvain_communities(G))
    
    node_to_comm={}
    for com_id, node in enumerate(partition):
        for node in nodes:
           node_to_comm[node]=comm_id
    node_colors = [node_to_comm[node] for node in G.nodes()]

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
     G,
     pos,
     with_labels=True,
     node_color=node_colors,
     cmap=plt.cm.tab20,   # better than rainbow
     node_size=500,
     font_size=9
    )

    plt.title("Louvain Communities (nx-cugraph backend)")
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

start_time=time.time()
louvain() 
end_time=time.time()

print(end_time-start_time)
