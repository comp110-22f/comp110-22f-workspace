"""EX04 - Utils."""

__author__ = "730470086"


def all(a: list[str], b: int) -> bool:
    """Determines if all numbers in list are the integer."""
    # Check if b is in list a
    counter: int = 0
    if len(a) == counter:
        return False
    while counter < len(a):
        while a[counter] == b:
            counter += 1
            if a[counter] != b:
                return False
            else: 
                return True


def max(input: list[int]) -> int:
    """Returns the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    big = input[0]
    for number in input:
        if number > big:
            big = number
    return big


def is_equal(c: list[int], d: list[int]) -> bool:
    """Determines if all indexes are equall in a list."""
    if c == d:
        return True
    else:
        return False