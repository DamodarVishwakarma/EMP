from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from employee.forms import RegisterForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from employee.models import Employee
from django.contrib import auth
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = 'base.html'
    
    def get_context_data(self, *args, **kwargs):
        context_data= super(HomePageView, self).get_context_data(*args, **kwargs)
        return context_data


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("home")

class EmployeeListView(ListView):
    model = Employee
    queryset = Employee.objects.all()
    template_name = 'employee/employee_list.html'
    context_object_name = 'emps'
    ordering = ['id']
    paginate_by = 8

    def get_context_data(self, *, object_list=queryset, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = "EMPLOYEE LIST"
        return context_data

class EmployeeCreateView(LoginRequiredMixin,CreateView):
    model = Employee
    template_name = 'employee/employee_add.html'
    fields = ['title', 'firstname', 'lastname','email', 'date_of_birth', 'contracts','address', 'date_of_joining']
    success_url = reverse_lazy('employee_list')

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'
    context_object_name = 'emps'
    fields = ['title', 'firstname', 'lastname','email', 'date_of_birth', 'contracts','address', 'date_of_joining']

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data()
        context_data['emps'] = Employee.objects.all()
        return context_data

class EmployeeUpdateView(UpdateView):
    model = Employee
    pk_url_kwarg = 'pk'
    template_name = 'employee/employee_update.html'
    context_object_name = 'emps'
    fields = ['title', 'firstname', 'lastname','email', 'date_of_birth', 'contracts','address', 'date_of_joining']
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

