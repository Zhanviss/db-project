from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Disease, Diseasetype, Country, Discover, Users, Publicservant, Doctor, Specialize, Record
from django.urls import reverse_lazy
# Create your views here.

class DiseaseList(ListView):
    model = Disease
    context_object_name = 'disease'
    template_name: str = 'diseases/disease_list.html'
class DiseaseDetail(DetailView):
    model = Disease
    template_name = 'diseases/disease_detail.html'
    context_object_name = 'disease'
class DiseaseCreate(CreateView):
    model = Disease
    template_name = 'diseases/disease_new.html'
    context_object_name = 'disease'
    fields = ['disease_code', 'description', 'pathogen', 'dtid',]
    success_url = reverse_lazy('disease_list')
class DiseaseDelete(DeleteView):
    model = Disease
    template_name = 'diseases/disease_delete.html'
    context_object_name = 'disease'
    success_url = reverse_lazy('disease_list')
class DiseaseUpdate(UpdateView):
    model = Disease
    template_name = 'diseases/disease_edit.html'
    context_object_name = 'disease'
    fields = ['description', 'pathogen', 'dtid',]
    success_url = reverse_lazy('disease_list')
class DiseaseTypeList(ListView):
    model = Diseasetype
    template_name = 'diseases/disease_type_list.html'
    context_object_name = 'disease_type'
    ordering = ['-did']
class DiseaseTypeDetail(DetailView):
    model = Diseasetype
    template_name = 'diseases/disease_type_detail.html'
    context_object_name = 'disease_type'
class DiseaseTypeCreate(CreateView):
    model = Diseasetype
    template_name = 'diseases/disease_type_new.html'
    context_object_name = 'disease_type'
    fields = ['description',]
    success_url = reverse_lazy('disease_type_list')
class DiseaseTypeDelete(DeleteView):
    model = Diseasetype
    template_name = 'diseases/disease_type_delete.html'
    context_object_name = 'disease_type'
    success_url = reverse_lazy('disease_type_list')
class DiseaseTypeUpdate(UpdateView):
    model = Diseasetype
    template_name = 'diseases/disease_type_edit.html'
    context_object_name = 'disease_type'
    fields = ['description',]
    success_url = reverse_lazy('disease_type_list')
class CountryList(ListView):
    model = Country
    context_object_name = 'country'
    template_name = 'countries/country_list.html'
class CountryDetail(DetailView):
    model = Country
    context_object_name = 'country'
    template_name = 'countries/country_detail.html'   
class CountryUpdate(UpdateView):
    model = Country
    template_name = 'countries/country_edit.html'
    context_object_name = 'country'
    fields = ['population',]
    success_url = reverse_lazy('country_list')
class CountryCreate(CreateView):
    model = Country
    template_name = 'countries/country_new.html'
    context_object_name = 'country'
    fields = ['cname', 'population',]
    success_url = reverse_lazy('country_list')
class CountryDelete(DeleteView):
    model = Country
    template_name = 'countries/country_delete.html'
    context_object_name = 'country'
    success_url = reverse_lazy('country_list')
class DiscoverList(ListView):
    model = Discover
    template_name = 'discovers/discover_list.html'
    context_object_name = 'discover'
class DiscoverDetail(DetailView):
    model = Discover
    template_name = 'discovers/discover_detail.html'
    context_object_name = 'discover'
class DiscoverCreate(CreateView):
    model = Discover 
    template_name = 'discovers/discover_new.html'
    context_object_name = 'discover'
    fields = [ 'cname', 'disease_code','first_enc_date',]
    success_url = reverse_lazy('discover_list')
class DiscoverUpdate(UpdateView):
    model = Discover
    template_name = 'discovers/discover_edit.html'
    context_object_name = 'discover'
    fields = ['first_enc_date',]
    success_url = reverse_lazy('discover_list')
class DiscoverDelete(DeleteView):
    model = Discover
    template_name = 'discovers/discover_delete.html'
    success_url = reverse_lazy('discover_list')
class UsersList(ListView):
    model = Users
    template_name = 'stuff/users_list.html'
    context_object_name = 'users'
class UsersDetail(DetailView):
    model = Users
    template_name = 'stuff/users_detail.html'
    context_object_name = 'users'
