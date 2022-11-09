""" Admin reviews """
from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Admin reviews """
    list_display = (
        'product',
        'user',
        'review_date'
    )
