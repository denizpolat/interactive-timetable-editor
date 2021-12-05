# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    course_code = models.IntegerField('course_code', unique=True)
    course_name = models.CharField('course_name', max_length=128)

    def __str__(self):
        return str(str(self.course_code) + ' - ' + str(self.course_name))


class Person(models.Model):
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


class Room(models.Model):
    id = models.BigAutoField(primary_key=True)
    capacity = models.IntegerField('room_capacity', default=0)
    description = models.CharField('description', max_length=2048)

    def __str__(self):
        return str('room id : ' + str(self.id))


class RoomList(models.Model):
    rooms = models.ManyToManyField(Room, related_name='room_ids', blank=False)


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    current_section = models.IntegerField('curr_section')
    total_section = models.IntegerField('curr_section')
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.course) + ' - ' + str(self.current_section))
