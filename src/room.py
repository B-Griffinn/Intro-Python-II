# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    '''Room name, room desctiption'''
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        # Make rooms able to hold multiple items
        self.items = []
    
    def add_item_to_room(self, item):
        self.items.append(item)
        print(f"You found a {self.items[0]}.")

    def __str__(self):
        return f"{self.room_name} {self.room_description}"

# r1 = Room("Laundry", "Lots of laundry to fold")
# print(r1.change_rooms("n"))
# print(r1.change_directions("n"))
# print(r1.moved_north("n"))