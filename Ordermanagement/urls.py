from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('Customers/add/', views.Customerpage, name='customer_add'),
    path('Customers/', views.AllCustomers, name='customer_list'),
    path('Customers/delete/<int:id>/', views.DeleteCustomer, name='customer_delete'),
    path('Customers/update/<int:id>/', views.UpdateCustomer, name='customer_update'),
 path('add/orders/', views.OrdersAdd ),
 path('orders/', views.Orderlist, name='order_list'),
 path('delete/orders/<int:id>/', views.OrdersDelete, name='order_delete'),
 path('update/orders/<int:id>/', views.OrdersUpdate, name='order_update'),


 ]
