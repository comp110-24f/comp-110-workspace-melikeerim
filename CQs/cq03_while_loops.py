"""Practicing with while loops: Challenge question 3"""

__author__: str = "730756528"


def num_instances(phrase: str, search_char: str) -> int:
    """Defining the num_instances function"""
    count: int = 0  # local variable count int
    index: int = 0  # local variable index int
    while index < len(phrase):  # while loop
        if (
            phrase[index] == search_char
        ):  # if it finds the character we are searching for
            count = count + 1  # increase count by 1
        else:
            count = count  # else count=count
        index = index + 1  # index increases by one at the end of each loop
    return count
