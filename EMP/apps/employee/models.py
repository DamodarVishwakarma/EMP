from django.db import models
from django.db import models

title_choice = (
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
    ('Jr.', 'Jr.'),
    ('Sr.', 'Sr.'),
)

class Employee(models.Model):
    title = models.CharField(max_length=50, choices=title_choice)
    firstname = models.CharField('first name', max_length=30, blank=False)
    lastname = models.CharField('last name', max_length=30, blank=True)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    date_of_joining = models.DateField()

    def __str__(self):
        return f"{self.firstname}"

class Contract(models.Model):
    name = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee")

    
    def __str__(self):
        return f"{self.name}"




