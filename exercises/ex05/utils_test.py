from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""EX05 Utils test: defining unit tests to test the function"""

__author__ = "730756528"


def test_only_evens_1() -> None:
    """Tests that the function returns the expected value"""
    test_1: list[int] = [1, 2, 3, 4]
    assert only_evens(test_1) == [2, 4]


def test_only_evens_2() -> None:
    """Tests that the function returns empty list when no even numbers found"""
    test_2: list[int] = [1, 7, 9, 5]
    assert only_evens(test_2) == []


def test_only_evens_3() -> None:
    """Tests edge case"""
    test_3: list[int] = []
    assert only_evens(test_3) == []


def test_sub_1() -> None:
    """Tests edge case"""
    test_4: list[int] = []
    assert sub(test_4, 2, 4) == []


def test_sub_2() -> None:
    """Tests edge case 2"""
    test_5: list[int] = [2, 3, 4, 5, 6]
    assert sub(test_5, 1, -2) == []


def test_sub_3() -> None:
    """Tests edge case 3"""
    test_6: list[int] = [2, 3, 4, 5, 6, 7]
    assert sub(test_6, 10, 5) == []


def test_sub_4() -> None:
    """Tests that the sub function returns the sublist"""
    test_7: list[int] = [2, 3, 4, 5]
    assert sub(test_7, 1, 3) == [3, 4]


def test_sub_5() -> None:
    """Tests that sub still returns the sublist when start_idx is negative"""
    test_8: list[int] = [1, 2, 3, 4]
    assert sub(test_8, -2, 3) == [1, 2, 3]


def test_add_at_index_1() -> None:
    """Tests that add_At_index function mutates the list"""
    test_9: list[int] = [1, 2, 4, 5, 6]
    add_at_index(test_9, 3, 2)
    assert test_9 == [1, 2, 3, 4, 5, 6]


def test_add_at_index_raises_indexerror() -> None:
    """Tests that add_at_index raises an IndexError for an invalid index."""
    test_10: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    with pytest.raises(IndexError):
        add_at_index(test_10, 3, 12)
        # an IndexError is raised for the case when add_at_index is given an idx_add
        # that is greater than the length of our <list_object>


def test_add_at_index_raises_indexerror_2() -> None:
    """Tests that add_at_index raises and IndexError when idx_add is negative"""
    test_11: list[int] = [1, 2, 4, 5, 6, 7, 8, 9]
    with pytest.raises(IndexError):
        add_at_index(test_11, 3, -3)
