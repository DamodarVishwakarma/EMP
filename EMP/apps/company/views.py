from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)
from company.models import Company
from employee.forms import CompanyAddressFormSet, CompanyForm
from django.db import transaction

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

class CompanyCreateView(CreateView):
    model = Company
    template_name = 'company/company_add.html'
    fields = ['name', 'contact_number', 'email']
    success_url = reverse_lazy('company_list')

    def get_context_data(self, **kwargs):
        data = super(CompanyCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            
            data['companyaddress'] = CompanyAddressFormSet(self.request.POST)
        else:
           
            data['companyaddress'] =CompanyAddressFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        companyaddress = context['companyaddress']
        with transaction.atomic():
            self.object = form.save()

            if companyaddress.is_valid():
                companyaddress.instance = self.object
                companyaddress.save()
                
        # import pdb; pdb.set_trace()
        return super(CompanyCreateView, self).form_valid(form)


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
    form_class = CompanyForm
    success_url = reverse_lazy('company_list')

    def get_context_data(self, **kwargs):
        data = super(CompanyUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            
            data['companyaddress'] = CompanyAddressFormSet(self.request.POST)
        else:
           
            data['companyaddress'] =CompanyAddressFormSet(instance=self.object)
        return data

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        companyaddress = CompanyAddressFormSet(self.request.POST, instance=self.object)
        if companyaddress.is_valid():
            return self.form_valid(form, companyaddress)
        else:
            #import pdb; pdb.set_trace()
            return self.form_invalid(form, companyaddress)


    def form_valid(self, form, companyaddress):
        context = self.get_context_data()
        companyaddress = context['companyaddress']
        with transaction.atomic():
            self.object = form.save()

            if companyaddress.is_valid():
                companyaddress.instance = self.object
                companyaddress.save()
                
        # import pdb; pdb.set_trace()
        return super(CompanyUpdateView, self).form_valid(form)

    def form_invalid(self, form, companyaddress):
        return self.render_to_response(self.get_context_data(form=form, companyaddress=companyaddress))



class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')


