from django.contrib import admin
from .models import Service, Subservice, ChooseService, Professional, Certificate, Portfolio, MySkills, AllPros, Order, Blog, BlogDetails

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

@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Professional._meta.fields]
    search_fields = [field.name for field in Professional._meta.fields]

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Certificate._meta.fields]

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Portfolio._meta.fields]

@admin.register(MySkills)
class MySkillsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MySkills._meta.fields]

@admin.register(AllPros)
class AllProsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AllPros._meta.fields]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    search_fields = [field.name for field in Order._meta.fields]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.fields]
    search_fields = [field.name for field in Blog._meta.fields]

@admin.register(BlogDetails)
class BlogDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BlogDetails._meta.fields]    
