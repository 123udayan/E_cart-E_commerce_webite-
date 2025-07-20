from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from login.models import user
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models

# Create your views here.
@login_required(login_url='loginscreen')
def customer(request):
    
    username = request.session['username']
    user1  = user.objects.get(username = username)
    usertype = user1.usertype
    customer = user1.first_name

    return render(request,'managecustomer.html',{'usertype':usertype,'customer':customer})

# customer List View.....................
@login_required(login_url='loginscreen')
def customerview(request):
    
    username = request.session['username']
    user1  = user.objects.get(username = username)
    usertype = user1.usertype
    customer = user1.first_name
    
    users = user.objects.all()
    return render(request,'customerview.html',{"users":users,'usertype':usertype,'customer':customer})

# delete Page Render..............................
@login_required(login_url='loginscreen')
def deletecustomer(request):
    
    username = request.session['username']
    user1 = user.objects.get(username = username)
    usertype = user1.usertype
    customer = user1.first_name
    
    users = user.objects.all()
    return render(request,'deletecustomer.html',{'usertype': usertype,"users":users,'customer':customer})


def delete_customer(request):
    
    cus_id = request.POST['submit']
    user1 = user.objects.get(customerID=cus_id)
    login_id = user1.login_id
    user1.delete()
    
    user1 = models.User.objects.get(id = login_id)
    user1.delete()
    
    messages.info(request,'User was Deleted Successfully')
    return redirect('deletecustomer')

#Add customer Screen Rendering....................
@login_required(login_url='loginscreen')
def addcustomer(request):
    
    username = request.session['username']
    user1 = user.objects.get(username = username)
    usertype = user1.usertype
    customer = user1.first_name
    
    return render(request,'addcustomer.html',{'usertype':usertype,'customer':customer})

#performe adding user....................

def add_customer(request):    
    
    if request.method == 'POST':
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        uname = request.POST['uname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2 and password1 !="":
            
            if user.objects.filter(username = uname).exists():   
                messages.info(request,'Username Already Taken')
                return redirect('addcustomer')
            
            elif user.objects.filter(email = email).exists():
                messages.info(request,'Email Already Taken')
                return redirect('addcustomer')
            
            else:
                users = user.objects.create(first_name = fname, last_name = lname, phone = phone, email = email, username = uname, password = password1, usertype = "user" )
                
                users.save();
                messages.info(request,'User Created')
                return redirect('addcustomer')
        else:
            messages.info(request,'User name Not Matching')
            return redirect('addcustomer')
    else:
        
        return redirect('addcustomer')
    
# Updating customer Screen................
@login_required(login_url='loginscreen')
def updatecustomer(request):
    
    users = user.objects.all()
    
    return render(request,'updatecustomer.html',{'usertype':'admin','users':users,})

@login_required(login_url='loginscreen')
def update_customer(request):
    global customerid
    
    username = request.session['username']
    users = user.objects.get(username = username)
    usertype = users.usertype
    customer = users.first_name
    customerid = request.POST['submit']
    users = user.objects.filter(customerID = customerid)
     
    return render(request,'update_customer.html',{'usertype':usertype,'users':users,'customer':customer})
    

def updateuser(request):
    
    upadate_user = user.objects.get(customerID = customerid)
    
    upadate_user.first_name = request.POST['f_name']
    upadate_user.last_name = request.POST['l_name']
    upadate_user.phone = request.POST['phone']
    upadate_user.email = request.POST['email']
    upadate_user.username = request.POST['u_name']
    upadate_user.usertype = request.POST['u_type']
    
    upadate_user.save()
    messages.info(request,'User Updated Successfully')
    return redirect('updatecustomer')

# Customer Profile View.....................................
@login_required(login_url='loginscreen')
def myprofile(request):
    
    username = request.session['username']
    users = user.objects.get(username = username)
    usertype = users.usertype
    customer = users.first_name
    
    
    users = user.objects.filter(username = username)
    
    return render(request,'myprofile.html',{'usertype':usertype,'user':users,'customer':customer})

def contacts(request):
    username = request.session['username']
    users = user.objects.get(username = username)
    usertype = users.usertype
    
    return render(request,'contact.html',{'usertype':usertype})

# address adding................................

def add_address(request):
    
    username = request.session['username']
    update_user = user.objects.get(username = username)
    
    if request.method == 'POST':
        
        update_user.address_home = request.POST['house']
        update_user.address_city = request.POST['city']
        update_user.address_state = request.POST['state']
        update_user.address_contry = request.POST['contry']
        update_user.phone = request.POST['phone']
        update_user.email = request.POST['email']
    
        update_user.save()
        messages.info(request,'Address Updated')
        return redirect('myprofile')
    else:
        
        messages.info(request,'Not Done')
        return redirect('myprofile')
        
        
    
    
    
    
    