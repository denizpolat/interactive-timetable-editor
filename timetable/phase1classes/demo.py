import cmd, sys, os
from people import *
from rooms import *
from section import *
from timetable import *

"""Variables to hold all creates instances"""
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
                room.updateDescription(update_arg[2])

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
            print('Room id:', room.id, '- Room capacity:',room.capacity,'- Room desc:', room.description)

    def do_showRoomLists(self, arg):
        'Show a list of Roomlists and the RoomIds they contain (no argument)'
        global roomlist
        for roomls in roomlist:
            print('Roomlist id:', roomls.id, '- Contained Rooms:', end=' ')
            for rooms in roomls.rooms:
                print(rooms, end=' ')
            print()

    def do_createSection(self, arg):
        'Create a section with arguments: CourseId(int) CurrentSection(int) TotalSections(int) Description(string) InstructorId(int)'
        global sections
        sections_args = arg.split()
        new_section = Section(int(sections_args[0]), int(sections_args[1]), int(sections_args[2]), sections_args[3], int(sections_args[4]))
        sections.append(new_section)

    def do_showSections(self, arg):
        'Show a list of sections with their courseId section description instructorId and studentIds in that section (no arguments)'
        global sections
        for section in sections:
            print('CourseId:',section.course_id,'- Section:',section.curr_section,'- Description',section.desc,'- InstructorId:',section.instructor_id,'- Students: ',end=' ')
            for students in section.student_list:
                print(students,end=" ")
            print()

    def do_createCourse(self, arg):
        'Create a course with arguments: CourseCode(int) CourseName(string)'
        global courses
        courses_arg = arg.split()
        new_course = Course(int(courses_arg[0]), courses_arg[1])
        course_codes = [crs.course_code for crs in courses]
        if int(courses_arg[0]) in course_codes:
            print('Can\'t add course with this course code.')
        else:
            courses.append(new_course)

    def do_showCourses(self, arg):
        'Show a list of courses with their codes and names (no argument)'
        global courses
        for course in courses:
            print('Course Code:',course.course_code,'- Course Name:', course.course_name)

    def do_createStudent(self, arg):
        'Create a student with arguments: StudentId(int) StudentName(string) CourseId1(int) CourseId2(int)...'
        global std_ids
        student_args = arg.split()
        if int(student_args[0]) in std_ids:
            print("You cannot add a student with this id.")
        else:
            global students
            std_ids.append(int(student_args[0]))
            courses = []
            for courseId in student_args[2:]:
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
        section_args = arg.split()
        section_list = [(sct.course_id, sct.curr_section) for sct in sections]
        if((int(section_args[0]),int(section_args[1])) not in section_list):
            print('No such section exists.')
        else:
            stlist = []
            for studentId in section_args[2:]:
                stlist.append(int(studentId))
            for section in sections:
                if section.course_id == int(section_args[0]) and section.curr_section == int(section_args[1]):
                    section.addStudent(stlist)

    def do_removeStudent(self, arg):
        'Remove students to a section with arguments: CourseId(int) Section(int) StudentId1(int) StudentId2(int)...'
        global sections
        section_args = arg.split()
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
            if event.id == int(event_args[0]):
                event.schedule(float(event_args[1]), int(event_args[2]))

    def do_showEvents(self, arg):
        'Show events with their sectionId length description dayname courseId'
        global events
        for event in events:
            print('Section:',event.section,'- Length(Hrs):',event.length,'- Description:',event.description,'- Day Name',event.day,'- Course Id',event.course_id)

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

    def do_showTimeTable(self, arg):
        'Show the TimeTable with all its elements (no argument)'
        global timetables
        if len(timetables) > 0:
            print('Days: ',end='')
            for day in timetables[0].days:
                print(day,end=' ')
            print()
            print('Slots per day: ', timetables[0].slots_per_day)
            print('Rooms: ', end='')
            for room in timetables[0].rooms:
                print(room,end=' ')
            print()
            print('Events:')
            for event in timetables[0].event_list:
                print('Section:',event.section,'- Length(Hrs):',event.length,'- Description:',event.description,'- Day Name',event.day,'- Course Id',event.course_id)

    def do_getConflicts(self, arg):
        'Get conflicts of a timetable: (no arguments)'
        if len(timetables) > 0:
            print(timetables[0].getConflicts())

    def do_addEvents(self, arg):
        'Add events to timetable with arguments: EventId1(int) EventId2(int)...'
        global timetables
        args = map(int,arg.split())
        if len(timetables) > 0:
            events_to_add = []
            for event in events:
                if event.id in args:
                    events_to_add.append(event)
            timetables[0].addEvents(events_to_add)

    def do_removeEvents(self, arg):
        'Remove events from timetable with arguments: EventId1(int) EventId2(int)...'
        global timetables
        args = map(int,arg.split())
        if len(timetables) > 0:
            events_to_remove = []
            for event in events:
                if event.id in args:
                    events_to_remove.append(event)
            timetables[0].removeEvents(events_to_add)

    def do_assign(self, arg):
        'Assign the given timeslot to the event with arguments: TimeSlot(float) EventId(int)'
        global timetables
        global events
        args = arg.split()
        for event in events:
            if event.id == int(args[1]):
                if len(timetables) > 0:
                    timetables[0].assign(float(args[0]), event)

    def do_getEventsAt(self, arg):
        'Get events at timeslot with arguments: TimeSlot(float)'
        arg = float(arg)
        global timetables
        if len(timetables) > 0:
            timetables[0].getEventsAt(arg)

