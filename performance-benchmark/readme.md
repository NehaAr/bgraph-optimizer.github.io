# Performance Benchmark: CPU vs GPU 

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=wave&color=auto&height=200&width=700&section=header&text=Performance%20Benchmark&fontSize=10animation=twinkling" />
</p>

## Introduction

This module compares the performance of **community detection algorithms** using **CPU** (NetworkX) and **GPU** (CuGraph) on a **random graph**(Erdos_Renyi). We focus on measuring the **execution time** for and visually comparing the results on both CPU and GPU.

The experiment demonstrates how **CuGraph** (GPU) can provide a significant performance boost over **NetworkX** (CPU) for large-scale graph computations(10,000 nodes).

## Requirements

To run the performance benchmark, you will need to install the following Python packages:
- **bgraph.env**:  Environment file to switch between cugraph and networkx backend
- **NetworkX**: For graph creation and CPU-based community detection algorithms.
- **CuGraph**: For GPU-accelerated graph algorithms.
- **Matplotlib**: For plotting the performance comparison.
- **Python 3.10**: Cugraph only works on previous versions of Python and is currently unavailable on Python 3.12

  To run any script implementing cugraph, use the following:
  ``` bash
  !python3.10 xyz.py
  ```

  | Device | Algorithm | Execution-Time |
  |--------|-----------|-----------------|
  |**Tesla100 GPU**|Louvain Community Detection(10000 nodes)|7.748s|
  
  

You can install the required dependencies using:

```bash
pip install networkx cugraph matplotlib
