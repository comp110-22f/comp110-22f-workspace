"""Functions and loves!"""

def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

# print(love("Jeeya")): This is used for the zsh terminal, not the python REPL


def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    counter_love_note: int = 0
    while counter_love_note < n:
        love_note += love(to) + "\n"  # in this line, love(Jeeya) goes to love function in the form of string
        counter_love_note += 1
    return love_note