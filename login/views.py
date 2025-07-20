# from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import user
from products.models import product
from django.contrib.auth import models,get_user_model
from .forms import useraddform

from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, authenticate, login

from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
# from django_email_verification import send_email

from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .tokens import account_activation_token

# Create your views here.

# Rendering the home screen view......................

def home(request):
    
    return render(request,'main.html')

def register(request):
    
    form = useraddform()

    if request.method == 'POST':
        
        form = useraddform(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            if models.User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('register')
            
            elif models.User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('register')
            
            else:
                new_user1 = form.save(commit=False)
                new_user1.is_active = False
                new_user1.save()
                
                new_user = models.User.objects.get(username=username)
                username1 = new_user.username
                first_name = new_user.first_name
                last_name = new_user.last_name
                email = new_user.email
                login_id = new_user.id
                
                add_user = user.objects.create(username = username1 , first_name = first_name, last_name = last_name, email = email,login_id =login_id,usertype = 'user')
                add_user.save()
                
                current_site = get_current_site(request)
                mail_subject = 'Activate your E-Cart account.'
                message = render_to_string('emailbody.html', {'user': new_user1,
                                                                     'domain': current_site.domain,
                                                                     'uid':urlsafe_base64_encode(force_bytes(new_user1.pk)),
                                                                     'token':account_activation_token.make_token(new_user1),})

                email = EmailMessage(mail_subject, message, to=[email])
                email.send(fail_silently=True)
                
                messages.success(request,"Activation email has been sent to your Email id. Please activate your E-CART account")
                return redirect('loginscreen')
    
    return render(request,'register.html',{'form':form})

# activation Link................accepted

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def loginscreen(request):

    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('homescreen')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('loginscreen')
    else:
        return render(request,'login.html')
        
    return render(request,'login.html')


def signout(request):
    
    logout(request)
    return redirect('home')


@login_required(login_url='loginscreen')  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)  
def homescreen(request):
    username = request.session['username']
    useragent = user.objects.get(username = username)
    usertype = useragent.usertype
    items = product.objects.all()
    
    context = {"usertype":usertype,'items':items}
    
    return render(request,'index.html',context)


    
            
        