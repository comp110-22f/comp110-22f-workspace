"""Choose your own adventure program."""

# A number guessing game such as the generating a random number and asking the user 
# to guess it and counting the number of attempts it takes them to guess it correctly.

__author__ = "730553672"

player: str = ""
points: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
PARTY: str = "\U0001F389"
CONFETTI: str = "\U0001F38A"
RED_X: str = "\U0000274C"


def main() -> None:
    """Entrypoint of program."""
    greet()
    print(f"Hello {player}! You now have 3 options.")
    print("Option 1: End the experience.")
    print("Option 2: This option will use your number of points as the maximum value of the random number.")
    print("Option 3: Choose a range and then guess the random number.")
    game: str = str(input("Would you like to choose an option? Yes or No? "))
    global points
    while game == "Yes":
        print(f"You have {points} points!. ")
        choice: int = int(input("Please choose option 1, 2, or 3. "))
        if choice == 1:
            print(option_one("1"))
        elif choice == 2:
            points = (option_two(points))
            print(f"You have {points} points! ")
        else:
            option_three()
            print(YELLOW_BOX * 75)
        game = str(input("Would you like to play any of the options again? Yes or No? "))
    print(f"{PARTY * 3} Thank you {player} for playing the game today! {PARTY * 3}")
    print(f"You finished with {points} points! {PARTY * 2}")


def greet() -> None:
    """Greeting to the player of the game."""
    print("Welcome! The game you are playing today involves the genertion of a random number and you, as the player, will try to guess it.")
    name: str = input("What is your name?: ")
    global player
    player += name


def option_one(y: str) -> str:
    """Option that ends the experience."""
    return (f"Thank you for playing the game! You ended with {points} points! ")


def option_two(point: int) -> int:
    """Option 2."""
    print(WHITE_BOX * 75)
    print(f"Hello {player}! In this option, your total points will be the maximum value and the minimum will be zero.")
    point += 10
    print(f"You will automatically recieve 10 points everytime you choose this option! {PARTY * 2}")
    print(GREEN_BOX * 75)
    print("Directions: Based on the number of points you have, that will be the max. This game will then choose a random number in that range and you will have to guess it.")
    print("If you guess correctly, you will recieve 50 points!")
    print("If you guess incorrectly, you will only get 1 point each time you guess wrong.")
    print("Let's start! ")
    start: str = str(input("Are you sure you want to choose this option? Yes or No? "))
    while start == "Yes":
        import random
        chosen_number: int = random.randint(0, point)
        guessed: int = int(input(f"Guess a number between 0 and {point}: "))
        if guessed <= 0 or guessed >= point:
            guessed = int(input(f"{player}, please guess another number within the range. "))
        if guessed == chosen_number:
            point += 50
            print(f"{CONFETTI * 3} YAY! You guessed the number correctly! You have {point} points. {CONFETTI * 3}")
        else:
            point += 1
            print(f"That is incorrect. {RED_X * 2} ")
            print(f"You have {point} points!")
            again: str = str(input("Would you like to play again? Yes or No? "))
            while again == "Yes":
                guessed = int(input(f"{player}, please enter another guess: "))
                if guessed == chosen_number:
                    point += 50
                    print(f"{CONFETTI * 3} YAY! You guessed the number correctly! You have {point} points. {CONFETTI * 3}")
                    again = "No"
                else:
                    point += 1
                    print(f"That is incorrect. {RED_X * 2} ")
                    print(f"You have {point} points!")
                    again = str(input("Would you like another guess? Yes or No? "))
        start = str(input("Would you like to restart this option and play the game again? Yes or No? "))
    return point


def option_three() -> None:
    """Option 3."""
    print(WHITE_BOX * 75)
    print(f"Hello {player}! In this option, you will choose different ranges of numbers and then try to guess the random number.")
    print(GREEN_BOX * 75)
    print("Directions: Think of a range of numbers. This game will then choose a random number in that range and you will have to guess it.")
    print("If you guess correctly, you will recieve 50 points!")
    print("If you guess incorrectly, you will only get 1 point each time you guess wrong.")
    print("Let's start! ")
    start: str = str(input("Are you sure you want to choose this option? Yes or No? "))
    while start == "Yes":
        min_value: int = int(input("Enter the minimum value: "))
        max_value: int = int(input("Enter the maximum value: "))
        while min_value >= max_value:
            max_value = int(input(f"Try again {player}. Please enter a number larger than the minimum value: "))
        import random
        secret_number: int = random.randint(min_value, max_value)
        guess: int = int(input(f"Guess a number between {min_value} and {max_value}. "))
        if guess <= min_value or guess >= max_value:
            guess = int(input(f"{player}, please guess another number within the range. "))
        if guess == secret_number:
            global points
            points += 50
            print(f"{CONFETTI * 3} YAY! You guessed the number correctly! You have {points} points. {CONFETTI * 3}")
        else:
            points += 1
            print(f"That is incorrect. {RED_X * 2} ")
            print(f"You have {points} points!")
            again: str = str(input("Would you like to play again? Yes or No? "))
            while again == "Yes":
                guess = int(input(f"{player}, please enter another guess: "))
                if guess == secret_number:
                    points += 50
                    print(f"{CONFETTI * 3} YAY! You guessed the number correctly! You have {points} points. {CONFETTI * 3}")
                    again = "No"
                else:
                    points += 1
                    print(f"That is incorrect. {RED_X * 2} ")
                    print(f"You have {points} points!")
                    again = str(input("Would you like another guess? Yes or No? "))
        start = str(input("Would you like to restart this option and play the game again? Yes or No? "))
    print(f"Thank you {player} for playing!")
    print(f"You have {points} points! {PARTY * 2}")
    

if __name__ == "__main__":
    main()