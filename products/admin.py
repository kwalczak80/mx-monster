from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """[ProductAdmin]"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'is_available',
        'image',
    )
    list_editable = ('is_available',)

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """[CategoryAdmin]"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
