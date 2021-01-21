def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    return n*factorial_recursive(n-1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    if n == 0 or n == 1:
        return 1
    i = 1
    factorial = 1
    while i != n:
        i += 1
        factorial *= i
    return factorial
