"""Id variable to make sure all created room and roomlists have a unique id"""
room_id = 0
roomlist_id = 0

class Room():
    id = 0
    capacity = 0
    description = ""

    def __init__(self, capacity, description):
        global room_id
        self.id = room_id
        room_id += 1
        self.capacity = capacity
        self.description = description

    def updateCapacity(self, capacity):
        self.capacity = capacity

    def updateDescription(self, description):
        self.desciption = desciption

class RoomList():
    id = 0
    rooms = []

    def __init__(self):
        global roomlist_id
        self.id = roomlist_id
        roomlist_id += 1

    def addRoom(self, room_id):
        if room_id not in rooms:
            rooms.append(room_id)

    def removeRoom(self, room_id):
        if room_id in rooms:
            rooms.remove(room_id)
