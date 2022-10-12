"""Game in which user goes to UNC dining hall and eats!"""
__author__ = "730574292"

from random import randint

# Below are emotion emojis used throughout the program.
HAPPY: str = "\U0001F604"
SMILE: str = "\U0001F642"
SAD: str = "\U00002639"
YUM: str = "\U0001F60B"
DISAPPOINTED: str = "\U0001F615"
MIND_BLOWN: str = "\U0001F92F"
DIZZY: str = "\U0001F635"
DEAD: str = "\U0001F635"
BARF: str = "\U0001F92E"

# Below are other miscellaneous emojis used throughout the program.
EXCLAIMATION_POINT = "\U00002757"
FOOTPRINT = "\U0001F463"

# Below are food emojis representing food at both dining halls.
BAGEL: str = "\U0001F96F"
FLAPJACKS: str = "\U0001F95E"
CHICKEN: str = "\U0001F357"
HAMBURGER: str = "\U0001F354"
FRIES: str = "\U0001F35F"
PIZZA: str = "\U0001F355"
DELI_SANDWICH: str = "\U0001F32E"
SALAD: str = "\U0001F957"
ICE_CREAM: str = "\U0001F366"
COOKIE: str = "\U0001F36A"

# Below are food emojis representing food at Chase Dining Hall.
CURRY_RICE: str = "\U0001F35B"
SUSHI: str = "\U0001F363"
SPAGHETTI: str = "\U0001F35D"
PRETZEL: str = "\U0001F968"

# Below are food emojis representing food at Lenoir Dining Hall.
CAKE: str = "\U0001F370"
POTATOES: str = "\U0001F954"
EGGPLANT: str = "\U0001F346"
TOMATOES: str = "\U0001F345"
MUSHROOMS: str = "\U0001F344"

# Below are miscellaneous named constants. 
FULL: int = 100         # Value to be reached in order to be full.
SUPER_FILLING: int = 20
FILLING: int = 15
NOT_FILLING: int = 10
DENOM_VAL: int = 25     # Is the constant denominator for determining how filling each food item is. 

# Below are global variables used throughout the program.
points: int         # Tracks how much more of the game remains, or, in other words, how 'full' the user is
player: str         # Contains name of user.
playing: bool       # Tracks when the game ends.
popped: str         # Tracks what the last thing the user ate was.
dining_hall: str    # Records the dining hall that the user chooses.
food_dict: dict[str, str]
# Contains options for food from the dining hall. Is food that the user is allowed to choose from. 


def pound_to_continue() -> None:
    """Requests the student to input value to continue. Also allows the user to quit."""
    global playing
    user_input: str = input(">>> ")
    while user_input != "#" and user_input != "quit":
        user_input = input(">>> ")
    if user_input == "quit":
        playing = False


def print_full_o_meter() -> None:
    """Function prints full-o-meter."""
    print(f"FULL_O_METER: {points}/{FULL}")


def check_if_full(points: int) -> int:
    """Function checks if the user is full (in other words, if points is greater than or equal to 100). Returns how many more point are needed."""
    global playing
    full_points_left = FULL - points
    if points >= FULL:
        playing = False
        print("You're full!")
    return full_points_left


def generate_food_selection() -> None:
    """Function determines the selection of food available to the user based on the dining hall they choose."""
    global food_dict
    global dining_hall
    food_dict = {
        "BAGEL": BAGEL,
        "CHICKEN": CHICKEN,
        "HAMBURGER": HAMBURGER,
        "FRIES": FRIES,
        "PIZZA": PIZZA,
        "DELI SANDWICH": DELI_SANDWICH,
        "SALAD": SALAD,
        "ICE CREAM": ICE_CREAM,
        "COOKIE": COOKIE}

    food_dict_type = dict[str, str]

    chase_food_dict: food_dict_type = {
        "CURRY RICE": CURRY_RICE,
        "FLAPJACK": FLAPJACKS,
        "SUSHI": SUSHI,
        "SPAGHETTI": SPAGHETTI,
        "PRETZEL": PRETZEL}

    lenoir_food_dict: food_dict_type = {
        "CAKE": CAKE,
        "POTATOES": POTATOES,
        "EGGPLANT": EGGPLANT,
        "TOMATOES": TOMATOES,
        "MUSHROOMS": MUSHROOMS}

    if dining_hall == "Lenoir":
        for each in lenoir_food_dict:
            food_dict[each] = lenoir_food_dict[each]
    elif dining_hall == "Chase":
        for each in chase_food_dict:
            food_dict[each] = chase_food_dict[each]


def choose_dining_hall() -> None:
    """Function prompts the user to choose a dining hall."""
    global dining_hall
    global playing
    tmp_input = input("What dining hall do you want to go to? Type 'C' for Chase and 'L' for Lenoir. If you want to quit, type 'quit': ")
    
    dining_hall = ""

    while tmp_input != "C" and tmp_input != "c" and tmp_input != "l" and tmp_input != "L" and tmp_input != "quit" and tmp_input != "QUIT":
        tmp_input = input()

    if tmp_input == "quit" or tmp_input == "QUIT":
        playing = False
        goodbye()
    elif tmp_input == "c" or tmp_input == "C":
        dining_hall = "Chase"
    elif tmp_input == "L" or tmp_input == "l":
        dining_hall = "Lenoir"

    if dining_hall == "Chase" or dining_hall == "Lenoir":
        generate_food_selection()


