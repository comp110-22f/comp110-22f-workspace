"""Creation of different types of dictionaries."""

__author__ = "730553672"


def invert(change: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values of a dictionary."""
    new = dict()
    for item in change:
        val = change[item]
        if val in new:
            raise KeyError("The original dictionary has multiple values that would result in the same key.")
        new[val] = item
    return new


def favorite_color(x: dict[str, str]) -> str:
    """Given names and colors, will return the most common color."""
    colors: list[str] = list()
    result: dict[str, int] = dict()
    for key in x:
        colors += [x[key]]
    for item in colors:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    max_value: int = 0
    final: str = ""
    while result[item] > max_value:
        for item in result:
            while result[item] > max_value:
                max_value = result[item]
                final = item
    return final
        

def count(y: list[str]) -> dict[str, int]:
    """Given a list, a dictionary will be returned with the list and the count of the list items."""
    creation: dict[str, int] = dict()
    for item in y:
        if item in creation:
            creation[item] += 1
        else:
            creation[item] = 1
    return creation