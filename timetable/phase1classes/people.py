global instructors, students
std_ids = []
students = []
instructors = []
courses = []
inst_ids = []


class Course:
    course_code = 0
    course_name = ""
    def __init__(self, cc, cn):
        self.course_code = cc
        self.course_name = cn
        courses.append(self)

class Student:
    id = 0
    name = ""
    courses_taken = []
    def __init__(self, id, name, courses_taken):
        self.id = id
        self.name = name
        self.courses_taken = courses_taken


class Instructor:
    id = 0
    name = ""
    courses_given = []
    def __init__(self, id, name, courses_given):
        self.id = id
        self.name = name
        self.courses_given = courses_given


def addStudent(id, name, ct):
    if id in std_ids:
        print("You cannot add a std with this id")
    else:
        std_ids.append(id)
        s = Student(id, name, ct)
        students.append(s)


def addInstructor(id, name, cg):
    if id in std_ids:
        print("You cannot add an instr with this id")
    else:
        inst_ids.append(id)
        s = Instructor(id, name, cg)
        instructors.append(s)


def getStudents():
    return students


def getInstructors():
    return instructors

def getCourses():
    return courses


def removeStudent(id):
    for std in students:
        if std.id == id:
            students.remove(std)


def removeStudents(ids):
    for id in ids:
        removeStudent(id)
