from django.contrib import admin
from .models import Product,Cart,CoverImage,BeautyTips,Contact,Address,Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','cat','pdetails','is_active','pimage']
    list_filter=['cat','is_active']

class CartAdmin(admin.ModelAdmin):
    list_display=['id','uid','pid']

class CoverImageAdmin(admin.ModelAdmin):
    list_display=['id','image']

class TipsAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','category','date','image']

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','fname','lname','email','msg','mob']

class AddressAdmin(admin.ModelAdmin):
    list_display=['id','user','line1','city','state','postal_code','mobile']

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','order_id','uid','pid','aid','qty']
admin.site.register(Product,ProductAdmin)
#admin.site.register(Product)
admin.site.register(Cart,CartAdmin)
admin.site.register(CoverImage,CoverImageAdmin)
admin.site.register(BeautyTips,TipsAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Order,OrderAdmin)

