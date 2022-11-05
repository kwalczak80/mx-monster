from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    """
    Admin class for Frequently Asked Questions section
    """
    list_display = ('question', 'answer')


admin.site.register(Faq, FaqAdmin)
