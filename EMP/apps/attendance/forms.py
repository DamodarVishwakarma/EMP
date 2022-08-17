from django.forms import ModelForm
from .models import*
from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'

class AttendanceForm(ModelForm):

    class Meta:
        model = EmployeeAttendance
        fields = ['employee_id','date', 'status', 'note']

        widgets = {
            'date' : DateInput(),
        }
