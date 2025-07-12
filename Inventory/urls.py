from django.urls import path
from . import views
from .views import *
urlpatterns = [
    #path('Product/add/', views.Productpage),
   #path('Products/', views.AllProducts),
    #path('Products/delete/<int:id>/', views.DeleteProducts,name='product_delete'),
    #path('Products/update/<int:id>/', views.UpdateProducts,name='product_update'),
    path('Product/add/', ProductsAddView.as_view()),
    path('Products/', ProductsListView.as_view(), name='all_products'),
    path('Products/delete/<int:id>/', ProductsDeleteView.as_view(), name='product_delete'),
    path('Products/update/<int:id>/', ProductsUpdateView.as_view(), name='product_update'),
]


