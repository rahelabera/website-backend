from django.contrib import admin
from .models import JobPost

class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'location_en', 'type', 'posted')
    list_filter = ('type', 'posted')
    search_fields = ('title_en', 'location_en', 'description_en')
    ordering = ('posted',)
    list_per_page = 10

    fieldsets = (
        (None, {
            'fields': ('title_en', 'title_am', 'location_en', 'location_am', 'type', 'posted', 'description_en', 'description_am', 'details_en', 'details_am')
        }),
    )

admin.site.register(JobPost, JobPostAdmin)
