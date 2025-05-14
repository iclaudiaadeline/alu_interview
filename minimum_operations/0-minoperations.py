#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """Return the minimum number of operations to get n H characters"""
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations

