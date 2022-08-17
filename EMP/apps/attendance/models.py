from django.db import models
from employee.models import Employee
from django.urls import reverse


ATTENDANCE = (
    ('A','A'),
    ('P','P'),
    ('H','H'),
    ('L','L'),
)

class EmployeeAttendance(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)
    date = models.DateField()
    status = models.CharField(max_length=2, choices=ATTENDANCE)
    note= models.TextField(max_length=100)

    objects = models.Manager()

    class Meta:
        get_latest_by = "date"
    
    def __str__(self):
        return f"{self.employee_id}"

    @property
    def get_absolute_url(self):
        url = reverse('edit_attendance', args=(self.id,))
        return f'<a href="{url}"> {self.status} </a>'

    # def date(self):
    #     return self.date.strftime('%B %d %Y')

