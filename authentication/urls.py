from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.LoginPage),
    path('logout/', views.LogoutUser),
    path('signup/', views.SignupPage),
]
