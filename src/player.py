### will contain the definition of the Player class
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    '''Players should have a name and current_room attributes'''
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

# Player Check
p1 = Player('Ben', 'Foyer')
print(f'Player one is {p1.name} and he is currently in the {p1.current_room}')