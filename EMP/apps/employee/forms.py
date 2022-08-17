from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from shared.models import Address
from employee.models import Employee, Contract
from company.models import Company
# from attendance.models import EmployeeAttendance


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


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'contact_number', 'email']


class ContractForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['class'] = 'startDate'
        self.fields['end_date'].widget.attrs['class'] = 'endDate'
    # start_date = forms.DateField(widget=forms.TextInput(attrs={'class':'startDate'}))
    # end_date = forms.DateField(widget=forms.TextInput(attrs={'class':'endDate'}))
    
    class Meta:
        model = Contract
        fields = ['name', 'start_date', 'end_date', 'salary', 'employee']
       
        
class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street_line1', 'street_line2', 'zipcode',
                  'city', 'state', 'employee', 'company']
        exclude = ('employee', 'company')




class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = ['title', 'firstname', 'lastname', 'email',
                  'date_of_birth', 'date_of_joining']


ContractFormSet = inlineformset_factory(Employee, Contract,
                                        form=ContractForm, extra=1)
AddressFormSet = inlineformset_factory(Employee, Address,
                                       form=AddressForm, extra=1)
CompanyAddressFormSet = inlineformset_factory(Company, Address,
                                              form=AddressForm, extra=1)

# class EmployeeAttendanceForm(ModelForm):
#     class Meta:
#         model = EmployeeAttendance
#         fields = ['employee_id', 'date', 'status', 'note']