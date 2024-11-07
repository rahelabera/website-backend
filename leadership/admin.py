from django.contrib import admin
from .models import Committee, LeadershipMember

class LeadershipMemberInline(admin.TabularInline):
    model = LeadershipMember
    extra = 1

@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_am')
    inlines = [LeadershipMemberInline]

@admin.register(LeadershipMember)
class LeadershipMemberAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_am', 'title_en', 'title_am', 'committee')
    list_filter = ('committee',)