# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from timetable_editor import models, views
admin.site.register(models.Course)
admin.site.register(models.Student)
admin.site.register(models.Section)
admin.site.register(models.Instructor)
admin.site.register(models.Room)
admin.site.register(models.RoomList)
