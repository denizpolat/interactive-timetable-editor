import people
import rooms
import section

event_id = 0

def does_have_time_conflict(event1, event2):
    duration1 = event1.length
    start1 = event1.time_slot
    duration2 = event2.length
    start2 = event2.time_slot
    end1 = duration1+start1
    end2 = duration2+start2
    if start1 >= end2 or start2 >= end1:
        return -1
    elif start1 > start2:
        return start1
    else:
        return start2

class Event():
    section = 0
    length = 0
    description = ""
    id = 0
    time_slot = -1
    room_id = -1
    course_id = -1
    day = ""

    def __init__(self, section, length, description, day, course_id):
        global event_id
        self.section = section
        self.length = length
        self.description = description
        self.day = day
        self.id = event_id
        self.course_id = course_id
        event_id += 1

    def schedule(self, time_slot, room):
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

    def addEvents(self, eventlist):
        event_ids = [evt for evt in self.event_list]
        for event in eventlist:
            if event.id not in event_ids:
                self.event_list.append(event)

    def removeEvents(self, eventlist):
        eventlist_ids = [evt.id for evt in eventlist]
        self.event_list = [Event(evt.section, evt.length, evt.description) for evt in self.event_list if evt.id not in eventlist_ids]

    def getRoomConflictingEvents(self):
        majorConf = []
        for event in self.event_list:
            for event2 in self.event_list:
                if event.id != event2.id and event.room_id == event2.room_id and event.day == event2.day and does_have_time_conflict(event, event2) != -1:
                    if event not in majorConf:
                        majorConf.append(event)
                    elif event2 not in majorConf:
                        majorConf.append(event2)
        return majorConf

    def getRoomConflicts(self):
        roomConf = []
        roomids = []
        confevents = []
        events = self.getRoomConflictingEvents()
        for event in events:
            currRoomId = 0
            timeslot = 0
            confevents.clear()
            if event.room_id not in roomids:
                roomids.append(event.room_id)
                currRoomId = event.room_id
                timeslot = event.time_slot
            for event2 in events:
                if event.id == event2.room_id or event.room_id != event2.room_id or event.day != event2.day or does_have_time_conflict(event, event2) != -1:
                    continue
                confevents.append(event2)
            roomConf.append((currRoomId, timeslot, confevents))
        return roomConf

    def getInstConflicts(self):
        eventct = len(self.event_list)
        result = []
        for event1 in self.event_list:
            for event2 in self.event_list:
                conf_timeslot = does_have_time_conflict(event1, event2)
                if conf_timeslot != -1:
                    inst1 = -1
                    inst2 = -1
                    for sect in section.sections:
                        if inst1 != -1 and inst2 != -1:
                            break
                        if sect.curr_section == event1.section and sect.course_id == event1.course_id:
                            inst1 = sect.instructor_id
                            continue
                        if sect.curr_section == event2.section and sect.course_id == event2.course_id:
                            inst2 = sect.instructor_id
                            continue
                    if inst1 == inst2:
                        result.append((people.getInstructorName(inst1), conf_timeslot, [event1, event2]))
        return result

    def getConflicts(self):
        roomConf = self.getRoomConflicts()
        instConf = self.getInstConflicts()
        return roomConf + instConf


    def assign(self, timeslot, event):
        event.time_slot = timeslot
        self.event_list.append(event)

    def getEventsAt(self, timeslot):
        events = []
        for event in self.event_list:
            if event.time_slot >= timeslot + 0.001 or event.time_slot <= timeslot:
                events.append(event)
        return events

    def updateView(self):
        return
