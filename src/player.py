# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room

    # function that helps us change rooms
    def change_room(self, room, direction):
        if getattr(room, f"{direction}_to") != None:
            new_room = getattr(room, f"{direction}_to")
            self.current_room = new_room
        else:
            print("You can not move that way.")

    def __str__(self):
        return f"I am {self.player_name} and I am currently in the {self.current_room}."


# test_p = Player("Ben", "Backyard")
# print(test_p.player_name, test_p.current_room)
