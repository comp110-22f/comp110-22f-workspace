"""Examples of using lists in a simple 'game'."""

from random import randint

rolls: list[int] =  list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove an item from the list by its index 
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls!
i: int = 0
total: int = 0

while i < len(rolls):
    total += rolls[i]
    i += 1

print(f"Sum is {total}!")

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item:
# print(rolls[0])
# print(rolls[1])

# # Access the length of a list 
# print(len(rolls))
