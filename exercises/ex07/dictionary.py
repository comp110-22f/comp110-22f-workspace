"""EX07 - Dictionary Practice."""

__author__ = "730470086"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    new: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in new:
            raise KeyError("More than one of the same key.")
        else:
            new[dictionary[key]] = key
    return new


def main() -> None:
    """Testing favorite color."""
    print(favorite_color({"Haley": "Blue", "Sydney": "Green", "Maya": "Pink", "Katie": "Orange"}))


def favorite_color(names: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    counter: int = 0
    popular: str = ""
    color: str = ""
    for key in names:
        i: int = 0
        color = names[key]
        for count in names:
            if names[count] == color:
                i += 1
            if i > counter:
                counter = i
                popular = color
    return popular


def count(original_list: list[str]) -> dict[str, int]:
    """Returns a list with the number of times a value appeared."""
    dictionary: dict[str, int] = {}
    for item in original_list:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary 