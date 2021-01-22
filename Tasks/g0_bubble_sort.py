from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for _ in range(len(container)):
        to_swap = False
        j = 0

        while j < len(container) - 1:
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]
                to_swap = True
            j = j + 1

        if not to_swap:
            return container

    return container


if __name__ == '__main__':
    arr = [random.randint(-100, 100) for _ in range(10)]
    print(arr)
    print(sort(arr))
