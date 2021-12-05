# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.views.generic import View
from forms import *
from django.contrib import messages
from django.shortcuts import render, redirect

from models import *

# Create your views here.

# class IndexView(View):
#     def get(self, request):
#         if request.is_ajax():
#             value = int(request.GET['value'])
#             staffs = Staff.objects.all()
#             if value == 1:  # for first statistic
#                 user_data_dict = {}
#                 names_user = []
#                 for staff in staffs:
#                     staff_team_ids = staff.team.all().values_list('id', flat=True)
#                     num_projects = Project.objects.filter(team_id__in=list(staff_team_ids)).count()
#                     num_deploys = DeploymentNote.objects.filter(sender_id=staff.staff_id).count()
#                     if num_projects != 0 or num_deploys != 0:
#                         user_data_dict[staff.staff_id] = [num_projects, num_deploys]
#
#                 cluster_centers, groups = k_means_clustering.find_clusters(4, user_data_dict)
#                 data_points = [[] for i in range(len(groups))]
#                 for i in range(len(groups)):
#                     elements = groups[i]
#                     for e in elements:
#                         staff_name = Staff.objects.get(staff_id=e).staff.first_name
#                         names_user.append(staff_name)
#                         data_points[i].append([user_data_dict[e][0], user_data_dict[e][1]])
#                 data = {
#                     "datapoints": data_points,
#                     "names_user": names_user,
#                 }
#
#                 return JsonResponse(data)
#
#             elif value == 2:  # for second statistic
#                 user_data_dict = {}
#                 names_user = []
#                 for staff in staffs:
#                     staff_team_ids = staff.team.all().values_list('id', flat=True)
#                     num_teams = Team.objects.filter(id__in=list(staff_team_ids)).count()
#                     num_projects = Project.objects.filter(team_id__in=list(staff_team_ids)).count()
#                     if num_teams != 0 or num_projects != 0:
#                         user_data_dict[staff.staff_id] = [num_teams, num_projects]
#
#                 cluster_centers, groups = k_means_clustering.find_clusters(4, user_data_dict)
#                 data_points = [[] for i in range(len(groups))]
#                 for i in range(len(groups)):
#                     elements = groups[i]
#                     for e in elements:
#                         staff_name = Staff.objects.get(staff_id=e).staff.first_name
#                         names_user.append(staff_name)
#                         data_points[i].append([user_data_dict[e][0], user_data_dict[e][1]])
#                 data = {
#                     "datapoints": data_points,
#                     "names_user": names_user,
#                 }
#                 return JsonResponse(data)
#
#         return render(request, 'deployment_app/index.html', {})


def removeStudent(idlist):
    students = Student.objects.all()
    deleteStudents = []
    for id_ in idlist:
        deleteStudents.append(students.get(id=id_))
    deleteStudents.delete()

def CourseView(request):
    course = forms.CourseForm()
    courses = Course.objects.all()
    context = {'course': course, 'courses': courses}
    if request.method == 'POST':
        course = forms.CourseForm(request.POST)
        if course.is_valid():
            messages.success(request, 'Class has been added.')
            course.save()
            return redirect('/add-classcourse')    # add
        else:
            messages.error(request, 'Do not enter the same class ID')
    return render(request, 'timetableapp/AddClass.html', context)
