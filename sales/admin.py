from django.contrib import admin
from .models import Customers,Sale_Type,Daily_Sale 
# Register your models here.

admin.site.register(Customers)
admin.site.register(Daily_Sale)
admin.site.register(Sale_Type)
admin.site.site_header = "Sale Module"
