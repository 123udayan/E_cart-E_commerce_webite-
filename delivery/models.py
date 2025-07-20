from django.db import models

from products.models import product

# Create your models here.
class delivery_items(models.Model):
    
    deliveryid = models.AutoField(primary_key=True)
    checkoutid = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    ordred_date = models.DateTimeField(auto_now_add=True)
    deliverd_date = models.DateTimeField(auto_now_add=True)
    
class dispatched_items(models.Model):
    
    item_id =models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=500)
    customer_phone = models.CharField(max_length=20)
    product_name = models.CharField(max_length=100)
    product_brand = models.CharField(max_length=100)
    product_dis = models.CharField(max_length=500)
    product_price = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to = 'del')
    ordred_date = models.DateTimeField(auto_now_add=True)
    dispached_date = models.DateTimeField(auto_now_add=True)
    delivery_ststus = models.CharField(max_length=100)
    
    

