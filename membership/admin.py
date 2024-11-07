from django.contrib import admin
from .models import Membership

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    list_filter = ('first_name',)
    list_per_page = 10