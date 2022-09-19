"""An example of a list utility algorithm."""

# Name: contains
# Function with 2 parameters 
# needle - what we are searching for 
# haystack - what we're searching through 
# Return type: bool 
def contains(needle: str, haystack: list[str]) -> bool:
# Start from first index
    i: int = 0 
# loop through each index of list
    while i < len(haystack):   
        if haystack[i] == needle:
            return True 
#   Test if equal to needle
#       # Yes! Return True
    i += 1 
# Return False 
    return False