import datetime
import json
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
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
import calendar
from attendance.forms import AttendanceForm
from .models import *
from django.views.generic import CreateView, UpdateView


class EmployeeAttendanceCreateView(CreateView):
    model = EmployeeAttendance
    form_class = AttendanceForm
    template_name = 'employee/attendance_form.html'
    success_url = reverse_lazy('employee_attendance')

class EmployeeAttendanceUpdateView(UpdateView):
    model = EmployeeAttendance
    pk_url_kwarg = 'pk'
    form_class = AttendanceForm
    template_name = 'employee/attendance_form.html'
    context_object_name = 'emps_attendance'
    success_url = reverse_lazy('employee_attendance')

    # def post(self,request, *args, **kwargs):
    #     # import pdb; pdb.set_trace()
    #     employee_attandance = get_object_or_404(EmployeeAttendance, pk=kwargs.get('pk'))
       
    #     if request.method == 'POST':
    #         form = AttendanceForm(request.POST, instance=employee_attandance)
    #     else:
    #         form = AttendanceForm(instance=employee_attandance)
          
    #         return self.save_attendance_form(request, form, 'employee/attendance_form.html')

    # def  post(self,request, *args, **kwargs):
    #     data =  dict()
    #     employee_attend = EmployeeAttendance.objects.get(pk=kwargs.get('pk'))
    #     form = AttendanceForm(instance=employee_attend, data=request.POST)
    #     if form.is_valid():
    #         employee_attend = form.save()
    #         data['employee_attend'] = employee_attend
    #     else:
    #         form = AttendanceForm(instance=employee_attend)
    #         data['employee_attend'] = form
    #     # import pdb; pdb.set_trace()
    #     return HttpResponse(json.dumps(data),content_type="application/json")

    # def save_attendance_form(request, form, template_name):
    #     data = dict()
    #     if request.method == 'POST':
    #      if form.is_valid():
    #         form.save()
    #         data['form_is_valid'] = True
    #         employees = EmployeeAttendance.objects.all()
    #         data['attendance_list'] = render_to_string('employee/attendance_form.html', {
    #             'employees': employees
    #         })
    #      else:
    #         data['form_is_valid'] = False
    #     context = {'form': form}
    #     data['html_form'] = render_to_string(template_name, context, request=request)
    #     return JsonResponse(data)

    


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
        # range=32
        days=[]
        if z>=0:
            dats = EmployeeAttendance.objects.filter(date__month=month_data)[z].date
            days_name = dats.strftime('%A')
            dats={dats:days_name}
            dats= list(dats.keys())[0]
            z+=1
            y=dats.month
            x=dats.year
            cal = calendar.HTMLCalendar(calendar.MONDAY)
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
        # context['prev_month'] = prev_month(month_data)
        # context['next_month'] = next_month(month_data)
        # import pdb; pdb.set_trace()
        get_all_details =EmployeeAttendance.objects.filter(date__month=month_data)
        context['get_all_details']=get_all_details  
        return render(request, 'employee/employee_attendance.html', context)
    context={'form':form}
    return render(request, 'employee/attendance_form.html', context)

def prev_month(month_data):
    first = month_data.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(month_data):
    days_in_month = calendar.monthrange(month_data.year, month_data.month)[1]
    last = month_data.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

