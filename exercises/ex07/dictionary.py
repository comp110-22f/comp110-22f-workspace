"""EX07 Dictionaries."""
__author__ = "730311638"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, inverts keys and values, returns new dictionary."""
    result: dict[str, str] = {}
    values: str = ""
    for key in a:
        values = a[key]
        result[values] = key
    return result


def favorite_color(favorites: dict[str, str]) -> str: 
    """Returns the most popular color."""
    result: dict[str, str] = {} 
    for key in favorites:
        if favorites[key] in result:
            result[favorites[key]] += 1
        else: 
            result[favorites[key]] = 1
    return max(result)
       

def count(colors: list[str]) -> dict[str, int]:
    """Given a list, returns the frequencies of each value in the list."""
    result: dict[str, int] = {}
    for item in colors:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result