"""Mutating functions"""

__author__ = "730756528"


def manual_append(list: list[int], input: int) -> None:
    list.append(input)


def double(list_double: list[int]) -> None:
    index: int = 0
    while index < len(list_double):
        list_double[index] = list_double[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
