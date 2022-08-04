from django.contrib import admin
from employee.models import Employee, Contract

# class ContratctDetailAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         Contract.start_date: {'input_formats': ('yy-mm-dd',)},
#         Contract.end_date: {'input_formats': ('yy-mm-dd',)},

#     }

# class EmployeeDetailAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         Employee.date_of_birth: {'input_formats': ('yy-mm-dd',)},
#         Employee.date_of_joining: {'input_formats': ('yy-mm-dd',)},

#     }
 

admin.site.register(Employee)
admin.site.register(Contract)
