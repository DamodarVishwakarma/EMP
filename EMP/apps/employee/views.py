from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import calendar
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from shared.models import Address

from employee.forms import (AddressFormSet, ContractFormSet, EmployeeForm,
                            RegisterForm)
from employee.models import Contract, Employee
from attendance.models import EmployeeAttendance


class HomePageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super(
            HomePageView, self).get_context_data(*args, **kwargs)
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
    paginate_by = 15

    def get_context_data(self, *, object_list=queryset, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = "EMPLOYEE LIST"
        return context_data


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_add.html'
    success_url = reverse_lazy('employee_list')


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'
    context_object_name = 'emps'
    fields = ['title', 'firstname', 'lastname', 'email',
              'date_of_birth', 'contracts', 'address', 'date_of_joining']

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data()
        context_data['emps'] = Employee.objects.all()
        return context_data


class EmployeeUpdateView(UpdateView):
    model = Employee
    pk_url_kwarg = 'pk'
    form_class = EmployeeForm
    template_name = 'employee/employee_update.html'
    context_object_name = 'emps'
    success_url = reverse_lazy('employee_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')


class DashboardView(TemplateView):
    template_name = 'registration/dashboard.html'


class AddressContractEmployeeCreate(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_list')
    context_object_name = 'emps'
    template_name = 'employee/employee_add.html'

    def get_context_data(self, **kwargs):
        data = super(AddressContractEmployeeCreate,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['contractemployee'] = ContractFormSet(self.request.POST)
            data['addressemployee'] = AddressFormSet(self.request.POST)
        else:
            data['contractemployee'] = ContractFormSet()
            data['addressemployee'] = AddressFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        contractemployee = context['contractemployee']
        addressemployee = context['addressemployee']
        with transaction.atomic():
            self.object = form.save()

            if contractemployee.is_valid() and addressemployee.is_valid():
                contractemployee.instance = self.object
                addressemployee.instance = self.object
                contractemployee.save()
                addressemployee.save()
        # import pdb; pdb.set_trace()
        return super(AddressContractEmployeeCreate, self).form_valid(form)


class AddressContractEmployeeUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_list')
    template_name = 'employee/employee_update.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        contractemployee = ContractFormSet(
            self.request.POST, instance=self.object)
        addressemployee = AddressFormSet(
            self.request.POST, instance=self.object)
        if (form.is_valid() and addressemployee.is_valid() and contractemployee.is_valid()):
            return self.form_valid(form, contractemployee, addressemployee)
        else:
            return self.form_invalid(form, contractemployee, addressemployee)

    def get_context_data(self, **kwargs):
        data = super(AddressContractEmployeeUpdate,
                     self).get_context_data(**kwargs)
        if self.request.POST:
            data['contractemployee'] = ContractFormSet(
                self.request.POST, instance=self.object)
            data['addressemployee'] = AddressFormSet(
                self.request.POST, instance=self.object)
        else:
            data['contractemployee'] = ContractFormSet(instance=self.object)
            data['addressemployee'] = AddressFormSet(instance=self.object)
            # import pdb; pdb.set_trace()
            return data

    def form_valid(self, form, contractemployee, addressemployee):
        self.object = form.save()
        contractemployee.instance = self.object
        contractemployee.save()
        addressemployee.instance = self.object
        addressemployee.save()
        # print('form is valid')
        return HttpResponseRedirect(self.get_success_url())

        # return super(AddressContractEmployeeCreate, self).form_valid(form)

    def form_invalid(self, form, contractemployee, addressemployee):
        return self.render_to_response(self.get_context_data(form=form, contractemployee=contractemployee, addressemployee=addressemployee))

# Contract Views-


class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contract/contract_add.html'
    fields = ['name', 'start_date', 'end_date', 'salary']
    success_url = reverse_lazy('employee_add')

