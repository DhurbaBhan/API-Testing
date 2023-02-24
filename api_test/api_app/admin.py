from django.contrib import admin
from .models import Products_Collection,Carts,Cart

# Register your models here.
admin.site.register(Products_Collection)
admin.site.register(Carts)
admin.site.register(Cart)