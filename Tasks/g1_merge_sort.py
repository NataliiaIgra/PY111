from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not container:
        raise Exception("Where is your container???")

    if len(container) == 1:
        return container

    left_part = container[:len(container) // 2]
    right_part = container[len(container) // 2:]
    sorted_left_part = sort(left_part)
    sorted_right_part = sort(right_part)

    return merge_procedure(sorted_left_part, sorted_right_part)


def merge_procedure(some_list1, some_list2):
    """
    Additional function, which merges two already-sorted lists.

    :param some_list1: sorted "left" list
    :param some_list2: sorted "right" list
    :return: result of merge sort algorithm
    """
    index_list1 = 0
    index_list2 = 0
    result = []

    while index_list1 < len(some_list1) and index_list2 < len(some_list2):
        if some_list1[index_list1] < some_list2[index_list2]:
            result.append(some_list1[index_list1])
            index_list1 += 1
        else:
            result.append(some_list2[index_list2])
            index_list2 += 1

    if index_list1 < len(some_list1):
        result = result + some_list1[index_list1:]
    elif index_list2 < len(some_list2):
        result = result + some_list2[index_list2:]

    return result
