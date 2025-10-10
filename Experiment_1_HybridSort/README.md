# Experiment 1: Hybrid Merge/Insertion Sort Analysis
**Objective:** To investigate the performance benefits of a hybrid sorting algorithm that combines Merge Sort and Insertion Sort.

**Description:**
Merge Sort's divide-and-conquer approach is inefficient for very small subarrays due to high recursion overhead. This experiment implements a hybrid algorithm that uses Merge Sort for large partitions but switches to the more efficient Insertion Sort when a subarray's size falls below a defined threshold S. We will empirically determine the optimal threshold S and compare the performance of the pure and hybrid algorithms against standard implementations.