"""Functions utilizing lists and commonly used functions."""

__author__ = "730574292"


def all(list_input: list[int], search_for: int) -> bool:
    """Function takes a list of integers and an integers and searches through list to check if all values are equal to int. Returns True or False."""
    if len(list_input) == 0:
        return False
    
    idx: int = 0
    while idx < len(list_input):
        if list_input[idx] != search_for:
            return False
        idx += 1
    
    return True


def max(list_input: list[int]) -> int:
    """Function takes a list of integers and determines the greatest value in the list."""
    if len(list_input) == 0:
        raise ValueError("max() arg is an empty List")

    maximum: int = list_input[0]
    idx: int = 1

    while idx < len(list_input):
        if maximum < list_input[idx]:
            maximum = list_input[idx]
        idx += 1
    
    return maximum


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Function takes two lists of integers and determines if all values of both lists are the same. Returns a boolean."""
    idx: int = 0

    if len(list_one) != len(list_two):
        return False

    while idx < len(list_one) and idx < len(list_two):
        if list_one[idx] != list_two[idx]:
            return False
        else:
            idx += 1
    
    return True