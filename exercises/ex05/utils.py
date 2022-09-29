"""EX05 - List Utility Functions."""

__author__ = "730470086"


def only_evens(xs: list[int]) -> list[int]:
    """Returns list of only the even numbers in a list."""
    new: list[int] = []
    for number in xs:
        if number % 2 == 0:
            new.append(number)
    return new


def concat(a: list[int], b: list[int]) -> list[int]:
    """Given two lists, returns concatination of the two."""
    new: list[int] = []
    for number in a:
        new.append(number)
    for number in b:
        new.append(number)
    return new


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Returrns subset of list."""
    if xs == [] or start >= end:
        return []
    elif start < 0:
        start = 0
    elif end > len(xs):
        end = len(xs)
    new: list[int] = []
    for number in range(start, end):
        new.append(xs[number])
    return new