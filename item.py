# ITEM CLASS
# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.

class Item:
    '''The item should have name and description attributes'''
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Item Check
item1 = Item('Cell Phone', 'Means of Communication')
print(f'You are holding a {item1.name} and it is your only {item1.description}')