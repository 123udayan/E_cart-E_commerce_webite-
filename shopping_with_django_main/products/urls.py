from django.urls import path
from.import views


urlpatterns = [
    path("product",views.product_display,name='product'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('additem',views.additem,name='additem'),
    path('productview',views.productview,name='productview'),
    
    path('deleteproduct',views.deleteproduct,name='deleteproduct'),
    path('delete_product',views.delete_product,name='delete_product'),
    path('dashboard',views.dashboard,name= 'dashboard'),
    path('updateproduct',views.updateproduct,name='updateproduct'),
    
    path('update_product',views.update_product,name='update_product'),
    path('updateitem',views.updateitem,name='updateitem'),
    
    
]







