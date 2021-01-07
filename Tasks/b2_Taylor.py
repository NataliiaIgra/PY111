"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float], tochnost: int = 10) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :param tochnost: number of iterations
    :return: e^x value
    """
    n: int = 0
    value = 0
    increment = 1
    while tochnost != n:
        value += x ** n / increment
        n += 1
        increment *= n
    return value


def sinx(x: Union[int, float], tochnost: int = 5) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :param tochnost: number of iterations
    :return: sin(x) value
    """
    n: int = 0
    value = 0
    increment = 1
    divisor = 1
    while tochnost != n:
        value += (-1) ** n * (x ** increment / divisor)
        n += 1
        increment = 2 * n + 1
        divisor *= increment * (increment - 1)
    return value
