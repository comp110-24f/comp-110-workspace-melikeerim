"""Summung the elements of a list using different loops"""

__author__ = "730756528"


def w_sum(vals: list[float]) -> float:  # while loop
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum = sum + vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:  # for loop
    sum: float = 0.0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float:  # for loop with range
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum = sum + vals[idx]
    return sum
