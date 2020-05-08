from room import Room
from player import Player
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """
            Dim light filters in from the south. Dusty
            passages run north and east.
    """),

    'overlook': Room("Grand Overlook", """
            A steep cliff appears before you, falling
            into the darkness. Ahead to the north, a light flickers in
            the distance, but there is no way across the chasm.
    """),

    'narrow':   Room("Narrow Passage", """
            The narrow passage bends here from west
            to north. The smell of gold permeates the air.
    """),

    'treasure': Room("Treasure Chamber", """
            You've found the long-lost treasure
            chamber! Sadly, it has already been completely emptied by
            earlier adventurers. The only exit is to the south but risk your luck checking north.
    """),
    'adventure': Room("Adventure Room", """
            You've found the Adventure Room!
            It looks like you can only move south.
    """),
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
room['treasure'].n_to = room['adventure']
room['adventure'].s_to = room['narrow']

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player1 = Player("Ben", room['outside'])
# print(player1)

## Cardinal Directions allowed
card_directions = ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']

# Add items to the game that the user can carry around
game_items = ['candle', 'key', 'shovel']

x = True
while x:

    user_input = input("Please enter a cardinal direction or 'q' to quit. You may also enter `bp` in order to view your backpack whenever you see this message ~~> ").lower()

    print(f"\nYou chose to move {user_input}\n")
    
    ### A PLAYER CHANGES ROOMS ###
    if user_input in card_directions:
        # CHANGE ROOMS 
        player1.change_rooms(player1.current_room, user_input)

        # ADD RANDOM ITEM TO ROOM
        player1.current_room.add_item_to_room(random.choice(game_items))

        # ADD ITEM TO PLAYERS BACK PACK
        # print('player1.current_room.items', player1.current_room.items)
        player1.get_item(player1.current_room.items[0], player1.current_room)

        print(f'''
            {player1}
        ''')
        ## IF USER_INPUT IS `BP` OPEN/SHOW THEIR BP AND LET THEM REMOVE ##
    elif user_input == 'bp':
        print('Here is what you are carrying in your backpack: ', player1.back_pack)
        # # REMOVE ITEM FROM PLAYERS BACK PACK # 
        player1.remove_item()

    # TODO
    ## ONLY DISPLAY RGN CHEST IN SELECT ROOMS ##
    # print(f'''
    # You stumbled upon a chest. Here is what you may choose from that chest: {game_items}.
    # ''')
    # item_choice = input("Enter `take *item name*` to pick up a random item or `no` to move on without an item. ")

    # split the users input in order to take item
    # split_item_choice = item_choice.split(' ')
    # print('split item [1]', split_item_choice[1])

    # CHECK IF THE ITEM THE USER CHOSE IS IN THE GAME ITEMS LIST #
    # if split_item_choice[0] == 'take' and split_item_choice[1] in game_items:
    #     player1.get_item(split_item_choice[1])

    ## ## ## ## ## ## END OF TAKE ITEM ## ## ## ## ## ## ## ## ##

    # TODO 
    ## WILL NEED FOR BACKBACK CONDITIONAL ##
        # if item_choice == 'no':
        #     print('''
        #     Sorry the collection is limited.\n
        #     ''')
        # if user_input == 'q':
        #     print('''
        #     Thank you for playing. Come back soon!\n
        #     ''')
        #     break

    if user_input == 'q':
        print("\nThank you for playing. Come back soon!\n")
        break
        # print(player1.current_room)


    # # **** NAIVE APPROACH **** ##
    # if user_input == 'n' or user_input == 'north':
    #     player1.current_room = player1.current_room.n_to
    # elif user_input == 's' or user_input == 'south':
    #     player1.current_room = player1.current_room.s_to
    # elif user_input == 'e' or user_input == 'east':
    #     player1.current_room = player1.current_room.e_to
    # elif user_input == 'w' or user_input == 'west':
    #     player1.current_room = player1.current_room.w_to
    # elif user_input == 'q' or user_input == 'quit':
    #     print("\nThank you for playing. Have a great day!\n")
    #     break
    # else:
    #     print("Please enter a cardinal direction such as `n`, `s`, `e`, `w` or even the full direction name such as `North`.")

        
    ## UPDATE DIRCTIONS GIVEN TO A FULL WORD ##
        ## Function to convert dirctions into full words: n == North ##
    # def convert_directions(direction):
    #     new_direction = ''
    #     if direction == 'n':
    #         new_direction += 'North'
    #         # return direction
    #     elif direction == 's':
    #         new_direction += 'South'
    #         # return direction
    #     elif direction == 'e':
    #         new_direction += 'East'
    #         # return direction
    #     elif direction == 'w':
    #         new_direction += 'West'
    #         # return direction
    #     return new_direction

    # convert_directions(user_input)
   