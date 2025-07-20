from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

  
class productform(forms.ModelForm):
  
    class Meta:
        model = product
        fields = '__all__'
        
        