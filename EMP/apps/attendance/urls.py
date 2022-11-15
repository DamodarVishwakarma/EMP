from django.urls import path
from django.urls import re_path as url
from .views import *


urlpatterns = [
    url(r'^employees/attendance/$', EmployeeAttendanceListView.as_view(), name='employee_attendance'),
    path('employees/attendance/new/', attendance_create, name='new_attendance'),
    path('employees/attendance/<int:pk>/', attendance_update, name='edit_attendance')
]
