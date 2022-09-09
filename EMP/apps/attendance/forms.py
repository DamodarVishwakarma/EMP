from django.forms import ModelForm
from .models import*
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from datetime import datetime



class DateInput(forms.DateInput):
    input_type = 'date'

class AttendanceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AttendanceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = EmployeeAttendance
        fields = ['employee','date', 'status']

        widgets = {
            'date' : DateInput(),
        }

class AttendanceUpdateForm(BSModalModelForm):
    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request')
        super(AttendanceUpdateForm, self).__init__(*args, **kwargs)


    class Meta:
        model = EmployeeAttendance
        fields = ['employee','date', 'status']

        widgets = {
            'date' : DateInput(),
        }
    # def clean(self):
    #     cleaned_data = super(AttendanceUpdateForm, self).clean()
    #     date = cleaned_data.get("date")

    #     if date > datetime.today().date():
    #         raise forms.ValidationError("Attendance can't be later than today!")
    #     return cleaned_data
