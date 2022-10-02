"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42

def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")

def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n

# Idiom for maknig a module able to run as a program
# or have its global definitions imported elsewhere
if __name__ == "main":
    main()
else:
    print(f"helpers.py was imported: {__name__}")
    # it is not idiomaticto have an else branch