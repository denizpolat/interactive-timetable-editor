class Room():
    id = 0
    capacity = 0
    description = ""

    def __init__(self, id, capacity, description):
        self.id = id
        self.capacity = capacity
        self.description = description

    def updateId(id):
        self.id = id

    def updateCapacity(capacity):
        self.capacity = capacity

    def updateDescription(description):
        self.desciption = desciption

class RoomList():
    id = 0
    rooms = []

    def __init__(self, id):
        self.id = 0

    def addRoom(room_id):
        if room_id not in rooms:
            rooms.append(room_id)

    def removeRoom(room_id):
        if room_id in rooms:
            rooms.append(room_id)
