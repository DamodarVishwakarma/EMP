import datetime
from django.views.generic.dates import MonthArchiveView
from .forms import AttendanceForm
from attendance.models import EmployeeAttendance
from django.http import Http404
from django.utils.timezone import now
from django.views.generic.dates import BaseDateListView
from django.views.generic.dates import MonthMixin, YearMixin
from calendar import HTMLCalendar
from datetime import date
from django.shortcuts import render
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
import calendar
from attendance.forms import AttendanceForm
from .models import *
# from .utils import Calendar




# class EmployeeAttendanceListView(MonthArchiveView):
#     queryset = EmployeeAttendance.objects.all()
#     date_field = "date"
#     date_list_period = 'month'
#     allow_future = False
#     template_name = 'employee/employee_attendance.html'


#     def get(self, request, *args, **kwargs):
#       self.date_list, self.object_list, extra_context = self.get_dated_items()
#       context = self.get_context_data(
#         object_list=self.object_list,
#         date_list=self.date_list,
#         **extra_context

#     )
    
#     #   import pdb; pdb.set_trace()
#       return self.render_to_response(context)


#     def get_month(self):
#         try:
#             month = super(EmployeeAttendanceListView, self).get_month()
#         except Http404:
#             month = now().strftime(self.get_month_format())

#         return month

#     def get_year(self):
#         try:
#             year = super(EmployeeAttendanceListView, self).get_year()
#         except Http404:
#             year = now().strftime(self.get_year_format())

#         return year


# class EmployeeAttendanceListView(YearMixin, MonthMixin, BaseDateListView):
#     """
#     List of objects published in a given month.
#     """
#     date_list_period = 'day'

#     def get_dated_items(self):
#         """
#         Return (date_list, items, extra_context) for this request.
#         """
#         year = self.get_year()
#         month = self.get_month()

#         date_field = self.get_date_field()
#         date = _date_from_string(year, self.get_year_format(),
#                                  month, self.get_month_format())

#         since = self._make_date_lookup_arg(date)
#         until = self._make_date_lookup_arg(self._get_next_month(date))
#         lookup_kwargs = {
#             '%s__gte' % date_field: since,
#             '%s__lt' % date_field: until,
#         }

#         qs = self.get_dated_queryset(**lookup_kwargs)
#         date_list = self.get_date_list(qs)

#         return (date_list, qs, {
#             'month': date,
#             'next_month': self.get_next_month(date),
#             'previous_month': self.get_previous_month(date),
#         })


    

# def calendar(request, month, year):
   
#     attendance = EmployeeAttendance.objects.group_by('employee_id').filter(
#       date__year=year, date__month=month
#     )
#     cal = Calendar(attendance, year, month).formatmonth(year, month)
#     return render(request,'employee/employee_attendance.html', {'calendar': mark_safe(cal)})

# class CalendarView(generic.ListView):
#     model = EmployeeAttendance
#     template_name = 'employee/employee_attendance.html'
#     allow_future = False
#     queryset = EmployeeAttendance.objects.all()


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         d = get_date(self.request.GET.get('month', None))
#         cal = Calendar(d.year, d.month)
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)
#         # import pdb; pdb.set_trace()
#         return context

# def get_date(req_month):
#     if req_month:
#         year, month = (int(x) for x in req_month.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def attendance(request, attendance_id=None):
    instance = EmployeeAttendance()
    if attendance_id:
        instance = get_object_or_404(EmployeeAttendance, pk=attendance_id)
    else:
        instance = EmployeeAttendance()
    form = AttendanceForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('employee_attendance'))
    # import pdb; pdb.set_trace()
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
        grab_data_passed = get_date(request.GET.get('month', None))
        z=0
        range=32
        days=[]
        if z< range:
            # import pdb; pdb.set_trace()
            dats = EmployeeAttendance.objects.filter(date__month=grab_data_passed)[z].date
            z+=1
            y=dats.month
            x=dats.year
            cal = calendar.TextCalendar(calendar.WEDNESDAY)
            for day in cal.itermonthdays(x, y):
                days.append(day)
                
        arg1 = set(days)
        arg1.remove(0)
        arg3 = list(arg1)
        context['days']= arg3
        # import pdb; pdb.set_trace()
        get_all_details =EmployeeAttendance.objects.filter(date__month=grab_data_passed)
        context['get_all_details']=get_all_details  
        return render(request, 'employee/employee_attendance.html', context)
    context={'form':form}
    return render(request, 'employee/attendance_form.html', context)