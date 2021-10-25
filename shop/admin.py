from django.contrib import admin
from .models import Customer, PartType, Part, Cart, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(PartType)
admin.site.register(Part)
admin.site.register(Cart)
admin.site.register(Order)
