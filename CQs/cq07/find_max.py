"""Challenge Question 7"""

__author__ = "730756528"


def find_and_remove_max(
    input: list[int],
) -> int:  # return largest number in input
    """Defining that find and remove function"""
    if len(input) == 0:  # if list is empty return -1
        return -1
    index: int = 0
    max_number: int = input[index]  # max number variable
    while index < (len(input)):
        if input[index] > max_number:
            max_number = input[index]
        index += 1
    index = 0  # index must be reassigned to 0
    while index < len(
        input
    ):  # 2 while loops needed to keep track of the index and the number
        if max_number == input[index]:
            input.pop(index)
        else:
            index += 1
    return max_number
