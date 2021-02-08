from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path("",views.index,name='home'),
    path("orders/",views.orders,name='orders'),
    path("contactus",views.contactus,name='contactus'),
    path("booking",views.booking,name='booking'),
    path("offers/",views.offers,name='offers'),
    path("category/",views.category,name='category'),
    path("printreceipt/",views.printreceipt,name='printreceipt'),
    path('login',views.login,name='login'),
    path('logoutuser',views.logoutuser,name='logout'),
]