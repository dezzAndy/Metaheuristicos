"""
    Implementación de Binary Search modificado para buscar el mejor elemento 
    de un arreglo a partir de un valor.
"""
def binary_search(arr, target, type_optimization):
    """
    Hace una busqueda binaria en un arreglo ordenado para encontrar el indice del mayor elemento.
    Usa un objetivo como punto de referencia.
    Performs binary search on a sorted array to find the index of the target element.

    Args:
        arr: El arreglo ordenado.
        target: El elemento sobre el cual se evalua.
        type_optimization: El tipo de optimización ("best" o "worst").

    Returns:
        El indice del mejor valor del arreglo según el tipo de optimización, de lo contrario -1.
    """
    left, right = 0, len(arr) - 1
    best_index = -1  # Variable para guardar nuestro mejor candidato

    if type_optimization == "best":
        # "best": Buscamos el elemento más grande posible en todo el arreglo
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > target:
                best_index = mid # Guardamos el candidato
                left = mid + 1
            else:
                # Si no superó el target, necesitamos números más grandes
                left = mid + 1

    elif type_optimization == "worst":
        # "worst": Buscamos un elemento más pequeño que el target
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                best_index = mid  # Es menor que el target, lo guardamos
                # Buscamos hacia la izquierda
                right = mid - 1
            else:
                # Si no es menor al target, necesitamos números más pequeños
                right = mid - 1
    return best_index
