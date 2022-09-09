from attendance.models import EmployeeAttendance
from django.shortcuts import render
from datetime import datetime, timedelta, date
from django.shortcuts import render
from attendance.forms import AttendanceUpdateForm
from .models import *
from bootstrap_modal_forms.generic import BSModalUpdateView, BSModalCreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from attendance.helper import get_date, next_month, prev_month, is_ajax ,Date
from django.http import JsonResponse
from django.template.loader import render_to_string



class EmployeeAttendanceCreateView(BSModalCreateView):
    model = EmployeeAttendance
    form_class = AttendanceUpdateForm
    template_name = 'employee/attendance_form.html'
    success_url = reverse_lazy('employee_attendance')

    def post(self, request):
        posts = EmployeeAttendance.objects.all()
        response_data = {}

        if request.POST.get('action') == 'post':
            employee = request.POST.get('employee')
            date = request.POST.get('date')
            status = request.POST.get('status')

            response_data['employee'] = employee
            response_data['date'] = date
            response_data['status'] = status

            EmployeeAttendance.objects.create(
                employee = employee,
                date = date,
                status = status
                )
            return JsonResponse(response_data)

        return render(request, 'employee/attendance_form.html', {'posts':posts})    

    
   
class EmployeeAttendanceListView(ListView):
    model = EmployeeAttendance
    template_name = 'employee/employee_attendance.html'

    def get(self, request, *args, **kwargs):
        context = {}
        month_data = get_date(request.GET.get('month', None))
        days = Date(month_data)
        start = days.beginning_of_month()
        end = days.end_of_month()
        dates = days.dates_range()
        month=month_data.strftime('%b')
        context['days']= dates
        context['month'] = month
        context['year'] = month_data.year
        context['req_month_data'] = month_data
        context['current_month'] = datetime.today().date().replace(day=1)-timedelta(days=1)
        context['prev_month'] = prev_month(month_data)
        context['next_month'] = next_month(month_data)
        get_all_details = EmployeeAttendance.objects.filter(date__range = (start, end))
        # import pdb; pdb.set_trace()
        context['get_all_details'] = get_all_details
        if is_ajax(request=request) and self.request.method == 'POST':
            context['table'] = render_to_string('employee/attendance_form.html', {'get_all_details':get_all_details}, request=request)
            return JsonResponse(context)
        return render(request,'employee/employee_attendance.html', context)
        

class EmployeeAttendanceUpdateView(BSModalUpdateView):
    model = EmployeeAttendance
    pk_url_kwarg = 'pk'
    form_class = AttendanceUpdateForm
    template_name = 'employee/attendance_update_form.html'
    context_object_name = 'emps_attendance'
    success_url = reverse_lazy('employee_attendance')




