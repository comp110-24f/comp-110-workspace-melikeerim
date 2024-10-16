"""Exercise 04: list utility functions"""

__author__ = "730756528"


def all(list_1: list[int], num: int) -> bool:
    """Checks if all elements of the list is equal to num"""
    if len(list_1) == 0:  # returns False if if list is empty
        return False
    for elem in list_1:  # for loop to go over every elem
        if elem is not num:  # if one element is not qual to num, return False
            return False
    return True  # returns bool - True or False


def max(input: list[int]) -> int:
    """max funtion to retun the biggest number in the inputted list"""
    if len(input) == 0:  # raises an error if list is empty
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max_num: int = input[index]
    while index < len(input):  # while loop to control index and max_num
        if input[index] > max_num:
            max_num = input[
                index
            ]  # if new number is bigger change to max_num to new number
        index += 1  # required line to avoid infinite loop
    return max_num


def is_equal(list_in1: list[int], list_in2: list[int]) -> bool:
    """is equal funtion return True if every elem @ every index is equal in 2 lists"""
    if len(list_in1) != len(list_in2):  # if not equal length - return False
        return False

    for idx in range(
        0, len(list_in1)
    ):  # for loop with range to checl elems at every idx
        if list_in1[idx] != list_in2[idx]:
            return False
    return True  # returns True if it didn't retun False


def extend(input_1: list[int], input_2: list[int]) -> None:  # returns None
    """uses append to add the second list's values to the end of the first list"""
    for number in input_2:  # go over every element in list 2
        input_1.append(
            number
        )  # add each elem from list 2 to the end of list 1 one by one
