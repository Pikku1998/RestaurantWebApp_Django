from django.contrib import admin
from .models import Item


class MenuItems(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status', 'meal_type')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


admin.site.register(Item, MenuItems)
