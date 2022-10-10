"""Demonstrations of dictionary capabilites."""


# declaring the type of dictionary
schools: dict[str, int]

# initialize an empty dictionary
schools = dict()

# set a key-value pariing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal representation
print(schools)

# access a value by its key
# side note: have to use single quotes because can't have 2 double quotes
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary
# by ITS key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# of, use if statement
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update/Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# demonstration of dictionary literals

# empty dictionary literal
schools = {} # same as dict()
print(schools)

# alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# what happens when a key does not exist?
# print(schools["UNCC"])

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")