from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    Product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    options=(
        ('Mobile Phone','Mobile Phone'),
        ('Laptop','laptop'),
        ('Tablet','tablet'),
        ('Smart Watch','Smartwatch')
    )
    category =  models.CharField(max_length=100)
    image =  models.ImageField(upload_to="product_images")
    price= models.PositiveIntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=300)
    phone = models.IntegerField()
    status = models.CharField(max_length=100,default="order placed")
