def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return n
    i = 1
    a, b = 0, 1
    while i != n:
        a, b = b, a+b
        i += 1
    return b
