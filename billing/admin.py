from django.contrib import admin
from .models import Item, Bill

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_cost')
