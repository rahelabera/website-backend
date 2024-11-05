from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('date', 'title_en', 'title_am', 'description_en', 'description_am')
    search_fields = ('title_en', 'title_am')
    list_per_page = 10