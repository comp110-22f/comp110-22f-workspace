"""Tests the utils functions."""


__author__ = "730553672"


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Tests empty list."""
    xs: list[int] = []
    assert only_evens(xs) == list()


def test_only_evens_multiple() -> None:
    """Tests multiple items."""
    xs: list[int] = [2, 4, 5, 4, 6]
    assert only_evens(xs) == [2, 4, 4, 6]


def test_only_evens_many() -> None:
    """Tests many items."""
    xs: list[int] = [1, 1, 1, 5, 5, 5, 7, 7]
    assert only_evens(xs) == list()


def test_sub_empty() -> None:
    """Tests empty list."""
    xs: list[int] = []
    start: int = 0
    end: int = 0
    assert sub(xs, start, end) == list()


def test_sub_many() -> None:
    """Tests multiple items."""
    xs: list[int] = [2, 3, 4, 5, 6]
    start: int = 0
    end: int = 3
    assert sub(xs, start, end) == [2, 3, 4]


def test_sub_many_items() -> None:
    """Tests many items."""
    xs: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    start: int = 2
    end: int = 10
    assert sub(xs, start, end) == [2, 3, 4, 5, 6, 7, 8, 9]


def test_concat_empty() -> None:
    """Tests empty list."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == list()


def test_concat_two_items() -> None:
    """Tests multiple items."""
    list_one: list[int] = [2, 3]
    list_two: list[int] = [3, 4]
    assert concat(list_one, list_two) == [2, 3, 3, 4]


def test_concat_many_items() -> None:
    """Tests many items."""
    list_one: list[int] = [2, 3, 4, 5]
    list_two: list[int] = [3, 4, 5, 6]
    assert concat(list_one, list_two) == [2, 3, 4, 5, 3, 4, 5, 6]