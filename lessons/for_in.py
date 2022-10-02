"""An example of for in syntax."""

names: list[str] = ["Jeeya", "Ritika", "Dhruti", "Ritesh"]

# Example of iterating thorugh names using a while loop
print("while output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The foolowing for...in loop is thae same as the while loop
print("for...in output:")
for name in names:
    print(name)


# both are the same