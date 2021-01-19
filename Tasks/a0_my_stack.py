"""
My little Stack
"""
from typing import Any

stack = []


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global stack
    stack.append(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    if len(stack):
        return stack.pop(-1)
    return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    if 0 <= ind < len(stack):
        return stack[-ind - 1]
    return None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global stack
    stack = []
    return None
