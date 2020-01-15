### where the main logic for the game should live

from room import Room
import sys

# 1. Add a REPL parser to adv.py that accepts directional commands to move the player
args = sys.argv

user_input_direction = input('Please enter a directional command: n, s, e, or w ~~~> ')
if user_input_direction == '':
    print('You did not choose a direction!')
else:
    print(f'You chose {user_input_direction}! ')

# print return North if user enters 'n'
if user_input_direction == 'n':
    north = 'North'
    print(f'You chose to go {north}!')

# print return South if user enters 's'
elif user_input_direction == 's':
    south = 'South'
    print(f'You chose to go {south}!')

# print return East if user enters 'e'
elif user_input_direction == 'e':
    east = 'East'
    print(f'You chose to go {east}!')

# print return West if user enters 'w'
elif user_input_direction == 'w':
    west = 'West'
    print(f'You chose to go {west}!')

else:
    print('Please provide a valid direction in the following format: n, s, e, or w. ')



# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


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
