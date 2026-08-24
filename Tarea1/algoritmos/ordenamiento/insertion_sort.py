"""
    Implementación del algoritmo Insertion Sort.
"""

def insertion_sort(arr, low, high):
    """
        Ordena un arreglo usando el Insertion Sort
    """
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
