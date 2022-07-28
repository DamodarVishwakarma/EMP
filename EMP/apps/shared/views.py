from django.shortcuts import render
from shared.models import Address
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, ListView
# from employee.forms import EmployeeAddressForm

class AddressCreateView(CreateView):
    model = Address
    template_name = 'shared/address_add.html'
    fields = ['street_line1', 'street_line2', 'zipcode','city', 'state']
    context_object_name = 'emp_address'
    success_url = reverse_lazy('address_list')

class AddressListView(ListView):
    model = Address
   