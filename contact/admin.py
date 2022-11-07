""" Admin panel for the contact app"""
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class to display email subject and message
    from the user
    """
    list_display = (
        'email',
        'subject',
        'message'
    )


admin.site.register(Contact, ContactAdmin)
