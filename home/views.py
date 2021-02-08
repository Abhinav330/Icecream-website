from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Booking, Contact
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout

# Create your views here.

def index(request):
    
    
    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        #check if user has entered correct credentials
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            return render(request,'index.html')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')




def booking(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        book=Booking(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        book.save()
        messages.success(request, 'your orders placed successfully')

    return render(request,'booking.html')

   

def category(request):
    
    return render(request,'category.html')

def contactus(request):
   
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Contact details sent successfully')

    return render(request,'contactus.html')

def offers(request):
    
    return render(request,'offers.html')

def orders(request):
   
    return render(request,'orders.html')

def printreceipt(request):
    
    return render(request,'printreceipt.html')


