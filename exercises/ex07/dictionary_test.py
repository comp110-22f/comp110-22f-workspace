"""EX07 - Tests For Dictionary."""

__author__ = "730470086"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count
import pytest


with pytest.raises(KeyError):
    my_dictionary = {'no': 'Haley', 'yes': 'Haley'}
    invert(my_dictionary)


def test_invert_edge() -> None:
    """Tests for one entry."""
    assert invert({'circle': 'round'}) == {'round': 'circle'}


def test_invert_use_capital() -> None:
    """Tests if capital letters do not raise keyerror."""
    assert invert({'Pig': 'pig', 'Sand': 'sand'}) == {'pig': 'Pig', 'sand': 'Sand'}


def test_invert_use_multiple() -> None:
    """Tests if multiple entries are inverted correctly."""
    assert invert({'pig': 'oink', 'cow': 'moo', 'cat': 'meow'}) == {'oink': 'pig', 'moo': 'cow', 'meow': 'cat'}


def test_favorite_color_edge() -> None:
    """Tests for one entry."""
    assert favorite_color({'Haley': 'blue'}) == 'blue'


def test_favorite_color_use_equal() -> None:
    """Tests if two have the same number, it returns the first."""
    assert favorite_color({'Haley': 'blue', 'Maya': 'blue', 'Addie': 'red', 'Katie': 'red'}) == 'blue'


def test_favorite_color_use_multiple() -> None:
    """Tests if multiple entries produces one color."""
    assert favorite_color({'Haley': 'yellow', 'Maya': 'orange', 'Addie': 'red', 'Katie': 'orange'}) == 'orange'


def test_count_edge() -> None:
    """Tests for one entry."""
    assert count(['apple']) == {'apple': 1}


def test_count_use_numerous() -> None:
    """Tests if works for numerous items in a list."""
    assert count(['apple', 'banana', 'orange', 'mango']) == {'apple': 1, 'banana': 1, 'orange': 1, 'mango': 1}


def test_count_use_multiple() -> None:
    """Tests if works for multiple entries of item."""
    assert count(['apple', 'apple', 'orange', 'apple', 'banana']) == {'apple': 3, 'orange': 1, 'banana': 1}