"""EX04 - Utils."""

__author__ = "730470086"

def all(a: list[str], b: int) -> bool:
    """Determines if number is in list."""
    # Check if b is in list a
    counter: int = 0
    while counter < len(a):
        if a[counter] == b:
            return True
        else:
            track: int = 0
            existence: bool = False
            while((existence is False) & (track < len(a))):
                if a[counter] == b:
                    existence = True
                else:
                    track += 1
                    counter += 1
            track = 0
        if existence is True:
            return True
        else:
            return False


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