"""EX05 Utils file: implement list utility functions"""

__author__ = "730756528"


def only_evens(input: list[int]) -> list:
    """Defining only_evens: returns a list w/only evens."""
    even_list: list[int] = []
    index: int = 0
    while index < len(input):
        if input[index] % 2 == 0:  # if it's even add to new list
            even_list.append(input[index])
        index += 1
    return even_list  # return the new list


def sub(input_2: list[int], start_idx: int, end_idx: int) -> list:
    """Defining the sub function that return a subset of the input list"""
    subset_list: list[int] = []  # start with an empty subset list

    if (len(input_2) == 0) or (start_idx >= len(input_2)) or (end_idx <= 0):
        return subset_list  # return empty list if the if statement is True
    if start_idx < 0:
        start_idx = 0  # if start_idx is negative, reassign it to 0
    if end_idx > len(input_2):
        end_idx = len(input_2)  # if end_idx is bigger than length of list, reassign it
    index: int = start_idx
    while index <= (end_idx - 1):
        subset_list.append(
            input_2[index]
        )  # add to subset list when index is between start and end
        index += 1
    return subset_list  # return new list


def add_at_index(input_3: list[int], elem_add: int, idx_add: int) -> None:
    """Defining the add_at_index funtion that adds elem at idx_add"""
    if idx_add < 0 or idx_add > len(input_3):  # raise error
        raise IndexError("Index is out of bounds for the input list")
    input_3.append(elem_add)
    total_idx: int = len(input_3) - 1
    while total_idx > idx_add:  # start looping from the end and continue till idx_add
        temp: int = input_3[total_idx]  # temporarily holding the number to not lose it
        input_3[total_idx] = input_3[total_idx - 1]
        input_3[total_idx - 1] = temp
        total_idx -= 1  # going backwards
