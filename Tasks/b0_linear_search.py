"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def search(arr: Sequence, elem: int) -> int:
    """
    Function that finds required element in array

    :param arr: Array containing numbers
    :param elem: Number to find in the array
    :return: index of first occurrence of required element in array
    """
    if not arr:
        return -1
    for index, element in enumerate(arr):
        if element == elem:
            return index
    return -1


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    if not arr:
        return -1
    min_index = 0
    min_element = arr[0]
    for index, element in enumerate(arr):
        if element < min_element:
            min_element = element
            min_index = index
    return min_index
