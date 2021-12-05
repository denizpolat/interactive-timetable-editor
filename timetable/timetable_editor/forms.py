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
