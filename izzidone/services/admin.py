from django.contrib import admin
from .models import Service, Subservice, ChooseService

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]
    search_fields = [field.name for field in Service._meta.fields]

@admin.register(Subservice)
class SubserviceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subservice._meta.fields]
    search_fields = [field.name for field in Subservice._meta.fields]

@admin.register(ChooseService)
class ChooseServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ChooseService._meta.fields]
    search_fields = [field.name for field in ChooseService._meta.fields]
