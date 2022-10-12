"""Choose Your Own Adventure!"""
__author__ = "730311638"


from random import randint


points: int = 0
player: str = ""


def main() -> None:
    """Main game body function."""
    global points
    greet()
    options()
    if points > 1 and points <= 3:
        print(f"{player}, Your song is 'When it rains it pours!'")
        print(f"{player}, You earned {points} points!")
    if points > 4 and points < 7:
        print(f"{player}, Your song is 'Better Together'! ")
        print(f"{player}, You earned {points} points!")
    if points > 6:
        print(f"{player}, Your song is 'Hurricane'!")
        print(f"{player}, You earned {points} points!")
    play_again: str = input("Play again? Yes or No.")
    if play_again == "Yes":
        main()
    if play_again == "No":
        quit()


def greet() -> None:
    """Function that greets the player."""
    emoji: str = "\U0001F920"
    print(f"Welcome to our quiz! Which Luke Combs song are you {emoji} ?")
    global player 
    player = input("What is your name? ")


def options() -> int:
    """3 options to start the game."""
    i: int = 0
    global player
    global points
    print("Choose one of the 3 options: Route 1, Route 2, or End Experience. ")
    player_option: str = input("Enter your choice: ")
    while i < 1:
        if player_option == "Route 1":
            route_1()
            i += 1
        if player_option == "Route 2": 
            route_2(points)
            i += 1
        if player_option == "End Experience":
            print(f"Goodbye! You earned {points} adventure points!")
            player_option = input("Enter your choice: ")
    return points


def route_1() -> int:
    """First route for the player."""
    global points
    global player
    i: int = 0
    while i < 1:
        question_1: str = input(f"{player}, what hobby do you prefer? Fishing, Riding horses, or Fixing your truck? ")
        if question_1 == "Fishing":
            points += 1
            print(f"{points} point earned!")
            i += 1
        if question_1 == "Riding horses":
            points += 2
            print(f"{points} points earned!")
            i += 1
        if question_1 == "Fixing your truck":
            points += 3
            print(f"{points} points earned!")
            i += 1
    while i < 2:
        question_2: str = input(f"{player}, what drink do you prefer? Sweet tea or Lemonade? ")
        if question_2 == "Sweet tea":
            points += 1
            i += 1
        if question_2 == "Lemonade":
            points += 2
            i += 1
    return points
    

def route_2(x: int) -> int: 
    """Second option from the main body."""
    global points
    global player
    while x == 0: 
        question_3: str = input(f"{player}, What season do you prefer? Summer or Winter?")
        summer: str = "Summer"
        winter: str = "Winter"
        if question_3 == summer:
            points += 2
            x += 1
        if question_3 == winter:
            points += 1
            x += 1
    while x == 1: 
        question_4: str = input(f"{player} Which color do you prefer? Blue or Red?")
        blue: str = "Blue"
        red: str = "Red"
        if question_4 == blue: 
            points += 4
            x += 1
        if question_4 == red:
            points += 2
            x += 1
    while x == 2:
        y: int = randint(1, 4)
        points = y + points
        x += 1
    return points


if __name__ == "__main__":
    main()