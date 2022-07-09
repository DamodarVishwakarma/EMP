from django.db import models
from shared.models import Address


class Company(models.Model):
    name = models.CharField('name', max_length=30, blank=False)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='company_address')


    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "company"
        verbose_name = "Company"
        verbose_name_plural = "Companies"

   

       

        
