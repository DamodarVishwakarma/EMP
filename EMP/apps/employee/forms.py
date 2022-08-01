from curses.ascii import NUL
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from shared.models import Address
from employee.models import Employee
from employee.models import Contract


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class DateInput(forms.DateInput):
    input_type = 'date'


class ContractForm(ModelForm):

    class Meta:
        model = Contract
        fields = ['name', 'start_date', 'end_date', 'salary', 'employee']
        widgets = {
            'end_date': DateInput(),
            'start_date':  DateInput(),
        }
       

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street_line1', 'street_line2', 'zipcode', 'city', 'state', 'employee']


# AddressFormSet = modelformset_factory(Address, extra=1, form=AddressForm)
# ContractFormSet = modelformset_factory(Contract,extra=1, form=ContractForm)

class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['title', 'firstname', 'lastname', 'email',
                  'date_of_birth', 'date_of_joining']
        widgets = {
            'date_of_birth': DateInput(),
            'date_of_joining':  DateInput(),
        }


ContractFormSet = inlineformset_factory(Employee, Contract,
                                            form= ContractForm, extra=1)
AddressFormSet = inlineformset_factory(Employee, Address,
                                            form= AddressForm, extra=1)
