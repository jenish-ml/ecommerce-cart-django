from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            if User(username=username):
                user = User.objects.create_user(username=username,email=email,password=password)
                customer = Customer(user=user,address=address,phone=phone)
                customer.save()
                return redirect('/')
        except Exception as e:
            error_message = 'Duplicate username or Invalid inputs'
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        messages.error(request,'Invalid User Credentials')
    return render(request,'account.html',context)

def signout(request):
    logout(request)
    return redirect('account')