from item import Item
from lightsource import LightSource
from monster import Monster
from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons a sign is right in front of you."
        'It says "do not pick the flowers".',
        True
    ),

    'foyer':    Room(
        "Foyer",
        "Dim light filters in from the south. Dusty passages run north and "
        "east.",
        True
    ),

    'overlook': Room(
        "Grand Overlook",
        "A steep cliff appears before you, falling into the darkness. Ahead "
        "to the north, a light flickers in the distance, but there is no way "
        "across the chasm.",
        True
    ),

    'narrow':   Room(
        "Narrow Passage",
        "The narrow passage bends here from west to north. The smell of gold "
        "permeates the air.",
        False
    ),

    'treasure': Room(
        "Treasure Chamber",
        "You found the long-lost treasure chamber!",
        False
    ),
}


# Add items to rooms

room['outside'].add_item(Item("flower", "a lovely flower", False))
room['foyer'].add_item(LightSource("torch", "a burning torch"))
room['treasure'].add_item(
    Item("doubloon", "a doubloon from a treasure chest", True, True)
)


# Add monsters to rooms

room['treasure'].add_monster(Monster("troll", 100, "Red Shirt The Troll"))


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = ""
while name == "":
    name = input("\nEnter your name: ").strip()
p = Player(name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

p.show_location()
while True:
    input_args = input().strip().lower().split(" ")
    input_args_count = len(input_args)
    if input_args_count == 1:
        input_ = input_args[0]
        if input_ == "n":
            p.move_to_room(p.current_room.n_to)
        elif input_ == "e":
            p.move_to_room(p.current_room.e_to)
        elif input_ == "s":
            p.move_to_room(p.current_room.s_to)
        elif input_ == "w":
            p.move_to_room(p.current_room.w_to)
        elif input_ == "i" or input_ == "inventory":
            p.show_inventory()
        elif input_ == "q":
            break
        elif input_ != "":
            print("\nNot a valid command.\n")
    elif input_args_count == 2:
        action, target = input_args
        if action == "get" or action == "take":
            is_win_condition, item_name = p.take_item(target)
            if is_win_condition:
                print(
                    f'Victory! You have found the legendary {item_name}!\n'
                    f'The name "{p.name}" will be remembered forever!'
                )
                break
        elif action == "drop":
            p.drop_item(target)
        elif action == "attack":
            p.attack(target)

        #   ============
        #   || CHEATS ||
        #   ============

        elif action == "helios":
            if not p.set_helios(target):
                print("\nNot a valid command.\n")

        else:
            print("\nNot a valid command.\n")
    else:
        print("\nNot a valid command.\n")