def choose_food() -> None:
    """Function allows you to choose which food to eat based on a selection provided to you."""
    global dining_hall
    global popped
    global food_dict
    print(f"Here are your options at {dining_hall}, {player}:")
    
    i: int = 0
    for each in food_dict:
        print(f"{i}: {food_dict[each]} {each}")
        i += 1

    tmp_food_selection: str = input("Pick one! (Type the name of the food you want in all caps.) ")
    while tmp_food_selection not in food_dict:
        print(f"That's not one of the options! Try again, {player}.")
        tmp_food_selection = input()
    
    popped = tmp_food_selection
    food_dict.pop(tmp_food_selection)


def get_food_points() -> int:
    """Function randomly determines the number of points the food you chose gives you. Returns this value."""
    global popped
    food_points: int = (ord(popped[0]) // DENOM_VAL) + 12
    if food_points > SUPER_FILLING: 
        print(f"Super filling!!! {MIND_BLOWN}")
    elif food_points > FILLING:
        print(f"That was pretty filling! {YUM}")
    print(f"+{food_points} full points.")
    return food_points


def food_quality() -> None:
    """Function randomly determines if the food you ate is ends your game."""
    global playing
    global popped
    random_int = randint(0, 100)
    random_int2 = randint(19, 21)
    if random_int // random_int2 == 0:
        playing = False
        print(f"OMG!!! {DIZZY}{BARF}{DEAD} That {popped} you just ate killed you!! {DISAPPOINTED}")
        print("GAME OVER!")


def goodbye() -> None:
    """Says goodbye to the user and displays collected points."""
    global points
    print(f"You accumulated {points} adventure/full points.")

    print("I hope to see you again!")
    print("Goodbye!")
    print("GAME OVER!")


def greet() -> None:
    """Greets the player and gives information about the game."""
    global player
    global playing
    player = input("\nBefore we start, what's your name?: ")
    print(f"\nWelcome, {player}! {HAPPY}")

    print("First off, please type '#' to continue.")
    pound_to_continue()

    print(f"Great! {SMILE} Seems like you have the hang of it.")
    print("Make sure you type '#' whenever you see '>>>' in order to advance through this game.")
    pound_to_continue()

    print(f"GRUMBLEEEEEE{EXCLAIMATION_POINT*3}")
    pound_to_continue()

    print("Uhhh...What was that?")
    pound_to_continue()

    print(f"GRUMBLEEEEEE{EXCLAIMATION_POINT*3}")
    pound_to_continue()

    print("Wait, is that coming from you?!")
    pound_to_continue()

    print(f"GRUMBLEEEEEE{EXCLAIMATION_POINT*3}")
    pound_to_continue()

    print("Wow, you seem really hungry.")
    pound_to_continue()

    print(f"GRUMBLEEEEEE{EXCLAIMATION_POINT*3}")
    print("Okay, okay, I get it.")
    pound_to_continue()

    print("Let's check out a dining hall and get you some food.")
    pound_to_continue()

    print("Oh, but before we start! I just remembered something really important...")
    pound_to_continue()

    print("I've heard that the dining halls here are...well...not the best.")
    pound_to_continue()

    print("You might want to be careful picking out what you want because the food might be deadly!")
    pound_to_continue()

    print("....")
    pound_to_continue()

    print("I'm kidding, of course.")
    pound_to_continue()

    print("Probably.")
    pound_to_continue()

    print(f"GRUMBLEEEEEE{EXCLAIMATION_POINT*7}")
    print("Anyways, let's go! Make sure to get your fill!")
    print("***Every time you eat something, you'll get feedback on how much more you need to eat to be full.***")
    
    pound_to_continue()
    print(f"***Your full-o-meter is at {points} right now and you need to get to {FULL} to be full!***")    
    print_full_o_meter()

    pound_to_continue()
    choose_dining_hall()

    if playing:
        print("Onward!!!")
        print(f"{FOOTPRINT*5}")


def main() -> None:
    """Function that serves as the entrypoint for this program/game."""
    global points
    global playing
    playing = True
    points = 0
    greet()

    if playing:
        print("NOTE: ***You can type 'quit' to quit the program whenever you are see '>>>'!!!***")
        pound_to_continue()

    while playing:
        choose_food()
        points += get_food_points()
        food_quality()
        if playing:
            print_full_o_meter()
            if points < FULL:
                print(f"{check_if_full(points)} full points still needed!")
            pound_to_continue()
        if points >= FULL:
            playing = False

    if points >= FULL:
        print("Alright, you're totally full! We can head back to the dorms now!")
        pound_to_continue()

        print("Onward!!!")
        print(f"{FOOTPRINT*5}")
    goodbye()


if __name__ == "__main__":
    main()