import datetime
from django.views.generic.dates import MonthArchiveView
from .forms import AttendanceForm
from attendance.models import EmployeeAttendance
from django.views.generic import ListView
from django.shortcuts import render
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
import calendar
from attendance.forms import AttendanceForm
from .models import *



def attendance(request, id=None):
    instance = EmployeeAttendance()
    if id:
        instance = get_object_or_404(EmployeeAttendance, pk=id)
    else:
        instance = EmployeeAttendance()
    form = AttendanceForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('employee_attendance'))
    return render(request, 'employee/attendance_form.html', {'form': form})

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today().month

def attendance_report(request):
    context = {}
    form = AttendanceForm(request.POST)
    if get_date(request.GET.get('month', None)):
        month_data = get_date(request.GET.get('month', None))
        z=0
        range=32
        days=[]
        if z< range:
            # import pdb; pdb.set_trace()
            dats = EmployeeAttendance.objects.filter(date__month=month_data)[z].date
            days_name = dats.strftime('%A')
            dats={dats:days_name}
            dats= list(dats.keys())[0]
            z+=1
            y=dats.month
            x=dats.year
            # import pdb; pdb.set_trace()
            cal = calendar.TextCalendar(calendar.MONDAY)
            for day in cal.itermonthdays(x, y):
                # https://stackabuse.com/introduction-to-the-python-calendar-module/
                days.append(day)
                month=dats.strftime('%b')
        arg1 = set(days)
        arg1.remove(0)
        arg2 = list(arg1)
        # day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
        # day = datetime.strptime(date, '%d %m %Y').weekday()
        # arg3 = day_name[day]
        context['days']= arg2
        context['days_name']= days_name
        context['month'] = month
        context['year'] = x
        # context['prev_month'] = prev_month(y)
        # context['next_month'] = next_month(y)
        # import pdb; pdb.set_trace()
        get_all_details =EmployeeAttendance.objects.filter(date__month=month_data)
        context['get_all_details']=get_all_details  
        # import pdb; pdb.set_trace()
        return render(request, 'employee/employee_attendance.html', context)
    context={'form':form}
    return render(request, 'employee/attendance_form.html', context)

