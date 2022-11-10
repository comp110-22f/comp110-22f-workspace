"""EX05 - Tests For List Utility Functions."""

__author__ = "730470086"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Tests if list is empty."""
    assert only_evens([]) == []


def test_only_evens_containing_odds() -> None:
    """Tests for list with odd numbers."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]


def test_only_evens_all_even() -> None:
    """Tests if list is all even."""
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_concat_list_of_one() -> None:
    """List only contains one item."""
    assert concat([1], [2]) == [1, 2]


def test_concat_empty() -> None:
    """Tests if it excludes the empty list."""
    assert concat([5], []) == [5]


def test_concat_different_sizes() -> None:
    """Tests if it works for lists of different sizes."""
    assert concat([1, 2, 3, 4, 5], [6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_sub_empty() -> None:
    """Tests if it returns the empty list."""
    assert sub([], 1, 2) == []


def test_sub_start_bigger() -> None:
    """Tests if it returns if start is bigger than end."""
    assert sub([1, 2, 3], 4, 1) == []


def test_sub_one() -> None:
    """List only contains one item."""
    assert sub([1], 2, 3) == [1] 