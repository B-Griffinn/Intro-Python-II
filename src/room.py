### will contain the definition of the Room class
# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_desc):
        # Name Description  
        self.room_name = room_name
        self.room_desc = room_desc
        # # n_to, s_to, e_to, w_to => which default to none so they do not need to be passed into the __init__
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        # Make rooms able to hold multiple items
        self.room_items = []

    def __str__(self):
        display_string = ""
        display_string += f'\n-------\n'
        display_string += f"\n{self.room_name}\n"
        display_string += f"\n{self.room_desc}\n"
        display_string += f"\n{self.get_exits_string()}\n"
        return display_string

       
    def get_room_in_direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None

    def get_item_in_room(self, room, item):
        if room == 'outside':
            return self.room_items.append(item)
        elif room == 'foyer':
            return self.room_items.append(item)
        elif room == 'overlook':
            return self.room_items.append(item)
        elif room == 'narrow':
            return self.room_items.append(item)
        elif room == 'treasure':
            return self.room_items.append(item)
        else:
            return None

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append('n')
        if self.s_to:
            exits.append('s')
        if self.e_to:
            exits.append('e')
        if self.w_to:
            exits.append('w')
        return exits
            

    # give us valid directions        
    def get_exits_string(self):
        return f"\n You may only exit: {','.join(self.get_exits())}"

    # add items to this room
    def add_item_to_room(self, room, item):
        room_item = self.room_items.append(room, item)
        if room_item is not None:
            self.room_name = room_item
            print(self.room_name)
        else:
            print('This room has no items.')