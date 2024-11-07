from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question_en', 'question_am', 'answer_en', 'answer_am')
    search_fields = ('question_en', 'question_am')
    list_filter = ('question_en',)
    list_per_page = 10

    # Optional: Customize the form layout
    fieldsets = (
        (None, {
            'fields': ('question_en', 'question_am', 'answer_en', 'answer_am')
        }),
    )
