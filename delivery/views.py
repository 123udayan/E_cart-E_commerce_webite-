from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import user
from .models import dispatched_items,delivery_items
from products.models import product
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
# orders Views For Admin.............
@login_required(login_url='loginscreen')
def orders(request):
    
    username = request.session['username']
    users = user.objects.get(username = username)
    usertype = users.usertype
    customer = users.first_name
    
    
    item_to_dispach = dispatched_items.objects.all()
        
    return render(request,'orders.html',{'usertype':usertype,'items':item_to_dispach,'customer':customer})

# customer wise order and delivery view...............
@login_required(login_url='loginscreen')
def customer_ordered_list(request):
    
    username = request.session['username']
    users = user.objects.get(username = username)
    usertype = users.usertype
    customer = users.first_name
    phone = users.phone
    customerid = users.customerID
    
    order_item = dispatched_items.objects.filter(customer_id=customerid)
    delivery = delivery_items.objects.filter(customer_id=customerid )   
    
    return render(request,'customer_ordered_list.html',{'usertype':usertype,'order_item':order_item,'deliverd':delivery,'customer':customer })

#order and dispach controls.................
def dispach_action1(request):
    
    item_id = request.POST['accept']
    
    item_update = dispatched_items.objects.get(id = item_id)
    item_update.delivery_ststus = 'Order Accepted'
    item_update.ordred_date = item_update.ordred_date
    item_update.dispached_date = datetime.now()
    item_update.save()
    
    return redirect('orders')

def dispach_action2(request):
    
    item_id = request.POST['dispach']
    item_update = dispatched_items.objects.get(id = item_id)
    item_update.delivery_ststus = 'Item Dispached'
    item_update.ordred_date = item_update.ordred_date
    item_update.dispached_date = datetime.now()
    
    item_update.save()
    
    return redirect('orders')  

def dispach_action3(request):
    
    item_id = request.POST['outdelivery']
    item_update = dispatched_items.objects.get(id = item_id)
    item_update.delivery_ststus = 'Item Out For Delivery'
    item_update.ordred_date = item_update.ordred_date
    item_update.dispached_date = datetime.now()
    
    item_update.save()
    
    return redirect('orders')

def dispach_action4(request):
    
    item_id = request.POST['deliverd']
    item_update = dispatched_items.objects.get(id = item_id)
    item_update.delivery_ststus = 'Deliverd'
    item_update.ordred_date = item_update.ordred_date
    item_update.dispached_date = datetime.now()
    
    item_update.save()
    
    delivery_data = delivery_items.objects.create(checkoutid=item_update.id, product_name=item_update.product_name, product_brand=item_update.product_brand, customer_id=item_update.customer_id, customer_name =item_update.customer_name, ordred_date=item_update.ordred_date,deliverd_date = item_update.dispached_date)
    
    delivery_data.save()
    item_update.delete()
    
    return redirect('orders')

# view delivered items after deliver............
@login_required(login_url='loginscreen')
def alldelivery(request):
    username = request.session['username']
    users = user.objects.get(username = username)
    usertype = users.usertype
    customer = users.first_name
    
    delivery = delivery_items.objects.all()
    return render(request,'alldelivery.html',{'usertype':usertype,'delivery':delivery,'customer':customer})

# deleting order for customer.....
def delete_order(request):
    
    
    if request.method == 'POST':
        order_id = request.POST['delete_order']
        order = dispatched_items.objects.get(id = order_id)
        order.delete()
        return redirect('customer_ordered_list')

# deleting order for admin.....  
def delete_order_admin(request):

    if request.method == 'POST':
        order_id = request.POST['delete_order']
        order = dispatched_items.objects.get(id = order_id)
        order.delete()
        return redirect('orders')

@login_required(login_url='loginscreen')    
def trackorder(request):
    
    username = request.session['username']
    users = user.objects.get(username = username)
    usertype = users.usertype
    customer = users.first_name
    customerid = users.customerID
    order_item = dispatched_items.objects.filter(customer_id=customerid)
    
    context = {'usertype':usertype,'customer':customer,'order_item':order_item,}
    
    return render(request,'trackorder.html',context)
        
    
    
