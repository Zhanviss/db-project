from django.contrib import admin
from .models import Diseasetype, Disease, Country, Discover, Users, Publicservant, Record, Doctor,  Specialize
# Register your models here.
admin.site.register(Country)
admin.site.register(Disease)
admin.site.register(Diseasetype)
admin.site.register(Discover)

admin.site.register(Users)
admin.site.register(Publicservant)
admin.site.register(Record)
admin.site.register(Doctor)
admin.site.register(Specialize)