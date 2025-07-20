from django.urls import path
from.import views

urlpatterns = [
    path('customer',views.customer,name='customer'),
    path('customerview',views.customerview,name="customerview"),
    path('deletecustomer',views.deletecustomer,name='deletecustomer'),
    path('delete_customer',views.delete_customer,name='delete_customer'),
    
    path('addcustomer',views.addcustomer,name='addcustomer'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('updatecustomer',views.updatecustomer,name='updatecustomer'),
    path('update_customer',views.update_customer,name='update_customer'),
    
    path('updateuser',views.updateuser,name="updateuser"),
    path('myprofile',views.myprofile,name='myprofile'),
    path('contacts',views.contacts,name='contacts'),
    path('add_address',views.add_address,name='add_address'),
]
