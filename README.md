# Algorithm Analysis Lab

A repository containing implementations and empirical analyses of core algorithms and data structures, exploring their theoretical and practical performance characteristics.


## 📁 Experiments

### [Experiment 1: Hybrid Merge/Insertion Sort](./Experiment_1_Hybrid_Sort/)
**Analysis of a hybrid sorting algorithm.**
- **Objective:** To determine the performance gain by combining Merge Sort with Insertion Sort for small subarrays.
- **Key Concepts:** Divide-and-Conquer, Recursion Overhead, Empirical Optimization.

### [Experiment 2: Dijkstra's Algorithm Implementations](./Experiment_2_Dijkstra_Implementations/)
**Comparative analysis of data structures on algorithm performance.**
- **Objective:** To evaluate how graph representations (Adjacency Matrix vs. List) and priority queue implementations (Array vs. Min-Heap) affect the efficiency of Dijkstra's algorithm.
- **Key Concepts:** Graph Theory, Time Complexity, Priority Queues, Empirical Analysis.


## 🛠️ Technologies Used

- **Language:** Python
- **Libraries:** `pandas`, `matplotlib`, `numpy`, `random`, `seaborn`, `csv`, `time`


## 📊 General Methodology

For each experiment, the process is:
1.  **Implementation:** Code the core algorithms.
2.  **Theoretical Analysis:** Derive and state the expected time/space complexity.
3.  **Empirical Analysis:** Design and run tests to collect performance data (e.g., runtime).
4.  **Comparison & Visualization:** Plot results and compare theoretical vs. empirical findings.
5.  **Conclusion:** Summarize insights and validate or challenge theoretical expectations.