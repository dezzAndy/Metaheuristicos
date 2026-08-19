"""
    Implementación del algoritmo Merge Sort.
"""
def merge(arr, left, mid, right):
    """
    Merges two subarrays of arr[].
    First subarray is arr[left..mid]
    Second subarray is arr[mid+1..right]
    """
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    l = [0] * n1
    r = [0] * n2

    # Copy data to temp arrays l[] and r[]
    for i in range(n1):
        l[i] = arr[left + i]
    for j in range(n2):
        r[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    # Copy the remaining elements of l[],
    # if there are any
    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1

    # Copy the remaining elements of r[],
    # if there are any
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    """
    Sorts an array using the merge sort algorithm.
    """
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
