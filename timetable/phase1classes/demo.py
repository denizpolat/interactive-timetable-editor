import cmd, sys, os
from people import *
from rooms import *
from section import *
from timetable import *

rooms = []
roomlist = []
sections = []
events = []
timetables = []

"""Class to test all methods of each class and show all created classes"""
class TimeTableDemo(cmd.Cmd):
    intro = 'Welcome to TimeTable Demo.   Type help or ? to list commands.\n'
    prompt = '(TimeTable) '

    def do_createRoom(self, arg):
        'Create a room with arguments: Capacity(int) Description(string)'
        global rooms
        room_arg = arg.split()
        new_room = Room(int(room_arg[0]), room_arg[1])
        rooms.append(new_room)

    def do_updateRoom(self, arg):
        'Update a room\'s capacity,description with arguments: RoomId(int) Capacity(int) Description(string)'
        global rooms
        update_arg = arg.split()
        for room in rooms:
            if room.id == int(update_arg[0]):
                room.updateCapacity(int(update_arg[1]))
                room.updateDescription(int(update_arg[2]))

    def do_createRoomList(self, arg):
        'Create a roomlist (no argument)'
        global roomlist
        new_roomlist = RoomList()
        roomlist.append(new_roomlist)
        print("Created RoomList with id",new_roomlist.id)

    def do_addRoom(self, arg):
        'Add a room to a roomlist with arguments: RoomListId(int) RoomId(int)'
        global roomlist
        roomlist_args = arg.split()
        for roomlists in roomlist:
            if roomlists.id == int(roomlist_args[0]):
                roomlists.addRoom(int(roomlist_args[1]))

    def do_removeRoom(self, arg):
        'Remove a room from a roomlist with arguments: RoomListId(int) RoomId(int)'
        global roomlist
        roomlist_args = arg.split()
        for roomlists in roomlist:
            if roomlists.id == int(roomlist_args[0]):
                roomlists.removeRoom(int(roomlist_args[1]))

    def do_showRooms(self, arg):
        'Show a list of Rooms and their ids, capacities and descriptions (no argument)'
        global rooms
        for room in rooms:
            print('Room id:', room.id, '- Room capacity:',room.capacity,'- Room desc:', room.desciption)

    def do_showRoomLists(self, arg):
        'Show a list of Roomlists and the RoomIds they contain (no argument)'
        global roomlist
        for roomls in roomlist:
            print('Roomlist id:', roomls.id, '- Contained Rooms: ' end=' ')
            for rooms in roomls.rooms:
                print(room.id, end=' ')
            print()

    def do_createSection(self, arg):
        'Create a section with arguments: CourseId(int) CurrentSection(int) TotalSections(int) Description(string) InstructorId(int)'
        global sections
        sections_args = arg.split()
        new_section = Section(int(arg[0]), int(arg[1]), int(arg[2]), arg[3], int(arg[4]))
        sections.append(new_section)

    def do_createCourse(self, arg):
        'Create a course with arguments: CourseCode(int) CourseName(string)'
        global courses
        courses_arg = arg.split()
        course_codes = [crs.course_code for crs in courses]
        if int(courses_arg[0]) in course_codes:
            print('Can\'t add course with this course code.')
        else:
            new_course = Course(int(courses_arg[0]), courses_arg[1])
            courses.append = new_course

    def do_createStudent(self, arg):
        'Create a student with arguments: StudentId(int) StudentName(string) CourseId1(int) CourseId2(int)...'
        global std_ids
        global students
        student_args = arg.split()
        if int(student_args[0]) in std_ids:
            print("You cannot add a student with this id.")
        else:
            std_ids.append(int(student_args[0]))
            courses = []
            for courseId in students_args[2:]:
                courses.append(int(courseId))
            student = Student(int(student_args[0]), student_args[0], courses)
            students.append(student)

    def do_createInstructor(self, arg):
        'Create an instructor with argments: InstructorId(int) InstructorName(string) CourseId1(int) CourseId2(int)...'
        global inst_ids
        global instructors
        instructor_args = arg.split()
        if int(instructor_args[0]) in inst_ids:
            print("You cannot add an instructor with this id.")
        else:
            inst_ids.append(int(instructor_args[0]))
            courses = []
            for courseId in instructor_args[2:]:
                courses.append(int(courseId))
            instructor = Instructor(int(instructor_args[0]), instructor_args[1], courses)
            instructors.append(instructor)

    def do_addStudent(self, arg):
        'Add students to a section with arguments: CourseId(int) Section(int) StudentId1(int) StudentId2(int)...'
        global sections
        sections_args = arg.split()
        section_list = [(sct.course_id, sct.curr_section) for sct in sections]
        if((int(section_args[0]),int(section_args[1])) not in section_list):
            print('No such section exists.')
        else:
            stlist = []
            for studentId in instructor_args[2:]:
                stlist.append(int(studentId))
            for section in sections:
                if section.course_id == int(section_args[0]) and section.curr_section == int(section_args[1]):
                    section.addStudent(stlist)

    def do_removeStudent(self, arg):
        'Remove students to a section with arguments: CourseId(int) Section(int) StudentId1(int) StudentId2(int)...'
        global sections
        sections_args = arg.split()
        section_list = [(sct.course_id, sct.curr_section) for sct in sections]
        if((int(section_args[0]),int(section_args[1])) not in section_list):
            print('No such section exists.')
        else:
            stlist = []
            for studentId in instructor_args[2:]:
                stlist.append(int(studentId))
            for section in sections:
                if section.course_id == int(section_args[0]) and section.curr_section == int(section_args[1]):
                    section.removeStudent(stlist)

    def do_createEvent(self, arg):
        'Create an event with arguments: SectionId(int) Length(int) Description(string) DayName(string) CourseId(int)'
        global events
        event_args = arg.split()
        new_event = Event(int(event_args[0]), int(event_args[1]), event_args[2], event_args[3], int(event_args[4]))
        events.append(new_event)

    def do_scheduleEvent(self, arg):
        'Schedule an event with arguments: EventId(int) TimeSlot(float) RoomId(int)'
        global events
        event_args = arg.split()
        for event in events:
            if event.event_id == int(event_args[0]):
                event.schedule(float(event_args[1]), int(event_args[2]))

    def do_createTimeTable(self, arg):
        'Create a timetable with arguments: Day1(string) Day2(string) ... StartingDaySlot(float) EndingDaySlot(float) RoomId1(int) RoomId2(int) ...'
        global timetables
        timetable_args = arg.split()
        days = []
        for arg in timetable_args[0:5]:
            days.append(arg)
        rooms = []
        for arg in timetable_args[7:]:
            rooms.append(int(arg))
        new_timetable = TimeTable(days,(float(timetable_args[5]),float(timetable_args[6])),rooms)
        timetables.append(new_timetable)

    def do_getConflicts(self, arg):
        'Get conflicts of a timetable: (no arguments)'
        if len(timetables) > 0:
            timetables[0].getConflicts()

    def do_addEvents(self, arg):
        'Add events to timetable with arguments: EventId1(int) EventId2(int)...'
        global timetables
        args = map(int,arg.split())
        if len(timetables) > 0:
            timetable[0].addEvents([event for event in args])

    def do_removeEvents(self, arg):
        'Remove events from timetable with arguments: EventId1(int) EventId2(int)...'
        global timetables
        args = map(int,arg.split())
        if len(timetables) > 0:
            timetable[0].removeEvents([event for event in args])

    def do_assign(self, arg):
        'Assign the given timeslot to the event with arguments: TimeSlot(float) EventId(int)'
        global timetables
        global events
        args = arg.split()
        for event in events:
            if event.event_id == int(args[1]):
                if len(timetables) > 0:
                    timetable[0].assign(float(args[0]), event)

    def do_getEventsAt(self, arg):
        'Get events at timeslot with arguments: TimeSlot(float)'
        arg = float(arg)
        global timetables
        if len(timetables) > 0:
            timetable[0].getEventsAt(arg)

    def do_bye(self, arg):
        'Exit'
        print('Thank you for using TimeTable App')
        bye()
        return True

if __name__ == '__main__':

    TimeTableDemo().cmdloop()
