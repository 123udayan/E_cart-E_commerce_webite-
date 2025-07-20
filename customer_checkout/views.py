from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from login import models, views
from .models import checkoutitem
from products.models import product
from delivery.models import delivery_items,dispatched_items
from django.contrib.auth.decorators import login_required 


# Create your views here.
@login_required(login_url='loginscreen') 
def cartview(request):
    
    global total_payable
    item_id =[]
    username = request.session['username']
    users = models.user.objects.get(username = username)
    usertype = users.usertype
    customer = users.first_name
    userid =  users.customerID
    cart = checkoutitem.objects.all()
    items = []
    total_payable = 0
    
    
    for element in cart:
        if element.customerid == str(userid):
            item_id.append(element.productid)
            continue
        else:
            continue
        
    for i in item_id:
        customer_item = product.objects.get(product_id = i)
        items.append(customer_item)
    
    for item in items:
        total_payable = total_payable + int(item.product_price)    
   
    return render (request,'cart.html',{'usertype':usertype,'cartitem':items,'total_payable':total_payable,'customer':customer })

# cart data Adding.....
def addtocart(request):
    
    product_id = request.POST['submit']
    username = request.session['username']
    users = models.user.objects.get(username = username)
    customerid = users.customerID
    
    if request.method == 'POST':
        
        checkout = checkoutitem.objects.filter(productid = product_id,customerid = customerid).exists()
        
        if checkout is True:
            product_item = checkoutitem.objects.get(productid = product_id,customerid = customerid)
            product_item.customer_checkout = int(float(product_item.customer_checkout)) + 1            
            product_item.save()
            
            return redirect('cartview')
        
        else:
            product_item = checkoutitem.objects.create(productid = product_id,customerid = customerid,customer_checkout = 1)
            product_item.save()
            messages.info(request,'Item Added to cart')
            return redirect('cartview')
    
    else:
        messages.info(request,"item not added")
        return redirect('homescreen')
    
#checkout and payment.......................
@login_required(login_url='loginscreen')
def checkout(request):
    
    username = request.session['username']
    user = models.user.objects.get(username = username)
    usertype = user.usertype
    customer = user.first_name
    
    return render(request,'checkout.html',{'usertype':usertype,'total_payable':total_payable,'customer':customer})

#payment confirm................................
@login_required(login_url='loginscreen')
def payment(request):
    
    username = request.session['username']
    user = models.user.objects.get(username = username)
    usertype = user.usertype
    customer = user.first_name
    
    user = models.user.objects.filter(username = username)
    
    return render(request,'payment.html',{'usertype':usertype,'total_payable':total_payable,'user':user,"customer":customer})

#Payment and delivery confirmation...................

def paymentconfirmation(request):
    
    global total_payable
    item_id =[]
    username = request.session['username']
    user = models.user.objects.get(username = username)
    customer = user.first_name
    userid =  user.customerID
    cart = checkoutitem.objects.all()
    items = []
    total_payable = 0
    
    for element in cart:
        if element.customerid == str(userid):
            item_id.append(element.productid)
        
            product_for_checkout = product.objects.get(product_id = element.productid)
            
            customer_ordered = models.user.objects.get(customerID = element.customerid)
            customer_name = str(customer_ordered.first_name) + " " + str(customer_ordered.last_name)
            customer_address = customer_ordered.address_home + "," + customer_ordered.address_city + ',' + customer_ordered.address_state + ',' + customer_ordered.address_contry 
            
            
            dispach = dispatched_items.objects.create(product_name = product_for_checkout.product_name,product_brand=product_for_checkout.product_brand,product_dis=product_for_checkout.product_dis,product_price=product_for_checkout.product_price,product_img = product_for_checkout.img,customer_id = element.customerid,customer_name = customer_name,customer_address = customer_address, customer_phone = customer_ordered.phone)
            dispach.save()
            element.delete()
            
            continue
        else:
            continue
        
    for i in item_id:
        customer_item = product.objects.get(product_id = i)
        items.append(customer_item)
        customer_item.product_stock = int(customer_item.product_stock) - 1
        customer_item.save()
    
    for item in items:
        total_payable = total_payable + int(item.product_price) 
        
    user = models.user.objects.filter(username = username)
    
    return render(request,'orderconfirmation.html',{'cartitem':items,'user':user,'total_payable':total_payable,'customer':customer})

# delete cart item........................................
@login_required(login_url='loginscreen')
def delete_from_cart(request):
    
    username = request.session['username']
    user = models.user.objects.get(username = username)
    userid =  user.customerID
    productid = request.POST['submit']
    
    if request.method == 'POST':
        
        product_item = checkoutitem.objects.get(productid = productid,customerid = userid)
        product_item.delete()
        messages.info(request,'Item Deleted from cart')
        return redirect('cartview')
    else:
        
        messages.info(request,'Not Done')
        return redirect('cartview')
    
# for individual item view
@login_required(login_url='loginscreen')
def viewitem(request):
    username = request.session['username']    
    users = models.user.objects.get(username = username)
    usertype = users.usertype
    customer = users.first_name
    
    if request.method == 'POST':
        prid = request.POST['pr_id']
        selected_item = product.objects.filter(product_id = prid)
    
    
    return render(request,'viewitem.html',{'usertype':usertype,'customer':customer,'selected_item':selected_item})
    
        
        
        
    
    

    
    
    
    
