from django.db import models


class Address(models.Model):
    street_line1 = models.CharField('Address 1', max_length = 100, blank = True)
    street_line2 = models.CharField('Address 2', max_length = 100, blank = True)
    zipcode = models.CharField('ZIP code', max_length = 5, blank = True)
    city = models.CharField('City', max_length = 100, blank = True)
    state = models.CharField('State', max_length = 100, blank = True)
   
     
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

     

    def __str__(self):
        return f"{self.street_line1}"
