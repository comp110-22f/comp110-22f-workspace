"""Demonstrations of dictoinary capabilities."""

# Declaring the type of a dicitonary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value paring in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key ("lookup")
print(f"UNC has {schools['UNC']} students")

# Revove a key-value pair from a dictionry
# by its key.
schools.pop("Duke")

# Test for the existance of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else: 
    print("No key 'Duke' in schools")

print(schools)

# Demonstration of dictionary literals
schools = {} # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

different: dict[str, str] = {"Crazy": "Eight"}
print(different)

schools["UNC"] += 600
print(schools["UNC"])

# Example looping over the keys of a dictionary
for school in schools:
    print(f"Key: {school} -> Value {schools[school]}")