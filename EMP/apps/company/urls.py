from django.urls import path
from .views import*

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('company/add/', CompanyCreateView.as_view(), name='company_add'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('company/<int:pk>/update/', CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete')
]