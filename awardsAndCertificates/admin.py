from django.contrib import admin
from .models import Award, Certificate

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_am', 'date_received', 'awarding_body_en', 'awarding_body_am', 'description_en', 'description_am')
    search_fields = ('name_en', 'name_am', 'awarding_body_en', 'awarding_body_am', 'description_en', 'description_am')
    list_filter = ('date_received',)
    list_per_page = 10

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_am', 'date_issued', 'issuing_organization_en', 'issuing_organization_am', 'description_en', 'description_am')
    search_fields = ('name_en', 'name_am', 'issuing_organization_en', 'issuing_organization_am', 'description_en', 'description_am')
    list_filter = ('date_issued',)
    list_per_page = 10