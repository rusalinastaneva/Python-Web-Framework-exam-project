from django.contrib import admin
from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'state', 'status', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('created_by',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'status', 'address', 'city', 'state', 'zipcode', 'price', 'type_of_home')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
