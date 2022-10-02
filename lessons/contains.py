"""Example implementing a list utility function."""

# function name: contains:
# we still have 2 parameters: needle(str), haystack(list[str])
# return type bool
# gameplan:
# 1. start with the first index
# 2. loop through every index
    # 2.A test if item at index equal to needle
        # 2.AA return true if found
# 3 return false


def contains(needle: str, haystack: list[str]) -> bool:
    """Finds if value is found any time in list."""
    indices: int = 0
    while indices < len(haystack):
        if needle == haystack[indices]:
            return True
        else:
            indices += 1
    return False