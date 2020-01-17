### will contain the definition of the Player class
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # Init player with name
    def __init__(self, player_name, current_room):
        # add player name attr
        self.player_name = player_name 

        # Player also has attr current_room
        self.current_room = current_room

         # allow the player to carry multiple items
        self.player_items = []
        
        # Player should be able to move
    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")
        
    # def item_in_room(self, room):
    #     item_curr_room = self.current_room.get_room_in_direction(room)
    #     if item_curr_room is not None:
    #         self.player_items.append(item_curr_room)