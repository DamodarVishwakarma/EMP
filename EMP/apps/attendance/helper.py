from datetime import datetime, timedelta, date
import calendar
from attendance.models import EmployeeAttendance
from django.http import JsonResponse
from django.template.loader import render_to_string

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today().date()

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

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'   

class Date:

    def __init__(self, obj=None):
      self.obj = obj

    def beginning_of_month(self, obj = None):
      obj = self.obj or date.today()
      return date(obj.year, obj.month, 1)

    def end_of_month(self, obj = None):
      obj = self.obj or date.today()
      return date(obj.year, obj.month, calendar.monthrange(obj.year, obj.month)[-1]) 

    def dates_range(self, start = None, end = None):
      start = self.beginning_of_month(start)
      end = self.end_of_month(end)
      delta = end - start
      days = [start + timedelta(days = i) for i in range(delta.days + 1)]
      return days

# Attendance list
def attendance_data(request):
    context = {}
    month_data = get_date(request.GET.get('month', None))
    x=month_data.month
    days = Date(month_data)
    dates = days.dates_range()
    month=month_data.strftime('%b')
    context['days']= dates
    context['month'] = month
    context['year'] = month_data.year
    context['req_month_data'] = month_data
    context['current_month'] = datetime.today().date().replace(day=1)-timedelta(days=1)
    context['prev_month'] = prev_month(month_data)
    context['next_month'] = next_month(month_data)
    value_list = EmployeeAttendance.objects.filter(date__month = x).values_list('employee', flat=True).distinct().order_by()
    group_by_value = {}
    for value in value_list:
       group_by_value[value] = EmployeeAttendance.objects.filter(employee=value)
    context['get_all_details'] = group_by_value
    return context

# attendance createview and updateview
def save_attendance_form(request, form, template_name):
    data = dict()
    month_data = get_date(request.GET.get('month', None))
    x=month_data.month
    days = Date(month_data)
    dates = days.dates_range()
    month=month_data.strftime('%b')
    data['days']= dates
    data['month'] = month
    year = month_data.year
    data['year'] = year
    data['req_month_data'] = month_data
    current_month = datetime.today().date().replace(day=1)-timedelta(days=1)
    data['current_month'] = current_month
    data['prev_month'] = prev_month(month_data)
    data['next_month'] = next_month(month_data)
    value_list = EmployeeAttendance.objects.filter(date__month = x).values_list('employee_id', flat=True).distinct().order_by()
    group_by_value = {}
    for value in value_list:
      group_by_value[value] = EmployeeAttendance.objects.filter(employee_id=value)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['html_book_list'] = render_to_string('includes/partial_attendance_list.html', {
                'get_all_details': group_by_value, 'days':dates, 'month':month, 'year':year,
                'current_month':current_month, 'prev_month':prev_month(month_data),
                'next_month':next_month(month_data)
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



