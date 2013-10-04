import sys
import doctest


def factorial(n):
    """
    Returns the factorial of a number N (N!)
    e.g. for N = 5, 5! = 5 x 4 x 3 x 2 x 1

    N should be an integer

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(5)
    120
    """
    # assert n >= 0
    # Exception test
    if not type(n) == int:
        raise Exception("The number provided is not an integer")
    if n < 0:
        raise Exception("Factorial of a negative number is not defined")
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def fibonacci(n):
    """
    Returns the Nth value in the fibonacci sequence
    
    F(N) = F(N-1) + F(N-2)
    F(0) = 0, F(1) = 1

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    >>> x = fibonacci(5)
    >>> x + 5
    10
    """

    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a

# When the function is ran directly, the __name__ variable is set to __main__
# Otherwise the __name__ is the name of the script that imported it
if __name__ == "__main__":
    # Test this by running the script with 'python functions.py -v'
    doctest.testmod()
