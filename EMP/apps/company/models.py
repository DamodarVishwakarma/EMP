from django.db import models


class Company(models.Model):
    name = models.CharField('name', max_length=30, blank=False)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "company"
        verbose_name = "Company"
        verbose_name_plural = "Companies"

   

       

        
