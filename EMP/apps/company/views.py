from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from company.models import Company

class CompanyListView(ListView):
    model = Company
    queryset = Company.objects.all()
    template_name = 'company/company_list.html'
    context_object_name = 'comps'
    ordering = ['id']
    paginate_by = 8

    def get_context_data(self, *, object_list=queryset, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = "COMPANY LIST"
        return context_data

class CompanyCreateView(LoginRequiredMixin,CreateView):
    model = Company
    template_name = 'company/company_add.html'
    fields = ['name', 'contact_number', 'email', 'address']
    success_url = reverse_lazy('company_list')

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'
    context_object_name = 'emps'
    fields = ['name', 'contact_number', 'email', 'address']

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data()
        context_data['emps'] = Company.objects.all()
        return context_data

class CompanyUpdateView(UpdateView):
    model = Company
    pk_url_kwarg = 'pk'
    template_name = 'company/company_update.html'
    context_object_name = 'emps'
    fields = ['name', 'contact_number', 'email', 'address']
    success_url = reverse_lazy('company_list')

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')


