from django.contrib import admin
from .models import Staff


class StaffAdmin(admin.ModelAdmin):
    """
    Admin class for Staff to display
    specific fields in the admin panel
    """
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Staff, StaffAdmin)
