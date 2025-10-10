## Experiment 2: Dijkstra's Algorithm - Implementation & Complexity Analysis
**Objective:** To analyze how different data structure choices impact the time complexity of Dijkstra's algorithm.

**Description:**
This experiment consists of two implementations:
- **Implementation A:** Uses an adjacency matrix for the graph and a simple array for the priority queue.
- **Implementation B:** Uses an adjacency list for the graph and a binary min-heap for the priority queue.

We will conduct a comparative analysis of both implementations by:
1. Deriving their theoretical time complexities in terms of |V| and |E|.
2. Performing empirical tests to measure their runtime performance on graphs of varying densities.
3. Concluding which implementation is superior and under what conditions (e.g., dense vs. sparse graphs).