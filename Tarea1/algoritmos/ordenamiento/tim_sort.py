"""
    Implementación del algoritmo Tim Sort.
"""
from algoritmos.ordenamiento.insertion_sort import insertion_sort
from algoritmos.ordenamiento.merge_sort import merge

def tim_sort(arr):
    """
    Sorts an array using the Tim sort algorithm.
    """
    n = len(arr)
    min_run = 32
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2
