"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary 
schools: dict[str, int]

# Initialize to an empty dictionary 
schools = dict()

# Set a key-value paring in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

#Access a value by its key -- "Lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# By its key bc thats how the table is made for looking up
schools.pop("Duke")

# Test for the existence of a key, asking if the key is in schools 
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

# Demonstration of dictionary literals 

# Empty dictionary literal
schools = {} # same as dict()
print(schools)

# Alternatively initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

print(schools["UNCC"])
