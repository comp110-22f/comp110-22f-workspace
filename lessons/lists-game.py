"""Examples of using lists in a simple 'game'. """


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:  # while the length of the rolls is 0 or the last roll is not equal to 1:
    rolls.append(randint(1, 6))

print(rolls)

# remove and item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls!
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access individual item
# print(rolls[0])
# print(rolls[1])

# # Access the lengtj of a list (# of items)
# last_index: int = len(rolls) - 1
# print(last_index)