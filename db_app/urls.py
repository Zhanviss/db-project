from django.urls import path
from .views import (
DiseaseList, DiseaseUpdate, DiseaseDetail, DiseaseCreate, DiseaseDelete, TemplateView, 
DiseaseTypeList, DiseaseTypeDetail, DiseaseTypeCreate, DiseaseTypeDelete, DiseaseTypeUpdate,
CountryList, CountryDetail, CountryCreate, CountryUpdate, CountryDelete,
DiscoverList, DiscoverDetail, DiscoverCreate, DiscoverDelete, DiscoverUpdate,
UsersList, UsersDetail, UsersCreate, UsersDelete, UsersUpdate,
PublicServantCreate, PublicServantDelete, PublicServantDetail, PublicServantList, PublicServantUpdate,
DoctorCreate, DoctorDelete, DoctorDetail, DoctorList, DoctorUpdate,
SpecializeCreate, SpecializeDelete, SpecializeDetail, SpecializeList, SpecializeUpdate,
RecordCreate, RecordDelete, RecordDetail, RecordList, RecordUpdate)


urlpatterns = [
	path('', TemplateView.as_view(template_name = "main.html"), name='main_page'),
	
    path('disease-codes/', DiseaseList.as_view(), name='disease_list'),
	path('disease-codes/<str:pk>/', DiseaseDetail.as_view(), name='disease_detail'),
	path('disease-codes/new', DiseaseCreate.as_view(), name='disease_new'),
	path('disease-codes/<str:pk>/delete/', DiseaseDelete.as_view(), name= 'disease_delete'),
	path('disease-codes/<str:pk>/edit/', DiseaseUpdate.as_view(), name='disease_edit'),

    path('disease-types/', DiseaseTypeList.as_view(), name='disease_type_list'),
	path('disease-types/<int:pk>/', DiseaseTypeDetail.as_view(), name='disease_type_detail'),
	path('disease-types/new', DiseaseTypeCreate.as_view(), name = 'disease_type_new'),
	path('disease-types/<int:pk>/delete/', DiseaseTypeDelete.as_view(), name= 'disease_type_delete'),
	path('disease-types/<int:pk>/edit/', DiseaseTypeUpdate.as_view(), name='disease_type_edit'),

	path('countries/', CountryList.as_view(), name='country_list'),
	path('countries/<str:pk>/', CountryDetail.as_view(), name='country_detail'),
	path('countries/new', CountryCreate.as_view(), name= 'country_new'),
	path('countries/<str:pk>/delete/', CountryDelete.as_view(), name= 'country_delete'),
	path('countries/<str:pk>/edit/', CountryUpdate.as_view(), name= 'country_edit'),
	path('discovers/', DiscoverList.as_view(), name='discover_list'),
	path('discovers/<str:pk>/', DiscoverDetail.as_view(), name = 'discover_detail'),
	path('discovers/<str:pk>/delete/', DiscoverDelete.as_view(), name = 'discover_delete'),
	path('discovers/<str:pk>/edit/', DiscoverUpdate.as_view(), name = 'discover_edit'),
	path('discovers/new', DiscoverCreate.as_view(), name='discover_new'),

	path('users/', UsersList.as_view(), name='users_list'),
	path('users/<str:pk>/', UsersDetail.as_view(), name = 'users_detail'),
	path('users/<str:pk>/delete/', UsersDelete.as_view(), name = 'users_delete'),
	path('users/<str:pk>/edit/', UsersUpdate.as_view(), name = 'users_edit'),
	path('users/new', UsersCreate.as_view(), name='users_new'),

	path('public-servants/', PublicServantList.as_view(), name='publicservant_list'),
	path('public-servants/<str:pk>/', PublicServantDetail.as_view(), name = 'publicservant_detail'),
	path('public-servants/<str:pk>/delete/', PublicServantDelete.as_view(), name = 'publicservant_delete'),
	path('public-servants/<str:pk>/edit/', PublicServantUpdate.as_view(), name = 'publicservant_edit'),
	path('public-servants/new', PublicServantCreate.as_view(), name='publicservant_new'),

	path('doctors/', DoctorList.as_view(), name='doctor_list'),
	path('doctors/<str:pk>/', DoctorDetail.as_view(), name = 'doctor_detail'),
	path('doctors/<str:pk>/delete/', DoctorDelete.as_view(), name = 'doctor_delete'),
	path('doctors/<str:pk>/edit/', DoctorUpdate.as_view(), name = 'doctor_edit'),
	path('doctors/new', DoctorCreate.as_view(), name='doctor_new'),

	path('specializes/', SpecializeList.as_view(), name='specialize_list'),
	path('specializes/<str:pk>/', SpecializeDetail.as_view(), name = 'specialize_detail'),
	path('specializes/<str:pk>/delete/', SpecializeDelete.as_view(), name = 'specialize_delete'),
	path('specializes/<str:pk>/edit/', SpecializeUpdate.as_view(), name = 'specialize_edit'),
	path('specializes/new', SpecializeCreate.as_view(), name='specialize_new'),
	
	path('records/', RecordList.as_view(), name='record_list'),
	path('records/<str:pk>/', RecordDetail.as_view(), name = 'record_detail'),
	path('records/<str:pk>/delete/', RecordDelete.as_view(), name = 'record_delete'),
	path('records/<str:pk>/edit/', RecordUpdate.as_view(), name = 'record_edit'),
	path('records/new', RecordCreate.as_view(), name='record_new'),
]


