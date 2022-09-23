"""Examples of importing Python."""


from lessons import helps


def main() -> None:
    """Entrypoint of program."""
    print(helps.powerful(2, 4))
    print(f"The answer: {helps.THE_ANSWER}")


if __name__ == "__main__":
    main()
