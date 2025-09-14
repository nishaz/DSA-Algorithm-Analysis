import random, csv, time

# Insertion Sort
def insertion_sort(arr, left, right, counter):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left:
            counter[0] += 1  # comparison
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key

# Merge Function
def merge(arr, left, mid, right, counter):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        counter[0] += 1  # comparison
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Standard MergeSort
def merge_sort(arr, left, right, counter):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, counter)
        merge_sort(arr, mid + 1, right, counter)
        merge(arr, left, mid, right, counter)

# Hybrid MergeSort (threshold S)
def hybrid_merge_sort(arr, left, right, counter, S):
    if right - left + 1 <= S:
        insertion_sort(arr, left, right, counter)
    else:
        if left < right:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid, counter, S)
            hybrid_merge_sort(arr, mid + 1, right, counter, S)
            merge(arr, left, mid, right, counter)


# Generate datasets
n = [1000, 10000, 100000, 1000000, 10000000] # sizes for n
x = 1000 # max value allowed in array
s = [10, 50, 100, 500, 1000] # threshold s for hybrid sort (if subarr<S, use insertion sort instead of recrusive mergesort)

# Experiment
def experiment_vary_n(ns, fixed_s,):
    results = []
    for n in ns:
        arr = [random.randint(0, x) for _ in range(n)]

        # run merge sort
        count_merge = [0]
        merge_sort(arr.copy(), 0, n-1, count_merge) # copy array so sorting doesn't overwrite original arr

        # run hybrid merge sort
        count_hybrid = [0]
        hybrid_merge_sort(arr.copy(), 0, n-1, count_hybrid, fixed_s)

        results.append({
            "n": n,
            "s": fixed_s,
            "merge_count": count_merge[0],
            "hybrid_count": count_hybrid[0]
        })
    return results


def experiment_vary_s(ss, fixed_n):
    results = []
    arr = [random.randint(0, x) for _ in range(fixed_n)]

    # run merge sort
    count_merge = [0]
    merge_sort(arr.copy(), 0, fixed_n-1, count_merge)

    # run hybrid sort w varying s
    for s in ss:
        count_hybrid = [0]
        hybrid_merge_sort(arr.copy(), 0, fixed_n-1, count_hybrid, s)

        results.append({
            "n": fixed_n,
            "s": s,
            "merge_count": count_merge[0],
            "hybrid_count": count_hybrid[0]
        })
    return results

# Export results to csv file
def save_results_to_csv(filename, results):
    keys = results[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

# Run code
res_n = experiment_vary_n(n, fixed_s=50)
res_s = experiment_vary_s(s, fixed_n=10000)

save_results_to_csv("Lab1/results_vary_n.csv", res_n)
save_results_to_csv("Lab1/results_vary_s.csv", res_s)