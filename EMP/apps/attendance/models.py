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
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)
    date = models.DateField()
    status = models.CharField(max_length=2, choices=ATTENDANCE)
    #note= models.CharField(max_length=200)

    class Meta:
        ordering = ['id']
        unique_together = (("employee","date"),) 
    
    def __str__(self):
        return f"{self.employee}"
        
    @property
    def get_absolute_url(self):
        url = reverse('edit_attendance', args=(self.id,))
        return f'<a href="{url}"> {self.status} </a>'

