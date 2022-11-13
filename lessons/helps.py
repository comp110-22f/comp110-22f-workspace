"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n

print("helps.py was evaluated")  


if __name__ == "__main__":
    main()
else: 
    print(f"helps.py was imported: {__name__}")