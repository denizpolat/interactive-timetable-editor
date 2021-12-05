from django import forms
from models import *
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class CourseForm(forms.ModelForm):
    course_code = forms.IntegerField(required=True)
    course_name = forms.CharField(required=True)

    class Meta:
        model = Course
        fields = ('course_code', 'course_name')


class RoomForm(forms.ModelForm):
    capacity = forms.IntegerField(required=True)
    description = forms.CharField(required=False)

    class Meta:
        model = Room
        fields = ('capacity', 'description')

class RoomListForm:
    rooms = forms.ManyToManyField(required=True)

    class Meta:
        model = RoomList
        fields = ('rooms')

class SectionForm:
    course = forms.ForeignKey(required=True)
    current_section = forms.IntegerField(required=True)
    total_section = forms.IntegerField(required=True)
    instructor_id = models.ForeignKey(required=True)

    class Meta:
        model = Section
        fields = ('course','current_section','total_section','instructor_id')

class InstructorForm:
    courses_given = forms.ManyToManyField(required=False)

    class Meta:
        model = Instructor
        fields = ('courses_given')


class StudentForm:
    courses_taken = forms.ManyToManyField(required=False)

    class Meta:
        model = Student
        fields = ('courses_taken')

class EventForm:
    course = forms.ForeignKey(required=True)
    section = forms.ForeignKey(required=True)
    length = forms.IntegerField(required=True)
    description = forms.CharField(required=False)

    class Meta:
        model = Event
        fields = ('course','section','length','description')

class TimeTableForm:
    days = forms.ManyToManyField(required=True)
    starting_slot_perday = forms.IntegerField(required=True)
    ending_slot_perday = forms.IntegerField(required=True)
    slot_offset = forms.IntegerField(required=True)
    events = forms.ManyToManyField(required=True)
    rooms = forms.ManyToManyField(required=True)

    class Meta:
        model = TimeTable
        fields = ('days','starting_slot_perday','ending_slot_perday','slot_offset','events','rooms')
