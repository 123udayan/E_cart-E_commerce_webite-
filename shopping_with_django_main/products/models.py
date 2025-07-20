from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import EmailField, IntegerField

# Create your models here.

class product(models.Model):
    
    product_id = models.AutoField(primary_key=True)
    product_catogary = models.CharField(max_length=50)
    product_brand = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_dis = models.CharField(max_length=250)
    product_price = models.IntegerField()
    product_offer = models.BooleanField(default=False)
    product_stock = models.IntegerField()
    img = models.ImageField(upload_to = 'pic')
    
