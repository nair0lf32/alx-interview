#!/usr/bin/python3

"""
Pascal triangle in python
"""


def pascal_triangle(n):
    """
    Returns a list of list of integers representing
    the pascal triangle sequence for a given n rows
    or an empty list if n <= 0
    """
    row = []
    if (n <= 0):
        return row
    cols = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(cols[i-1][j-1] + cols[i-1][j])
        row.append(1)
        cols.append(row)
    return cols
