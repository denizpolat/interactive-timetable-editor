event_id = 0

class Event():
    section = 0
    length = 0
    description = ""
    id = 0
    time_slot = -1
    room_id = -1

    def __init__(self, section, length, description):
        self.section = section
        self.length = length
        self.description = description
        self.id = event_id
        event_id += 1

    def schedule(time_slot, room):
        self.time_slot = time_slot
        self.room_id = room

class TimeTable():
    days = []
    slots_per_day = ()
    slot_offset = 40
    rooms = []
    event_list = []

    def __init__(self, days, slots_per_day, rooms, slot_offset=40):
        for day in days:
            self.days.append(day)
        self.slots_per_day = (slots_per_day[0],slots_per_day[1])
        for room in rooms:
            self.rooms.append(room)
        self.slot_offset = slot_offset

    def addEvents(eventlist):
        event_ids = [evt.id for evt in self.event_list]
        for event in eventlist:
            if event.id not in event_ids:
                self.event_list.append(event)

    def removeEvents(eventlist):
        eventlist_ids = [evt.id for evt in eventlist]
        self.event_list = [Event(evt.section, evt.length, evt.description) for evt in self.event_list if evt.id not in eventlist_ids]

    def getConflicts():
        return

    def assign(timeslot, event):
        return

    def getEventsAt(timeslot):
        return

    def updateView():
        return 
