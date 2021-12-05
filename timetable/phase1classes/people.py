class Person():
    def __init__(self, id, name, courses_taken):
        self.id = id
        self.name = name
        self.courses_taken = courses_taken
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('name', max_length=256)

    class Meta:
        abstract = True


class Instructor(Person):
    courses_given = models.ManyToManyField(Course, related_name='courses_given', blank=True)

    def __str__(self):
        return str(self.name)


class Student(Person):
    courses_taken = models.ManyToManyField(Course, related_name='courses_taken', blank=True)

    def __str__(self):
        return str(self.name)
