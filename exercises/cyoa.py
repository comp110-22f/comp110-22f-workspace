"""Choose Your Own Adventure."""

__author__ = "730470086"

from random import randint
points: int = 0
player: str = ""
EMOJI: str = "\U0001F970"
correct: bool = True


def main() -> None:
    """Entry point into game."""
    global points
    global correct
    global player
    points = 0
    greet()
    heads: str = "1"
    points += next(1)
    if points == 1:
        print(f"You now have {points} correct guesses in a row!")
    else:
        oops()
    guess_one: str = input(f"{player}, you were correct! What is your next guess? Enter 1 for heads or 2 for tails. If you want to quit enter 'end': ")
    if guess_one == "end":
        end()
    if guess_one == heads:
        points += 1
        print(f"You now have {points} correct guesses in a row!")
    if guess_one != heads:
        oops()
    while correct is True:
        if guess_one == heads:
            next_guess: str = input(f"{player}, what is your next guess? Enter 1 for heads or 2 for tails. If you want to quit enter 'end': ")
            if next_guess == heads:
                points += 1
                print(f"You now have {points} correct guesses in a row!")
                correct = True
            else:
                correct = False
                oops()
        else:
            correct = False
            points += 0
            oops()


def greet() -> None:
    """Greats the player."""
    global player
    player = input("What is your name? ")
    print(f"Welcome {player} {EMOJI}! This game is called flip coin. Guess whether the coin is heads or tails and see how many you can get right in a row! Have fun!")


def next(xs: int) -> int:
    """Next guess."""
    global player
    global points
    right: str = (f"{randint(1, 2)}")
    if xs == 1:
        yay: str = input(f"So {player}, what is your guess? Enter 1 for heads or 2 for tails. If you want to quit enter 'end': ")
        if yay == "end":
            end()
        if yay == right:
            xs += 0
        else:
            xs -= 1
    return xs


def oops() -> None:
    """End of the game."""
    global player
    global points
    end: str = input(f"Sorry that was wrong. {player} you guessed heads or tails {points} times in a row. If you would like to play again enter 'yes': ")
    if end == "yes":
        main()
    else: 
        print(f"Thanks for playing {player} {EMOJI}!")
    exit()


def end() -> None:
    """Player wants to stop."""
    global player
    global points
    print(f"Thanks for playing {player} {EMOJI}! You guessed heads or tails {points} times!")


if __name__ == "__main__":
    main()