"""EX07."""
__author__ = "730311638"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Tests invert when paramenters are empty."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert_many() -> None:
    """Tests invert when many values in original dictionary."""
    a: dict[str, str] = {"1": "2", "3": "4", "5": "6"}
    assert invert(a) == {"2": "1", "4": "3", "6": "5"}


def test_invert_many_again() -> None:
    """Tests invert when many values in original dictionary."""
    a: dict[str, str] = {"11": "22", "33": "44", "55": "66"}
    assert invert(a) == {"22": "11", "44": "33", "66": "55"}


def test_count_empty() -> None: 
    """Tests count when the function parameters are empty."""
    colors: list[str] = []
    assert count(colors) == {}


def test_count_many() -> None:
    """Tests count when there are many colors in the list."""
    colors: list[str] = ["red", "red", "blue", "blue"]
    assert count(colors) == {"red": 2, "blue": 2}


def test_count_many_again() -> None:
    """Tests count when there are many colors in the list again."""
    colors: list[str] = ["red", "red", "red", "yellow", "orange", "blue"]
    assert count(colors) == {"red": 3, "yellow": 1, "orange": 1, "blue": 1}


def test_favorite_color_empty() -> None:
    """Tests favorite color when empty."""
    favorites: dict[str, str] = {}
    assert favorite_color(favorites) == ""


def test_favorite_color_many() -> None:
    """Tests favorite color when many."""
    favorites: dict[str, str] = {"Nickey": "red", "Caroline": "red", "Jordan": "blue"}
    assert favorite_color(favorites) == "red"


def test_favorite_color_again() -> None:
    """Tests favorite color when many again."""
    favorites: dict[str, str] = {"Jo": "red", "Carl": "blue"}
    assert favorite_color(favorites) == "red"