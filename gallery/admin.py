from django.contrib import admin
from .models import Slide, SlideImage

class SlideImageInline(admin.TabularInline):
    model = SlideImage
    extra = 1  # Number of empty slots for images

class SlideAdmin(admin.ModelAdmin):
    inlines = [SlideImageInline]
    list_display = ('text_en', 'text_am')
    search_fields = ('text_en', 'text_am',)
    list_per_page = 10

admin.site.register(Slide, SlideAdmin)
