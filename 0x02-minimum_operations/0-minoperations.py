#!/usr/bin/python3
"""Method that calculates the fewest number of operations
needed to result in exacty n H characters in the file"""


def minOperations(n):
    """Gets fewest # of operations needed to result
    in exactly n H characters"""
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smallers vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops
