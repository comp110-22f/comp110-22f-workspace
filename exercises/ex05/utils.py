"""Utils Ex05."""
__author__ = "730311638"


def only_evens(even_and_odds: list[int]) -> list[int]:
    """Given a list, returns a list of only the even ints."""
    evens: list[int] = list()
    i: int = 0
    while i < len(even_and_odds):
        if even_and_odds[i] % 2 == 0:
            evens.append(even_and_odds[i])
        i += 1
    return evens


def concat(x: list[int], y: list[int]) -> list[int]:
    """Adds second list to the end of the first list."""
    i: int = 0
    z: list[int] = list()
    while i < len(x):
        z.append(x[i])
        i += 1
    i = 0
    while i < len(y):
        z.append(y[i])
        i += 1 
    return z


def sub(x: list[int], start: int, end: int) -> list[int]:
    """Returns a List that is a subset of given list."""
    subset: list[int] = list()
    end -= 1
    if len(x) == 0 or start > len(x) or start == len(x) or end > len(x):
        return []
    else: 
        subset.append(x[start])
        subset.append(x[end])
        return subset