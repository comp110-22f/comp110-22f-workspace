"""'List' Utility Function Practice."""

__author__ = "730553672"


def all(list_of_integers: list[int], single_int: int) -> bool:
    """Checks if the single integer matches all the integers in the list."""
    indices: int = 0
    if len(list_of_integers) == 0:
        return False
    while indices < len(list_of_integers):
        if single_int == list_of_integers[indices]:
            indices += 1
        else:
            return False
    return True


def max(integer_list: list[int]) -> int:
    """When given an integer list, will return the highest valued integer."""
    indices: int = 0
    if len(integer_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_value: int = integer_list[indices]
    while indices < len(integer_list):
        if integer_list[indices] > max_value:
            max_value = integer_list[indices]
        indices += 1
    return max_value


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Compares if the two lists are equal."""
    indices: int = 0
    while len(list_one) == len(list_two):
        while indices < len(list_one):
            if list_one[indices] != list_two[indices]:
                return False
            else:
                indices += 1
        return True
    return False