class UsersCreate(CreateView):
    model = Users 
    template_name = 'stuff/users_new.html'
    context_object_name = 'users'
    fields = ['email', 'name', 'surname', 'salary', 'phone', 'cname',]
    success_url = reverse_lazy('users_list')
class UsersUpdate(UpdateView):
    model = Users
    template_name = 'stuff/users_edit.html'
    context_object_name = 'users'
    fields = ['name', 'surname', 'salary', 'phone', 'cname',]
    success_url = reverse_lazy('users_list')
class UsersDelete(DeleteView):
    model = Users
    template_name = 'stuff/users_delete.html'
    success_url = reverse_lazy('users_list')
class PublicServantList(ListView):
    model = Publicservant
    template_name = 'stuff/publicservants_list.html'
    context_object_name = 'publicservant'
class PublicServantDetail(DetailView):
    model = Publicservant
    template_name = 'stuff/publicservants_detail.html'
    context_object_name = 'publicservant'
class PublicServantCreate(CreateView):
    model = Publicservant
    template_name = 'stuff/publicservants_new.html'
    context_object_name = 'publicservant'
    fields = ['email', 'department',]
    success_url = reverse_lazy('publicservant_list')
class PublicServantUpdate(UpdateView):
    model = Publicservant
    template_name = 'stuff/publicservants_edit.html'
    context_object_name = 'publicservant'
    fields = ['department',]
    success_url = reverse_lazy('publicservant_list')
class PublicServantDelete(DeleteView):
    model = Publicservant
    template_name = 'stuff/publicservants_delete.html'
    success_url = reverse_lazy('publicservant_list')
class DoctorList(ListView):
    model = Doctor
    template_name = 'stuff/doctor_list.html'
    context_object_name = 'doctor'
class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'stuff/doctor_detail.html'
    context_object_name = 'doctor'
class DoctorCreate(CreateView):
    model = Doctor
    template_name = 'stuff/doctor_new.html'
    context_object_name = 'doctor'
    fields = ['email', 'degree',]
    success_url = reverse_lazy('doctor_list')
class DoctorUpdate(UpdateView):
    model = Doctor
    template_name = 'stuff/doctor_edit.html'
    context_object_name = 'doctor'
    fields = ['degree',]
    success_url = reverse_lazy('doctor_list')
class DoctorDelete(DeleteView):
    model = Doctor
    template_name = 'stuff/doctor_delete.html'
    success_url = reverse_lazy('doctor_list')
class SpecializeList(ListView):
    model = Specialize
    template_name = 'specialize_list.html'
    context_object_name = 'specialize'
class SpecializeDetail(DetailView):
    model = Specialize
    template_name = 'specialize_detail.html'
    context_object_name = 'specialize'
class SpecializeCreate(CreateView):
    model = Specialize
    template_name = 'specialize_new.html'
    context_object_name = 'specialize'
    fields = ['sid', 'email',]
    success_url = reverse_lazy('specialize_list')
class SpecializeUpdate(UpdateView):
    model = Specialize
    template_name = 'specialize_edit.html'
    context_object_name = 'specialize'
    fields = ['sid',]
    success_url = reverse_lazy('specialize_list')
class SpecializeDelete(DeleteView):
    model = Specialize
    template_name = 'specialize_delete.html'
    success_url = reverse_lazy('specialize_list')

class RecordList(ListView):
    model = Record
    template_name = 'records/record_list.html'
    context_object_name = 'record'
class RecordDetail(DetailView):
    model = Record
    template_name = 'records/record_detail.html'
    context_object_name = 'record'
class RecordCreate(CreateView):
    model = Record
    template_name = 'records/record_new.html'
    context_object_name = 'record'
    fields = ['email', 'cname', 'disease_code',  'total_deaths', 'total_patients',]
    success_url = reverse_lazy('record_list')
class RecordUpdate(UpdateView):
    model = Record
    template_name = 'records/record_edit.html'
    context_object_name = 'record'
    fields = ['total_deaths', 'total_patients',]
    success_url = reverse_lazy('record_list')
class RecordDelete(DeleteView):
    model = Record
    template_name = 'records/record_delete.html'
    success_url = reverse_lazy('record_list')
