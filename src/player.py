# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    '''Holds player info, current_room, player name.'''
    def __init__(self, player_name, current_room):
        self.current_room = current_room
        self.player_name = player_name

    def __str__(self):
        return f"\n{self.player_name} is currently {self.current_room}"

# p1 = Player("Player1", "Main Lobby")
# print(p1)