if __name__ == '__main__':
    # c1 = Course(242, "pl")
    # c2 = Course(140, "c")
    # c3 = Course(351, "file")
    # c4 = Course(445, "script")
    # c5 = Course(444, "compiler")
    # c6 = Course(232, "data")
    # s1 = Student(223770, "Deniz Polat", [c1, c2,c4,c5])
    # s2 = Student(223770, "Deniz Caglarca", [c1, c3,c6])
    # s3 = Student(223770, "Husna Yilmaz", [c2,c3,c5, c6])
    # s4 = Student(223770, "Elif Karakoyun", [c1, c2,c4,c5,c6])
    # s5 = Student(223770, "Erinc Deg", [c1, c6])
    # i1 = Instructor(1, "Onur Tolga Seh", [c1, c4])
    # i2 = Instructor(2, "Nihan Cicekli", [c3, c6])
    # i3 = Instructor(3, "Pelin Angin", [c2, c5])
    # r1 = Room(100, "bmb1")
    # r2 = Room(100, "bmb2")
    # sec1 = Section(242, 1,3,"",1)
    # sec2 = Section(242, 2,3,"",1)
    # sec3 = Section(242, 3,3,"",1)
    # sec4 = Section(444, 1,1,"",3)
    # sec5 = Section(140, 1,1,"",3)
    # sec6 = Section(351, 1,1,"",2)
    # sec7 = Section(445, 1,1,"",1)
    # sec8 = Section(232, 1,2,"",2)
    # sec9 = Section(232, 2,2,"",2)
    # ev1 = Event(sec1, 5,"","Monday",242)
    # ev2 = Event(sec2, 5,"","Tuesday",242)
    # ev3 = Event(sec3, 5,"","Wednesday",242)
    # ev4 = Event(sec4, 6,"","Monday",242)
    # ev5 = Event(sec5, 2,"","Monday",242)
    # ev6 = Event(sec6, 1,"","Monday",242)
    # ev7 = Event(sec7, 8,"","Monday",242)
    # ev8 = Event(sec8, 4,"","Monday",242)
    # ev9 = Event(sec9, 4,"","Monday",242)
    # ttbl = Timetable(["Monday","Tuesday","Wednesday"], 10, [r1,r2], 40)



    TimeTableDemo().cmdloop()
