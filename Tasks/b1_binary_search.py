from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if len(arr) == 0:
        return None
    if arr[0] == arr[-1]:
        return 0
    min_border = 0
    max_border = len(arr) - 1
    middle = (max_border - min_border) // 2
    while True:
        if arr[middle] == elem:
            while elem == arr[middle - 1]:
                middle -= 1
            return middle
        elif elem > arr[middle]:
            min_border = middle + 1
            middle += (max_border - min_border) // 2
        else:
            max_border = middle - 1
            middle -= (max_border - min_border) // 2
        if max_border - min_border == 1:
            if arr[min_border] == elem:
                return min_border
            elif arr[max_border] == elem:
                return max_border
            else:
                return None
