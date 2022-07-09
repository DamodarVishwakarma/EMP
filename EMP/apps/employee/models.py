from django.db import models
from shared.models import Address
from django.db import models

class Contract(models.Model):
    name = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    title = models.CharField(max_length=50)
    firstname = models.CharField('first name', max_length=30, blank=False)
    lastname = models.CharField('last name', max_length=30, blank=True)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='employee_address')
    date_of_joining = models.DateField()
    contracts = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="contract")


    def __str__(self):
        return f"{self.title}"



