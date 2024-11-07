from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'role_en', 'quote_en')
    search_fields = ('name_en', 'name_am', 'role_en', 'role_am', 'quote_en', 'quote_am',)
    list_filter = ('name_en', 'name_am', 'role_en', 'role_am', 'quote_en', 'quote_am',)