from django.contrib import admin

# Register your models here.
from homeplace.team.models import TeamMembers


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10


admin.site.register(TeamMembers, TeamAdmin)
