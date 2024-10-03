#!/usr/bin/python3
"""
Pscal's Triangle Module
"""


def pascal_triangle(n):
    """pascal trianlge generator"""
    triangle = [[1]]
    for i in range(1, n):
        triangle.append([1] +
                        [triangle[i-1][j] + triangle[i-1][j+1]
                         for j in range(i - 1)] + [1])
    return triangle if n > 0 else []
