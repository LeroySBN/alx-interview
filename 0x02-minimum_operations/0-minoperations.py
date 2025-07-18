#!/usr/bin/python3
"""0-minoperations.py
Calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Args:
        n - number of H characters to print
    Return:
        the minimum number of operations needed
        to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(int(n / i))
