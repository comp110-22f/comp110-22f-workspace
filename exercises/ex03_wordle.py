"""Wordle with 6 tries."""

__author__ = "730553672"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, one_character: str) -> bool:
    """Searches for character within word."""
    assert len(one_character) == 1  # asserts that the character is length 1 and if not, an error will occur
    index_word: int = 0  # index of the word
    while index_word < len(word):  # while the index of the word in less than the length of the word
        if word[index_word] == one_character:  # if the word index equals the character, the return will be True
            return True
        else:
            index_word += 1  # else. the program will continue until it returns True or the while loop becomes false, returning to False
    return False


def emojified(guessed_word: str, same_length_word: str) -> str:
    """The first word is a guess and the second word is the secret word and any characters will result in a printed emoji."""
    assert len(guessed_word) == len(same_length_word)  # asserts that the length of the guess is equal to the length of the secret
    indices: int = 0 
    store_emoji: str = ""
    while indices < len(guessed_word):  # while the indices is less than the length of the guesses word
        if contains_char(same_length_word[indices], guessed_word[indices]):  # if the index of the secret and guessed word are equal
            store_emoji += GREEN_BOX  # a green box will be stored
        else:
            if contains_char(same_length_word, guessed_word[indices]):  # else, the program will go through the indices of the secret word and compare the guessed word
                store_emoji += YELLOW_BOX  # if any characters of the guessed word exist in the secret, a yellow box will be stored
            else:
                store_emoji += WHITE_BOX  # else, a white box will be stored
        indices += 1
    return store_emoji  # the stored emojis will be returned in the print form


def input_guess(expected_length_guess: int) -> str:
    """Given an integer “expected length” of a guess, the function will prompt the user for a guess until the guess is the expected length."""
    guess: str = input(f"Enter a {expected_length_guess} character word: ")
    while len(guess) != expected_length_guess:
        guess = (input(f"That wasn't {expected_length_guess} chars! Try again: "))
    return guess


def main() -> None:  # main results in None so no return is necessary
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    secret_word: str = "codes"
    game_won: bool = False
    turn: int = 1
    while turn <= 6 and game_won is False:  # while the turn number is less than or equal to six, AND the game has not been won
        print(f"=== Turn {turn}/6 ===")  # print the turn number
        guessed: str = input_guess(len(secret_word))  # prompt for a guess input with the same numnber of characters as the secret word
        codify: str = emojified(guessed, secret_word)  # variable that codified the guess against the secret word
        print(codify)  # prints the codified emoji string
        if guessed == secret_word:  # if the guessed word and secret word are the same
            game_won = True  # the game has been won
        else:
            turn += 1  # otherwise, increase the turn by 1
    if game_won is True:
        print(f"You won in {turn}/6 guesses! ")
    else:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()

