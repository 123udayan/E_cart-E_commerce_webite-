from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class checkoutitem(models.Model):
    
    checkoutid = models.AutoField(primary_key=True)
    productid = models.CharField(max_length=100)
    customerid = models.CharField(max_length=100)
    customer_checkout = models.CharField(max_length=100)
    
