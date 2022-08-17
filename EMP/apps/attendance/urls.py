from django.urls import path
from django.urls import re_path as url
from .views import *


urlpatterns = [
    url(r'^employees/attendance/$', attendance_report, name='employee_attendance'),
    # path('employees/attendance/new/', attendance, name='new_attendance'),
    path('employees/attendance/<int:attendance_id>/', attendance, name='edit_attendance')
]
