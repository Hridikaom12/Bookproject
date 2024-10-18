# URL configuration
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.homePage, name='home'),   
    path('register/', views.userRegistration, name='register'), 
    path('login/', views.loginPage, name='login'), 
    path('logout/', views.logoutView, name='logout'),         
]







