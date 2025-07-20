from django.db import models
from django.db.models.fields import EmailField, IntegerField

# Create your models here.
class user(models.Model):
    
    customerID = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    usertype = models.CharField(max_length=10)
    address_home = models.CharField(max_length=250)
    address_city = models.CharField(max_length=250)
    address_state = models.CharField(max_length=250)
    address_contry =models.CharField(max_length=250)
    
    
    
