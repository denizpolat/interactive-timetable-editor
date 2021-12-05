global sections
sections = []

class Section():
    course_id = 0
    curr_section = 0
    tot_section = 0
    desc = ""
    instructor_id = 0
    student_list = []

    def __init__(self, course_id, curr_section, tot_section, desc, instructor_id):
        self.course_id = course_id
        self.curr_section = curr_section
        self.tot_section = tot_section
        self.desc = desc
        self.instructor_id = instructor_id
        sections.append(self)

    def addStudent(self, stlist):
        for student in stlist:
            if student not in self.student_list:
                self.student_list.append(student)

    def removeStudent(self, stlist):
        for student in stlist:
            if student in self.student_list:
                self.student_list.remove(student)
