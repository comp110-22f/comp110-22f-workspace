""""An example of conditional (if-else) statements"""

from random import choice

SECRET: int = choice([1, 2, 3, 4, 5])
print(SECRET)

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")
else:
    print("Sorry, you guessed incorrectly :( \nThe number was " + str(SECRET) + ".")
    print("Try running the program again.")

print("Game over.")