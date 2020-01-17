# ITEM CLASS
# Hint: the name should be one word for ease in parsing later.

# This will be the base class for specialized item types to be declared later.
class Item:
    '''The item should have name and description attributes.'''
    def __init__(self, item_name, item_desc):
        # name and desc attrs
        self.item_name = item_name
        self.item_desc = item_desc
    def __str__(self):
        return f'{self.item_name} {self.item_desc}'


    # add items to this room
    def add_item_to_room(self, room, item):
        room_item = self.item_name.append(room, item)
        if room_item is not None:
            self.room_name = room_item
            print(self.room_name)
        else:
            print('This room has no items.')