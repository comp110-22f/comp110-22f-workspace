"""Class lesson Python document 9/8/2022."""

def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times."""
    love_note: str = ""
    i = 0

    while i < n:
        love_note += love(to) + "\n"
        i += 1
    
    return love_note

 
subject: str = input("Insert subject name pls: ")

print(love(subject))
print("\n")
print(spread_love(subject, 5))