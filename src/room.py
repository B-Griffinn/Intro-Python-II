# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_desc):
        self.room_name = room_name
        self.room_desc = room_desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"you are currently {self.room_name}. {self.room_desc}."


# test_room = Room('Hooby Lobby', 'Empty')
# print(test_room.room_name, test_room.room_desc)
