from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('',  HomePageView.as_view(), name='home'),
    path('register/', register, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', logout, name='logout'),
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employee/add/', AddressContractEmployeeCreate.as_view(), name='employee_add'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/update/<int:pk>/', AddressContractEmployeeUpdate.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #contract pattern
    path('address/add/', ContractCreateView.as_view(), name='contract_add'),
]
