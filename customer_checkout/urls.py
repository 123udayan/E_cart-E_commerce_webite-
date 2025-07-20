from django.urls import path
from.import views

urlpatterns = [
    path('cartview',views.cartview,name='cartview'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('checkout',views.checkout,name='checkout'),
    path("payment",views.payment,name='payment'),
    
    path('paymentconfirmation',views.paymentconfirmation,name='paymentconfirmation'),
    path('delete_from_cart',views.delete_from_cart,name='delete_from_cart'),
    path('viewitem',views.viewitem,name='viewitem'),
]
