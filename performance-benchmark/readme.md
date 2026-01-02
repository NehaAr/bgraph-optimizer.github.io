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
However, a special environment has been created for GPU in tox.ini, where you just need to install Python 3.10 and run scripts via the tox.ini scripts folder. The scripts folder contains all GPU algorithms related to the bgraph project.

  | Device | Algorithm | Execution-Time |
  |--------|-----------|-----------------|
  |**Tesla100 GPU**|Louvain Community Detection(10000 nodes)|7.748s|
  |**Intel(R) Xeon(R) CPU @ 2.00GHz**|Louvain Community Detection(10000 nodes)|257.841s|
   |**Tesla100 GPU**|Louvain Community Detection(20000 nodes)|83.500s|
  |**Tesla100 GPU**|Leiden Community Detection(10000 nodes)|4.524s|
   |**Intel(R) Xeon(R) CPU @ 2.00GHz**|Leiden Community Detection(10000 nodes)|265.794s|

NVIDIA T4(Tesla 100) GPU is an energy-efficient data center GPU built on top of turing architecture, which is designed for accelerating AI inference, deep learning, and data analytics.

**Memory-16GB GDDR6**

**Power Draw 70W**

**T4 GPU performance overview before and after running the community detection Louvain algorithm for 20000 nodes**
**The GPU utilization for transferring data from CPU to GPU is 14 percent at 27W, while the GPU utilization is 86% at 35W when the algorithm is running**

![GPU-Performance](/assets/gpu_perf.jpg)

**Note:** Only two community detection algorithms are supported by nx-cugraph as of 2025

