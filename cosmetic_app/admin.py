from django.contrib import admin
from .models import Product,Cart
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','cat','pdetails','is_active','pimage']
    list_filter=['cat','is_active']

class CartAdmin(admin.ModelAdmin):
    list_display=['id','uid','pid']

admin.site.register(Product,ProductAdmin)
#admin.site.register(Product)
admin.site.register(Cart,CartAdmin)