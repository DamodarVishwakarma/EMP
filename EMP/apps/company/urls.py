from django.urls import path
from .views import*

urlpatterns = [
    path('list/', CompanyListView.as_view(), name='company_list'),
    path('add/', CompanyCreateView.as_view(), name='company_add'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('<int:pk>/update/', CompanyUpdateView.as_view(), name='company_update'),
    path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete')
]