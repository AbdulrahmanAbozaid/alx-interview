#!/usr/bin/env python3
"""
Min Ops
"""


def minOperations(n):
    """Calc Min Ops"""
    if n <= 1:
        return 0

    # Extract Prime Factors
    i = 2
    ct = 0
    while i*i <= n:
        while n % i == 0:
            ct = ct + i
            n //= i
        i += 1

    if n != 1:
        ct = ct + n

    return ct
