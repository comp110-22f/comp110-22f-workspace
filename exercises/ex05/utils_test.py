"""Test functions for the functions contained in utils Python file."""

__author__ = "730574292"

from utils import only_evens
from utils import concat
from utils import sub


# Test fuctions for only_evens.
def test_one_only_evens() -> None:
    """Tests if a list of only the evens of a list is returned by the only_evens() function when a list of odds and evens is provided."""
    assert only_evens([5, 7, 8, 3, 2, 10, 3, 9, 2, 4, 6, 10]) == [8, 2, 10, 2, 4, 6, 10]


def test_two_only_evens() -> None:
    """Again tests if a list of only the evens of a list is returned by the only_evens() function when a list of odds and evens is provided."""
    assert only_evens([1, 82, 50, 2, 23, 8, 4]) == [82, 50, 2, 8, 4]


def test_three_only_evens() -> None:
    """Tests for the edge case of the list provided by the user to the only_evens() function being empty."""
    assert only_evens([]) == []


# Test functions for concat.
def test_one_concat() -> None:
    """Tests if the function concat() successfully concatenates two lists of integers and returns this new list."""
    assert concat([1, 5, 4, 6], [2, 4, 3, 6]) == [1, 5, 4, 6, 2, 4, 3, 6]


def test_two_concat() -> None:
    """Tests if the function concat() successfully concatenates two lists of integers of two different lengths and returns this new list."""
    assert concat([1, 3, 4, 6, 7], [2, 2]) == [1, 3, 4, 6, 7, 2, 2]
    assert concat([3, 4, 3], [3, 4, 2, 6, 7, 3]) == [3, 4, 3, 3, 4, 2, 6, 7, 3]


def test_three_concat() -> None:
    """Tests if the function concat() successfully concatenates two lists when one or both are empty and returns an empty list."""
    assert concat([3, 2], []) == [3, 2]
    assert concat([], [1]) == [1]
    assert concat([], []) == []


# Test functions for sub.
def test_one_sub() -> None:
    """Tests if function sub() returns an exerpt of the provided list using the provided start and end indices."""
    assert sub([2, 3, 6, 4, 3, 9, 19, 9, 10], 1, 3) == [3, 6]
    assert sub([2, 3, 6, 4, 3, 9, 19, 9, 10], 0, 5) == [2, 3, 6, 4, 3]
    assert sub([9, 8, 2, 1, 0, 8], -9, 3) == [9, 8, 2]


def test_two_sub() -> None:
    """Tests if function sub() returns an empty list if the provided start index is greater than the provided end index."""
    assert sub([2, 3, 6, 4, 3, 9, 19, 9, 10], 100, 3) == []
    assert sub([2, 3, 6, 4, 3, 9, 19, 9, 10], 4, 1) == []


def test_three_sub() -> None: 
    """Tests if funciton sub() returns an appropriate sublist if either or both the provided start and/or end indices are out of range."""
    assert sub([3, 2, 8, 4, 6, 6], 3, 8) == [4, 6, 6]
    assert sub([3, 7, 2, 9, 10], 99, 3) == []