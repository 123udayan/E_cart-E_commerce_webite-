from django.urls import path
from.import views

urlpatterns = [
    path('orders',views.orders,name='orders'),
    path('customer_ordered_list',views.customer_ordered_list,name= 'customer_ordered_list'),
    
    path('dispach_action1',views.dispach_action1,name = 'dispach_action1'),
    path('dispach_action2',views.dispach_action2,name = 'dispach_action2'),
    path('dispach_action3',views.dispach_action3,name = 'dispach_action3'),
    path('dispach_action4',views.dispach_action4,name = 'dispach_action4'),
    
    path('alldelivery',views.alldelivery,name='alldelivery'),
    path('delete_order',views.delete_order,name='delete_order'),
    path('delete_order_admin',views.delete_order_admin,name='delete_order_admin'),
    path('trackorder',views.trackorder,name='trackorder')
]