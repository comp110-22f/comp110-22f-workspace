"""Tests for the dictionary.py functions."""

__author__ = "730574292"

import pytest
from dictionary import invert, favorite_color, count


def test_invert1() -> None:
    """Test function for invert() function. Checks if invert() successfully swaps all keys and values of a dictionary."""
    assert (invert({"spring": "fall", "summer": "winter", "stand": "lay", "love": "hate"}) == {"fall": "spring", "winter": "summer", "lay": "stand", "hate": "love"})


def test_invert2() -> None:
    """Test function for invert() function. Checks if a KeyError is raised when two values of a dictionary are the same and it attempts to swap values and keys."""
    with pytest.raises(KeyError):
        my_dictionary: dict = {"spring": "fall", "summer": "winter", "stand": "fall"}
        invert(my_dictionary)


def test_edge_invert() -> None:
    """Edge test function for invert() function. Checks if invert() works on an empty dictionary."""
    assert (invert({}) == {})


def test_favorite_color1() -> None:
    """Test function for favorite_color() function. Checks if favorite_color() correctly identifies the most frequent color in the dictionary."""
    assert (favorite_color({"Max": "orange", "Opal": "blue", "Macey": "orange", "Pearl": "orange"}) == "orange")


def test_favorite_color2() -> None:
    """Test function for favorite_color() function. Checks if favorite_color() correctly identifies the most frequent color in the dictionary if there is a tie in frequency."""
    assert (favorite_color({"Noah": "red", "Daisy": "yellow", "Bryan": "teal", "Ashton": "teal", "Lindsay": "red"}) == "red") 


def test_edge_favorite_color() -> None:
    """Test function for favorite_color() function. Checks if favortie_color() return empty string when given an empty dictionary."""
    assert (favorite_color({}) == "")


def test_count1() -> None:
    """Test funciton for count() funciton. Checks if count() returns correct dictionary with correct frequencies for list of values."""
    assert (count(["orange", "apple", "hotdog", "steak", "burger", "apple", "soup", "soup", "hotdog"]) == {"orange": 1, "apple": 2, "hotdog": 2, "steak": 1, "burger": 1, "soup": 2})


def test_count2() -> None:
    """Test funciton for count() funciton. Checks if count() returns correct dictionary with correct frequencies for list of values."""
    assert (count(["bird", "bird", "birdie", "bird"]) == {"bird": 3, "birdie": 1}) 


def test_edge_count1() -> None:
    """Test funciton for count() funciton. Checks if count() returns empty dictionary when given an empty list."""
    assert (count([]) == {})