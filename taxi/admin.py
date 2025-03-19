from django.contrib import admin
from .models import Client, Driver, Order

admin.site.register(Client)
admin.site.register(Driver)
admin.site.register(Order)