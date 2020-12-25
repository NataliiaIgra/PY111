"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

priority_queue = []


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global priority_queue
    priority_queue.append((elem, priority))
    priority_queue = sorted(priority_queue, key=lambda x: x[1])
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global priority_queue
    if 0 < len(priority_queue):
        return priority_queue.pop(0)[0]
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global priority_queue
    small_list = []
    if 0 <= ind < len(priority_queue):
        for element in priority_queue:
            if element[1] == priority:
                small_list.append(element)
    return small_list[ind][0]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_queue
    priority_queue = []
    return None
