from django.contrib import admin
from .models import Menu, Booking

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'menu_item_description', 'image')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Booking)