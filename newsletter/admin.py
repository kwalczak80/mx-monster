""" Admin newsleter """
from django.contrib import admin
from .models import NewsletterUser


class NewsletterAdmin(admin.ModelAdmin):
    """ Admin newsleter """
    list_display = ('email', 'date_added',)


admin.site.register(NewsletterUser, NewsletterAdmin)
