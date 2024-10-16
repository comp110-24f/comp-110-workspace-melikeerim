from CQs.cq07.find_max import find_and_remove_max

"""Challenge question 7"""

__author__ = "730756528"


def test_find_and_remove_max() -> None:
    """Tests that function returns the expected value"""
    test: list[int] = [1, 2, 3]
    assert find_and_remove_max(test) == 3


def test_2_find_and_remove_max() -> None:
    """Tests that function mutates the input in the expected way"""
    test_2: list[int] = [1, 2, 3, 4, 2, 4]
    assert find_and_remove_max(test_2) == 4


def test_3_find_And_remove_max() -> None:
    """Tests that function returns the correct value in case of unconventional input"""
    test_3: list[int] = []
    assert find_and_remove_max(test_3) == -1
