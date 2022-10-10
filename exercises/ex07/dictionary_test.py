"""Tests of the different types of dictionaries."""

__author__ = "730553672"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_empty() -> None:
    """Tests empty dictionary."""
    xs: dict[str, str] = dict()
    assert invert(xs) == dict()


def test_invert_some_items() -> None:
    """Tests some items in dictionary."""
    xs: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(xs) == {"b": "a", "d": "c", "f": "e"}


def test_invert_many_items() -> None:
    """Tests many items in dictionary."""
    xs: dict[str, str] = {"a": "b", "c": "d", "e": "f", "g": "h", "i": "j", "k": "l"}
    assert invert(xs) == {"b": "a", "d": "c", "f": "e", "h": "g", "j": "i", "l": "k"}


def test_favorite_color_single() -> None:
    """Tests empty dictionary."""
    xs: dict[str, str] = {"Jack": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_all_same() -> None:
    """Tests same values in dictionary."""
    xs: dict[str, str] = {"John": "blue", "Jamie": "blue", "Jack": "blue"}
    assert favorite_color(xs) == "blue"

    
def test_favorite_color_many() -> None:
    """Tests many items in dictionary."""
    xs: dict[str, str] = {"Jack": "blue", "James": "green", "Jamie": "purple", "Jasmine": "red"}
    assert favorite_color(xs) == "blue"


def test_count_empty() -> None:
    """Tests empty dictionary."""
    xs: list[str] = list()
    assert count(xs) == dict()


def test_count_some_items() -> None:
    """Tests some items in a dictionary."""
    xs: list[str] = ["2", "3", "4"]
    assert count(xs) == {"2": 1, "3": 1, "4": 1}


def test_count_many_items() -> None:
    """Tests many items in a dictionary."""
    xs: list[str] = ["2", "3", "4", "2", "3", "4", "2", "3", "4", "2", "5"]
    assert count(xs) == {"2": 4, "3": 3, "4": 3, "5": 1}