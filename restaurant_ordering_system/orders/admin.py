from django.contrib import admin
from .models import Order, Customer, Menu, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Menu)

# Register your models here.
