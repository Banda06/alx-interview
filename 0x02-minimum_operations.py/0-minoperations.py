#!/usr/bin/python3
""" Minimum operations questions
    Topic: Dynamic programming
"""


def minOperations(n):
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    # While n is greater than 1, factorize n
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
