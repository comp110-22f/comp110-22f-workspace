"""One-Shot Wordle with Loops."""

__author__ = "730553672"

secret_word: str = "python"
guessed_word: str = input(f'What is your {len(secret_word)}-letter guess? ')
index_guessed_word: int = 0
emoji_guess: str = ""

while len(guessed_word) != len(secret_word):  # while the length of the guessed word is not equal to the length of the secret word
    guessed_word = input(f'That was not {len(secret_word)} letters! Try again: ')

while index_guessed_word < len(secret_word):  # when the index of the guessed word is less than the length of the secret word
    if guessed_word[index_guessed_word] == secret_word[index_guessed_word]:  # if the index of the guessed word is equal to the index of the secret word
        emoji_guess += "\U0001F7E9"  # store green box
    else:
        guessed_character_exists: bool = False  # if the character does not exist
        alternate_indices: int = 0
        while guessed_character_exists is not True and alternate_indices < len(secret_word):  # while the guessed character does not exists and the alternate indices number is less than the length of the secret word
            if secret_word[alternate_indices] == guessed_word[index_guessed_word]:  # if the alternate index of the secret word matches the index of the guessed word
                guessed_character_exists = True  # change this variable to true
            else:
                alternate_indices += 1
        if guessed_character_exists is True:
            emoji_guess += "\U0001F7E8"  # store yellow box
        else:
            emoji_guess += "\U00002B1C"  # store white box
    index_guessed_word += 1
print(emoji_guess)

if guessed_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon! ")