from django.shortcuts import render,redirect
from django.http import HttpResponse
from login import models,views
from .models import product
from django.contrib import messages
from .forms import *

from django.contrib.auth.decorators import login_required

# Create your views here.
# manageproducts screen display ..................
@login_required(login_url='loginscreen')
def product_display(request):
    usertype = "admin"
    return render(request,'manageproducts.html',{"usertype" : usertype})

# adding products screen display.........................
def addproduct(request):
   
    usertype = 'admin'
    form = productform()
    
    return render(request,'addproducts.html',{'usertype': usertype,'form':form})

# adding new products to database......................

def additem(request):
    
    if request.method == 'POST':
        
        # cat = request.POST['p_catogary']
        # brand = request.POST['p_brand']
        # name = request.POST['p_name']
        # dis = request.POST['p_dis']
        # price = request.POST['p_price']
        # # offer = request.POST['p_offer']
        # stock = request.POST['stock']
        form = productform(request.POST, request.FILES)

        
        # new_product = product.objects.create(product_catogary=cat,product_brand=brand,product_name=name,product_dis=dis,product_price=price,product_stock=stock)
        
        if form. is_valid():
            form.save() 
        else:
            form = productform()
        
        # new_product.save();
        messages.info(request,"Product added to List")
        return redirect('addproduct')
    else:
        messages.info(request,"Not Done")
        return redirect('product')
    
# prodecut view page ddisplay.................................
@login_required(login_url='loginscreen')
def productview(request):
    
    products = product.objects.all()
    usertype = "admin"
    
    return render(request,'productview.html',{'products': products, 'usertype': usertype})
# delation page display...................

def deleteproduct(request):
    products = product.objects.all()
    usertype = "admin"
    
    return render(request,'deleteproduct.html',{'products': products, 'usertype': usertype})

# deleting Selected Product..............................
def delete_product(request):
    if request.method == 'POST':
        
        id = request.POST['submit']
        prdt = product.objects.get(product_id = id)
        prdt.delete();
        
        messages.info(request,'Product Deleted successfully')
        return redirect('deleteproduct')
        
#dashboard view................................................
@login_required(login_url='loginscreen')
def dashboard(request):
    
    items = product.objects.all()
    usertype = 'admin'
    return render(request,'index.html',{'items':items,'usertype':usertype})
        
    
# update product.......................
# Display page..
@login_required(login_url='loginscreen')
def updateproduct(request):
    
    products = product.objects.all()
    return render(request,'update_prod.html',{'products':products, 'usertype':'admin'})

# Update .........................
@login_required(login_url='loginscreen')
def update_product(request):
    global ID
    ID = request.POST['submit']
    items = product.objects.filter(product_id = ID)
    usertype = 'admin'
    return render(request,'update_product.html',{'usertype':usertype,'items':items})

def updateitem(request):
    if request.method == 'POST':
        
        updated_product = product.objects.get(product_id = ID)
        updated_product.product_catogary = request.POST['p_catogary']
        updated_product.product_brand = request.POST['p_brand']
        updated_product.product_name = request.POST['p_name']
        updated_product.product_dis = request.POST['p_dis']
        updated_product.product_price = request.POST['p_price']
        updated_product.product_stock = request.POST['stock']
        
        updated_product.save()
        messages.info(request,'Product Updated Successfully')
        return redirect('updateproduct')
    

        
    
    
        
        



        
        
        
         