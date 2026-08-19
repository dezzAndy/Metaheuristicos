"""
This module contains the implementation of the linear search algorithm.
"""

def linear_search(arr, target):
    """
    Performs linear search on an array to find the index of the target element.

    Args:
        arr: A list of elements.
        target: The element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
