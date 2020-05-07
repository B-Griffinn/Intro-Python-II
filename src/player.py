# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:

    '''Holds player info, current_room, player name.'''
    def __init__(self, player_name, current_room, back_pack=None):
        self.current_room = current_room
        self.player_name = player_name
        self.back_pack = []


    # TAKE ITEM METHOD #
    def get_item(self, item, room):
        # TAKE ITEM FROM ROOM # 
        item_taken_by_player = input(f"You may take the {item} by entering `take *item name*` (below) or press `enter` to continue without taking.").lower()

        # SPLIT THE INPUT IN ORDER TO CHECK IF THE USER DROPPED CORRECTLY ##
        split_take_item = item_taken_by_player.split(' ')

        # PRINT STATEMENTS TO CHECK INPUT
        # print('split_take_item[0]', split_take_item[0])
        # print('split_take_item[1]', split_take_item[1])
        # print('current_room', self.current_room)
        
        if split_take_item[0] == 'take' and split_take_item[1] in room.items:
            self.back_pack.append(split_take_item[1])
        else:
            print(f"\nYou chose not to take the item.\n")

        if len(self.back_pack) >= 1:
            print( f"\nYou are carrying {self.back_pack} in your backpack.\n")

    # DROP ITEM METHOD #
    def remove_item(self):
        # REMOVE ITEM FROM PLAYERS BACK PACK # 
        item_dropped_by_player = input('''
        You may remove an item by entering `drop *item name*` (below) or press `enter` to continue without dropping. 
        ''').lower()
        # SPLIT THE INPUT IN ORDER TO CHECK IF THE USER DROPPED CORRECTLY ##
        split_drop_item = item_dropped_by_player.split(' ')
        
        if split_drop_item[0] == 'drop' and split_drop_item[1] in self.back_pack:
            self.back_pack.remove(split_drop_item[1])
            print(f"You dropped the {split_drop_item[1]}")
    
    # CHANGE ROOMS #
    def change_rooms(self, room, direction):
        if getattr(room, f"{direction}_to") != None:
            new_room = getattr(room, f"{direction}_to")
            self.current_room = new_room
        else:
            print(f"\nYou cannot go {direction}.")
    
    # PRINT STR FORMAT #
    def __str__(self):
        return f"{self.player_name} is currently {self.current_room}"

# p1 = Player("Player1", "Main Lobby")
# print(p1.change_rooms("Player1", "n"))
