"""
    Implementación del algoritmo Merge Sort.
"""
def merge(arr, left, mid, right):
    """
    Mezcla dos subarreglos de arr[]
    El primer subarreglo es arr[left..mid]
    El segundo es arr[mid+1..right]
    """
    n1 = mid - left + 1
    n2 = right - mid

    # Crea dos arreglos temporales
    l = [0] * n1
    r = [0] * n2

    # Copia los datos a los arreglos temporales l[] y r[]
    for i in range(n1):
        l[i] = arr[left + i]
    for j in range(n2):
        r[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Mezcla los arreglos temporales de vuelta
    # en arr[left..right]
    while i < n1 and j < n2:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    # Copia los elementos restante de l[], si los hubiera.
    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1

    # Copia los elementos restante de r[], si los hubiera.
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    """
    Ordena un arreglo usando merge sort.
    """
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
