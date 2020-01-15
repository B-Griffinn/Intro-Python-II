### will contain the definition of the Room class
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    '''The room should have name and description attributes'''
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        # Add the ability to add items to rooms.
        self.back_pack = [] # holds my items

# Class Check
r1 = Room('Foyer', 'Small but cozy')
print(f'The {r1.name} is {r1.description}')
