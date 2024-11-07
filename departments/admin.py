from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'head_name_en', 'head_email')
    search_fields = ('name_en', 'head_name_en')