from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    CAT=((1,'makeup products'),(2,'hair care products'),(3,'skin care products'),(4,'appliances'),(5,'manicure pedicure'))
    name=models.CharField(max_length=50,verbose_name="Product Name")
    price=models.FloatField()
    pdetails=models.CharField(max_length=900,verbose_name="Product Details")
    cat=models.IntegerField(choices=CAT,verbose_name="Catogory")
    is_active=models.BooleanField(default=True,verbose_name="Available")
    pimage=models.ImageField(upload_to='image' , verbose_name="Product Image")
   

class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    line1 = models.TextField(verbose_name="Building and Area")
    city = models.CharField(max_length=200, verbose_name="City")
    state = models.CharField(max_length=200, verbose_name="State")
    postal_code = models.IntegerField(verbose_name="Postal Code")
    mobile=models.CharField(max_length=100,verbose_name="Mobile Number")

class Order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column="pid")
    aid = models.ForeignKey(Address, on_delete=models.CASCADE, db_column="Aid")
    qty=models.IntegerField(default=1)

class CoverImage(models.Model):
    image=models.ImageField(upload_to='image',verbose_name="image name")

class BeautyTips(models.Model):
    cat=(('Hair Care Tips','Hair Care Tips'),('Skin Care Tips','Skin Care Tips'),('Makeup Tips','Makeup Tips'))
    title=models.CharField(max_length=200,verbose_name="Title Of Tips")
    desc=models.TextField(verbose_name="Tips Description")
    category=models.CharField( max_length=200,choices=cat,verbose_name="Category")
    date=models.DateTimeField(verbose_name="Date", default=timezone.now)
    image=models.ImageField(upload_to='image',verbose_name="Image",default='image/beauty1.jpg')

class Contact(models.Model):
    fname=models.CharField(max_length=200,verbose_name="first name")
    lname=models.CharField(max_length=200,verbose_name="last name")
    email=models.CharField(max_length=200,verbose_name="Email")
    msg=models.TextField(verbose_name="message")
    mob=models.CharField(max_length=200,verbose_name="Mobile number")

