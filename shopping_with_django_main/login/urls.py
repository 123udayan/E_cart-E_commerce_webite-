from django.urls import path,include
from django.conf.urls import url
from.import views
# from django_email_verification import urls as mail_urls

urlpatterns = [
    
    path("",views.home,name='home'),
    path("loginscreen",views.loginscreen,name="loginscreen"),
    path("register",views.register,name="register"),
    # path("registration",views.registration,name="registration"),
    
    # path('login',views.login,name = 'login'),
    path('logout',views.signout,name='logout'),
    path('homescreen',views.homescreen,name='homescreen'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    # path('mail/',include(mail_urls))
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),
  
]
