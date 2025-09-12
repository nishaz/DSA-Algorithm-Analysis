# -----------------------
# Insertion Sort
# -----------------------
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


# -----------------------
# Merge Function
# -----------------------
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


# -----------------------
# Standard MergeSort
# -----------------------
def merge_sort(arr, left, right, counter):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, counter)
        merge_sort(arr, mid + 1, right, counter)
        merge(arr, left, mid, right, counter)


# -----------------------
# Hybrid MergeSort (with threshold S)
# -----------------------
def hybrid_merge_sort(arr, left, right, counter, S=10):
    if right - left + 1 <= S:
        insertion_sort(arr, left, right, counter)
    else:
        if left < right:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid, counter, S)
            hybrid_merge_sort(arr, mid + 1, right, counter, S)
            merge(arr, left, mid, right, counter)

