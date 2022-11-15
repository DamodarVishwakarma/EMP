from attendance.models import EmployeeAttendance
from django.shortcuts import render
from django.shortcuts import render
from attendance.forms import AttendanceUpdateForm
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView
from attendance.helper import attendance_data, save_attendance_form
from django.shortcuts import render, get_object_or_404

   
class EmployeeAttendanceListView(ListView):
    template_name = 'attendance/employee_attendance.html'

    def get(self, request):
        context = attendance_data(request)
        # import pdb; pdb.set_trace()
        return render(request, self.template_name, context)

        
def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceUpdateForm(request.POST)
    else:
        form = AttendanceUpdateForm()
    return save_attendance_form(request, form, 'attendance/attendance_create_form.html')


def attendance_update(request, pk):
    book = get_object_or_404(EmployeeAttendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceUpdateForm(request.POST, instance=book)
    else:
        form = AttendanceUpdateForm(instance=book)
    return save_attendance_form(request, form, 'attendance/attendance_update_form.html')


#class EmployeeAttendanceCreateView(CreateView):
#     model = EmployeeAttendance
#     form_class = AttendanceUpdateForm
#     template_name = 'attendance/attendance_create_form.html'
#     success_url = reverse_lazy('employee_attendance')

#     def get(self, request):
#         if request.method == 'POST':
#            form = AttendanceUpdateForm(request.POST)
#         else:
#            form = AttendanceUpdateForm()
#         return save_attendance_form(request, form, self.template_name)
 
# class EmployeeAttendanceUpdateView(UpdateView):
#     model = EmployeeAttendance
#     pk_url_kwarg = 'pk'
#     form_class = AttendanceUpdateForm
#     template_name = 'attendance/attendance_update_form.html'
#     success_url = reverse_lazy('employee_attendance')

#     def get(self,request, **kwargs):
#         employee_attendance = EmployeeAttendance.objects.get(pk=kwargs.get('pk'))
#         if self.request.method == 'POST':
#            form = AttendanceUpdateForm(self.request.POST, instance=employee_attendance)
#         else:
#            form = AttendanceUpdateForm(instance=employee_attendance)
#         return save_attendance_form(request, form, self.template_name)
