from django.urls import path
from .views import*

urlpatterns = [
path('address/list/', AddressListView.as_view(), name='address_list'),
path('address/add/', AddressCreateView.as_view(), name='address_add'),
]

