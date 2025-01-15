from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_price', 'special_quantity', 'special_price')
    search_fields = ('name',)
